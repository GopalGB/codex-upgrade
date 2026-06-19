---
name: m365-graph-powershell-sdk
description: >-
  Administer M365 from the Microsoft Graph PowerShell SDK (Connect-MgGraph, Get-Mg* / New-Mg* cmdlets) — when scripting tenant admin tasks
---

# m365-graph-powershell-sdk

Install `Install-Module Microsoft.Graph -Scope CurrentUser`. Connect interactively with explicit scopes: `Connect-MgGraph -Scopes 'User.ReadWrite.All','Group.ReadWrite.All'`. For unattended use a cert app: `Connect-MgGraph -ClientId $id -TenantId $tid -CertificateThumbprint $thumb`. Cmdlets mirror endpoints: `Get-MgUser -All`, `Get-MgUser -UserId u@contoso.com`, `New-MgUser -BodyParameter $h`, `Update-MgUser`, `Get-MgGroupMember -GroupId $gid`. For endpoints with no cmdlet, drop to raw: `Invoke-MgGraphRequest -Method GET -Uri '/v1.0/...'`.

Pitfall: the SDK is huge — install only sub-modules you need (`Microsoft.Graph.Users`, `.Groups`) or import time is painful; `Import-Module Microsoft.Graph` loads everything and is slow. Pitfall 2: many cmdlets default to v1.0 — switch with `Select-MgProfile beta` (older) or target beta via `-Uri '/beta/...'`. Pitfall 3: paging — add `-All` or you only get the first page; without it you silently miss users. Pitfall 4: the old MSOnline/AzureAD modules are **retired** — migrate to Graph SDK; their cmdlets stopped working in 2025.

**Tools:** Microsoft.Graph module, Connect-MgGraph, Get-MgUser, New-MgUser, Invoke-MgGraphRequest
