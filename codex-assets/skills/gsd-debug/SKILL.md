---
name: gsd-debug
description: >-
  Systematic debugging with persistent state across context resets — hypothesis-driven, one change at a time, logged to .planning/debug/. Use for any non-trivial bug.
---

# gsd-debug

Debug like a scientist, and PERSIST the state so a context reset doesn't lose progress. In `.planning/debug/<bug>.md` log: the exact symptom + repro, the current hypothesis (one), the test that would confirm/refute it, what you changed, and the result. Read the full error/stack first; form ONE minimal hypothesis; make the SMALLEST change; rerun the exact failing command (§D). If a fix is tried twice with no progress → STOP, you're stuck, escalate with the hypothesis history. Never paper over a failing test or claim fixed while red. Adapted from `gsd-debug`. Pitfall: shotgun-changing many things at once means you can't tell what worked; and losing the debug journal on a reset restarts the whole hunt. Next: once green, add a regression test, then `gsd-verify`.

**Tools:** .planning/debug/JOURNAL.md, scientific method, self-healing loop
