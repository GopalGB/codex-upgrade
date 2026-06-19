---
name: sde-sharding-partitioning
description: >-
  Split data across nodes by hash, range, or directory - shard-key choice, hot spots, resharding, and cross-shard query pain.
---

# sde-sharding-partitioning

When one DB can't hold the data or the write load, partition it. **Vertical partitioning** splits columns/tables by feature (orders DB vs users DB). **Horizontal partitioning (sharding)** splits rows across nodes by a **shard key**. Strategies: **hash-based** (key % N or consistent hashing) spreads evenly but kills range scans; **range-based** keeps ranges together (good for time queries) but risks hot shards (newest range gets all writes); **directory/lookup** keeps a mapping service for flexibility at the cost of an extra hop. **Use consistent hashing** so adding/removing a node remaps only ~1/N keys instead of everything. **Choosing the shard key is the whole game**: pick high-cardinality, evenly-accessed keys (user_id), not monotonic ones (auto-increment, timestamp) that create hot spots. **Pain points**: cross-shard joins/transactions become app-level scatter-gather; aggregate queries fan out to all shards; resharding is operationally hard - plan capacity ahead. **Pitfall**: sharding too early - exhaust vertical scaling, read replicas, and caching first; sharding is a one-way door.

**Tools:** consistent hashing, range/hash partitioning, shard key, vertical partitioning
