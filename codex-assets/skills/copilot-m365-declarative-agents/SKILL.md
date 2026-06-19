---
name: copilot-m365-declarative-agents
description: >-
  Build M365 Copilot declarative agents and extensions: instructions, knowledge, capabilities, API/MCP plugins, and ship via Agents Toolkit or Copilot Studio.
---

# copilot-m365-declarative-agents

A **declarative agent** runs *inside* M365 Copilot - it reuses Copilot's orchestrator and GPT model, so you only supply: a **name**, **instructions** (the system prompt that shapes tone/behavior/scope), **knowledge** (SharePoint sites, Graph connectors, web, files), **capabilities** (Web search, Code interpreter, Image generation, Graph), and **actions** (API plugins from an OpenAPI spec, or **MCP servers** - GA-direction in 2026). Build two ways: (1) low-code in **Copilot Studio agent builder** / the M365 Copilot 'Create agent' UI; (2) pro-code with the **Microsoft 365 Agents Toolkit** (VS Code) editing the declarative-agent manifest JSON + plugin manifests. 2026 additions: **MCP Apps** render interactive UI (approval forms, dashboards) directly in Copilot chat. Pitfalls: (1) Declarative agents *can't* override Copilot's base model or run autonomous background triggers - for that you need a standalone Copilot Studio agent. (2) Instructions have a character limit; be concise and directive. (3) Knowledge is constrained to the signed-in user's permissions. (4) Publishing routes through Teams/M365 admin approval before org-wide availability.

**Tools:** Copilot Studio agent builder, Microsoft 365 Agents Toolkit, declarative agent manifest, API plugins, MCP, Teams admin
