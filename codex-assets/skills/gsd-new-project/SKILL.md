---
name: gsd-new-project
description: >-
  Initialize a project the GSD way — deep context gathering into .planning/PROJECT.md (goal, users, constraints, stack, success criteria) before any build.
---

# gsd-new-project

Start every real project by capturing intent, not code. Create `.planning/PROJECT.md` with: the ONE-sentence goal, who it's for + the job-to-be-done, hard constraints (deadline/stack/budget/compliance), the existing stack (detect it — read package manifests, don't assume), explicit out-of-scope, and 3-5 measurable success criteria. Ask the few questions only the user can answer (don't guess scope or identifiers — §A.6); infer the rest from the repo. This file is the project's source of truth that survives context resets — every later GSD phase reads it. Adapted from Claude Code's `gsd-new-project`. Pitfall: jumping to code before WHAT/WHY is written produces confident-but-wrong work; PROJECT.md is the cheap insurance. Keep it tight (one screen), update it when scope genuinely changes (don't silently drift). Next: `gsd-spec` a phase, or `gsd-map-codebase` if joining an existing repo.

**Tools:** .planning/PROJECT.md, context interview
