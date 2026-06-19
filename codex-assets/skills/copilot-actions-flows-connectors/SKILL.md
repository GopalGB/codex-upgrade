---
name: copilot-actions-flows-connectors
description: >-
  Add tools/actions to an agent: call a Power Automate flow, a connector action, a prompt, or an MCP server; wire inputs/outputs and handle auth.
---

# copilot-actions-flows-connectors

Actions (now called **Tools**) let an agent *do* things. Add via the agent's **Tools** tab > Add a tool. Types: **Flow** - a Power Automate cloud flow triggered by 'Run a flow from Copilot Studio'; define input/output parameters in the flow's trigger and 'Respond to Copilot' action, then map agent variables to them. **Connector action** - any of 1500+ connectors (e.g., create a SharePoint item, send Outlook mail, query SQL). **Prompt** - an AI Builder GPT prompt as a reusable tool. **MCP server** - connect a Model Context Protocol server to expose its tools (2026). **REST API plugin** - point at an OpenAPI spec. In **classic** orchestration you must call a tool explicitly from inside a topic via the 'Call an action' node; in **generative** orchestration the orchestrator picks the tool automatically based on its Name + Description + input descriptions - so write those carefully. Pitfall: flow connection references break on environment import - reconfigure connections after deployment. Long-running flows: Copilot Studio times out actions around ~100 seconds; offload heavy work to async patterns. Always set the tool's Description as instructions for *when* to call it.

**Tools:** Tools page, Power Automate cloud flow, connector actions, Prompt tool, MCP servers, REST API plugin
