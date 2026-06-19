---
name: copilot-human-handoff
description: >-
  Hand off a conversation to a live human agent with full context via Escalate topic + engagement hub (D365 Omnichannel / Genesys / contact center), or notify in Teams.
---

# copilot-human-handoff

Two patterns. **Lightweight notify**: in a topic, on escalation trigger a Power Automate flow that posts the transcript/summary to a Teams channel or creates a ticket - cheap, no live takeover. **True live handoff** (agent transfer): configure **Settings > (Customer engagement / Agent transfer)** to connect an **engagement hub** - Dynamics 365 Contact Center / Omnichannel, or third-party (Genesys, etc.). Customize the **Escalate** system topic to set the conditions and the hand-off message. When triggered, Copilot Studio transfers the conversation **with full chat context** so the human agent sees what was already discussed and routing rules send it to the right queue/skill. Pitfalls: (1) Live handoff *requires* a contact-center/engagement-hub solution - it does not work standalone; without one, 'Escalate' just shows a message. (2) Context transfer needs the integration configured correctly or the human starts blind - test that the transcript actually arrives. (3) Channel matters: handoff is richest on web/voice channels wired to the engagement hub; Teams-only internal agents often use the notify-a-human pattern instead. (4) Set clear escalation triggers (N failed turns, explicit 'talk to a person', low confidence) so it neither over- nor under-escalates.

**Tools:** Escalate system topic, Settings > Agent transfer, Dynamics 365 Omnichannel, contact center connectors, transfer handoff
