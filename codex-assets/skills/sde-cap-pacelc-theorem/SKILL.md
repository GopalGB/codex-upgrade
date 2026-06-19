---
name: sde-cap-pacelc-theorem
description: >-
  Reason about consistency vs availability under partitions (CAP) and the latency-vs-consistency tradeoff even without them (PACELC).
---

# sde-cap-pacelc-theorem

**CAP**: during a network **P**artition, a distributed system must choose **C**onsistency (reject/block to avoid stale or divergent data) or **A**vailability (keep serving, possibly stale). You can't have both while partitioned; partitions are not optional, so the real choice is CP vs AP. **CP** systems (HBase, etcd/ZooKeeper, traditional RDBMS with sync replication) refuse some requests to stay correct - pick for money/inventory/locks. **AP** systems (Cassandra, Dynamo, Riak) stay up and reconcile later - pick for feeds, carts, telemetry where availability beats strict freshness. **PACELC** completes the picture: even with no partition (**E**lse), you trade **L**atency vs **C**onsistency - synchronous cross-region consistency costs round-trips. So Cassandra is PA/EL (available + low-latency), a strongly-consistent store is PC/EC. **Practical move**: most real systems are **tunable** - set consistency per operation (quorum for the checkout write, ONE for the analytics read). **Pitfall**: treating CAP as 'pick 2 of 3' permanently - C and A only conflict during a partition; and forgetting PACELC's everyday latency cost when you mandate global strong consistency.

**Tools:** CAP, PACELC, CP vs AP, tunable consistency, linearizability
