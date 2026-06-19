---
name: xls-named-ranges
description: >-
  Named ranges and named formulas: scope (workbook vs sheet), dynamic names, Name Manager hygiene, using names in formulas and validation
---

# xls-named-ranges

Names make formulas readable and maintainable: `=TaxRate*Subtotal` beats `=$B$1*C7`. Create via Name Box, Formulas > Define Name, or Create from Selection (uses header labels). **Scope** matters: workbook-scoped names work everywhere; sheet-scoped names (`Sheet1!myName`) avoid collisions in multi-sheet models — set scope at creation. Names can hold **constants** (e.g. `Pi`), **formulas/LAMBDAs** (reusable functions — see lambda skill), or **dynamic ranges**. Prefer **Table structured refs** or **spill refs (`A2#`)** for dynamic ranges over the old volatile `OFFSET`/`INDEX` trick (`=OFFSET($A$1,0,0,COUNTA($A:$A),1)` recalcs constantly and slows big files; an INDEX-based name `=$A$1:INDEX($A:$A,COUNTA($A:$A))` is non-volatile). Pitfalls: orphaned/`#REF!` names accumulate after deletes — clean them in Name Manager (sort by Value to spot errors); names with typos surface as `#NAME?`; don't name ranges things that look like cell refs (e.g. `TAX1`). Good naming is the difference between an auditable model and a black box.

**Tools:** Name Manager, OFFSET, INDEX, LAMBDA names, scope
