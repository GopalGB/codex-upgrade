---
name: ml-regularization
description: >-
  Apply L1/L2/ElasticNet penalties to control overfitting, induce sparsity, and stabilize coefficients in linear and other models
---

# ml-regularization

Regularization adds a penalty to the loss to shrink coefficients. **L2 (Ridge):** adds λ·Σβ²; shrinks all coefficients smoothly toward zero, never exactly zero; handles multicollinearity well by spreading weight across correlated features; has closed form (XᵀX+λI)⁻¹Xᵀy. **L1 (Lasso):** adds λ·Σ|β|; drives some coefficients exactly to zero → automatic feature selection and sparse models; among correlated features it arbitrarily picks one. **ElasticNet:** α·L1 + (1-α)·L2 — use when p≫n and features are grouped/correlated (gets Lasso sparsity + Ridge stability). **The core mechanic:** larger λ = more bias, less variance — tune λ by cross-validation (LassoCV/RidgeCV automate this). **Pitfall #1:** you MUST standardize features first — penalties act per-coefficient, so unscaled features get unfairly penalized. **Pitfall #2:** don't penalize the intercept. Same idea = weight decay in neural nets (L2). When in doubt between L1 and L2: need feature selection → L1; just need stability → L2; both/correlated → ElasticNet.

**Tools:** Ridge, Lasso, ElasticNet, LogisticRegression penalty, weight decay
