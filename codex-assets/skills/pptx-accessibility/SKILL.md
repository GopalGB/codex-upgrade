---
name: pptx-accessibility
description: >-
  Make decks accessible: alt text on images/charts, correct reading order, color contrast, table headers, meaningful link text, and the built-in Accessibility Checker
---

# pptx-accessibility

Run Review > Check Accessibility — it flags missing alt text, low contrast, reading-order issues, and tables without headers, with one-click fixes. Alt text: right-click image/chart/SmartArt > View Alt Text; describe meaning ('Revenue up 22% QoQ'), not appearance; mark purely decorative items as decorative. Reading order: a screen reader reads shapes in z-order shown in the Selection Pane (Home > Arrange > Selection Pane) — reorder so Title reads first, then content top-to-bottom; the Accessibility ribbon has a dedicated Reading Order pane. Contrast: body text needs 4.5:1 against its background (3:1 for large text) per WCAG 2.2 AA — don't rely on color alone to convey meaning (add labels/patterns to charts). Tables: set a header row (Table Design > Header Row) so structure is announced. Use descriptive hyperlink text ('Q3 report'), never 'click here'. Unique slide titles aid navigation — if a title must be hidden visually, move it off-canvas rather than deleting (or use the title placeholder collapsed). In python-pptx, set a picture's alt via the shape's element (`descr` on the cNvPr). Export PDF with 'Document structure tags' on to preserve all of this.

**Tools:** Review > Check Accessibility; Selection Pane (reading order); Alt Text pane; WCAG contrast 4.5:1
