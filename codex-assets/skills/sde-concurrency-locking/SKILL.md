---
name: sde-concurrency-locking
description: >-
  Write correct concurrent code - races, mutexes, deadlock, optimistic vs pessimistic locking, and lock-free atomics.
---

# sde-concurrency-locking

Shared mutable state + multiple threads = **race conditions** (non-atomic read-modify-write, e.g., `count++`). Protect critical sections with a **mutex**; use a **read-write lock** when reads vastly outnumber writes (many readers OR one writer). **Deadlock** needs four conditions (mutual exclusion, hold-and-wait, no preemption, circular wait) - break one: acquire locks in a **global consistent order**, use try-lock with timeout, or minimize lock scope. **Pessimistic locking** (SELECT ... FOR UPDATE) assumes conflict and blocks - safe under high contention but limits throughput and risks deadlock. **Optimistic locking** assumes no conflict: read a version, compute, then update WHERE version = old (compare-and-swap); if the row changed, retry - great for low-contention, no blocking. **Lock-free** uses atomic CAS primitives for counters/queues - fast but subtle (ABA problem). Minimize shared state entirely: prefer immutability, message passing, thread-confinement, or per-thread state. **Pitfall**: holding a lock during I/O or a network call (serializes everything and invites deadlock), and double-checked locking done wrong without proper memory barriers/volatile. Keep critical sections tiny and side-effect-free.

**Tools:** mutex, RWLock, deadlock, optimistic concurrency (CAS/version), atomics, semaphore
