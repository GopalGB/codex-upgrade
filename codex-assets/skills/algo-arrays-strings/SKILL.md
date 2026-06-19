---
name: algo-arrays-strings
description: >-
  Manipulate arrays and strings in-place — reversal, rotation, dedup, in-place writes — when memory matters or interviewers forbid extra space.
---

# algo-arrays-strings

Arrays are contiguous O(1)-indexed memory; strings are immutable in Java/Python (mutate via list/char[]). Master the **read/write two-index** idiom for in-place compaction: a `write` pointer trails a `read` pointer, copying only kept elements (remove-duplicates-from-sorted, move-zeroes) in O(n) time, O(1) space. **Rotate by k** via the reverse trick: reverse whole, reverse first k, reverse rest — O(n), no buffer. For max-subarray use **Kadane**: `cur = max(x, cur+x); best = max(best, cur)` in one pass. Frequency problems: a fixed 26/128-size count array beats a hashmap for ASCII. 

Complexity gotchas: building a string by `+=` in a loop is O(n²) (each concat copies) — collect into a list and `join` for O(n). Slicing `arr[i:j]` copies (O(j-i)); use indices when you only read. 

Classic pitfall: shifting elements on each delete inside a loop turns an O(n) job into O(n²). Always think "can a second pointer or a reversal avoid the shift?"

**Tools:** two-pointer in-place, Kadane, read/write index, char-count array
