---
name: copilot-conversational-nodes
description: >-
  Build conversation flow with Message, Question, and Condition nodes including adaptive cards, multiple-choice options, and branching logic in the topic canvas.
---

# copilot-conversational-nodes

Three core authoring nodes on the topic canvas. **Message** - sends text/rich content; supports variables in `{x.var}` syntax, Markdown, images, and **Adaptive Cards** (paste card JSON or build inline) for buttons/forms. **Question** - asks the user and stores the answer in a variable; choose response type: Multiple choice options (renders buttons, each option becomes a branch), Text, Number, entity-typed, or 'User's entire response'. **Condition** - branches on variable values/expressions; uses Power Fx under the hood (e.g., `Topic.OrderTotal > 1000`). Add an 'All other conditions' branch to catch the else case. Sequence them: Message (acknowledge) > Question (collect) > Condition (branch) > Message (confirm). Pitfall: Question nodes have a built-in **escalation/no-match retry** - after N failed attempts it can fall to the Escalate system topic; tune the retry count rather than building your own loop. Another trap: referencing a variable in a Message before any node has set it shows blank - check variable scope (Topic vs Global). Use the **Variables** block (2026) to initialize/increment/append in one node instead of scattered Set-variable nodes.

**Tools:** Message node, Question node, Condition node, Adaptive Cards, variable references {x}
