---
name: xls-power-query-transform
description: >-
  Power Query (Get & Transform): import/clean/reshape data, unpivot, merge/append queries, M language, query folding, refresh
---

# xls-power-query-transform

Power Query (Data > Get Data) is the ETL layer — record steps once, refresh forever. Core moves: **Remove/Promote Headers**, **Change Type** (set explicitly, locale-aware), **Split Column** by delimiter, **Unpivot** (select id cols > Unpivot Other Columns to turn wide cross-tabs into tidy long data — the single most valuable PQ skill), **Group By** for aggregation, **Fill Down** for merged-cell gaps. **Merge Queries** = SQL join (pick join kind: left outer/inner/anti); **Append Queries** = stack tables (great for combining monthly files via **Get Data from Folder**). The **M** language underlies every step (formula bar + Advanced Editor). **Query folding**: when sourcing from a database, PQ pushes steps back to SQL — keep filters/removes EARLY so they fold (check 'View Native Query'); folding breaks after certain steps (added index, custom M). Pitfalls: 'Changed Type' hardcodes column names and breaks if source headers shift — rename defensively; load to Connection Only + Data Model for big data instead of dumping to a sheet; set datatypes before loading to avoid downstream errors.

**Tools:** Power Query, M language, Merge, Append, Unpivot, Query Folding
