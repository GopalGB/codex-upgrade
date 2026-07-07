---
name: craft-tdd-red-green
description: >-
  Drive code with the RED-GREEN-REFACTOR test-first loop — write the failing test first, watch it fail for the right reason, write the minimum code to pass, then refactor under green. Use when building or fixing logic that can be tested; treat tests written after the implementation as grounds to delete and redo.
---

# craft-tdd-red-green

Write the test **before** the implementation. The loop is three strict beats: **RED** — write one small failing test that pins the next behavior; run it; confirm it fails *for the reason you expect* (a test that passes immediately or errors for the wrong reason proves nothing). **GREEN** — write the least code that makes it pass, even if ugly; run the suite green. **REFACTOR** — now improve names/structure with the test as your safety net; stay green the whole time.

One behavior per cycle, smallest step that moves forward. Don't write five tests then five implementations — interleave. Don't add code no test demands (that's untested code pretending to be done). If you wrote the implementation first and bolted tests on after, you can't trust them — they were written to match what the code *does*, not what it *should* do; delete and re-drive from RED.

Test behavior and contracts, not private internals; assert on observable outputs and side effects so refactors don't break the tests. Keep tests fast and isolated (mock at boundaries — network, clock, filesystem — not core logic). A bug fix is a RED test that reproduces the bug *first*, then the fix that turns it green — that test is now a permanent regression guard.

**Tools:** RED→GREEN→REFACTOR · one behavior per cycle · watch-it-fail-first · minimal-code-to-pass · bug = failing-test-first · test contracts not internals
