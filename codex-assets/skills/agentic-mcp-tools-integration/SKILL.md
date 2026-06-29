---
name: agentic-mcp-tools-integration
description: >-
  Connect agents to external tools and data through the Model Context Protocol (MCP) — servers exposing tools/resources/prompts over stdio or HTTP — and decide when to use an existing server vs build a custom one. Use when wiring an agent to systems (files, DBs, SaaS, internal APIs) and you want a standard, reusable integration instead of bespoke glue.
---

# agentic-mcp-tools-integration

MCP is a standard client-server protocol for giving agents capabilities: an **MCP server** exposes **tools** (callable actions), **resources** (readable data/context), and **prompts** (reusable templates); an **MCP client** inside the agent host connects and uses them. The payoff is reuse and decoupling — one well-built server (GitHub, Postgres, a filesystem, your internal API) works across any MCP-capable host, and you stop rewriting bespoke tool glue per agent. Transports are typically **stdio** for local servers and **streamable HTTP** for remote ones.

Prefer an **existing server** before building: there's a large ecosystem, and a maintained server beats a hand-rolled integration. Build a **custom server** when you're exposing your own system or need tools shaped specifically for your agents — and when you do, apply tool-design discipline (clear names, typed inputs, structured errors, right-sized outputs), because an MCP tool is still an agent-computer interface. Expose data the agent should *read* as resources and *do* as tools; keep each tool coherent and single-purpose.

Treat MCP as a **security boundary**, not just plumbing. Servers run with real credentials and can take real actions, so scope each connection to least privilege, isolate untrusted tool output (it can carry prompt-injection), require confirmation for destructive tools, and audit calls. Note the deployment reality: interactively-authenticated servers may be unavailable in headless/CI runs, so design agents to degrade gracefully when a server is absent. Test servers with the inputs an agent actually generates, and version their tool schemas.

**Tools:** MCP = standard server(tools/resources/prompts) + client · stdio local / HTTP remote · reuse existing servers, build custom for your own systems · tool-design rules apply · least-privilege + isolate untrusted output + confirm destructive · degrade when a server is absent
