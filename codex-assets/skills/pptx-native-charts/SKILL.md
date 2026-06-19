---
name: pptx-native-charts
description: >-
  Insert and format native (editable) PowerPoint charts — column/bar/line/combo/waterfall — with clean axes, data labels, and theme colors, not pasted images
---

# pptx-native-charts

Insert > Chart embeds a live mini-Excel; the chart stays editable and recolors with the theme. Prefer this over pasting an image from Excel (images don't reflow, don't theme, and pixelate when projected). Pick the right type: column for comparison-over-few-categories, line for trend-over-time, 100% stacked for composition, combo (Chart Design > Change Chart Type > Combo) to overlay a line on bars with a secondary axis. Declutter: delete gridlines and chart border, put data labels directly on series (right-click series > Add Data Labels) and drop the value axis, sort categories by value not alphabetically. In python-pptx: `slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, x,y,cx,cy, chart_data)` where chart_data is a CategoryChartData with `add_category` / `add_series`; then `chart.plots[0].has_data_labels = True` and set `number_format`. Pitfall: linked (not embedded) Excel charts break when the deck is emailed — embed unless live links are required. To force brand colors, set series fill to a theme accent so it survives theme swaps.

**Tools:** Insert > Chart; Chart Design / Format tabs; python-pptx add_chart, CategoryChartData, XL_CHART_TYPE
