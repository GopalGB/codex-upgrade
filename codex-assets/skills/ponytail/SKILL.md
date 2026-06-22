---
name: ponytail
description: >-
  The minimal-code discipline — before writing ANY code, climb the laziness ladder
  and stop at the first rung that holds: does this need to exist (YAGNI)? · stdlib? ·
  platform/framework native? · an already-installed dep? · one line? · only then the
  minimum that works. Delete over add, boring over clever, fewest files, no unrequested
  abstractions. Use on every code-writing decision. NEVER simplify away input validation,
  error handling, security, or accessibility. Triggers: "minimal", "simplest way",
  "don't over-engineer", "is this needed", "smallest change", "reduce code", "too complex".
---

# ponytail — write the least code that works (no MCP)

Think like the laziest senior dev in the room: the best code is the code you never
wrote. Lazy means *efficient*, not careless. Every line is a line someone debugs at
3am. This is a reflex applied to **every** code-writing decision — it does not need a
command. It refines the kit's reuse ladder (§D) and code discipline (§K).

## The ladder — run BEFORE writing code, stop at the first rung that holds
1. **Does this need to exist at all?** Speculative need → skip it, say so in one line. (YAGNI — the cheapest code is none.)
2. **Standard library does it?** Use it. (`itertools`, `collections`, `pathlib`, `dataclasses`, `functools.lru_cache`, `sqlite3`, `json`, `argparse` …)
3. **Platform / framework native?** A DB constraint over app validation, a CSS rule over a JS handler, `<input type="date">` over a picker lib, a built-in over a plugin.
4. **An already-installed dependency?** Reuse it before adding a new one (pairs with §E expert-hire / §D reuse). Never add a dep for what a few lines do.
5. **Can it be one line?** Write the one line.
6. **Only then** — the minimum code that works.

The ladder is a reflex, not a research project. Two rungs both work → take the higher
one and move on. The first lazy solution that works is the right one.

## Rules
- **No unrequested abstractions:** no interface with one implementation, no factory for
  one product, no config knob for a value that never changes, no "manager/helper/util"
  layer added "for later". Later can scaffold for itself.
- **Deletion over addition.** The best diff is often a `-`. Boring over clever — clever
  is what someone decodes at 3am.
- **Fewest files.** Shortest working diff wins. Don't split into modules before a second
  caller exists.
- **Patch, don't regenerate.** Smallest change that fixes it (this is §D + the
  `PATCH_DONT_REGENERATE` lesson). Rewrite a whole file only if asked, or a patch is more
  fragile — and say which.
- **Two stdlib options, same size?** Pick the one that's correct on edge cases. Lazy =
  less code, never the flimsier algorithm.

## When NOT to be lazy (these are not optional — never simplify them away)
Input validation at trust boundaries · error handling that prevents data loss · security
(parameterize queries, no secrets in code, the §H floor) · accessibility basics · anything
the user explicitly asked for. The user wants the full version → build it, no re-arguing.
Hardware/real-world tuning knobs (a clock drifts, a sensor reads off) stay — the physical
world needs calibration a minimal model can't see.

## Mark deliberate simplifications
Leave a one-line marker so a shortcut reads as intent, not ignorance — and name the
ceiling + upgrade path for a known-limited shortcut:

```python
# ponytail: global lock — switch to per-account locks if throughput matters
# ponytail: O(n^2) scan; fine at n<1k, index it if the list grows
```

## Leave one check behind
Minimal code without its check is unfinished. Non-trivial logic (a branch, a loop, a
parser, a money/security path) leaves ONE runnable check — the smallest thing that fails
if the logic breaks: an `assert`-based `demo()`/`__main__` self-check, or one tiny
`test_*.py`. No frameworks, no fixtures unless asked. Trivial one-liners need no test —
YAGNI applies to tests too. (This is the `tdd-engineer` discipline at minimal dose.)

## Output discipline
Code first. Then at most three short lines: what was skipped, when to add it.
Pattern: `[code] → skipped: <X>, add when <Y>.` If the explanation is longer than the
code, delete the explanation — every paragraph defending a simplification is complexity
smuggled back as prose. (A report/walkthrough the user *asked* for is not debt — give it
in full; the rule is only against unrequested prose. Refines §I/§P.)

## How it stacks with the kit
- **§D (reuse ladder)** = SEARCH → REUSE/PATCH/CREATE. Ponytail rungs 2–4 are the same
  reflex one level earlier: prefer stdlib/native/installed before you even decide to create.
- **§K (code discipline)** caps function length / params / dead code — ponytail removes the
  function entirely when it shouldn't exist.
- **§C (GSD)** still runs. Ponytail keeps the OUTPUT minimal while the THINKING stays
  maximal (§O high/xhigh) — think hard, write little.

The shortest path to done is the right path.
