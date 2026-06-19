---
name: pa-variables-vs-compose
description: >-
  Initialize/Set/Increment/Append variables vs Compose for immutable values; when each wins, scope rules, array-build pitfalls
---

# pa-variables-vs-compose

**Variables** are mutable and global: **Initialize variable** must be at the **top level** (never inside a Condition/loop - set name, type String/Integer/Float/Boolean/Array/Object, value), then **Set variable**, **Increment/Decrement** (numbers), **Append to string/array variable** (accumulate inside loops). **Compose** is immutable - stores one computed value (`outputs('Compose')`), cheaper, faster, side-effect-free; use for a one-time expression, a constant, a JSON literal, or to debug-print. Rule: only *compute and reference* -> **Compose**; need to *mutate across iterations* (counter, running list) -> **variable**. Pitfalls: appending to an **array variable inside a concurrent Apply to each** loses items - set loop concurrency to 1, or replace the pattern with a **Select** that maps the array in one step (no loop, no variable). Initialize can't be conditional - initialize at top with a default and Set later. Object variables need valid JSON (`json('{"k":"v"}')` or `setProperty()`). Variables count as actions and add overhead at scale - Compose + Select usually beats variable-in-loop.

**Tools:** Initialize/Set/Increment/Append variable, Compose, outputs(), Select, json(), addProperty/setProperty
