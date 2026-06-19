---
name: ml-recommender-systems
description: >-
  Build recommendations via collaborative filtering, matrix factorization, content-based, and hybrid models with implicit/explicit feedback
---

# ml-recommender-systems

**Collaborative filtering (CF):** recommend from user-item interaction patterns. Memory-based: user-user or **item-item** kNN (item-item is more stable and scalable — Amazon's classic). Model-based: **matrix factorization** learns latent user/item vectors whose dot product predicts the rating/affinity — SVD for explicit ratings, **ALS or BPR** for implicit feedback (clicks/views, where absence ≠ dislike — you optimize ranking, not rating; libraries: implicit, LightFM). **Content-based:** recommend items similar to a user's past via item features/embeddings — solves item cold-start, no need for other users. **Hybrid** (e.g., LightFM combines CF + content) is usually best in production. **The defining pitfall — cold start:** new users/items have no interactions → CF fails; fall back to content-based, popularity, or onboarding signals. **Other pitfalls:** popularity bias (rich-get-richer — inject diversity/serendipity); sparsity (most user-item cells empty); evaluate with ranking metrics (Recall@K, NDCG, MAP, hit rate) via temporal/leave-last-out splits, NOT RMSE alone and never a random split that leaks the future; feedback loops bias future data. Implicit feedback dominates real systems — model it as ranking with negative sampling.

**Tools:** matrix factorization (SVD/ALS), item-item kNN, implicit/Surprise/LightFM, BPR, cold-start
