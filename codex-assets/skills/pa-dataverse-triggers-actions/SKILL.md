---
name: pa-dataverse-triggers-actions
description: >-
  Dataverse connector: When a row is added/modified/deleted (scope/filter), List/Get/Add/Update rows, FetchXML, $expand, @odata.bind
---

# pa-dataverse-triggers-actions

The **Microsoft Dataverse** connector is the native data layer (premium). Trigger **"When a row is added, modified or deleted"** - pick **Change type**, **Table**, **Scope** (Organization/Business Unit/Parent:Child/User), optional **Select columns** (fire only when those change) and a **Filter rows** OData (`statuscode eq 1`) to gate runs. Actions: **List rows** (Filter rows OData `statecode eq 0 and createdon gt @{addDays(utcNow(),-7)}`, Select columns, Sort, Row count, **Expand Query** `$expand` for related tables, or paste **FetchXML** for complex/aggregate queries), **Get a row by ID**, **Add/Update/Delete a row**, **Relate/Unrelate rows** (N:N), **Perform a bound/unbound action** for custom APIs/plugins. Use **logical names** (`cr123_amount`). Pitfalls: modify trigger + Update on the same row = **infinite loop** - guard with a trigger filter or select-columns; **Select columns** cuts payload massively; lookups are set via `@odata.bind` (`accounts(guid)`); List rows pages at 5000 - enable **Pagination** and raise threshold for full sets; choice/optionset values are integers, map them explicitly.

**Tools:** Dataverse connector, When a row is added/modified/deleted, List rows, Filter rows (OData), FetchXML, $expand, @odata.bind
