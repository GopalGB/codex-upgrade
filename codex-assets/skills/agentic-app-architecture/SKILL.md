---
name: agentic-app-architecture
description: >-
  Architect an agentic application end-to-end — the core agent loop (gather context → act via tools → verify), a state/memory store, a tool layer, an eval harness, and a deployment with observability and guardrails. Use when building a real agent app (not a demo) and you need the pieces to fit into something reliable, debuggable, and shippable.
---

# agentic-app-architecture

A production agent app is a handful of well-separated parts around one **core loop**: gather just-enough context → decide and act through tools → verify the result → repeat until done or stopped. Build that loop explicitly and keep its pieces decoupled: a **model/provider layer** (swappable, so you're not welded to one API), a **tool layer** (well-designed ACIs, often MCP), a **state/memory store** (durable, the source of truth the loop reads/writes), and an **orchestration layer** that picks the right pattern — a fixed workflow where steps are predictable, an autonomous agent only where they aren't.

Wrap the loop in the operational essentials from day one, not as an afterthought: **observability** (trace every run as spans — calls, tools, tokens, latency), an **eval harness** (golden tasks + a regression gate in CI), **guardrails** (input/output validation, least-privilege tools, untrusted-content isolation, confirm-before-destructive), and **failure handling** (retry/backoff, fallbacks, bounded loops, durable resume). These are what separate an agent that demos from one you can run unattended. Treat cost/latency as first-class metrics with per-role model routing and prompt caching baked in.

Sequence the build to control risk: start with the simplest architecture that could work (often a single call or a short chain), get an eval harness and tracing in place early so you can measure, then add agency, sub-agents, or orchestration only where the evals show you need it. Keep a human at the high-blast-radius checkpoints. Resist premature framework lock-in — understand the raw calls first, adopt a framework when it earns its abstraction. The result is an app whose behavior you can see, test, bound, and improve — not a black box that works until it doesn't.

**Tools:** core loop (context→act→verify) · decoupled layers: model / tools / state / orchestration · observability + eval-gate + guardrails + failure-handling from day one · cost/latency first-class · start simplest, add agency where evals demand · human at high-blast-radius gates · avoid premature framework lock-in
