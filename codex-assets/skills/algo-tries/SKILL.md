---
name: algo-tries
description: >-
  Trie (prefix tree) for string sets — autocomplete, prefix search, word-dictionary with wildcards, longest-common-prefix, XOR-maximization via bit-tries.
---

# algo-tries

A trie stores strings by shared prefixes: each node holds children (a 26-slot array for lowercase, or a hashmap for large alphabets) and an `isEnd` flag. Insert/search/startsWith are O(L) in the word length — independent of how many words are stored — which beats hashing when you need *prefix* queries (autocomplete, spell-check, IP routing). 

For wildcard search (`.` matches any char), recurse over all children at a `.` position. **Bit-trie** (binary trie over the 32 bits of integers) solves maximum-XOR-pair: insert numbers bit-by-bit, then for each query greedily take the opposite bit at each level to maximize XOR — O(32) per query. 

Memory is the tradeoff: 26-array nodes are fast but bloat on sparse data; hashmap nodes save space but add overhead — choose per alphabet. 

Pitfalls: (1) forgetting the `isEnd` flag and treating any reached node as a complete word ('app' matching inside 'apple'). (2) array-vs-map mismatch for the alphabet (unicode, uppercase). (3) not handling deletion (mark non-end and prune empty branches) when required. (4) ignoring that a node can be both a prefix and a complete word.

**Tools:** children map/array[26], isEnd flag, prefix walk, bitwise trie
