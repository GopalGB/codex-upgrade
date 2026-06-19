---
name: ml-classification-metrics
description: >-
  Choose and interpret classification metrics (ROC-AUC, PR-AUC, F1, precision/recall) for the actual business cost
---

# ml-classification-metrics

Start from the confusion matrix: precision = TP/(TP+FP) (of predicted positives, how many right — cost of false alarms), recall/sensitivity = TP/(TP+FN) (of actual positives, how many caught — cost of misses). **F1** is their harmonic mean; use **F-beta** to weight recall (β>1) or precision (β<1) per business cost. **ROC-AUC** = threshold-independent ranking quality, but it's misleadingly optimistic under heavy class imbalance because the huge true-negative count flatters the FPR axis. **PR-AUC (average precision)** is the right summary for imbalanced/rare-positive problems. **Log-loss/Brier** judge probability quality (use when calibrated probabilities matter). **MCC** is a balanced single number robust to imbalance. **Decision steps:** define the cost of FP vs FN first, then pick the metric and the operating threshold from the PR/ROC curve — don't default to 0.5. **Pitfalls:** never report accuracy on imbalanced data; report a metric tied to the decision, not the most flattering one; for multiclass choose macro (treats classes equally — surfaces minority failure) vs weighted (by support) vs micro (aggregate) deliberately. Always show the confusion matrix, not just a scalar.

**Tools:** confusion matrix, ROC, precision-recall curve, F-beta, log-loss, MCC, sklearn metrics
