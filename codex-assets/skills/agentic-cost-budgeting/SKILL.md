---
name: agentic-cost-budgeting
description: >-
  Control token cost and latency in agentic systems — route each role to the cheapest capable model, cap sub-agent token budgets, cache stable context, and choose parallel vs sequential deliberately. Use when a multi-step or multi-agent system is too slow or expensive, since agents multiply calls and cost compounds fast.
---

# agentic-cost-budgeting

Agentic systems multiply LLM calls — loops, sub-agents, retries, evaluators — so cost and latency compound far faster than in a single-call app, and a naive multi-agent design can be 10–15× the tokens of one good prompt. Budget deliberately. **Right-size the model per role**: a small fast model for routing, classification, extraction, and simple workers; the large model only for the steps that genuinely need its reasoning. Per-role routing is usually the single biggest lever.

**Cap and cache.** Give each sub-agent and loop an explicit token/iteration budget so no single branch runs away, and degrade gracefully when a cap is hit. Use **prompt caching** for the stable prefix (system prompt, tools, fixed context) so repeated calls don't re-pay for it — structure prompts stable-part-first to maximize cache hits. Trim tool outputs and retrieved context to what's needed; oversized observations are silent cost. Set `max_tokens` to what the step actually requires.

Choose **parallel vs sequential** with cost in mind: parallelization cuts wall-clock latency but spends the tokens concurrently (you pay the same total, faster), while orchestrator-workers spend *more* total tokens for depth — justify that spend by the task's value. Reserve the expensive patterns (multi-agent, long eval loops, high-N voting) for high-value tasks; use a single call for the rest. Measure cost per task as a first-class metric alongside success, and watch for the pattern where a "smarter" architecture costs 5× for a 2% quality gain that wasn't worth it.

**Tools:** per-role model routing (small for easy) · explicit token/iteration budgets + graceful degrade · prompt-cache the stable prefix · trim tool/context outputs · set max_tokens · parallel=faster-not-cheaper, orchestration=more-tokens · cost-per-task as a metric
