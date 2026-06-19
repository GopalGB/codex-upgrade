---
name: sde-design-key-value-store
description: >-
  Design a distributed KV store like Dynamo - consistent hashing, replication, quorum, vector clocks, gossip, and tunable consistency.
---

# sde-design-key-value-store

Design a scalable, highly-available KV store (Dynamo/Cassandra-class). **Partitioning**: **consistent hashing** maps keys onto a ring so adding/removing a node remaps only ~1/N keys; use **virtual nodes** (each physical node owns many ring positions) to spread load evenly and handle heterogeneous hardware. **Replication**: each key is stored on the next **N** nodes clockwise on the ring (replication factor), spanning racks/AZs for fault tolerance. **Tunable consistency via quorum**: a write succeeds on **W** replicas, a read queries **R**; **W + R > N** guarantees read/write overlap (strong-ish consistency); W=1,R=1 = fast but eventual. **Conflict resolution**: concurrent writes to different replicas diverge - detect with **vector clocks** (or last-write-wins via timestamps, simpler but can lose data) and reconcile on read. **Membership/failure detection** via **gossip** protocol; tolerate transient failures with **hinted handoff** (a neighbor temporarily holds writes for a down node) and repair drift with **anti-entropy / Merkle trees** (compare hashed ranges, sync only differences). **Storage engine**: LSM-tree (write-optimized) underneath. **Pitfall**: choosing last-write-wins without understanding it silently drops concurrent updates, and ignoring the read-repair/anti-entropy path so replicas drift permanently. State your N/W/R and the consistency it yields.

**Tools:** consistent hashing, virtual nodes, quorum W+R>N, vector clocks, gossip, Merkle trees, hinted handoff
