---
name: vba-class-modules-oop
description: >-
  Object-oriented VBA with class modules — properties (Get/Let/Set), private fields, methods, Class_Initialize/Terminate, custom events with RaiseEvent/WithEvents, collections of objects
---

# vba-class-modules-oop

Insert a **Class Module**, name it like a type (`Customer`, `Invoice`). Hold state in `Private` fields (`Private mName As String`) and expose them through property procedures: `Property Get Name`, `Property Let Name(v As String)` for value types, `Property Set Obj(v As Object)` for object types. Add methods as `Public Sub`/`Function`. `Class_Initialize` runs on `New`; `Class_Terminate` on destruction (set defaults / release resources there). Instantiate with `Set c = New Customer`.

Expert moves: model a domain as a class plus a **collection of those objects** (or a Dictionary keyed by ID) instead of parallel arrays — far cleaner. Declare **custom events**: in the class `Public Event StatusChanged(ByVal s As String)`, fire with `RaiseEvent StatusChanged("Paid")`; consume in another module via `Dim WithEvents inv As Invoice`. Use `Implements IShape` for interface-style polymorphism. Read-only properties = omit the `Let`/`Set`. Validate inside `Property Let` to enforce invariants.

Pitfalls: VBA classes have **no constructor parameters** — you can't `New Customer("Bob")`; use an `Init` method or a factory function instead. No true inheritance — `Implements` gives interfaces only, and you must stub every member. `WithEvents` variables must be at module level in a class/form, not in a Sub. Circular object references can prevent `Class_Terminate` from firing (memory leak). `Property Set` vs `Let` mix-up on object properties is a common compile error.

**Tools:** Class Module, Property Get/Let/Set, Private fields, Class_Initialize, Class_Terminate, Public Event, RaiseEvent, WithEvents, Implements
