---
name: pbi-performance-vertipaq-aggregations
description: >-
  Tune model speed: reduce VertiPaq cardinality, use aggregation tables, and profile DAX with Performance Analyzer/DAX Studio
---

# pbi-performance-vertipaq-aggregations

VertiPaq compresses columns; compression depends on cardinality (distinct values), so the biggest wins come from reducing distinct values. Split datetime into separate Date and Time columns (a datetime to the second has millions of distinct values — kills compression); drop unused columns; round floats; avoid high-cardinality text keys (use integer surrogates). Profile with VertiPaq Analyzer (in DAX Studio) to find the fattest columns by size, and use Power BI's Performance Analyzer (View > Performance Analyzer > Start recording > interact) to see each visual's DAX query duration. Copy the slow query into DAX Studio > Server Timings to see Formula Engine vs Storage Engine split — high FE time means an inefficient measure, high SE with many queries means missing materialization. For huge facts, build aggregation tables (Model > Manage aggregations) mapping a pre-summarized table to the detail fact at, say, day+product grain; the engine transparently hits the agg for summary queries and the detail only when needed. Pitfall #1: a single high-cardinality column (GUIDs, timestamps, free-text notes) can be larger than the rest of the model combined. Pitfall #2: aggregations only work in Import/DirectQuery composite setups and require matching grain + GroupBy columns. Pitfall #3: optimizing DAX before fixing the model is backwards — fix cardinality first.

**Tools:** VertiPaq Analyzer, DAX Studio, aggregations, Performance Analyzer, cardinality
