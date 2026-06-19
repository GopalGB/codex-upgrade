---
name: vba-debugging
description: >-
  Debug in the VBE — breakpoints (F9), step F8/Shift-F8, Watch and Locals windows, Immediate window Debug.Print and ?expr, Stop, conditional watch break, call stack, Err inspection
---

# vba-debugging

Set a **breakpoint** with F9 (or click the margin) to halt before a line. Step with **F8** (into), **Shift+F8** (over a called Sub), **Ctrl+Shift+F8** (out). Hover a variable while paused to see its value, or watch it in the **Locals** window (all in-scope vars) and **Watch** window (add expressions, set a watch to *break when value changes* or *when true* — invaluable for catching when a variable goes wrong without single-stepping a huge loop).

Expert moves: the **Immediate** window (Ctrl+G) is your REPL — `Debug.Print x` from code logs there; type `?Range("A1").Value` to inspect live, or run statements like `Application.EnableEvents = True` to fix a stuck state without restarting. `Stop` is a code-based breakpoint that survives save. `Debug.Assert condition` halts only when the condition is False (cheap invariants). Use **Call Stack** (Ctrl+L) to see how you got here. **Set Next Statement** (Ctrl+F9) re-runs or skips a line. After an error, type `?Err.Number; Err.Description` in the Immediate window.

Pitfalls: breakpoints are **not saved** with the file (use `Stop` if you need persistence). Editing code while paused can reset execution ('this action will reset your project'). `Debug.Print` survives in shipped code and can flood the Immediate window/slow loops — strip it. Stepping through event handlers re-enters them confusingly; disable events while debugging. A watch that breaks on change adds overhead in tight loops.

**Tools:** F8, F9, Breakpoint, Watch window, Locals window, Immediate window, Debug.Print, Debug.Assert, Stop, Call Stack, Set Next Statement
