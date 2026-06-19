---
name: algo-binary-search
description: >-
  Classic binary search on sorted data plus lower/upper-bound variants — find element, first/last occurrence, insertion point — in O(log n).
---

# algo-binary-search

On a sorted array, halve the search space each step: O(log n). Compute `mid = lo + (hi-lo)//2` (avoids overflow in fixed-width languages). The hard part is the *boundary variant*: plain find returns any match; **lower_bound / bisect_left** returns the first index ≥ target; **upper_bound / bisect_right** the first index > target. First-occurrence: on a match, keep searching left (`hi = mid`); last-occurrence: search right. 

Pick one invariant and never mix them. The robust template uses a half-open `[lo, hi)` with `while lo < hi: if cond(mid): hi = mid else: lo = mid+1`, where `cond` is a monotone predicate (false…false true…true) — it converges to the first true. 

Pitfalls: (1) the infinite loop from `lo = mid` without `+1` when `mid == lo`. (2) using `<=` with `[lo, hi]` closed but updating `hi = mid` — mismatched conventions. (3) searching unsorted data. (4) integer mid overflow (`(lo+hi)/2`). Use the language's `bisect`/`lower_bound` when allowed.

**Tools:** lo/hi/mid, bisect_left/right, lower_bound, half-open invariant
