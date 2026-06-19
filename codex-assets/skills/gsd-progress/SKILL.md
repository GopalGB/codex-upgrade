---
name: gsd-progress
description: >-
  The situational GSD command — 'where am I, what's next?' Reads .planning/ state and advises the next GSD step (or dispatches a freeform intent to the right phase). Use anytime you're unsure.
---

# gsd-progress

The unified situational command. Read `.planning/` (PROJECT.md, the active phase's SPEC/PLAN/STATE) and report: what phase you're in, what's done vs pending, and the ONE next GSD action. If the user gives a freeform intent ('add auth', 'fix the slow query'), route it to the right phase: new work → `gsd-spec`; mid-build → `gsd-execute-phase`; done-building → `gsd-verify`; bug → `gsd-debug`; unfamiliar repo → `gsd-map-codebase`. Adapted from `gsd-progress`. The GSD lifecycle is: new-project → spec → discuss → plan → execute → verify → code-review → ship → extract-learnings. Pitfall: working without knowing which phase you're in leads to skipped gates (no spec, no verify). When unsure, run this first. This pack reinforces AGENTS.md §C — GSD is the default for ALL non-trivial work, not optional.

**Tools:** .planning/ state, the GSD lifecycle
