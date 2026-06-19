---
name: vba-automate-office-apps
description: >-
  Drive Outlook/Word/PowerPoint from Excel via late vs early binding — CreateObject vs GetObject, send mail, mail-merge, build decks; release objects, avoid orphaned EXE processes
---

# vba-automate-office-apps

Cross-app automation uses COM. **Late binding** — `Set olApp = CreateObject("Outlook.Application")` — needs no reference, works across Office versions, but loses IntelliSense and named constants (you hardcode `1` instead of `olMailItem`). **Early binding** — add Tools > References > Microsoft Outlook xx.x Object Library, then `Dim olApp As Outlook.Application` — gives IntelliSense, compile-time checks, and enums. Develop early-bound, ship late-bound for version portability.

Expert moves: send mail — `Set mail = olApp.CreateItem(0)` (0 = olMailItem), set `.To/.Subject/.HTMLBody/.Attachments.Add path`, then `.Send` (silent) or `.Display` (let user review). Reuse an already-open app with `GetObject(, "Excel.Application")` (errors if none running — trap it). Word mail-merge: open the doc, `wdDoc.MailMerge.Execute`. PowerPoint: `pptApp.Presentations.Add`, `.Slides.AddSlide`, paste a chart as picture.

Pitfalls: the **orphaned process** trap — if you don't `Set olApp = Nothing` (and release every intermediate object you `Set`), the hidden EXE keeps running in Task Manager and locks files. Never qualify Office objects against the wrong app's default. `.Send` may trip Outlook security prompts (use a trusted setup or Redemption). Mixing early-bound code with a missing reference = compile error on other machines — that's why production code is often late-bound.

**Tools:** CreateObject, GetObject, Outlook.Application, Word.Application, PowerPoint.Application, MailItem, late binding, early binding, Set Nothing
