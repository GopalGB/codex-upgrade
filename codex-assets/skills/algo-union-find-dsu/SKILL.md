---
name: algo-union-find-dsu
description: >-
  Union-Find / Disjoint Set Union for dynamic connectivity — connected components, Kruskal's MST, cycle detection in undirected graphs, account-merge, redundant-connection.
---

# algo-union-find-dsu

DSU maintains a partition of elements into disjoint sets with two operations: **find(x)** (which set / representative root) and **union(a,b)** (merge two sets). With both optimizations — **path compression** (point nodes directly at the root during find) and **union by rank/size** (attach the smaller tree under the larger) — each op is amortized α(n) (inverse Ackermann), effectively O(1). 

Use it for offline dynamic connectivity: counting connected components, **Kruskal's MST** (add an edge iff its endpoints are in different sets), detecting a cycle in an undirected graph (an edge whose endpoints already share a root closes a cycle → redundant-connection), and merging groups (accounts-merge, friend-circles, number-of-islands-II as edges arrive). 

Pitfalls: (1) implementing find without path compression → O(n) chains. (2) unioning by always attaching a→b instead of by rank/size → tall trees. (3) using DSU when you need to *remove* edges — DSU only merges, never splits (handle deletions offline in reverse). (4) forgetting to union both representatives, comparing raw indices instead of roots.

**Tools:** path compression, union by rank/size, parent array, near-O(1) amortized
