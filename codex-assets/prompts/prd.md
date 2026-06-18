---
description: Write a PRD for a software / irreversible / auth-data-money build, then STOP for approval before any plan or code.
argument-hint: "[what you want built]"
---
# /prompts:prd — PRD then approval (heavy-build gate)

For SOFTWARE, irreversible, or auth/data/money/migration work. Trivial and standard
non-trivial work uses the §C clarity 4-liner instead — don't run this for those.

1. **GROUND** (§F/§C): read `~/.codex/memory/{MEMORY,LESSONS}.md` + `.planning/{MEMORY,LESSONS}.md`,
   and the repo for what already exists (§D reuse ladder). Don't re-research a logged answer.
2. If WHAT/WHY is ambiguous, ask ONE sharp question first. Preserve every
   user-supplied identifier in `$ARGUMENTS` VERBATIM (§A.6) — the `What:` line is
   exactly where a "Gemma 4 → Gemma 3" silent substitution would otherwise creep in.
3. Write `.planning/PRD.md`:

   ```
   # PRD: <name>
   What:    <one sentence — the exact thing; user's words/identifiers verbatim>
   Why:     <the real problem / who hurts without it>
   Success: <2-5 checkable bullets — a test passes / behavior works / number hit>
   Scope:   <in>
   Out:     <explicitly NOT this>
   Risks & security layers: <failure modes; authz at boundary, input validation,
            secrets via env, data exposure, clean layering — pre-fill from §K>
   Open questions: <blockers needing the user, or "none">
   ---
   APPROVAL: reply `approved` / `go` to proceed to /plan, or correct anything above.
   ```
4. Emit `STATUS: AWAITING_APPROVAL` and **STOP** — make NO further tool calls. Your
   turn is over. On `approved`/`go`, proceed to `/plan` (§C). A reply that edits the
   PRD is a CORRECTION → patch it, re-emit `AWAITING_APPROVAL`, stop again.
