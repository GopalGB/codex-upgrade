---
name: ai-vector-search
description: >-
  Build and query a vector index for similarity search: ANN algorithms (HNSW/IVF), distance metrics, metadata filtering, and recall tuning — use to retrieve nearest neighbors at scale.
---

# ai-vector-search

Exact KNN is O(n·d) — too slow past ~100k vectors, so use Approximate Nearest Neighbor (ANN). HNSW (graph-based) is the default: high recall, fast queries, tune `M` (graph degree, build quality) and `ef_search` (query-time breadth — higher = better recall, slower). IVF partitions space into clusters (`nprobe` clusters searched); add Product Quantization (IVF-PQ) to compress vectors for huge datasets at some recall cost. Match the distance metric to your embeddings (cosine for normalized text embeddings; L2/dot otherwise) — mismatch silently wrecks results. Metadata filtering is the trap: post-filtering (ANN then filter) can return too few results if the filter is selective; pre-filtering is correct but needs index support (Qdrant/Weaviate/pgvector do filtered HNSW). Choose infra by scale: pgvector for <1-5M and 'already have Postgres'; Qdrant/Weaviate/Pinecone for larger or managed. Common mistake: trusting ANN as exact — measure recall@k against a brute-force ground truth on a sample, and raise ef_search until recall plateaus. Re-index after large deletions.

**Tools:** HNSW, IVF-PQ, pgvector, FAISS, Pinecone/Qdrant/Weaviate, ef_search/M, pre/post-filter
