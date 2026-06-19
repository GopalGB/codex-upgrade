---
name: pbi-power-query-m-transforms
description: >-
  Shape and clean data in Power Query M before load — unpivot, merge, type, custom columns, and folding-aware transforms
---

# pbi-power-query-m-transforms

Power Query (M) is the ETL layer; do all shaping here, not in DAX. Key transforms: set types early (`Table.TransformColumnTypes`) so downstream steps fold; unpivot wide month columns to a tidy long table with `Table.UnpivotOtherColumns(Source, {"Region","Product"}, "Month", "Value")`; add columns with `Table.AddColumn(prev, "Margin", each [Sales]-[Cost], type number)`; merge tables via `Table.NestedJoin` then `Table.ExpandTableColumn`. Reference the M editor via View > Advanced Editor for the full `let ... in` script. The make-or-break concept is query folding: when the source is a database, PQ pushes transforms back as SQL. Right-click a step > View Native Query — if greyed out, folding broke at that step. Pitfall #1: putting `Table.Buffer`, custom functions, `Table.AddIndexColumn`, or row-based operations too early kills folding, forcing a full extract. Order folding-friendly steps (filter, select, type) first, folding-breakers last. Pitfall #2: `Changed Type` auto-step with hardcoded column names breaks when source columns rename — reorder so removal/rename precedes typing. Pitfall #3: referencing columns by index instead of name breaks on schema change. Use Reference (not Duplicate) queries to build staging layers without re-querying the source.

**Tools:** Power Query M, Table.UnpivotOtherColumns, Table.AddColumn, Table.NestedJoin, query folding
