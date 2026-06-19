---
name: pbi-storage-modes
description: >-
  Choose Import vs DirectQuery vs Direct Lake (2026: on-SQL vs on-OneLake) by data size, freshness, and capacity
---

# pbi-storage-modes

Three storage modes. Import loads data into the in-memory VertiPaq engine — fastest queries, full DAX, but data is a snapshot refreshed on schedule and limited by capacity RAM; default choice for most models. DirectQuery leaves data at source and sends SQL per interaction — real-time freshness and no size limit, but slow, limited DAX/time-intelligence, and source load; use only when data is too big to import or must be live. Direct Lake (Fabric) reads Delta/Parquet directly from OneLake with near-Import speed and near-DirectQuery freshness — the 2026 sweet spot. Know the two flavors: Direct Lake on SQL endpoint still falls back to DirectQuery when guardrails (row/memory limits or unsupported features) are exceeded; Direct Lake on OneLake runs DirectLakeOnly with NO DirectQuery fallback — if guardrails are exceeded queries FAIL rather than degrade, so SKU sizing must be accurate but performance is predictable, and it can combine tables from multiple sources. Pitfall #1: silent DQ fallback on Direct Lake-on-SQL masks an undersized capacity — monitor it. Pitfall #2: DirectQuery + complex DAX time-intelligence is painfully slow; pre-aggregate at source. Pitfall #3: mixing modes (composite) is powerful but adds limited-relationship caveats.

**Tools:** Import, DirectQuery, Direct Lake, OneLake, Fabric capacity
