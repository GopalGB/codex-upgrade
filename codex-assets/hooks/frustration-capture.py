#!/usr/bin/env python3
"""frustration-capture.py — Codex UserPromptSubmit hook (OPTIONAL, opt-in).

Makes AGENTS.md §F (the LESSONS / wtf-log) DETERMINISTIC instead of best-effort:
when the user's message contains a frustration/correction signal, this hook fires
BEFORE the model sees the turn and (1) appends an audit line so nothing is ever
lost, and (2) injects a context reminder that FORCES the model to write a proper
LESSONS.md entry + fix — per the §F loop.

It deliberately does NOT write the lesson itself (a hook can't author a good
`correct:` rule from the trigger text alone). Hook = reliable trigger + audit;
model = the quality lesson + the fix.

Wiring (Codex v0.121, verified at tag rust-v0.121.0):
  config.toml:   [features]\n  codex_hooks = true     # experimental, off by default
  ~/.codex/hooks.json registers this on "UserPromptSubmit".
  Payload arrives as JSON on STDIN with snake_case keys incl. `prompt`.
  Injecting context: print JSON with hookSpecificOutput.additionalContext to stdout.

SAFETY: this must NEVER break a session. Any error → exit 0 with no output.
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone

# Frustration / correction signal classes — matched by MEANING via word patterns,
# case-insensitive. Kept conservative to avoid false positives on normal chat.
SIGNALS = [
    r"\bwtf\b",
    r"what the (?:f|hell|heck)",
    r"\bthis is (?:shit|crap|garbage|broken|wrong|terrible)\b",
    r"\bthat'?s (?:not right|wrong|not what)\b",
    r"\bnot what i (?:asked|wanted|said)\b",
    r"\bi (?:already )?told you\b",
    r"\bi said\b.*\bnot\b",
    r"\bwhy did you\b",
    r"\bstop (?:doing|adding|changing)\b",
    r"\byou (?:keep|always) (?:doing|breaking|ignoring)\b",
    r"\bdon'?t do that\b",
    r"\bthis (?:doesn'?t|does not) work\b",
    r"\byou broke\b",
    r"\bundo (?:that|this)\b",
    r"\bthat'?s (?:useless|pointless)\b",
    r"\bredo\b",
]
_RX = re.compile("|".join(SIGNALS), re.IGNORECASE)


def _codex_home() -> str:
    return os.environ.get("CODEX_HOME") or os.path.expanduser("~/.codex")


def main() -> int:
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return 0
        payload = json.loads(raw)
        prompt = (payload.get("prompt") or "").strip()
        if not prompt or not _RX.search(prompt):
            return 0  # no signal → say nothing, let the turn proceed

        home = _codex_home()
        mem = os.path.join(home, "memory")
        os.makedirs(mem, exist_ok=True)
        ts = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
        # 1) durable audit line (never lost, even if the model ignores the nudge)
        try:
            with open(
                os.path.join(mem, ".frustration-log.jsonl"), "a", encoding="utf-8"
            ) as fh:
                fh.write(
                    json.dumps(
                        {
                            "ts": ts,
                            "cwd": payload.get("cwd", ""),
                            "session_id": payload.get("session_id", ""),
                            "trigger": prompt[:500],
                        }
                    )
                    + "\n"
                )
        except OSError:
            pass  # auditing is best-effort; never block the turn

        # 2) inject a forcing reminder into the model's context for THIS turn
        reminder = (
            "⚠ FRUSTRATION SIGNAL DETECTED in the user's message (Codex Upgrade §F "
            "wtf-log hook). Before anything else this turn you MUST: (1) STOP the "
            "rejected approach; (2) write a proper lesson to LESSONS.md — grep first, "
            "bump `hits`/tighten `correct` if it exists, else append the schema entry; "
            "cross-project rule → ~/.codex/memory/LESSONS.md, repo-specific → "
            ".planning/LESSONS.md; (3) THEN fix, obeying the rule you just wrote; "
            "(4) cite the TAG in your §J LESSON: field. Do not repeat the mistake."
        )
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "UserPromptSubmit",
                        "additionalContext": reminder,
                    }
                }
            )
        )
        return 0
    except Exception:
        # A hook must never crash the session.
        return 0


if __name__ == "__main__":
    sys.exit(main())
