---
name: ai-llm-evals
description: >-
  Build an offline eval harness for LLM systems: golden datasets, deterministic vs model-graded metrics, regression gates in CI — use before shipping any prompt/model change.
---

# ai-llm-evals

You can't improve what you don't measure — every prompt or model change needs a fixed eval set (20-200 representative cases with expected outputs/criteria) run before/after. Pick metrics by task: deterministic where possible (exact match, JSON-schema-valid rate, regex/assertion, F1 for extraction); model-graded (LLM-as-judge) for open-ended quality, faithfulness, and relevance; pairwise A/B comparison when absolute scoring is noisy. For RAG specifically, separate retrieval metrics (recall@k, MRR, context precision) from generation metrics (faithfulness/groundedness, answer relevancy) so you know which half broke. Tooling: promptfoo (config-driven, CI-friendly), Ragas (RAG metrics), DeepEval. Wire it into CI: gate merges if pass-rate drops >2% vs baseline. Build the golden set from REAL failures and edge cases, not happy-path toys — and grow it every time prod surfaces a new failure. Common mistake: vibes-based 'looks better' evaluation that silently regresses on cases you forgot — and judging on a tiny set where 1 flip = 5%. Version prompts and tie eval runs to versions.

**Tools:** golden set, exact-match/F1/BLEU, faithfulness/answer-relevancy, pairwise comparison, promptfoo/Ragas/DeepEval
