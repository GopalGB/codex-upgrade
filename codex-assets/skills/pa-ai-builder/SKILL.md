---
name: pa-ai-builder
description: >-
  AI Builder in flows: prebuilt + custom document processing, GPT prompts, extract/classify text, sentiment, and credit consumption
---

# pa-ai-builder

**AI Builder** adds AI actions to flows (premium / AI Builder credits). **Prebuilt models** need no training: **Extract information from documents** (invoices, receipts, IDs), **Recognize text (OCR)**, **Analyze sentiment**, **Detect language**, **Translate**, **Key phrase extraction**, **Category classification**. **Custom models** trained in AI Builder studio: **Document processing** (teach your invoice/form layout with 5+ samples + tagged fields, then extract returns your fields), **Category classification**, **Object detection**, **Entity extraction**, **Prediction** (binary outcome from Dataverse history). The modern **"Create text with GPT" / "Run a prompt"** action uses a **custom prompt** (input variables + grounding) to summarize, draft, extract structured JSON, or classify free text - reference outputs as dynamic content. Pattern: email-with-PDF -> Get attachment -> AI Builder extract -> create Dataverse/SharePoint row. Pitfalls: AI Builder consumes **credits** (per-page docs, per-call GPT) - high volume needs a capacity plan and you hit limits silently; custom doc models need consistent layouts + enough labeled samples; validate/confidence-check extracted values before writing to systems of record; GPT is non-deterministic - prompt for strict JSON and **Parse JSON** with error handling; PII/data-residency governance applies.

**Tools:** AI Builder, Extract information from documents, OCR, Analyze sentiment, custom document processing, Run a prompt / Create text with GPT, AI Builder credits
