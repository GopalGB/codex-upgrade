#!/usr/bin/env python3
"""patents.py - US patent search via USPTO Open Data Portal (no MCP, stdlib only).

REALITY CHECK (verified June 2026): there is no longer a production-grade KEYLESS
patent API. PatentsView (search.patentsview.org) was retired 2026-03-20 and migrated
to the USPTO Open Data Portal (ODP) at https://api.uspto.gov, which needs a FREE key.

So this tool is key-aware, not keyless:
  - With USPTO_ODP_API_KEY set -> real search against USPTO ODP.
  - Without it -> a NAMED BLOCKER (never a silent fake): it prints exactly how to
    get the free key, emits ready-to-open manual search URLs (Espacenet + Google
    Patents), and points you at the `research-scout` skill for an academic
    prior-art proxy.

Subcommands:
  search QUERY [--limit 10] [--since YYYY]   USPTO ODP search (needs key)
  urls   QUERY                                emit manual search URLs (always works)
  key                                         show how to get the free key

Env: USPTO_ODP_API_KEY  (free, ~30s signup at https://data.uspto.gov "Getting Started";
     from 2026-06-18 a USPTO.gov account sign-in is required to obtain/keep a key).

Examples:
  python patents.py search "graphene battery anode" --limit 10
  python patents.py urls "garment cost optimization"
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request

ODP_SEARCH = "https://api.uspto.gov/api/v1/patent/applications/search"
KEY_ENV = "USPTO_ODP_API_KEY"
KEY_HELP = (
    "USPTO ODP API key not set.\n"
    f"  1. Get a FREE key: https://data.uspto.gov  (Getting Started -> request API key;\n"
    "     a USPTO.gov account sign-in is required as of 2026-06-18).\n"
    f"  2. export {KEY_ENV}=<your-key>\n"
    "  3. Re-run this command.\n"
    'Until then: use `patents.py urls "<query>"` for manual search links, and the\n'
    "`research-scout` skill (Semantic Scholar/arXiv/Crossref) for an academic prior-art proxy."
)


def manual_urls(query: str) -> dict:
    q = urllib.parse.quote(query)
    return {
        "google_patents": f"https://patents.google.com/?q={q}",
        "espacenet": f"https://worldwide.espacenet.com/patent/search?q={urllib.parse.quote('ti%3D' + query)}",
        "uspto_ppubs": "https://ppubs.uspto.gov/pubwebapp/  (USPTO Patent Public Search - free UI)",
    }


def cmd_key(a):
    print(KEY_HELP)


def cmd_urls(a):
    print(f"Manual patent search links for: {a.query}\n")
    for name, url in manual_urls(a.query).items():
        print(f"  {name:16} {url}")
    print(
        "\nFor academic prior-art (keyless): "
        'research-scout/bin/research.py search "%s" --source scholar' % a.query
    )


def cmd_search(a):
    import os

    key = os.environ.get(KEY_ENV)
    if not key:
        # NAMED BLOCKER (per the basic-chatbot lesson: never silent-degrade)
        print("BLOCKED: " + KEY_HELP, file=sys.stderr)
        print("\nManual links meanwhile:", file=sys.stderr)
        for name, url in manual_urls(a.query).items():
            print(f"  {name:16} {url}", file=sys.stderr)
        sys.exit(3)

    body: dict = {
        "q": a.query,
        "pagination": {"offset": 0, "limit": a.limit},
        "sort": [{"field": "applicationMetaData.filingDate", "order": "desc"}],
    }
    if a.since:
        body["rangeFilters"] = [
            {
                "field": "applicationMetaData.filingDate",
                "valueFrom": f"{a.since}-01-01",
                "valueTo": "2100-01-01",
            }
        ]
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        ODP_SEARCH,
        data=data,
        method="POST",
        headers={
            "X-API-KEY": key,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "codex-patent-scout/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            payload = json.loads(resp.read())
    except Exception as exc:  # noqa: BLE001
        sys.exit(
            f"USPTO ODP request failed: {exc}\n"
            f"(check the key, or confirm the endpoint/body at https://data.uspto.gov docs)"
        )

    if a.json:
        print(json.dumps(payload, indent=2)[:20000])
        return
    # ODP response shape can evolve; print defensively.
    results = (
        payload.get("patentFileWrapperDataBag")
        or payload.get("results")
        or payload.get("docs")
        or []
    )
    count = payload.get("count") or payload.get("total") or len(results)
    print(f"USPTO ODP results (~{count}):")
    if not results:
        print(
            "(no parseable result list - dumping top-level keys)", list(payload.keys())
        )
        return
    for i, r in enumerate(results[: a.limit], start=1):
        meta = r.get("applicationMetaData", r)
        title = meta.get("inventionTitle") or meta.get("title") or "(no title)"
        num = (
            r.get("applicationNumberText")
            or meta.get("applicationNumberText")
            or meta.get("patentNumber")
            or ""
        )
        filed = meta.get("filingDate", "")
        print(f"\n[{i}] {title}")
        print(f"    appl: {num}   filed: {filed}")


def main():
    p = argparse.ArgumentParser(description="USPTO patent search (key-aware, no MCP)")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=10)
    s.add_argument("--since", type=int)
    s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_search)
    s = sub.add_parser("urls")
    s.add_argument("query")
    s.set_defaults(fn=cmd_urls)
    s = sub.add_parser("key")
    s.set_defaults(fn=cmd_key)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
