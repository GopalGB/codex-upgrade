---
name: vba-event-handling
description: >-
  Handle Worksheet (Change/SelectionChange/BeforeDoubleClick), Workbook (Open/BeforeSave/SheetChange), and Application events; Target.Address, disable events to avoid recursion
---

# vba-event-handling

Worksheet events live in the **sheet's** code module; Workbook events in **ThisWorkbook**. The dropdowns at the top of the code pane list valid events. `Worksheet_Change(ByVal Target As Range)` fires on cell edits; `SelectionChange` on navigation; `BeforeDoubleClick(Target, Cancel)` lets you set `Cancel = True` to suppress edit mode.

Expert moves: scope a Change handler to one column with `If Not Intersect(Target, Me.Range("B:B")) Is Nothing Then`. The classic recursion bug: writing a cell inside `Worksheet_Change` re-fires the event — guard with `Application.EnableEvents = False` ... your writes ... `Application.EnableEvents = True`, and wrap it so an error can't leave events disabled (use `On Error GoTo` that re-enables). Handle multi-cell paste: `Target` may be a range — loop `For Each c In Target` or test `Target.CountLarge > 1`. For Application-level events (any workbook), declare `Dim WithEvents App As Application` in a class module and hook `App_WorkbookOpen`.

Pitfalls: a crash with `EnableEvents=False` leaves your handlers dead until you reset it (or restart Excel) — always restore in error handler. `Workbook_Open` doesn't fire if macros are disabled or the file opens via certain automation. `Worksheet_Change` doesn't fire on recalculated formula results — use `Worksheet_Calculate` for that. Don't put heavy work in `SelectionChange`; it fires constantly.

**Tools:** Worksheet_Change, Workbook_Open, Application.EnableEvents, WithEvents, Target, Intersect, Workbook_BeforeSave
