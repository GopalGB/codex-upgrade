---
name: career-coding-interview-patterns
description: >-
  Master the ~15 algorithm patterns that cover most coding interviews, with recognition triggers and complexity — use when prepping LeetCode-style technical screens.
---

# career-coding-interview-patterns

Don't grind 800 random problems — learn **patterns** and their recognition triggers. Core set: two-pointers (sorted array / pair-sum, O(n)); sliding window (contiguous subarray/substring optimum, O(n)); fast-slow pointers (cycle detection); binary search (sorted *or* monotonic predicate / 'search the answer', O(log n)); BFS (shortest path in unweighted graph/grid); DFS + backtracking (permutations/combinations/subsets, prune to cut branching); heap / top-K (k-th largest, merge-k-lists, O(n log k)); intervals (merge/insert, sort by start O(n log n)); union-find (connected components / cycle in undirected, near-O(1) amortized); topological sort (dependency ordering / course-schedule); monotonic stack (next-greater-element, histogram); DP (overlapping subproblems + optimal substructure — define state, recurrence, base case, then memoize→tabulate).

**What top candidates do differently:** they verbalize the pattern recognition ('this is a contiguous-window max → sliding window'), state brute-force + complexity first, then optimize, and always state final time/space. Practice with **spaced repetition** (re-solve at 1d/3d/7d/21d) and timed (25–35 min) over fresh grinding.

**Common mistake:** silent coding (interviewer can't follow → no partial credit), jumping to code before clarifying constraints (input size dictates target complexity), and memorizing solutions instead of the underlying recurrence/invariant — which collapses on any variation.

**Tools:** two-pointers, sliding window, BFS/DFS, binary search, heap, backtracking, DP, union-find, monotonic stack, topo sort
