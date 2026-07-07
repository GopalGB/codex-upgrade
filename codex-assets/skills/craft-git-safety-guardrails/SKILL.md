---
name: craft-git-safety-guardrails
description: >-
  Apply safe git hygiene — never force-push a shared branch, never commit secrets or .env, branch off main instead of committing to it, review the diff before staging, and write atomic Conventional Commits. Use for any git operation to avoid destroying history, leaking credentials, or polluting the default branch.
---

# craft-git-safety-guardrails

Git operations are easy to get irreversibly wrong. The hard rules: **never `git push --force` a shared branch** (use `--force-with-lease` on your own feature branch only, never on main/shared); **never commit secrets** — scan the diff for keys, tokens, `.env`, credentials before every commit, and if one slips in, rotate it (history rewrite alone doesn't un-leak it); **never commit straight to `main`/`master`** — branch first; **never `git reset --hard`, `clean -fd`, or `checkout .`** over uncommitted work without confirming you're not destroying something you can't recover.

Stage deliberately. Read `git diff` (and `git diff --staged`) before you commit — `git add -A` blindly is how debug prints, large binaries, and stray files get committed. Add a focused `.gitignore` rather than committing build output and dependencies.

Commit atomically with **Conventional Commits**: one logical change per commit, `type(scope): summary` (feat/fix/refactor/docs/test/chore), imperative mood, the *why* in the body when it isn't obvious. Small, well-described commits make review, revert, and bisect work. Before any history-altering or outward-facing action (force-push, rebase of shared history, tag, release), pause and confirm intent — these are the ones you can't quietly undo.

**Tools:** no force-push to shared · scan for secrets pre-commit · branch off main · review diff before staging · atomic Conventional Commits · confirm before irreversible ops
