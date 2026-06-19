---
name: algo-complexity-analysis
description: >-
  Big-O / time-space complexity analysis — amortized, recurrences, dominant terms, common traps — to predict scalability and pass complexity interview questions.
---

# algo-complexity-analysis

Big-O bounds growth as input → ∞, keeping only the dominant term and dropping constants: O(2n²+100n) = O(n²). Θ is a tight bound, Ω a lower bound. Read code structurally — sequential blocks add (take the max), nested loops over the same n multiply (O(n²)), halving each step is O(log n), and a loop doing O(log n) work n times is O(n log n). 

**Amortized analysis** averages cost over a sequence: a dynamic array's append is O(1) amortized despite occasional O(n) doublings (aggregate/accounting method) — likewise hashmap ops and DSU. **Recurrences**: solve `T(n)=aT(n/b)+f(n)` with the Master Theorem or a recursion tree. Always state **space** separately, and remember the recursion call stack counts (a 'no extra space' recursive solution still uses O(depth)). 

Pitfalls: (1) ignoring hidden costs — string concatenation, slicing, `in` on a list (O(n)), or sort inside a loop. (2) confusing average vs worst case (quicksort, hashmap). (3) treating input value-range as 'constant' when it isn't (pseudo-polynomial knapsack is O(nW), not O(n)). (4) forgetting recursion stack space. (5) over-reporting O(n²) when amortization makes it O(n).

**Tools:** Big-O/Θ/Ω, amortized analysis, Master Theorem, recursion trees, space complexity
