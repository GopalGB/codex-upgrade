---
name: data-engineer
description: >-
  Modern data engineering — idempotent ELT, no-OOM big-data, schema contracts, lineage,
  CI-tested transforms. NOT a pandas script that read_csv's everything and dies. Use for:
  data pipelines, ETL/ELT, dbt/SQLMesh models, DuckDB/Polars, ingestion, orchestration,
  data quality, warehouses/lakehouse. Triggers: "data pipeline", "ETL", "ELT", "dbt",
  "SQLMesh", "DuckDB", "Polars", "Dagster", "Airflow", "dlt", "Iceberg", "data quality",
  "schema evolution", "big csv", "process a huge dataset".
---

# data-engineer — idempotent, no-OOM, tested (verified 2026)

ELT not ETL: land raw, push the transform down to the engine where the data already is.
Idempotency is the whole game — every load/transform must be safely re-runnable.

## Absorb these repos (current, maintained — beware stale knowledge)
- **dbt-labs/dbt-core** (13k) https://github.com/dbt-labs/dbt-core — SQL-first transforms
  (models/refs/tests/snapshots/incremental). ⚠ **dbt Core v2.0 is RUST (Fusion engine),
  June 2026** — do NOT generate pre-1.5 patterns.
- **TobikoData/sqlmesh** (3.1k) https://github.com/TobikoData/sqlmesh — fixes dbt's
  incremental/state pain: virtual (zero-copy) dev environments, column-level lineage,
  automatic breaking-change detection. Linux-Foundation-governed (safe to adopt).
- **duckdb/duckdb** (38.9k) — in-process OLAP SQL; reads/writes Parquet/CSV/JSON/Iceberg/
  Delta from local/S3/GCS. The "SQLite for analytics" — default for local dev + CI.
- **pola-rs/polars** (38.8k) — lazy/streaming DataFrame (Arrow, predicate/projection
  pushdown, larger-than-RAM). The pandas replacement for real data.
- **dlt-hub/dlt** (5.5k) https://github.com/dlt-hub/dlt — code-first Python EL with
  automatic schema inference + evolution + incremental + state. The ingest default.
- **dagster-io/dagster** (15.7k) — asset-oriented orchestrator (software-defined assets,
  declarative auto-materialize, partitions/backfills, native dbt/dlt/Sling). Greenfield default.
- **apache/airflow** (45.9k) — incumbent. ⚠ **Airflow 3.x** = assets (renamed from datasets)
  + data-aware scheduling; don't generate 1.x/2.x raw-operator DAGs.
- **apache/iceberg-python (PyIceberg)** — open lakehouse table format (JVM-free): schema/
  partition evolution, time travel. **Iceberg = 2026 open default**; Delta strongest in
  Databricks.
- **unionai-oss/pandera** (3.9k) — DataFrame schema validation (⚠ org is `unionai-oss`, not
  `pandera-dev`). + **elementary-data/elementary** for dbt-native observability.
- **ibis-project/ibis** (6.6k) + **tobymao/sqlglot** (9.3k) — portable dataframe API /
  SQL transpiler+lineage across 20+ engines (write once, run on DuckDB→BigQuery/Snowflake).

## Canonical 2026 stack
Ingest: **dlt** (code-first, schema evolution) / managed connectors for the long tail ·
Table format: **Iceberg** (+ REST catalog) · Engine: **DuckDB** (single-node/dev/CI) +
**Polars** (Python pipelines) · Transform: **dbt Core v2/Fusion** (or **SQLMesh** at scale)
· Orchestrate: **Dagster** (assets) or Airflow 3.x · Quality: **Pandera** (Python) + dbt
tests + Elementary · Substrate: **Arrow** (memory) + **Parquet** (disk) under everything ·
env: **uv** · runs in git with PR review + CI.

## Deep patterns
1. **Idempotency** — MERGE/upsert on a stable key (dlt `write_disposition='merge'`, dbt
   incremental + unique_key); re-runs converge, never duplicate.
2. **Late-arriving data** — naive `WHERE updated_at > max()` silently DROPS late records;
   use a lookback window / watermark + partition-replace backfill.
3. **Schema evolution is DESIGNED** — pin a contract at ingest (dlt evolve/freeze/discard
   per column); decide additive-only vs breaking deliberately.
4. **Big data without OOM** — never `pd.read_csv(huge)`; stream — Polars
   `scan_parquet().collect(streaming=True)` or DuckDB querying Parquet on S3 with
   projection/predicate pushdown.
5. **Column-level lineage** — dbt Fusion / SQLMesh / sqlglot show which downstream columns
   break BEFORE you run. Gate merges on breaking-change detection.
6. **Virtual/zero-copy dev** — SQLMesh virtual environments (or dbt defer + state:modified)
   build only changed models against prod data without copying it.
7. **Test transforms in CI on DuckDB** — spin DuckDB in GitHub Actions, run dbt/SQLMesh
   build + data tests against seeds/sampled prod on every PR (sub-minute, $0 warehouse).
8. **ELT + push-down** — land raw, transform in-engine (Ibis/dbt/SQLMesh compile to
   server-side SQL); pulling into Python then writing back doesn't scale.

## Expert vs generic
Generic: pandas read_csv → OOM, full reload or lossy incremental, assumes static schema,
no CI, hardcodes one dialect, ETL-pulls-into-python, treats Parquet as "just a file".
Expert: Polars/DuckDB push-down, MERGE-on-key + lookback, schema contracts, CI on DuckDB,
Ibis/sqlglot portability, ELT push-down, Arrow/Parquet column-pruning awareness.

## Pitfalls (stale-knowledge traps)
dbt-is-Python-and-slow (it's Rust/Fusion now) · Airflow 1.x/2.x DAGs (use 3.x assets) ·
`pandera-dev` (use `unionai-oss/pandera`) · defaulting to Great Expectations (heavy — prefer
Pandera/dbt-tests/Elementary) · Iceberg vs Delta confusion (Iceberg = open default) ·
treating SQLMesh as risky (it's LF-governed).

## Guardrails
Never load secrets/PII into logs; parameterize. For the ML data boundary see `ml-engineer`
(DuckDB/Polars → numpy only at the model edge). For huge Excel specifically use `xlsx-wrangler`.
