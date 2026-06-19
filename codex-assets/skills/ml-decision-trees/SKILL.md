---
name: ml-decision-trees
description: >-
  Build interpretable single decision trees for non-linear tabular splits and as the base learner for ensembles
---

# ml-decision-trees

Recursively split feature space to maximize purity. CART uses Gini impurity (1-Σpᵢ²) or entropy for classification, variance reduction (MSE) for regression; greedily picks the split with max impurity decrease. Captures non-linearities and interactions with zero feature scaling needed and handles mixed feature types. Use as a transparent model or, more often, as the weak learner inside RF/boosting. **Key hyperparams (all about overfitting control):** `max_depth`, `min_samples_leaf` (most reliable regularizer — set ≥1% of data), `min_samples_split`, `ccp_alpha` for cost-complexity post-pruning. **The defining pitfall:** a single unpruned tree memorizes noise — it has high variance, tiny data changes produce totally different trees. Always prune or constrain depth, and validate. **Other pitfalls:** biased toward high-cardinality features in split selection; can't extrapolate (predictions are piecewise-constant — flat outside training range); axis-aligned splits struggle with diagonal boundaries. Read feature_importances_ with caution — they inflate for high-cardinality features; prefer permutation importance.

**Tools:** sklearn DecisionTreeClassifier/Regressor, Gini, entropy, CART, cost-complexity pruning
