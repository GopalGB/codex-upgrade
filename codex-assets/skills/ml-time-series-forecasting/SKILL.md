---
name: ml-time-series-forecasting
description: >-
  Forecast temporal data with ARIMA/SARIMA, Prophet, ETS, and ML approaches — handling trend, seasonality, and stationarity
---

# ml-time-series-forecasting

**Classical:** ARIMA(p,d,q) models autocorrelation — d differences to reach stationarity (test with ADF/KPSS), p from PACF, q from ACF; **SARIMA** adds seasonal terms; **ETS/Holt-Winters** for level+trend+seasonality via exponential smoothing (robust, simple). **Prophet** (Meta) decomposes trend + multiple seasonalities + holidays, tolerates missing data and outliers, needs little tuning — great for business series with strong seasonality, weaker for short/high-frequency. **ML approach:** turn it into supervised learning with lag features, rolling stats, and calendar features, then use LightGBM (often wins on multiple related series / many regressors) — but you must avoid leaking the future into features. **Validation is the make-or-break:** use rolling/expanding-window backtesting (walk-forward), NEVER random k-fold or a shuffled split — that leaks the future and gives fantasy accuracy. **Pitfalls:** check/enforce stationarity for ARIMA; account for structural breaks/regime change; don't trust long horizons (uncertainty compounds — show prediction intervals); beware data leakage from look-ahead features; handle missing timestamps and resampling explicitly. Always benchmark against naive (last value) and seasonal-naive.

**Tools:** statsmodels SARIMA, Prophet, ETS/Holt-Winters, ADF test, ACF/PACF, lag features, backtesting
