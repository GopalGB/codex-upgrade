---
name: m365-excel-graph-api
description: >-
  Read/write Excel workbook ranges, tables, and formulas via Graph workbook sessions — when automating xlsx in OneDrive/SharePoint without opening the file
---

# m365-excel-graph-api

Target a workbook by drive item: `/sites/{id}/drive/items/{itemId}/workbook` (or `/me/drive/...`). Read a range: `GET .../workbook/worksheets('Sheet1')/range(address='A1:C10')` — returns `values`, `formulas`, `text`. Write: `PATCH` the same range with `{"values":[[1,2,3]]}`. Tables: `POST .../tables/{name}/rows/add` with `{"values":[[...]]}`.

**Use a session** for multi-call work: `POST .../workbook/createSession {"persistChanges":true}` returns `id`; send it as header `workbook-session-id` on every subsequent call. Persistent sessions batch edits and are far faster; non-persistent (`persistChanges:false`) is for read-only what-if calc.

Pitfall: without a session each call opens/closes the workbook (slow, and risks lost updates under concurrency). Pitfall 2: ranges are 1-based A1 notation strings, and `values` must be a 2D array even for one cell (`[[x]]`). Pitfall 3: workbook APIs only work on `.xlsx` stored in OneDrive/SharePoint (not local, not `.xls`), and the file must be <~25MB for the workbook engine; a checked-out or open-in-desktop file can 423-lock.

**Tools:** /drive/items/{id}/workbook, createSession, /worksheets/{name}/range, workbook-session-id
