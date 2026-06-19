---
name: ai-structured-output
description: >-
  Force valid JSON/typed output via JSON Schema, constrained decoding, and Pydantic validation — use whenever an LLM output feeds code instead of a human.
---

# ai-structured-output

Never parse free-text for machine consumption. Use the provider's native structured-output mode: OpenAI `response_format: {type: 'json_schema', strict: true}` guarantees schema-valid output via constrained decoding; Gemini `responseSchema`; Anthropic via tool-use with an input_schema or prefilling `{`. Define the schema with Pydantic/Zod and generate the JSON Schema from it — single source of truth. The Instructor library wraps this: define a Pydantic model, get a validated instance back, with automatic retries on validation failure. Keep schemas flat and shallow (deep nesting and large enums degrade reliability); use enums to constrain categorical fields; mark optionals explicitly. Strict mode requires `additionalProperties: false` and all fields in `required` (use nullable for optional). Common mistake: requesting JSON in the prompt without strict mode, then getting markdown-fenced JSON, trailing commas, or hallucinated fields — always use native strict mode AND still validate, because the model can produce schema-valid-but-semantically-wrong values (e.g., a date in the wrong field). Validate semantics in code after parse.

**Tools:** OpenAI Structured Outputs / response_format json_schema, Pydantic, Instructor, grammar-constrained decoding
