---
name: xls-array-formulas-legacy
description: >-
  Legacy CSE array formulas vs modern dynamic arrays, implicit intersection @, array constants, SUMPRODUCT as array engine, migration
---

# xls-array-formulas-legacy

Pre-365, multi-cell array math required **CSE** (Ctrl+Shift+Enter), shown as `{=SUM(IF(...))}` braces — you can't type the braces. Modern Excel mostly removes the need (formulas spill natively), but you'll still meet CSE in inherited files and must maintain them. **SUMPRODUCT** is the evergreen array engine that never needed CSE: `=SUMPRODUCT((a=x)*(b=y),vals)`. **Array constants** `{1,2,3}` (commas=cols, semicolons=rows) feed lookups: `=SUM(LARGE(rng,{1,2,3}))` sums top 3. The **@ implicit-intersection operator** appears when 365 opens old files — `=@A1:A10` forces a single value (old behavior); remove `@` to let a formula spill. Migration: many `{=...}` CSE formulas can be deleted and re-entered as plain dynamic arrays (FILTER/SUMIFS) that are faster and clearer. Pitfalls: editing a CSE formula and pressing Enter (not CSE) breaks it silently; CSE over whole columns is brutally slow; mixing dynamic-array output into a Table fails; an `@` sneaking into a new formula collapses an intended spill to one value — delete it. Know both worlds: read legacy CSE, write modern spills.

**Tools:** Ctrl+Shift+Enter, SUMPRODUCT, implicit intersection @, array constants
