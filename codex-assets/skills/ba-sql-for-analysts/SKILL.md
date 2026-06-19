---
name: ba-sql-for-analysts
description: >-
  Analyst SQL: window functions, CTEs, conditional aggregation, date_trunc cohorts, anti-joins for gaps; avoid the SELECT-DISTINCT fan-out trap and GROUP BY filtered-with-WHERE-not-HAVING bug.
---

# ba-sql-for-analysts

Lean on window functions for analyst work: ROW_NUMBER()/RANK() OVER (PARTITION BY user ORDER BY ts) to dedupe-to-latest or get first-touch; SUM(...) OVER (ORDER BY d) for running totals; LAG/LEAD for period-over-period deltas; AVG(...) OVER (ORDER BY d ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) for rolling 7-day. Structure multi-step logic in CTEs (WITH), one transformation per CTE, named for what it produces — readable and debuggable beats nested subqueries. Conditional aggregation pivots without a PIVOT clause: SUM(CASE WHEN status='paid' THEN amt END). Bucket time with date_trunc('week', ts) for cohorts. Find missing records with a LEFT JOIN ... WHERE b.id IS NULL anti-join, not NOT IN (which breaks on NULLs). Expert moves: COUNT(DISTINCT) is the tell that a JOIN fanned out — fix the grain instead; filter pre-aggregation with WHERE, post-aggregation with HAVING (the classic bug: putting an aggregate condition in WHERE). QUALIFY (BigQuery/Snowflake) filters window results directly. Pitfalls: SELECT DISTINCT masking a join fan-out instead of fixing it; NULL-unsafe = comparisons; non-sargable WHERE (functions on indexed columns); forgetting timezone in date_trunc. Always sanity-check row counts before and after a join.

**Tools:** PostgreSQL, BigQuery, Snowflake, DuckDB, dbt
