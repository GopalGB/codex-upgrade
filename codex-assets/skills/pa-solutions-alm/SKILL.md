---
name: pa-solutions-alm
description: >-
  Solutions + ALM: environments (dev/test/prod), managed vs unmanaged, connection references, environment variables, pac CLI, pipelines
---

# pa-solutions-alm

**Solutions** are the unit of ALM - never build production flows outside one. Develop in a **dev environment** in an **unmanaged** solution (editable, loose components), then **export as managed** and import to **test** then **prod** (managed = sealed, not editable in target, cleanly removable). Add flows, custom connectors, tables, apps, **Connection References** (rebind connections per environment at import) and **Environment Variables** (parameterize per-env values like a site URL or key - set the value during import, not in the flow). Use a **publisher + prefix** to namespace logical names. Move solutions via manual **Export/Import**, the **Power Platform CLI** (`pac solution export/import/pack/unpack` for Git source control), or **Power Platform Pipelines** (automate dev->test->prod with approvals). Pitfalls: importing without **connection references** breaks/prompts for connections - always use them; hardcoded env-specific URLs/IDs should be **environment variables**; managed solutions can't be edited in prod (no "fix in prod" - fix in dev, re-promote); deleting a managed solution removes its components (and table data); flows arrive disabled and need manual enable; unmanaged layering over a managed base can block updates; source-control the **unpacked** solution, not the .zip.

**Tools:** Solutions, environments (dev/test/prod), managed vs unmanaged, Connection references, Environment variables, pac CLI, Power Platform Pipelines
