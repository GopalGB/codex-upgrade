---
name: pa-cloud-flow-basics
description: >-
  Cloud flow anatomy: one trigger -> sequential actions, dynamic content, Peek code/JSON, test and run history, the maker portal
---

# pa-cloud-flow-basics

Every cloud flow = exactly **one trigger** + an ordered list of **actions**. Build at make.powerautomate.com > Create. The trigger fires the run; each action references prior outputs via **Dynamic content** (right-side picker) or an expression. Reference an earlier action with `outputs('Compose')` or `body('Get_items')?['value']` - spaces in action names become underscores in expressions. Use **Peek code** (... menu) to see raw JSON and exact reference paths. Always run **Test > Manually**, then open **Run history** > a run > expand each action to inspect INPUTS/OUTPUTS - your primary debugger. Rename every action immediately ("Get_active_orders" not "Get items 2"); default names make flows unmaintainable. Add a **Compose** mid-flow to print any value. Group related actions in a **Scope**. Pitfalls: a flow with repeated failures gets auto-turned-off by the service (check the status toggle); the **connection** behind an action can expire (re-auth under Connections); dynamic content that vanishes means the upstream action was renamed/deleted - fix the broken reference or the flow won't save.

**Tools:** make.powerautomate.com, Dynamic content, Peek code, Run history, Compose, Scope
