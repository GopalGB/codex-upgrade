---
name: pa-retry-policy-timeout
description: >-
  Per-action retry policy (default/none/fixed/exponential), action timeout (ISO 8601 duration), and handling 429 throttling
---

# pa-retry-policy-timeout

Each action has resiliency settings under ... > **Settings**. **Retry Policy**: **Default** (exponential, ~4 retries on 408/429/5xx), **None** (fail immediately - use for non-idempotent actions where a retry double-posts), **Fixed Interval** (Count + ISO 8601 interval like `PT10S`), **Exponential** (Count + Interval + Min/Max, backs off `PT5S`,`PT10S`,`PT20S`...). Retries fire only on retryable status (429, 5xx, 408) - a 400/401/404 is not retried (fix the request). **Timeout** caps how long an action waits, also ISO 8601 (`PT1H`, `PT30M`); pair with run-after **has timed out** to catch hangs. For **429 throttling**, exponential retry + honoring **Retry-After** is correct - managed connectors respect it automatically; for custom/HTTP add a manual **Delay** between batches. Pitfalls: Default retry on a record-creating POST can duplicate rows on a flaky network - set retry None and handle failure, or make it idempotent with a dedupe key; a tight Do until poll loop without a Delay hammers the API and trips throttling - add a `PT15S` Delay inside.

**Tools:** Retry Policy (Default/None/Fixed/Exponential), action Timeout, ISO 8601 (PT10S/PT1H), Delay, Delay until, Retry-After
