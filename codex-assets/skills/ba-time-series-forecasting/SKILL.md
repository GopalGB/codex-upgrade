---
name: ba-time-series-forecasting
description: >-
  Forecast business series: decompose trend/seasonality, pick naive/MA/Holt-Winters/ARIMA/Prophet by data shape, hold out + backtest with MAPE/RMSE; avoid leakage and random-split on time data.
---

# ba-time-series-forecasting

First plot and decompose the series into trend + seasonality + residual (STL or seasonal_decompose) — the shape dictates the method. Ladder of models by complexity: naive/seasonal-naive (always your baseline — beat it or stop), moving average, simple/double/triple exponential smoothing (Holt-Winters = level+trend+seasonality, great for clean seasonal demand), ARIMA/SARIMA (autocorrelated series; make stationary via differencing, read ACF/PACF or let pmdarima auto_arima search p,d,q), Prophet (multiple seasonalities + holidays + missing data, robust default for business). Evaluate with a time-ordered holdout, NEVER a random split (that leaks the future); use rolling-origin / walk-forward backtesting and report MAPE for interpretability plus RMSE for penalizing big misses, both vs the naive baseline. Always produce a prediction interval, not a point — stakeholders need the range. Expert moves: log-transform multiplicative growth; add known regressors (promos, price, holidays); detect and flag changepoints. Pitfalls: data leakage (scaling/feature-engineering before the split, or using same-period actuals); forecasting far beyond the seasonal cycles you have; ignoring intermittent/zero-heavy demand (use Croston, not ARIMA); trusting a model that can't beat seasonal-naive; extrapolating a trend with no causal basis.

**Tools:** statsmodels, Prophet, pmdarima, Excel FORECAST.ETS, pandas
