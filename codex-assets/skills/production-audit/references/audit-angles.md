# Audit angles — the 24 lenses

Sweep each lens as an independent pass. Different lenses catch different defects on
the same code, so run diverse angles and repeat until two consecutive passes find
nothing new. Each finding must be verified against real `file:line` before it counts.

1. **Subsystem sweep** — Walk each system end-to-end, tracing entry point → logic → storage → back. Find the gaps between layers.
2. **Attack-class** — Pick one vulnerability category (IDOR, injection, hardcoded secrets, auth bypass, SSRF) and hunt it *everywhere* in one pass.
3. **Claim-vs-code** — Verify every documented promise (README, comments, names, tests) against the actual implementation. Names lie; code doesn't.
4. **Data-shape** — Exercise key flows at the extremes: empty sets, nulls, unicode/emoji, very long strings, huge datasets, negative/zero, duplicates.
5. **Platform-divergence & responsiveness** — Compare behavior across web/mobile/CLI/OS; test layout at every width and both light/dark.
6. **Lifecycle** — Follow an entity through its whole life: signup, normal use, plan/role change, member removal, deactivation, deletion, re-creation.
7. **Write-path integrity** — Ensure external/state writes are idempotent and atomic; no partial-write windows, no unprotected read-modify-write gaps.
8. **Failure-mode** — Test what happens when a dependency times out, errors, returns corrupted/partial data, or is missing. Graceful vs cascade.
9. **Dead-and-stale** — Outdated docs, removed features still referenced, `TODO`/`FIXME` in prod paths, drifted migrations, dead code, stale versions/dates.
10. **Gate-run & gate-escape** — Actually run all CI checks/tests/linters; then find defects that slip through via suppressions, `# noqa`, skipped tests, ignored dirs.
11. **Performance** — N+1 queries, missing indexes, unbounded fetches/loops, O(n²) on hot paths, redundant work, large payloads, Web Vitals.
12. **A11y & UX-jank** — Focus order, ARIA/labels, contrast, keyboard nav, animation/motion, and guards on destructive actions (confirm before delete).
13. **Content & copy** — Typos, placeholder/lorem text, jargon, inconsistent numbers/terms across pages, broken/wrong links.
14. **Asset & icon integrity** — Images/icons/favicons actually load, correct paths, alt text present, no 404'd or oversized assets.
15. **Connection & wiring** — Frontend↔API calls line up, DB/connection pools sized and closed, third-party integrations wired with the right creds/endpoints.
16. **LLM & prompt quality** — Prompt correctness, output parsing/validation, token/context caps, injection resistance, fallback on model error, cost caps.
17. **Auth & permissions deep-dive** — Build the full role × action matrix and verify each cell **server-side**; no client-only checks; default-deny.
18. **Resource leaks & long-running drift** — Memory/handle/connection/file-descriptor leaks; unbounded caches/queues; state that degrades over uptime.
19. **Observability & operations** — Errors are captured, critical paths logged with context, metrics exist, startup validates, shutdown is graceful.
20. **Abuse & limits** — Unbounded/expensive operations without limits: auth endpoints (brute force), uploads, exports, API calls, quotas, rate limits.
21. **Config & environment** — Required env vars validated at boot; no dev defaults / debug flags / test creds leaking into production; secrets not in code.
22. **Dependency & supply-chain** — Known CVEs, deprecated/unmaintained packages, version drift, lockfile integrity, license issues.
23. **Caching correctness** — Cache key scoping, invalidation, tenant/user isolation (no cross-tenant leaks), TTLs, auth/permission cache expiry.
24. **Concurrency & races** — Double-submit/double-click, concurrent edits, lost updates, TOCTOU; enforce atomicity/locking/optimistic-concurrency.
