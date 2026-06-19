---
name: pptx-slide-master-layouts
description: >-
  Build and edit Slide Master + custom layouts (placeholders, inheritance) so every slide is on-grid; fix off-template slides and rogue text boxes
---

# pptx-slide-master-layouts

Open View > Slide Master: the top thumbnail is the Master (global), children are Layouts. Edit the Master once for org-wide fonts/logo/background; never restyle individual slides. Each layout exposes typed placeholders — Title (idx 0), Body/Content, Picture, plus inserted placeholders via Insert Placeholder. Expert move: build a small set of purpose layouts (Title, Section, 1-col, 2-col, Full-bleed image, Chart, Comparison) instead of dumping everything on 'Title and Content'. Placeholders inherit position/font from layout->master, so changing the master font cascades everywhere — that's the whole point. In python-pptx: `prs.slide_layouts[i]`, then `slide.placeholders[idx]` to fill by index (idx is stable, position in list isn't). Pitfall: text typed into a free text box (not a placeholder) won't appear in Outline view, won't reflow, and breaks Reset. If 'Reset' doesn't restore a slide, it's using a non-placeholder box — replace it. Use Home > Layout to re-point a slide at the correct layout; Home > Reset to snap placeholders back to layout-defined geometry. Delete unused layouts before shipping a template.

**Tools:** PowerPoint View > Slide Master; python-pptx slide_layouts, placeholders, idx
