---
name: gsd-spec
description: >-
  Clarify WHAT a phase delivers, with ambiguity scoring, into .planning/SPEC.md — the contract before planning. Use before plan-phase on non-trivial work.
---

# gsd-spec

Before planning HOW, pin down WHAT. Write `.planning/<phase>/SPEC.md`: the deliverable in one sentence, concrete acceptance criteria (checkable: a test passes / a behavior works / a number is hit), in-scope vs explicitly-out, and an AMBIGUITY SCORE (HIGH/MED/LOW) — if HIGH, list the open questions and STOP for the user (§C gate) rather than guess. For software/irreversible/auth-data-money work this IS the PRD (`/prompts:prd`). Identifiers from the user go in verbatim (§A.6). Adapted from `gsd-spec-phase`. Pitfall: vague specs ('make it better') guarantee rework — every criterion must be falsifiable. The spec is the contract `gsd-verify` checks against at the end, so write it so 'done' is unarguable. Next: `gsd-discuss` to gather context, then `gsd-plan-phase`.

**Tools:** .planning/SPEC.md, ambiguity score
