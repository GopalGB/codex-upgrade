---
name: gsd-ship
description: >-
  Ship after verification — branch, commit (Conventional Commits), run the security/secret gate, open a PR, prep for merge. Use only after verify + review pass.
---

# gsd-ship

Ship only after `gsd-verify` + `gsd-code-review` are green. Steps: ensure you're on a feature branch (never commit straight to main/master), make atomic Conventional Commits, run `security-auditor` (secret scan) BEFORE the push — never `--no-verify` past a pre-push hook (§H), open a PR with a clear description (what/why/how-to-test/risks), and state the rollback plan. Confirm before any outbound action (push to shared remote, public PR) per §G. Adapted from `gsd-ship`. Pitfall: shipping with a skipped scan manufactures false confidence; force-pushing main is banned. A PR over ~400 lines should be split. Next: after merge, `gsd-extract-learnings`.

**Tools:** git, security-auditor, Conventional Commits, PR
