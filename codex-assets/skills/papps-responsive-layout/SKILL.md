---
name: papps-responsive-layout
description: >-
  Responsive canvas apps: disable fixed-aspect Size/Width, containers (horizontal/vertical/auto-layout), Parent-relative sizing, and breakpoints with App.Width.
---

# papps-responsive-layout

First turn OFF 'Scale to fit / Lock aspect ratio' in Settings > Display so the app uses real device size. Build with **containers**: a **vertical/horizontal container** auto-stacks children; an **auto-layout container** distributes them with Gap/Align/Justify and `FillPortions` (flex-grow) so children share space proportionally. Size children relative to their parent: `Width = Parent.Width`, `Height = Parent.Height - Header.Height`, never hardcoded pixels. Implement **breakpoints** with `App.Width`: e.g. `If(App.Width < App.SizeBreakpoints.Small, 1, 3)` for column counts, or toggle a container's `Wrap`/`Direction`. `App.SizeBreakpoints` (Small/Medium/Large/ExtraLarge) is the built-in responsive scale. Pitfalls: mixing absolute X/Y positioning with containers (containers ignore X/Y and lay out by order — set order, not coordinates); nesting many containers deeply (perf + hard to debug); forgetting that controls inside an auto-layout container can't be free-positioned; designing only for desktop then the mobile player squishes it. Test with the device preview and resize. Modern apps lean heavily on auto-layout containers for a true flex model.

**Tools:** Containers, horizontal/vertical/auto-layout container, Parent.Width, App.Width/Height, Size, Fill portions
