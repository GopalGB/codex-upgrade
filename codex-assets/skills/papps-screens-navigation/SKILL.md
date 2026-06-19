---
name: papps-screens-navigation
description: >-
  Screens & navigation: Navigate transitions, Back, passing context, Param() deep links, OnVisible/OnHidden, and the single-screen anti-pattern.
---

# papps-screens-navigation

Move between screens with `Navigate(TargetScreen, ScreenTransition.Cover, {locPassed: value})` — the optional record sets context variables on the target. `Back()` returns to the prior screen (and reverses the transition). Pass data by context record (above), by global variable, or by selecting a record before navigating (`Set(gblSel, Gallery.Selected); Navigate(Detail)`). Use `Screen.OnVisible` to load/refresh data each time a screen opens (good place to ClearCollect the screen's data) and `OnHidden` to clean up. **Deep links / launch params**: read `Param("recordid")` (from a URL `&recordid=...` or `Launch()`) in App.OnStart/Screen.OnVisible to open a specific record. `Exit()` closes the app; `Launch()` opens URLs or other apps. Pitfalls: cramming everything onto one screen with Visible toggles 'to avoid navigation' — it loads all controls/data at once and tanks startup (use real screens, they load lazily); heavy data loads in OnVisible firing on every revisit (cache and guard with a flag); relying on Back() after a Navigate chain that branched (the stack may not go where you expect — use explicit Navigate).

**Tools:** Navigate, Back, Screen.OnVisible, Param, Exit, transition effects
