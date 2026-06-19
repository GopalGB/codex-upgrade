---
name: gsd-verify
description: >-
  Goal-backward verification + conversational UAT — re-read the SPEC criteria, run the FULL suite, confirm each criterion actually passes, get Claude Opus review. Use before ship.
---

# gsd-verify

Done means the SPEC's criteria pass, not 'it compiles'. Re-read `.planning/<phase>/SPEC.md`; for EACH acceptance criterion mark COVERED/PARTIAL/MISSING with the evidence (test output, behavior, file). Run the FULL suite + linter/types (not just changed files). Walk the user through conversational UAT — show what to click/run to confirm it works for real. Then the HARD gates: `claude-review` (Claude Opus 4.8 reviews the diff) + `security-auditor` (secrets/SAST/deps) — both must pass. Emit the §J completion block. Adapted from `gsd-verify-work`. Pitfall: a passing test suite ≠ the feature works for the user; UAT catches the gap. Never call it DONE with a MISSING criterion or an unreviewed diff. Next: `gsd-ship`.

**Tools:** .planning/SPEC.md, full test suite, claude-review
