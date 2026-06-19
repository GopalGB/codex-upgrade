---
name: xls-groupby-pivotby
description: >-
  GROUPBY and PIVOTBY dynamic-array aggregation functions — formula-based pivot tables that auto-refresh, with custom LAMBDA aggregators
---

# xls-groupby-pivotby

**GROUPBY** and **PIVOTBY** (365, 2024+) build live summary tables from a formula — no manual refresh like PivotTables. `=GROUPBY(row_fields, values, function, [field_headers], [total_depth], [sort_order], [filter_array])`. Function can be a builtin (SUM, AVERAGE, COUNT, MAX) or a LAMBDA, or PERCENTOF for share-of-total. Example: `=GROUPBY(Sales[Region], Sales[Amt], SUM, 3, 2)` groups by region with headers and subtotals, sorted descending. **PIVOTBY** adds a column dimension: `=PIVOTBY(Sales[Region], Sales[Year], Sales[Amt], SUM)` makes a true cross-tab. Both accept multiple fields by stacking with HSTACK. Advantages over PivotTables: recalc automatically, spill so charts auto-grow, compose with FILTER/SORT. Pitfalls: these are 365-only (break in older Excel — `#NAME?`), so don't ship to 2019 users; large data can be slower than a cached PivotTable; for drill-down, slicers, or printed reports a classic PivotTable is still better. Use GROUPBY for dashboards that must stay live.

**Tools:** GROUPBY, PIVOTBY, PERCENTOF, HSTACK
