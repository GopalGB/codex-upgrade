---
name: agentic-failure-recovery
description: >-
  Make agent loops resilient — retry with backoff on transient errors, fall back through a chain when a step fails, reflect on errors to self-correct, and bound everything so a stuck agent can't loop or burn budget forever. Use on any agent that calls flaky tools/APIs or runs unattended, where a single failure shouldn't sink the whole run.
---

# agentic-failure-recovery

Agents fail constantly at the edges — a flaky API, a timeout, a tool returning garbage, a step that doesn't converge — and the difference between a toy and a system is how it recovers. Layer your defenses. **Retry with exponential backoff + jitter** on transient faults (timeouts, 429/503, network) — but only on idempotent operations, and cap the attempts. **Fall back** when a step keeps failing: a cheaper/alternate tool, a degraded-but-useful result, or a clean escalation to a human — a fallback chain beats a hard crash.

Use the agent's own loop for **error reflection**: feed a structured error back ("tool X failed: <reason>") so the model can adjust its approach rather than repeating the same failing call. This is powerful but dangerous — without limits an agent will retry the identical action forever. So **bound everything**: max iterations, max tool calls, max tokens/cost, and a wall-clock timeout, with a defined behavior when a limit is hit (stop and report the best partial result + what's blocked). Detect loops (same action/observation repeating) and break out.

Fail **loud and legibly**: capture what failed, where, and why into the run's state/trace so a human or the next session can diagnose — never swallow an error into a silent dead end or a confident hallucinated success. Distinguish *recoverable* (retry/fallback) from *terminal* (stop and surface) failures and handle each deliberately. Pair with durable state so a crash mid-run resumes instead of restarting. The goal: an agent that bends under failure and reports honestly, not one that either crashes or pretends it succeeded.

**Tools:** retry+backoff+jitter on idempotent transients · fallback chains over hard crash · error-reflection back into the loop · bound iterations/calls/tokens/time · detect + break repeat loops · fail loud into the trace · recoverable vs terminal
