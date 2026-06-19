---
name: algo-bit-manipulation
description: >-
  Bitwise tricks — masks, single-number XOR, count-bits, power-of-two checks, subset enumeration, lowest-set-bit — for O(1) state and tight inner loops.
---

# algo-bit-manipulation

Bits give O(1) set operations and compact state. Core idioms: **test** bit i: `x & (1<<i)`; **set**: `x | (1<<i)`; **clear**: `x & ~(1<<i)`; **toggle**: `x ^ (1<<i)`. **XOR** properties (`a^a=0`, `a^0=a`, commutative) solve single-number (XOR all → the lone element) and swapping without a temp. **`x & (x-1)`** clears the lowest set bit — loop it to count set bits (Brian Kernighan) or test power-of-two (`x>0 && (x&(x-1))==0`). **`x & -x`** isolates the lowest set bit (the basis of Fenwick trees). 

**Bitmask DP** encodes a subset of ≤~20 elements as an int — Traveling-Salesman, assignment problems: `dp[mask][i]`. **Enumerate all subsets** of a mask with `for s = mask; s; s = (s-1) & mask`. 

Pitfalls: (1) signed-shift / sign-extension surprises and Python's unbounded ints (no 32-bit wrap — mask with `& 0xFFFFFFFF` when emulating). (2) operator precedence: `&`/`|`/`^` bind looser than `==`/`+` in C/Java — parenthesize. (3) `1 << 32` overflow in 32-bit languages — use `1L`. (4) off-by-one in bit indexing.

**Tools:** AND/OR/XOR/shift, x&(x-1), x&-x, popcount, bitmask DP, subset iteration
