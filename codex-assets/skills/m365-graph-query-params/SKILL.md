---
name: m365-graph-query-params
description: >-
  Shape Graph responses with $select, $filter, $expand, $orderby, $top, $count and ConsistencyLevel for advanced queries — when a call returns too much or needs server-side filtering
---

# m365-graph-query-params

Always send `$select` to cut payload and avoid returning every property: `GET /users?$select=displayName,mail,department`. Filter server-side: `GET /users?$filter=startswith(displayName,'A')`. Expand related entities in one call: `GET /me/messages?$expand=attachments`. Sort with `$orderby=receivedDateTime desc`, page-size with `$top=50`.

**Advanced queries** (count, not-equals, endsWith, search on directory objects) require the header `ConsistencyLevel: eventual` AND `$count=true` in the query string together — omit either and you get a 400 'Request_UnsupportedQuery'. Example: `GET /users?$filter=endsWith(mail,'@contoso.com')&$count=true` with `ConsistencyLevel: eventual`.

Pitfall: `$filter` and `$orderby` on the same non-indexed property often errors ('inefficient filter') — Graph requires both on indexed props or returns 400. Pitfall 2: `$search` on people/messages uses different syntax (`$search="displayName:John"`) than directory search and needs the eventual header too. Pitfall 3: string `$filter` values are single-quoted; escape embedded quotes by doubling them.

**Tools:** $select, $filter, $expand, $count, ConsistencyLevel: eventual, $search
