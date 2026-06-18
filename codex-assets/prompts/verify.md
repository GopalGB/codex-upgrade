---
description: Verify work is actually done — run the real tests/lint/build, read the output, emit the §J completion block. No green-by-assertion.
argument-hint: "[optional: scope, e.g. a file or feature]"
---
# /prompts:verify — prove it's done (AGENTS.md §C VERIFY + LESSON VERIFY_BEFORE_DONE)

Do NOT claim success by assertion. Actually run things and read the output.
Scope (optional): $ARGUMENTS — default to the whole current change.

1. **Re-read the goal:** `.planning/PRD.md` success criteria if present, else the
   task as stated. List the criteria you're verifying against.
2. **Detect + run the project's real checks** (whichever exist — don't invent):
   - JS/TS: `npm test` / `pnpm test`, `npm run lint`, `npm run build`, `tsc --noEmit`
   - Python: `pytest -q`, `ruff check .`, `mypy` (or the repo's configured commands)
   - Go: `go test ./...`, `go vet ./...`   · Rust: `cargo test`, `cargo clippy`
   - Run from the repo root; use the project's actual scripts (read package.json /
     pyproject.toml / Makefile first). Paste the real pass/fail counts.
3. **Diff check:** `git diff --stat` — every changed file is intentional and (if a
   PLAN exists) referenced in it. Flag any stray edits.
4. **Security/quick scan** when code changed: no secrets added (`git diff` for keys),
   inputs validated at new boundaries (§K).
5. **Emit the §J block** honestly:
   ```
   STATUS:   DONE | DONE_WITH_CONCERNS | BLOCKED
   CHANGED:  <files>
   TESTS:    <command> — <pass/fail counts, real output>
   GATE:     verify
   LESSON:   <TAG if a frustration/mistake surfaced, else none>
   NEXT:     <user action OR n/a>
   ```
   If anything is red or a check doesn't exist, say so — never report DONE on a
   guess. Red or unrun = NOT done.
