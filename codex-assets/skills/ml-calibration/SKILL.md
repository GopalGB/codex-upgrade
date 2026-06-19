---
name: ml-calibration
description: >-
  Calibrate predicted probabilities (Platt/isotonic) so outputs match true frequencies for thresholding, ranking, and decisions
---

# ml-calibration

A model can rank well (high AUC) yet output miscalibrated probabilities — a '0.8' should be correct 80% of the time. Calibration matters whenever you use probabilities for cost-sensitive decisions, thresholds, expected value, or downstream combination. **Who needs it:** SVMs, naive Bayes, boosted trees, and over-regularized/over-confident neural nets are typically miscalibrated; logistic regression is usually well-calibrated by construction. **Diagnose:** reliability diagram (predicted prob bucket vs observed frequency — diagonal = perfect), plus **Brier score** and **Expected Calibration Error (ECE)** as scalars. **Fix with sklearn CalibratedClassifierCV:** Platt scaling (fits a sigmoid — good for small data, assumes a sigmoid distortion) or **isotonic regression** (non-parametric, more flexible, needs more data — risk of overfitting on small sets). **The critical pitfall:** calibrate on a SEPARATE held-out set (or via CV inside CalibratedClassifierCV), never on the training data the model already saw — that yields falsely perfect calibration. **Also:** calibration changes probabilities but not the ranking/AUC; recalibrate after threshold/cost changes; class imbalance and dataset shift both wreck calibration — re-check in production.

**Tools:** CalibratedClassifierCV, Platt scaling, isotonic regression, reliability diagram, Brier score, ECE
