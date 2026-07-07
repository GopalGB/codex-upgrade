---
name: craft-verify-before-done
description: >-
  Never claim a change is done or 'should work' without actually running it — build it, run the tests, exercise the real code path, and read the output. Use before reporting any task complete; 'it compiles' and 'it looks right' are not evidence that it works.
---

# craft-verify-before-done

"Done" means **verified**, not "written". Before you report a task complete, actually run it: execute the build, run the test suite, hit the endpoint, call the function with real input, render the page. Then *read the output* — don't assume green; confirm it. The phrases "this should work", "it looks correct", and "it compiles, so it's fine" are predictions, not evidence, and they are how silent bugs ship.

Verify the *specific thing you changed*, end to end, through the path a user would take — not just the unit in isolation. If you fixed a bug, reproduce the original failure first, then show it's gone. If you added a feature, drive the actual feature, not a proxy. Capture the concrete signal (test summary, exit code, response body, screenshot) and let that be what you report.

When you genuinely *can't* run something (no network, missing creds, sandbox limit), say so explicitly and name exactly what remains unverified and how the user can check it — never paper over the gap with confident language. Honest "I couldn't run X; here's how to verify" beats a false "done".

**Tools:** run-it-don't-assume · read the actual output · exercise the real path end-to-end · reproduce-then-confirm-fixed · name what's unverified
