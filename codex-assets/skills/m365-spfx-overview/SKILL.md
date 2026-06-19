---
name: m365-spfx-overview
description: >-
  Scaffold SharePoint Framework (SPFx) web parts/extensions and call Graph from them via MSGraphClientV3 — when building custom UI inside SharePoint/Teams
---

# m365-spfx-overview

SPFx is the supported model for custom client-side components hosted in SharePoint Online and Teams. Scaffold with `yo @microsoft/sharepoint` (Node LTS + the pinned SPFx generator version — versions are strict). Dev loop: `gulp serve` opens the local workbench / hosted workbench (`/_layouts/15/workbench.aspx`). Build & package: `gulp bundle --ship` then `gulp package-solution --ship` produces a `.sppkg` you upload to the tenant App Catalog.

Call Graph from a web part with `this.context.msGraphClientFactory.getClient('3').then(c => c.api('/me').get())` (MSGraphClientV3) — permissions are requested in `package-solution.json` `webApiPermissionRequests` and approved by an admin in the **API access** page of the SharePoint admin center. For SharePoint REST use `this.context.spHttpClient` against `/_api`.

Pitfall: SPFx Node/generator/gulp versions must match the targeted SPFx release exactly — a mismatched Node version is the #1 scaffold failure. Pitfall 2: `webApiPermissionRequests` only *requests* perms; nothing works until an admin approves them in API access. Pitfall 3: forgetting `--ship` ships unminified bundles that point at localhost.

**Tools:** yo @microsoft/sharepoint, gulp serve, MSGraphClientV3, package-solution, /_api
