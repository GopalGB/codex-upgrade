---
name: papps-collections-and-variables
description: >-
  State: global vars (Set), context vars (UpdateContext), collections (ClearCollect/Collect/Patch), scope rules, and the OnStart-vs-named-formula choice.
---

# papps-collections-and-variables

Three state types. **Global variables** — `Set(gblUser, User().Email)` — readable on any screen, any type. **Context variables** — `UpdateContext({locStep:2})` or `Navigate(Scr2,None,{locStep:2})` — scoped to ONE screen, good for screen-local UI state. **Collections** — `ClearCollect(colCart, {Item:"A",Qty:1})` to (re)fill, `Collect(colCart, row)` to append, `Remove`/`RemoveIf`/`Clear` to edit — in-memory tables, NOT delegable (everything local). Use Patch on a collection to update a specific in-memory row. Prefer **named formulas** (App.Formulas) over OnStart `Set` for static/derived values: they compute lazily, stay live, and skip the slow OnStart. Reserve OnStart for true one-time setup; heavy OnStart kills launch time. Pitfalls: loading a whole big table into a collection then filtering locally (defeats delegation — filter at source first, cache the small result); using global vars where a context var suffices (harder to reason about); assuming a collection refreshes itself (it's a snapshot — re-Collect or call Refresh on the source). Concurrent setup: wrap independent loads in `Concurrent(...)` to parallelize.

**Tools:** Set, UpdateContext, ClearCollect, Collect, Clear, Remove, Patch, App.OnStart, named formulas
