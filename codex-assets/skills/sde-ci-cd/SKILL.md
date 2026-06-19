---
name: sde-ci-cd
description: >-
  Automate build-test-deploy - fast pipeline stages, trunk-based flow, and safe rollout via blue-green/canary with rollback.
---

# sde-ci-cd

**CI** = every push triggers an automated build + lint + type-check + test on a clean environment, so integration problems surface in minutes not at release. **CD** = an automated, repeatable path from green build to production. Pipeline order, fail-fast first: lint/format -> type-check -> unit tests -> build -> integration tests -> security/dependency scan -> deploy. Keep it **fast** (parallelize, cache deps, run the quick checks first) - a 40-minute pipeline kills the feedback loop. Prefer **trunk-based development** with short-lived branches and **feature flags** to decouple deploy from release (ship dark code, enable per-cohort). **Safe rollout strategies**: **blue-green** (stand up the new version alongside old, flip the LB, instant rollback by flipping back); **canary** (route 1% -> 5% -> 50% -> 100%, watching error/latency metrics, auto-halt on regression); **rolling** (replace instances in batches). Always have a **one-command rollback** and DB migrations that are backward-compatible (expand-then-contract: add column, deploy code reading both, backfill, then drop old - never break the running version). **Pitfall**: deploys that can't be rolled back (irreversible migrations run before the new code is proven), and a manual release step that becomes the bottleneck. Make deploys boring and frequent.

**Tools:** GitHub Actions, pipeline stages, trunk-based, blue-green, canary, feature flags, rollback
