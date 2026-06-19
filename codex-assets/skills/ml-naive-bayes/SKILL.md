---
name: ml-naive-bayes
description: >-
  Naive Bayes probabilistic classifiers — fast baselines for text/spam and high-dimensional sparse features
---

# ml-naive-bayes

Applies Bayes' theorem with the 'naive' assumption that features are conditionally independent given the class. Despite the unrealistic assumption it works remarkably well for text classification and is extremely fast (one pass, O(n·d)), needs little data, and handles thousands of sparse features. **Pick the variant:** MultinomialNB for word counts/TF-IDF (default for text); ComplementNB for imbalanced text (often beats Multinomial); BernoulliNB for binary presence/absence features; GaussianNB for continuous features (assumes per-class normality). **Key hyperparam:** `alpha` Laplace/Lidstone smoothing (default 1.0) — prevents zero probability for unseen feature-class combos; tune it (smaller alpha = less smoothing). **Pitfalls:** probabilities are poorly calibrated (the independence violation pushes them toward 0/1) — use rankings/thresholds, not raw probabilities, or calibrate; correlated features get double-counted and hurt it; GaussianNB suffers when features are non-normal. Great as a fast, strong text baseline before reaching for heavier models; pair MultinomialNB with TF-IDF vectorization.

**Tools:** sklearn MultinomialNB/ComplementNB/BernoulliNB/GaussianNB, Laplace smoothing, TF-IDF
