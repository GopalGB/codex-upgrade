---
name: copilot-generative-vs-classic-orchestration
description: >-
  Choose and configure classic (topic-routing) vs generative (LLM-planned) orchestration, and migrate an existing classic agent to generative without breaking flows.
---

# copilot-generative-vs-classic-orchestration

Set this in **Settings > Generative AI > Orchestration** (Classic vs Generative). **Classic**: deterministic - only topics respond, matched by trigger phrases; actions fire only when explicitly called inside a topic. Use it for highly regulated, scripted flows where you must guarantee the exact path. **Generative**: an LLM planning layer reads user intent, decomposes multi-step requests, and dynamically selects the best mix of topics + tools + knowledge, even chaining several in one turn. Use it for natural, flexible assistants. When you flip an existing classic agent to generative, Copilot Studio auto-generates a **Description** for each existing topic - review and rewrite these, because descriptions (not trigger phrases) now drive routing. Pitfalls: (1) Generative orchestration can *repeat questions* or ignore valid answers if a Question node's variable isn't clearly described or if two tools have ambiguous descriptions - disambiguate names/descriptions. (2) Generative mode is less predictable for compliance demos; if a specific path must always run, keep that flow as an explicit topic and constrain with instructions. (3) Test both modes in the Test pane after switching - routing behavior changes.

**Tools:** Settings > Generative AI > Orchestration toggle, topic Descriptions, tool/knowledge descriptions
