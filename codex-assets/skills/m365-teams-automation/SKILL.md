---
name: m365-teams-automation
description: >-
  Post messages, create channels, and read Teams chats via Graph — when automating Teams notifications or channel management
---

# m365-teams-automation

Post to a channel: `POST /teams/{teamId}/channels/{channelId}/messages` with body `{"body":{"contentType":"html","content":"Build <b>passed</b> @user"}}`. List channels `GET /teams/{id}/channels`; create one `POST /teams/{id}/channels` with `{"displayName":"Releases","membershipType":"standard"}`. 1:1/group chat messages go to `/chats/{chatId}/messages`. Mentions need a `mentions` array linking `<at id="0">Name</at>` to a user id.

Delegated needs `ChannelMessage.Send`; app-only posting to channels needs `ChannelMessage.Send` + is **protected** — it requires either RSC (resource-specific consent in the Teams app manifest) or the special application-permission approval, and Microsoft meters/limits app-only channel posts.

Pitfall: there is **no app-only permission to read all channel messages** for arbitrary tenants without going through the Teams Export/RSC model or paying for the change-notifications metered API — many automations fail here. Pitfall 2: for simple inbound notifications, an **Incoming Webhook** connector or Workflows (Power Automate) is far simpler than Graph and needs no app registration. Pitfall 3: `contentType:html` is sanitized — script/style stripped.

**Tools:** /teams/{id}/channels/{id}/messages, /chats/{id}/messages, ChannelMessage.Send
