---
name: sde-replication-consistency
description: >-
  Replicate data for availability and read scale - leader-follower, replication lag, sync vs async, and quorum reads/writes.
---

# sde-replication-consistency

Replication copies data to multiple nodes for fault tolerance and read scaling. **Single-leader (primary-replica)**: writes go to the leader, reads fan out to followers - simple, scales reads, but the leader is a write bottleneck and a failover point. **Multi-leader**: writes on several nodes (multi-region) - higher write availability but you must resolve write conflicts. **Leaderless/quorum** (Dynamo-style): write to W nodes, read from R nodes; if **W + R > N** you get overlap and read-your-writes-style consistency. **Sync replication** = no data loss on failover but higher write latency; **async** = fast writes but a window of data loss and **replication lag** (a follower serves stale reads). The lag bug: user writes then immediately reads a replica and sees old data - fix with read-your-writes (route the user's own reads to the leader briefly) or monotonic-read routing. **Failover hazards**: split-brain (two leaders), lost writes, and choosing a stale replica as new leader. **Pitfall**: assuming replicas are instantly consistent - design the UX for eventual consistency where you use async replicas.

**Tools:** leader-follower, multi-leader, quorum (W+R>N), read-your-writes, replication lag
