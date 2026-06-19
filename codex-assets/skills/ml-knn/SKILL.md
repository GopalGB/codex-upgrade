---
name: ml-knn
description: >-
  k-Nearest Neighbors instance-based classification/regression for local non-parametric patterns and quick baselines
---

# ml-knn

Lazy learner: stores all training data, predicts by majority vote (classification) or mean (regression) of the k closest points under a distance metric. No training cost; all cost is at inference — O(n·d) per query with brute force, reduced by KD-tree (low d) or ball-tree. Use as a quick non-linear baseline or when the decision boundary is highly local/irregular. **Key hyperparams:** `n_neighbors` k (small k = low bias/high variance/noisy; large k = smooth/high bias — tune via CV, odd values avoid ties), `weights='distance'` (closer neighbors count more — usually helps), and the distance `metric` (Euclidean default; Manhattan for high-dim). **Mandatory:** scale features — distances are dominated by large-magnitude features otherwise. **Pitfalls:** curse of dimensionality — in high dimensions all points become equidistant and kNN degrades; do PCA/feature selection first. Slow and memory-heavy at scale (stores everything, scans at query time) — use approximate NN (FAISS, HNSW) for large data. Sensitive to irrelevant features and class imbalance.

**Tools:** sklearn KNeighborsClassifier/Regressor, KD-tree, ball-tree, distance weighting
