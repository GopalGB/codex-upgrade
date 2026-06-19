---
name: gsd-execute-phase
description: >-
  Execute a phase plan ONE step at a time with checkpoints — change, run the exact tests, self-heal on red, mark done. Parallelize independent steps via swarm. Use after plan approval.
---

# gsd-execute-phase

Execute the approved PLAN.md one step at a time. Per step: make the change → run THE exact tests for it → on red enter the self-healing loop (§D, max 5) → on green mark `[x]` + a one-line note → STOP and report (don't silently barrel through phases). For genuinely INDEPENDENT steps, fan them out in parallel with the `swarm` skill (Codex's equivalent of GSD's wave-based parallelization — isolated `codex exec` workers). Keep `.planning/<phase>/STATE.md` updated so an interrupted session resumes cleanly. Adapted from `gsd-execute-phase`. Pitfall: doing more than one step before verifying compounds errors; skipping the exact-test run = green-by-assertion (a lie). Never mark done on red. Next: when all steps `[x]`, `gsd-verify`.

**Tools:** .planning/PLAN.md, swarm (parallel), self-healing loop
