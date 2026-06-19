---
name: sde-observability
description: >-
  Make systems debuggable in prod - structured logs, RED/USE metrics, distributed traces, correlation IDs, and symptom-based alerts.
---

# sde-observability

Observability = inferring internal state from outputs. Three pillars. **Logs**: structured JSON (not free text) with `timestamp, level, service, requestId, message`; log business events and errors at the right level; never log secrets/PII; carry a **correlation/trace ID** across services. **Metrics**: cheap aggregates for dashboards and alerts - use **RED** for services (Rate, Errors, Duration) and **USE** for resources (Utilization, Saturation, Errors). Track latency as **histograms/percentiles (p50/p95/p99)**, never averages (an average hides the tail that's actually hurting users). Name with a namespace (`app_http_requests_total`). **Traces** (OpenTelemetry): a request's spans across services reveal where latency goes and which hop failed - essential for microservices. **Alert on symptoms, not causes**: page on 'error rate > 1%' or 'p99 latency > SLO', not 'CPU > 80%' (high CPU may be fine); every page needs a runbook. Tie alerts to **SLOs/error budgets** so you alert on user-facing impact. **Pitfall**: logging everything at INFO (cost + noise drowns signal), alert fatigue from cause-based alerts, and dashboards full of averages that look healthy while the p99 is on fire.

**Tools:** structured logging, Prometheus metrics, OpenTelemetry tracing, RED/USE, correlation IDs, SLO
