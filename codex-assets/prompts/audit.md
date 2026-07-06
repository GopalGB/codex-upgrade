---
description: Exhaustive production-readiness audit (production-audit skill) — sweep 24 lenses to convergence, verify every finding against file:line, optionally fix in severity waves. Not a one-pass summary.
argument-hint: "[mode/scope: fix | security | docs-vs-code | <path>]"
---
# /prompts:audit — exhaustive production audit (production-audit skill)

Engage the **production-audit** skill. Find everything that's actually wrong, proven
against the real code — no reassuring one-pass summary, no invented findings.

Argument (optional): $ARGUMENTS
- empty        → full **discovery** audit, read-only (report the list, change nothing)
- `fix`        → audit, then fix in severity waves (CRITICAL→…), re-verify each fix
- `security`   → one lens family at depth
- `docs-vs-code` → verify every documented claim against the implementation
- `<path>`     → audit that subsystem/path only

Method (see the skill's `references/`):
1. **Scope** the target; map entry points → logic → storage → back.
2. **Sweep** the 24 lenses in `references/audit-angles.md` — diverse angles catch
   different defects on the same code.
3. **Verify** every candidate against real `file:line`; discard what can't survive a
   refutation attempt. Trust what the code does, not what it's named.
4. **Converge:** keep running fresh, diverse passes; **stop only when two consecutive
   passes find nothing new.** One clean pass is not convergence.
5. **Report** a flat list sorted by severity, one row each:
   `[SEVERITY] [AREA] file:line — defect + concrete harm — fix`
   (severity + areas: `references/finding-taxonomy.md`).
6. **fix mode only:** apply fixes wave-by-wave (smallest correct diff each), then
   re-run the relevant lens + the project's tests to confirm the fix holds with no
   regression. Loop until the wave is clean. Then emit the §J completion block.
