---
name: m365-change-notifications-webhooks
description: >-
  Subscribe to Graph change notifications (webhooks) for mail, lists, drives, and Teams instead of polling — when reacting to M365 changes in near-real-time
---

# m365-change-notifications-webhooks

Create a subscription: `POST /subscriptions` with `{"changeType":"created,updated","notificationUrl":"https://you/api/hook","resource":"/users/{id}/mailFolders('inbox')/messages","expirationDateTime":"...","clientState":"secret"}`. On creation Graph immediately POSTs a `validationToken` to your URL — you must echo it back as plain text within 10s or the subscription fails. Thereafter Graph POSTs notification payloads; verify the `clientState` matches yours.

Subscriptions expire fast (messages ~3 days max, others vary) — renew with `PATCH /subscriptions/{id}` before expiry, and set a `lifecycleNotificationUrl` to catch `reauthorizationRequired`/`subscriptionRemoved` events.

Pitfall: notifications are **lightweight** (they tell you *what* changed, not the content) — fetch the resource by id, and de-dup since delivery is at-least-once. Pitfall 2: your endpoint must be public HTTPS and answer the validation handshake synchronously, or creation 400s. Pitfall 3: for guaranteed delivery use **rich notifications with encrypted resource data** (supply an `encryptionCertificate`) or pair with a **delta query** as a backstop — webhooks can miss events during outages.

**Tools:** POST /subscriptions, notificationUrl, validationToken, lifecycleNotificationUrl, clientState
