---
name: ai-fine-tuning-decision
description: >-
  Decide IF and HOW to fine-tune (LoRA/QLoRA vs full vs prompt/RAG) and avoid the classic 'fine-tune when you should've RAG'd' mistake — use before committing to a training run.
---

# ai-fine-tuning-decision

First rule: fine-tuning teaches FORM/behavior (style, format, tone, a narrow skill), NOT facts — for facts/freshness use RAG. Ladder: prompt → few-shot → RAG → fine-tune, in that order; only fine-tune when prompting plateaus AND you have ≥hundreds-to-thousands of clean examples. Method by budget: LoRA freezes the base model and trains small low-rank adapter matrices (huge memory savings, swappable adapters); QLoRA quantizes the base to 4-bit (NF4) and trains LoRA on top — fine-tunes a 7-13B model on a single consumer/cloud GPU. Set rank r=8-64 (higher = more capacity/overfit risk), alpha ≈ 2r, target attention (q,k,v,o) and often MLP projections. SFT on input→output pairs first; add DPO/preference tuning to align toward preferred vs rejected outputs. Data quality dominates quantity — a few hundred excellent examples beat thousands of noisy ones. Hold out an eval set and watch for overfitting (train loss down, eval up) and catastrophic forgetting of general ability. Common mistake: fine-tuning to inject knowledge — it hallucinates confidently; RAG that instead.

**Tools:** LoRA, QLoRA (4-bit NF4), PEFT, rank/alpha, full fine-tune, SFT vs DPO/preference tuning
