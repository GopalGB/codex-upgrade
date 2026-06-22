#!/usr/bin/env python3
"""session-start.py — Codex SessionStart hook (OPTIONAL, opt-in).

The "single always-run opening ritual" that makes the AGENTS.md law sticky: at the
start of every session it injects ONE short reminder of the GSD loop + how many
lessons are loaded. Deterministic counterpart to the behavioral law.

Wiring (Codex v0.121): [features] codex_hooks = true + ~/.codex/hooks.json on
"SessionStart". Payload on STDIN (snake_case). Inject via stdout JSON
hookSpecificOutput.additionalContext. MUST never break a session → errors exit 0.
"""

from __future__ import annotations

import json
import os
import sys


def _codex_home() -> str:
    return os.environ.get("CODEX_HOME") or os.path.expanduser("~/.codex")


def _count_lessons(path: str) -> int:
    try:
        with open(path, encoding="utf-8") as fh:
            return sum(1 for line in fh if line.startswith("### "))
    except OSError:
        return 0


def _count_cards(cards_dir: str) -> int:
    try:
        return sum(1 for f in os.listdir(cards_dir) if f.endswith(".md"))
    except OSError:
        return 0


def main() -> int:
    try:
        sys.stdin.read()  # drain payload; we don't need its fields
        home = _codex_home()
        lessons = _count_lessons(os.path.join(home, "memory", "LESSONS.md"))
        cards = _count_cards(os.path.join(home, "memory", "cards"))
        recall = (
            f' {cards} memory cards stored — `memory.py recall "<query>"` to pull the '
            "top-k relevant ones (context-safe); `add` durable facts after."
            if cards
            else " Use the memory-keeper skill (`memory.py add/recall`) for durable facts."
        )
        msg = (
            "CODEX UPGRADE active. Default method (AGENTS.md §C): trivial work → just "
            "do it; real work → clarify WHAT+WHY → approval → phased plan → approval → "
            "one phase at a time → verify; software/irreversible → /prompts:prd first. "
            f"Read LESSONS.md before non-trivial work ({lessons} lessons loaded) and log "
            "a new one on any frustration signal (§F)." + recall
        )
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "SessionStart",
                        "additionalContext": msg,
                    }
                }
            )
        )
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
