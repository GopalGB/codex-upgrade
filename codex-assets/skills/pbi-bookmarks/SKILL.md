---
name: pbi-bookmarks
description: >-
  Use bookmarks + selection pane + buttons to build navigation, toggles, show/hide states, and guided storytelling
---

# pbi-bookmarks

Bookmarks capture a report state: filters, slicer values, visual visibility, sort, drill level, and spotlight. Build interactive UX by combining the Selection pane (toggle visibility of each visual/group) with bookmarks: hide a panel, capture a bookmark; show it, capture another; wire buttons (Insert > Buttons) with Action = Bookmark to flip between them. Common patterns: a chart/table view toggle, a slicer flyout panel, a 'reset filters' button (bookmark capturing default slicers with 'Data' enabled), and storytelling page-by-page. When capturing, control scope precisely: in the bookmark's '...' menu choose Data (filters/slicers), Display (visibility/spotlight), Current page, and 'Selected visuals' so a bookmark only affects intended elements. Group related bookmarks for a Bookmark navigator (Insert > Buttons > Navigator > Bookmark navigator) which auto-builds buttons. Pitfall #1: a bookmark with 'Data' on will overwrite users' own slicer choices — for pure show/hide toggles uncheck Data. Pitfall #2: forgetting 'Selected visuals' makes one toggle bookmark reset unrelated visuals. Pitfall #3: adding a visual after creating bookmarks means it's not in their visibility state — update each bookmark. Pitfall #4: buttons need the right Action type; a Bookmark action with no bookmark selected does nothing. Use Bookmark/Page navigators over manual buttons for maintainability.

**Tools:** Bookmarks pane, Selection pane, buttons, actions, bookmark groups
