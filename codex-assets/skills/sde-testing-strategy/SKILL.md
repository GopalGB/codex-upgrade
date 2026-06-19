---
name: sde-testing-strategy
description: >-
  Build the test pyramid - fast unit, focused integration, few e2e - plus TDD red-green-refactor and what to mock at boundaries.
---

# sde-testing-strategy

Aim for the **test pyramid**: many fast unit tests (milliseconds, no I/O), fewer integration tests (real DB/queue, slower), a thin layer of e2e (full stack through the UI/API, slowest and flakiest). Inverting it into an ice-cream cone (mostly e2e) gives slow, brittle suites. **Test behavior, not implementation** - tests should survive refactors; one logical assertion per test; descriptive names (`should_reject_expired_token`). **Mock only at boundaries**: network, DB, filesystem, clock, randomness - never mock the unit under test, and prefer **fakes** (in-memory implementations) over heavily-stubbed mocks because mocks couple tests to call sequences. Assert on outputs and observable state, not on 'mock was called twice'. **TDD loop**: red (write a failing test for the next behavior) -> green (simplest code to pass) -> refactor (clean up with tests as a safety net). It forces testable design and documents intent. **Coverage** is a floor (e.g., 80% on new code) not a goal - 100% coverage of trivial getters proves nothing. **Pitfall**: tests that pass even when the code under test is deleted (tautological), and flaky e2e tests 'fixed' by bumping timeouts instead of removing the nondeterminism.

**Tools:** test pyramid, unit/integration/e2e, TDD, mocks vs fakes, coverage
