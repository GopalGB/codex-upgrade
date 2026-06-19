---
name: ai-cost-latency-optimization
description: >-
  Cut LLM cost and latency without wrecking quality: model right-sizing, prompt caching, batching, max-token caps, streaming, and distillation — use when bills or p95 latency are too high.
---

# ai-cost-latency-optimization

Cost is driven by tokens × price × calls; latency by output tokens (sequential generation) and TTFT. Levers, biggest first: (1) PROMPT CACHING — cache the stable prefix (system, tools, RAG context reused across calls) for ~75-90% cheaper cached-input reads; structure prompts stable-first to maximize hits. (2) RIGHT-SIZE THE MODEL — route easy requests to a small/cheap model, hard ones to a frontier model; most traffic doesn't need the biggest model. (3) BATCH API — non-interactive jobs (evals, bulk extraction) at ~50% off with relaxed latency. (4) CAP OUTPUT — output tokens dominate latency AND cost; set max_tokens and prompt for terse output (output is often 3-5x the input price). (5) STREAM — doesn't reduce cost but slashes perceived latency (first token fast). (6) SHRINK INPUT — compress/trim retrieved context, drop redundant few-shot once the model is reliable. (7) DISTILL — fine-tune a small model on the big model's outputs for a fixed task. Common mistake: optimizing input tokens while ignoring that OUTPUT tokens are pricier and the latency bottleneck. Measure p50/p95 and $/request, not averages.

**Tools:** prompt caching, Batch API (50% off), model tiering, max_tokens caps, streaming, request batching, output compression
