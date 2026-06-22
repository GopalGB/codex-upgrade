---
name: sql-pro
description: >-
  Expert SQL query craft — fast, correct, injection-safe queries: read EXPLAIN
  ANALYZE bottom-up, index strategy (composite/covering/partial), kill N+1, keyset
  pagination over OFFSET, window functions, CTEs vs subqueries, upserts, NULL
  three-valued-logic traps, parameterization, isolation levels. PostgreSQL-first,
  MySQL/SQLite/DuckDB notes. Use when writing or tuning a query, fixing a slow plan,
  or adding indexes (data-engineer owns pipelines). Triggers: "slow query",
  "EXPLAIN", "add an index", "N+1", "optimize this SQL", "upsert", "pagination".
---

# sql-pro — fast, correct, safe SQL (no MCP)

The QUERY-CRAFT layer: writing SQL that is fast, correct, and injection-proof. `data-engineer`
owns ELT/pipelines/lineage/orchestration — do not duplicate it. Here the unit of work is a single
query and its plan. **Default to PostgreSQL semantics**; dialect divergences are flagged inline.

## Locked-down office reality (no network, no admin)
- `psql` / `sqlite3` / `duckdb` CLIs may not be installed. Check: `command -v psql sqlite3 duckdb`.
- **DuckDB** is the killer offline tool: a single static binary, zero server, reads CSV/Parquet/JSON
  in place. If you can drop `duckdb` on the box, you can prototype + benchmark real SQL with no DBA:
  `duckdb -c "SELECT * FROM read_csv_auto('data.csv') LIMIT 5;"`. SQLite (`sqlite3 :memory:`) is the
  fallback if even that is absent — almost always present on macOS/Linux.
- No DB to hit? Reason from the plan + schema. Ask for `\d+ tablename` (psql) or the `CREATE TABLE`
  + existing index DDL before guessing. Never invent column names or index existence.

## Read EXPLAIN like an X-ray — BOTTOM-UP, INNERMOST-FIRST
Use `EXPLAIN (ANALYZE, BUFFERS)` — `ANALYZE` actually runs it (don't ANALYZE writes in prod without a
transaction you `ROLLBACK`). Read the deepest-indented node first; that is where execution starts.

```
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;
-- Each node: (cost=startup..total rows=PLANNER_estimate width=..)
--            (actual time=..  rows=REAL_rows loops=N)
```

The four numbers that matter, in order:
1. **estimate vs actual rows** — a 100x+ gap = stale stats or a bad correlation assumption. Fix with
   `ANALYZE tbl;` (refreshes stats) before touching the query. This is the #1 cause of bad plans.
2. **node type** — what you want to SEE vs what's a RED FLAG:
   - `Seq Scan` on a big table with a selective `WHERE` → missing/unused index. (Fine for small tables
     or when returning >~10-20% of rows — a scan beats random index I/O there.)
   - `Index Scan` / `Index Only Scan` → good. "Only" means it never touched the heap (covering index).
   - `Nested Loop` with large `loops=N` on the inner side → the N+1 plan; usually wants a `Hash Join`
     or `Merge Join`. Nested Loop is correct only when the outer side is tiny.
   - `Bitmap Heap Scan` → many matching rows via an index; reasonable middle ground.
3. **`Rows Removed by Filter`** — rows read then thrown away. High value = the index isn't selective
   enough, or the predicate isn't sargable (see below). Push the filter into the index.
4. **`loops=N`** — multiply `actual time` by `loops` for the node's true cost. A "fast" node run 50k
   times is your bottleneck.

MySQL: `EXPLAIN ANALYZE` (8.0.18+) or `EXPLAIN FORMAT=JSON`. SQLite: `EXPLAIN QUERY PLAN` (coarse —
shows SCAN vs SEARCH + index used). DuckDB: `EXPLAIN ANALYZE`.

## Indexing — the decision rules (not "add an index and pray")
- **Composite column order = leftmost-prefix rule.** `INDEX (a, b, c)` serves `WHERE a=`, `WHERE a= AND
  b=`, `WHERE a= AND b= AND c=`, and `ORDER BY a,b,c`. It does NOT serve `WHERE b=` alone. Order:
  **equality columns first, then the range/sort column last.** `WHERE tenant=? AND created_at > ?
  ORDER BY created_at` → `INDEX (tenant, created_at)`.
- **Covering index → Index-Only Scan.** Put the columns the query SELECTs into the index so the heap is
  never read: Postgres `CREATE INDEX ix ON orders (customer_id) INCLUDE (status, total);`. MyS/InnoDB:
  the PK is always implicitly included (clustered); add columns to the index body. Index-Only Scan in
  Postgres also needs the visibility map fresh (`VACUUM`).
- **Partial index for a hot filtered subset** — index only the rows you query, smaller + faster:
  `CREATE INDEX ix_open ON jobs (created_at) WHERE status = 'open';` Great for soft-delete
  (`WHERE deleted_at IS NULL`) or a small "pending" slice of a huge table. (Postgres + SQLite support
  partial indexes; MySQL does NOT — use a generated column or a narrower table.)
- **Expression index** when you filter on a function: `WHERE lower(email)=?` needs
  `CREATE INDEX ON users (lower(email));` or it can't be used.
- **Sargability** — an index on `col` is unusable if you wrap `col` in a function or do math on it.
  `WHERE date(created_at)=?` → seq scan; rewrite as a range: `WHERE created_at >= ? AND created_at < ?`.
  `WHERE col + 1 = 5` → `WHERE col = 4`. Leading-wildcard `LIKE '%x'` can't use a b-tree (use trigram/FTS).
- **When an index WON'T help / hurts:** tiny tables; low-cardinality columns (a boolean — usually
  worthless unless partial); queries returning a large fraction of rows; write-heavy tables (every index
  is a write tax + bloat). Don't index speculatively — index the predicates that show up in EXPLAIN.

## Kill N+1 at the query layer
N+1 = a loop in app code firing one query per row. The plan-level symptom is a `Nested Loop` with huge
`loops`. The fix is to **fetch the set in one query**:
```sql
-- BAD: app does SELECT * FROM line_items WHERE order_id = ? once per order
-- GOOD: one round-trip
SELECT o.id, json_agg(li.*) AS items          -- Postgres aggregate the children
FROM orders o JOIN line_items li ON li.order_id = o.id
WHERE o.id = ANY($1) GROUP BY o.id;            -- $1 is an int[] of order ids
```
ORM escapes: `JOIN`/`include`/`prefetch_related`/`joinedload`. Verify by counting queries in a test
(the kit's `data-engineer` covers pipeline-level batching; here it's per-request query shape).

## Patterns a generic agent gets wrong
**Semi/anti-joins — `EXISTS` vs `IN` vs `JOIN`:**
- Semi-join (does a match exist?): `WHERE EXISTS (SELECT 1 FROM b WHERE b.a_id = a.id)`. Prefer `EXISTS`
  over `IN (subquery)` — it short-circuits and is NULL-safe. A plain `JOIN` can duplicate left rows if
  the right side isn't unique; `EXISTS` never does.
- Anti-join (no match): `WHERE NOT EXISTS (...)`. **Never `NOT IN (subquery)` if the subquery column is
  nullable** — one NULL makes the whole `NOT IN` return zero rows (three-valued logic: `x NOT IN (1,
  NULL)` is `UNKNOWN`, never `TRUE`). This is a silent correctness bug. Use `NOT EXISTS` or `LEFT JOIN
  ... WHERE b.id IS NULL`.

**NULL / three-valued logic traps:** `NULL = NULL` is `UNKNOWN`, not `TRUE`; use `IS NULL` /
`IS DISTINCT FROM`. `COUNT(col)` skips NULLs but `COUNT(*)` counts rows. `NULL` sorts last in
Postgres `ASC` (control with `NULLS FIRST/LAST`). Aggregates ignore NULLs — `AVG` over a column with
NULLs divides by the non-null count.

**Window functions** for running totals / rank / dedup without a self-join:
```sql
SELECT *, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn
FROM events;                       -- rn=1 is the latest row per user; filter rn=1 in an outer query
SELECT id, SUM(amount) OVER (PARTITION BY acct ORDER BY ts
         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_balance FROM ledger;
```
You cannot filter on a window result in `WHERE` (it's computed after) — wrap in a CTE/subquery and
filter the alias. `QUALIFY` does this in one line on DuckDB (and Snowflake/BigQuery), NOT Postgres/MySQL.

**CTEs vs subqueries — the optimization-fence caveat:** A CTE reads cleaner, but historically
PostgreSQL **materialized** every `WITH` (an optimization fence — predicates didn't push in). **Postgres
12+ inlines** non-recursive, single-reference CTEs by default; force either way with
`WITH x AS MATERIALIZED (...)` / `AS NOT MATERIALIZED (...)`. If you're on PG<12 and a CTE is slow,
rewrite it as a subquery so the planner can push filters. MySQL 8 and SQLite also inline. Recursive
CTEs (`WITH RECURSIVE`) are the right tool for trees/graphs/hierarchies.

**Set ops:** `UNION` dedups (sorts — costs); `UNION ALL` does not — use `ALL` unless you truly need
distinct. `EXCEPT`/`INTERSECT` for set difference/overlap (MySQL got these in 8.0.31; older MySQL needs
`NOT EXISTS` / `JOIN` rewrites).

## Upserts — dialect-specific, get it right
```sql
-- PostgreSQL / SQLite
INSERT INTO inv (sku, qty) VALUES ($1, $2)
ON CONFLICT (sku) DO UPDATE SET qty = inv.qty + EXCLUDED.qty
RETURNING id;                       -- RETURNING: Postgres yes; SQLite 3.35+ yes; MySQL NO
```
- **MySQL** has no `ON CONFLICT`: use `INSERT ... ON DUPLICATE KEY UPDATE qty = qty + VALUES(qty);`
  (no `RETURNING`; use `LAST_INSERT_ID()` / a follow-up select).
- **`MERGE`** (SQL standard) exists in Postgres 15+, SQL Server, Oracle — more flexible (insert/update/
  delete in one) but verbose; `ON CONFLICT` is simpler for the common upsert. The conflict target must
  have a unique/PK constraint or it errors.

## Keyset (seek) pagination — never large OFFSET
`OFFSET 100000 LIMIT 20` scans and discards 100k rows every page — O(offset). Use a seek on the last
row's sort key (O(log n) per page via the index):
```sql
-- page 1
SELECT id, created_at FROM events ORDER BY created_at DESC, id DESC LIMIT 20;
-- next page: pass the LAST row's (created_at, id) as the cursor
SELECT id, created_at FROM events
WHERE (created_at, id) < ($last_created_at, $last_id)   -- row-value comparison, tie-break on id
ORDER BY created_at DESC, id DESC LIMIT 20;
```
Needs an index matching the `ORDER BY`. Include a unique tiebreaker (`id`) so pages don't skip/repeat on
ties. Trade-off: no random "jump to page N" — that's the cost of being fast. (MySQL/SQLite/DuckDB all
support row-value `(a,b) < (x,y)` comparison.)

## SECURITY — parameterize, always (the kit has a security floor)
**Never string-concatenate user input into SQL. No f-strings, no `+`, no `%`, no template literals.**
Use the driver's placeholders so values are sent out-of-band and can never be parsed as SQL:
```python
cur.execute("SELECT * FROM users WHERE email = %s", (email,))   # psycopg
db.execute("SELECT * FROM users WHERE email = ?", [email])       # sqlite3 / DuckDB
```
- Identifiers (table/column names) can't be parameterized — if dynamic, validate against an allow-list,
  never interpolate raw user text. A user-chosen `ORDER BY` column = allow-list only.
- `LIKE` user input: escape `%` `_`; for `IN`-lists generate N placeholders, never join strings.
- Grant least privilege: the app role should not own the schema or have `DROP`. Read paths get a
  read-only role.

## Transactions & isolation (correctness under concurrency)
- Wrap multi-statement invariants in `BEGIN ... COMMIT`; on error, `ROLLBACK`. Keep transactions SHORT —
  open transactions hold locks and bloat.
- Default isolation: Postgres = `READ COMMITTED` (each statement sees latest committed). Risks:
  non-repeatable reads, lost updates on read-modify-write. Fixes: `SELECT ... FOR UPDATE` to lock rows
  you'll modify, or bump to `REPEATABLE READ` / `SERIALIZABLE` (Postgres SERIALIZABLE can raise a
  serialization error — your code MUST retry the transaction).
- **MySQL/InnoDB default is `REPEATABLE READ`** (different from Postgres — don't assume). **SQLite is
  single-writer** (one write transaction at a time; enable WAL mode for concurrent reads). DuckDB is
  single-process OLAP — concurrency is not its job.

## Workflow fit
Slow query → reproduce with `EXPLAIN (ANALYZE, BUFFERS)` → fix stats (`ANALYZE`) → make the predicate
sargable → add the right index (composite/covering/partial) → re-measure, don't assume. Schema/index
changes that touch large tables or migrations are irreversible-class — gate them through the GSD plan
loop and confirm `CREATE INDEX CONCURRENTLY` (Postgres, non-blocking) before running on a live table.
Pipeline/ELT/lineage work hands off to `data-engineer`.
