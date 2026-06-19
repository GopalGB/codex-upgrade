---
name: ml-kmeans-clustering
description: >-
  Partition data into k clusters via k-means for customer segmentation, vector quantization, and unsupervised grouping
---

# ml-kmeans-clustering

Iteratively assigns points to the nearest centroid then recomputes centroids (Lloyd's algorithm) to minimize within-cluster sum of squares (inertia); O(n·k·d·iters). Use k-means++ init (sklearn default) to avoid bad random starts. Fast and scalable (MiniBatchKMeans for huge data); the go-to for roughly spherical, similar-sized clusters. **Choosing k (the hard part):** elbow method (plot inertia vs k, find the kink), silhouette score (−1…1, higher = better separation — more reliable than elbow), or gap statistic. **Mandatory preprocessing:** scale features (it's distance-based) and consider PCA first in high dimensions. **Pitfalls:** you must pre-specify k; assumes convex, isotropic, equal-variance clusters — fails on elongated, varied-density, or non-convex shapes (use DBSCAN/GMM there); sensitive to outliers (they drag centroids — consider k-medoids); non-deterministic (run n_init≥10, sklearn now defaults to 'auto'). Inertia always decreases with k, so never pick k by minimizing it. Empty clusters can occur with bad k.

**Tools:** sklearn KMeans, MiniBatchKMeans, k-means++, elbow method, silhouette score
