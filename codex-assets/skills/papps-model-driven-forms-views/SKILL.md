---
name: papps-model-driven-forms-views
description: >-
  Model-driven UI: main forms (tabs/sections/columns), views (columns, filter, sort), and business rules for no-code validation/show-hide logic.
---

# papps-model-driven-forms-views

Model-driven apps render from metadata, not pixels. **Forms** (edit in the form designer) organize a record's columns into Tabs > Sections > columns; types: Main (full record), Quick View (read related record inline), Quick Create (fast new record). Control visibility/required/order here; security roles can be granted per form. **Views** define list layouts: pick columns, set the filter (FetchXML/grid filter), sort, and column width; System vs Personal views; the default public view drives grids/lookups. **Business rules** add no-code logic that runs on the form (and some server-side): conditions -> actions like set value, set required, show/hide column, lock, show error message — e.g. 'if Priority = High then Owner becomes required'. They run without JavaScript and work across web/mobile/tablet. Pitfalls: business rules don't fire on all entry points (some bulk/API writes bypass form-scope rules — use real-time workflows/plug-ins for hard server validation); hiding a column with a business rule isn't security (use field-level security or roles); too many columns on one tab hurts load; forgetting to add a column to the FORM means it can't be edited even if on the table. Use the modern designer; classic is deprecated.

**Tools:** Form designer, view designer, business rules, main/quick-view/quick-create forms, classic vs modern designer
