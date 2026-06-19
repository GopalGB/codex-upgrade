---
name: xls-financial-modelling
description: >-
  Financial functions and model structure: NPV/XNPV/IRR/XIRR, PMT/IPMT/PPMT, depreciation, amortization schedules, 3-statement linkage best practices
---

# xls-financial-modelling

Use the **X-functions for real dates**: **XNPV(rate, values, dates)** and **XIRR(values, dates, [guess])** handle irregular cash-flow timing — plain NPV/IRR assume equal periods AND (NPV trap) treat the first value as end-of-period-1, so you must add the period-0 outflow OUTSIDE the NPV: `=cashflow0 + NPV(r, cf1:cfn)`. **PMT(rate,nper,pv)** for level loan payment; split into interest **IPMT** and principal **PPMT** to build an **amortization schedule** (beginning balance → IPMT/PPMT → ending balance, rolling down). **FV/PV** for time value; **RATE/NPER** to back-solve. Depreciation: **SLN** (straight-line), **DB/DDB** (declining balance), **SYD**. Modelling discipline: separate **inputs (blue) / calcs (black) / outputs**, one formula per row copied across (no hardcodes mid-row), flag circularity (interest-on-debt loops) and enable iterative calc only deliberately, build **error checks** (balance sheet balances, sources=uses). Pitfall: monthly rate = annual/12 and nper in months — mismatched units silently corrupt every payment; IRR can return multiple roots on sign-flipping flows — verify with XNPV at the result.

**Tools:** NPV, XNPV, IRR, XIRR, PMT, IPMT, PPMT, FV, SLN
