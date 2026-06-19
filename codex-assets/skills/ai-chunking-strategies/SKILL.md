---
name: ai-chunking-strategies
description: >-
  Split documents for retrieval without destroying meaning: size/overlap tuning, semantic and structure-aware chunking, and contextual retrieval — use when retrieved chunks are fragmented or context-less.
---

# ai-chunking-strategies

Chunk size is the central RAG knob: too big dilutes the embedding (one vector for many topics → poor matches); too small loses context. Start ~256-512 tokens with 10-20% overlap so sentences spanning a boundary aren't orphaned. Prefer structure-aware splitting: recursive splitting on natural boundaries (headings → paragraphs → sentences) beats fixed character counts; for markdown/code/HTML, split on semantic units (sections, functions). Semantic chunking groups sentences by embedding similarity, breaking at topic shifts. Two power moves: PARENT-DOCUMENT retrieval — embed small chunks for precise matching but return the larger parent for context; and Anthropic's CONTEXTUAL RETRIEVAL — prepend an LLM-generated 1-2 sentence summary of how each chunk fits the whole doc before embedding (large retrieval-failure reductions). For tables/lists, never split mid-structure. Common mistake: one chunking config for all doc types — tune per corpus and verify by eyeballing what actually gets retrieved for real queries. Store metadata (source, page, section) on every chunk for filtering and citations.

**Tools:** recursive character splitting, token-based sizing, semantic chunking, parent-document/late-chunking, contextual retrieval
