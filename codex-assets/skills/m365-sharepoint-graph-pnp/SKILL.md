---
name: m365-sharepoint-graph-pnp
description: >-
  Read/write SharePoint Online lists and document libraries via Graph or PnP PowerShell — when automating list items, files, or site provisioning
---

# m365-sharepoint-graph-pnp

**Via Graph:** resolve site `GET /sites/{host}:/sites/{path}`, get lists `GET /sites/{siteId}/lists`, read items `GET /sites/{siteId}/lists/{listId}/items?$expand=fields`. Create: `POST .../items` with body `{"fields":{"Title":"X","Status":"Open"}}` — internal field names, not display names. Files live in the default doc library, reachable via `/sites/{id}/drive/root:/folder/file.xlsx`.

**Via PnP PowerShell** (richer for SharePoint ops): `Connect-PnPOnline -Url https://contoso.sharepoint.com/sites/Finance -Interactive`; `Get-PnPListItem -List 'Tasks'`; `Add-PnPListItem -List 'Tasks' -Values @{Title='X';Status='Open'}`. PnP supports CSOM-level things Graph can't (content types, field provisioning, site templates via `Invoke-PnPSiteTemplate`).

Pitfall: list field **internal names** differ from display names (spaces become `_x0020_`, lookup fields append `LookupId`) — query `/columns` to discover them. Pitfall 2: PnP needs its own Entra app registration with consented Graph+SharePoint perms (use `Register-PnPEntraIDApp`) since the default PnP app id was retired. Pitfall 3: list views cap at 5,000 items (list view threshold) — index columns or filter.

**Tools:** /sites/{id}/lists/{id}/items, PnP.PowerShell, Get-PnPListItem, Add-PnPListItem
