---
name: pptx-smartart-diagrams
description: >-
  Use SmartArt for process/cycle/hierarchy/relationship diagrams, convert bullet lists to SmartArt, and know when to hand-build shapes instead
---

# pptx-smartart-diagrams

SmartArt turns structured text into diagrams that auto-layout and recolor with the theme. Fast path: select a bullet list, Home > Convert to SmartArt (right-click placeholder > Convert). Pick by relationship type: Process (sequential steps/arrows), Cycle (loop), Hierarchy (org chart), Relationship (overlap/balance), Matrix, Pyramid. Edit via the Text Pane (left arrow on the frame) — promote/demote with Tab/Shift-Tab to control nesting. Recolor with SmartArt Design > Change Colors (theme-driven). Expert move: once the structure is right, SmartArt Design > Convert > Convert to Shapes to break it into editable shapes for precise tweaks PowerPoint's auto-layout won't allow — but you lose auto-reflow, so do it last. Pitfall: SmartArt tempts overuse — for a clean 3-step process, three rectangles + chevrons you control look more bespoke than the canned 'Chevron List'. Org charts beyond ~20 boxes get cramped; consider a dedicated layout or split across slides. python-pptx cannot create SmartArt (it's complex DrawingML); build diagrams there with shapes + connectors instead.

**Tools:** Insert > SmartArt; Convert to SmartArt; SmartArt Design > Convert to Shapes; SmartArt Tools
