---
name: pbi-relationships-cardinality
description: >-
  Configure relationship cardinality, cross-filter direction, and active/inactive relationships; fix many-to-many and ambiguity
---

# pbi-relationships-cardinality

Relationships in Model view define how filters propagate. Default and best is one-to-many (dimension '1' side to fact 'many' side) with single cross-filter direction (dimension filters fact). Cardinality options: 1:*, *:1, 1:1, and *:* (many-to-many). Avoid native *:* relationships when possible — they're slower and can produce unexpected blank-row semantics; instead introduce a bridge dimension of distinct keys (1:* on both sides). For multiple date roles (OrderDate, ShipDate) create multiple relationships but only one can be active; the others are inactive (dashed). Activate an inactive one inside a measure: `Shipped Sales = CALCULATE([Total Sales], USERELATIONSHIP('Date'[Date], Sales[ShipDate]))`. To filter across an unrelated table use `TREATAS(VALUES(A[Key]), B[Key])`. Pitfall #1: ambiguous paths (two routes between tables) — Power BI deactivates one automatically; verify which, or your numbers silently use the wrong path. Pitfall #2: turning on bi-directional cross-filter to fix a slicer often introduces ambiguity errors elsewhere — prefer CROSSFILTER inside a specific measure. Pitfall #3: a relationship on a column with blanks/duplicates on the 'one' side fails or adds a blank member; clean keys first. Always check the relationship is on integer keys for speed.

**Tools:** USERELATIONSHIP, CROSSFILTER, TREATAS, relationships, cardinality
