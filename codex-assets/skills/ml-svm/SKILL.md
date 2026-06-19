---
name: ml-svm
description: >-
  Support Vector Machines for max-margin classification/regression, strong in high-dimensional or small-sample problems with kernel non-linearity
---

# ml-svm

Finds the hyperplane maximizing the margin to the nearest points (support vectors); the kernel trick (RBF, polynomial) maps to high-dim space implicitly to learn non-linear boundaries without computing the mapping. Excels when p is large relative to n (text, genomics) and on small/medium clean datasets. **Key hyperparams:** `C` (regularization — low C = wider margin, more tolerance for misclassification = more bias; high C = tight fit = more variance) and `gamma` for RBF (high gamma = each point's influence is local = wiggly boundary, overfits; low gamma = smooth). Tune C and gamma jointly on a log grid via cross-validation — they interact strongly. **Hard requirement:** standardize/scale features — SVM is distance-based and breaks on unscaled data. **Pitfalls:** training is O(n²)–O(n³), so it does NOT scale to large n — use LinearSVC or switch to boosting beyond ~50k–100k rows; SVC probabilities (probability=True) come from slow Platt scaling and are mediocre — prefer decision_function + separate calibration. RBF SVM is rarely the best choice on big tabular data vs gradient boosting.

**Tools:** sklearn SVC/SVR, RBF/linear/poly kernel, kernel trick, C, gamma, LinearSVC
