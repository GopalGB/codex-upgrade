---
name: algo-hashing-hashmaps
description: >-
  Trade space for O(1) average lookup with hashmaps/sets — complement search, frequency counting, grouping, dedup, caching seen state.
---

# algo-hashing-hashmaps

A hashmap gives expected O(1) insert/lookup/delete, worst-case O(n) under collisions. The killer pattern is **store-what-you-need, look-up-the-complement**: Two-Sum stores `value→index` and checks `target-x` in one pass — O(n) vs O(n²) brute force. Use a **set** for membership/dedup, a **Counter/defaultdict(int)** for frequencies, and `defaultdict(list)` for grouping (anagrams keyed by sorted string or a 26-count tuple). 

Key design choices: keys must be hashable and immutable — use tuples/frozensets, never lists. For grouping by canonical form, the key IS the canonical form. 

Pitfalls: (1) iterating a dict while mutating it raises/corrupts — collect keys first. (2) Hash collisions and adversarial inputs can degrade to O(n) (hash-flooding) — fine for interviews, matters in security. (3) Reaching for sorting (O(n log n)) when a hashmap solves it in O(n). (4) Float keys are fragile due to precision — round or use integers. Memory is O(n); if space is constrained, reconsider sorting or bit-tricks.

**Tools:** dict/HashMap, set, defaultdict, Counter, frozenset keys
