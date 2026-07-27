# Fixes Log — Outstanding Bugs and Issues

> Live list of unresolved bugs, defects, broken flows, and important technical issues.
> Keep entries concrete and actionable.
> Remove resolved items instead of turning this file into a history archive.

This file is for:
- actual bugs
- incorrect behavior
- broken assumptions found during implementation
- issues discovered during manual testing
- important technical debt that actively causes defects or blocks progress

This file is not for:
- future features
- vague ideas
- roadmap items
- long retrospectives

---

## Usage rules

- Newest or highest-priority items go near the top.
- Be specific about symptom and repro.
- If the cause is unknown, say so.
- If fixed, remove the entry.
- If an issue turns out to be a design decision, move that insight to `docs/design/decisions.md`.

---

## Severity legend

- 🔴 blocker — stops meaningful progress or core usage
- 🟠 major — serious incorrect behavior, but work can continue
- 🟡 minor — incorrect but non-blocking
- 🔵 polish — rough edge, low risk, cosmetic or UX quality issue

---

## Entry template

### [SEVERITY] Short title
- **Symptom:** What goes wrong.
- **Repro:** Exact steps to reproduce.
- **Expected:** What should happen instead.
- **Suspect:** File, subsystem, or unknown.
- **Notes:** Any useful context, workaround, or related decision.

---

## Open issues

No open issues.