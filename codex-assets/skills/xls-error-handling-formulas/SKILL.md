---
name: xls-error-handling-formulas
description: >-
  IFERROR vs IFNA, trapping #DIV/0! #N/A #VALUE! #REF! #SPILL! #CALC!, ISERROR/ISNA, error-tolerant lookups and aggregation
---

# xls-error-handling-formulas

Use **IFNA** not IFERROR around lookups: `=IFNA(XLOOKUP(...),"not found")` traps only `#N/A` and lets real bugs (`#REF!`, `#VALUE!`) surface instead of hiding them. Reserve **IFERROR** for math you know can divide by zero: `=IFERROR(a/b,0)`. Know the error meanings: `#DIV/0!` (zero/blank denominator), `#N/A` (lookup miss), `#VALUE!` (text where number expected), `#REF!` (deleted cell — a structural bug, never mask it), `#NAME?` (typo'd function/missing named range), `#SPILL!` (blocked spill range), `#CALC!` (empty array/nested-array). To **sum a column that contains errors**, use `=AGGREGATE(9,6,range)` (function 9 = SUM, option 6 = ignore errors) instead of array IFERROR. Pitfall: blanket `IFERROR(...,"")` is the #1 cause of silently-wrong models — it converts every error to blank including the ones telling you the model is broken. Add an audit cell counting errors: `=SUMPRODUCT(--ISERROR(range))`.

**Tools:** IFERROR, IFNA, ISERROR, ISNA, ISERR, AGGREGATE, NA
