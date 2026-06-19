---
name: ml-density-hierarchical-clustering
description: >-
  DBSCAN/HDBSCAN and hierarchical/agglomerative clustering for arbitrary-shape clusters, outlier detection, and unknown k
---

# ml-density-hierarchical-clustering

Two families that don't need k upfront. **DBSCAN:** groups dense regions, marks sparse points as noise/outliers; finds arbitrary (non-convex) shapes. Hyperparams: `eps` (neighborhood radius — set via the k-distance elbow plot) and `min_samples` (≈2·dim). Pitfall: a single global eps fails when clusters have varying density → use **HDBSCAN** (varies density automatically, far more robust, main param `min_cluster_size`) — prefer it in 2026. **Hierarchical/agglomerative:** bottom-up merging by `linkage` — ward (minimizes variance, compact clusters, default), complete (tight), average, single (chaining, fragile). Produces a dendrogram you cut at a height to choose cluster count post hoc — great for exploration and nested structure. Cost: O(n²) memory/time, so it doesn't scale past ~10–50k points. **Shared pitfalls:** scale features first; both are distance-based and degrade in high dimensions (reduce dims first); DBSCAN struggles when density varies. Pick DBSCAN/HDBSCAN for outlier-aware, unknown-k, odd shapes; hierarchical for interpretable nested taxonomies on smaller data.

**Tools:** sklearn DBSCAN, HDBSCAN, AgglomerativeClustering, dendrogram, eps, min_samples, linkage
