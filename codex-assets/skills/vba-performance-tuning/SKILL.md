---
name: vba-performance-tuning
description: >-
  Speed up macros: ScreenUpdating Off, Calculation manual, EnableEvents off, DisplayAlerts, restore in cleanup, avoid Select/Activate, array I/O, timing with Timer — the standard speed wrapper
---

# vba-performance-tuning

The standard speed wrapper, set at the top and restored in cleanup: `Application.ScreenUpdating = False` (stop repaints), `Application.Calculation = xlCalculationManual` (stop recalc after every write), `Application.EnableEvents = False` (stop your own event handlers re-firing), `Application.DisplayAlerts = False` (suppress confirmation dialogs). Restore all four in a `CleanExit` label so an error can't leave Excel in a broken, frozen-looking state. This alone can turn a 60-second macro into 3 seconds.

Expert moves: the biggest wins are algorithmic, not flags — **read/write ranges as arrays** (see array I/O), and **never use `.Select`/`.Activate`** (the macro-recorder habit); operate on objects directly (`ws.Range("A1").Value = x`, not `Range("A1").Select: Selection.Value = x`). Disable automatic page breaks (`ws.DisplayPageBreaks = False`). Profile with `Dim t As Double: t = Timer ... Debug.Print Timer - t`. After a manual-calc run, call `Application.Calculate` once at the end. Turn off `Application.PrintCommunication`/use `Application.Cursor = xlWait` for UX.

Pitfalls: leaving `Calculation = xlCalculationManual` set after the macro means the user's other workbooks won't recalc — always restore. `ScreenUpdating` resets to True automatically when a Sub ends normally, but **not** on error — hence the cleanup label. Setting these inside a tight loop instead of once around it wastes the benefit. `DisplayAlerts = False` also auto-confirms destructive prompts (e.g., 'delete sheet?') — be deliberate.

**Tools:** Application.ScreenUpdating, Application.Calculation, xlCalculationManual, Application.EnableEvents, DisplayAlerts, Timer, .Select avoidance
