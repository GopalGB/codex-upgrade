---
name: xls-conditional-formatting
description: >-
  Conditional formatting: formula-based rules, data bars/color scales/icon sets, highlight duplicates, rule precedence, performance
---

# xls-conditional-formatting

Beyond presets, **formula-based rules** are where the power is: New Rule > 'Use a formula'. Write one relative to the top-left of the applied range with mixed refs: `=$D2>TODAY()` highlights whole rows where a date is overdue (lock the column with `$`, leave the row relative). Highlight **duplicates** with `=COUNTIF($A:$A,$A2)>1`; highlight **mismatches between two columns** `=$A2<>$B2`. **Data bars / color scales / icon sets** visualize magnitude in-cell — set min/max to Number or Percentile (not Automatic) for honest scaling, and tick 'Show Bar Only' to hide values. Manage **rule precedence** in Manage Rules (top wins; 'Stop If True' halts lower rules) — order matters when rules overlap. Pitfalls: CF is **volatile-ish and slow** at scale — thousands of formula rules over whole columns tank performance; bound ranges tightly and prefer one rule over many. Copy-paste can fragment a rule into dozens of identical ranges (Manage Rules > consolidate). Reference other sheets in CF formulas now works in 365 (older Excel needs a named range).

**Tools:** Conditional Formatting, formula rules, data bars, color scales, icon sets
