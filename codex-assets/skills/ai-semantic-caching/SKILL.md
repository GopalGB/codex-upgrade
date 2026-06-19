---
name: ai-semantic-caching
description: >-
  Cache LLM responses by meaning, not exact string: embedding-similarity lookup, threshold tuning, TTL/invalidation, and the false-hit risk — use to cut cost/latency on repetitive or paraphrased queries.
---

# ai-semantic-caching

Exact-match caching misses paraphrases ('reset password' vs 'how do I change my password'). Semantic cache embeds the incoming query, does a vector similarity lookup against cached query→response pairs, and returns the stored response if similarity ≥ threshold. Two-tier is best: try exact-match (hash) first (free, zero false hits), then semantic. The threshold is the critical, dangerous knob — too low returns WRONG answers for merely-similar-but-different questions (a stale/incorrect hit is worse than a cache miss); tune it on labeled query pairs and start conservative (high threshold). Scope the cache key by anything that changes the answer (user/tenant, retrieved context version, model, system prompt) or you'll serve cross-user or stale results. Set TTL and invalidate when underlying data changes (critical for RAG-backed answers). Tools: GPTCache, or a vector store + your own logic. Don't cache personalized, time-sensitive, or stochastic-by-design outputs. Common mistake: a single global cache with a loose threshold that confidently returns a near-neighbor's answer to a different question — log hits and sample them for correctness.

**Tools:** embedding similarity cache, similarity threshold, vector store key, exact+semantic two-tier, TTL/invalidation, GPTCache
