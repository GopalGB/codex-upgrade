---
name: algo-trees-traversals
description: >-
  Binary-tree traversals and tree DFS/BFS — preorder/inorder/postorder, level-order, height/diameter, LCA, path sums — recursive and iterative.
---

# algo-trees-traversals

Three DFS orders differ by *when you visit the node* relative to children: **preorder** (node, L, R — copy/serialize), **inorder** (L, node, R — sorted output on a BST), **postorder** (L, R, node — when children must be computed first: height, diameter, deleting a tree, bottom-up DP). **Level-order/BFS** uses a queue and processes one level per outer-loop iteration (track `len(queue)` at level start) — shortest depth, right-side-view, zigzag. 

Most tree problems are postorder aggregation: each node returns a summary to its parent (height, max-path-sum, balanced?). Compute the global answer as a side effect while returning the local value. **LCA**: recurse; if a node sees the targets split across left/right it's the LCA. Iterative traversals use an explicit stack; **Morris traversal** does inorder in O(1) space via threading. 

Pitfalls: (1) null-child checks before recursing. (2) confusing 'height' (edges/nodes) conventions — pick one. (3) mixing the per-node return value with the global answer (diameter returns height but updates a global max). (4) BFS without snapshotting level size, merging levels.

**Tools:** DFS recursion, explicit stack, BFS queue, Morris traversal, postorder aggregation
