---
name: algo-two-pointers
description: >-
  Two-pointer technique on sorted arrays/strings — pair-sum, dedup, partition, palindrome, merge — to drop O(n²) brute force to O(n).
---

# algo-two-pointers

Two patterns. **Opposite ends**: pointers at `lo`/`hi` move toward each other on a *sorted* array — for pair-sum, if `a[lo]+a[hi] > target` move `hi--`, else `lo++`; O(n) after the O(n log n) sort. Powers 3Sum/4Sum (fix one index, two-pointer the rest), container-with-most-water, valid-palindrome. **Same direction (fast/slow)**: slow marks the write/partition boundary while fast scans — removes duplicates, partitions even/odd, and (in linked lists) detects cycles. **Dutch national flag** is a three-pointer partition that sorts 0/1/2 in one O(n) pass. 

The correctness argument is monotonicity: each move provably can't skip a valid answer because the array is ordered. 

Pitfalls: (1) forgetting the array must be sorted for opposite-ends sum logic. (2) Off-by-one with `while lo < hi` vs `<=` (use `<` for distinct-index pairs). (3) Not skipping duplicate values in 3Sum, producing repeat triples — advance past equal neighbors. (4) Moving the wrong pointer breaks the invariant.

**Tools:** opposite-ends, fast/slow, partition (Dutch flag), merge pointers
