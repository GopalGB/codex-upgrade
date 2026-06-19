---
name: algo-recursion-fundamentals
description: >-
  Reason about recursion correctly — base case, recursive case, the call stack, and recursion-to-iteration — to write provably-terminating recursive solutions.
---

# algo-recursion-fundamentals

A correct recursion has three parts: a **base case** that returns without recursing, a **recursive case** that calls itself on a strictly smaller subproblem, and a guarantee that every path reaches the base (the variant decreases). Trust the recursion: assume the recursive call returns the right answer for the smaller input, then combine. Model cost with a **recursion tree** or the Master Theorem. 

Depth costs O(depth) stack frames — deep recursion blows the stack (Python default ~1000). Convert to iteration with an explicit stack, or use tail-recursion where the language optimizes it (not Python/Java). Overlapping subproblems (naive Fibonacci is O(2ⁿ)) demand **memoization** to collapse to O(n). 

Pitfalls: (1) missing or unreachable base case → infinite recursion / stack overflow. (2) recursing on a subproblem that isn't actually smaller. (3) mutating shared state across branches without undoing it (see backtracking). (4) recomputing identical subproblems — memoize. (5) returning the wrong thing from the base case (e.g., 0 vs 1 for empty product).

**Tools:** base case, recursion tree, tail-call, memoization, explicit stack
