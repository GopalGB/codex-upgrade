---
name: py-pro
description: >-
  Expert Python engineering discipline for production-grade code - structure,
  typing, testing, packaging, and the modern 2026 toolchain. Use when writing or
  refactoring Python beyond a throwaway script. Triggers: "python", "refactor
  this python", "write a python module", "add tests", "package this", "type hints".
---

# py-pro — production Python discipline (no MCP)

## Toolchain (2026 defaults)
- **Env/deps:** `uv` (10-100x faster than pip/poetry). Fallback: `python -m venv`
  + `pip`. In a locked-down office, the `codex_env` tools-venv pattern applies.
- **Format + lint:** `ruff format` and `ruff check --fix` (replaces black/isort/flake8).
- **Types:** `mypy --strict` or `pyright`. New code is fully typed.
- **Tests:** `pytest` + `pytest-asyncio`; `hypothesis` for property-based tests.
- **Data models:** `pydantic` v2 for validation; `dataclasses` for plain records.
- **HTTP:** `httpx` (async-ready) over `requests`. **Speed-critical data:** `polars`.

## Code rules
- Type every function signature; `from __future__ import annotations` at the top.
- Functions ≤ 40 lines, ≤ 3 positional params (use a dataclass/options object beyond).
- `pathlib.Path` over `os.path`. f-strings over `%`/`.format`.
- No bare `except:`; catch specific exceptions; never swallow errors silently.
- No mutable default args. No magic numbers — name them.
- Comments explain WHY (a constraint/workaround), never WHAT. Code says what.
- `logging` over `print` in anything that isn't a CLI's user-facing output.

## Structure
- One responsibility per module; `__init__.py` only re-exports.
- `src/` layout for packages; `pyproject.toml` is the single source of truth.
- Keep pure logic separate from I/O so it's unit-testable without mocks.

## Testing bar
- Test behavior, not implementation — tests survive refactors.
- One logical assertion per test; descriptive names (`test_rejects_expired_token`).
- Mock only at boundaries (network, disk, clock, randomness), never the unit.
- New code: ≥ 80% line / ≥ 75% branch coverage; fix or quarantine flaky tests.

## Before declaring done
`ruff format . && ruff check . && mypy --strict . && pytest -q` — paste the real
output. If a step fails, it isn't done.
