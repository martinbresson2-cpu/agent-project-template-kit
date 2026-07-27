# docs/design/architecture.md

# Architecture

> Canonical description of the system's current technical structure.
> Keep this file short, current, and practical.
> Delete it during template bootstrap if the project is too small to need it.

---

## Purpose

Describe the system in technical terms only:
- what it does
- what the main runtime or deliverable is
- what the key technical constraint is

Keep this brief.

---

## System overview

Replace this with the actual project flow.

    User / Caller
      -> Entry point
      -> Application logic
      -> Data / external systems
      -> Output

---

## Main components

Document only meaningful components.

### `<component>`

- **Owns:** ...
- **Inputs:** ...
- **Outputs:** ...
- **Depends on:** ...
- **Location:** ...
- **Does not own:** ...

Repeat only as needed.

---

## Boundary rules

List the few rules that matter.

- `...` may depend on `...`
- `...` must not depend on `...`
- Business logic must not live in `...`
- External integrations must stay behind `...`
- Generated artifacts must stay separate from authored source

Delete rules that do not apply.

---

## Data flow

Describe the main flow in 3–6 steps.

1. ...
2. ...
3. ...
4. ...

If there is an important alternative flow, add it briefly.

---

## State and persistence

- **Source of truth:** ...
- **Persistent storage:** ...
- **Transient state:** ...
- **Ownership:** ...
- **Consistency rules:** ...

If this project has little or no meaningful state, say so briefly.

---

## External interfaces

List only interfaces that matter architecturally.

### `<interface>`

- **Purpose:** ...
- **Direction:** inbound / outbound
- **Format:** API / CLI / file / event / library
- **Owned by:** ...
- **Failure behavior:** ...

---

## Repository map

Only include directories needed for orientation.

    <path>/    # responsibility
    <path>/    # responsibility
    <path>/    # responsibility

Do not paste the whole repo tree.

---

## Constraints

List current architectural constraints.

- ...
- ...
- ...

Only include constraints that implementation must respect now.

---

## Known gaps

List architectural gaps relevant to current or near-term work.

- ...
- ...

Do not use this for bugs or roadmap tasks.

---

## Update rule

Update this file when:
- component responsibilities change
- dependency direction changes
- data flow or state ownership changes
- a significant interface is added or replaced
- a constraint changes

Significant rationale belongs in `docs/design/decisions.md`.