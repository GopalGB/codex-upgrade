---
name: craft-no-hallucinated-apis
description: >-
  Never invent functions, methods, flags, config keys, or packages — verify every symbol and dependency actually exists in the installed version before using it. Use whenever writing code against any library, API, or CLI; confabulated APIs that look plausible are the single most common LLM coding failure.
---

# craft-no-hallucinated-apis

LLMs confidently invent APIs that *look* right but don't exist — a method with the perfect name, a CLI flag that should be there, a config key from a different version. Before you call any non-trivial symbol, **confirm it exists**: grep the installed source, read the actual docs for the pinned version, check `--help`, or open the package in `node_modules`/site-packages. Plausibility is not existence.

Pin to reality, not memory. Check the *installed* version (`pip show`, `npm ls`, lockfile) — APIs move between majors, and your training memory may describe a version this project doesn't use. Don't add a new dependency to get a function the standard library or an already-installed package provides, and never import a package that isn't in the manifest without flagging it.

When you're not sure a symbol exists, treat that as a blocker to resolve, not a guess to ship: look it up. If you truly can't verify (no network, no source), say "I believe X exists but couldn't confirm against this version" rather than presenting it as fact. The cost of checking is seconds; the cost of a hallucinated API is a broken build and lost trust.

**Tools:** verify-the-symbol-exists · read docs for the installed version · grep the actual source · check the lockfile · don't invent flags/keys/packages
