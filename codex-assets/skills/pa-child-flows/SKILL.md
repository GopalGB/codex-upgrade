---
name: pa-child-flows
description: >-
  Reusable child flows via Run a Child Flow, request/respond trigger, passing typed inputs/outputs, solution requirement, sync limits
---

# pa-child-flows

Child flows make logic reusable. Build the child with an instant trigger that defines typed **inputs** (text/number/boolean/file), do the work, then end with **Respond to a Power App or flow** to return typed **outputs**. The parent calls it with **"Run a Child Flow"**, supplies inputs, and reads outputs as dynamic content. Hard requirement: **both parent and child must live in the same Solution** - child flows aren't available outside a solution (the #1 gotcha). Child flows run **synchronously**; the parent waits for the response, so keep them fast, and the child's run counts against quota too. Use them to DRY shared steps (a "Send branded email" or "Log error" subroutine) and tame giant flows. Pitfalls: the child must have a **Respond** action on every path or the parent hangs/times out; set the child's run-only/connection permissions; you can't easily pass arbitrary objects - serialize complex data as a JSON string input and `json()`-parse inside; child-of-child chains complicate debugging since each is a separate run in history.

**Tools:** Run a Child Flow, instant trigger inputs, Respond to a Power App or flow, Solutions (required), json() for objects
