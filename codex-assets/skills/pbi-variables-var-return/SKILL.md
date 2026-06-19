---
name: pbi-variables-var-return
description: >-
  Use VAR/RETURN to make DAX readable, avoid recomputation, and dodge the context-capture trap that bites filter-modifying measures
---

# pbi-variables-var-return

VAR stores an evaluated value once; RETURN yields the final expression. Use it to name intermediate logic and to prevent re-evaluating an expensive sub-expression. Example: `Sales YoY % = VAR Curr = [Total Sales] VAR Prev = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date])) RETURN DIVIDE(Curr - Prev, Prev)`. The critical, non-obvious rule: a VAR is evaluated in the filter context where it is DEFINED, not where it is USED. So `VAR Total = [Total Sales]` captures the value before any later CALCULATE changes context — this is exactly how you compute a baseline to divide by. Pitfall #1: people expect a VAR to recompute inside a later CALCULATE — it does not; if you need the recomputed value, put the measure inside the CALCULATE, not a VAR before it. Pitfall #2: using a VAR named the same as a column causes confusion; prefix vars (e.g. `__curr`). Pitfall #3: VARs cannot be referenced outside their RETURN scope or in sibling branches incorrectly. Bonus: VARs also short-circuit — wrap divide guards in a single VAR to evaluate the denominator once and reuse it, both readable and faster than repeating the sub-expression.

**Tools:** VAR, RETURN, DAX
