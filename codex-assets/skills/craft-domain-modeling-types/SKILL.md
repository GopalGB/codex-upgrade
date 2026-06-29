---
name: craft-domain-modeling-types
description: >-
  Model the domain in the type system so illegal states are unrepresentable — parse input into precise types at the boundary, prefer enums/sum types over stringly-typed flags, and let the compiler enforce invariants. Use when designing data structures, function signatures, or APIs to push bugs from runtime to compile time.
---

# craft-domain-modeling-types

Make **illegal states unrepresentable**. If a value can only be one of three things, model it as an enum/sum type, not a string you hope is valid. If two fields can't both be set, encode that with a tagged union instead of a comment saying "don't set both". The compiler is a free, exhaustive test suite — give it enough type information to reject bad states before they run.

**Parse, don't validate**: at the system boundary, convert untyped input (JSON, form data, env vars) into precise domain types *once*, and pass those typed values inward. Then the core never re-checks "is this a valid email / non-empty / positive" because the type already guarantees it. A function that takes `UserId` and `NonEmptyList<Item>` can't be called wrong; one that takes `string` and `array` invites every caller to mishandle it.

Name types for the domain, not the primitive — `EmailAddress`, `Cents`, `OrderId`, not `string`, `number`, `string`. Make wrong units a type error (don't add `Cents` to `Dollars`). Use `Option`/nullable-by-design over sentinel values, and make required fields non-optional so "forgot to set it" doesn't compile. Reach for this when a bug class keeps recurring — often the real fix is a type that makes that bug impossible.

**Tools:** illegal-states-unrepresentable · parse-don't-validate at the boundary · enums/sum-types over stringly-typed · domain newtypes not primitives · let the compiler enforce invariants
