---
name: papps-theming
description: >-
  Theming canvas apps: central color/font tokens via named formulas/App.Theme, applying to controls, modern controls + theme JSON, and consistency at scale.
---

# papps-theming

Centralize design tokens instead of hardcoding colors per control. Define a theme record in **App.Formulas** (named formulas): e.g. `AppTheme = { Primary: ColorValue("#0F6CBD"), Surface: RGBA(255,255,255,1), Font: Font.'Segoe UI', Radius: 8 }`, then set control properties to `AppTheme.Primary` everywhere — change one place, retheme the app. (Named formulas beat OnStart `Set` here: live, lazy, no startup cost.) **Modern controls** (the newer Fluent-based control set) support a built-in **theme** you can switch/define via theme JSON for Fluent design tokens and dark mode, giving consistent platform styling with less manual property-setting. For multi-app consistency, put themed components (buttons, headers, cards) in a **Component Library** so the tokens and styles propagate org-wide. Use `ColorValue("#RRGGBB")` or `ColorFade(base, 0.2)` for hover/disabled variants. Pitfalls: hardcoding hex on dozens of controls (a rebrand becomes a slog); mixing classic and modern controls so themes don't apply uniformly; forgetting hover/pressed/disabled state colors (DisabledFill, PressedFill) so the theme looks half-applied; relying on OnStart-set theme vars that delay launch — use named formulas.

**Tools:** Named formulas, App.Theme, modern controls, theme JSON, RGBA/ColorValue, Component Library
