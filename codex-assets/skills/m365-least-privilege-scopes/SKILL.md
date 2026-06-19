---
name: m365-least-privilege-scopes
description: >-
  Choose the minimal Graph permission and delegated-vs-application type, then enforce app access policies — when securing any Graph integration
---

# m365-least-privilege-scopes

Always pick the narrowest scope that works, and prefer **delegated** (acts as a user, inherits their limits) over **application** (tenant-wide) whenever a user context exists. Granularity ladder: `Mail.ReadBasic` < `Mail.Read` < `Mail.ReadWrite` < `Mail.Send`; `Sites.Selected` (per-site, app-only) instead of `Sites.ReadWrite.All`; `User.Read` for self vs `User.Read.All` for directory. For SharePoint app-only, use **Sites.Selected** then grant the app rights to specific sites via `POST /sites/{id}/permissions` — this avoids tenant-wide file access.

Constrain app-only mail/calendar to specific mailboxes with an Exchange **Application Access Policy**: `New-ApplicationAccessPolicy -AppId $id -PolicyScopeGroupId grp@contoso.com -AccessRight RestrictAccess`.

Pitfall: requesting `.ReadWrite.All` 'to be safe' triggers security reviews and is the top finding in M365 audits — request what you use. Pitfall 2: app-only permissions are tenant-wide by default; `Sites.Selected` and Application Access Policies are the only built-in ways to narrow them. Pitfall 3: each added scope needs re-consent — over-scoping early forces an admin-consent round trip later anyway.

**Tools:** Mail.Read vs Mail.ReadBasic, .Read vs .ReadWrite, RSC, New-ApplicationAccessPolicy
