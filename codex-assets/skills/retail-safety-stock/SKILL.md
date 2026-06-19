---
name: retail-safety-stock
description: >-
  Compute safety stock and reorder points with service-level Z-scores, demand and lead-time variability for inventory buffers, stockout prevention, fill rate targets
---

# retail-safety-stock

Safety stock buffers against demand AND lead-time variability. The statistically correct formula when both vary: **SS = Z x sqrt( LT x sigma_d^2 + d^2 x sigma_LT^2 )**, where Z = service-level factor (NORM.S.INV(0.95)=1.65, 0.975=1.96, 0.99=2.33), LT = avg lead time, sigma_d = std dev of demand per period, d = avg demand, sigma_LT = std dev of lead time (in same period units).

**Reorder point = (d x LT) + SS**. Order when on-hand + on-order crosses ROP.

The expert move: set Z by item criticality and margin, not a blanket 95% — a high-margin A-item destination SKU may justify 99% (Z=2.33) while a C-item gets 90% (Z=1.28). Doubling service from 95% to 99% can roughly double safety stock, so segment via ABC.

Pitfalls: using only the simplified **SS = Z x sigma_d x sqrt(LT)** when lead time is the bigger variance source (overseas freight) — it under-buffers badly. Match units (weekly demand needs weekly sigma and lead time in weeks). Recompute sigma seasonally; one annual number over-stocks slow months and stocks out in peak. Lead-time variance usually dominates — fix supplier reliability before piling on buffer.

**Tools:** Z-score safety stock formula, reorder point, NORM.S.INV in Excel
