---
name: pbi-parameters-whatif
description: >-
  Build what-if scenario analysis with numeric range parameters and field/calculation parameters for dynamic measure/axis switching
---

# pbi-parameters-whatif

Two parameter kinds. Numeric what-if: Modeling > New parameter > Numeric range — Power BI generates a disconnected table via `GENERATESERIES(min, max, step)` plus a slicer and a `[Param Value] = SELECTEDVALUE('Param'[Param], default)` measure. Use it in measures for scenarios: `Adjusted Revenue = [Total Sales] * (1 + 'Discount %'[Discount % Value])`. Because the table is disconnected, SELECTEDVALUE reads the slider without filtering data. Field parameters (Modeling > New parameter > Fields): let users swap which measure or dimension a visual shows — pick a set of fields, Power BI builds a table and slicer; drop the parameter on the visual's axis/values and the slicer toggles between, say, Sales/Profit/Margin without separate visuals. Pitfall #1: a what-if parameter measure with no SELECTEDVALUE default returns blank when nothing/multiple selected — always supply a default and handle multi-select. Pitfall #2: people relate the what-if table to data — don't; it must stay disconnected so the slider is independent. Pitfall #3: field parameters reference fields by name; renaming a measure breaks the parameter table — edit the generated DAX. Pitfall #4: field parameters can show/hide via the third column (boolean) to control display order and visibility. Combine field params with calc groups for measure-by-time matrices.

**Tools:** GENERATESERIES, SELECTEDVALUE, what-if parameter, field parameters
