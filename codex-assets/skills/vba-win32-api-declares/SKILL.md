---
name: vba-win32-api-declares
description: >-
  Call Windows API from VBA with Declare statements — PtrSafe and LongPtr for 64-bit, Sleep/GetTickCount/timers, file dialogs, window handles, conditional compilation #If Win64
---

# vba-win32-api-declares

VBA reaches the Windows API via `Declare` at the top of a module. Since Office 2010 (VBA7) on 64-bit you **must** add `PtrSafe` and use `LongPtr` for anything that holds a pointer/handle (hWnd, hDC, memory addresses): `Private Declare PtrSafe Function Sleep Lib "kernel32" (ByVal ms As Long)`. Common ones: `Sleep` (pause without burning CPU), `GetTickCount` (millisecond timer), `FindWindow`/`SetForegroundWindow` (window control), `SHGetPathFromIDList` / `GetOpenFileName` (native dialogs), `timeGetTime`.

Expert moves: write **cross-bitness** code with conditional compilation so the same file runs on 32- and 64-bit Office:
```vba
#If VBA7 Then
  Private Declare PtrSafe Function Sleep Lib "kernel32" (ByVal ms As Long)
#Else
  Private Declare Function Sleep Lib "kernel32" (ByVal ms As Long)
#End If
```
Use `#If Win64 Then` to branch on the actual bitness (handle sizes differ). Match parameter types to the C signature exactly — `As Any` with `ByVal` for string/null flexibility, `ByVal` strings get passed as pointers automatically.

Pitfalls: a wrong type or missing `ByVal` causes an instant **Excel crash** (not a catchable VBA error) because you're poking memory directly — save before testing. `Long` where the API expects a pointer corrupts on 64-bit (that's exactly what `LongPtr` fixes). `Sleep` blocks the whole UI — for cooperative waits, loop with `DoEvents`. Declares without `PtrSafe` won't even compile in 64-bit Office. Library names are case-sensitive on the export, not the DLL.

**Tools:** Declare PtrSafe, LongPtr, Win64, VBA7, Sleep, GetTickCount, FindWindow, kernel32, user32, #If conditional compilation
