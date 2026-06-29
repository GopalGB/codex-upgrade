---
name: agentic-context-engineering
description: >-
  Treat the context window as a finite, degrading budget — curate what's in it via just-in-time retrieval over stuffing, compaction/summarization of long histories, structured external notes, and sub-agent isolation. Use on long agent loops, multi-turn sessions, or large documents where 'context rot' and lost-in-the-middle degrade quality.
---

# agentic-context-engineering

Context is a **finite resource with diminishing returns** — as a window fills, models attend worse ("context rot"), miss the middle, and slow down. Context engineering is the discipline of curating the *smallest set of high-signal tokens* that lets the agent take the next correct action, rather than stuffing in everything that might be relevant. More context is not better; the *right* context is.

The core moves: **just-in-time retrieval** — load data when a step needs it (search, open the file, call the tool) instead of front-loading the whole corpus; keep lightweight identifiers (paths, IDs, queries) and hydrate on demand. **Compaction** — when a history grows long, summarize the resolved parts into a dense state note and drop the raw transcript, keeping decisions/open-threads and shedding the chatter. **External memory** — persist durable state to a scratchpad/file/store the agent re-reads, so knowledge survives a context reset. **Sub-agent isolation** — push deep exploration into sub-agents that return only distilled findings, sparing the main window.

Structure what remains: put stable instructions up front (cache-friendly), the live task state where the model will look, and trim tool outputs to the fields that matter (paginate/summarize large blobs). Order matters — prefer recency for what's volatile, stability for what's cached. Measure: if quality degrades as a session runs long, you have a context problem, not a model problem — compact, retrieve, and isolate rather than just upgrading the model.

**Tools:** context = finite budget (beware context rot / lost-in-middle) · JIT retrieval over stuffing · compaction/summarize long history · external memory survives resets · sub-agent isolation · trim tool outputs · stable-prompt-up-front for caching
