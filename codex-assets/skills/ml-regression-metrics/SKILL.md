---
name: ml-regression-metrics
description: >-
  Select and read regression error metrics (RMSE, MAE, MAPE, R²) matched to scale, outliers, and business meaning
---

# ml-regression-metrics

**MAE** (mean absolute error) is robust to outliers and reads in target units — use when large errors shouldn't be punished disproportionately. **RMSE** squares errors so it penalizes large misses heavily — use when big errors are especially bad; it's the default optimization target but outlier-sensitive. **MAPE** (mean absolute percentage error) is scale-free and intuitive to stakeholders but explodes near zero targets and is asymmetric (penalizes over-prediction more) — avoid when targets approach 0; consider SMAPE or MSLE (log errors, for multiplicative/skewed targets, penalizes under-prediction more). **R²** = fraction of variance explained (1 = perfect, 0 = no better than the mean, can go negative on test); **adjusted R²** penalizes adding features. **Steps:** report an in-units error (MAE/RMSE) plus R² for context, against a naive baseline (predict the mean / last value). **Pitfalls:** R² alone hides bias and heteroscedasticity — always plot residuals vs predicted (look for funnels, curves, structure); a high R² with patterned residuals means a misspecified model; choose the metric you optimize (loss) to match the metric you report. For heavy-tailed targets, use Huber/quantile loss.

**Tools:** sklearn RMSE/MAE/MAPE, R², adjusted R², MSLE, Huber loss, residual plots
