---
name: pbi-calculate-filter-context
description: >-
  Master CALCULATE to modify filter context — the single most important DAX function; filter args, removing/keeping filters, context transition
---

# pbi-calculate-filter-context

CALCULATE is the only function that modifies filter context. Syntax: `CALCULATE(<expression>, <filter1>, <filter2>...)`. Each filter argument either adds or overrides context. Simple boolean filters are sugar: `CALCULATE([Total Sales], Product[Color] = "Red")` is internally `CALCULATE([Total Sales], FILTER(ALL(Product[Color]), Product[Color]="Red"))` — note it REPLACES any existing Color filter. To keep the existing filter and intersect, wrap in `KEEPFILTERS(Product[Color]="Red")`. To ignore filters use `ALL`/`REMOVEFILTERS`: `% of Total = DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Product)))`. CALCULATE also triggers context transition: inside an iterator (SUMX) or calculated column, the current ROW becomes a filter. This is why `CALCULATE([Total Sales])` inside SUMX over Customers gives per-customer totals. Pitfall #1: filter arguments can only be boolean conditions or table expressions — you cannot pass a measure directly as a filter. Pitfall #2: applying ALL on a whole table when you only meant one column wipes more than intended — target the specific column. Pitfall #3: forgetting that boolean filters override silently, producing wrong subtotals.

**Tools:** CALCULATE, FILTER, ALL, ALLEXCEPT, KEEPFILTERS, REMOVEFILTERS
