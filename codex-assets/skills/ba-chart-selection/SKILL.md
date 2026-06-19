---
name: ba-chart-selection
description: >-
  Pick the right chart for the data relationship — comparison/composition/distribution/correlation/trend — bar vs line vs scatter vs box; kill pie>5-slices, dual-axis, and truncated-baseline deception.
---

# ba-chart-selection

Choose by the relationship you're showing, not by what looks pretty. Comparison across categories → horizontal bar (sorted descending, labels readable). Change over time → line (continuous) or column (few discrete periods). Part-to-whole → stacked bar or 100% stacked; use a pie ONLY for 2-3 slices summing to 100%. Distribution → histogram or box/violin (never a bar of an average — it hides spread). Correlation → scatter, add a trend line + r. Ranking change → slopegraph or bump chart. Flows/transitions → Sankey. Expert moves: sort bars by value not alphabetically; start bar axes at zero (truncating exaggerates differences — the #1 deception); for line charts the y-axis may be non-zero if you annotate. Use direct labeling over legends when ≤5 series. Encode one variable per visual channel; color = category, position = primary value. Pitfalls: dual-axis charts (imply correlation that isn't there), 3D/exploded pies, rainbow palettes (use sequential for ordered, categorical for nominal, diverging for +/- around a midpoint), and dot-density maps where population just tracks area. When in doubt, a sorted bar beats everything.

**Tools:** matplotlib, ggplot2, Vega-Lite, Excel charts, Datawrapper
