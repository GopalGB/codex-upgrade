---
name: ml-imbalanced-data
description: >-
  Handle skewed class distributions (fraud/churn/rare-event) so the minority class is actually learned, not ignored
---

# ml-imbalanced-data

When one class is rare (1–5%), accuracy is useless (predicting majority scores 95%+) and models ignore the minority. **Techniques, roughly in order of preference:** (1) **algorithm-level cost weighting** — `class_weight='balanced'` (sklearn) or `scale_pos_weight = neg/pos` (XGBoost/LightGBM); cheap, no data distortion, usually try first. (2) **Threshold tuning** — don't predict at 0.5; pick the operating point from the precision-recall curve to match your cost tradeoff (often the single biggest lever). (3) **Resampling via imbalanced-learn** — SMOTE synthesizes minority points by interpolating between neighbors (ADASYN focuses on hard regions); random undersampling for huge data; combine (SMOTEENN/Tomek). **The non-negotiable pitfall:** apply SMOTE/resampling ONLY on the training fold inside a Pipeline — resampling before the split leaks synthetic neighbors into validation and produces fake-great scores. **Metrics:** use PR-AUC (more informative than ROC-AUC under heavy imbalance), F1/F-beta, recall@precision — never plain accuracy. Also question whether it's really a rare-event detection / anomaly problem. Collect more minority data if you can — it beats every trick.

**Tools:** SMOTE/ADASYN, class_weight, scale_pos_weight, threshold tuning, imbalanced-learn, PR-AUC
