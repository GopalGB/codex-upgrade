---
name: pptx-vba-automation
description: >-
  Automate PowerPoint with VBA — batch-format slides, find/replace across a deck, export each slide, recolor shapes by theme, loop the object model (Slides/Shapes/TextRange)
---

# pptx-vba-automation

VBA is the in-app automation layer when python-pptx isn't available or you need the live Application object. Open with Alt+F11, Insert > Module. Core object model: `ActivePresentation.Slides` -> each `.Shapes` -> `.TextFrame.TextRange.Text` for text, `.Fill.ForeColor.ObjectThemeColor = msoThemeAccent1` for theme-aware recolor, `.Line`, `.Width/.Height/.Left/.Top` (in points). Common jobs: loop all slides to standardize fonts (`For Each sld In ActivePresentation.Slides: For Each shp In sld.Shapes: If shp.HasTextFrame Then shp.TextFrame.TextRange.Font.Name = "..."`); deck-wide find/replace via `TextRange.Replace`; export every slide as PNG with `sld.Export "C:\out\" & sld.SlideIndex & ".png", "PNG", 1920, 1080`; renumber/retitle; bulk-apply a layout. Save as .pptm to keep macros; sign or set Trust Center > Macro Settings for distribution. Expert moves: use `ActiveWindow.Selection` to act on what the user picked, and guard with `On Error Resume Next` only around known-skippable shapes (placeholders without text frames throw). Pitfall: Mac PowerPoint VBA support is partial (no FileDialog, limited APIs) — test on target OS. For headless/server batch generation prefer python-pptx; VBA shines for interactive, GUI-bound tasks.

**Tools:** VBA editor (Alt+F11); PowerPoint object model: Presentation.Slides, Shape.TextFrame.TextRange, Shape.Fill; .pptm macros
