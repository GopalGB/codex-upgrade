---
name: pptx-slide-size-export
description: >-
  Set slide size/aspect ratio (16:9 vs 4:3 vs custom A4), and export to PDF, high-res images, handouts, and MP4 video with the right settings
---

# pptx-slide-size-export

Set aspect BEFORE designing: Design > Slide Size > Widescreen 16:9 (default, 13.333"x7.5") for screens/projectors, 4:3 only for legacy hardware, or Custom for print (A4/Letter, posters). Resizing late distorts placement — PowerPoint asks Maximize vs Ensure Fit; neither is perfect, so choose early. Export PDF: File > Export > Create PDF/XPS, Options > choose 'Slides' vs 'Notes pages' vs 'Handouts (N per page)', and enable 'Document structure tags for accessibility' + 'Create bookmarks using Sections'. High-res images: File > Export > Change File Type > PNG, 'All Slides' (registry/Save As can push DPI past the default ~96-150). Video: File > Export > Create a Video — pick resolution (Full HD 1080p), set 'Use Recorded Timings and Narrations' or a fixed seconds-per-slide, then it renders MP4 (transitions/animations bake in; Morph survives). Handouts to Word: Export > Create Handouts for editable notes layout. In python-pptx set `prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)`. Pitfall: video export of heavy animations is slow and large — preview one slide first.

**Tools:** Design > Slide Size; File > Export (PDF/Video/Handouts); Create Handouts (to Word); python-pptx Inches for slide_width
