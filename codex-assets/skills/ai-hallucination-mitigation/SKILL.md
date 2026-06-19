---
name: ai-hallucination-mitigation
description: >-
  Reduce confident fabrication: grounding/RAG, citation enforcement, abstention thresholds, chain-of-verification, and self-consistency — use for any factual or high-stakes output.
---

# ai-hallucination-mitigation

Hallucination = the model asserting unverifiable facts. Defense stack: (1) GROUND — give the facts in-context (RAG) and instruct 'answer only from the provided context; if it's not there, say you don't know.' (2) CITE — require inline citations to source spans (Anthropic Citations API ties claims to document locations); unciteable claims get dropped. (3) ABSTAIN — set a confidence gate: below threshold, return 'I don't have enough information' — abstention beats a confident wrong answer in high-stakes settings. (4) VERIFY — Chain-of-Verification: draft → generate independent check questions → answer them in a FRESH context (draft not visible) → revise, removing unsupported claims (50-70% reduction on factual QA). (5) SELF-CONSISTENCY — sample n times; claims that don't recur across samples are suspect. Note: temperature=0 does NOT meaningfully reduce hallucination — it's a myth. Common mistake: asking the model 'are you sure?' (it just agrees) instead of independent verification, and trusting fluency as a confidence signal — fluency and correctness are uncorrelated. Log every claim's source for audit.

**Tools:** RAG grounding, Citations API, CoVe (chain-of-verification), abstention/IDK, self-consistency, confidence calibration
