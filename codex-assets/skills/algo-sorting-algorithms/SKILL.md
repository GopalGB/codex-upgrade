---
name: algo-sorting-algorithms
description: >-
  Sorting algorithms and when to use which — quicksort, merge sort, heapsort, Timsort, counting/radix sort — by stability, space, and data shape.
---

# algo-sorting-algorithms

Comparison sorts are bounded at Ω(n log n). **Quicksort**: in-place, O(n log n) average / O(n²) worst (mitigate with random or median-of-3 pivot), not stable — the typical unstable in-memory default. **Merge sort**: stable, guaranteed O(n log n), O(n) extra space — the choice for linked lists and external/large data. **Heapsort**: O(n log n), O(1) space, not stable — when memory is tight. **Timsort** (Python `sorted`/`list.sort`, Java `Arrays.sort` for objects): adaptive, stable, exploits existing runs → near O(n) on partly-sorted data — what you actually call in practice. 

Non-comparison sorts beat the bound when keys are bounded integers: **counting sort** O(n+k) (k = value range), **radix sort** O(d·(n+k)) for fixed-width keys, **bucket sort** for uniform reals. 

Decide by: need stability? bounded keys? memory budget? data already partly sorted? 

Pitfalls: (1) quicksort's O(n²) on sorted/duplicate-heavy input without pivot randomization or 3-way partition. (2) assuming a sort is stable when it isn't (custom-comparator multi-key sorts break). (3) counting/radix on unbounded or floating keys. (4) writing a comparator that isn't a total order (inconsistent ties → undefined/throwing sorts).

**Tools:** quicksort, merge sort, heapsort, Timsort, counting/radix sort, comparator design
