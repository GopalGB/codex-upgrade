---
name: pptx-master-cleanup-footer
description: >-
  Clean a bloated deck: remove unused masters/layouts, fix multiple-theme drift, add slide numbers/date/footer correctly (skip on title), and standardize fonts
---

# pptx-master-cleanup-footer

Decks accumulate junk: copy-paste imports extra masters ('Theme 2','Theme 3'), orphan layouts, and mismatched fonts. Cleanup pass: View > Slide Master, right-click extra masters/layouts not in use > Delete (PowerPoint won't let you delete one that's applied — re-point those slides to your canonical layout first via Home > Layout). Standardize type with Home > Replace > Replace Fonts to swap a stray Calibri/Arial to the theme font globally. Footer/number/date: Insert > Header & Footer > check Slide Number, Date (fixed vs auto-update), and Footer text; check 'Don't show on title slide' so the cover stays clean; Apply to All. If numbers don't appear, the layout's placeholder was deleted — re-add it in Slide Master (Insert Placeholder > Slide Number) or it silently won't render. Run Home > Reset per slide to snap drifted placeholders back to layout geometry. Pitfall: hand-typing page numbers in text boxes — they don't renumber on reorder; always use the Slide Number field (Insert > Slide Number). Finish by File > Info > Check for Issues to strip hidden/off-slide content and personal metadata before delivery.

**Tools:** Slide Master view; Insert > Header & Footer; Replace Fonts; Reset; Remove Unused Master/Layouts
