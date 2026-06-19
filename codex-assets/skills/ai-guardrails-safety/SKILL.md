---
name: ai-guardrails-safety
description: >-
  Add input/output guardrails to an LLM app: content moderation, PII redaction, topic/scope restriction, schema validation, and a fallback chain — use before exposing an LLM to users or untrusted input.
---

# ai-guardrails-safety

Wrap the model in two checkpoints. INPUT guardrails: moderation/classification to block disallowed content, prompt-injection screening, off-topic detection (keep a customer-support bot on-topic), and PII detection/redaction (Presidio) before logging or sending upstream. OUTPUT guardrails: re-run moderation on the generation, validate it against a schema/format, check for leaked secrets or PII, and verify it stays in scope. Tools: provider moderation endpoints, Llama Guard (open classifier for safe/unsafe categories), NeMo Guardrails (programmable rails with a flow DSL), Guardrails-AI / Pydantic validators for structure. Run cheap guardrails synchronously and expensive ones async where latency matters; fail CLOSED for safety-critical paths (block on uncertainty), fail-open only for low-stakes UX. Always have a graceful fallback message, never a stack trace. Common mistake: only guarding the output and forgetting input screening (so injected instructions reach the model), or hardcoding refusal strings the model can paraphrase around. Log every block with reason for tuning and audit.

**Tools:** moderation API, Llama Guard / NeMo Guardrails / Guardrails-AI, PII detection (Presidio), output validators, refusal/fallback
