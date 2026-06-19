---
name: copilot-analytics-transcripts
description: >-
  Measure agent performance and debug real conversations using the Analytics dashboards, session details, conversation transcripts, and Dataverse/Application Insights export.
---

# copilot-analytics-transcripts

The **Analytics** page surfaces engagement (total/engaged sessions), **resolution rate**, **escalation rate**, **abandon rate**, CSAT, and per-topic/per-tool usage. Drill into **Session details** for individual conversations and download **conversation transcripts** (available a few minutes after a session times out; retained ~28-29 days in the UI). For longer retention and BI, transcripts are stored in **Dataverse** (the `conversationtranscript` table) - query them with Power BI/Power Automate, or stream telemetry to **Application Insights** for production monitoring and custom dashboards. Use analytics to find topics with high escalation (bad answers) or low engagement (never triggered). Pitfalls: (1) The 28-day UI window means you *must* set up Dataverse/App Insights export for compliance or long-term trend analysis - don't rely on the dashboard. (2) Resolution rate is inferred (no explicit handoff/escalation = 'resolved'), so it overstates success; pair it with CSAT and manual transcript review. (3) Transcripts can contain PII - govern access to the Dataverse table and respect retention policy. (4) Generative-orchestration tool-call details show in session view - use them to find tools that fire incorrectly.

**Tools:** Analytics page, engagement/resolution/escalation rates, Session details, transcript download, Dataverse, Application Insights
