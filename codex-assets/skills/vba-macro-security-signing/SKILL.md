---
name: vba-macro-security-signing
description: >-
  Macro security and digital signing — Trust Center settings, signed vs unsigned macros, SelfCert vs CA certs, trusted locations, VBA project password, distribute macros that don't get blocked
---

# vba-macro-security-signing

Excel runs macros per the **Trust Center** (File > Options > Trust Center > Macro Settings). Default blocks unsigned macros; the safe distribution path is **digital signing**. Self-sign for testing with **SelfCert.exe** (ships with Office), then in the VBE: Tools > Digital Signature > choose your cert. A self-cert is only trusted on machines that explicitly trust it; for real distribution buy a **code-signing certificate** from a CA so the publisher is trusted org-wide.

Expert moves: **Trusted Locations** (Trust Center) let macros run without signing from a known folder — common for internal add-in deployment on a network share (mark it trusted via Group Policy). Files downloaded from the internet carry the **Mark of the Web**, and since 2022 Office **blocks VBA in MOTW files by default** — users must Unblock (file Properties > Unblock) or you must deliver via a trusted location/signed package. Re-sign after **every** code change — editing invalidates the signature. Set a **VBA project password** (project Properties > Protection) to deter casual viewing (note: it's weak, not real security).

Pitfalls: the MOTW block is the modern #1 'why won't my macro run' — emailing an .xlsm just gets it blocked. Self-signed certs vanish if the user profile is rebuilt. A project password locks *you* out if forgotten and can be cracked, so don't treat it as protection of IP. 'Enable all macros' guidance to users is a security anti-pattern — sign instead.

**Tools:** Trust Center, Digital Signature, SelfCert.exe, code-signing certificate, Trusted Locations, Mark of the Web, VBA project password
