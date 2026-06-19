---
name: pbi-composite-models
description: >-
  Combine Import + DirectQuery + DirectQuery-over-PBI-datasets in one composite model; manage storage modes and limited relationships
---

# pbi-composite-models

Composite models mix storage modes in one model: some tables Import, some DirectQuery, plus DirectQuery over Power BI semantic models / Azure AS (chaining a shared certified model and extending it locally). Set per-table Storage mode in Model view (Import, DirectQuery, or Dual). Use Dual for dimensions shared by both Import and DirectQuery facts — Dual tables act as Import when queried alone (fast) and as DirectQuery when joined to a DQ fact (avoids slow cross-source joins). This pattern underpins aggregations: an Import agg table over a DirectQuery detail fact, with Dual dimensions. Pitfall #1: a relationship spanning two different sources/storage modes becomes a 'limited' relationship — it can't assume referential integrity, may show a blank row, and disables some optimizations; minimize cross-source relationships. Pitfall #2: setting a shared dimension to Import instead of Dual forces slow per-row DQ joins. Pitfall #3: DirectQuery over a remote semantic model surfaces the remote RLS — understand whose security applies (the chained model's RLS travels). Pitfall #4: composite adds governance complexity (multiple credentials, mixed refresh). Pitfall #5: measures defined on a chained remote model may not all be visible/editable locally — you extend, you don't override. Use composite when you must blend a real-time source with imported data or extend a central model, not as a default.

**Tools:** composite models, dual storage mode, DirectQuery on Power BI datasets, aggregations
