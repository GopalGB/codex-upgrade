---
name: pbi-iterators-sumx-averagex
description: >-
  Row-by-row aggregation with SUMX/AVERAGEX/MAXX when you need per-row math before aggregating, plus context-transition gotchas
---

# pbi-iterators-sumx-averagex

Iterators (X-functions) evaluate an expression for each row of a table, then aggregate. Use them whenever the math must happen at row grain before summing: `Revenue = SUMX(Sales, Sales[Qty] * Sales[UnitPrice])`. Doing `SUM(Sales[Qty]) * SUM(Sales[UnitPrice])` is the classic wrong answer — it multiplies grand totals, not line items. Weighted average: `AVERAGEX(VALUES(Product[Category]), [Total Sales])` averages across categories, not rows. RANKX needs the table to rank over: `Rank = RANKX(ALL(Product[Name]), [Total Sales],, DESC)`. Iterators establish row context but NOT filter context — to make a measure inside the iterator respect the current row, context transition via CALCULATE happens automatically when you reference a measure (a measure is implicitly wrapped in CALCULATE). Pitfall #1: iterating a huge fact table with a complex expression is slow — iterate the smallest table that gives correct grain (often a dimension via VALUES). Pitfall #2: nested iterators multiply cardinality and can explode evaluation time. Pitfall #3: referencing a column without an aggregator inside SUMX over the wrong table gives a single-context error. Prefer SUM over SUMX when no per-row product is needed — the engine optimizes plain SUM better.

**Tools:** SUMX, AVERAGEX, MAXX, MINX, RANKX, COUNTX
