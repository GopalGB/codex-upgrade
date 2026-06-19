---
name: ai-prompt-engineering
description: >-
  Engineer reliable LLM prompts: role+task+constraints+format scaffolding, delimiter discipline, instruction placement, and iterative refinement — use when output is vague, inconsistent, or ignores constraints.
---

# ai-prompt-engineering

Structure every prompt as: persona/role, task, context, explicit constraints, output format, then the input wrapped in delimiters (XML tags like `<doc>...</doc>` beat triple-backticks for nested content). Put the actual instruction LAST when context is long — models attend most to the end (recency) and start (primacy); the middle is the lost-in-the-middle dead zone. Be positive and specific: 'respond in 3 bullets' beats 'don't be verbose' (models follow do better than don't). Use prefilling (seed the assistant turn with `{` or `Answer:`) to force format and skip preamble. For Claude, XML tags are first-class; for GPT, use the system message for stable rules and user message for the variable task. Iterate empirically: change ONE variable, run on a fixed eval set of 10-20 cases, measure. Common mistake: stuffing conflicting instructions ('be concise' + 'be thorough') — the model picks one nondeterministically. Resolve conflicts explicitly with priority ('if conflict, prioritize accuracy over brevity'). Test the prompt against adversarial inputs (empty, huge, malformed) before shipping.

**Tools:** system/user role separation, XML delimiters, prefill, instruction-at-end
