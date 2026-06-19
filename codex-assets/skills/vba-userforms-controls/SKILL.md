---
name: vba-userforms-controls
description: >-
  Build UserForms with TextBox/ComboBox/ListBox/OptionButton/CheckBox/Frame, Initialize/Activate, Show modal vs modeless, validate input, populate ListBox.List 2-D, MultiPage tabs
---

# vba-userforms-controls

Design forms in the VBE (Insert > UserForm), drop controls from the Toolbox, set `Name` properties meaningfully (`txtCustomer`, `cboRegion`). Show with `UserForm1.Show` (modal — code halts until closed) or `.Show vbModeless` (code continues, form floats). Populate combos/lists in `UserForm_Initialize` (fires once on load) not `Activate` (fires every time it regains focus).

Expert moves: fill a ListBox in one shot with a 2-D array — `lstData.List = Range("A2:C50").Value` plus `lstData.ColumnCount = 3` and `ColumnWidths = "60;120;40"`; far faster than `.AddItem` in a loop. Read multiselect with `For i = 0 To lst.ListCount-1: If lst.Selected(i) Then ...`. Use `Frame` to group OptionButtons (mutual exclusion is per-container). `MultiPage` gives tabbed wizards. Validate in the OK button handler and `Cancel = True` in `QueryClose`/keep form open on bad input.

Pitfalls: closing with the X button doesn't run your OK code — handle `UserForm_QueryClose` and check `CloseMode = vbFormControlMenu`. `Unload Me` destroys state; `Me.Hide` preserves control values so the calling Sub can read them after `.Show`. Don't reference `UserForm1.txtX` after Unload — it silently reloads a fresh form. Bind events to control names; renaming a control orphans its event handlers.

**Tools:** UserForm, Show vbModeless, UserForm_Initialize, ListBox.List, ComboBox.AddItem, Me.Hide, Frame, MultiPage, SpinButton
