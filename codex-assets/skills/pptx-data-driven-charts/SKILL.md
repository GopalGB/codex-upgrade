---
name: pptx-data-driven-charts
description: >-
  Generate charts programmatically from CSV/DataFrame and refresh embedded chart data at scale — batch decks, monthly reporting, parameterized exports
---

# pptx-data-driven-charts

For repeatable reporting, never hand-build charts. Read data with pandas, then drive python-pptx: build `CategoryChartData()`, `chart_data.categories = df.index`, loop `chart_data.add_series(name, df[col].tolist(), number_format='#,##0')`, and `chart.replace_data(chart_data)` to swap data while preserving all formatting/colors. Use `XyChartData`/`BubbleChartData` for scatter. Expert pattern: build one perfectly-formatted template deck with placeholder charts, then for each reporting period clone it and call `replace_data` per chart — formatting is authored once, data is the only variable. Find a chart via `for shp in slide.shapes: if shp.has_chart: shp.chart`. Pitfall: python-pptx writes the categories/values but the embedded workbook cache can go stale; `replace_data` rewrites it, but if you need the user to 'Edit Data' afterward, verify the embedded xlsx matches. For thousands of points or live dashboards, render the chart in matplotlib/plotly as a high-DPI PNG and `add_picture` instead — editability traded for fidelity. Always set explicit `number_format` so 0.224 doesn't render as a raw float.

**Tools:** python-pptx CategoryChartData/XyChartData, chart.replace_data; pandas; openpyxl for the embedded workbook
