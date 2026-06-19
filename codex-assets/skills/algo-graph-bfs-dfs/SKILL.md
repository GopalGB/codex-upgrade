---
name: algo-graph-bfs-dfs
description: >-
  Graph traversal — BFS for shortest path in unweighted graphs, DFS for connectivity/components/cycle detection — on adjacency lists or grids.
---

# algo-graph-bfs-dfs

Represent graphs as **adjacency lists** (O(V+E) space, the default) — adjacency matrices only for dense graphs. Both traversals are O(V+E). **BFS** (queue) explores level by level → it finds the **shortest path in an unweighted graph** and is the basis for multi-source spreading (rotting-oranges: seed the queue with all sources, count levels). **DFS** (recursion or explicit stack) is for connectivity, counting components, flood-fill, topological order, and cycle detection. 

Grids are implicit graphs: each cell connects to 4 (or 8) neighbors — iterate direction deltas, bound-check, skip visited/walls. 

**Cycle detection** differs by graph type: undirected → DFS finding a visited neighbor that isn't the parent; directed → DFS with three colors (white/gray/black), a gray-node back-edge means a cycle. 

Pitfalls: (1) marking visited at *dequeue* instead of *enqueue* in BFS → the same node queued many times → blowup. (2) revisiting in DFS without a visited set → infinite loops. (3) recursion depth overflow on large grids — use iterative DFS or BFS. (4) using DFS and expecting shortest paths (it doesn't give them).

**Tools:** adjacency list, visited set, queue BFS, recursive/stack DFS, grid 4/8-dir, multi-source BFS
