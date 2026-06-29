---
name: craft-delete-dead-code
description: >-
  Delete dead code as you go — unreachable branches, unused functions/vars/imports, commented-out blocks, and orphaned dependencies — and trust git history instead of keeping code 'just in case'. Use whenever you touch a file with cruft; deletion is a feature, and every dead line is a maintenance tax and a false signal.
---

# craft-delete-dead-code

Dead code is a liability, not an asset. Unreachable branches, functions nobody calls, variables never read, imports nothing uses, and especially **commented-out blocks** all cost real money: they mislead readers into thinking they matter, they show up in searches and break grep-driven reasoning, they get "maintained" during refactors for no reason, and they hide the code that's actually live. When you touch a file and spot cruft in your path, remove it.

Don't keep code "just in case" — that's what version control is for. The old implementation lives in git history with full context; a commented-out block in the working tree has none and only rots. If you're replacing logic, delete the old, don't comment it out "to be safe". Remove the now-unused import, the helper that lost its last caller, the feature flag that's been fully rolled out, the dependency you just stopped using.

Be sure it's actually dead before you cut: check for callers (including dynamic/reflective and cross-package use), tests, and config/serialized references — then delete confidently. Deletion is one of the highest-leverage edits you can make: it shrinks the surface area, speeds comprehension, and removes places for bugs to hide. A diff that's net-negative lines while keeping the tests green is usually a good diff.

**Tools:** remove unreachable/unused/commented-out code · trust git history not "just in case" · drop orphaned imports + deps + dead flags · verify no callers/tests/config first · deletion is a feature · net-negative diffs win
