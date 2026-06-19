---
name: sde-scalability-horizontal-scaling
description: >-
  Scale out with stateless services, vertical vs horizontal tradeoffs, and the path from single server to multi-tier fleet.
---

# sde-scalability-horizontal-scaling

**Vertical** (bigger box) is simplest but has a hard ceiling and a single point of failure; **horizontal** (more boxes) scales near-linearly but adds coordination cost. Prefer horizontal once you exceed one machine's headroom. The enabling move: make app servers **stateless** - push session/state out to a shared store (Redis) or a signed token, so any server handles any request and you can add/remove nodes freely behind a load balancer. Separate tiers (web, app, data) so each scales independently. Use **autoscaling** keyed on a real signal (CPU, p95 latency, queue depth), with min/max bounds and a cooldown to avoid thrash. **Database is usually the bottleneck**: scale reads with replicas, writes with sharding; the stateless app tier is the easy part. **Pitfall**: sticky sessions and in-memory caches on app servers - they break horizontal scaling and cause cache inconsistency after a scale event. Design shared-nothing: no node depends on another node's local state.

**Tools:** stateless design, autoscaling, shared-nothing
