---
name: pbi-drillthrough-tooltips
description: >-
  Build drillthrough pages and report-page tooltips to give detail-on-demand without cluttering the main report
---

# pbi-drillthrough-tooltips

Drillthrough: create a detail page, drag the field users will drill on (e.g. Product) into the Drillthrough well in the Visualizations pane — Power BI auto-adds a Back button and passes the clicked context. Users right-click any visual with that field > Drill through > [page]. Enable 'Keep all filters' so the source page's filter context carries over. Cross-report drillthrough (toggle in page settings) lets you drill from one report to a detail page in another report in the same workspace — match field names exactly. Report-page tooltips: design a small page (Page Information > Allow use as tooltip; set page size to Tooltip), then on a visual set Format > Tooltip > Type = Report page > pick it; hovering shows a rich mini-report scoped to the hovered data point. Pitfall #1: drillthrough field must exist on both the source visual and the target page's drillthrough well, with compatible data lineage — a calculated/aggregated field won't pass. Pitfall #2: forgetting to size the tooltip page to 'Tooltip' makes it render huge or clipped. Pitfall #3: 'Keep all filters' off surprises users when the detail page shows unfiltered data. Pitfall #4: cross-report drillthrough requires both reports published to the same workspace and matching column names; mismatches silently disable the option.

**Tools:** drillthrough filters, report page tooltips, cross-report drillthrough, back button
