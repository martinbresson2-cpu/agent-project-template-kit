# docs/design/decisions.md

# Decisions

> Canonical record of significant technical or structural decisions.
> Keep entries short and useful.
> Delete this file during template bootstrap if the project is too small to need it.

---

## Use this file for

Record decisions that affect:
- architecture
- data ownership
- dependencies
- interfaces
- testing strategy
- deployment
- long-term repository structure

Do not use it for:
- task status
- bugs
- feature ideas
- temporary notes
- implementation diary

---

## Status

- **Proposed** — under consideration
- **Accepted** — currently in effect
- **Superseded** — replaced by a later decision
- **Rejected** — considered and not adopted

---

## Index

- `D-001` — `<title>` — `<status>`

Remove the example line when real decisions exist.

---

## Entry template

### D-XXX — `<short title>`

- **Status:** Proposed
- **Date:** YYYY-MM-DD
- **Owners:** ...
- **Related files:** `path/to/file`
- **Supersedes:** None
- **Superseded by:** None

#### Context

What problem or constraint required a decision?

#### Decision

We will ...

#### Why

Why this option was chosen.

#### Alternatives considered

- **`<option>`:** why not chosen
- **`<option>`:** why not chosen

Remove this section if not useful.

#### Consequences

- Positive: ...
- Trade-off: ...
- Follow-up: ...

---

## Active decisions

Add accepted or proposed decisions below this heading.

<!-- Add decisions here. -->

---

## Superseded or rejected decisions

Move old entries here only if keeping them prevents confusion.

---

## Update rule

Update this file when:
- a significant decision is accepted
- an earlier decision is replaced
- a new constraint changes the reasoning
- the project would likely re-argue the same choice later

If a decision changes:
1. keep the old entry if still useful
2. mark it `Superseded`
3. add the new entry
4. update `docs/design/architecture.md` if the current system changed