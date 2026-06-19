---
name: ai-agent-memory
description: >-
  Give agents memory across turns and sessions: working vs episodic vs semantic memory, summarization buffers, vector recall, and write/forget policies — use when an agent must remember beyond one context window.
---

# ai-agent-memory

Separate memory tiers. WORKING memory = the live context window (recent turns) — bounded; manage with a rolling summary buffer (compress old turns into a running summary so the gist survives eviction). EPISODIC memory = past interactions/events, stored and retrieved by embedding similarity when relevant ('what did we decide last week'). SEMANTIC memory = distilled facts/preferences about the user/domain, written as discrete statements and retrieved or pinned. The retrieval mechanism is the whole game: score candidate memories by relevance (embedding) × recency × importance, and inject only the top few into context — dumping all memory defeats the purpose and rots the context. Decide WHAT to write (don't persist every token; extract durable facts) and WHEN to forget (TTL/decay, or supersede contradicting facts). Tools/frameworks: Letta/MemGPT-style self-editing memory, Mem0, or a plain vector store + a write policy. Pitfalls: stale memories contradicting new info (reconcile on write), and unbounded growth slowing retrieval. Common mistake: treating the context window as memory and re-sending the whole history — summarize and retrieve instead. Make memory writes auditable.

**Tools:** summary buffer, vector store recall, episodic/semantic split, recency+relevance scoring, memory write/eviction policy
