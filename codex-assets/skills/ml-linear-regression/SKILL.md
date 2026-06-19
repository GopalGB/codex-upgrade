---
name: ml-linear-regression
description: >-
  Fit and diagnose linear/OLS regression for continuous targets when relationships are roughly additive and interpretability matters
---

# ml-linear-regression

Models y = Xβ + ε by minimizing squared residuals. Closed form β = (XᵀX)⁻¹Xᵀy is O(n·p² + p³); for large p use SGD/iterative solvers instead. Use when the signal is approximately linear, you need coefficient interpretability, and want a fast baseline. **Assumptions to check (the real work):** linearity, no multicollinearity (VIF < 5–10), homoscedastic residuals, independent errors, roughly normal residuals for valid p-values. **Steps:** standardize features so coefficients compare; fit; plot residuals-vs-fitted (funnel shape = heteroscedasticity → log-transform y or use weighted least squares / robust HC3 SE); check Q-Q plot. Report R² and adjusted R² (penalizes added features), plus RMSE on held-out data. **Pitfall #1:** extrapolating beyond the training range — linear fits go wild outside support. **Pitfall #2:** multicollinearity inflates coefficient variance so signs flip and 'feature importance' from raw coefficients becomes meaningless — drop/combine correlated features or move to ridge. Always split train/test before judging — in-sample R² always overstates.

**Tools:** scikit-learn LinearRegression, statsmodels OLS, normal equation, gradient descent
