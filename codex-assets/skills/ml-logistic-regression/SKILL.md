---
name: ml-logistic-regression
description: >-
  Binary/multiclass classification with calibrated probabilities and interpretable log-odds when you need a transparent linear classifier
---

# ml-logistic-regression

Models P(y=1) = σ(Xβ) via the logistic sigmoid; fit by maximizing log-likelihood (minimizing log-loss / cross-entropy), solved with L-BFGS, newton-cg, or saga. Coefficients are log-odds: exp(βⱼ) is the odds ratio per unit increase — genuinely interpretable. Use as the default linear classifier baseline; outputs are reasonably calibrated probabilities out of the box (unlike SVM/trees). **Key hyperparams:** `C` (inverse regularization — smaller = stronger penalty; tune on a log grid 1e-3…1e2), `penalty` (l2 default; l1/elasticnet with saga for sparsity), `class_weight='balanced'` for skew. **Multiclass:** multinomial (true softmax) beats one-vs-rest for probability quality. **Steps:** scale features (regularization is scale-sensitive), fit, threshold at 0.5 only if costs are symmetric — otherwise pick threshold from the PR/ROC curve. **Pitfall:** perfect separation makes coefficients diverge to ±∞ — regularization fixes it. Don't read raw coefficient magnitude as importance unless features are standardized.

**Tools:** sklearn LogisticRegression, softmax/multinomial, log-loss, class_weight
