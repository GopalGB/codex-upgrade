---
name: sde-database-indexing
description: >-
  Speed reads with B-tree and hash indexes - composite key order, covering indexes, and the write-cost tradeoff.
---

# sde-database-indexing

An index is a sorted side-structure that turns O(n) scans into O(log n) lookups. Most RDBMS indexes are **B+ trees** (range + equality + ORDER BY); **hash indexes** do O(1) equality only (no ranges). **Index the columns in WHERE, JOIN, ORDER BY**. **Composite index column order is the rule that trips people**: an index on (a,b,c) serves predicates on a, a+b, a+b+c, but NOT b alone (leftmost-prefix rule). Put the equality/high-selectivity column first, the range column last. A **covering index** includes every column the query needs so the engine never touches the table (index-only scan) - huge win. **Cost**: each index slows INSERT/UPDATE/DELETE and consumes space; only add indexes a real query uses. **Verify with EXPLAIN/EXPLAIN ANALYZE** - look for 'index scan' not 'seq scan', and a low estimated rows. **Pitfall**: indexing a low-cardinality column (e.g., boolean) - the planner ignores it; and wrapping the column in a function (`WHERE lower(email)=...`) disables the index unless you build an expression index.

**Tools:** B-tree, composite index, covering index, EXPLAIN, cardinality
