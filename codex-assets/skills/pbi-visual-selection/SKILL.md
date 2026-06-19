---
name: pbi-visual-selection
description: >-
  Pick the right chart for the analytical question — comparison, trend, composition, distribution, relationship — and avoid misleading visuals
---

# pbi-visual-selection

Match visual to intent. Comparison across categories: horizontal bar (long labels) or clustered column; sort descending by value, not alphabetically, so the eye reads ranking instantly. Trend over time: line chart (continuous), never a pie. Part-to-whole: stacked bar or a single donut with <=5 segments — beyond that switch to a sorted bar. Distribution: histogram or box plot. Two-measure relationship: scatter (add a play axis for time). Detailed numbers with hierarchy: matrix with row/column subtotals and conditional formatting. Two scales (revenue vs growth %): combo chart (column + line on secondary axis). KPI vs target: KPI visual or gauge sparingly (gauges waste space). Pitfall #1: pie/donut for many categories or for comparison — humans judge angles poorly; use bars. Pitfall #2: dual-axis combo charts mislead unless axes are clearly labeled; many readers infer false correlation. Pitfall #3: starting a bar chart's value axis above zero exaggerates differences — keep bars zero-based; truncation is only acceptable on line charts of tightly-ranged trends. Pitfall #4: 3D/funnel/word-cloud novelty visuals reduce comprehension. Pitfall #5: too many series on one line chart (spaghetti) — use small multiples instead.

**Tools:** bar/column charts, line charts, scatter, matrix, combo charts
