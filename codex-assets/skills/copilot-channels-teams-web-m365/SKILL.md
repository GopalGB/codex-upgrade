---
name: copilot-channels-teams-web-m365
description: >-
  Publish an agent to channels: Microsoft Teams, custom website embed, M365 Copilot, SharePoint, Power Pages, Direct Line API, and the right channel for each audience.
---

# copilot-channels-teams-web-m365

After publishing, wire up delivery on the **Channels** page. **Teams + Microsoft 365** - one toggle publishes the agent as a Teams app and surfaces it in M365 Copilot; admins may need to approve it in the Teams admin center. **Custom website** - copy the embed `<iframe>` / web-chat snippet into any page; **Demo website** gives a quick shareable test URL. **Microsoft 365 Copilot** - makes it a declarative agent in the Copilot side panel. **SharePoint / Power Pages** - embed in intranet/portal sites. **Direct Line** - REST/WebSocket API + secret for full custom apps and mobile, giving you programmatic control of the conversation. Also: Facebook, Slack, custom telephony via Azure. Pitfalls: (1) Each channel has different auth/identity behavior - an Entra-authenticated agent works inside Teams but a public website channel needs anonymous or manual auth. (2) Adaptive Cards and some rich content render differently per channel - test the actual channel, not just the Test pane. (3) Teams app deployment is governed by tenant app-permission policies; coordinate with the Teams admin or the agent silently won't appear for users.

**Tools:** Channels page, Teams + M365 channel, Custom website snippet, Direct Line API, Demo website
