---
name: agentic-prompt-chaining
description: >-
  Decompose a task into a fixed sequence of LLM calls where each step's output feeds the next, with programmatic gates between steps. Use when a task cleanly splits into ordered subtasks and you want higher accuracy per step by trading latency — the simplest, most reliable workflow pattern.
---

# agentic-prompt-chaining

Prompt chaining splits a task into a **fixed sequence** of LLM calls: step 1's output becomes step 2's input, and so on. Each call does one narrow thing well, which raises accuracy versus asking a single prompt to do everything at once. You trade latency (more sequential calls) for reliability and control. This is the workflow to reach for first whenever a task has obvious ordered stages — e.g. *outline → draft → polish*, or *extract fields → validate → format*.

The power comes from **gates between steps** — plain code (not the model) that checks the intermediate result and decides whether to proceed, retry, or bail. After "generate outline", assert it has the required sections before drafting; after "extract JSON", validate the schema before the next call consumes it. Gates keep an early error from compounding through the chain, and they're where you put deterministic logic the model shouldn't be guessing at.

Keep each link single-purpose and pass forward only what the next step needs (not the whole transcript) to control cost and context. Chaining is the right call when **reliability matters more than latency** and the decomposition is known ahead of time; if a step's path depends on the input, add a routing step rather than branching inside one mega-prompt. When steps are independent rather than ordered, parallelize them instead of chaining.

**Tools:** fixed ordered LLM calls · one narrow job per step · programmatic gates between steps (validate/retry/bail) · pass only what's needed forward · accuracy-over-latency · known decomposition
