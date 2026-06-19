---
name: pa-expressions-wdl
description: >-
  Workflow Definition Language: concat/if/coalesce/formatDateTime, triggerBody()/items(), null-safe ?[] access, type coercion
---

# pa-expressions-wdl

Power Automate expressions use **WDL** (Logic Apps language) in the fx box. Strings: `concat('Hi ', items('Apply_to_each')?['Name'])`, `replace()`, `substring(s,0,5)`, `split(t,';')`, `trim()`, `toLower()`. Logic: `if(greater(item()?['Qty'],100),'Bulk','Std')`, `and()`, `or()`, `equals()`, `empty()`. **`coalesce(x,y,'default')`** returns the first non-null - essential for optional fields. Dates: `utcNow()`, `formatDateTime(utcNow(),'yyyy-MM-dd')`, `addDays(utcNow(),-7)`, `convertTimeZone(utcNow(),'UTC','India Standard Time','dd MMM yyyy')`. Data refs: `triggerBody()`, `triggerOutputs()?['body/value']`, `outputs('Compose')`, `variables('Counter')`, `items('Apply_to_each')`. Parse paths with **null-safe `?[]`**: `body('Get_item')?['Customer']?['Email']` - `['x']` on null throws "property cannot be selected", `?['x']` returns null. Coercion bites: `int()`, `float()`, `string()`, `bool()`; "5" != 5. Pitfalls: build complex expressions in a **Compose** and inspect output before chaining; escape single quotes by doubling; deep `?[]` chains are unreadable - prefer **Parse JSON** for typed dynamic content.

**Tools:** concat, if, coalesce, formatDateTime, utcNow, addDays, convertTimeZone, triggerBody, items, ?[] null-safe, int/string
