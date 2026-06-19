---
name: copilot-content-moderation-guardrails
description: >-
  Configure content moderation, response controls, and guardrails at agent/topic/prompt level to balance answer coverage against safety and off-topic responses.
---

# copilot-content-moderation-guardrails

Guardrails operate at three levels. **Agent level**: Settings > **Generative AI** - a **content moderation** control (High > Medium > Low) trades safety for coverage; High blocks more potentially harmful/off-topic content but answers fewer questions, Low does the reverse. Also here: toggle whether the agent may use **general knowledge** (the base LLM) vs *only* your knowledge sources - turn general knowledge OFF for grounded, on-brand-only agents that won't hallucinate beyond your data. **Topic level**: the **Generative answers** node has its own moderation setting. **Prompt level**: the Prompt tool has moderation per prompt. Reinforce scope in the **Instructions** field ('Only answer questions about HR policy; for anything else, say you can only help with HR'). At the platform layer, **DLP policies** (Power Platform admin center) restrict which connectors the agent can use, and **Managed Environments** add governance. Pitfalls: (1) Lowering moderation to fix 'I can't answer that' increases harmful-content risk - prefer adding knowledge over loosening moderation. (2) Leaving general knowledge ON makes the agent answer off-topic/outdated things confidently. (3) Moderation settings don't replace data-permission security - SharePoint/Dataverse permissions still govern *what* it can read.

**Tools:** Generative AI settings, Content moderation slider, allowed knowledge toggle, instructions, DLP policies
