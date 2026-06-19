---
name: research-linear-regression
description: >-
  Fit and diagnose OLS linear regression: model spec, coefficient interpretation, R-squared, assumptions (LINE), multicollinearity, dummy coding — use for predicting/explaining a continuous outcome
---

# research-linear-regression

Interpret each coefficient as: expected change in Y per one-unit increase in that X, HOLDING other predictors constant. Report unstandardized b (for units) and standardized beta (to compare predictor strength). Use **adjusted R-squared** (penalizes added predictors) over raw R-squared for model comparison; R-squared is variance explained, not model correctness.

Check the LINE assumptions via plots, not faith: **L**inearity (residuals vs fitted — no curve), **I**ndependence of errors (Durbin-Watson for time series), **N**ormality of residuals (QQ plot), **E**qual variance / homoscedasticity (residuals vs fitted — no fan). Heteroscedasticity? Use **robust (HC) standard errors**. Detect **multicollinearity** with VIF (> 5-10 = problem) — it inflates SEs and flips signs.

Encode categoricals as dummies (k-1 levels, one reference); add **interaction terms** when an effect depends on another variable, and center continuous predictors before interacting to ease interpretation. In Python use statsmodels (gives p-values, CIs) over sklearn for inference.

Pitfall: reading correlation as causation — regression on observational data is association, not effect. Second pitfall: extrapolating beyond the observed X range.

**Tools:** OLS, statsmodels/sklearn/R lm, VIF, residual plots, R-squared/adjusted, robust SE, dummy/interaction terms
