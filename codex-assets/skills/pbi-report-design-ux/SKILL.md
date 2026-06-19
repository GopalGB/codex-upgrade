---
name: pbi-report-design-ux
description: >-
  Lay out reports for clarity and speed — grid alignment, visual hierarchy, theme JSON, consistent formatting, and fewer-faster visuals
---

# pbi-report-design-ux

Good report UX is layout discipline plus performance. Establish hierarchy: most important KPI top-left (Western reading path), supporting detail below/right; group related visuals with subtle backgrounds; align everything to a grid (View > Snap to grid / Gridlines, use the Format > General X/Y/Width/Height for pixel-exact placement). Enforce consistency with a custom theme JSON (View > Themes > Customize/Browse) defining colors, fonts, default visual padding/title styles — change it once, every visual updates, avoiding manual per-visual formatting drift. Limit each page to the visuals that answer one question; too many visuals slow rendering (each fires its own DAX query). Use sync slicers (View > Sync slicers) to share a slicer across pages without duplicating filter logic, and the filter pane for secondary filters to keep the canvas clean. Pitfall #1: 15+ visuals per page tanks load time — split into pages or use drillthrough/tooltips for detail. Pitfall #2: mixing fonts/number formats/colors looks amateur and confuses — drive all formatting from the theme. Pitfall #3: misaligned, differently-sized visuals signal low quality; snap to grid and match dimensions. Pitfall #4: ignoring accessibility — set tab order (Selection pane), alt text, and 4.5:1 contrast. Pitfall #5: huge background images and many custom visuals inflate file size and load — optimize assets and prefer core visuals.

**Tools:** theme JSON, grid/snap to grid, page layout, sync slicers, performance
