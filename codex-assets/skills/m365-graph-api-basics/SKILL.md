---
name: m365-graph-api-basics
description: >-
  Call Microsoft Graph REST endpoints (/me, /users, /sites, /drives, /groups) against v1.0 vs beta — when querying any M365 data via HTTP
---

# m365-graph-api-basics

Base URL is `https://graph.microsoft.com/v1.0` (use `/beta` only for preview features — never in production, schema changes without notice). All calls need `Authorization: Bearer {token}` plus `Content-Type: application/json` on writes. Core read endpoints:

- `GET /me` — signed-in user (delegated only; app-only context has no `/me`, returns 400 — use `/users/{id|userPrincipalName}` instead).
- `GET /users` — directory users; `GET /users/{upn}/messages`, `/events`, `/drive`.
- `GET /sites/{hostname}:/sites/{path}` — resolve a SharePoint site by path, e.g. `/sites/contoso.sharepoint.com:/sites/Finance`.
- `GET /drives/{id}/root/children` — OneDrive/doclib items.
- `GET /groups`, `/teams`, `/planner`.

Pitfall: the single most common 400 is calling `/me` with a client-credentials (app-only) token — there is no user in that flow, so you must address resources by explicit id/UPN. Second pitfall: forgetting that GUIDs and UPNs are both valid for `/users/{}` but `me` is delegated-only. Test interactively in Graph Explorer (developer.microsoft.com/graph/graph-explorer) before coding — it shows the exact permissions each call needs.

**Tools:** graph.microsoft.com/v1.0, /me, /users/{id}, /sites, /drives, GET/POST
