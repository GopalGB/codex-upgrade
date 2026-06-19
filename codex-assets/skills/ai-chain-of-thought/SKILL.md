---
name: ai-chain-of-thought
description: >-
  Elicit step-by-step reasoning for math, logic, and multi-hop tasks via CoT, self-consistency voting, and reasoning-model controls — use when the model rushes to a wrong final answer.
---

# ai-chain-of-thought

For multi-step problems, instruct the model to reason before answering ('think step by step', or better, give a structured plan: 'first identify X, then compute Y, then conclude'). CoT trades tokens/latency for accuracy on arithmetic, logic, and multi-hop QA. Force separation of reasoning and answer (reasoning in `<thinking>` tags, final answer in `<answer>`) so you can parse the answer cleanly and optionally hide the reasoning from users. Self-consistency: sample n=5 reasoning chains at temperature 0.5-0.8 and majority-vote the final answers — 5-15% accuracy gains on reasoning benchmarks at 5x cost. In 2026, dedicated reasoning models (o-series, Claude extended-thinking, Gemini thinking) do CoT internally; control them with reasoning-effort/thinking-budget params instead of prompting 'think harder' — and DON'T add manual CoT on top of a reasoning model, it can hurt. Common mistake: parsing the final answer with a naive regex that grabs a number from the reasoning instead of the conclusion — always demand a delimited final answer. Don't use CoT for simple lookups; it just adds cost and latency.

**Tools:** CoT, self-consistency (n-sample majority vote), reasoning-effort params, scratchpad
