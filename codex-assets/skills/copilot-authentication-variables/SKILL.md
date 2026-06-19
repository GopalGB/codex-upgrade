---
name: copilot-authentication-variables
description: >-
  Configure agent authentication (no auth / Entra ID / manual OAuth) and manage variable scope (topic, global, system) including passing Entra user identity to flows.
---

# copilot-authentication-variables

**Authentication** is set in **Settings > Security > Authentication**: (1) *No authentication* (anonymous - public web bots), (2) *Authenticate with Microsoft* (Entra ID, easiest for Teams/M365 internal agents - gives you the signed-in user), (3) *Authenticate manually* (custom OAuth2 - bring your own identity provider / connector auth). Entra auth is required for SharePoint/Dataverse knowledge to honor per-user permissions and for handing the user's identity to downstream flows. **Variables**: scope matters - **Topic** variables live only within one topic; **Global** variables (prefix `Global.`) persist across topics in a session; **System** variables (`System.User.DisplayName`, `System.Conversation.Id`, `System.Activity.Channel`) are read-only context. Mark a variable as global in its properties to share it. Pitfalls: (1) After enabling auth you get `System.User.Id`/token to call Graph or pass to flows - don't hardcode identity. (2) Switching auth modes can require re-publishing and updating the Azure app registration redirect URIs. (3) Variables reset between sessions - persist long-lived state in Dataverse, not in Global vars.

**Tools:** Settings > Security > Authentication, Entra ID SSO, Global vs Topic variables, System.User variables
