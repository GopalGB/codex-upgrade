---
name: pbi-dataflows
description: >-
  Centralize reusable ETL with Power BI/Fabric dataflows (Gen2) so multiple datasets share cleaned, certified tables
---

# pbi-dataflows

Dataflows run Power Query in the cloud and store the output (in Dataflows Gen2, to a Fabric Lakehouse/Warehouse or internal storage) so many semantic models reuse the same cleaned tables — one source of truth for, say, a conformed Date or Customer dimension. Build in Power Query Online (workspace > New > Dataflow Gen2), apply transforms, and set a destination. Use linked entities to reference another dataflow's table without re-importing, and computed entities to transform on top of already-loaded data (in-storage compute). This separates ETL (dataflow, refreshed on its own schedule) from modeling (dataset connects to the dataflow). Gateways apply for on-prem sources just like datasets. Pitfall #1: chaining many computed/linked entities creates refresh dependency chains — if an upstream dataflow fails, downstream silently uses stale data; orchestrate refresh order. Pitfall #2: computed entities require the enhanced compute engine / appropriate capacity; on Pro they may be unavailable or slow. Pitfall #3: doing per-report transforms in each dataset instead of once in a dataflow duplicates logic and load — centralize. Pitfall #4: Gen1 vs Gen2 differ (Gen2 has data destinations, better compute, Fabric integration) — new work should use Gen2. Pitfall #5: large dataflow refreshes can be slower than a direct import for a single consumer; dataflows pay off with reuse, not single use.

**Tools:** Dataflows Gen2, Power Query Online, computed entities, linked entities, staging
