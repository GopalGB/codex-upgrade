---
name: copilot-topics-trigger-phrases
description: >-
  Author classic topics and write trigger phrases / topic descriptions so the orchestrator routes the right conversation path; fix topics that never fire.
---

# copilot-topics-trigger-phrases

A topic = a conversation branch with a Trigger plus nodes. In **classic** orchestration, add 5-10 varied **trigger phrases** ('reset my password', 'I forgot my login', 'can't sign in') - the NLU model matches user intent to the closest phrase. Don't write near-duplicates; spread the semantic space. In **generative** orchestration, trigger phrases are mostly ignored - the LLM routes using the topic **Description** field instead, so every topic needs a clear plain-language description ('Use when the user wants to reset or recover an account password'). Topic types: trigger-phrase, On Recognized Question, On Unknown Intent (fallback), system topics (Greeting, Goodbye, Escalate, Start Over). Pitfall: two topics with overlapping trigger phrases cause unpredictable routing - check the **'topic overlap'** warnings. Use **Redirect** nodes to chain topics and keep each topic single-purpose. To test routing, open the Test pane, type the utterance, and check which topic lit up. If a topic never fires under generative mode, the cause is almost always a missing or vague Description, not bad trigger phrases.

**Tools:** Topics page, trigger phrases, topic Description field, Trigger node
