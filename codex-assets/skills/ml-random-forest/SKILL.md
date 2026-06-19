---
name: ml-random-forest
description: >-
  Bagged decision-tree ensemble for robust low-tuning tabular classification/regression with built-in variance reduction
---

# ml-random-forest

Trains many deep decision trees on bootstrap samples (bagging) and, crucially, at each split considers only a random subset of features (`max_features` ≈ √p for classification, p/3 for regression). This decorrelates the trees so averaging slashes variance without raising bias much. The single best low-effort tabular baseline — strong accuracy, minimal tuning, robust to outliers and noise. **Key hyperparams:** `n_estimators` (more = better but diminishing returns; 200–500 typical — never hurts accuracy, only speed), `max_features` (the lever that controls decorrelation), `max_depth`/`min_samples_leaf` (usually leave trees deep). **Free perk:** out-of-bag (OOB) score gives a validation estimate without a holdout set (oob_score=True). **Pitfalls:** large models are memory-heavy and slower at inference than boosting; impurity-based feature_importances_ are biased toward high-cardinality/continuous features — use permutation importance or SHAP instead. RF rarely beats well-tuned gradient boosting on accuracy but wins on robustness-per-tuning-hour. Cannot extrapolate beyond training range.

**Tools:** sklearn RandomForestClassifier/Regressor, bootstrap, OOB score, feature_importances_
