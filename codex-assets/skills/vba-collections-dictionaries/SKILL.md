---
name: vba-collections-dictionaries
description: >-
  Use Collection and Scripting.Dictionary for lookups, dedup, grouping; .Exists, key/item iteration, Dictionary vs Collection tradeoffs, late vs early binding the Scripting runtime
---

# vba-collections-dictionaries

Reach for a **Dictionary** (`Scripting.Dictionary`) over a `Collection` for almost everything that needs keyed lookup: it has `.Exists(key)` (Collection has no clean existence check — you'd have to trap an error), it can return `.Keys` and `.Items` as arrays, and it lets you update items by key. Create it via late binding `Set d = CreateObject("Scripting.Dictionary")` (no reference needed) or early binding (Tools > References > Microsoft Scripting Runtime) for IntelliSense and `As Scripting.Dictionary` typing.

Expert moves: **deduplicate** by using values as keys — `If Not d.Exists(k) Then d.Add k, 1`. **Group/aggregate** in one pass — `d(k) = d(k) + amount` (reading a missing key auto-creates it with the default, so this idiom accumulates totals). Iterate with `For Each k In d.Keys`. Combine with the array pattern: read range to array, build the Dictionary in memory, write results back. Use `d.CompareMode = vbTextCompare` for case-insensitive keys (set it before adding any).

Pitfalls: `Collection` is 1-based and great for ordered FIFO lists, but lookups are O(n) and removing by value is painful. Dictionary keys must be unique — `.Add` on an existing key errors; assign with `d(k) = v` to upsert. Object keys compare by reference, not value. Setting `CompareMode` after items exist throws. Don't store huge objects as values if you only need flags.

**Tools:** Collection, Scripting.Dictionary, CreateObject, .Add, .Exists, .Keys, .Items, .Count, Microsoft Scripting Runtime
