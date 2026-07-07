---
name: agentic-tool-design
description: >-
  Design the agent-computer interface (ACI) — the tools/function schemas an agent calls — with clear names, typed parameters, self-explanatory descriptions, helpful error returns, and shapes that make misuse hard. Use when giving an LLM tools; tool quality determines agent reliability as much as the model does.
---

# agentic-tool-design

Tools are the agent's hands, and their **interface** (the ACI — agent-computer interface) deserves the same care you'd give a public API for human developers — more, because the agent can't ask follow-up questions. Invest in the schema: descriptive tool and parameter **names**, explicit **types**, and a **description** that states what the tool does, when to use it, and any constraints, with an example call. If a smart engineer would misuse the tool from its description alone, the model will too — fix the description, not the model.

Shape tools to make wrong use **hard** (poka-yoke). Prefer absolute paths over relative so the agent can't get lost; prefer a few well-chosen tools over dozens of overlapping ones (selection error grows with count); return **structured, actionable errors** ("file not found: /x — did you mean /y?") instead of stack traces or silent nulls, so the agent can self-correct in the loop. Keep each tool's job coherent — one tool that does one thing beats a god-tool with a mode flag.

Match the tool's output to what the agent needs to decide its next step: return the relevant fields, not a 50KB blob that blows the context; paginate or summarize large results. Give consequential tools (writes, sends, deletes) clear names and consider a confirmation/dry-run mode. Test tools the way you'd test code — call them with the inputs an agent would actually produce, watch where it fumbles, and iterate on the interface. A great model with badly designed tools is an unreliable agent.

**Tools:** ACI = treat tool schemas as a product · descriptive names/types/descriptions + example · poka-yoke (hard to misuse) · structured actionable errors · few coherent tools over many · right-sized outputs · test with agent-shaped inputs
