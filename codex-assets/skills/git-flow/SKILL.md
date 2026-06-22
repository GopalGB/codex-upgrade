---
name: git-flow
description: >-
  Everyday git craft for a coding agent — atomic Conventional commits,
  interactive rebase/squash/fixup, bisect for regressions, conflict resolution,
  reflog recovery, worktrees, stash, cherry-pick, and safe rewrite
  (force-with-lease only, never shared history). The craft used during EXECUTE;
  gsd-ship owns the final commit+PR+secret-scan gate. Use when branching,
  committing, rebasing, hunting a regression, or recovering work.
  Triggers: "commit this", "rebase", "squash commits", "fix conflict",
  "git bisect", "undo commit", "lost my work", "reflog".
---

# git-flow — everyday git craft (no MCP, no `gh` assumed)

Field manual for the EXECUTE phase of the GSD loop. `git` is present; `gh` may NOT be —
every `gh` step below gives a plain-git fallback. **`gsd-ship` owns SHIP** (final commit,
open PR, secret scan) — do not duplicate it here.

## LAW — destructive-command guardrails (read first)
- **NEVER** `git push --force`. Use `git push --force-with-lease` — it refuses if the remote moved (someone else pushed), preventing silent overwrite of teammates' work.
- **NEVER** `--no-verify`. Hooks (lint, secret scan) are the safety net; bypassing them is forbidden.
- **NEVER rewrite history that is already shared/pushed to a branch others use** (`main`, release branches, any branch with open PRs/reviewers). Rewrite ONLY your own un-pulled feature branch.
- `git reflog` is the undo-net. Before any rebase/reset/amend, know that reflog can recover the pre-op state for ~90 days. Almost nothing is truly lost.
- `git reset --hard` and `git clean -fd` discard uncommitted work permanently — `git stash` first if unsure.

## Branch hygiene
```bash
git switch -c feat/payment-retry        # create + switch (modern; not `checkout -b`)
git switch main && git pull --ff-only   # update main without surprise merge commits
git switch -c fix/null-cart main        # branch off fresh main
git branch -d feat/old                  # delete merged branch (-D forces; avoid)
```
- One branch = one logical unit of work. Name `type/short-desc`: `feat/`, `fix/`, `refactor/`, `docs/`, `chore/`.
- Rebase your feature branch onto updated main to keep history linear: `git fetch && git rebase origin/main` (only while the branch is yours alone).

## Atomic commits + Conventional Commits
Commit the **smallest coherent change** that still builds/passes. Stage selectively:
```bash
git add -p                  # interactively stage hunks — split unrelated changes
git add path/to/file.ts     # or stage by path
git restore --staged file   # unstage without losing edits
```
Conventional Commits format (`type(scope): summary`):
```
feat(cart): retry failed payment captures up to 3x

Adds exponential backoff between retries. Closes the gap where a
transient gateway 503 dropped the order silently.
```
- Types: `feat fix refactor perf docs test chore build ci`. `feat!:` or a `BREAKING CHANGE:` footer marks a break.
- Summary ≤ ~50 chars, imperative ("add", not "added"). Body wraps ~72, explains **why**, not what.
- Reference issues in the body/footer (`Closes #42`), not the summary.

## Amend & fixup (clean up BEFORE pushing)
```bash
git commit --amend                      # fold staged changes into last commit, edit msg
git commit --amend --no-edit            # same message
```
For an older commit on your branch, use **autosquash** (don't amend the wrong one):
```bash
git commit --fixup <sha>                # makes "fixup! <subject>" targeting <sha>
git rebase -i --autosquash origin/main  # auto-orders & marks the fixup for squashing
```
Only amend/fixup commits **not yet pushed** (or pushed only to your solo branch).

## Interactive rebase — squash / reorder / reword
```bash
git rebase -i HEAD~5        # edit the last 5 commits
git rebase -i origin/main   # edit everything since you branched
```
In the todo list change the verb per line:
- `pick` keep · `reword` edit message · `squash` merge into previous (keep both msgs) ·
  `fixup` merge silently · `edit` stop to amend · `drop` delete · reorder lines to reorder commits.
If a rebase goes wrong mid-flight: `git rebase --abort` returns to the exact pre-rebase state.
After a clean rebase of an already-pushed solo branch, update the remote with the safe push:
```bash
git push --force-with-lease
```

## Conflict resolution
During merge/rebase/cherry-pick, conflicted files show `<<<<<<<`, `=======`, `>>>>>>>` markers.
```bash
git status                  # list conflicted paths
git diff                    # see both sides in context
# edit files: keep the correct combination, delete ALL markers
git add <resolved-file>
git rebase --continue       # or: git merge --continue / git cherry-pick --continue
```
- Understand `--ours` vs `--theirs` — and that they **invert** between merge and rebase:
  - In a **merge**, `ours` = your current branch, `theirs` = the branch being merged in.
  - In a **rebase**, "ours" = the branch you're rebasing **onto** (upstream), "theirs" = your replayed commits — because rebase replays your work on top.
- Take one side wholesale for a file (use only when certain): `git checkout --theirs path && git add path`.
- Bail out anytime: `git merge --abort` / `git rebase --abort` / `git cherry-pick --abort`.
- Enable `git config rerere.enabled true` so git remembers conflict resolutions and replays them on repeated rebases.

## git bisect — find the commit that introduced a regression
Manual binary search:
```bash
git bisect start
git bisect bad                 # current commit is broken
git bisect good v1.4.0         # this tag/sha was known-good
# git checks out a midpoint — test it, then mark:
git bisect good                # or: git bisect bad
# repeat until git names the first bad commit
git bisect reset               # return to where you started
```
**Automate it** — let git run a test command at each step and walk the whole range hands-free:
```bash
git bisect start HEAD v1.4.0          # bad ... good in one line
git bisect run npm test -- failing.spec.ts
git bisect reset
```
The `run` command's exit code drives it: `0` = good, `1–124/126/127` = bad, `125` = skip (untestable commit). Use a script that exits non-zero ONLY on the specific regression, not on unrelated failures.

## reflog — recover "lost" commits
The single most valuable recovery tool. Every HEAD move is logged:
```bash
git reflog                      # HEAD@{0}, HEAD@{1}, ... with the op that caused each
git reflog show <branch>        # per-branch history
```
Recover after a bad reset/rebase/amend or a deleted branch:
```bash
git reset --hard HEAD@{2}        # restore working state to a prior point
git switch -c rescue <sha>       # rebuild a deleted branch from its last reflog sha
git cherry-pick <sha>            # pull back one specific lost commit
```
If reflog is pruned, `git fsck --no-reflogs --lost-found` surfaces dangling commits.

## git worktree — parallel branches, no stashing
Run a hotfix or review without disturbing your in-progress branch — separate working dirs sharing one repo:
```bash
git worktree add ../proj-hotfix fix/urgent   # new dir on a new branch
git worktree add ../proj-review origin/main  # detached checkout to inspect
git worktree list
git worktree remove ../proj-hotfix           # clean up when done
```
Each worktree has its own index/HEAD; a branch can be checked out in only one worktree at a time. Beats `git stash` thrash when juggling two tasks.

## stash — shelve work-in-progress
```bash
git stash push -m "wip: cart refactor"   # shelve tracked changes
git stash push -u                        # include untracked files
git stash list
git stash pop                            # reapply newest + drop it
git stash apply stash@{1}                # reapply a specific one, keep it
git stash drop stash@{1}
```
Prefer a quick WIP commit + later `--fixup` over deep stash stacks — stashes are easy to forget.

## cherry-pick — port a specific commit
```bash
git cherry-pick <sha>          # apply that commit's change here
git cherry-pick -x <sha>       # appends "(cherry picked from commit <sha>)" — keep traceability across branches
git cherry-pick A^..B          # a range (A exclusive .. B inclusive)
```
Always use `-x` when porting between long-lived branches so the origin is auditable.

## .gitignore discipline
- Ignore build output, deps, env, local state: `node_modules/`, `dist/`, `.env`, `*.log`, `.DS_Store`, `__pycache__/`, `coverage/`.
- **NEVER** commit secrets, `.env`, keys, or credential files — that's also `gsd-ship`'s secret-scan gate, but catch it here first.
- Already tracked a file you now want ignored? Add it to `.gitignore`, then untrack without deleting: `git rm --cached path && git commit -m "chore: stop tracking path"`.
- Project-specific ignores → `.gitignore` (committed). Personal/editor noise → `.git/info/exclude` (local, uncommitted).

## Inspect & verify (before you commit or hand off)
```bash
git status -sb                 # compact status + branch tracking
git diff --staged              # exactly what will commit
git log --oneline --graph --decorate -20
git log -p -- path/to/file     # line-history of one file
git blame -L 40,60 path        # who/when/why for specific lines
git show <sha>                 # full diff of one commit
```

## Hand-off to gsd-ship
When the feature is built, history is clean, and tests pass — stop here. Invoke **`gsd-ship`** for the
final commit, PR creation (with its `gh`-or-fallback handling), and secret scan. git-flow gets you to a
clean, atomic, recoverable branch; gsd-ship takes it across the line.
