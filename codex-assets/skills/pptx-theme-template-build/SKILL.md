---
name: pptx-theme-template-build
description: >-
  Author a reusable .thmx/.potx theme: theme colors (12-slot), theme fonts, effects, and ship a branded template that propagates everywhere
---

# pptx-theme-template-build

A theme is the color/font/effect engine behind every template. In Slide Master, set Colors > Customize Colors to define the 12 theme slots: 4 Text/Background (dk1/lt1/dk2/lt2), 6 Accents (1-6), Hyperlink, Followed Hyperlink. Use theme slots everywhere — shapes that reference 'Accent 1' recolor automatically when the theme changes; hard-coded RGB does not. Set Fonts > Customize Fonts for a Heading + Body pair (this is the Office font scheme, surfaced as '+Heading'/'+Body'). Effects sets shadow/line/fill presets. Save As template: .potx keeps layouts+content placeholders for new decks; .thmx is theme-only for applying to existing decks via Design > Themes > Browse. Expert move: define tints/shades by relying on the accent + theme's automatic 'lighter/darker' variants rather than 10 separate colors — keeps the palette coherent. Pitfall: pasting content from another deck imports its theme as a second master ('Theme 2'); use Paste > Use Destination Theme or Keep Text Only. Store the .potx in a shared location and set it as default via the template gallery so File > New is on-brand.

**Tools:** Slide Master > Colors/Fonts/Background Styles; Save As .potx/.thmx; theme1.xml
