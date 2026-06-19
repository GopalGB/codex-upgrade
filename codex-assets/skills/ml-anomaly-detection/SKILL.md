---
name: ml-anomaly-detection
description: >-
  Detect outliers/novelties/fraud with Isolation Forest, LOF, one-class SVM, and statistical methods under extreme imbalance
---

# ml-anomaly-detection

Find rare points that deviate from normal — fraud, defects, intrusions, monitoring. Usually unsupervised/semi-supervised because anomalies are scarce and unlabeled. **Algorithms:** Isolation Forest (isolates points via random splits — anomalies need fewer splits; fast, scalable, the strong default, set `contamination` to expected anomaly rate); Local Outlier Factor (compares local density to neighbors — catches local anomalies in varying-density data, but transductive); One-Class SVM (learns a boundary around normal data — sensitive to params, slower); autoencoder reconstruction error (deep, for images/high-dim/sequences — high error = anomaly); statistical (z-score/MAD/IQR for univariate, Mahalanobis for multivariate Gaussian, Extreme Value Theory for tails). **Steps:** scale features; set/tune contamination; score, then threshold by the score distribution (often the harder decision than the model). **Pitfalls:** evaluate with PR-AUC / precision@k on whatever labels you have — accuracy is meaningless; contamination misspecification swings results; concept drift means 'normal' changes over time (retrain/monitor); high dimensions dilute distance-based methods (reduce dims first). If you have labels, a supervised imbalanced-classification approach often beats pure anomaly detection.

**Tools:** IsolationForest, LocalOutlierFactor, OneClassSVM, autoencoder reconstruction, z-score, EVT
