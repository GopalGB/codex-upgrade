---
name: ba-dashboard-design
description: >-
  Design BI dashboards (Tableau/Power BI/Looker) that drive decisions: inverted-pyramid layout, the 5-second test, audience-tiered KPI/diagnostic/operational views; avoid chart-junk gauges and 30-tile vanity walls.
---

# ba-dashboard-design

Start from the decision, not the data: write the one question the dashboard answers and who acts on it. Layout by Z/F-pattern reading order — top-left = the single headline KPI vs target, then trend, then breakdown, then detail. Apply the 5-second test: a stakeholder must read the top metric and its direction within 5 seconds. Tier by audience: executive (3-5 KPIs, RAG status, MoM/YoY delta), manager (diagnostic drill-downs), analyst (operational grain). Expert moves: use small multiples instead of one cluttered combo chart; put a target/benchmark reference line on every KPI so a number has meaning; show variance (actual vs plan) not just absolutes; add 'last refreshed' timestamp + data-source footnote for trust. Keep to one accent color for the metric-of-interest, gray everything else (preattentive emphasis). Pitfalls: gauge/donut/3D charts that waste pixels; >7 tiles above the fold; dual-axis charts that imply false correlation; no filters state shown so users misread a filtered view as the whole. Default to a single page; a scroll or tab is a new dashboard, not more clutter. Mock in Figma first, validate the question with the user, then build.

**Tools:** Tableau, Power BI, Looker, Metabase, Figma
