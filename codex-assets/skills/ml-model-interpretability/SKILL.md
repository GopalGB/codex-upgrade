---
name: ml-model-interpretability
description: >-
  Explain model predictions with SHAP, LIME, permutation importance, and PDP/ICE for trust, debugging, and compliance
---

# ml-model-interpretability

**Global (whole model):** permutation importance (shuffle a feature, measure metric drop — model-agnostic, on held-out data, unbiased unlike impurity importance); partial dependence plots (PDP) show marginal effect of a feature on predictions; ICE plots show per-instance curves (reveal heterogeneous/interaction effects PDP averages away). **Local (single prediction):** **SHAP** assigns each feature a Shapley value (game-theoretic, additive, consistent) — TreeExplainer is exact and fast for tree ensembles (use it for XGBoost/LightGBM/RF), KernelExplainer is slow/approximate for any model; summary plots give global+local in one view. **LIME** fits a local surrogate linear model around one instance — faster but less stable than SHAP (explanations vary run to run). **Steps:** use SHAP TreeExplainer for tabular boosting as the default; permutation importance + PDP/ICE for global understanding. **Pitfalls:** correlated features split/mislead importance (SHAP and permutation both distort under collinearity — interpret cautiously); PDP assumes feature independence (misleading when correlated — ICE or accumulated local effects/ALE are safer); explanations are descriptive, NOT causal — don't read SHAP as 'changing X causes Y'. Match the method to model type for speed and exactness.

**Tools:** SHAP (TreeExplainer/KernelExplainer), LIME, permutation_importance, PDP, ICE, partial dependence
