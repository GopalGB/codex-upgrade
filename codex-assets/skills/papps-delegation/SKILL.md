---
name: papps-delegation
description: >-
  THE #1 gotcha: delegation — which functions/operators each data source pushes to the server vs evaluates locally on the 500/2000-row cap, per source.
---

# papps-delegation

Delegation = Power Apps pushing query work (Filter/Sort/LookUp/aggregates) to the data source so it processes ALL rows server-side. If a function/operator is **not delegable** for that source, Power Apps pulls only the first N rows (default 500, max 2000 in Settings > General) and evaluates locally — silently returning wrong results on large tables. The blue-underline **delegation warning** in Studio is your alarm; never ship one over a table that can exceed the cap. Delegability is per-source: **Dataverse and SQL** delegate the most (=, <, >, StartsWith, And/Or, Sort, Sum/Count/Avg, In partially); **SharePoint** is more limited and does NOT delegate `Search()`, `in` on choice, or many text ops; **Collections/Excel** delegate nothing (always local). Non-delegable everywhere: `Search()` (use `StartsWith`/`Filter` with `=`), most `If` inside Filter, calculated columns, `Len`, `Distinct` over big sets. Pattern: filter delegably to a small set, THEN do local work. Pitfalls: `Filter(BigTable, Status = varStatus && Owner.Email = User().Email)` may be partly non-delegable on SharePoint; trusting a test that 'works' on 200 rows but breaks at 2000+; using `CountRows(Filter(...))` non-delegably. Verify against the source's delegable-function list, not memory.

**Tools:** Filter, Search, LookUp, Sort, SortByColumns, delegation warning (blue underline), data row limit
