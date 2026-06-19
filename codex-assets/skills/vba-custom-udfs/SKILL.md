---
name: vba-custom-udfs
description: >-
  Build custom worksheet functions (UDFs) in VBA — Application.Volatile, Application.Caller, array-returning UDFs, #VALUE handling, Function Wizard categories, recalc behavior
---

# vba-custom-udfs

A UDF is a `Public Function` in a **standard module** (not a sheet or ThisWorkbook module, or it won't be callable from cells). Type it with the cell's input as arguments: `Public Function NetMargin(rev As Double, cost As Double) As Double`. Return errors properly with `CVErr(xlErrValue)` (shows `#VALUE!`) instead of raising a VBA error that yields `#VALUE!` with no control.

Expert moves: `Application.Volatile True` forces recalc on every sheet change (use sparingly — it kills performance on big sheets). `Application.Caller` gives the calling cell/range so a UDF can know its own row. Return a **spill array** by declaring `As Variant` and assigning a 2-D array — modern Excel (365/2021+) spills it natively; legacy needs Ctrl+Shift+Enter. Add a description and argument help via `Application.MacroOptions Macro:="NetMargin", Description:="...", Category:="Finance"`.

Pitfalls: UDFs are **side-effect-free** — they cannot write to other cells, format, or sort; attempting it returns `#VALUE!`. UDFs are slower than native functions; a sheet with thousands of UDF calls recalcs slowly. Volatile UDFs + many cells = frozen Excel. Avoid `Variant`/`Range` round-trips inside loops; read the input range into an array once. Never `On Error Resume Next` silently — return `CVErr`.

**Tools:** Application.Volatile, Application.Caller, CVErr, xlErrValue, Function, Variant arrays
