---
name: vba-range-cells-manipulation
description: >-
  Reference and manipulate ranges: Cells(r,c), Range, Offset, Resize, End(xlUp/xlToLeft), CurrentRegion, UsedRange, find last row, SpecialCells, Union/Intersect
---

# vba-range-cells-manipulation

Find the last used row reliably with `lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row` — start from the bottom and go up, which ignores blank gaps that `UsedRange` includes. Build dynamic ranges by combining `Cells` with `Resize`/`Offset`: `ws.Cells(2,1).Resize(n, 3)` is the data block; `.Offset(1,0)` shifts down a row. `CurrentRegion` grabs the contiguous block around a cell (like Ctrl+A on a list).

Expert moves: always qualify with a worksheet object (`ws.Range`, not bare `Range`) — unqualified `Range` uses the ActiveSheet and breaks when focus shifts. `Range(Cells(2,1), Cells(n,3))` builds a block from corner cells. `SpecialCells(xlCellTypeVisible)` targets only filtered rows; `xlCellTypeBlanks` finds empties; `xlCellTypeConstants`/`xlCellTypeFormulas` split values from formulas. `Union(r1, r2)` combines disjoint ranges; `Intersect` finds overlap (used in event scoping).

Pitfalls: `UsedRange` is bloated by old formatting and rarely shrinks — prefer `End(xlUp)`. `.Rows.Count` returns 1048576 (use `Rows.Count`, never hardcode 65536). `Cells(r,c)` is (row, col) — easy to swap. `SpecialCells` raises an error if **no** cells match (e.g., no blanks) — wrap in error handling. `ActiveCell`/`Selection` are fragile; reference cells explicitly instead of selecting.

**Tools:** Range, Cells, Offset, Resize, End, xlUp, CurrentRegion, UsedRange, SpecialCells, Union, Intersect
