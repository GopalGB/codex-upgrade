---
name: pptx-embed-excel-objects
description: >-
  Embed vs link Excel ranges/objects, paste options (picture/keep-formatting/embed), live-updating linked charts, and managing/breaking links before sending
---

# pptx-embed-excel-objects

Three ways to put Excel on a slide, each a tradeoff. (1) Embed: Paste Special > Microsoft Excel Worksheet Object, or Insert > Object > Create from File (unchecked Link) — the workbook travels inside the .pptx, editable by double-click, but bloats file size and won't auto-update. (2) Link: same dialogs with 'Link' checked — slide shows live data from the source .xlsx and refreshes via File > Info > Edit Links to Files (or right-click > Update Link); breaks if the source moves/renames or the deck is emailed without the file. (3) Picture: Paste Special > Picture (Enhanced Metafile) — crisp, tiny, but static and not editable. For recurring reports, native embedded charts (separate skill) usually beat raw Excel objects. Before sending externally: File > Info > Edit Links to Files > Break Link to freeze data and avoid 'update links?' prompts and broken-reference errors on the recipient's machine — or Convert to a picture. Pitfall: a linked object pointing at a file on your local drive shows '#REF'/stale data for everyone else. The Paste Options popup (Ctrl after paste) lets you switch Keep Source Formatting vs Use Destination Theme vs Picture without redoing the paste.

**Tools:** Paste Special; Insert > Object; Data > Edit Links to Files; Paste Options icon; OLE objects
