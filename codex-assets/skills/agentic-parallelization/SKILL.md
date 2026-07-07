---
name: agentic-parallelization
description: >-
  Run LLM subtasks concurrently and aggregate — either sectioning (split a task into independent parts done in parallel) or voting (run the same task N times and combine results). Use to cut wall-clock latency on independent work or to raise confidence/coverage through diverse or repeated attempts.
---

# agentic-parallelization

Parallelization runs multiple LLM calls **at the same time** and aggregates their outputs. It comes in two flavors. **Sectioning** splits a task into independent subtasks that run concurrently — e.g. evaluate code for security, performance, and style with one call each, then merge; or process 50 documents in parallel. Wall-clock time drops to the slowest single call instead of the sum. **Voting** runs the *same* task several times (varied prompts/temperature) and combines the results — majority vote, take-the-best, or union — to raise confidence or coverage where one shot is unreliable.

Use sectioning when subtasks are genuinely independent and a focused prompt per piece beats one prompt juggling all of them — separating concerns also improves quality, since each call attends to a single dimension. Use voting when a task has a high variance or a high cost of being wrong: catching vulnerabilities (union of findings), grading (median score), or generating options to choose among. Pick the aggregator deliberately — majority, max, union, or an LLM/code synthesizer — because it determines the failure mode.

The barrier is real: parallel calls must all finish before you aggregate, so the slowest one sets your latency and a single failure shouldn't sink the batch — make each call independent and tolerate a missing result (filter nulls, retry stragglers). When subtasks must run *in order* (each needs the last one's output), chain instead; when a lead agent must decide the subtasks at runtime, use orchestrator-workers.

**Tools:** sectioning (independent subtasks concurrently) · voting (same task N times, aggregate) · choose the aggregator (majority/max/union/synthesize) · latency = slowest call · tolerate partial failure · independent calls only
