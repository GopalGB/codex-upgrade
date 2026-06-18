#!/usr/bin/env python3
"""validate_skill.py - lint Codex SKILL.md files against the v0.121 loader rules.

Replicates skill-creator's quick_validate checks (stdlib only, no network):
  - frontmatter delimited by --- on line 1 and a closing ---
  - `name` present, non-empty, <=64 chars, lowercase/digits/hyphens, == folder name
  - `description` present, non-empty, <=1024 chars
  - warns on Anthropic-only keys Codex silently drops (allowed-tools/model/license)
  - warns on forbidden helper files inside a skill dir (README.md/CHANGELOG.md/...)

Usage:
  python3 validate_skill.py <skills-root-or-skill-dir> [more...]
Exit code 0 = all valid, 1 = at least one error.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
DROPPED = ("allowed-tools", "model", "license", "version", "argument-hint")
FORBIDDEN_FILES = (
    "README.md",
    "INSTALLATION_GUIDE.md",
    "CHANGELOG.md",
    "QUICK_REFERENCE.md",
)


def _frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip("\n")
    fm: dict = {}
    key = None
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            key = m.group(1)
            fm[key] = m.group(2).strip()
    return fm


def validate_one(skill_dir: Path) -> list[str]:
    errs: list[str] = []
    sk = skill_dir / "SKILL.md"
    if not sk.is_file():
        return [f"{skill_dir}: missing SKILL.md"]
    fm = _frontmatter(sk.read_text(encoding="utf-8"))
    if fm is None:
        return [f"{sk}: missing/un-terminated YAML frontmatter (--- ... ---)"]
    name = (fm.get("name") or "").strip().strip('"').strip("'")
    desc = (fm.get("description") or "").strip()
    if not name:
        errs.append(f"{sk}: empty `name`")
    elif not NAME_RE.match(name):
        errs.append(
            f"{sk}: `name` must be lowercase/digits/hyphens <=64 (got '{name}')"
        )
    elif name != skill_dir.name:
        errs.append(
            f"{sk}: `name` ('{name}') must equal folder name ('{skill_dir.name}')"
        )
    if not desc:
        errs.append(f"{sk}: empty `description` (it is the sole trigger signal)")
    elif len(desc) > 1024 and "|" not in desc and ">" not in desc:
        errs.append(f"{sk}: `description` >1024 chars")
    for k in DROPPED:
        if k in fm:
            print(
                f"  warn {sk}: frontmatter `{k}` is silently dropped by Codex "
                f"(put tool/policy metadata in agents/openai.yaml)"
            )
    for f in FORBIDDEN_FILES:
        if (skill_dir / f).exists():
            print(
                f"  warn {skill_dir}: `{f}` inside a skill dir is discouraged by skill-creator"
            )
    return errs


def iter_skill_dirs(root: Path):
    if (root / "SKILL.md").is_file():
        yield root
        return
    for child in sorted(root.iterdir()):
        if (
            child.is_dir()
            and not child.name.startswith(".")
            and (child / "SKILL.md").is_file()
        ):
            yield child


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1
    all_errs: list[str] = []
    n = 0
    for arg in argv:
        for d in iter_skill_dirs(Path(arg)):
            n += 1
            all_errs.extend(validate_one(d))
    if all_errs:
        print(f"\nINVALID ({len(all_errs)} error(s) across {n} skill(s)):")
        for e in all_errs:
            print("  ✗", e)
        return 1
    print(f"OK: {n} skill(s) valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
