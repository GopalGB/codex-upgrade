---
name: m365-entra-id-basics
description: >-
  Manage Entra ID users, groups, roles, and conditional access fundamentals via Graph/PowerShell — when handling identity, licensing, or RBAC
---

# m365-entra-id-basics

Entra ID (formerly Azure AD) is the identity layer behind all of M365. Key objects via Graph: users `/users`, groups `/groups` (security vs Microsoft 365 vs mail-enabled — set `groupTypes:['Unified']` for M365 groups), directory roles `/directoryRoles`, app registrations `/applications`, service principals `/servicePrincipals`.

Assign a license: `POST /users/{id}/assignLicense` with `{"addLicenses":[{"skuId":"<guid>"}],"removeLicenses":[]}` — find SKU GUIDs via `GET /subscribedSkus`. Add to group: `POST /groups/{id}/members/$ref` body `{"@odata.id":"https://graph.microsoft.com/v1.0/directoryObjects/{userId}"}`. Assign a role: add the user to the role via `/directoryRoles/{id}/members/$ref`.

Pitfall: a user must have `usageLocation` set before `assignLicense` or it 400s ('License assignment failed because... usage location'). Pitfall 2: group-based licensing is preferred over per-user; assigning directly then also via group causes duplicate-license conflicts. Pitfall 3: dynamic groups need Entra ID P1 and use membership rules, not `members/$ref`. Pitfall 4: conditional access and PIM are read/written via `/identity/conditionalAccess/policies` and the privileged-access endpoints — high blast radius, test in report-only mode.

**Tools:** /users, /groups, /directoryRoles, assignLicense, Get-MgUserLicenseDetail
