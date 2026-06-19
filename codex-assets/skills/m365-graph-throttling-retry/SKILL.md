---
name: m365-graph-throttling-retry
description: >-
  Handle Graph 429 throttling with Retry-After and exponential backoff so automations survive rate limits — when bulk-calling Graph
---

# m365-graph-throttling-retry

Graph enforces per-app, per-tenant, per-service limits. When exceeded it returns **429 Too Many Requests** with a **`Retry-After`** header (seconds) — honor it exactly; do not retry sooner. Also retry on 503/504 (transient). Pattern: respect `Retry-After` when present, else exponential backoff with jitter, cap at ~5 retries.

```python
for attempt in range(5):
    r = requests.get(url, headers=h)
    if r.status_code not in (429,503,504): break
    wait = int(r.headers.get('Retry-After', 2**attempt))
    time.sleep(wait + random.random())
```

Pitfall: ignoring `Retry-After` and hammering with fixed retries gets your app's traffic pattern flagged and limits tightened — the header is authoritative. Pitfall 2: throttling is per-resource (Outlook mailbox limits differ from SharePoint) — back off the *specific* call, don't pause everything. Pitfall 3: reduce calls in the first place — use `$select`, `$batch`, and delta queries instead of polling; the SDKs (`GraphClientFactory` with the built-in retry handler) handle 429 automatically, so prefer them over hand-rolled HTTP.

**Tools:** 429, Retry-After header, exponential backoff, x-ms-throttle-information
