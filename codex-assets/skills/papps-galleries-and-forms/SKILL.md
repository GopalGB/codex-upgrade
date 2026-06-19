---
name: papps-galleries-and-forms
description: >-
  Galleries (Items, ThisItem, Selected, templates) and Edit/Display/View forms (DataSource, Item, Update, SubmitForm); when to use which.
---

# papps-galleries-and-forms

A **Gallery** repeats a template over `Items` (a table); inside the template reference the current row with `ThisItem.Field` and read the highlighted row elsewhere via `Gallery1.Selected.Field`. Set `Gallery1.Default` to preselect. Galleries are read/list surfaces; do not Patch from inside the template loop. A **Form** (Edit/Display) binds `DataSource` + `Item` (usually `Gallery1.Selected`), auto-generates DataCards per field, and writes back. The card's input lives in `DataCardValue`, the value sent to the source is the card's `Update` property — customize validation/format by editing `Update`, not the input. Submit with `SubmitForm(Form1)`; it respects `Required`/`DisplayMode` and triggers `OnSuccess`/`OnFailure`. Switch modes with `EditForm`, `NewForm`, `ViewForm`. Read submit results via `Form1.LastSubmit` (gets the new record incl. autonumber/ID). Pitfalls: building manual TextInputs + Patch when a Form gives validation/required/error UI for free; reading `DataCardValue` after switching to NewForm (it resets); forgetting `ResetForm` after a NewForm submit so the next entry starts clean.

**Tools:** Gallery, Edit/Display Form, ThisItem, Gallery.Selected, SubmitForm, EditForm/NewForm/ViewForm
