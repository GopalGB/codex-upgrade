---
name: m365-graph-pagination
description: >-
  Follow @odata.nextLink to page through large Graph collections without losing items or hardcoding skip tokens — when a list returns partial results
---

# m365-graph-pagination

Graph caps collection responses (often 100, sometimes 999 for directory). When more exist, the body includes `@odata.nextLink` — a full opaque URL containing a `$skiptoken`. Loop: call the URL as-is, append items, repeat until `@odata.nextLink` is absent.

```python
items, url = [], 'https://graph.microsoft.com/v1.0/users?$top=100'
while url:
    r = requests.get(url, headers=hdr).json()
    items += r['value']
    url = r.get('@odata.nextLink')
```

In the Graph SDKs use `PageIterator` (.NET/Java) or `graph_client.users.get()` then iterate — it handles nextLink automatically.

Pitfall: **never** parse or rebuild the skiptoken yourself or strip query params — it is opaque and tenant-specific; reissue the nextLink URL verbatim with the same auth header. Pitfall 2: `$top` is a page hint, not a total limit — you still must follow nextLink to get everything. Pitfall 3: don't add `$top` to the nextLink (it's already baked in) or you may get an error.

**Tools:** @odata.nextLink, $top, $skiptoken, PageIterator (SDK)
