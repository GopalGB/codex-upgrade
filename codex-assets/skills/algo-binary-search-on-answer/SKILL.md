---
name: algo-binary-search-on-answer
description: >-
  Binary-search the answer space when checking feasibility is easy but computing the optimum is hard — min capacity, Koko bananas, split-array, allocation.
---

# algo-binary-search-on-answer

When the answer is a number in a known range and a monotone `feasible(x)` predicate exists ('can we do it with capacity/speed/time x?'), binary-search x instead of computing it directly. Total cost is O(log(range) × cost-of-check). Examples: **ship-within-D-days** (min capacity), **Koko-eating-bananas** (min speed), **split-array-largest-sum** / **book-allocation** (minimize the max chunk), **smallest-divisor**. 

The recipe: (1) identify the search bound `[lo, hi]` (lo = max single element, hi = total sum, for partition problems). (2) Write a greedy O(n) feasibility check. (3) Binary-search for the first/last x where feasible flips. 

For continuous answers (e.g., minimize-max-distance), bisect on reals for ~100 iterations or until `hi-lo < eps`. 

Pitfalls: (1) wrong/non-monotone predicate — verify feasibility is truly step-shaped before trusting bisection. (2) wrong bounds (lo too low makes a single element infeasible). (3) returning `mid` instead of the converged boundary. (4) eps too tight causing float-loop hangs.

**Tools:** monotone predicate, feasibility check, parametric search, real-valued bisection
