---
name: algo-sliding-window
description: >-
  Sliding-window for contiguous subarray/substring problems — longest/shortest/at-most-K, fixed or variable size — in a single O(n) pass.
---

# algo-sliding-window

When a problem asks for a contiguous range optimizing a constraint, slide a window with two indices. **Fixed size k**: add the entering element, remove the leaving one, recompute the aggregate in O(1) (max-average-subarray). **Variable size**: expand `right` to include elements; while the window violates the constraint, advance `left` to shrink; record the best at each step. Total work is O(n) because each index enters and leaves at most once (amortized). 

Keep window state in a hashmap/Counter (char counts for longest-substring-without-repeat, anagram windows) or running sum. The "at most K" → "exactly K" trick: `exactly(K) = atMost(K) - atMost(K-1)`. 

Pitfalls: (1) sliding window only works when shrinking is valid — it breaks with negative numbers in 'minimum-subarray-sum ≥ target' (use prefix-sum + monotonic deque instead). (2) Forgetting to update the answer at the right moment (after shrink vs during expand). (3) Letting the window-state map keep zero-count keys, corrupting size checks — delete keys at count 0.

**Tools:** variable window expand/shrink, fixed-k window, window hashmap/Counter
