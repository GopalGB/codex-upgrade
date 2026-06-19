---
name: ml-feature-selection
description: >-
  Reduce feature count via filter/wrapper/embedded methods to cut overfitting, speed inference, and improve interpretability
---

# ml-feature-selection

Three families. **Filter (fast, model-agnostic):** rank features by univariate stats — correlation, mutual information (captures non-linear), chi² (categorical), ANOVA F-test; cheap first pass but ignores feature interactions and redundancy. **Wrapper (accurate, expensive):** search subsets by retraining — Recursive Feature Elimination (RFE drops the weakest feature iteratively), forward/backward selection, Boruta (vs shadow features). **Embedded (best default):** selection happens during training — L1/Lasso zeros coefficients, tree-based importance, or use SelectFromModel. **The reliable signal:** permutation importance (shuffle a feature, measure metric drop) computed on a held-out set — model-agnostic and not biased like impurity importance. **Pitfalls:** must run selection inside CV folds, not before splitting, or you leak target info and overstate scores (a classic mistake that produces near-perfect biased CV); drop multicollinear features (high VIF) since they split importance and destabilize linear models; remember high impurity importance ≠ causal/useful. Start with variance threshold + correlation pruning, then embedded selection.

**Tools:** mutual_info, chi2, RFE, Lasso, tree importance, Boruta, permutation importance, VIF
