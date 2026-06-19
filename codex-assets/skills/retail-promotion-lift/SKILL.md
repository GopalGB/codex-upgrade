---
name: retail-promotion-lift
description: >-
  Measure promotional lift, baseline uplift, halo/cannibalization and promo ROI/profitability vs pre-promo baseline for promo analysis, campaign effectiveness, incrementality
---

# retail-promotion-lift

The only number that matters is **incremental** units, not total. Build a **baseline** from non-promo weeks (same DOW, deseasonalized), then **lift % = (promo sales - baseline) / baseline**. Incremental units = promo sales - baseline.

Promo ROI = (incremental margin - promo cost) / promo cost. Incremental margin = incremental units x discounted margin — discounted, because you gave price away on every unit including the ones that would have sold anyway (the **subsidy/pull-forward** cost).

The expert move: net out **cannibalization** (the promo steals sales from full-price siblings — measure the dip in substitute SKUs) and add **halo** (basket attach: promo drives traffic that buys non-promo items — measure incremental basket size of promo redeemers vs control). A promo that 'works' on its own SKU but cannibalizes a higher-margin sibling can be margin-negative.

Pitfalls: counting total promo sales as the win (most would have happened), ignoring **forward-buy/pantry-loading** (a deep promo just pulls future demand forward — measure the post-promo trough), and no control group. Use matched-store or pre/post with a non-promoted control panel to isolate true incrementality.

**Tools:** baseline uplift, incremental margin, cannibalization rate, promo ROI, halo effect
