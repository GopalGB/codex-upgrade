---
name: agent-builder
description: >-
  Build PRODUCTION agentic systems — design for the failure path, eval + observe from
  commit one, one reliable agent before any "crew". Use for: building an AI agent,
  tool/function-calling design, multi-agent orchestration, agent memory, agent eval,
  MCP/A2A. Triggers: "build an agent", "agentic system", "multi-agent", "LangGraph",
  "OpenAI Agents SDK", "Pydantic AI", "CrewAI", "smolagents", "MCP server", "A2A",
  "tool calling", "agent memory", "agent eval", "my agent loops / breaks".
---

# agent-builder — reliable agents, not demos (verified 2026)

Compounding error is the enemy: 95%/step over 20 steps ≈ **36%** end-to-end. Reliability
= fewer decisions + verification + observability, not more agents.

## Absorb these repos (current, maintained)
- **langchain-ai/langgraph** (~126k) https://github.com/langchain-ai/langgraph — the
  default for stateful/durable graph agents: checkpointing, human-in-the-loop interrupts,
  time-travel. + **deepagents** (long-horizon harness: planner + virtual FS + subagents).
- **openai/openai-agents-python** (~17k) — lightweight, provider-agnostic (100+ LLMs);
  Agents, handoffs, agents-as-tools, guardrails.
- **pydantic/pydantic-ai** (~17k) https://github.com/pydantic/pydantic-ai — type-safe:
  Pydantic-validated tool args + structured outputs with retry-on-validation-failure.
- **huggingface/smolagents** (~22k) — CodeAgents: the agent writes Python AS its actions
  (fewer round-trips, lower error rate) — reach for it on composable tasks.
- **crewAIInc/crewAI** (~48k) — role-based multi-agent (roles/tasks/crews/process).
- **modelcontextprotocol** (~70k org) — **MCP** = the standard agent→tool protocol; define
  tools as MCP servers so every client reuses them.
- **a2aproject/A2A** (~20k) + **google/adk-python** (~12k) — **A2A** = agent→agent protocol
  (use MCP for tools, A2A for agents — at the correct layer).
- **langfuse/langfuse** (~28k) https://github.com/langfuse/langfuse — OSS, self-host, OTel
  tracing/evals/cost. (Or LangSmith + LangGraph Studio — best agent debugger.)
- **confident-ai/deepeval** (~15k) — pytest-style agent eval (tool-correctness, task-
  completion) → CI gate. + **UKGovernmentBEIS/inspect_ai** for rigorous agentic evals.
- ⚠ **AutoGen & Semantic Kernel are MAINTENANCE-ONLY (Apr 2026)** — folded into Microsoft
  Agent Framework 1.0. Don't start new builds on them; old tutorials are stale.

## Canonical approach
1. **One reliable agent FIRST.** Add agents only for true parallelism/isolation. Multi-
   agent multiplies tokens + coordination failure modes — it's not a reliability fix.
2. **Design the failure path first** — recursion/step limits, `handle_tool_errors=True`
   (feed tool errors BACK as observations to self-correct), retries w/ backoff, fallbacks.
3. **Tools are prompts** — tool descriptions matter MORE than implementation; typed/strict
   schemas; rich, actionable error messages. Define them as MCP servers.
4. **Code-as-action** (smolagents) for composable tasks — one code block loops/branches/
   nests tool calls, cutting round-trips, latency, cost, and error rate vs JSON tool-calls.
5. **Context engineering, not prompt engineering** — Write (external scratchpad/checkpoints)
   · Select (JIT tool/context loading) · Compress (compaction/summary). Respect **context
   rot**: recall degrades as the window grows, before the hard limit. Fewer high-signal
   tokens win.
6. **Orchestration shape** — Manager (agents-as-tools, central, traceable) vs Handoffs
   (peer transfer, autonomous, harder to debug). Start with Manager.
7. **Eval from commit one** — domain golden set, DeepEval CI gate + Inspect AI; never trust
   a benchmark score (2026 agent benchmarks are reward-hackable; top agents still <50% on
   hard real-world tasks).
8. **Observe from commit one** — Langfuse/LangSmith trace every step/token/tool/cost.
9. **Budget** — cap steps/timeouts, route sub-tasks to cheaper models, watch cost in traces.

## Expert vs generic
Generic: happy-path demo, jumps to a 5-agent crew, no evals/observability, terse tool
descriptions + raw stack-trace errors, stuffs whole history every turn, trusts tool/web
output, uses 2024-25 AutoGen tutorials. Expert: failure-path-first, one agent first, evals
+ traces from day one, tools-as-prompts, context engineering, untrusted-content barriers,
current frameworks.

## Pitfalls (incl. stale-knowledge + security)
Uncontrolled loops → recursion error (fix the tool-error message/stop condition, don't
just raise the limit) · compounding error over long chains · building on AutoGen/Semantic
Kernel (maintenance-only) · context rot · **prompt injection via tool/MCP/web output** —
mandatory data barriers + treat external content as untrusted + split read-sensitive from
write-outbound (two-loop prohibition) + human-in-the-loop on irreversible actions ·
over-orchestration before one agent works.

## Guardrails
Confirm before outbound/irreversible tool calls. For the retrieval side see `rag-engineer`;
for model/serving see `ml-engineer`; for parallel multi-angle analysis use `swarm`.
