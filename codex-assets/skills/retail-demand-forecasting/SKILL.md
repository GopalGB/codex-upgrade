---
name: retail-demand-forecasting
description: >-
  Forecast retail demand with moving averages, exponential smoothing, Holt-Winters seasonality and MAPE accuracy tracking for sales forecasts, baseline demand, replenishment planning
---

# retail-demand-forecasting

Pick the method to the demand shape. Stable SKU: **simple/weighted moving average**. Trended: **double exponential (Holt)**. Seasonal (apparel, holiday): **Holt-Winters triple smoothing** with level, trend, and seasonal components — multiplicative when seasonal swing scales with volume.

Build a **seasonal index**: avg each period's sales / overall avg; a December index of 1.8 means decompose, forecast the deseasonalized baseline, then re-apply the index. Smoothing alpha 0.1-0.3 = stable, 0.4+ = reactive to recent change.

The expert move: forecast a clean **baseline** separately from **promo/event lift**, then add lift back. Never let a past promo spike inflate next year's baseline — strip promo weeks or it compounds. Track **WMAPE** (weighted by volume) not plain MAPE, which explodes on low-volume SKUs.

Pitfalls: forecasting on shipments instead of POS sell-through (whip effect); ignoring stockout-censored demand (lost sales look like low demand, you under-forecast forever — uncensor); and over-trusting one global model — A-items deserve hand review, C-items get auto-stat. Anchor new-product forecasts to a like-item analog, not a flat guess.

**Tools:** Holt-Winters, exponential smoothing alpha, MAPE/WMAPE, seasonal index
