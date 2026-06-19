---
name: m365-graph-batch-requests
description: >-
  Combine up to 20 Graph calls into one $batch request to cut round-trips and latency — when issuing many small Graph calls
---

# m365-graph-batch-requests

POST to `https://graph.microsoft.com/v1.0/$batch` with a body listing up to **20** sub-requests:
```json
{"requests":[
  {"id":"1","method":"GET","url":"/me"},
  {"id":"2","method":"GET","url":"/me/messages?$top=5"},
  {"id":"3","method":"POST","url":"/me/events","headers":{"Content-Type":"application/json"},"body":{...},"dependsOn":["2"]}
]}
```
The response is a `responses` array — match by `id` (order is NOT guaranteed). Sub-request `url`s are **relative** (no host, no /v1.0). Sequence dependent calls with `dependsOn`.

Pitfall: the 20-request cap is hard — chunk larger sets. Pitfall 2: each sub-request needs its own `Content-Type` header in `headers` and an inline JSON `body` (object, not string) for writes. Pitfall 3: a 429 can come back on an *individual* sub-response while the batch itself returns 200 — inspect each sub-status, and a sub-request's `Retry-After` is in its own headers. Pitfall 4: `dependsOn` requires the referenced request to succeed; if it fails the dependent returns 424.

**Tools:** POST /$batch, JSON batching, id, dependsOn
