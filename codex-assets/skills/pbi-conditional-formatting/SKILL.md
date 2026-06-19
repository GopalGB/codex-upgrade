---
name: pbi-conditional-formatting
description: >-
  Apply data-driven colors, data bars, icons, and dynamic formatting via rules or DAX measures on tables, matrices, and visuals
---

# pbi-conditional-formatting

Conditional formatting drives color/icon by value. On a table or matrix, open the field's dropdown > Conditional formatting > Background color/Font color/Data bars/Icons. Three ways to set: Color scale (gradient min-max), Rules (if value between X and Y then color), and 'Field value' / 'Format by field value' which uses a DAX measure returning a hex string — the most flexible. Example measure: `Color = SWITCH(TRUE(), [Total Sales] >= [Target], "#2E7D32", [Total Sales] >= 0.8*[Target], "#F9A825", "#C62828")` then set Format style = Field value, base on `Color`. This also works for column headers, KPI cards, and many chart elements (bars can be colored by a measure). Use icons for status with a field-value measure returning Unicode or via the rules engine. Pitfall #1: a measure returning a color string must be a valid hex or named color — invalid strings silently render default. Pitfall #2: 'Color by field value' requires the measure to be in the same context; a measure that ignores row context colors every row identically. Pitfall #3: color-only encoding fails accessibility — pair color with icons or text for colorblind users (WCAG). Pitfall #4: data bars on negative values need the axis configured or bars look wrong. Dynamic format strings (for measures/calc items) are separate — use the format string expression, not conditional formatting, to change number formatting.

**Tools:** FORMAT, SWITCH, conditional formatting, field value, data bars, icons
