---
name: pbi-measures-vs-calc-columns
description: >-
  Decide measure vs calculated column vs visual calculation; when each stores/computes and why measures win for aggregation
---

# pbi-measures-vs-calc-columns

Calculated columns compute row-by-row at refresh and are stored in the VertiPaq model (consume RAM, hurt compression). Use them only when you need a value materialized for slicing, relationships, or RLS filters — e.g. `Margin Bucket = IF([UnitPrice]-[Cost] > 10, "High", "Low")`. Measures compute at query time in filter context, store nothing, and are the default for any aggregation: `Total Sales = SUMX(Sales, Sales[Qty] * Sales[Price])`. Never write `Total Sales = SUM(Sales[LineTotal])` as a column then sum the column — that bloats the model. Rule: if it aggregates, make it a measure; if it categorizes a row for grouping/filtering, make it a column. Pitfall: people create a calculated column referencing a measure (`= [Total Sales]`) — this fails or returns a constant because measures need filter context a column row doesn't provide. For row-relative running totals scoped to one visual, prefer the now-GA (May 2026) Visual Calculations instead of either, since they avoid model bloat entirely. Always default to measure first; only materialize a column when you hit a concrete need.

**Tools:** DAX, SUM, RELATED, calculated columns, measures, visual calculations
