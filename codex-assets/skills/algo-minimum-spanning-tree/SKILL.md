---
name: algo-minimum-spanning-tree
description: >-
  Minimum spanning tree — Kruskal (edge-sort + DSU) and Prim (grow via PQ) — for least-cost connection: networks, clustering, road/cable layout.
---

# algo-minimum-spanning-tree

An MST connects all V vertices with V-1 edges at minimum total weight (undirected, connected graph). Both algorithms rely on the **cut property**: the lightest edge crossing any cut is safe to include. 

**Kruskal**: sort all edges ascending, add each edge if its endpoints are in different DSU sets (skip if it would form a cycle), stop at V-1 edges. O(E log E), dominated by the sort — best for **sparse** graphs and when edges are given as a list. **Prim**: grow a tree from a start vertex, repeatedly adding the cheapest edge leaving the tree via a min-heap of candidate edges. O((V+E) log V) — better for **dense** graphs, especially with a Fibonacci/array variant. 

For 'connect all points' (complete graph on coordinates), Prim is usually cleaner since edges are implicit. 

Pitfalls: (1) Kruskal without union-find (or without path compression) — cycle checks become the bottleneck. (2) Prim adding a vertex twice — mark visited on extraction and skip stale heap entries. (3) assuming MST is unique (it isn't with equal weights). (4) running on a disconnected graph and expecting one tree (you get a forest).

**Tools:** Kruskal + union-find, Prim + min-heap, cut property, sparse vs dense choice
