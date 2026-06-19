---
name: xls-power-pivot-dax
description: >-
  Power Pivot data model, relationships, DAX measures (CALCULATE/FILTER), row vs filter context, time intelligence, SUMX iterators
---

# xls-power-pivot-dax

Power Pivot loads multiple tables into an in-memory **Data Model** and links them with **relationships** (one-to-many on key columns) — replacing giant flattened VLOOKUP sheets. Write **DAX measures** (not calculated columns when you can avoid them; measures compute at query time and are smaller). Master the two contexts: **row context** (current row, in iterators/calc columns) vs **filter context** (slicers, pivot rows/cols). **CALCULATE(expr, filters…)** is the heart of DAX — it modifies filter context: `Sales YTD := CALCULATE(SUM(Sales[Amt]), DATESYTD('Date'[Date]))`. Iterators **SUMX/AVERAGEX** evaluate row-by-row then aggregate — use for weighted ratios: `SUMX(Sales, Sales[Qty]*Sales[Price])`. **RELATED** pulls a value across a relationship. Time intelligence (TOTALYTD, SAMEPERIODLASTYEAR, DATEADD) needs a proper marked **Date table**. Pitfalls: don't build relationships on text keys with mismatched whitespace; avoid bi-directional filters unless needed (ambiguity/perf); calculated columns bloat the model — prefer measures. This powers pivots/charts with KPIs impossible in plain pivots (distinct count, weighted avg, YoY).

**Tools:** Power Pivot, DAX, CALCULATE, SUMX, RELATED, Data Model
