---
name: papps-canvas-vs-model-driven
description: >-
  Choose canvas vs model-driven (vs custom pages): pixel UI on any connector vs Dataverse-metadata-driven apps; when each wins and the hybrid.
---

# papps-canvas-vs-model-driven

Canvas apps give pixel-level control and bind to 1000+ connectors (SharePoint, SQL, Excel, Dataverse); you place every control and write Power Fx for behavior. Model-driven apps are metadata/data-first: you define Dataverse tables, forms, views, and business rules, and the platform renders a responsive, accessible UI automatically — you cannot freely position controls. Pick canvas for task/process apps, bespoke layouts, mixed data sources, or mobile-first UX. Pick model-driven for complex relational data, role-based security (Dataverse security roles), dashboards, and CRUD-heavy line-of-business apps where consistency beats custom pixels. The 2026 hybrid: model-driven app + embedded **custom pages** (canvas surfaces inside a model-driven shell) to get bespoke screens where the metadata UI is too rigid. Pitfall: starting canvas on SharePoint then needing record security, auditing, or 50+ relationships — you'll rebuild on Dataverse. Decide the data backbone (Dataverse vs connector) first; the app type largely follows. Model-driven REQUIRES Dataverse; canvas does not. Licensing: model-driven and Dataverse-backed canvas need a Power Apps premium license, not just M365 seeded.

**Tools:** Power Apps Studio, model-driven app designer, custom pages, Dataverse
