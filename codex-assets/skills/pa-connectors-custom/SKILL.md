---
name: pa-connectors-custom
description: >-
  Standard vs premium connectors, connection references, and building custom connectors from OpenAPI/Postman with auth + policies
---

# pa-connectors-custom

Connectors wrap APIs as actions/triggers. **Standard** (SharePoint, Outlook, Teams, OneDrive) vs **Premium** (Dataverse, SQL, HTTP, Azure, Salesforce - need premium license or pay-as-you-go). Each action runs under a **Connection** (stored auth); in solutions always use **Connection References** so connections rebind on import to another environment. Build a **Custom Connector** (Data > Custom connectors > New) when none exists: General (host, base URL), **Security** (OAuth 2.0 with auth/token URLs + client id/secret, API Key, or Basic), **Definition** (import **OpenAPI/Swagger** or a Postman collection to auto-generate actions, or add operations with request/response schemas), then **Test**. Use **policy templates** to inject headers or route dynamically. Pitfalls: importing OpenAPI beats hand-building - get a clean swagger.json first; OAuth custom connectors need the **redirect URL** (shown after first save) registered in the app registration or consent fails; premium connectors silently fail at runtime if the owner's license lapses; throttle limits are per-connection, so high-volume flows hit 429s - check published limits and add retry.

**Tools:** Custom connectors, OpenAPI/Swagger import, Connection references, OAuth 2.0, policy templates, premium connectors
