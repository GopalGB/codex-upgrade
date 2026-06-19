---
name: algo-dynamic-programming
description: >-
  Dynamic programming — 1D/2D states, knapsack, LIS, LCS/edit-distance, grid paths, coin-change — via state definition, recurrence, memo vs tabulation.
---

# algo-dynamic-programming

DP applies when a problem has **optimal substructure** (optimum built from sub-optima) and **overlapping subproblems** (same sub-results reused). The workflow: (1) define the state precisely (what does `dp[i]` / `dp[i][j]` mean?), (2) write the recurrence (transition), (3) set base cases, (4) choose memoization (top-down recursion + cache) or tabulation (bottom-up loop), (5) compress space if only the last row(s) are needed. 

Canonical recurrences: **0/1 knapsack** `dp[w]=max(dp[w], dp[w-wt]+val)` iterating weight *descending* (each item once); **unbounded/coin-change** iterates *ascending* (reuse). **LCS/edit-distance** `dp[i][j]` over the two string prefixes. **LIS** is O(n²) DP or **O(n log n)** via patience-sorting (binary-search a tails array). **Grid paths** `dp[i][j]=dp[i-1][j]+dp[i][j-1]`. 

Pitfalls: (1) a state that doesn't capture enough information to be Markovian. (2) knapsack loop direction (ascending vs descending) silently allowing/forbidding reuse — the #1 bug. (3) wrong base cases (empty string/zero capacity). (4) memoizing on a mutable key. (5) reaching for DP when greedy is provably optimal.

**Tools:** memoization, bottom-up tabulation, state compression, knapsack 0/1 vs unbounded, LIS O(n log n)
