---
name: pbi-kpis-cards-visual-calcs
description: >-
  Build KPI cards, the KPI visual, and visual calculations (GA May 2026) for running totals/moving averages without new model measures
---

# pbi-kpis-cards-visual-calcs

For headline numbers use the Card (single value) or the newer multi-value Card visual for several KPIs in one tile with per-value formatting and reference labels. The KPI visual shows a value vs a target with a trend axis and good/bad coloring — supply Value, Target, and Trend axis fields. Cards respect the filter context, so a slicer changes them; format the displayed measure with a dynamic format string for currency/percent. Visual Calculations (General Availability since the May 2026 release) compute within a single visual over its already-aggregated result — perfect for running totals, moving averages, percent-of-parent, and ranks WITHOUT adding measures to the semantic model (no VertiPaq bloat). Add via the visual's 'New calculation' button using functions like `RUNNINGSUM([Total Sales])`, `MOVINGAVERAGE([Total Sales], 3)`, `[Total Sales] / COLLAPSE([Total Sales], ROWS)` for percent-of-parent. Pitfall #1: visual calculations only see the visual's data — they can't be reused on another visual; if many visuals need it, make a measure instead. Pitfall #2: their result depends on the visual's axis/sort order (RUNNINGSUM follows the row order) — sort intentionally. Pitfall #3: a Card showing a measure with no aggregation/blank guard displays (Blank); wrap with a default. Pitfall #4: KPI visual needs a continuous trend axis (usually Date) or it renders flat. Prefer visual calculations for one-off visual-scoped math; measures for anything shared.

**Tools:** Card visual, new Card (multi-row), KPI visual, RUNNINGSUM, MOVINGAVERAGE, visual calculations
