---
name: agentic-skill-authoring
description: >-
  Write effective agent skills and instructions — a sharp description that acts as the trigger signal, progressive disclosure of detail, one capability per skill, and concrete how-to over generic advice. Use when authoring a SKILL.md, system prompt, or agent instruction so the agent reliably finds and correctly applies the capability.
---

# agentic-skill-authoring

A skill is a packaged capability the agent loads on demand; its **description is everything**, because that one line is the always-in-context signal the agent uses to decide whether to trigger the skill. Pour the "when to use this" into the description — the task, the symptoms, the keywords a relevant request would contain — not into the body. A perfect body with a vague description never fires; a sharp description routes correctly. Write it from the *trigger's* point of view ("use when X / when you see Y"), not a title.

Apply **progressive disclosure**: keep the always-loaded surface (name + description) tight, put the procedure in the body, and push bulky references, schemas, or scripts into separate files the agent opens only when it actually runs the skill. This keeps the context budget lean while still having depth available just-in-time. One skill = one capability; if a skill is trying to do three things, split it so each gets a clean trigger.

Make the body **concrete and imperative**: real steps, real commands, the specific functions/flags/formulas, and the common pitfalls — the expert how-to a generic model wouldn't already know. Skip the obvious. State preconditions and failure handling. For agent *instructions/system prompts*, the same rules apply: be specific about the goal, the constraints, the output format, and what NOT to do; show the canonical example; and prefer rules the agent can actually follow over aspirational prose. Validate that the skill loads and that its description actually fires on the intended inputs.

**Tools:** description = the trigger signal (write "use when…") · progressive disclosure (lean surface, deep on demand) · one capability per skill · concrete imperative how-to, skip the obvious · state preconditions + pitfalls · test that it triggers
