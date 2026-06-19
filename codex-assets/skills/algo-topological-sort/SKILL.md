---
name: algo-topological-sort
description: >-
  Topological ordering of a DAG — task/build scheduling, course prerequisites, dependency resolution, cycle detection — via Kahn's BFS or DFS post-order.
---

# algo-topological-sort

A topological sort linearizes a **directed acyclic graph** so every edge u→v has u before v — the dependency order for builds, course schedules, and task pipelines. Two algorithms, both O(V+E). 

**Kahn's (BFS)**: compute in-degrees, queue all zero-in-degree nodes, repeatedly pop one into the output and decrement its neighbors' in-degrees, enqueuing any that hit zero. If you output fewer than V nodes, the graph has a **cycle** (no valid order) — this is the standard course-schedule feasibility check. **DFS**: post-order finish times reversed give a topo order; detect cycles with the gray/black coloring. 

For **lexicographically smallest** topo order, replace Kahn's queue with a min-heap. There can be many valid orderings. 

Pitfalls: (1) not detecting cycles — a cyclic graph has no topo order, and forgetting the count check silently returns garbage. (2) building edges in the wrong direction (prereq→course vs course→prereq) inverts the answer. (3) modifying in-degrees of the wrong endpoint. (4) assuming a unique answer when the grader accepts any valid order.

**Tools:** Kahn's in-degree queue, DFS post-order reverse, indegree array, cycle detection
