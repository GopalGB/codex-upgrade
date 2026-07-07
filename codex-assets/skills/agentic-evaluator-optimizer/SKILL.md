---
name: agentic-evaluator-optimizer
description: >-
  Loop a generator and an evaluator — one LLM produces a result, a second critiques it against explicit criteria, and the first revises until it passes or a cap is hit. Use when you have clear quality criteria and iterative refinement measurably helps: translation, code that must pass tests, writing to a rubric, search that must meet a bar.
---

# agentic-evaluator-optimizer

This pattern pairs a **generator** with an **evaluator** in a feedback loop: generate a candidate, have a separate evaluation step judge it against explicit criteria and return actionable feedback, then regenerate using that feedback — repeat until it passes or you hit a max-iterations cap. It mirrors how a human drafts, gets review notes, and revises. It works when two conditions hold: you can articulate **clear evaluation criteria**, and **iteration demonstrably improves** the output (the first draft is rarely the best).

The leverage is in the **evaluator**. Give it a concrete rubric or, better, a *ground-truth check* — run the tests, validate against a schema, diff against expected, or score on named dimensions — so its verdict is grounded rather than vibes. Have it return *specific, fixable* feedback ("missing error handling on the null case", not "make it better"); the generator can only act on concrete notes. Separating generator from evaluator matters: a fresh critical pass catches what the producing context rationalized away.

Always bound the loop — a max iteration count and a clear pass condition — or it can oscillate or run forever; if it isn't converging after a few rounds, stop and surface the best attempt plus the remaining gaps rather than burning tokens. Use real signals where you can (compiler/tests/validators beat an LLM judge); reserve the LLM evaluator for fuzzy criteria where no deterministic check exists. Don't use this when the criteria are vague or one-shot is already good enough — the loop is pure overhead then.

**Tools:** generate → evaluate vs criteria → refine · ground the evaluator (tests/schema/rubric) · specific actionable feedback · separate evaluator from generator · bound iterations + pass condition · prefer deterministic checks over LLM-judge
