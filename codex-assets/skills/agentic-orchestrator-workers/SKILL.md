---
name: agentic-orchestrator-workers
description: >-
  Use a lead orchestrator agent that dynamically decomposes a task, dispatches subtasks to worker sub-agents (often in parallel, each with its own context), and synthesizes their results. Use for complex, open-ended tasks where you can't predict the subtasks up front — research sweeps, multi-file changes, broad audits.
---

# agentic-orchestrator-workers

This is parallelization's dynamic cousin: a **lead/orchestrator** agent looks at the task, decides *at runtime* how to break it up, spins up **worker** sub-agents to handle the pieces, and then **synthesizes** their outputs into the final answer. The difference from fixed parallelization is that the subtasks aren't predetermined — the orchestrator invents them based on the specific input, which is exactly what you need for open-ended work (research a question across many angles, refactor an unknown set of files, audit a codebase).

Each worker runs in its **own isolated context** with a tightly scoped instruction and returns a compact, structured result. This is the key efficiency: workers explore in parallel and in depth without polluting each other's or the orchestrator's context window, and the orchestrator only ever sees their distilled findings, not their full transcripts. Give each worker a clear objective, the inputs it needs, an output contract, and a boundary ("only this file / only this sub-question"). Dedicate real effort to the orchestrator's **synthesis** step — merging, deduping, and resolving conflicts across workers is where quality is won or lost.

It costs more tokens than a single agent (you're running several), so reserve it for tasks whose value justifies the spend and that genuinely parallelize. Watch the failure modes: workers given overlapping scopes duplicate work; vague objectives produce unusable results; and an orchestrator that just concatenates worker outputs isn't synthesizing. Cap the number of workers and the depth, and have the orchestrator decide when it has enough to stop.

**Tools:** orchestrator decomposes at runtime · workers in isolated contexts with scoped objectives + output contracts · parallel explore, distilled returns · invest in synthesis (merge/dedup/resolve) · non-overlapping scopes · cap workers + depth
