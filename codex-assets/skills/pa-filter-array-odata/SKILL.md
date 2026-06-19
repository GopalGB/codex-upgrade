---
name: pa-filter-array-odata
description: >-
  Filter array action (in-memory) vs source-side OData $filter, Select for projection, and pushing filters to the data source
---

# pa-filter-array-odata

Two places to filter: **at the source** (connector Filter Query / OData `$filter`) or **in-memory** (the **Filter array** action). Prefer source-side - fewer rows, far faster. **OData filter** syntax: `Status eq 'Open' and Amount gt 1000`, operators `eq ne gt ge lt le`, functions `startswith(Title,'INV')`, `contains`, combine `and`/`or`, dates as ISO/`@{utcNow()}`. **Filter array** runs *after* fetch: set **From**, then a condition row (`item()?['Amount']` greater than 1000) or **advanced mode** `@greater(item()?['Amount'],1000)`; output = `body('Filter_array')`. Pair with **Select** to project/reshape (map "Name" -> `item()?['Title']`) before Create HTML table/CSV. Pitfalls: Filter array still pulled every row over the wire - if you went in-memory because OData "didn't work", the real fix is usually the **internal column name** or a missing index; coerce types before comparing (`int()`); "is not empty" = `@not(empty(item()?['Email']))`; chain Filter array + `length()` for counts without a loop; for a single match use `first(body('Filter_array'))` and null-check it.

**Tools:** Filter array, OData $filter (eq/ne/gt, startswith, contains), Select (projection), first(), length(), advanced mode @greater
