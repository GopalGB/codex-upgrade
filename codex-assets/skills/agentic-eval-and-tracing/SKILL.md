---
name: agentic-eval-and-tracing
description: >-
  Evaluate and observe agents, not just prompts — score end-state success and trajectory quality, trace every step (calls, tools, tokens, latency) with spans, and gate changes behind a regression eval. Use before shipping or changing any agent so you measure whether it actually completes tasks instead of guessing from a few demos.
---

# agentic-eval-and-tracing

Agents are non-deterministic and multi-step, so "it worked when I tried it" is not evidence. You need two things: **evaluation** that measures task success, and **tracing** that shows you *why* a run went the way it did. Build a golden set of representative tasks with checkable success criteria and run the agent against it. Score on two axes: **end-state** (did it achieve the goal? — the metric that ultimately matters) and **trajectory** (did it take a sane path — right tools, no flailing, reasonable cost?), since two runs can both succeed while one is 5× the tokens.

**Trace everything.** Instrument each run as a tree of spans — LLM calls (prompt, response, tokens), tool calls (inputs, outputs, errors), timings, and the decisions between them — so you can replay a failure and see the exact step that broke. Without traces, debugging an agent is guesswork; with them, you find the bad tool result or the misrouted step in seconds. Capture cost and latency per run as first-class metrics, not afterthoughts.

Prefer **deterministic checks** (did the test pass, the file get created, the API return 200, the output match the schema) and reserve LLM-as-judge for fuzzy criteria — and when you use a judge, calibrate it against human labels and watch for its biases. Then make eval a **gate**: run it in CI on every prompt/model/tool change and block regressions, so improvements are real and you catch the change that quietly made things worse. Eval-driven development is to agents what test-driven development is to code.

**Tools:** golden task set with checkable criteria · score end-state + trajectory · trace runs as spans (calls/tools/tokens/latency) · cost+latency as first-class metrics · deterministic checks over LLM-judge (calibrate judges) · regression gate in CI
