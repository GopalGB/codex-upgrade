---
name: pa-trigger-types
description: >-
  Automated vs instant vs scheduled triggers, trigger conditions, Split On, concurrency, and the infinite-loop trap
---

# pa-trigger-types

Three trigger classes: **Automated** (event-driven: "When an item is created", "When a new email arrives"); **Instant** (manual button, "Manually trigger a flow", or "When a HTTP request is received"); **Scheduled** (Recurrence: interval + frequency + start time + **time zone** - set it explicitly or runs drift across DST). The key optimization is **Trigger conditions** (trigger > Settings > Trigger Conditions): an expression like `@equals(triggerOutputs()?['body/Status'],'Approved')` so the flow only *starts* when true, saving runs and quota. **Split On** turns an array trigger output into one run per element. **Concurrency Control** caps parallel runs (degree=1 forces serial). The classic trap: a "When item modified" trigger whose actions modify the same item -> **infinite loop**; fix with a trigger condition checking a flag column or version field. Pitfall: automated triggers poll on an interval tied to license (1-5 min on lower tiers), so true instant reaction needs a webhook-based connector, not polling.

**Tools:** Recurrence, Trigger conditions, Split On, Concurrency Control, triggerOutputs(), When a HTTP request is received
