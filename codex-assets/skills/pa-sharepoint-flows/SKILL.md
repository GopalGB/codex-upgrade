---
name: pa-sharepoint-flows
description: >-
  SharePoint flows: item/file triggers, Get items with OData Filter Query, Update item, Send an HTTP request to SharePoint REST, attachments
---

# pa-sharepoint-flows

The **SharePoint** connector (standard) automates lists/libraries. Triggers: **When an item is created**, **created or modified**, **When a file is created (properties only)**, **For a selected item** (instant). Key actions: **Get items** (**Filter Query** uses internal names: `Status eq 'Open' and Created gt '2026-01-01'`; set **Top Count** + enable Pagination for >100 rows), **Get item**, **Create/Update/Delete item**, **Get/Add attachment**, **Get attachment content**, file actions **Get file content**, **Create file**, **Move/Copy file**. For what the connector can't do, **"Send an HTTP request to SharePoint"** hits the **REST/CSOM API** (`_api/web/lists/getbytitle('Tasks')/items`, POST, `Content-Type: application/json;odata=verbose`) for managed metadata, permissions, batching. Pitfalls: **Filter Query uses internal names** not display names ("Order #" may be `Order_x0020__x0023_`); date filters need ISO strings; people/lookup fields are objects - set via `{"Claims":"i:0#.f|membership|user@x.com"}` or the lookup Id; the modify trigger looping on its own Update needs a guard column; lists past the 5000-item view threshold fail on un-indexed columns - add an index or filter on an indexed column; choice columns return `{"Value":"..."}`.

**Tools:** SharePoint connector, Get items (Filter Query OData), Update item, Send an HTTP request to SharePoint, internal column names, pagination
