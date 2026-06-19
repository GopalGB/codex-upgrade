---
name: sde-rate-limiting
description: >-
  Throttle traffic to protect services - token bucket, leaky bucket, sliding window, distributed counters, and 429 semantics.
---

# sde-rate-limiting

Rate limiting caps request rate per client to prevent abuse, ensure fairness, and protect downstreams. **Token bucket** (most popular): a bucket of N tokens refills at rate r; each request spends one; empty = reject. Allows controlled bursts up to bucket size - ideal for APIs. **Leaky bucket**: requests queue and drain at a fixed rate - smooths bursts into a constant outflow, good for protecting a fixed-throughput backend. **Fixed-window counter**: count per minute window - simple but allows 2x bursts at the window boundary. **Sliding-window log** is accurate (timestamps in a sorted set) but memory-heavy; **sliding-window counter** approximates it cheaply and is the common production choice. **Distributed enforcement**: keep counters in Redis (INCR+EXPIRE or a Lua script for atomicity) so all app nodes share one limit; per-node limits leak N x the intended rate. Return **HTTP 429** with `Retry-After` and `X-RateLimit-Remaining/Reset` headers so clients back off correctly. **Pitfall**: rate-limiting in app memory behind a load balancer (each node counts separately), and not failing-open vs fail-closed deliberately when the limiter store is down.

**Tools:** token bucket, leaky bucket, sliding-window log/counter, Redis, 429 + Retry-After
