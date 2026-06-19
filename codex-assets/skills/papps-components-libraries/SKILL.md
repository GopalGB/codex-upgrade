---
name: papps-components-libraries
description: >-
  Reusable components & component libraries: custom + behavior input/output properties, instance vs definition, and sharing across apps for consistency.
---

# papps-components-libraries

A **component** is a reusable control group with a typed interface: define **custom properties** — Input (data flows in, like a parameter), Output (data flows out, read via `Cmp.PropName`), and **behavior** Input properties (let the host pass in an OnX action the component invokes, e.g. an OnSelect callback). Inside the component reference its own props directly and use `Parent.Width`/`Self.Fill`. Components are isolated — they can't see the host's screen controls except through declared properties (this is the point: decoupling). A **Component Library** is the canonical store: build header/nav/cards/dialogs once, publish, then add to many apps; consuming apps get an **Update available** prompt to pull new versions. Use for design-system consistency across an org. Pitfalls: components historically could NOT directly access a data source/connector (pass data in via input property, or accept the dependency) — verify current capability before relying on it; not versioning the library (apps drift); putting screen-specific logic in a shared component (breaks reuse); circular property dependencies. For code-level reuse beyond components, PCF (Power Apps Component Framework) builds custom React controls.

**Tools:** Component, custom properties (input/output), behavior properties, Component Library, Self/Parent
