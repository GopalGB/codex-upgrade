---
name: xls-structured-tables
description: >-
  Excel Tables (Ctrl+T), structured references, total rows, auto-expand ranges, table-driven formulas and slicers
---

# xls-structured-tables

Convert ranges to **Tables** with Ctrl+T (give it a real name in Table Design). Tables auto-expand when you add rows/cols, so formulas and pivots/charts pointing at them never need range edits. **Structured references** replace A1: `=Sales[Amount]` is the whole column, `=Sales[@Amount]` is this row's value, `=Sales[#Totals]` the total row, `=Sales[[#Headers],[Amount]]` the header. They survive insert/delete and read like English. Turn on the **Total Row** (Table Design) for per-column SUBTOTAL aggregations that ignore filtered-out rows. Add **slicers** (Insert > Slicer) for click-filtering. Pitfalls: structured refs are NOT absolute — copying `Sales[@Amount]` sideways shifts the column; lock with `Sales[[Amount]:[Amount]]`. Dynamic-array spills can't live inside a Table. Tables can't have merged cells or blank header names. Naming the table well (e.g. `tblOrders`) makes Power Query, DAX, and lookups far cleaner. This is the foundation for clean, maintainable workbooks.

**Tools:** Ctrl+T, structured refs [@Column], Table.Name, slicers
