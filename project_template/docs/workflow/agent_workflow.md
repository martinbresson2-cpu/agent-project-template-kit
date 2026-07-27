# docs/workflow/agent_workflow.md

# Agent Workflow

> Repeatable workflow for AI-assisted work in this repository.
> Keep this file lean.
> Stable operating rules belong in `AGENTS.md`.
> Delete this file during template bootstrap if `AGENTS.md` is enough.

---

## Purpose

Use this file to define the normal working loop:
- how to start a session
- how to work on one active slice
- how to verify changes
- how to update canonical docs
- how to leave the repo ready for the next session

Current project state does not belong here.
That lives in `docs/roadmap/current_feature.md`.

---

## 1. Start the session

Follow the session-start and template-bootstrap steps in `AGENTS.md`.
This file does not restate them.

---

## 2. Reconstruct the active state

Before coding, identify:
- the current goal
- what is already done
- the next concrete action
- blockers
- relevant open bugs
- applicable constraints
- any human dependency

If `docs/roadmap/current_feature.md` is stale, update it before substantial work.

---

## 3. Work in the smallest coherent slice

A good slice:
- has one clear outcome
- touches only relevant files
- can be verified
- leaves the repo in a valid state

Avoid speculative abstraction and unrelated cleanup unless required.

---

## 4. Resolve uncertainty correctly

### Technical uncertainty
Investigate narrowly:
- relevant source
- nearby tests
- relevant config
- targeted search
- architecture/decision docs if needed

### Product or UX uncertainty
Ask the human instead of silently deciding.

### Architectural uncertainty
If it changes boundaries, ownership, interfaces, or long-term constraints:
- identify the options
- state the trade-offs
- get approval if needed
- record the result in `docs/design/decisions.md`
- update `docs/design/architecture.md`

### Low-risk reversible uncertainty
Use the simplest reasonable default.

---

## 5. Implement

While implementing:
- change only what the slice requires
- preserve boundaries
- avoid duplicate sources of truth
- add or update tests when behavior changes
- keep generated artifacts separate from authored files
- avoid unnecessary new dependencies

If the plan turns out to be wrong, revise it instead of pushing through on bad assumptions.

---

## 6. Verify

Use the narrowest relevant verification first:
- targeted tests
- focused build/run checks
- lint/type checks if relevant
- manual verification if required

If something cannot be verified, say:
- what was not checked
- why
- what risk remains
- what human action is needed

---

## 7. Update canonical files

Update only the files affected by the new truth.

- `docs/roadmap/current_feature.md` — active work status and next action
- `docs/roadmap/next_phase.md` — milestone ordering or future scope changes
- `docs/fixes/fixes_log.md` — unresolved defects
- `docs/design/architecture.md` — current system structure
- `docs/design/decisions.md` — important accepted choices
- `docs/workflow/human_handoff.md` — required human actions

Do not duplicate the same status across multiple files.

---

## 8. Request human action when needed

If the next step requires human action, use `docs/workflow/human_handoff.md`.

Typical reasons:
- credentials or secrets
- external service configuration
- manual testing
- UX or scope approval
- deployment
- signoff

Keep handoffs small and explicit.

---

## 9. End the session cleanly

Before finishing, make sure:
- the active slice is reflected in code and docs
- verification results are clear
- unresolved issues are documented
- required human actions are listed
- the exact next action is obvious

The next session should be able to resume from the standard session-start files without reconstructing context from chat history.