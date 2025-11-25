# notification-service

An extensible Python notification service that demonstrates several classic design patterns:

- **Composition over Inheritance**
- **Adapter**
- **Bridge**
- **Decorator**

The project is intentionally small but realistic: it models a notification system that can send messages over multiple channels (email, SMS, Slack, etc.), while being easy to extend and test.

---

## Goals

- Show **clean, modular code** with clear separation of concerns.
- Demonstrate how to:
  - Wrap external APIs using the **Adapter** pattern.
  - Decouple *what* is being sent from *how* it is delivered using the **Bridge** pattern.
  - Add cross-cutting behavior like logging and retry using the **Decorator** pattern.
  - Prefer **composition over inheritance** to avoid deep, rigid class hierarchies.

---

## High-Level Design

### Core Concepts

- **Notification** – a high-level abstraction representing something that should be sent (title, body, metadata).
- **Channel** – an implementation detail describing *how* a notification is sent (email, SMS, etc.).
- **Notifier** – coordinates filters, formatting and the underlying channel to actually send notifications.

### Where Each Pattern Appears

- **Composition over Inheritance**
  - `Notifier` is composed of a channel, formatter, and zero or more filters.
  - Behaviors are plugged in rather than implemented via a large inheritance tree.

- **Adapter**
  - `EmailClientAdapter`, `SmsClientAdapter`, etc. adapt third-party or low-level APIs to a common interface.

- **Bridge**
  - `Notification` is the abstraction; `Channel` types (`EmailChannel`, `SmsChannel`, etc.) are the implementors.
  - `Notification` delegates sending to a `Channel`, allowing them to vary independently.

- **Decorator**
  - `LoggingNotifier`, `RetryNotifier` wrap a `Notifier` to add behavior at runtime (logging, retries, etc.).

---

## Project Structure

```text
notification-service/
├─ src/
│  └─ notify/
│     ├─ __init__.py
│     ├─ core.py          # Notification, Notifier, basic interfaces
│     ├─ channels.py      # EmailChannel, SmsChannel, etc.
│     ├─ adapters.py      # EmailClientAdapter, SmsClientAdapter, etc.
│     ├─ decorators.py    # LoggingNotifier, RetryNotifier, etc.
│     ├─ filters.py       # Simple filters for notifications
│     └─ examples/
│        └─ basic_email.py
├─ tests/
│  ├─ test_notifier.py
│  └─ test_decorators.py  # (you can add more)
├─ pyproject.toml         # or setup.cfg / requirements.txt
└─ README.md
