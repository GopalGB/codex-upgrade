---
name: xls-xlookup-lookups
description: >-
  XLOOKUP, INDEX/MATCH, two-way lookups, approximate match, multi-criteria and reverse lookups — replace VLOOKUP, handle not-found and left-lookups
---

# xls-xlookup-lookups

Default to **XLOOKUP** over VLOOKUP: `=XLOOKUP(lookup, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`. It looks left, returns spilled rows/cols, and the 4th arg kills `#N/A` cleanly (no nested IFERROR). Set `match_mode=0` for exact (default), `-1`/`1` for next-smaller/larger, `2` for wildcard. Use `search_mode=-1` to find the LAST match (latest record). **Two-way lookup:** `=XLOOKUP(rowKey,rowHdrs,XLOOKUP(colKey,colHdrs,grid))` — cleaner than INDEX/MATCH/MATCH. **Multi-criteria:** concatenate keys `XLOOKUP(a&"|"&b, rng1&"|"&rng2, ret)` or use a BYROW/boolean approach. Keep **INDEX/MATCH** for legacy files: `=INDEX(ret,MATCH(key,lookup,0))` — survives column insertion, unlike VLOOKUP's hardcoded col_index. Pitfalls: VLOOKUP approximate match (4th arg TRUE/omitted) silently returns wrong values on unsorted data — always pass FALSE/0. Numbers-stored-as-text break exact match (wrap with VALUE or fix the source). For binary-search speed on huge sorted lists, use `search_mode=2`.

**Tools:** XLOOKUP, INDEX, MATCH, VLOOKUP, HLOOKUP, CHOOSE
