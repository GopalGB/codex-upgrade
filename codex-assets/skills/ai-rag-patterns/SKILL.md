---
name: ai-rag-patterns
description: >-
  Production RAG beyond naive retrieve-then-stuff: hybrid search, reranking, corrective/self-RAG, and query rewriting — use when naive RAG misses relevant docs or hallucinates over them.
---

# ai-rag-patterns

Naive RAG (embed query → top-k → stuff context) fails on keyword/acronym queries, returns irrelevant chunks, and answers anyway. Upgrade in layers: (1) HYBRID SEARCH — run BM25 (keyword) and dense (semantic) in parallel and fuse with Reciprocal Rank Fusion; catches exact terms dense misses. (2) RERANK — over-retrieve top-50, then a cross-encoder reranker (Cohere Rerank, bge-reranker) scores query-doc pairs jointly and keeps top-5; biggest single quality win. (3) QUERY TRANSFORM — rewrite conversational queries to standalone, decompose multi-part questions, or HyDE (generate a hypothetical answer, embed THAT). (4) CORRECTIVE/SELF-RAG — grade retrieved docs for relevance; if weak, rewrite the query or fall back to web search; let the model decide whether to retrieve at all and to cite. Always instruct: 'answer ONLY from context; if absent, say you don't know' and require inline citations to chunk ids. Common mistake: skipping reranking and blaming the LLM for hallucination when retrieval surfaced garbage — fix retrieval first. Measure retrieval (recall@k, MRR) separately from generation (faithfulness).

**Tools:** hybrid BM25+dense (RRF), cross-encoder rerank, Corrective-RAG, Self-RAG, HyDE, query decomposition
