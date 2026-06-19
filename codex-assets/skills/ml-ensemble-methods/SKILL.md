---
name: ml-ensemble-methods
description: >-
  Combine models via bagging, boosting, stacking, and voting to cut variance/bias and squeeze out final accuracy
---

# ml-ensemble-methods

Three orthogonal strategies. **Bagging:** train models in parallel on bootstrap samples and average — reduces variance, needs high-variance base learners (deep trees → random forest); doesn't reduce bias. **Boosting:** train sequentially, each correcting prior errors — reduces bias (and variance), needs weak learners (shallow trees → XGBoost/LightGBM); the accuracy king on tabular but can overfit noise. **Stacking:** train diverse base models (e.g., GBM + RF + linear + kNN), then a meta-learner (often logistic/linear) learns to combine their predictions — gains come from base-model **diversity**, not individual strength. **Voting:** hard (majority) or soft (average probabilities — usually better) for a quick combine. **The stacking pitfall that ruins it:** the meta-learner must train on **out-of-fold** predictions of the base models — feeding it in-sample base predictions leaks and overfits massively; use cross_val_predict. **Practical notes:** ensembles cost inference latency/complexity for often small accuracy gains — justify it; diversity (different algorithms/features/seeds) matters more than adding copies of the same model; a single tuned GBM frequently beats a sloppy ensemble.

**Tools:** VotingClassifier, StackingClassifier, bagging, boosting, blending, out-of-fold predictions
