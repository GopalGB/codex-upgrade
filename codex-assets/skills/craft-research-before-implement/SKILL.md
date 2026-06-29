---
name: craft-research-before-implement
description: >-
  For an unfamiliar library, API, framework, or subsystem, read the actual docs and source for the installed version before writing code against it — don't pattern-match from stale training memory. Use when working with anything you don't already know cold; minutes of research prevents hours of debugging confident-but-wrong code.
---

# craft-research-before-implement

When the task crosses into territory you don't know cold — a library you haven't used, an internal subsystem, a framework's lifecycle, a protocol's edge cases — **research first, code second**. Read the real docs for the *installed* version, skim the source or types, find one or two existing usages in this repo or upstream examples. Your training memory of an API is a snapshot that may be stale, partial, or from a different major version; the installed reality is the source of truth.

Spend the research where the risk is: the exact signature and return shape you'll call, the error/exception contract, version-specific behavior, threading/async constraints, and the failure modes the happy-path docs gloss over. Reading the *types* or the function body often answers in seconds what guessing would get wrong. Prefer primary sources (official docs, source, changelog) over half-remembered blog patterns.

This is the opposite of "start typing and fix the errors as they come" — that loop is slow and produces code shaped by compiler whack-a-mole rather than understanding. Front-load enough understanding to write it right the first time, then implement. When you can't research (no network/docs), say what you're unsure of and verify against the smallest possible runnable check before building on top of it.

**Tools:** read docs/source for the installed version · find existing usages · check signatures + error contracts + version behavior · primary sources over stale memory · understand-then-implement
