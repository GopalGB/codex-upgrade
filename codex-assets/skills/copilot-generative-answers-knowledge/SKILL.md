---
name: copilot-generative-answers-knowledge
description: >-
  Ground an agent on enterprise data with generative answers over SharePoint, Dataverse, files, public websites, and connectors; fix 'no answer found' grounding gaps.
---

# copilot-generative-answers-knowledge

Generative answers = RAG over your knowledge sources. Add sources on the **Knowledge** tab: **SharePoint** (URL to a site/library; honors user permissions via Graph), **Dataverse** (structured tables - best for business records), **File upload** (PDFs/Office docs up to source limits), **Public website** (Bing-indexed URLs, max ~25 per source set), **Documents in OneDrive/SharePoint**, and **custom connectors / Microsoft Copilot connectors (Graph connectors)**. Drop a **Generative answers** node inside a topic to do an ad-hoc lookup over selected sources or specify a custom data source variable. For enterprise design, layer it: Dataverse for structured data, SharePoint for policy docs, a few curated web URLs only if required. A background **scheduled sync** reindexes SharePoint/OneDrive files automatically. Pitfalls: (1) SharePoint grounding respects the *signed-in user's* permissions, so unauthenticated/web channels return nothing - configure authentication. (2) Freshly added SharePoint sources take time to index - 'no answer' right after adding is normal. (3) Public-website answers need the URL to actually be Bing-indexed. (4) Cite sources: turn on in-text citations so users can verify.

**Tools:** Knowledge sources, Generative answers node, SharePoint/Dataverse/Website/File sources, semantic indexing
