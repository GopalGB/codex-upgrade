---
name: sde-idempotency
description: >-
  Make retries safe - idempotency keys, dedup stores, and designing operations that survive at-least-once delivery and client retries.
---

# sde-idempotency

In distributed systems, requests get retried (timeouts, queue at-least-once delivery, flaky networks), so the same operation can arrive twice. **Idempotent** means repeating it has the same effect as doing it once. GET/PUT/DELETE are naturally idempotent; POST (create, charge) is not - and that's where double-charges happen. **The pattern for POST**: client sends an **Idempotency-Key** (UUID) header; server records key -> result in a store with a TTL; on a duplicate key, return the stored result instead of re-executing. Wrap the check+execute in a transaction or use an atomic conditional insert so two concurrent retries don't both run. For internal writes, prefer **upserts** (INSERT ... ON CONFLICT) and **conditional updates** (compare-and-set on a version) over blind inserts. For queue consumers, dedupe on message ID. **Pitfall**: storing the idempotency record only after the side effect completes - a crash between the side effect and the record means the retry runs it again; record the in-progress key first, then execute, then mark complete (or use a single atomic transaction). Idempotency is how you get exactly-once *effects* on top of at-least-once *delivery*.

**Tools:** idempotency keys, upsert, dedup table, exactly-once illusion, conditional writes
