# Finding taxonomy — severity, categories, format

## Severity levels
- **CRITICAL** — Data loss/corruption; exploitable security breach; a core flow is broken; crashes on a primary path.
- **HIGH** — A claimed feature is broken; a security issue gated behind a single precondition; silent failure; limited-scope data leak.
- **MEDIUM** — Degraded or inconsistent behavior; edge-case failure with a workaround; a bounded performance problem.
- **LOW** — Minor bug; cosmetic defect; polish.
- **IMPROVEMENT** — A specific, concrete upgrade at a named location (not a vague "consider refactoring").

Rank by real-world impact, not by how interesting the bug is. When on the border between two levels, pick the higher only if the harm is genuinely reachable in production.

## Area categories (~18)
Bugs · Incomplete · Security · Build & gates · Stale content · Content quality ·
Inconsistency · UX & A11y · Performance · Data integrity · Reliability ·
Resource leaks · Operations & observability · Abuse & limits · Config & environment ·
Dependencies · LLM & AI quality · Promises-vs-reality

## Required fields per finding
- **Location** — `file:line` (or `URL + selector` for UI). Every finding is pinned; no location, no finding.
- **Category** — one of the area labels above.
- **Severity** — CRITICAL / HIGH / MEDIUM / LOW / IMPROVEMENT.
- **Evidence** — a specific, verifiable claim that **survives a refutation attempt** (you traced it in the code and confirmed the harm). Not a hunch.
- **Description** — names the harm concretely, no hedging.
- **Fix** — the specific change that resolves it.

## Report format
One row per finding, sorted by severity (CRITICAL first):

```
[SEVERITY] [AREA] path/to/file:line — <what's wrong and the concrete harm> — <the fix>
```

No preamble, no reassuring summary, no "overall this looks solid." Just the list.
A finding you can't prove against the code does not go on the list.
