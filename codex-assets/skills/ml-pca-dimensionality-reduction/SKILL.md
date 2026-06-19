---
name: ml-pca-dimensionality-reduction
description: >-
  PCA and friends (t-SNE/UMAP) to compress features, remove multicollinearity, denoise, and visualize high-dimensional data
---

# ml-pca-dimensionality-reduction

**PCA** finds orthogonal directions of maximum variance via eigendecomposition of the covariance matrix (or SVD of centered X) and projects onto the top components. Use it to fight the curse of dimensionality, remove multicollinearity, denoise, speed up downstream models, and compress. **Steps:** standardize features first (PCA is variance-based — unscaled features dominate), fit, choose number of components from the scree plot or cumulative `explained_variance_ratio_` (e.g., keep 95%). Components are linear combinations — interpretability is lost. For sparse/text use TruncatedSVD (LSA) which skips centering. **Pitfalls:** PCA only captures linear structure and global variance — directions of max variance aren't always the discriminative ones (LDA is supervised if you need class separation); never fit PCA on test data (fit on train, transform both); outliers distort components. **For visualization only:** t-SNE and UMAP capture non-linear local structure for 2D plots — but never use their output as ML features, distances/cluster sizes between groups are not meaningful, and t-SNE is sensitive to perplexity. UMAP is faster and preserves more global structure than t-SNE.

**Tools:** sklearn PCA, TruncatedSVD, t-SNE, UMAP, explained_variance_ratio_, scree plot
