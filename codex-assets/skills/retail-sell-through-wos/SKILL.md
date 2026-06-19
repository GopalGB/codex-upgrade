---
name: retail-sell-through-wos
description: >-
  Compute sell-through %, weeks-of-supply (WOS), sell-through rate and forward cover to flag slow/fast movers for inventory health, in-season tracking, reorder timing
---

# retail-sell-through-wos

**Sell-through % = units sold / (units sold + units on-hand)** over a period (or units sold / units received for a buy). It answers 'how much of what I bought is gone.' Apparel benchmark: ~60-70% full-price sell-through before markdown is healthy; <50% at midpoint signals trouble.

**Weeks of Supply = current on-hand units / average weekly sales rate** — the forward cover. WOS=12 means at current pace you'll run out in 12 weeks. Compare to lead time + review period: if WOS < lead time, you'll stock out before a reorder lands — reorder NOW.

The expert move: track sell-through against a **planned sell-through curve** (cumulative % by week of life). Being above curve = chase/reorder (it's a winner); below curve = markdown candidate. Use **rate of sale (units/store/week)** to compare SKUs of different distribution fairly.

Pitfalls: confusing sell-through (% of inventory) with sell-out (gone entirely) and with **turn** (annualized); reading WOS without seasonality (10 WOS in October might be 2 WOS in December's pace); and aggregating to category level so a dead SKU hides behind a hot one. Always drill to SKU x store. Stockout-censored weeks understate true rate of sale.

**Tools:** sell-through % formula, weeks of supply, forward weeks of cover, sell-through curve
