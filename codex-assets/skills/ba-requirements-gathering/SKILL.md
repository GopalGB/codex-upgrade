---
name: ba-requirements-gathering
description: >-
  Elicit analytics/BI requirements: stakeholder interviews, the 5 Whys to the real question, define metrics + grain + filters, write acceptance criteria and a data dictionary; avoid solutioning before the question.
---

# ba-requirements-gathering

The job is to find the decision behind the request, not to build the chart they asked for. When someone says 'I need a dashboard of sales', apply the 5 Whys to surface the actual question and the action it drives ('so I can spot which reps to coach this month'). Interview structure: current state, the decision being made, frequency/latency needed, definition of every term ('active', 'revenue' — net or gross? recognized or booked?), the grain (per what — customer, order, day?), required filters/segments, and the threshold that triggers action. Pin down each metric's exact formula, source table, and refresh cadence in a data dictionary so 'churn' means one thing org-wide. Write requirements as user stories with acceptance criteria ('As a regional manager, I can filter pipeline by rep and stage; AC: numbers reconcile to the CRM weekly export to the dollar'). Expert moves: prototype a throwaway mock and react-test it — people critique a draft far better than they spec from scratch; separate must-have from nice-to-have explicitly; confirm who consumes it and what they'll do when the number is bad. Pitfalls: jumping to a tool/chart before the question (solutioning); accepting vague terms without nailing definitions and grain; gathering from one stakeholder when the metric crosses teams; no acceptance criteria so 'done' is contested; scope creep from undocumented assumptions; building the literal ask instead of the underlying need.

**Tools:** stakeholder interviews, 5 Whys, user stories, data dictionary
