---
name: vba-subs-vs-functions
description: >-
  Write Sub vs Function procedures, pass ByRef/ByVal, Optional/ParamArray args, return values, scope with Public/Private — when to use which in Excel VBA
---

# vba-subs-vs-functions

Use a **Sub** for actions with no return value (run from the macro list, assign to a button); use a **Function** when you need a return value, especially a worksheet UDF. Return by assigning to the function name: `MyFunc = result`. Key argument rules: VBA defaults to **ByRef** (the caller's variable can be mutated) — pass `ByVal` explicitly when you want a private copy. This is the #1 silent bug: a helper accidentally overwrites a caller variable because nobody typed `ByVal`.

Expert moves: `Optional arg As Long = 0` for defaults (only trailing args may be optional); `ParamArray args() As Variant` for variadic input (must be last, always ByRef Variant). Use `Exit Sub`/`Exit Function` to bail early rather than nesting Ifs. Scope: `Private Sub` keeps it out of the Alt+F8 macro list and other modules; `Public` (default) exposes it. Mark a Sub `Private` and it won't clutter the macro picker.

Pitfalls: a Function called from a worksheet cell **cannot** alter other cells, change formats, or call most Application methods — it only returns a value. Subs with arguments don't appear in the Run dialog. Don't use `Call` syntax with parens unless using `Call`; `MySub arg1, arg2` (no parens) vs `result = MyFunc(arg1)` (parens for return).

**Tools:** Sub, Function, ByRef, ByVal, Optional, ParamArray, Static, Exit Sub/Function
