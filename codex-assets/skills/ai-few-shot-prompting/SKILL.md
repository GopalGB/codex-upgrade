---
name: ai-few-shot-prompting
description: >-
  Steer format and behavior with in-context examples (k-shot) when zero-shot is inconsistent — covers example selection, ordering, and label balance to avoid majority-label bias.
---

# ai-few-shot-prompting

Add 2-8 input→output examples in-context to teach format and edge-case handling without fine-tuning. Few-shot wins when the task has a specific output shape (extraction, classification, style) that's hard to describe but easy to demonstrate. Pick examples that COVER the distribution including hard/boundary cases, not just easy ones; for retrieval-augmented few-shot, select examples by embedding similarity to the query (dynamic k-shot) — this beats fixed examples on diverse inputs. Order matters: models exhibit recency bias toward the last example, and for classification, imbalanced example labels induce majority-label bias — keep labels balanced and shuffle order. Format examples IDENTICALLY to how you want output (same delimiters, same field names). Diminishing returns past ~5-8 examples and you burn context/cost; if you need 20+ examples, fine-tune instead. Common mistake: examples that leak the answer pattern (all 'yes' answers) or use a different format than the real task, teaching the model the wrong thing. Always include at least one negative/counter-example for classification.

**Tools:** k-shot, example selection by embedding similarity, label balancing
