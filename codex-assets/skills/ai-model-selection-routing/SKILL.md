---
name: ai-model-selection-routing
description: >-
  Pick and route between LLMs by task: capability/cost/latency/context tradeoffs, prompt-based vs learned routers, cascades, and fallback chains — use to match each request to the cheapest model that can do it.
---

# ai-model-selection-routing

There's no single best model — match each request to the cheapest one that clears the quality bar. Build a capability matrix per task (reasoning, coding, vision, long-context, tool-use, multilingual) × cost × latency × context size, and decide per request type. ROUTING approaches: rule/heuristic (route by detected task type or input length), classifier/embedding router (a small model/classifier predicts which tier is needed), or CASCADE (try cheap model first; if a self-check/verifier judges low confidence, escalate to the strong model) — cascades capture most savings since most queries are easy. Always have a FALLBACK chain across providers for outages/rate-limits/timeouts (primary → secondary → degraded), with retries and circuit breakers. Pin exact model IDs (don't let an alias silently swap models) and re-run your eval suite on any model change — a new model can regress your specific prompts even if benchmarks improve. Gate swaps behind A/B + eval. Common mistake: defaulting everything to the biggest model 'to be safe' (10-50x overspend) or hot-swapping models without re-evaluating prompts that were tuned for the old one.

**Tools:** model tiering, classifier/embedding router, LLM cascade, fallback chain, capability matrix, A/B + eval gating
