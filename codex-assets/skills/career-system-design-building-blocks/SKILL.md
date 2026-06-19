---
name: career-system-design-building-blocks
description: >-
  Know the canonical distributed-systems components and when each applies (caches, queues, sharding, replication, CDN, consensus) — use to back design choices with depth.
---

# career-system-design-building-blocks

System design rewards knowing the standard building blocks and their *tradeoffs*. **Load balancing:** L4 vs L7, round-robin/least-conn, plus consistent hashing to minimize remapping when nodes change. **Caching:** cache-aside (lazy), write-through, write-back; eviction (LRU/LFU); the hard part is invalidation and stampede (use TTL jitter + locks). **Databases:** SQL for transactions/joins/strong consistency; NoSQL (KV, doc, wide-column, graph) for scale/flexible schema. **Sharding** (horizontal partitioning) by hash or range — beware hot keys and cross-shard joins. **Replication:** leader-follower (read scaling, async = stale reads), multi-leader, quorum (R+W>N). **Async/queues:** Kafka/SQS to decouple, buffer spikes, enable retries; require idempotent consumers (idempotency keys) and dead-letter queues. **CDN** for static/edge. **Bloom filters** to avoid disk lookups for absent keys. **Rate limiting:** token bucket / sliding window.

**What top candidates do differently:** they map each block to a concrete real system (Kafka, Redis, Cassandra, DynamoDB, S3) and cite the failure mode it introduces, not just the benefit.

**Common mistake:** name-dropping a tech without its tradeoff (adding Redis but never addressing invalidation; adding a queue but ignoring exactly-once/duplicate delivery; sharding without a hot-key plan). Depth = benefit + cost + failure mode for every component.

**Tools:** consistent hashing, cache-aside, Kafka, leader-follower replication, read replicas, bloom filters, idempotency keys
