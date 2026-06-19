---
name: copilot-entities-slot-filling
description: >-
  Extract structured values from user input with prebuilt/custom entities and slot-fill required question variables; stop the bot re-asking for info already given.
---

# copilot-entities-slot-filling

Entities turn free text into typed values. **Prebuilt entities**: Email, Phone, Number, Date and time, Money, City, Age, etc. - select them in a Question node's 'Identify' dropdown so 'my flight is on the 3rd' resolves to a date variable. **Custom entities**: (a) *Closed list* - finite values with synonyms ('Small/S/small size'); great for product categories or departments. (b) *Regular expression (regex)* - for IDs/order numbers like `ORD-\d{6}`. **Slot filling** is the key behavior: when a Question node has 'Smart match' / entity identification on, and the user pre-supplies the value in their utterance ('book a flight to Paris tomorrow'), the bot skips asking that slot. Pitfall: if you use a plain Text question instead of an entity-typed question, slot-filling won't pre-populate and the bot re-asks for data already given. In generative orchestration, the orchestrator can fill inputs for tools automatically from conversation context, so define tool input descriptions well. Always set a variable name on the Question so downstream nodes/conditions can read it.

**Tools:** Entities, prebuilt entities, closed/regex custom entities, Question node 'Identify'
