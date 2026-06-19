---
name: algo-heaps-priority-queue
description: >-
  Binary heaps / priority queues — top-K, k-way merge, running median, Dijkstra's PQ, scheduling — with O(log n) push/pop and O(1) peek.
---

# algo-heaps-priority-queue

A binary heap is a complete tree in an array: parent at `i`, children at `2i+1/2i+2`. Push/pop are O(log n) (sift up/down), peek is O(1), and **heapify** builds from n items in O(n) (not n log n). Use it whenever you repeatedly need the current min/max. 

**Top-K largest**: keep a *min*-heap of size k — push each element, pop when size > k; O(n log k), beats full sort O(n log n). **K-way merge** (merge k sorted lists): heap of k heads. **Running median**: two heaps — a max-heap for the lower half, min-heap for the upper, rebalanced to differ by ≤1. Dijkstra and Prim use a PQ keyed by distance/weight. 

Python's `heapq` is a *min*-heap only — negate values (or use tuples) for a max-heap; break ties with an insertion counter to avoid comparing un-orderable payloads. 

Pitfalls: (1) using a max-heap for top-K-largest (wastes space; you want a size-k min-heap). (2) decrease-key isn't supported by `heapq` — use **lazy deletion** (push updated entries, skip stale ones on pop). (3) forgetting heapify is O(n) and sorting instead.

**Tools:** min/max-heap, heapq, sift-up/down, heapify, two-heap median, lazy deletion
