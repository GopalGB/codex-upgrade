---
name: sde-message-queues-event-driven
description: >-
  Decouple services with queues and logs - Kafka vs RabbitMQ, delivery guarantees, consumer groups, ordering, and backpressure.
---

# sde-message-queues-event-driven

Queues decouple producers from consumers so spikes are absorbed and services fail independently. **Two models**: **message broker** (RabbitMQ, SQS) - a message is delivered then removed, good for task/work queues, competing consumers; **log** (Kafka, Pulsar) - an append-only partitioned log consumers read by offset, messages retained for replay, good for event streaming and multiple independent consumers. **Delivery semantics**: at-most-once (may lose), **at-least-once** (may duplicate - the practical default), exactly-once (expensive, usually faked via idempotency). Because you get duplicates, **make consumers idempotent** (dedupe on a message ID / use upserts). **Ordering** holds only within a Kafka partition - to keep per-entity order, partition by entity key. **Consumer groups** let you parallelize: one partition per consumer max. **Backpressure**: bound queue depth, alert on lag; a growing queue means consumers can't keep up. **Dead-letter queue** for poison messages after N retries. **Pitfall**: assuming exactly-once and ordered-everything for free - design for duplicates and partial ordering, and watch consumer lag as your saturation signal.

**Tools:** Kafka, RabbitMQ, SQS, at-least-once, idempotent consumers, DLQ, partitions
