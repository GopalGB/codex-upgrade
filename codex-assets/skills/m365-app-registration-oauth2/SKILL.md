---
name: m365-app-registration-oauth2
description: >-
  Register an Entra app and choose client-credentials (app-only) vs authorization-code (delegated) flow with correct scopes — when setting up any Graph auth
---

# m365-app-registration-oauth2

Register at Entra admin center > App registrations > New. Note the Application (client) ID and Directory (tenant) ID. Add a client secret (Certificates & secrets) or, better for production, a certificate.

Two flows:
- **Client credentials (app-only)** — daemon/cron with no user. POST to `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token` with `grant_type=client_credentials`, `client_id`, `client_secret`, `scope=https://graph.microsoft.com/.default`. Permissions are **Application** type and require **admin consent**. `.default` is mandatory here — you cannot request dynamic scopes.
- **Authorization code (delegated)** — acts as a signed-in user. Redirect to `/authorize`, exchange the code at `/token` with `scope=User.Read Mail.Send offline_access`. `offline_access` is what gets you a refresh token.

Pitfall: app-only permissions do nothing until an admin clicks **Grant admin consent** — the token issues fine but Graph returns 403. Pitfall 2: delegated grants the *intersection* of app permission AND the user's own rights; app-only grants the full tenant-wide permission, so scope it tightly.

**Tools:** Entra portal, /oauth2/v2.0/token, client_credentials, .default, az ad app create
