---
name: copilot-publishing-alm
description: >-
  Publish, version, and move agents across environments using solutions, connection references, and environment variables for proper dev/test/prod ALM.
---

# copilot-publishing-alm

Clicking **Publish** pushes the latest authored version to all connected channels - nothing the user sees changes until you publish. For real ALM, treat the agent as a **Dataverse solution component**: create the agent inside a custom (unmanaged) **Solution** in a dev environment, add its dependencies (flows, connection references, environment variables, custom connectors), then export and import (as **managed**) into test/prod - or use **Power Platform Pipelines** to deploy one-click. Use **environment variables** for anything that differs per environment (API base URLs, SharePoint site URLs) and **connection references** so connections rebind on import instead of breaking. Pitfalls: (1) The Default environment can't be a clean source - build in a dedicated dev environment. (2) On import you must re-establish connections for flows/connectors or tools fail silently. (3) Publishing in the target environment is still required after import - import alone doesn't go live. (4) Knowledge sources (SharePoint URLs) often need re-pointing per environment - parameterize them with environment variables. Keep version history; you can revert by re-publishing a prior version.

**Tools:** Publish button, Solutions, connection references, environment variables, Power Platform Pipelines, managed solutions
