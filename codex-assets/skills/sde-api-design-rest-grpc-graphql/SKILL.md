---
name: sde-api-design-rest-grpc-graphql
description: >-
  Pick and design the right API style - resource-oriented REST, contract-first gRPC, client-shaped GraphQL - with versioning and errors.
---

# sde-api-design-rest-grpc-graphql

**REST**: resource nouns + HTTP verbs, stateless, cacheable, universal - the default for public/external APIs. Plural nouns (`/orders/{id}/items`), correct status codes (201+Location on create, 204 on delete, 409 conflict, 422 validation, 429 rate limit), and a consistent error envelope `{error:{code,message,details}}`. **gRPC**: contract-first protobuf over HTTP/2, binary, streaming, codegen'd clients - fastest for internal service-to-service; weak browser support. **GraphQL**: client specifies exactly the fields it needs in one query - kills over/under-fetching for rich UIs and mobile, but you must guard against the **N+1 resolver problem** (batch with DataLoader) and unbounded query depth/cost (depth limits, persisted queries). **Versioning**: URL path (`/v1`) for public REST, header/field-level for internal; never break a live contract - add fields, don't remove or retype them. **Idempotency & pagination** are design-time, not afterthoughts (cursor pagination, idempotency keys on POST). **Pitfall**: GraphQL exposed publicly without query-cost limiting - a single deep nested query can take down the backend.

**Tools:** REST, gRPC, protobuf, GraphQL, HTTP status codes, OpenAPI
