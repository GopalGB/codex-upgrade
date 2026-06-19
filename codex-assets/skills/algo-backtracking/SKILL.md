---
name: algo-backtracking
description: >-
  Backtracking for combinatorial generation and constraint search — permutations, combinations, subsets, N-Queens, Sudoku, word-search — with pruning.
---

# algo-backtracking

Backtracking is DFS over a decision tree: at each step **choose** a candidate, **explore** (recurse), then **un-choose** (undo the mutation) so the next branch starts clean. The skeleton: `if goal: record; return; for c in candidates: if valid(c): place(c); recurse(); remove(c)`. 

Generate **subsets** by include/exclude at each index (2ⁿ); **permutations** by swapping or a used[] mask (n!); **combinations** by passing a `start` index to avoid reusing earlier elements and prevent duplicate sets. Dedup with sorted input + 'skip if same as previous sibling'. 

The whole game is **pruning**: cut branches that can't lead to a solution early (N-Queens column/diagonal sets, partial-sum > target). Without pruning it's brute force. 

Pitfalls: (1) forgetting to undo state on return — corrupts sibling branches (the #1 bug). (2) appending a reference to the running path instead of a copy when recording (`res.append(path[:])`). (3) generating duplicate combinations by not using a start index. (4) re-marking visited cells in grid DFS without unmarking.

**Tools:** choose/explore/un-choose, visited set, pruning, candidate ordering
