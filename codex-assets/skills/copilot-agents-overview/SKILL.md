---
name: copilot-agents-overview
description: >-
  Decide agent type and orchestration mode when starting a new Copilot Studio agent: classic vs generative, declarative M365 vs standalone, autonomous vs conversational.
---

# copilot-agents-overview

Build agents at copilotstudio.microsoft.com (Power Platform-hosted) or via the agent builder inside M365 Copilot. Three design decisions before building: (1) **Where it lives** - a standalone Copilot Studio agent (its own URL/Teams app, billed by message packs/pay-as-you-go) vs a **declarative agent** that runs inside M365 Copilot using the host orchestrator and GPT model. (2) **Orchestration** - Classic (rule-based topic routing) vs Generative (LLM picks topics/tools/knowledge). New agents default to generative. (3) **Trigger model** - conversational (user-initiated) vs **autonomous** (event/Power Automate/scheduled trigger, no human in the loop). Pick the environment carefully on the Create screen: agents are bound to a Dataverse environment and Solution; moving across tenants/environments later means export/import of the solution, not copy-paste. Pitfall: people prototype in the Default environment, then can't apply DLP/managed-environment governance. Create a dedicated dev environment with Dataverse first. Every agent has Name, Description (the description is read by the orchestrator - write it as instructions, not marketing copy), Instructions, Knowledge, Topics, Tools, and Channels.

**Tools:** copilotstudio.microsoft.com, Agent overview page, Power Platform admin center
