---
name: ml-gradient-boosting
description: >-
  Sequential boosted-tree ensembles (XGBoost/LightGBM/CatBoost) — the top performer for structured/tabular data
---

# ml-gradient-boosting

Builds trees sequentially, each fitting the negative gradient (residuals) of the loss from prior trees; modern libs use second-order (Newton) info with hessians. State of the art for tabular data. **Pick the library:** LightGBM = fastest, leaf-wise growth, best for large data (watch overfitting → cap num_leaves); XGBoost = level-wise, battle-tested, great regularization; CatBoost = best native categorical handling (ordered target encoding) and strong defaults, least tuning. **Core hyperparams (tune in this order):** `learning_rate` (0.01–0.1, lower = more trees needed), `n_estimators` with **early_stopping_rounds** on a validation set (the single most important practice — let it pick tree count), `max_depth`/`num_leaves`, then `subsample` + `colsample_bytree` (~0.8 for stochastic regularization), then `reg_lambda`/`min_child_weight`. **Pitfalls:** overfits if learning_rate high without early stopping; sensitive to noisy labels (it chases residuals = noise); needs a real eval_set. Use `scale_pos_weight` for imbalance. Always early-stop; never hand-fix n_estimators.

**Tools:** XGBoost, LightGBM, CatBoost, early stopping, learning_rate, gradient/hessian, DART
