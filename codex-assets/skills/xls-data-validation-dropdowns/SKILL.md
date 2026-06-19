---
name: xls-data-validation-dropdowns
description: >-
  Data validation dropdowns (lists), dependent/cascading dropdowns, input/error messages, custom-formula validation, dynamic-array lists
---

# xls-data-validation-dropdowns

Data > Data Validation. **List** type makes a dropdown — source from a named range or a **Table column** (e.g. `=tblDepts[Dept]`) so it auto-extends, or a **spill range** `=UNIQUE(data)#` for a self-maintaining unique list. **Dependent/cascading dropdowns**: the child list filters on the parent's pick — modern way is `=FILTER(items, category=$A2)` in a helper spill then point validation at it; legacy way uses `=INDIRECT($A2)` with named ranges per category (fragile: names can't have spaces). **Custom formula** validation enforces rules: `=AND(ISNUMBER(B2),B2>0)`, or `=REGEXTEST(B2,"^\d{10}$")` for a 10-digit code, or `=COUNTIF($A:$A,A2)=1` to block duplicates. Add **Input Message** (guidance) and **Error Alert** (Stop/Warning/Info). Pitfalls: validation does NOT block pasted values (paste overrides it) — combine with protection or a CF flag; INDIRECT is volatile and breaks on renamed sheets; existing invalid data isn't re-checked — use 'Circle Invalid Data' to audit.

**Tools:** Data Validation, List, INDIRECT, FILTER, custom formula
