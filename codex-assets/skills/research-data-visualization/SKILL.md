---
name: research-data-visualization
description: >-
  Build honest, clear research figures: chart choice by data type, error bars, axis integrity, color/accessibility, small multiples, publication-ready figures — use when presenting findings visually
---

# research-data-visualization

Choose the chart from the data + the message: distribution -> histogram/box/violin (violin shows shape a boxplot hides); comparison of groups -> bar with error bars or dot plot; relationship -> scatter (+ fit + CI band); trend over time -> line; part-to-whole -> stacked bar (avoid pie for > 3 slices). For group means, ALWAYS show uncertainty — and state whether the bars are SD, SE, or 95% CI (they imply very different things).

Protect axis integrity: start bar-chart y-axes at zero (truncation exaggerates differences); use a **log scale** only when the data span orders of magnitude, and label it. Reveal raw data when n is small (jittered points / strip plot over a bar). Use **small multiples** (faceting) instead of cramming many series onto one axis.

Make it accessible: colorblind-safe palettes (viridis, ColorBrewer), redundant encoding (shape + color), direct labels over legends where possible, sufficient font size. Maximize data-ink; delete chartjunk, gridlines that don't help, and 3D.

Pitfall: dual y-axes that manufacture a spurious correlation by arbitrary scaling. Second pitfall: bar charts of means hiding bimodal or skewed distributions — when the distribution matters, show it (box/violin/raincloud).

**Tools:** matplotlib/seaborn/ggplot2, error bars (CI/SE/SD), boxplot/violin, small multiples, colorblind palettes, log scale
