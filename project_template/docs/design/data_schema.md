# Data Schema

> Current data shapes, key entities, and ownership.
> Keep this practical.
> Delete this file during bootstrap if the project has little meaningful data structure.

---

## Purpose

Use this file for the data model the project currently depends on:
- key entities
- important fields
- relationships
- ownership and validation rules

Do not turn this into a full database spec unless the project truly needs that.

---

## How to use this file

Document only data that matters to current or near-term work:
- persisted entities
- important request or response shapes
- shared internal structures
- versioned file formats

Skip trivial DTOs and obvious one-off payloads.

---

## Entity template

### `<entity or structure>`

- **Purpose:** ...
- **Source of truth:** ...
- **Owned by:** ...
- **Stored as:** DB table / file / API payload / in-memory / other
- **Key fields:**
  - `field_name`: type — meaning
  - `field_name`: type — meaning
- **Relations:** ...
- **Validation rules:** ...
- **Notes:** ...

Repeat only as needed.

---

## Shared rules

List only rules that multiple data structures depend on.

- IDs are ...
- Timestamps use ...
- Nullable fields mean ...
- Deletion behavior is ...
- Versioning rule is ...

Delete any rule that does not apply.

---

## Known gaps

Only include data-shape gaps that affect implementation clarity.

- ...
- ...

Do not track bugs or roadmap tasks here.

---

## Update rule

Update this file when:
- a core entity changes
- a shared payload shape becomes important
- validation or ownership rules change
- persistence structure changes in a meaningful way

Architecture belongs in `docs/design/architecture.md`.
Decision rationale belongs in `docs/design/decisions.md`.