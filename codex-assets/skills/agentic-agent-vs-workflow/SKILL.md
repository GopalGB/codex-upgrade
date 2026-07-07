---
name: agentic-agent-vs-workflow
description: >-
  Choose between a deterministic workflow and an autonomous agent before building — predictability, cost, and testability vs flexibility. Use when designing any LLM-powered system so you start with the simplest pattern that works and add agency only when the task genuinely needs it.
---

# agentic-agent-vs-workflow

There are two architectures, and most teams reach for the wrong one. **Workflows** orchestrate LLMs and tools through *predefined code paths* — you wrote the control flow, the model fills in the steps. They're predictable, testable, cheap, and easy to debug. **Agents** let the model *direct its own process* — choosing which tools to call and in what order, looping until done. They're flexible but slower, costlier, and harder to reason about when they go wrong.

Start with the simplest thing that could work and only add complexity when it demonstrably helps. A single well-prompted LLM call with retrieval and a few in-context examples beats a multi-agent system for the majority of tasks. If the task decomposes into a fixed set of steps, build a **workflow** (chaining, routing, parallelization). Reach for a true **agent** only when you can't predict the steps in advance — the path depends on the input at runtime and the model must adapt, use feedback, and decide when it's finished.

The litmus test: *if you can draw the flowchart, build the workflow; if the flowchart's shape depends on the input, consider an agent.* Agency is a cost — latency, tokens, unpredictability, a wider failure surface — that you pay for flexibility; buy it deliberately. Whatever you build, instrument it, cap the loops, and define explicit stop conditions so an agent can't run away. Frameworks (LangGraph, the Agents SDK, etc.) help, but add abstraction layers that hide the prompt and make debugging harder — understand the underlying calls before adopting one.

**Tools:** workflow (predefined paths) vs agent (model-directed) · start simplest · add agency only when steps are unpredictable · "can you draw the flowchart?" test · cap loops + stop conditions · don't over-frameworkize
