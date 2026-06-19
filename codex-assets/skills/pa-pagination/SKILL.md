---
name: pa-pagination
description: >-
  Pagination settings to fetch beyond default 100/256 limits, threshold caps, skip-token loops, and HTTP @odata.nextLink paging
---

# pa-pagination

By default list actions return a capped page (SharePoint Get items ~100, Dataverse List rows ~5000, others 256). For the full set, open ... > **Settings > Pagination**, toggle **On**, and set a **Threshold** = max total rows (e.g. 5000, up to the connector ceiling - SharePoint up to 100000, Dataverse 100000+). The platform then follows continuation tokens until the threshold. Set it realistically - too high wastes time/quota, too low silently truncates (the #1 bug: "my flow only processes 100 records" = pagination off). For **HTTP** calls to APIs returning `@odata.nextLink`/`nextPageToken` the connector won't auto-paginate - build a **Do until**: call the API, append `body('HTTP')?['value']` to an array variable, set the next URI from `body('HTTP')?['@odata.nextLink']`, repeat until empty (`@empty(variables('NextUrl'))`); raise the Do until Count/Timeout limits. Pitfalls: pagination is per-action - enable on every list action that can overflow; **Top Count** (page size) and threshold (total) interact; some connectors cap regardless of threshold; large pulls increase run time and message size - filter at source first to shrink the page count.

**Tools:** Settings > Pagination, Threshold, @odata.nextLink, Do until paging loop, Top Count, append to array variable, empty()
