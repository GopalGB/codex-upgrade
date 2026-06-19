---
name: xls-charts-combo
description: >-
  Charts and combo charts: dual-axis, secondary axis, sparklines, dynamic chart ranges off spill/Tables, data labels, chart types selection
---

# xls-charts-combo

Pick the right type: line for trend, clustered bar for category comparison, stacked for composition, scatter for correlation (NEVER line for two unrelated x). **Combo chart** (Insert > Combo) mixes types and adds a **secondary axis** — e.g. revenue bars + margin% line; set the % series to secondary axis so scales don't crush each other. **Make charts dynamic**: source them from a **Table** or a **spill range** (`=Series#`) so they auto-grow as data is added — far simpler than OFFSET-based dynamic named ranges (which are volatile). Add **data labels** (last point only for clean line charts), and use **sparklines** (Insert > Sparklines) for in-cell trend mini-charts in dashboards/tables. Format: remove gridlines/chartjunk, label axes, sort bars by value. Pitfall: secondary-axis combos mislead if the two scales aren't intentionally aligned — annotate units; pie charts beyond ~5 slices are unreadable (use bar); 3-D charts distort — avoid. For many small comparisons use sparklines or a paneled set, not one cluttered chart.

**Tools:** Combo chart, secondary axis, sparklines, chart from Table/spill
