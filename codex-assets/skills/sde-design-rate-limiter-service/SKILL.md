---
name: sde-design-rate-limiter-service
description: >-
  Design a distributed rate-limiter service - algorithm choice, shared Redis counters, atomicity, and where to place it.
---

# sde-design-rate-limiter-service

Design a service that limits requests per user/IP/API-key across a fleet. **Placement**: implement as **API-gateway/middleware** in front of services (one enforcement point, reusable) rather than scattered in each app. **Algorithm**: **token bucket** is the usual pick - allows bursts, simple state (token count + last-refill timestamp per key); for stricter smoothing use **sliding-window counter**. **The distributed challenge**: many gateway nodes must share one limit, so per-node memory counters won't work - keep state in a **central Redis**. To avoid races between read-count and increment across nodes, do it **atomically** with a Redis Lua script (or INCR + EXPIRE) that reads, decides, and updates in one round-trip. Store per key: `key -> {tokens, last_refill}` with a TTL. **Return 429 + Retry-After + X-RateLimit-* headers** so clients self-throttle. **Tradeoffs**: every request now hits Redis (latency + a dependency) - mitigate with local approximate counters synced periodically, accepting slight over-allowance. Decide **fail-open vs fail-closed** explicitly: if Redis is down, do you allow traffic (protect availability) or block (protect the backend)? Usually fail-open for user-facing, fail-closed for abuse-critical. **Pitfall**: non-atomic check-then-set under concurrency (lets bursts through), and a single Redis as a SPOF - cluster/replicate it.

**Tools:** token bucket, Redis + Lua, sliding window, middleware/gateway placement, fail-open
