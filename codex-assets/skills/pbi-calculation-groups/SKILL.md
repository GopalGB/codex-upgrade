---
name: pbi-calculation-groups
description: >-
  Eliminate measure sprawl with calculation groups — apply YTD/PY/YoY/currency logic to any base measure via SELECTEDMEASURE
---

# pbi-calculation-groups

Calculation groups let one set of items (Current, YTD, PY, YoY %) apply to ANY base measure, instead of writing those variants for every measure. Create them in Tabular Editor (or now Power BI Desktop's model view) > add a calculation group > add calculation items whose expression uses `SELECTEDMEASURE()` as a placeholder: e.g. YTD item = `CALCULATE(SELECTEDMEASURE(), DATESYTD('Date'[Date]))`; PY item = `CALCULATE(SELECTEDMEASURE(), SAMEPERIODLASTYEAR('Date'[Date]))`. Put the calc group on a slicer/columns and pick a base measure — the report shows that measure transformed. Use a dynamic format string expression per item so a YoY % item formats as percent while Current inherits the base format. Set the Precedence property when stacking multiple calc groups (e.g. time + currency) so they apply in the right order. Pitfall #1: items apply to the measure currently in context — if no measure is on the visual, the calc item shows blank; guard with `ISSELECTEDMEASURE`. Pitfall #2: forgetting precedence makes two calc groups multiply in an undefined order. Pitfall #3: calc groups change implicit measures' behavior — convert implicit aggregations to explicit measures first. Pitfall #4: a SUM-style base measure inside a calc item still needs correct format string handling or numbers show as raw. Calc groups need a compatible engine (Premium/PPU/Fabric historically; verify your capacity).

**Tools:** Tabular Editor, SELECTEDMEASURE, calculation items, ISSELECTEDMEASURE, format string expression
