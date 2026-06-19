---
name: vba-regexp
description: >-
  Pattern matching with VBScript RegExp — extract/validate/replace text, Global/IgnoreCase, capturing groups via SubMatches, Test vs Execute, build a regex UDF, common patterns
---

# vba-regexp

VBA has no native regex; use the COM `VBScript.RegExp` engine: `Set re = CreateObject("VBScript.RegExp")` (or reference Microsoft VBScript Regular Expressions 5.5 for early binding). Set `re.Pattern`, `re.Global = True` (match all, not just first), `re.IgnoreCase = True`, `re.MultiLine` as needed. `re.Test(str)` returns Boolean (validation); `re.Execute(str)` returns a `MatchCollection` you iterate; `re.Replace(str, repl)` does substitution with `$1`/`$2` backreferences.

Expert moves: pull captured pieces from `Match.SubMatches(0)`, `.SubMatches(1)` — e.g., split `INV-2026-0042` with pattern `(\w+)-(\d{4})-(\d+)`. Wrap it in a UDF: `=RegexExtract(A1,"\d+")`. Common patterns: email `[\w.-]+@[\w.-]+\.\w+`, phone digits `\d{10}`, trim multiple spaces `re.Pattern="\s+": re.Replace(s," ")`. Reuse one `re` object across a loop — creating it per iteration is slow.

Pitfalls: the engine is the **VBScript flavor** (POSIX-ish ERE) — no lookbehind, no named groups, limited Unicode classes; `\d` is ASCII-centric. `.Execute` returns matches, not submatches at the top level — drill into `.SubMatches`. Greedy `.*` over-matches; use `.*?` (lazy) or character classes. Forgetting `.Global = True` only replaces the first hit. On Mac Excel the VBScript engine may be unavailable — test before relying on it cross-platform.

**Tools:** VBScript.RegExp, CreateObject, .Pattern, .Global, .IgnoreCase, .Test, .Execute, Match, SubMatches, .Replace, Microsoft VBScript Regular Expressions
