---
name: pbi-star-schema-modeling
description: >-
  Design a star schema (facts + conformed dimensions) instead of a flat table or snowflake — the foundation of fast, correct Power BI models
---

# pbi-star-schema-modeling

The single highest-leverage decision in Power BI: model as a star schema — narrow fact tables (measures + foreign keys, high row count) surrounded by dimension tables (descriptive attributes, low row count). Never import one giant flat denormalized table; it bloats memory, duplicates attributes, and breaks cross-filtering. Build dimensions for Date, Product, Customer, Geography, etc., each with a single-column key relating to the fact. Avoid snowflaking (dimensions linking to sub-dimensions) — flatten the snowflake into one dimension in Power Query so relationships stay single-hop and DAX stays simple. Keep facts at a consistent grain (e.g. one row per order line); if you have multiple grains (orders vs targets), use separate fact tables connected through shared (conformed) dimensions, not a merge. Pitfall #1: bi-directional relationships to make filtering 'just work' cause ambiguity and performance hits — keep single-direction (dimension filters fact) and use CROSSFILTER/TREATAS in DAX when you truly need reverse flow. Pitfall #2: relating two fact tables directly creates ambiguous paths — always route through a dimension. Pitfall #3: text/composite business keys as relationship keys are slow; prefer integer surrogate keys. A clean star also makes RLS, aggregations, and Direct Lake far simpler.

**Tools:** data modeling, fact tables, dimension tables, surrogate keys
