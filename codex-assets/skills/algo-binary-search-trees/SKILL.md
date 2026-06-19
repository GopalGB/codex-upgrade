---
name: algo-binary-search-trees
description: >-
  Binary search trees — ordered insert/search/delete, validate-BST, inorder-successor, kth-smallest, range queries — and why balance matters.
---

# algo-binary-search-trees

A BST keeps `left < node < right` recursively, giving O(h) search/insert/delete where h is height. **Inorder traversal yields sorted order** — the key fact behind kth-smallest (stop at the kth inorder node), validate-BST (check inorder is strictly increasing, or pass down (min,max) bounds), and range-sum (prune subtrees outside [lo,hi]). 

**Delete** has three cases: leaf (remove), one child (splice), two children (replace with inorder successor = leftmost of right subtree, then delete that successor). **Successor**: if right subtree exists, leftmost of it; else the lowest ancestor for which the node is in the left subtree. 

The catch: a plain BST degrades to a linked list (O(n)) on sorted insertions. Real systems use self-balancing trees — **Red-Black** (Java TreeMap, C++ std::map) or **AVL** (stricter balance, faster reads) — keeping h = O(log n). 

Pitfalls: (1) validating with only local `left<node<right` checks instead of inherited bounds — a deep violator passes. (2) botching two-child delete. (3) assuming balance on adversarial/sorted input. (4) duplicate-key policy left undefined.

**Tools:** BST invariant, inorder, successor/predecessor, delete-two-children, balanced trees
