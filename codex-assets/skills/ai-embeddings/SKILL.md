---
name: ai-embeddings
description: >-
  Turn text into vectors for semantic search, clustering, and dedup: model choice, dimensions, normalization, cosine similarity, and batching — use when you need meaning-based comparison, not keywords.
---

# ai-embeddings

Embeddings map text to dense vectors where semantic similarity ≈ geometric closeness (cosine). Pick a model by your tradeoff: OpenAI text-embedding-3-small (cheap, 1536d) vs -large (better, 3072d); open models like bge/e5/gte/nomic for self-hosting and multilingual. Matryoshka models let you truncate dimensions (3072→256) for cheaper storage with graceful quality loss — truncate then re-normalize. Normalize vectors to unit length so cosine similarity = dot product (faster). Critical: embed queries and documents with the SAME model and the SAME instruction prefix if the model uses asymmetric prefixes (e.g., e5 needs 'query:' / 'passage:'). Batch embedding calls (100s per request) to cut latency/cost. Embeddings have a token limit (~8k); chunk longer text first. Common mistakes: comparing vectors from two different models (meaningless), forgetting the asymmetric prefix (silently worse retrieval), and using cosine on un-normalized vectors when your index expects normalized. For dedup/clustering, embeddings + threshold beats exact match; tune the threshold on labeled pairs.

**Tools:** text-embedding-3, Matryoshka/dimension truncation, cosine similarity, L2 normalization, batching
