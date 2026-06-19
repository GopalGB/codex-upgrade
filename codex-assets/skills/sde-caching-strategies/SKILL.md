---
name: sde-caching-strategies
description: >-
  Apply cache-aside, write-through, write-back, write-around with correct invalidation, TTLs, and stampede protection.
---

# sde-caching-strategies

Caching trades freshness for speed. **Cache-aside (lazy)**: app reads cache, on miss loads DB then populates cache - most common, resilient to cache failure, but first read is slow and risks stale data; pair with TTL. **Write-through**: write cache and DB synchronously - cache always fresh, write latency higher. **Write-back (write-behind)**: write cache, flush to DB async - fastest writes, risk data loss on crash. **Write-around**: write only DB, skip cache - good when written data is rarely re-read. **Eviction**: LRU is the default; size the cache to hold the hot working set. **Invalidation is the hard part**: on update, delete (don't update) the key to avoid races, and use short TTLs as a backstop. **Three classic failures**: (1) **stampede/thundering herd** - many misses hit DB at once when a hot key expires; mitigate with a lock/single-flight or staggered TTL. (2) **penetration** - queries for nonexistent keys bypass cache; cache the negative result or use a Bloom filter. (3) **avalanche** - many keys expire simultaneously; jitter the TTLs.

**Tools:** Redis, Memcached, cache-aside, write-through, TTL, LRU
