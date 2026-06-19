---
name: sde-load-balancing
description: >-
  Distribute traffic across servers - L4 vs L7, algorithms, health checks, and avoiding the LB as a single point of failure.
---

# sde-load-balancing

A load balancer spreads requests so no server is overwhelmed and dead nodes get bypassed. **L4** (transport) routes by IP/port - fast, protocol-agnostic, no payload inspection. **L7** (application) reads HTTP - can route by path/header/cookie, do TLS termination and sticky sessions, at higher cost. **Algorithms**: round-robin (uniform servers), weighted round-robin (mixed capacity), least-connections (long-lived/uneven requests), consistent hashing (route same key to same node - critical for cache affinity). **Health checks**: active probes (LB pings /health) plus passive (eject after N failed requests); fail fast and re-add after recovery. **Avoid the LB being a SPOF**: run a pair in active-passive with a floating VIP, or use DNS/anycast across multiple LBs. **Pitfall**: enabling sticky sessions by default - it concentrates load and breaks rebalancing; prefer stateless servers + external session store, and reserve stickiness for cases that truly need it.

**Tools:** round-robin, least-connections, consistent hashing, L4/L7, health checks
