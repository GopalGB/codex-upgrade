---
name: production-audit
description: >-
  Run an exhaustive, converge-until-clean production-readiness audit — sweep the codebase through 24 distinct lenses (security, data integrity, concurrency, perf, a11y, failure modes, ops, abuse, config, deps, LLM quality, claim-vs-code…), verify every finding against real file:line before reporting, and (in fix mode) fix in severity waves then re-verify. Use when the user wants to find — and optionally fix — ALL the real bugs, not a reassuring one-pass summary.
---

# production-audit

A single-pass "audit my code" finds ~15 issues and writes a reassuring summary. This does the opposite: it sweeps the product through **24 diverse lenses**, repeats until convergence, and **proves every finding against the real code** before it's allowed on the list. It is exhaustive by design and honest by construction — no hedging, no invented findings. (Ported from the open-source `production-audit` skill; lens catalog and taxonomy live in `references/`.)

**Core principle — trust what the code does, not what it's called.** A function named `sanitizeInput` that doesn't sanitize is a finding, not a guarantee. Verify claims (docs, comments, names, tests) against the implementation. Every candidate finding must **survive a refutation attempt**: trace it in the actual code, confirm the harm is real, and pin it to `file:line` (or `URL + selector`). If you can't prove it, you drop it — a false finding is worse than a missed one.

**Method — iterate diverse lenses to convergence:**
1. **Scope** the target (whole product, a subsystem/path, or one lens family) and map entry points → storage → back.
2. **Sweep** the lenses in `references/audit-angles.md` — each is a different angle (subsystem walk, one attack-class everywhere, claim-vs-code, data-shape extremes, lifecycle, write-path integrity, failure modes, perf, a11y, concurrency, config, deps, observability, abuse/limits, caching, resource leaks, LLM quality, …). Different lenses catch different bugs; a security pass and a perf pass see different defects on the same line.
3. **Verify** each candidate against the code; discard what doesn't survive.
4. **Converge:** keep running fresh, diverse passes and **stop only when two consecutive passes surface zero new findings.** One clean pass is not convergence.

**Output — a flat, actionable list, no summary theatre.** One row per finding, each pinned to a location, sorted by severity:
`[SEVERITY] [AREA] file:line — <concrete defect + the harm> — <specific fix>`
Severity (CRITICAL/HIGH/MEDIUM/LOW/IMPROVEMENT) and the ~18 area categories are defined in `references/finding-taxonomy.md`. Name the harm concretely; never hedge ("might possibly"). No reassuring preamble, no "overall the code looks good."

**Modes:**
- **discovery** (default, read-only) — audit and report the list; change nothing.
- **fix** — after the audit, fix in **waves by severity** (CRITICAL → HIGH → …), smallest correct diff per fix, then **re-verify**: re-run the relevant lens and the tests to confirm each fix holds and introduced no regression. Loop until the wave is clean.
- **scoped** — one lens family at depth (e.g. security only) or one subsystem/path.
- **docs-vs-code** — verify every documented claim against the implementation.

**Discipline:** be exhaustive but precise; prefer deterministic proof (run the test, trace the call, check the query) over assertion; report only what you verified; in fix mode, dogfood the craft-* rules (surgical diffs, verify-before-done, no-hallucinated-apis, self-review).

**Tools:** 24 lenses (`references/audit-angles.md`) · taxonomy + severity (`references/finding-taxonomy.md`) · verify-every-finding (survive refutation) · converge = 2 clean passes · `[SEV][AREA] file:line — defect — fix` · fix in severity waves + re-verify · trust code not names
