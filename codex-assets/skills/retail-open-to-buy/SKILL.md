---
name: retail-open-to-buy
description: >-
  Calculate and manage Open-To-Buy (OTB) dollar plans: planned purchases, EOM/BOM stock, monthly receipt flow for buy budgets, in-season buying control
---

# retail-open-to-buy

OTB controls how many receipt dollars a buyer can still commit without overbuying. Core identity: **OTB (at retail) = Planned EOM Stock + Planned Sales + Planned Markdowns - BOM Stock - Merchandise On Order**. Convert to cost by x (1 - IMU%).

Build it monthly: derive planned BOM from a **stock-to-sales ratio** (BOM stock / sales for that month) — typically 3-5 for apparel, lower for fast turners. Planned EOM of one month = planned BOM of the next. Always include planned markdowns and shrink in the reduction side or OTB inflates.

The expert move: run OTB in-season every week. If sales run ahead of plan, OTB *opens up* (chase the winner); if behind, it tightens and you cancel/push orders. Watch **on-order** religiously — committed POs not yet received eat OTB even though stock looks low.

Pitfalls: planning at cost when sales/stock are at retail (mixing valuations); forgetting markdowns (the #1 cause of overbought, marked-down-to-death seasons); and ignoring lead time — Q4 OTB must be largely committed by mid-Q3. Negative OTB = stop buying; positive but small = chase only proven sellers.

**Tools:** OTB formula, stock-to-sales ratio, retail method of accounting
