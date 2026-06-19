---
name: pa-desktop-flows-rpa
description: >-
  Power Automate Desktop RPA: attended vs unattended, machine/gateway, UI/web automation selectors, run from a cloud flow, error handling
---

# pa-desktop-flows-rpa

**Power Automate Desktop (PAD)** is the RPA engine for legacy/UI apps with no API. Build **desktop flows** in the designer: **UI automation** (record clicks/typing against Windows apps via UI elements), **Web automation** (browser actions via the PAD extension and CSS/XPath selectors), Excel, file/folder, run scripts (VBScript/PowerShell/Python). **Attended** runs on a logged-in user's machine (assist scenarios, can interact); **Unattended** runs headless with no signed-in user on a schedule (needs an **unattended RPA license** + a configured machine or **machine group**). Register the target machine via the **on-premises data gateway** or PAD runtime, then a **cloud flow** calls **"Run a flow built with Power Automate Desktop for Windows"** (pick machine/group + run mode, pass inputs, read outputs). Handle failures with PAD's **On block error** / subflows and return a status the cloud flow checks. Pitfalls: UI selectors are **brittle** - anchor on stable attributes (id/name) not position, and "wait for element" before acting; unattended needs the machine awake, auto-login set, screen unlocked; concurrent unattended runs need enough bot licenses (else queued); credentials from Key Vault or the PAD credential store, never hardcoded; record-then-refine - raw recordings are fragile.

**Tools:** Power Automate Desktop, attended/unattended, machine groups, on-prem data gateway, UI/Web automation selectors, Run a desktop flow, On block error
