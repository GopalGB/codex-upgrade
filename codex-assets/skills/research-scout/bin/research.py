#!/usr/bin/env python3
"""research.py - keyless academic/web research from free APIs (stdlib only, no MCP).

Zero pip dependencies - uses only urllib/json/xml from the standard library, so it
runs even when the office blocks package installs. All sources are keyless.

Sources:
  arxiv     export.arxiv.org           preprints (CS/physics/math/stat/econ/bio)
  openalex  api.openalex.org           240M+ works, very generous rate limit
  crossref  api.crossref.org           150M+ DOIs (journals, books, proceedings)
  scholar   api.semanticscholar.org    Semantic Scholar (rate-limited unauthenticated)

Subcommands:
  search QUERY [--source S] [--n 10] [--since YEAR] [--json]
  doi    DOI                           resolve a single DOI via Crossref

Examples:
  python research.py search "retrieval augmented generation" --source arxiv --n 8
  python research.py search "garment cost optimization" --source openalex --since 2022
  python research.py doi 10.1145/3576915.3623064
"""

from __future__ import annotations

import argparse
import json
import sys
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# Set CODEX_RESEARCH_MAILTO to join the Crossref/OpenAlex "polite pool" (~10x faster).
MAILTO = os.environ.get("CODEX_RESEARCH_MAILTO", "")
UA = f"codex-research-scout/1.0 ({'mailto:' + MAILTO if MAILTO else 'no-mailto'})"


def _get(
    url: str,
    accept: str = "application/json",
    timeout: int = 30,
    headers: dict | None = None,
    retries: int = 3,
) -> bytes:
    """GET with backoff on 429/5xx (the Semantic Scholar pool is shared + bursty)."""
    h = {"User-Agent": UA, "Accept": accept}
    if headers:
        h.update(headers)
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(2 * (attempt + 1))  # 2s, 4s backoff (deterministic)
                continue
            raise
    raise last  # pragma: no cover


def _trim(text: str, n: int = 280) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= n else text[: n - 1] + "…"


def arxiv(query: str, n: int, since: int | None):
    q = urllib.parse.quote(f"all:{query}")
    url = (
        f"http://export.arxiv.org/api/query?search_query={q}"
        f"&start=0&max_results={n}&sortBy=submittedDate&sortOrder=descending"
    )
    root = ET.fromstring(_get(url, accept="application/atom+xml"))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for e in root.findall("a:entry", ns):
        published = (e.findtext("a:published", default="", namespaces=ns) or "")[:10]
        year = int(published[:4]) if published[:4].isdigit() else None
        if since and year and year < since:
            continue
        out.append(
            {
                "title": _trim(e.findtext("a:title", default="", namespaces=ns), 200),
                "authors": [
                    a.findtext("a:name", default="", namespaces=ns)
                    for a in e.findall("a:author", ns)
                ][:6],
                "year": year,
                "venue": "arXiv",
                "url": e.findtext("a:id", default="", namespaces=ns),
                "abstract": _trim(e.findtext("a:summary", default="", namespaces=ns)),
            }
        )
    return out


def openalex(query: str, n: int, since: int | None):
    # NOTE: since 2026-02-13 OpenAlex is key-gated; keyless = demo-only. Set
    # OPENALEX_API_KEY for real use and CODEX_RESEARCH_MAILTO for the polite pool.
    params = {"search": query, "per-page": n, "sort": "relevance_score:desc"}
    if since:
        params["filter"] = f"from_publication_date:{since}-01-01"
    if MAILTO:
        params["mailto"] = MAILTO
    if os.environ.get("OPENALEX_API_KEY"):
        params["api_key"] = os.environ["OPENALEX_API_KEY"]
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = json.loads(_get(url))
    out = []
    for w in data.get("results", []):
        out.append(
            {
                "title": _trim(w.get("title") or "", 200),
                "authors": [
                    a["author"]["display_name"] for a in w.get("authorships", [])
                ][:6],
                "year": w.get("publication_year"),
                "venue": (w.get("primary_location") or {})
                .get("source", {})
                .get("display_name")
                if w.get("primary_location")
                else None,
                "url": w.get("doi") or w.get("id"),
                "abstract": _trim(
                    _reconstruct_abstract(w.get("abstract_inverted_index"))
                ),
            }
        )
    return out


def _reconstruct_abstract(inv):
    if not inv:
        return ""
    positions = []
    for word, idxs in inv.items():
        for i in idxs:
            positions.append((i, word))
    return " ".join(w for _, w in sorted(positions))


def crossref(query: str, n: int, since: int | None):
    params = {
        "query": query,
        "rows": n,
        "select": "title,author,issued,DOI,container-title,abstract",
    }
    if since:
        params["filter"] = f"from-pub-date:{since}-01-01"
    if MAILTO:
        params["mailto"] = MAILTO  # Crossref polite pool
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = json.loads(_get(url))
    out = []
    for it in data.get("message", {}).get("items", []):
        parts = (it.get("issued", {}).get("date-parts") or [[None]])[0]
        out.append(
            {
                "title": _trim((it.get("title") or [""])[0], 200),
                "authors": [
                    f"{a.get('given', '')} {a.get('family', '')}".strip()
                    for a in it.get("author", [])
                ][:6],
                "year": parts[0] if parts else None,
                "venue": (it.get("container-title") or [None])[0],
                "url": "https://doi.org/" + it["DOI"] if it.get("DOI") else None,
                "abstract": _trim(_strip_jats(it.get("abstract", ""))),
            }
        )
    return out


def _strip_jats(text: str) -> str:
    import re

    return re.sub(r"<[^>]+>", "", text or "")


def scholar(query: str, n: int, since: int | None):
    params = {
        "query": query,
        "limit": min(n, 100),
        "fields": "title,authors,year,venue,abstract,externalIds,url",
    }
    if since:
        params["year"] = f"{since}-"
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/search?"
        + urllib.parse.urlencode(params)
    )
    # Optional free key (S2_API_KEY) lifts you off the shared 5k/5min anon pool.
    hdr = (
        {"x-api-key": os.environ["S2_API_KEY"]}
        if os.environ.get("S2_API_KEY")
        else None
    )
    data = json.loads(_get(url, headers=hdr))
    out = []
    for p in data.get("data", []):
        out.append(
            {
                "title": _trim(p.get("title") or "", 200),
                "authors": [a["name"] for a in p.get("authors", [])][:6],
                "year": p.get("year"),
                "venue": p.get("venue"),
                "url": p.get("url"),
                "abstract": _trim(p.get("abstract") or ""),
            }
        )
    return out


SOURCES = {
    "arxiv": arxiv,
    "openalex": openalex,
    "crossref": crossref,
    "scholar": scholar,
}


def cmd_search(a):
    fn = SOURCES[a.source]
    try:
        results = fn(a.query, a.n, a.since)
    except Exception as exc:  # noqa: BLE001 - report cleanly, never traceback-crash
        alt = "crossref" if a.source != "crossref" else "arxiv"
        sys.exit(
            f"{a.source} request failed: {exc}\n"
            f"(scholar shares a global anon pool and 429s under load; "
            f"try --source {alt}, or set S2_API_KEY / CODEX_RESEARCH_MAILTO)"
        )
    if a.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return
    if not results:
        print("no results", file=sys.stderr)
        return
    for i, r in enumerate(results, start=1):
        auth = ", ".join(r["authors"][:3]) + (
            " et al." if len(r["authors"]) > 3 else ""
        )
        print(f"\n[{i}] {r['title']}  ({r.get('year') or 'n.d.'})")
        print(f"    {auth}  -  {r.get('venue') or ''}")
        if r.get("url"):
            print(f"    {r['url']}")
        if r.get("abstract"):
            print(f"    {r['abstract']}")


def cmd_doi(a):
    url = f"https://api.crossref.org/works/{urllib.parse.quote(a.doi)}"
    try:
        data = json.loads(_get(url))["message"]
    except Exception as exc:  # noqa: BLE001
        sys.exit(f"could not resolve DOI: {exc}")
    print(
        json.dumps(
            {
                "title": (data.get("title") or [""])[0],
                "authors": [
                    f"{x.get('given', '')} {x.get('family', '')}".strip()
                    for x in data.get("author", [])
                ],
                "year": (data.get("issued", {}).get("date-parts") or [[None]])[0][0],
                "venue": (data.get("container-title") or [None])[0],
                "doi": data.get("DOI"),
                "url": "https://doi.org/" + data["DOI"] if data.get("DOI") else None,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def main():
    p = argparse.ArgumentParser(description="keyless research search (stdlib only)")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--source", choices=list(SOURCES), default="scholar")
    s.add_argument("--n", type=int, default=10)
    s.add_argument("--since", type=int)
    s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_search)
    s = sub.add_parser("doi")
    s.add_argument("doi")
    s.set_defaults(fn=cmd_doi)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
