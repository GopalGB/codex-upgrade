---
name: algo-greedy
description: >-
  Greedy algorithms — interval scheduling, jump-game, gas-station, Huffman, fractional knapsack — and proving the local-optimal choice is globally optimal.
---

# algo-greedy

Greedy makes the locally best choice at each step and never reconsiders — O(n log n) when it needs a sort, O(n) otherwise — far cheaper than DP *when it's correct*. The discipline is the proof: it works only when the problem has the **greedy-choice property** (a local optimum extends to a global one) and optimal substructure. Justify with an **exchange argument** ('any optimal solution can be transformed to the greedy one without getting worse') or 'greedy stays ahead'. 

Classic correct greedies: **interval scheduling** (max non-overlapping → sort by end time, take earliest finishing); **min meeting rooms** (sweep starts/ends); **jump-game** (track farthest reachable); **gas-station** (if total gas ≥ cost, the unique start is just after the lowest running deficit); **fractional knapsack** (sort by value/weight); **Huffman coding** (merge two least-frequent). 

Pitfalls: (1) applying greedy to **0/1 knapsack** — provably wrong, needs DP. (2) sorting by the wrong key (start vs end time flips correctness). (3) assuming greedy works without proof — coin-change is greedy-safe only for canonical coin systems. (4) not handling ties/edge cases that break the exchange argument.

**Tools:** exchange argument, sort-then-pick, interval scheduling, greedy-stays-ahead
