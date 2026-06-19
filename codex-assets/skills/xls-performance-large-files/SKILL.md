---
name: xls-performance-large-files
description: >-
  Large-workbook performance: calculation modes, volatile functions, full-column references, .xlsb format, used-range bloat, calc tree
---

# xls-performance-large-files

Slow workbooks usually have fixable causes. **Calculation mode**: switch to Manual (Formulas > Calculation Options) while building; F9 recalcs all, Shift+F9 the sheet, Ctrl+Alt+F9 forces a full rebuild of the dependency tree. **Volatile functions** (NOW, TODAY, RAND, OFFSET, INDIRECT, CELL, INFO) recalc on EVERY change — replace OFFSET/INDIRECT with INDEX and structured/spill refs; they're the top hidden cost. **Avoid whole-column refs** (A:A) in SUMPRODUCT/array formulas — bound to the used range or a Table. **Kill used-range bloat**: phantom formatting inflates the file and slow-scrolls — delete unused rows/cols entirely and save (Ctrl+End should land near your data). Save as **.xlsb** (binary) for big files — smaller and faster to open than .xlsx. Move heavy lookups into the **Data Model/Power Pivot** rather than millions of sheet formulas. Use **AGGREGATE/SUMIFS** over array CSE formulas. Pitfalls: array formulas over huge ranges, conditional formatting on whole columns, and circular references with iterative calc on all murder performance — find the slow sheet by toggling calc and timing F9.

**Tools:** Calculation Options, F9, .xlsb, AGGREGATE, Data Model
