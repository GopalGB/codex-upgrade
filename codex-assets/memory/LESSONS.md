# Codex Lessons — mistakes to never repeat
> Read BOTH this file and the project `.planning/LESSONS.md` before non-trivial work (§C/§F).
> Append on any user-frustration signal (§F). Grep before adding — bump `hits:` and
> tighten `correct:` instead of duplicating. ONE entry = one mistake-class.
> Schema:
>   ### <TAG> — <one-line title>            (hits: N · since YYYY-MM-DD)
>   - trigger: <what the user said / the situation>
>   - mistake: <what was done wrong>
>   - correct: <imperative rule that prevents recurrence>
>   - scope:   global | project:<name>

### SILENT_DEGRADE — never return fake-looking results when a dep/key/tool is missing   (hits: 1 · since 2026-06-18)
- trigger: "this is shit, basic chatbot" / output that looked real but wasn't
- mistake: continued past a missing API key/dep/tool and produced plausible-but-empty output
- correct: on any missing key/dep/tool emit a NAMED BLOCKER with the exact command or signup URL — never degrade silently into something that looks like real results.
- scope:   global

### LITERAL_INPUT — preserve user identifiers verbatim   (hits: 1 · since 2026-06-18)
- trigger: user typed a specific model/version/date/URL/repo/flag/path
- mistake: "corrected" it to a familiar value from stale training priors (Gemma 4 → Gemma 3)
- correct: copy user-supplied identifiers character-for-character. Suspect a typo? ASK. Never silently substitute.
- scope:   global

### PATCH_DONT_REGENERATE — smallest change that fixes it   (hits: 1 · since 2026-06-18)
- trigger: "why did you rewrite the whole file" / "I only asked you to change X"
- mistake: regenerated a working file/section to dodge a failure instead of a targeted edit
- correct: patch by default. Rewrite a whole file ONLY if the user asked, or a patch is more fragile — and say which. Regenerating to dodge an undiagnosed failure is banned.
- scope:   global

### GROUND_FIRST — read/run/search before generating   (hits: 1 · since 2026-06-18)
- trigger: an answer that turned out wrong because it came from memory
- mistake: asserted from "I recall that…" without reading the file or running the command
- correct: read the file, run the command, or search before generating. Reuse a prior MEMORY/LESSONS answer if still valid; re-verify if stale. No memory-only facts.
- scope:   global

### CLOSED_LOOPS — VERIFIED-DONE or NAMED-BLOCKER, never vague   (hits: 1 · since 2026-06-18)
- trigger: "is this actually done?" / a "should work" that didn't
- mistake: ended a task with a vague claim and no proof
- correct: every task ends with the §J block — either VERIFIED-DONE (test output shown) or a NAMED BLOCKER (exact gap + next action). Never "should work".
- scope:   global

### NO_CONFIDENTLY_WRONG — abstain below ~70%   (hits: 1 · since 2026-06-18)
- trigger: a confident claim that was wrong
- mistake: shipped a low-confidence guess as if it were verified
- correct: tag claims HIGH/MEDIUM/LOW (§A). Below ~70%, abstain — state what you know and the ONE thing that would close the gap.
- scope:   global

### ASK_BEFORE_SCOPE — don't expand scope unasked   (hits: 1 · since 2026-06-18)
- trigger: "I never asked you to add/change that"
- mistake: added files, dependencies, or architecture the user didn't request
- correct: build exactly what was asked. New scope/files/deps/architecture → one sharp question first (§C clarity gate).
- scope:   global

### VERIFY_BEFORE_DONE — run the tests, read the output   (hits: 1 · since 2026-06-18)
- trigger: "you said it works but it doesn't"
- mistake: claimed success by assertion without running the build/tests
- correct: run the actual tests/build and READ the output before saying it works. Green-by-assertion is a lie (§C VERIFY).
- scope:   global
