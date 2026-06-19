---
name: ml-cross-validation
description: >-
  Design leakage-free validation (k-fold, stratified, grouped, time-series) to estimate generalization honestly
---

# ml-cross-validation

Cross-validation estimates out-of-sample performance by rotating which fold is held out, averaging the score across folds — far more stable than a single split. **Pick the splitter by data structure (this is where people fail):** StratifiedKFold for classification (preserves class ratios per fold — mandatory for imbalance); GroupKFold when rows share an entity (same user/patient/device) so no group leaks across folds; **TimeSeriesSplit for temporal data** — never shuffle time series, train only on the past and validate on the future (expanding/rolling window) or you leak the future and get fantasy scores. Standard k=5 or 10; repeated k-fold reduces variance; nested CV when you also tune hyperparameters (outer loop = honest estimate, inner loop = tuning) — otherwise tuning leaks into the estimate. **The cardinal rule:** fit ALL preprocessing (scaling, imputation, encoding, feature selection, SMOTE) INSIDE each fold via a Pipeline — fitting on the full dataset before CV leaks test stats and inflates scores. Report mean ± std; a high-variance CV signals instability or too-small folds.

**Tools:** sklearn KFold, StratifiedKFold, GroupKFold, TimeSeriesSplit, cross_val_score, Pipeline
