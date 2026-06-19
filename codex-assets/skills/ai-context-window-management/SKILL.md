---
name: ai-context-window-management
description: >-
  Fit work into the context window and fight 'lost in the middle' / context rot: budgeting, summarization, retrieval over stuffing, and prompt/cache structuring — use on long docs, chats, or agent loops.
---

# ai-context-window-management

A big context window is not free attention: models lose info in the MIDDLE (lost-in-the-middle) and degrade as context fills (context rot) — more tokens ≠ better, and you pay per token. Budget the window explicitly: reserve room for output, then allocate the rest to system + retrieved context + history. Prefer RETRIEVE over STUFF — pull only the relevant chunks instead of dumping whole docs. For long docs that must be fully processed, use map-reduce (summarize chunks, then summarize summaries) or refine (iteratively update a running answer). Place the most important content at the START and END, never buried mid-context; restate the task at the end of a long prompt. In agent loops, prune/compact tool outputs and old turns aggressively (summarize, drop raw logs). Structure prompts for PROMPT CACHING: put stable content (system, tools, few-shot) first so it's cached, variable content last — big cost/latency wins on repeated calls. Common mistake: maxing out context 'to be safe' and getting worse, slower, pricier answers — curate ruthlessly. Measure quality vs context length on your task.

**Tools:** token budgeting, map-reduce/refine summarization, RAG vs stuff, position-aware placement, context pruning, prompt caching
