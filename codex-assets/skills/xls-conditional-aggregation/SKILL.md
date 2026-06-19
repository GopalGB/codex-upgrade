---
name: xls-conditional-aggregation
description: >-
  SUMIFS/COUNTIFS/AVERAGEIFS, SUMPRODUCT for complex multi-criteria math, MAXIFS/MINIFS, wildcard and date-range conditions
---

# xls-conditional-aggregation

**SUMIFS(sum_range, crit_range1, crit1, …)** is the workhorse — criteria_range first differs from old SUMIF. Use comparison strings: `">="&DATE(2026,1,1)` for date floors, `"<"&cellRef` referencing cells, `"<>"&""` for non-blank, `"*tex*"` wildcards. Multiple pairs are ANDed; for OR, sum two SUMIFS or use SUMPRODUCT. **COUNTIFS/AVERAGEIFS/MAXIFS/MINIFS** share the same signature. **SUMPRODUCT** handles what *IFS can't: math across arrays, OR logic, and conditions on computed values: `=SUMPRODUCT((region=x)*(MONTH(dates)=6)*sales)` — multiply boolean arrays (TRUE*1) then weight. Use `--` to coerce booleans: `=SUMPRODUCT(--(a>b))`. Pitfalls: SUMIFS ranges must be equal-sized or you get `#VALUE!`; criteria text >255 chars fails; SUMPRODUCT over whole columns (A:A) is slow — bound the range. For grouped summaries from one formula, prefer GROUPBY/PIVOTBY (see that skill). Dates: never compare to a text date literal — build with DATE() to avoid locale issues.

**Tools:** SUMIFS, COUNTIFS, AVERAGEIFS, SUMPRODUCT, MAXIFS, MINIFS
