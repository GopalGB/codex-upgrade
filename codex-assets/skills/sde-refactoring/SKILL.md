---
name: sde-refactoring
description: >-
  Improve code structure without changing behavior - small safe steps under test coverage, smell-driven, never mixed with features.
---

# sde-refactoring

Refactoring is changing structure while preserving behavior - so it MUST happen under a green test suite; if coverage is missing, write **characterization tests** first (capture current behavior, even if quirky) so you can detect regressions. Work in **small reversible steps**, running tests after each: extract method, extract class, rename for clarity, inline, replace conditional with polymorphism/strategy, introduce parameter object. Commit each step separately so rollback is one revert. **Drive it by code smells**: long method (>~40 lines), large class, long parameter list (>3 - use an options object), duplicated code, feature envy (a method using another object's data more than its own), shotgun surgery (one change touches many files), primitive obsession. **Never mix refactoring with feature work or bug fixes in the same commit/PR** - it makes review impossible and hides behavior changes among structural ones; do the refactor, ship/verify, then build the feature on the cleaner base (or vice versa). **Pitfall**: a 'refactor' that quietly changes behavior (the most dangerous kind), and big-bang rewrites - prefer the strangler pattern, incrementally replacing pieces behind a stable interface. Boy-scout rule: leave each touched file slightly cleaner.

**Tools:** extract method/class, rename, code smells, test harness, strangler, characterization tests
