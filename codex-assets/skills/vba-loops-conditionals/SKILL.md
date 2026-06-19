---
name: vba-loops-conditionals
description: >-
  Control flow: For/For Each, Do While/Until, Select Case, If/ElseIf, Exit For/Do, nested loops, GoTo for cleanup; choosing For Each vs indexed For over collections
---

# vba-loops-conditionals

Use `For i = 1 To n` (optionally `Step -1` to iterate backwards) when you need the index — **always loop backwards when deleting rows**, because deleting shifts later rows up and a forward loop skips them. Use `For Each item In collection` for object collections (Worksheets, Cells, a Range, a Collection) — it's faster and cleaner than indexed access on COM collections. `Do While cond ... Loop` tests first; `Do ... Loop Until cond` runs at least once.

Expert moves: `Select Case` beats long `ElseIf` chains and supports ranges and lists — `Case 1 To 10`, `Case "A", "B", "C"`, `Case Is > 100`, `Case Else`. `Exit For`/`Exit Do` short-circuit once you've found what you need. For multi-level cleanup, a forward `GoTo CleanExit` label that runs teardown (close files, re-enable events) is idiomatic VBA, not a code smell.

Pitfalls: `For Each` over a Range that you're modifying can behave oddly — read into an array first. There is no `Continue`/`break` like C; emulate skip with a nested `If` or `GoTo NextIteration` label before `Next`. `While...Wend` exists but has no `Exit` — prefer `Do...Loop`. An infinite `Do Loop` with no exit condition hangs Excel (Ctrl+Break to stop, if events allow). Off-by-one: `For i = 1 To UBound(arr)` misses index 0 on a 0-based array — use `LBound`/`UBound`.

**Tools:** For Next, For Each, Do Loop, While Wend, Select Case, If Then Else, Exit For, Step, GoTo
