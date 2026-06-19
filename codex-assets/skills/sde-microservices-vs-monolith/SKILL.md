---
name: sde-microservices-vs-monolith
description: >-
  Choose between modular monolith and microservices - decomposition boundaries, the distributed-systems tax, and the migration path.
---

# sde-microservices-vs-monolith

**Start with a modular monolith.** One deployable, in-process calls, ACID transactions, trivial debugging - it carries most teams far. **Microservices** buy independent deploy/scale/tech-choice and team autonomy, but you pay a heavy tax: network calls fail and add latency, distributed transactions become **sagas** (compensating actions, eventual consistency), debugging needs distributed tracing, and you inherit service discovery, versioning, and data-ownership-per-service. The right trigger to split is **organizational** (many teams stepping on one codebase/deploy) more than technical. **Decompose by bounded context** (DDD) - cohesive business capabilities that own their data - not by technical layer. Each service owns its database; never share a DB across services (that recreates the monolith's coupling with worse failure modes). **Migrate with the strangler fig**: route slices of traffic to new services behind a facade, shrinking the monolith incrementally rather than a big-bang rewrite. **Pitfall**: a 'distributed monolith' - services so chatty and co-deployed you get all the network pain and none of the autonomy; if two services always deploy together, they should be one.

**Tools:** bounded contexts, modular monolith, strangler fig, service mesh, saga
