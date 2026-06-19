---
name: pa-conditions-switch
description: >-
  Condition (if/else branches), nested conditions vs Switch action, multi-criteria AND/OR rows, expression-mode conditions
---

# pa-conditions-switch

The **Condition** action gives **If yes** / **If no** branches. Build the test with the row builder (left value, operator, right value) or flip to **Edit in advanced mode** for an expression: `@equals(triggerBody()?['Status'],'Open')`. Add multiple rows and pick **AND** / **OR** at the group level; nest groups for `(A and B) or C`. Operators (equal, contains, starts with, greater than) are **type-strict** - compare like types, wrapping with `int()`/`string()`. For many discrete cases, the **Switch** action beats nested Conditions: set "On" to a value (`triggerBody()?['Priority']`), add a **Case** per value plus a **Default**. Switch matches **exact equality only** (no ranges/contains) on a primitive. Pitfalls: 3+ levels of nested Conditions become unmaintainable - refactor to Switch or Filter+lookup; a Condition on a possibly-null value silently falls to "If no" - coalesce first; Switch has no fall-through; for range logic ("amount between") use a Condition with two AND rows, not Switch; empty string vs null both fail literal equality - normalize upstream.

**Tools:** Condition action, Switch/Case/Default, advanced mode expression, AND/OR groups, equals, contains, greater
