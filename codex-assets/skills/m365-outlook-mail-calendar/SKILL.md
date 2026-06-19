---
name: m365-outlook-mail-calendar
description: >-
  Send mail, read messages, and manage calendar events via Graph — when automating Outlook/Exchange email or scheduling
---

# m365-outlook-mail-calendar

Send mail: `POST /users/{id}/sendMail` body `{"message":{"subject":"Hi","body":{"contentType":"HTML","content":"..."},"toRecipients":[{"emailAddress":{"address":"a@b.com"}}]},"saveToSentItems":true}`. Read inbox: `GET /users/{id}/mailFolders/inbox/messages?$select=subject,from,receivedDateTime&$top=25`. Reply: `POST /messages/{id}/reply`.

Calendar: create `POST /users/{id}/events` with `start`/`end` objects carrying `dateTime`+`timeZone`; find free slots `POST /users/{id}/calendar/getSchedule` with attendee addresses and a time window; `POST /me/findMeetingTimes` suggests slots.

Delegated `Mail.Send`/`Calendars.ReadWrite`; app-only `Mail.Send` lets the daemon send **as any mailbox** — lock it down with an **Application Access Policy** (`New-ApplicationAccessPolicy` in Exchange Online PowerShell) scoping the app to a mail-enabled security group.

Pitfall: timezone — always set `Prefer: outlook.timezone="India Standard Time"` header on reads, and include `timeZone` in event bodies, or times come back in UTC and shift. Pitfall 2: app-only Mail.Send without an access policy is a tenant-wide spoofing risk auditors flag. Pitfall 3: large attachments (>3MB) need an upload session, not inline base64.

**Tools:** /me/sendMail, /users/{id}/messages, /events, /calendar/getSchedule, Mail.Send
