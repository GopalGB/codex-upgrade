---
name: pa-http-rest-action
description: >-
  HTTP premium action for REST: method/headers/body/auth, Parse JSON the response, pagination, and the HTTP-trigger webhook
---

# pa-http-rest-action

The **HTTP** action (premium) calls any REST API: **Method** (GET/POST/PUT/PATCH/DELETE), **URI**, **Headers** (`Content-Type: application/json`, `Authorization: Bearer ...`), **Queries**, **Body** (a JSON object inline or from a Compose). **Authentication** supports None, Basic, **OAuth (Active Directory)** with tenant/client id/secret/resource, Managed Identity, Client Certificate - prefer OAuth/Managed Identity over hardcoded tokens. The response is raw - chain a **Parse JSON** action ("Generate from sample" builds the schema) so downstream actions get typed dynamic content instead of `body('HTTP')?['deep']?['path']`. Read status with `outputs('HTTP')['statusCode']`. For incoming calls, **"When a HTTP request is received"** gives a POST webhook URL (generated on save) - define the JSON schema and secure it (the URL has a SAS signature; add API-key validation in a first Condition since it's anonymous by default). Pitfalls: HTTP needs premium; a non-2xx response **fails** the action (catch with run-after or it aborts) - inspect `result()` for the error body; large responses can exceed message-size limits (paginate or trim fields); set retry None for non-idempotent POSTs; never log the webhook URL.

**Tools:** HTTP action, Parse JSON, OAuth/Managed Identity, When a HTTP request is received, statusCode, Generate from sample
