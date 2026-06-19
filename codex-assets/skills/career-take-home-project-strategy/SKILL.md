---
name: career-take-home-project-strategy
description: >-
  Maximize a take-home assignment with scoping, tests, README, and production-mindset signals while time-boxing — use when given a take-home or work-sample.
---

# career-take-home-project-strategy

Take-homes are scored on code quality, judgment, communication, and completeness — and reviewers compare you to dozens of submissions. **Time-box hard** (respect the stated limit; going 3× over both burns you out and is unfair signal — instead document what you'd do with more time). Read requirements twice; build the core happy path *fully working* before any polish — a partial impressive feature loses to a complete simple one.

Signal production maturity: meaningful tests (not 100%, but the critical paths + edge cases), error handling, input validation, clear module boundaries, and a config/setup that runs in one command. **The README is half the grade:** state assumptions, design decisions and tradeoffs, how to run, how to test, and an explicit 'what I'd do with more time / what I cut and why' section. Use small, atomic, well-messaged commits — reviewers read git history to see how you think.

**What top candidates do differently:** they treat it like a real PR — clean diffs, no dead code, no commented-out blocks — and they make the reviewer's job effortless (one-command setup, sample data, screenshots).

**Common mistake:** over-engineering (a microservices architecture for a CRUD task), gold-plating one feature while core requirements are missing, no tests, no README, and ignoring the stated stack/constraints. Completeness + clarity + judgment beats cleverness.

**Tools:** time-boxing, README with tradeoffs, tests + CI, clean commits, scope-cut documentation
