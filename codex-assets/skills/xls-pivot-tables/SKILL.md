---
name: xls-pivot-tables
description: >-
  PivotTables: build, group dates/numbers, value field settings, % of total / running total, calculated fields, slicers/timelines, GETPIVOTDATA
---

# xls-pivot-tables

Build from a named Table (so the source auto-extends). Drag fields to Rows/Columns/Values/Filters. **Value Field Settings** > Summarize By (Sum/Count/Average) and **Show Values As** for `% of Grand Total`, `% of Parent Row`, `Running Total In`, `Rank`, `% Difference From` — these compute without extra columns. **Group** dates by year/quarter/month (right-click > Group) or numbers into bins. Add **slicers** (Insert > Slicer) and **timelines** for date filtering; one slicer can drive multiple pivots via Report Connections. **Calculated Fields** (PivotTable Analyze > Fields, Items & Sets) add formula columns, but they aggregate-then-calculate (so `Sum(Price)/Sum(Qty)` not avg of ratios — a classic trap; for true weighted ratios use Power Pivot/DAX measures instead). Refresh with Alt+F5 (or PivotTable Options > Refresh on open). **GETPIVOTDATA** pulls a specific cell reliably for dashboards — disable auto-GETPIVOTDATA if you want plain refs. Pitfall: stale source range — always base on a Table or dynamic named range.

**Tools:** PivotTable, slicers, timelines, GETPIVOTDATA, calculated fields
