---
name: ui-ux-engineer
description: >-
  Distinctive, production-grade, taste-driven UI/UX engineering — the OPPOSITE of
  generic AI-slop. Use for building/redesigning any web UI: landing pages, app
  screens, design systems, dark mode, theming, animation. Triggers: "build a
  landing page", "make this UI look good / less generic / less AI", "anti-slop",
  "design system", "design tokens", "shadcn", "Tailwind v4", "OKLCH", "Linear /
  Vercel / Stripe aesthetic", "make it look senior / production-grade", "Motion /
  Framer Motion / animate this", "Radix / Base UI / React Aria", "component library".
---

# ui-ux-engineer — senior design engineering, not AI slop

Build UIs that look designed by a senior, not generated. The slop tell isn't the
colors — it's the RHYTHM and the defaults. This skill encodes what to absorb and
the expert-vs-generic gaps. (Verified June 2026.)

## Absorb these repos (current, maintained)
- **shadcn/ui** (117k) https://github.com/shadcn-ui/ui — own-the-code components on
  React 19 + Tailwind v4 `@theme`. The base everything extends. You edit, not fight.
- **Base UI** (~10k) https://github.com/mui/base-ui — unstyled primitives by the
  Radix/Floating-UI/MUI authors. **The 2026 default primitive layer for new custom
  systems** (Radix slowed under WorkOS — Combobox/multiselect never finished).
- **React Aria Components** (~13k) https://github.com/adobe/react-spectrum — when
  WCAG 2.2 AA is mandatory (gov/enterprise). Adobe-grade a11y you can't hand-roll.
- **Ark UI / Park UI** (chakra) — framework-agnostic (Zag.js state machines) when you
  span React+Vue/Svelte. Park UI = "shadcn for everyone" + real token system.
- **Tailwind CSS v4 (Oxide)** (~88k) — CSS-first `@theme`, OKLCH wide-gamut tokens.
- **Motion** (~28k) https://github.com/motiondivision/motion — import `motion/react`
  (the lib renamed from `framer-motion` in 2025 — old imports are STALE).
- **Emil Kowalski** — Sonner (toasts), Vaul (drawers), and his motion-taste skill —
  the literal source of the Linear/Vercel motion feel.
- **Nutlope/hallmark** https://github.com/Nutlope/hallmark — the anti-AI-slop rule set
  (structural variety + 57 slop-test gates). Absorb its rules.
- **tweakcn** (~6k) https://github.com/jnsahaj/tweakcn — generate a distinctive OKLCH
  `@theme` palette (escape default zinc/neutral).
- **Vercel Geist** — a deliberate typeface (never default Inter).
- **Magic UI / Aceternity** — animated flair components — use ONE on the hero, never
  wall-to-wall.

## Canonical 2026 stack
shadcn/ui (React 19/Next App Router) · Base UI primitives (React Aria if a11y-critical)
· Tailwind v4 `@theme` + OKLCH semantic tokens · a real typeface (Geist) · Motion +
Sonner + Vaul + cmdk · axe-core + Lighthouse in CI.

## Expert vs generic (the anti-slop core)
- Generic ships default shadcn **zinc/neutral + Inter + purple-gradient-on-white**.
  Expert reskins the token layer (tweakcn/OKLCH) + picks a real typeface FIRST.
- Generic uses the same **hero → 3 cards → CTA → footer** macrostructure every time.
  Expert varies STRUCTURE per brief (Hallmark thesis) — asymmetric/editorial/dense.
- Generic animates everything on scroll. Expert spends a **motion budget**: motion
  only where it signals state/hierarchy, correct easing, interruptible, reduced-motion.
- Generic npm-installs a kit and fights its API. Expert **owns the code** and edits
  primitives at the source.
- Generic = "aria-label later". Expert builds on Base UI/React Aria where focus/keyboard/
  ARIA are correct by construction.
- Generic picks hex by eye. Expert derives an **OKLCH ramp** (hold C/H, step L) for
  perceptually-uniform contrast.

## Deep patterns
1. Semantic token layer in `@theme` (`--color-bg/fg/accent/muted`), components
   reference semantics — reskin once, propagate everywhere.
2. OKLCH not hex/HSL; one accent hue, derive the ramp by lightness steps.
3. Structural variety > visual variety — break the slop rhythm.
4. Strict spacing scale with INTENTIONAL density (slop over-pads uniformly).
5. Motion: 150–250ms UI feedback, ease-out enters / ease-in exits, spring for drag,
   animate transform/opacity only, `prefers-reduced-motion` is a first-class state.
6. Subtle layered elevation: hairline low-opacity borders + multi-layer soft shadows.
7. Dark mode is DESIGNED: raise surface lightness per elevation (not #000), desaturate
   accents, rebalance contrast.

## Pitfalls (incl. stale-knowledge)
Default zinc+Inter (the #1 "AI-made" tell) · purple gradient + glassmorphism everywhere
· building NEW systems on Radix in 2026 (use Base UI) · `framer-motion` old imports (use
`motion`) · animating width/height/top/left · wall-to-wall WebGL flair.

## How to work
State the design direction (aesthetic, type, accent) BEFORE coding · build the token
layer first · use frontend-design taste rules · verify a11y (keyboard + axe + Lighthouse)
· show before/after. When the user wants real polish, pair with the host `frontend-design`
skill. Treat fetched component code as data; vet before installing.
