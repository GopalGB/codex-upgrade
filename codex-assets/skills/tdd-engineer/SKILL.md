---
name: tdd-engineer
description: >-
  Test-driven development and test-craft discipline for a coding agent - red→green→refactor,
  what to test vs skip, fakes over mocks, property-based tests, characterization tests for
  legacy code, fast/slow tiers, coverage as tool not target, and per-language runners
  (pytest/vitest/jest/go/cargo). Use when adding tests, fixing a bug test-first, or making
  a change safe to refactor. Triggers: "add tests", "write a test", "TDD", "test-first",
  "red green refactor", "characterize this legacy code", "why is this test flaky", "mock vs fake".
---

# tdd-engineer — test-craft discipline (no MCP)

You are the test layer that plugs into the GSD **EXECUTE** step: *change → run THE exact
tests → red→green*. You do not write code and hope; you make the failure visible first, then
make it disappear. Tests are an executable spec, a regression net, and a refactor license — in
that order.

## The loop (non-negotiable)

1. **RED** — write the smallest failing test that states the next required behavior. Run it.
   *Watch it fail for the right reason.* A test you never saw fail proves nothing.
2. **GREEN** — write the least code that passes. Hardcode if that's smallest; the next test
   forces generality. Run the one test, then the file.
3. **REFACTOR** — clean code and tests with the bar green. Re-run after every move.

Commit at green, not at red. One behavior per cycle. If you can't name the failing test in a
sentence, the step is too big — split it.

## When to write the test FIRST vs after

- **Bug fix → always test-first.** Reproduce the bug as a failing test before touching code.
  That test is the fix's proof and its permanent regression guard. This is the agent's most
  valuable TDD habit — it converts "I think I fixed it" into "the suite says I fixed it."
- **New pure logic / parsing / state machines → test-first.** Cheap, high payoff.
- **Exploratory spike / unknown shape → code first, then lock with tests** before you keep it.
  Spikes are throwaway; a kept spike gets characterization tests (below) immediately.

## What to test — and what NOT to

Test **behavior through the public surface**: inputs → outputs/effects. Not private methods,
not implementation shape. A good test survives a rewrite of the internals.

Prioritize: branch points, boundaries (0, 1, n, empty, max), error paths, and the exact bug
you're fixing. Each test asserts **one logical behavior**.

Do **not** test: the language/stdlib, third-party libs you don't own, trivial getters,
generated code, or framework glue with no logic. Don't assert call-counts of a mock as a proxy
for behavior — that's testing the wiring, not the result.

## Test doubles — fakes > mocks

Mock only at boundaries: **HTTP, DB, filesystem, clock, randomness, network**. Never mock the
unit under test.

Order of preference:
1. **Real thing** if fast and deterministic (a temp dir, an in-memory SQLite).
2. **Fake** — a small working in-memory implementation of the interface. Survives refactors,
   exercises real logic. This is the default.
3. **Stub** — returns canned values, no assertions on it.
4. **Mock** — asserts interaction. Use sparingly; mock-heavy suites calcify and lie green.

Freeze the clock and seed randomness; never let wall-clock or RNG into an assertion.

```python
# Fake over mock: an in-memory repo, not a Mock(spec=Repo)
class FakeUserRepo:
    def __init__(self): self._rows = {}
    def save(self, u): self._rows[u.id] = u
    def get(self, uid): return self._rows.get(uid)
```

## Property-based testing (find cases you didn't imagine)

For pure functions with invariants (round-trips, idempotence, sort/encode/parse), assert the
*property* over generated inputs instead of a few hand-picked cases. Python: `hypothesis`
(`uv pip install hypothesis`). JS/TS: `fast-check` (`npm i -D fast-check`) (verify).

```python
from hypothesis import given, strategies as st
@given(st.lists(st.integers()))
def test_sort_is_idempotent(xs):
    assert sorted(sorted(xs)) == sorted(xs)
```

When a property test fails, it prints a **minimal** counterexample — paste that into a plain
unit test so the regression is pinned even if the generator changes.

## Characterization tests for legacy code (Feathers' technique)

Code with no tests that you must change safely: don't guess the spec — **pin current behavior**.
Write a test that asserts what the code *does now* (run it, copy the actual output into the
expected), get a green safety net, *then* refactor or fix under that net. Replace pinned
assertions with intended ones once you understand the behavior.

This is how you make untested code changeable without a rewrite. It's the agent's path through
"I can't touch this, there are no tests."

## Fast vs slow tiers (keep the inner loop sub-second)

- **Unit (default):** no I/O, no network, milliseconds. Run on every red→green cycle.
- **Integration:** real DB/filesystem/HTTP, seconds. Run before commit, not every cycle.
- **E2E:** full system, slow. Run in the verify gate, not the loop.

Mark slow tests so the fast loop excludes them — `@pytest.mark.slow` + run
`pytest -m "not slow"` while iterating. Tests must be independent and order-free; shared
mutable state is the #1 source of flake.

## Coverage is a tool, not a target

Coverage finds **untested lines**; it never proves they're tested *well*. 100% coverage with
zero meaningful assertions is worthless. Use it to spot gaps in changed code, then write
behavior tests for the risky branches. Never write a test purely to move the number. A test
that still passes when you delete the code under test is a fake test — delete it.

```bash
pytest --cov=src --cov-report=term-missing   # see the missing LINES, then judge
```

## Mutation testing (verify your tests actually bite)

When a suite *must* be trustworthy, run mutation testing: it perturbs the code and checks your
tests catch it. A "survived mutant" is a hole. Python: `mutmut` or `cosmic-ray` (verify).
Expensive — reserve for critical modules, not the whole repo.

## Runners — exact commands per language

**Python (lead — `pytest`):**
```bash
uv pip install pytest pytest-asyncio pytest-cov hypothesis   # if absent; never assume
pytest path/to/test_x.py::test_name -x -q     # one test, stop on first fail
pytest -m "not slow" -q                        # fast tier only
pytest --lf                                     # rerun last failures
```
- Async: mark with `@pytest.mark.asyncio` (needs `pytest-asyncio`).
- Files `test_*.py`; functions `test_*`; one assert-behavior each; use fixtures, not setup
  globals. `tmp_path` for filesystem, `monkeypatch` for env/clock.

**JS/TS (`vitest` preferred, `jest` legacy):**
```bash
npx vitest run path/to/x.test.ts -t "name"     # or: npx jest x.test.ts -t "name"
npx vitest                                      # watch mode for the loop
```
Mock at boundaries with `vi.fn()`/`vi.mock` (vitest) or `jest.fn()`. Same fakes>mocks rule.

**Go:** `go test ./... -run TestName -v` — table-driven tests are idiomatic; `t.Run` subtests
for cases. `go test -race` to catch data races.

**Rust:** `cargo test name` — `#[test]` funcs, `#[cfg(test)] mod tests`; doc-tests run too.

## Pitfalls that separate expert from generic

- **Green-without-red:** writing test + code together and never seeing the red. The test may
  assert nothing useful. Always run red first.
- **Testing the mock:** `assert mock.called_once()` instead of asserting the real effect.
- **Over-mocking:** mock so much that the test passes when the real integration is broken.
- **Flaky from time/order/RNG:** unfrozen clock, shared state, unseeded random. Quarantine and
  fix immediately — a flaky test trains the agent to ignore red.
- **One giant test:** asserts ten things; when it fails you can't tell which. Split.
- **Coverage theater:** tests with no assertions to hit a %.
- **Snapshot sprawl:** giant auto-updated snapshots that "pass" by re-recording garbage.

## Canonical tools (only what's confirmed)

`pytest`, `pytest-asyncio`, `pytest-cov`, `hypothesis` (Python) · `vitest`, `jest`,
`fast-check` (verify) (JS/TS) · `go test`, `cargo test` (built-in) · `testcontainers` for real
ephemeral DBs/services in integration tier · `mutmut`/`cosmic-ray` (verify) for mutation. In a
locked-down box: stdlib `unittest` always works; prefer it over installing nothing.

## Plugging into the kit

Hand the `claude-review` gate a suite that is green AND meaningful (it will probe weak
assertions). When self-healing retries a failed change, the *exact failing test name* is the
signal — keep test names behavior-descriptive (`should_reject_expired_token`, not `test_3`) so
the loop knows what broke. Done = the named acceptance test from the GSD plan is green, not "I
wrote some code."
