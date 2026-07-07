---
name: craft-handoff-context-notes
description: >-
  When pausing, finishing a session, or handing off, leave a precise state note — what's done, what's next, what's broken, and exactly how to run and verify it. Use before ending work or when context is about to reset so the next session or person resumes without re-deriving everything.
---

# craft-handoff-context-notes

Context evaporates — between sessions, across a compaction, when a teammate picks up. A good **handoff note** is the antidote: a short, concrete record of state so the next actor resumes in minutes instead of reconstructing your reasoning by archaeology. Write it before you stop, not from memory afterward.

Capture five things: **Done** — what's actually complete and verified. **Next** — the immediate next step, specific enough to start cold. **Broken/blocked** — what's failing, the error, what you suspect, and any blocker awaiting someone else. **How to run/verify** — the exact commands, the test that matters, the URL/credentials path (never the secrets themselves). **Decisions & gotchas** — non-obvious choices made and traps discovered, so they aren't relitigated or re-stepped-on.

Keep it where the next session will look — a `HANDOFF.md`, a `.planning/` scratchpad, a PR description, or the issue thread — not buried in chat. Be honest about uncertainty ("I think the failure is in the auth middleware but didn't confirm"). The test of a handoff note: could someone with this repo and your note continue without asking you a single question? Write to pass that test.

**Tools:** Done / Next / Broken / How-to-run / Decisions · write before stopping · store where the next session looks · concrete commands not prose · honest about unknowns
