---
name: xls-dynamic-arrays-spill
description: >-
  Dynamic array spill, FILTER/UNIQUE/SORT/SORTBY/SEQUENCE, spill operator #, #SPILL! errors, single-formula reports
---

# xls-dynamic-arrays-spill

Modern Excel (365/2021+) spills one formula across a range. **FILTER**: `=FILTER(data, (region="East")*(sales>100), "none")` — multiply conditions for AND, add `+` for OR, 3rd arg avoids `#CALC!` on empty. **UNIQUE**: `=UNIQUE(rng)`; pass `TRUE` 3rd arg for items appearing exactly once. **SORT/SORTBY**: `=SORT(FILTER(...),2,-1)` sorts by 2nd col descending; SORTBY sorts one array by another without the sort key being in output. **SEQUENCE**: `=SEQUENCE(rows,cols,start,step)` for dynamic row numbers/date scaffolds. Reference a spill with the **spill operator**: `A2#` refers to the whole dynamic range — feed it to charts/dropdowns so they auto-grow. **#SPILL!** means the spill range is blocked: clear cells below/right, or the formula is in a Table (tables don't allow spills — move it out). Combine: `=SORT(UNIQUE(FILTER(names,dept=x)))`. Don't wrap dynamic arrays in implicit-intersection `@` unless you deliberately want one value.

**Tools:** FILTER, UNIQUE, SORT, SORTBY, SEQUENCE, RANDARRAY, spill #
