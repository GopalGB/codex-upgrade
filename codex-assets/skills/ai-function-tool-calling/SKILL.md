---
name: ai-function-tool-calling
description: >-
  Wire LLMs to external actions via tool/function calling: schema design, the call→execute→result loop, parallel calls, and forced tool choice — use to let a model fetch data or take actions.
---

# ai-function-tool-calling

Expose actions as tools with a name, a one-sentence description of WHEN to use it, and a JSON Schema for parameters. The model returns a tool_call (name + JSON args); YOU execute it and feed the result back as a tool-result message; the model then continues or calls more tools. The description is the highest-leverage field — write it for the model's decision ('Use this to look up current order status by order_id', not 'order lookup'). Keep tool count low (≤10-20 active); too many tools tank selection accuracy — gate by relevance or use a router. Use `tool_choice` to force a specific tool (extraction) or 'required'/'auto'/'none'. Models can request parallel calls — execute concurrently and return all results. Validate args against the schema before executing (the model can hallucinate args or invent enum values). ALWAYS return a result for every tool_call id, even errors (return a structured error message the model can recover from), or the conversation breaks. Common mistake: vague descriptions causing the model to pick the wrong tool, or not returning a result and leaving a dangling call. Make tools idempotent where possible.

**Tools:** tools/functions param, tool_choice, parallel tool calls, JSON Schema for params
