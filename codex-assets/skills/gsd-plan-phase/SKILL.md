---
name: gsd-plan-phase
description: >-
  Create a detailed, verifiable phase plan in .planning/PLAN.md — 3-7 phased steps, each with a success criterion, files affected, out-of-scope, security step. Use before executing.
---

# gsd-plan-phase

Turn the SPEC into an executable plan: `.planning/<phase>/PLAN.md` with the goal line, 3-7 ordered `[ ]` steps EACH with its own success criterion + the files it touches, an explicit out-of-scope list, and a dedicated security/validation step for software (§K). Do a goal-backward check: re-read the success criteria and confirm the steps, if all done, actually achieve them — if not, the plan is wrong, fix it now. Emit `STATUS: AWAITING_APPROVAL` and STOP for the user's go (§C). Adapted from `gsd-plan-phase`. Pitfall: plans that are task-lists without per-step success criteria can't be verified; and a plan that doesn't trace back to the goal builds the wrong thing efficiently. Next: on approval, `gsd-execute-phase`.

**Tools:** .planning/PLAN.md, goal-backward check
