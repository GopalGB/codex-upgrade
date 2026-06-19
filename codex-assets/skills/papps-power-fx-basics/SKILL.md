---
name: papps-power-fx-basics
description: >-
  Power Fx essentials: declarative formulas, behavior vs property formulas, operators, If/Switch, error-handling (IfError/IsError), named formulas.
---

# papps-power-fx-basics

Power Fx is Excel-like and declarative: a control property is a formula that auto-recalculates when dependencies change (e.g. `Label.Text = ThisItem.Name`). Two formula kinds: **property formulas** (return a value, no side effects — Text, Visible, Fill) and **behavior formulas** (run on events like OnSelect, chained with `;` and allowed to call Set, Patch, Navigate). Core: `If(cond, then, [elseif, then,] else)`, `Switch(value, m1,r1, m2,r2, default)`, `With({a:1, b:2}, a+b)` for local scoping. Logic operators are `And`/`Or`/`Not` or `&&`/`||`/`!`; string concat is `&`. Handle errors with `IfError(risky, fallback)` and `IsError/IsBlank/IsBlankOrError`; `Coalesce(a,b,c)` returns first non-blank. **Named formulas** (App.Formulas) define reusable computed values that evaluate lazily and stay live — prefer them over OnStart Set for static config. Pitfall: Power Fx has no statements/loops in property formulas — use ForAll (which returns a table, it is NOT a procedural loop) and table functions instead. Enable Formula-level error management in app settings for IfError to work fully.

**Tools:** Power Fx, If, Switch, IfError, With, Coalesce, named formulas
