---
name: agentic-routing
description: >-
  Classify an input and dispatch it to a specialized prompt, model, or handler tuned for that category. Use when distinct kinds of input need different handling and lumping them into one prompt hurts quality — routing gives separation of concerns and lets you optimize each path independently.
---

# agentic-routing

Routing adds a **classification step** up front: an LLM (or a cheap classifier) labels the input, and code dispatches it to the handler built for that label. Customer queries → refund flow vs. technical-support flow vs. general-question flow; incoming docs → invoice parser vs. contract parser. The win is **separation of concerns**: each downstream prompt is specialized and stays simple, instead of one bloated prompt trying to cover every case and degrading on all of them.

Routing also enables **cost/quality tiering** — route easy/common inputs to a small fast model and only the hard ones to a large model, cutting cost without hurting the cases that need the big model. Keep the router itself narrow: its only job is an accurate label, so give it the category list, crisp definitions, and a few examples per class, and have it output a structured label you can switch on in code.

Design for the **unrouted case**: include an explicit "other/unsure" class with a sensible default handler rather than forcing every input into a bucket it doesn't fit. Validate the router's label against the allowed set before dispatching, and log misroutes to refine the categories. Use routing when inputs fall into distinct kinds that are better handled separately; if every input needs the same multi-step treatment, chain instead.

**Tools:** classify-then-dispatch · specialized handler per category · cost tiering (small model for easy, large for hard) · explicit "other/unsure" + default · structured label validated in code · log + refine misroutes
