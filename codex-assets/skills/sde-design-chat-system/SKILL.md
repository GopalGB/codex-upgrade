---
name: sde-design-chat-system
description: >-
  Design WhatsApp/Messenger - WebSocket connections, message store, online presence, fan-out, ordering, and delivery receipts.
---

# sde-design-chat-system

Real-time, so HTTP polling won't do - use **persistent WebSocket** connections held by stateless **connection/gateway servers**; a service-discovery/registry maps user -> which gateway holds their socket so messages can be routed to the right box. **Send flow**: client -> gateway -> message service -> persist to a **message store** (write-heavy, billions of small rows, partition by conversation/user ID - a wide-column store like Cassandra/HBase fits) -> look up recipient's gateway -> push over their socket; if offline, queue and trigger a **push notification** (APNs/FCM). **Ordering**: don't trust client timestamps (clock skew) - assign a server-side monotonic **sequence ID per conversation** so clients sort correctly. **Presence (online/last-seen)**: client sends periodic **heartbeats**; mark offline after a missed-heartbeat timeout; presence changes fan out only to that user's contacts (don't broadcast globally). **Group chat**: fan-out per group; cap group size or use a copy-per-member inbox model. **Delivery/read receipts**: ack states (sent -> delivered -> read) tracked per message. **Pitfall**: stateful connection servers that can't be load-balanced simply (need the registry + sticky routing to the socket), and unbounded group fan-out. Scale connections horizontally - a single box holds limited concurrent sockets.

**Tools:** WebSocket, connection servers, message queue per user, presence heartbeat, sequence IDs, push
