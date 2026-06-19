---
name: ai-multimodal-vision
description: >-
  Use vision LLMs for image understanding, OCR, document/chart extraction, and grounding: detail/resolution control, multi-image prompts, and structured extraction — use to read images, screenshots, or PDFs.
---

# ai-multimodal-vision

Vision-language models take interleaved image+text. For document/chart/screenshot extraction, pair vision with structured output: pass the image plus a JSON Schema and instruct 'extract these fields'; this beats classic OCR for layout-heavy docs (invoices, forms, tables) because the model reads semantics, not just glyphs. Control cost/quality with the detail/resolution param — 'low' for gist, 'high' for fine text/small UI; high-res images are tiled and cost more tokens, so downscale to the minimum legible resolution. For multi-image tasks, label each image in text ('Image 1 is the before, Image 2 the after') so references are unambiguous. Some models support grounding (bounding boxes / point coordinates) for 'where is X' — useful for UI agents. Pitfalls: vision models hallucinate text in blurry/low-res regions (always allow 'illegible' as a value and verify critical numbers), miscount dense objects, and struggle with rotated/handwritten text. For PDFs, prefer native PDF input (preserves text layer) over rasterizing when the model supports it. Common mistake: sending a full-res screenshot when a cropped region would be cheaper and more accurate.

**Tools:** GPT-4o/Claude/Gemini vision, image detail/resolution params, document extraction to JSON Schema, bounding-box grounding
