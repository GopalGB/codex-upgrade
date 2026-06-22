#!/usr/bin/env python3
"""memory.py — file-based long-term memory for Codex (stdlib only, no MCP, no network).

Gives Codex durable recall across sessions WITHOUT a vector DB or any server: each
memory is one markdown "card" on disk; `recall` does TF-IDF keyword scoring × recency ×
importance and returns only the top-k — so memory NEVER floods the context window
(progressive-disclosure-safe: the cards live on disk, only the few relevant ones are
printed when you ask). Complements the flat logs: LESSONS.md = mistakes, MEMORY.md =
task log, these cards = queryable facts/decisions/preferences.

Storage:  $CODEX_MEMORY_DIR  (else $CODEX_HOME/memory/cards  else ~/.codex/memory/cards)
Card file: <id>.md — frontmatter (id/created/updated/tags/importance/hits/last_used/scope)
           then the fact as markdown body.

Commands:
  memory.py add "fact"  [--tags a,b] [--importance 1-5] [--scope global|project:NAME]
  memory.py recall "query" [--k 5] [--scope ...] [--tag T] [--json]
  memory.py list   [--scope ...] [--tag T] [--json]
  memory.py forget <id> [--decay]            # delete the card (or just lower importance)
  memory.py gc     [--ttl-days 120] [--max N] [--dry-run]   # bound growth
  memory.py stats  [--json]
  memory.py selftest                         # round-trip self-check (ponytail: one check)

Design notes: ai-agent-memory skill — score by relevance×recency×importance, write durable
facts only, forget on decay/TTL to bound growth. Pure stdlib: nothing to install.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

STOPWORDS = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "but",
    "if",
    "to",
    "of",
    "in",
    "on",
    "for",
    "is",
    "are",
    "was",
    "were",
    "be",
    "it",
    "this",
    "that",
    "with",
    "as",
    "at",
    "by",
    "we",
    "you",
    "i",
    "my",
    "our",
    "do",
    "does",
    "how",
    "what",
    "when",
}
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_+-]{1,}")
FM_KEYS = (
    "id",
    "created",
    "updated",
    "tags",
    "importance",
    "hits",
    "last_used",
    "scope",
)


# --- paths & time -------------------------------------------------------------
def memory_dir() -> Path:
    env = os.environ.get("CODEX_MEMORY_DIR")
    if env:
        d = Path(env)
    else:
        home = os.environ.get("CODEX_HOME") or os.path.expanduser("~/.codex")
        d = Path(home) / "memory" / "cards"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _new_id() -> str:
    return (
        datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S") + "-" + os.urandom(2).hex()
    )


def _tokens(text: str) -> list[str]:
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOPWORDS]


# --- card read/write ----------------------------------------------------------
def _parse_card(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    fm: dict = {
        "id": path.stem,
        "tags": "",
        "importance": "3",
        "hits": "0",
        "last_used": "",
        "scope": "global",
        "created": "",
        "updated": "",
    }
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].strip("\n").splitlines():
                m = re.match(r"^([a-z_]+):\s*(.*)$", line)
                if m and m.group(1) in FM_KEYS:
                    fm[m.group(1)] = m.group(2).strip()
            body = text[end + 4 :].lstrip("\n")
    fm["body"] = body.strip()
    fm["importance"] = _clamp_int(fm.get("importance"), 3, 1, 5)
    fm["hits"] = _clamp_int(fm.get("hits"), 0, 0, 10**9)
    return fm


def _clamp_int(val, default: int, lo: int, hi: int) -> int:
    try:
        return max(lo, min(hi, int(str(val).strip())))
    except (TypeError, ValueError):
        return default


def _write_card(card: dict) -> Path:
    d = memory_dir()
    path = d / f"{card['id']}.md"
    fm = (
        f"---\nid: {card['id']}\ncreated: {card.get('created') or _now()}\n"
        f"updated: {_now()}\ntags: {card.get('tags', '')}\n"
        f"importance: {card['importance']}\nhits: {card['hits']}\n"
        f"last_used: {card.get('last_used', '')}\nscope: {card.get('scope', 'global')}\n---\n\n"
    )
    path.write_text(fm + card["body"].strip() + "\n", encoding="utf-8")
    return path


def _load_all(scope: str | None = None, tag: str | None = None) -> list[dict]:
    cards = []
    for p in sorted(memory_dir().glob("*.md")):
        c = _parse_card(p)
        if c is None:
            print(f"  warn: skipping unreadable card {p.name}", file=sys.stderr)
            continue
        if scope and c.get("scope") != scope:
            continue
        if tag and tag.lower() not in [
            t.strip().lower() for t in c.get("tags", "").split(",")
        ]:
            continue
        cards.append(c)
    return cards


# --- scoring (TF-IDF × recency × importance) ----------------------------------
def _doc_terms(card: dict) -> Counter:
    # tags weigh 3x — they are deliberate index terms.
    return Counter(_tokens(card["body"]) + _tokens(card.get("tags", "")) * 3)


def _recency_factor(card: dict) -> float:
    stamp = card.get("last_used") or card.get("created") or ""
    try:
        age = (
            datetime.now(timezone.utc)
            - datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc
            )
        ).days
    except (ValueError, TypeError):
        return 1.0
    return 1.0 + 0.3 * (0.5 ** (max(age, 0) / 45.0))  # fresh≈1.3 → old≈1.0, gentle


def _score(cards: list[dict], query: str) -> list[tuple[float, dict]]:
    q_terms = set(_tokens(query))
    if not q_terms:
        return []
    n = len(cards) or 1
    df = Counter()
    docs = []
    for c in cards:
        dt = _doc_terms(c)
        docs.append(dt)
        for t in set(dt):
            df[t] += 1
    out = []
    for c, dt in zip(cards, docs):
        s = 0.0
        for t in q_terms:
            if t in dt:
                idf = math.log(1 + n / (1 + df[t]))
                s += min(dt[t], 3) * idf
        if s > 0:
            s *= (c["importance"] / 3.0) * _recency_factor(c)
            out.append((s, c))
    out.sort(key=lambda x: x[0], reverse=True)
    return out


def _touch(card: dict) -> None:
    card["hits"] += 1
    card["last_used"] = _now()
    _write_card(card)


# --- commands -----------------------------------------------------------------
def cmd_add(args) -> int:
    body = sys.stdin.read() if args.text == "-" else args.text
    body = body.strip()
    if not body:
        print("BLOCKER: empty fact — nothing to store.", file=sys.stderr)
        return 1
    norm = " ".join(_tokens(body))
    for c in _load_all():  # dedup: bump instead of duplicating (LESSONS-style)
        if " ".join(_tokens(c["body"])) == norm:
            c["importance"] = min(5, c["importance"] + 1)
            c["hits"] += 1
            c["last_used"] = _now()
            if args.tags:
                merged = {
                    t.strip()
                    for t in (c.get("tags", "") + "," + args.tags).split(",")
                    if t.strip()
                }
                c["tags"] = ",".join(sorted(merged))
            _write_card(c)
            print(
                f"DUP → bumped {c['id']} (importance={c['importance']}, hits={c['hits']})"
            )
            return 0
    card = {
        "id": _new_id(),
        "created": _now(),
        "tags": args.tags or "",
        "importance": _clamp_int(args.importance, 3, 1, 5),
        "hits": 0,
        "last_used": "",
        "scope": args.scope or "global",
        "body": body,
    }
    path = _write_card(card)
    print(
        f"stored {card['id']}  (scope={card['scope']}, importance={card['importance']})  -> {path}"
    )
    return 0


def cmd_recall(args) -> int:
    cards = _load_all(args.scope, args.tag)
    ranked = _score(cards, args.query)[: args.k]
    for _, c in ranked:
        _touch(c)
    if args.json:
        print(
            json.dumps(
                [
                    {
                        "id": c["id"],
                        "score": round(s, 3),
                        "scope": c["scope"],
                        "importance": c["importance"],
                        "tags": c["tags"],
                        "body": c["body"],
                    }
                    for s, c in ranked
                ],
                indent=2,
            )
        )
        return 0
    if not ranked:
        print(f"(no memory matched '{args.query}' — {len(cards)} card(s) searched)")
        return 0
    for s, c in ranked:
        tags = f" [{c['tags']}]" if c["tags"] else ""
        print(
            f"• ({s:.2f}·imp{c['importance']}·{c['scope']}){tags} {c['id']}\n  {c['body']}\n"
        )
    return 0


def cmd_list(args) -> int:
    cards = _load_all(args.scope, args.tag)
    cards.sort(key=lambda c: (c["importance"], c.get("last_used", "")), reverse=True)
    if args.json:
        print(
            json.dumps(
                [
                    {k: c[k] for k in ("id", "scope", "importance", "hits", "tags")}
                    | {"first_line": c["body"].splitlines()[0] if c["body"] else ""}
                    for c in cards
                ],
                indent=2,
            )
        )
        return 0
    print(f"{len(cards)} card(s):")
    for c in cards:
        first = c["body"].splitlines()[0] if c["body"] else ""
        print(
            f"  {c['id']}  imp{c['importance']} hits{c['hits']} [{c['tags']}] {first[:80]}"
        )
    return 0


def cmd_forget(args) -> int:
    if "/" in args.id or "\\" in args.id or ".." in args.id:  # no path traversal
        print(f"BLOCKER: invalid card id '{args.id}'", file=sys.stderr)
        return 1
    path = memory_dir() / f"{args.id}.md"
    if not path.exists():
        print(f"BLOCKER: no card '{args.id}'", file=sys.stderr)
        return 1
    if args.decay:
        c = _parse_card(path)
        c["importance"] = max(1, c["importance"] - 1)
        _write_card(c)
        print(f"decayed {args.id} -> importance {c['importance']}")
    else:
        path.unlink()
        print(f"forgot {args.id}")
    return 0


def cmd_gc(args) -> int:
    cards = _load_all()
    doomed = []
    for c in cards:  # prune low-value stale never-hit cards
        try:
            age = (
                datetime.now(timezone.utc)
                - datetime.strptime(
                    c.get("last_used") or c.get("created"), "%Y-%m-%dT%H:%M:%SZ"
                ).replace(tzinfo=timezone.utc)
            ).days
        except (ValueError, TypeError):
            age = 0
        if c["importance"] <= 1 and c["hits"] == 0 and age >= args.ttl_days:
            doomed.append(c)
    keep = [c for c in cards if c not in doomed]
    if (
        args.max and len(keep) > args.max
    ):  # over cap → drop lowest importance, then oldest
        keep.sort(key=lambda c: (c["importance"], c.get("last_used", "")))
        doomed += keep[: len(keep) - args.max]
    for c in doomed:
        print(
            f"  {'[dry] ' if args.dry_run else ''}prune {c['id']} (imp{c['importance']} hits{c['hits']})"
        )
        if not args.dry_run:
            (memory_dir() / f"{c['id']}.md").unlink(missing_ok=True)
    print(
        f"{'would prune' if args.dry_run else 'pruned'} {len(doomed)} card(s); {len(cards) - len(doomed)} remain"
    )
    return 0


def cmd_stats(args) -> int:
    cards = _load_all()
    by_scope, by_tag = Counter(), Counter()
    for c in cards:
        by_scope[c["scope"]] += 1
        for t in c.get("tags", "").split(","):
            if t.strip():
                by_tag[t.strip()] += 1
    data = {
        "cards": len(cards),
        "dir": str(memory_dir()),
        "by_scope": dict(by_scope),
        "top_tags": dict(by_tag.most_common(10)),
    }
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(f"{data['cards']} card(s) in {data['dir']}")
        print(f"  by scope: {data['by_scope']}")
        print(f"  top tags: {data['top_tags']}")
    return 0


def cmd_selftest(_args) -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        os.environ["CODEX_MEMORY_DIR"] = tmp
        _run(
            [
                "add",
                "GetCallBounce backend uses FastAPI with httpx and pydantic v2",
                "--tags",
                "gcb,stack",
                "--importance",
                "4",
            ]
        )
        _run(
            [
                "add",
                "The office Codex box blocks pip — use the tools-venv bootstrap",
                "--tags",
                "office",
            ]
        )
        ranked = _score(_load_all(), "what backend framework does gcb use")
        assert ranked, "recall returned nothing"
        assert "fastapi" in ranked[0][1]["body"].lower(), (
            f"wrong top hit: {ranked[0][1]['body']}"
        )
        cid = ranked[0][1]["id"]
        _run(
            ["add", "GetCallBounce backend uses FastAPI with httpx and pydantic v2"]
        )  # dup → bump
        assert len(_load_all()) == 2, "dedup failed — duplicate stored"
        _run(["forget", cid])
        assert len(_load_all()) == 1, "forget failed"
        print("OK: memory.py selftest passed (add · dedup · recall-rank · forget)")
    return 0


# --- arg wiring ---------------------------------------------------------------
def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="memory.py", description="file-based long-term memory for Codex"
    )
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("text")
    a.add_argument("--tags", default="")
    a.add_argument("--importance", default="3")
    a.add_argument("--scope", default="global")
    a.set_defaults(fn=cmd_add)
    r = sub.add_parser("recall")
    r.add_argument("query")
    r.add_argument("--k", type=int, default=5)
    r.add_argument("--scope")
    r.add_argument("--tag")
    r.add_argument("--json", action="store_true")
    r.set_defaults(fn=cmd_recall)
    l = sub.add_parser("list")
    l.add_argument("--scope")
    l.add_argument("--tag")
    l.add_argument("--json", action="store_true")
    l.set_defaults(fn=cmd_list)
    f = sub.add_parser("forget")
    f.add_argument("id")
    f.add_argument("--decay", action="store_true")
    f.set_defaults(fn=cmd_forget)
    g = sub.add_parser("gc")
    g.add_argument("--ttl-days", type=int, default=120)
    g.add_argument("--max", type=int, default=0)
    g.add_argument("--dry-run", action="store_true")
    g.set_defaults(fn=cmd_gc)
    s = sub.add_parser("stats")
    s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_stats)
    sub.add_parser("selftest").set_defaults(fn=cmd_selftest)
    return p


def _run(argv: list[str]) -> int:  # used by selftest
    args = _build_parser().parse_args(argv)
    return args.fn(args)


def main(argv: list[str]) -> int:
    args = _build_parser().parse_args(argv)
    try:
        return args.fn(args)
    except BrokenPipeError:
        return 0
    except Exception as exc:  # never hard-crash a Codex session
        print(f"BLOCKER: memory.py {args.cmd} failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
