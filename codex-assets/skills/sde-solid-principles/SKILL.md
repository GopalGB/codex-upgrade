---
name: sde-solid-principles
description: >-
  Apply SOLID to keep OO code flexible - single responsibility, open-closed, Liskov, interface segregation, dependency inversion.
---

# sde-solid-principles

Five principles that make OO code change-tolerant. **S - Single Responsibility**: a class has one reason to change; mixing persistence, business logic, and formatting in one class means every concern's change risks the others - split them. **O - Open/Closed**: open for extension, closed for modification; add behavior via new subtypes/strategies rather than editing a growing switch statement. **L - Liskov Substitution**: a subtype must be usable anywhere its base is, honoring the base's contract - the classic violation is a Square subclassing Rectangle whose setWidth breaks callers' assumptions, or a subclass that throws on a method the base promised. **I - Interface Segregation**: many small focused interfaces over one fat interface, so clients don't depend on methods they don't use. **D - Dependency Inversion**: depend on abstractions, not concretions; high-level policy shouldn't import a concrete DB class - inject an interface (enables testing with fakes). **Pitfall**: over-applying SRP into a sea of one-method classes, or adding interfaces with a single implementation 'just in case' - SOLID serves changeability, not ceremony. Apply when a class is actually churning, not preemptively everywhere.

**Tools:** SRP, OCP, LSP, ISP, DIP, dependency injection
