---
description: Decompose a goal into a verifiable, phased plan written to .planning/PLAN.md (does not execute)
argument-hint: "[goal]"
---
# /plan — decompose a goal into a verifiable plan (don't execute yet)

Goal from the user: $ARGUMENTS

1. If the goal is ambiguous, ask ONE sharp question before planning. Otherwise proceed.
2. Read `.planning/PLAN.md` (build on it) and `./.codex/memory/MEMORY.md` for prior context.
3. Write `.planning/PLAN.md`:
```markdown
# <task name>
**Goal:** <one sentence success criterion>
**Started:** <timestamp>

## Phases
- [ ] Phase 1: <verb> <object> — <success criterion>
- [ ] Phase 2: …

## Success criteria (goal-backward)
- [ ] <a test that passes / a file that exists / a behavior that works>

## Files affected
- `path` — <why>

## Out of scope
- <what NOT to touch>
```
4. Output `STATUS: PLANNED` + the plan inline. Do NOT execute — wait for the user
   to say "go" (then execute one phase at a time per § C of `~/.codex/AGENTS.md`).
