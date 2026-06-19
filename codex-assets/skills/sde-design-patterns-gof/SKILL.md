---
name: sde-design-patterns-gof
description: >-
  Reach for the right Gang-of-Four pattern - factory, strategy, observer, decorator, adapter, singleton - and know when not to.
---

# sde-design-patterns-gof

GoF patterns are named solutions to recurring design problems. **Creational**: **Factory Method/Abstract Factory** centralize object creation so callers depend on an interface, not a constructor; **Builder** assembles complex objects step-by-step (avoids telescoping constructors); **Singleton** ensures one instance (overused - it's global state in disguise, hard to test; prefer DI). **Structural**: **Adapter** wraps an incompatible interface to fit yours; **Decorator** adds behavior by wrapping (composable, beats subclass explosion - e.g., stacking streams); **Facade** gives a simple entry point over a complex subsystem; **Proxy** intercepts access (lazy load, cache, access control). **Behavioral**: **Strategy** swaps algorithms behind one interface (the OCP enabler - replaces conditional chains); **Observer** notifies subscribers of state changes (the basis of event systems); **State** makes state-dependent behavior explicit objects; **Command** encapsulates an action as an object (undo, queues). **Pitfall**: pattern-itis - forcing patterns where a plain function or a map would do. Patterns are vocabulary for tradeoffs you've identified, not a checklist to maximize. Recognize the problem first, then name the pattern.

**Tools:** Strategy, Factory, Observer, Decorator, Adapter, Builder, Singleton
