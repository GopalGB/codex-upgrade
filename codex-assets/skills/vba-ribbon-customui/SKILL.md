---
name: vba-ribbon-customui
description: >-
  Customize the Ribbon with customUI XML — Custom UI Editor, onAction callbacks, dynamic controls (getEnabled/getVisible/getImage), invalidate to refresh, getCustomUI for COM add-ins
---

# vba-ribbon-customui

Ribbon tabs/buttons are defined in **customUI XML** embedded in the workbook/add-in (use the free Office RibbonX / Custom UI Editor to inject `customUI14.xml` for 2010+). Declare a tab, group, and `<button id="btn1" label="Run" onAction="OnRunClick" imageMso="FileSave"/>`. The `onAction` names a public VBA callback with the required signature `Sub OnRunClick(control As IRibbonControl)`. Use built-in icons via `imageMso` names (there are galleries of them).

Expert moves: for **dynamic** controls, use callbacks — `getEnabled="GetEnabled"`, `getVisible`, `getLabel`, `getImage` — each a callback that returns the state via a `ByRef returnedVal`. Capture the ribbon object in `onLoad="RibbonLoaded"` storing `IRibbonUI` in a module variable, then call `myRibbon.Invalidate` (or `InvalidateControl id`) to force Excel to re-query your getCallbacks and refresh the UI after state changes. Custom images load via `getImage` returning an `IPictureDisp`.

Pitfalls: a typo or wrong callback **signature** makes Excel silently ignore the control (no error) — match signatures exactly. Excel caches the ribbon; you can't repaint a single button without `Invalidate`. The stored `IRibbonUI` is lost if the project resets (an unhandled error/Stop), after which `Invalidate` errors — re-acquire via `onLoad`. customUI14 vs customUI (2007) namespaces differ. Macro-free `.xlsx` can't host callbacks; use `.xlsm`/`.xlam`.

**Tools:** customUI14.xml, Custom UI Editor, onAction callback, getEnabled, getVisible, IRibbonUI, ribbon.Invalidate, RibbonX, imageMso
