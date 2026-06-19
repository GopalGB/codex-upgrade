---
name: papps-data-sources-connectors
description: >-
  Connecting data: standard vs premium connectors, SharePoint/SQL/Dataverse/Excel, implicit vs explicit connections, connection references for ALM.
---

# papps-data-sources-connectors

Add data via the Data pane; each source becomes a named source you reference directly (`'Orders'`, `Office365Users`). **Standard** connectors (SharePoint, Outlook, OneDrive, Office365Users) come with M365; **premium** (SQL Server, Dataverse via connector, Azure, Salesforce, HTTP) need a Power Apps premium license. On-prem SQL/SharePoint needs an **on-premises data gateway**. Dataverse is the native store and the only one with row-level security, audit, and relationships — prefer it for serious apps. For ALM, bind connectors through **connection references** (in a solution) so dev/test/prod swap connections without editing the app. Authentication: most connectors use the signed-in user's connection (per-user); SQL can use a shared SQL auth connection (all users share one identity — careful with row security). Pitfalls: Excel-in-OneDrive as a backend (no delegation, table must be a named Table, brittle, hard limits) — use it only for demos; treating connection as security (a SQL shared connection bypasses per-user permissions); not putting connectors in a solution, breaking promotion between environments.

**Tools:** Connectors, SharePoint, SQL Server, Dataverse, connection references, gateways
