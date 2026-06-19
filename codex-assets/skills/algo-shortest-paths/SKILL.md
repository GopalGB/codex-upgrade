---
name: algo-shortest-paths
description: >-
  Weighted shortest-path algorithms — Dijkstra, Bellman-Ford, Floyd-Warshall, 0-1 BFS — choosing by negative edges, single vs all-pairs, and edge weights.
---

# algo-shortest-paths

Pick by the graph. **Dijkstra** — single-source, **non-negative** weights, O((V+E) log V) with a binary-heap PQ. Pop the closest unsettled node, relax its edges; use lazy deletion (skip stale PQ entries). Fails with negative edges because a settled node could later be improved. **Bellman-Ford** — single-source, **handles negative edges**, O(V·E); relax all edges V-1 times, and a Vth relaxation that still improves something detects a **negative cycle**. **Floyd-Warshall** — all-pairs, O(V³) DP: `d[i][j] = min(d[i][j], d[i][k]+d[k][j])` with k as the outer loop. **0-1 BFS** — weights only 0/1, O(V+E) using a deque (push-front for 0, push-back for 1). For unweighted, plain BFS suffices. 

Pitfalls: (1) running Dijkstra on negative edges (wrong answer, not just slow). (2) Floyd-Warshall with the k-loop *not* outermost — incorrect. (3) forgetting to skip stale heap entries in Dijkstra, inflating runtime. (4) integer overflow when summing INF as a distance — guard before relaxing. (5) reconstructing paths without storing predecessors.

**Tools:** Dijkstra (PQ), Bellman-Ford (relax V-1), Floyd-Warshall (DP), 0-1 BFS deque
