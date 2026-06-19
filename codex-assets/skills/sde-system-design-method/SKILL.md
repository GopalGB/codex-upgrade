---
name: sde-system-design-method
description: >-
  Drive any system-design problem through the canonical 5-step flow: requirements, estimation, API, data model, then scale.
---

# sde-system-design-method

Never jump to boxes-and-arrows. Run the funnel in order. (1) **Clarify requirements**: split functional (what it does) from non-functional (latency, availability target like 99.9%, consistency, durability). Pin scale: DAU, read:write ratio, peak QPS. (2) **Estimate**: QPS = DAU x actions/user / 86400, then x2-3 for peak. Storage = items/day x bytes x retention_years x 365. Bandwidth = QPS x payload. Memorize: 1 day approx 10^5 s, 1M writes/day approx 12/s. (3) **API**: define the 3-5 core endpoints with params and response shape before any internals. (4) **Data model**: pick SQL vs NoSQL from access patterns, sketch tables/keys and the hot query. (5) **Scale**: only now add LB, cache, replicas, sharding, queues - each justified by a number from step 2. **Pitfall**: designing for 1B users when the spec says 10K, or skipping estimation so you can't justify a cache. State assumptions out loud and revise as the interviewer pushes; the method is the signal, not a memorized diagram.

**Tools:** back-of-envelope estimation, QPS/storage math, capacity planning
