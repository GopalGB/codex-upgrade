---
name: ml-engineer
description: >-
  Expert machine-learning playbook for building real models the right way -
  tabular (the common case for Excel/CSV data), plus NLP/CV and LLM fine-tune
  decisions. Use when asked to train / build / evaluate / improve a model, do
  feature engineering, pick a metric, or diagnose over/underfitting. Triggers:
  "machine learning", "train a model", "ML model", "predict", "classifier",
  "regression", "feature engineering", "cross validation", "fine-tune".
---

# ml-engineer — build models that actually generalize (no MCP)

Stdlib + the standard scientific stack. The `xlsx-wrangler` / `research-scout`
skills feed this one (data in, papers in). Install deps via the tools venv on
demand: `scikit-learn pandas numpy` (+ `xgboost`/`lightgbm` for tabular SOTA,
`torch` only when truly needed).

## The non-negotiable order of operations
1. **Frame the problem.** Supervised? classification vs regression? What is the
   ONE metric that maps to the real objective (not just accuracy)? Write it down.
2. **Split BEFORE you look.** Hold out a test set first. For time data, split by
   time, never randomly. Leakage is the #1 way ML lies — guard it explicitly.
3. **Baseline first.** Dummy/most-frequent, then a linear/logistic or a single
   tree. No fancy model ships until it beats the baseline on the holdout.
4. **Cross-validate honestly.** k-fold (StratifiedKFold for imbalance,
   GroupKFold when rows share an entity, TimeSeriesSplit for time). Report
   mean ± std, not a single lucky fold.
5. **Feature engineering inside the pipeline.** Fit scalers/encoders/imputers on
   train folds only — use `sklearn.pipeline.Pipeline` + `ColumnTransformer` so
   preprocessing can't leak. No manual fit-on-all-data.
6. **Then tune.** Strong tabular default: gradient-boosted trees (XGBoost /
   LightGBM). Tune with a small randomized/Bayesian search, not a giant grid.
7. **Evaluate on the untouched test set ONCE.** Report the metric + a confusion
   matrix / residual plot + calibration. If you peeked, you no longer have a
   test set — say so.

## Metric cheat-sheet
- Imbalanced classification → PR-AUC, F1, recall@k — NOT raw accuracy.
- Probabilities matter → log-loss / Brier + a calibration curve.
- Regression → MAE for robustness, RMSE when big errors hurt more, plus R².
- Ranking/recsys → NDCG, MAP, recall@k.

## Anti-fabrication law (this is the point)
- NEVER report a metric you did not actually compute from a real run. If you
  haven't run it, say "not yet measured."
- NEVER claim a model is "good" without the baseline number next to it.
- Show the exact command + dataset shape that produced every number.
- Surface leakage risks, distribution shift, and tiny-sample caveats up front.

## When NOT to do ML
If a rule, a SQL query, or a lookup table solves it — do that. ML is for when
the mapping is learned from data and worth the maintenance cost.

## LLM / fine-tune decisions
- Need facts → RAG, not fine-tune (facts go stale in weights).
- Need style/format → system prompt + few-shot first.
- Need a smaller/cheaper model to match a big one → distill (fine-tune on the
  big model's outputs) only after RAG + prompting plateau.
Build the eval set (50-200 labeled examples) BEFORE touching the prompt/model.
