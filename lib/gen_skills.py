#!/usr/bin/env python3
"""gen_skills.py - generate SKILL.md files from a catalog JSON (the library pack).

Reads a Workflow result file (wrapper: {result:{cats:[{domain,prefix,skills:[...]}]}})
or a bare {cats:[...]} JSON, and writes one codex-assets/skills/<name>/SKILL.md per
skill (frontmatter name+description as a folded block scalar + the body). Idempotent:
overwrites only the names in the catalog; never touches other (core) skills.

Usage:
  python3 gen_skills.py <catalog.json> [--out codex-assets/skills] [--dry-run]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"[^a-z0-9-]+")


def load_cats(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "result" in data:
        data = data["result"]
        if isinstance(data, str):
            data = json.loads(data)
    return data.get("cats", data.get("domains", []))


def slug(name: str, prefix: str) -> str:
    s = NAME_RE.sub("-", (name or "").strip().lower()).strip("-")[:64]
    if prefix and not s.startswith(prefix + "-") and s != prefix:
        s = f"{prefix}-{s}"[:64].strip("-")
    return s


def oneline(text: str, cap: int = 980) -> str:
    t = " ".join((text or "").split())
    return t if len(t) <= cap else t[: cap - 1] + "…"


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1
    src = Path(argv[0])
    out = Path("codex-assets/skills")
    dry = "--dry-run" in argv
    if "--out" in argv:
        out = Path(argv[argv.index("--out") + 1])

    cats = load_cats(src)
    if not cats:
        print("no catalog found in input")
        return 1

    seen: set[str] = set()
    written = 0
    per_domain: dict[str, int] = {}
    for cat in cats:
        if not cat:
            continue
        prefix = (cat.get("prefix") or "").strip().lower()
        for sk in cat.get("skills", []):
            name = slug(sk.get("name", ""), prefix)
            if not name:
                continue
            if name in seen:  # dedupe
                i = 2
                while f"{name}-{i}" in seen:
                    i += 1
                name = f"{name}-{i}"
            seen.add(name)
            desc = oneline(sk.get("description", ""))
            body = (sk.get("body_md") or "").strip()
            tools = (sk.get("tools") or "").strip()
            if not desc or not body:
                continue
            md = (
                "---\n"
                f"name: {name}\n"
                "description: >-\n"
                f"  {desc}\n"
                "---\n\n"
                f"# {name}\n\n"
                f"{body}\n"
            )
            if tools:
                md += f"\n**Tools:** {tools}\n"
            per_domain[prefix] = per_domain.get(prefix, 0) + 1
            written += 1
            if dry:
                continue
            d = out / name
            d.mkdir(parents=True, exist_ok=True)
            (d / "SKILL.md").write_text(md, encoding="utf-8")

    print(f"{'[dry-run] would write' if dry else 'wrote'} {written} skills")
    for p, n in sorted(per_domain.items()):
        print(f"  {p or '(none)':10} {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
