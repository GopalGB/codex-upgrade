---
description: Capture, list, or promote a lesson learned (a mistake to never repeat) into LESSONS.md — the wtf-log.
argument-hint: "[what went wrong]  |  list  |  promote <TAG>"
---
# /prompts:lesson — the wtf-log (manual fallback for the §F frustration rule)

The honest answer to "no hooks": when the model misses a frustration signal, you force
the capture here. ONE schema, shared with `~/.codex/memory/LESSONS.md`.

- **bare `$ARGUMENTS` = CAPTURE.** Read both ledgers (global `~/.codex/memory/LESSONS.md`
  + project `.planning/LESSONS.md`); grep for the same TAG/intent. If it exists, bump
  `hits:` and tighten `correct:` — do NOT add a near-duplicate. Else append a fresh
  entry. Cross-project rule → global; repo-specific → `.planning/LESSONS.md` (create
  the dir if absent — `.planning/` is a sanctioned write target, §H). Echo it back.
- **`list`** = print both ledgers.
- **`promote <TAG>`** = move a project lesson to the global ledger.

Entry schema:
```
### <TAG> — <one-line title>            (hits: N · since YYYY-MM-DD)
- trigger: <what the user said / the situation>
- mistake: <what was done wrong>
- correct: <the imperative rule that prevents recurrence>
- scope:   global | project:<name>
```
