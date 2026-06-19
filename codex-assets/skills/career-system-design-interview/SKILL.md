---
name: career-system-design-interview
description: >-
  Structure a system-design interview with a repeatable method (requirements→estimation→API→data→architecture→scale→tradeoffs) — use for senior/staff loops.
---

# career-system-design-interview

Drive the conversation with a method, don't free-associate components. Phases (45 min): (1) **Functional + non-functional requirements** — scope features, then nail scale (DAU, QPS, read/write ratio, latency SLO, durability). (2) **Capacity estimation** — back-of-envelope: QPS = DAU × actions/day / 86400; storage = items × size × years; bandwidth. (3) **API design** — a few core endpoints. (4) **Data model** — SQL vs NoSQL by access pattern; pick keys. (5) **High-level architecture** — client → LB → stateless app tier → cache → DB → async workers/queue. (6) **Scale & deep-dive** — the interviewer picks; discuss sharding (by key, consistent hashing), replication (leader-follower), caching (cache-aside, eviction, invalidation), CDN, message queues (Kafka) for decoupling, rate limiting. (7) **Tradeoffs & bottlenecks** — invoke CAP (CP vs AP), consistency models, single points of failure.

**What top candidates do differently:** they spend real time on requirements (juniors jump straight to boxes), justify every choice with a tradeoff ('NoSQL because write-heavy + flexible schema, accepting eventual consistency'), and proactively name failure modes and mitigations (replication, dead-letter queues, idempotency).

**Common mistake:** designing for infinite scale on a 1K-user product (over-engineering), drawing boxes with no justification, ignoring estimation (so scaling decisions are ungrounded), and going silent on tradeoffs. There's no single right answer — the reasoning *is* the answer.

**Tools:** RESHADED/requirements-first, back-of-envelope estimation, load balancers, sharding, caching, CAP, queues
