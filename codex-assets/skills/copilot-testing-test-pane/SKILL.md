---
name: copilot-testing-test-pane
description: >-
  Test an agent in the Test pane: trace topic/tool routing, inspect variable values, watch generative orchestration steps, and debug why a turn went wrong.
---

# copilot-testing-test-pane

Open the **Test your agent** pane (right side of the authoring canvas) - it refreshes with each save. Type utterances and watch which topic/tool the orchestrator selects. Turn on **'Track between topics'** (the toggle in the pane) to see the canvas highlight the exact nodes executing and redirects between topics in real time. In **generative** orchestration, expand the **activity / steps** view to see the orchestrator's plan: which knowledge it searched, which tools it called, and the inputs it auto-filled - this is how you debug 'why did it pick the wrong tool'. Inspect variable values mid-conversation to confirm slot filling worked. Pitfalls: (1) The Test pane uses *your* identity and permissions - SharePoint answers that work for you may fail for end users with less access; don't certify grounding from the Test pane alone. (2) Save before testing - the pane reflects authored (not published) state, so it can differ from what live users get if you haven't published. (3) Reset the conversation (the refresh icon) after changing variables/auth or you'll test against stale session state. (4) Test in the *actual channel* for rendering/auth issues the pane can't reproduce.

**Tools:** Test pane, 'Track between topics', activity map, variable inspection, orchestration step view
