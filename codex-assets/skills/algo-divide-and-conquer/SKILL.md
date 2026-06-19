---
name: algo-divide-and-conquer
description: >-
  Divide-and-conquer — merge sort, quickselect, binary-search variants, max-subarray, count-inversions, the Master Theorem — split, solve, combine.
---

# algo-divide-and-conquer

Divide-and-conquer splits a problem into independent subproblems, solves them recursively, and **combines** the results. The combine step is where the work (and the insight) usually lives. Analyze cost with the **Master Theorem** for `T(n)=aT(n/b)+O(nᵈ)`: compare d to log_b(a) — merge sort (a=2,b=2,d=1) is the balanced O(n log n) case. 

Workhorses: **merge sort** (stable, O(n log n), the merge step also **counts inversions** in one pass); **quickselect** (find the kth smallest by partitioning around a pivot and recursing into one side — O(n) average, O(n²) worst, fixed by a random/median-of-medians pivot); **max-subarray** via D&C (left, right, or crossing the midpoint); **maximum points / closest-pair** in O(n log n). 

Pitfalls: (1) a combine step that's more expensive than expected, pushing complexity above the intended class. (2) quickselect/quicksort worst case from a bad pivot on sorted/adversarial input — randomize. (3) not solving subproblems on *disjoint* ranges, double-counting. (4) deep recursion stack on near-sorted input.

**Tools:** recurrence + Master Theorem, merge step, quickselect O(n) avg, count-inversions
