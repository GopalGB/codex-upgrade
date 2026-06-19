---
name: xls-dashboards
description: >-
  Interactive dashboards: KPI cards, slicers/timelines wiring, dynamic titles, sparklines, camera tool, layout and single-source design
---

# xls-dashboards

Architect in layers: **raw data (Table/Data Model) → calc/staging sheet → dashboard sheet** (never compute on the display sheet). Feed visuals from **GROUPBY/PIVOTBY spills** or PivotTables so they refresh live. **KPI cards**: big number = a measure/formula cell, with a dynamic delta vs prior period and a CF arrow icon. **Slicers + timelines** are the interactivity layer — wire ONE slicer to multiple PivotTables/charts via Report Connections so the whole dashboard filters together; for formula-based dashboards drive a control cell with a dropdown and have FILTER/CHOOSE react. **Dynamic titles**: `="Sales — "&selectedRegion&" — "&TEXT(TODAY(),"mmm yyyy")` linked to a chart title. **Sparklines** for trend in tight space; the **Camera tool** mirrors a live range as a resizable picture for flexible layout. Form controls (option buttons, scrollbars) drive scenario switching. Pitfalls: volatile functions + many charts = sluggish refresh — minimize OFFSET/INDIRECT; keep one source of truth; design for the smallest screen it'll be viewed on; lock the layout with sheet protection leaving only inputs/slicers editable.

**Tools:** slicers, sparklines, GROUPBY, camera tool, form controls, named refs
