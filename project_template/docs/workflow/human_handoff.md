# docs/workflow/human_handoff.md

# Human Handoff

> Canonical list of actions that require human input, approval, access, or execution.
> Keep this file short and actionable.
> Delete it during template bootstrap if the project does not need it.

---

## Purpose

Use this file when the agent cannot safely or directly complete something.

Typical cases:
- credentials or access
- product or UX approval
- external service setup
- deployment or privileged action
- manual verification
- milestone signoff

This file is not a general task list.

---

## Rules

- Only create a handoff when human action is genuinely required.
- Ask for the smallest action needed to unblock progress.
- Never ask for secrets to be pasted into source, docs, commits, or chat.
- Give exact steps when manual action is needed.
- Remove completed handoffs promptly.
- Update the affected canonical files after the human responds.

---

## Priority

- 🔴 Blocking
- 🟠 Required soon
- 🟡 Review
- 🔵 Optional

---

## Open handoffs

No open handoffs.

Replace the line above when real handoffs exist.

---

## Entry template

### H-XXX — `<short title>`

- **Priority:** 🔴 Blocking
- **Owner:** `<person or role>`
- **Related work:** `docs/roadmap/current_feature.md`
- **Status:** Open

#### Why

Why the agent cannot complete this directly.

#### Human action

1. ...
2. ...
3. ...

If this is a decision, give options:

- **Option A:** ...
  - Impact: ...
- **Option B:** ...
  - Impact: ...

#### Expected result

What the human should provide, approve, change, or verify.

#### Verification

How the result should be checked.

- ...
- ...

#### Agent follow-up

After completion, the agent should:
1. verify where possible
2. continue the blocked work
3. update canonical docs
4. remove this handoff

---

## Manual verification template

### H-XXX — Verify `<feature or behavior>`

- **Priority:** 🟡 Review
- **Owner:** Human
- **Environment:** `<local, staging, production, device, platform>`
- **Related work:** `docs/roadmap/current_feature.md`
- **Status:** Open

#### Preconditions

- ...
- ...

#### Steps

1. ...
2. ...
3. ...

#### Expected result

- ...
- ...

#### Report back

Provide:
- pass or fail
- failed step if any
- observed result
- relevant sanitized logs or screenshots

---

## Sensitive actions

For secrets or privileged access:
- name the secret or setting, not its value
- state where it should be configured
- do not store it in this file
- do not ask for it in chat
- provide a safe validation method

Example:
- **Secret name:** `SERVICE_API_KEY`
- **Configure in:** local `.env` or approved secret manager
- **Validation:** run the connection check and report success or sanitized error only

---

## Cleanup rule

A handoff is complete only when:
- the action or decision happened
- the agent acknowledged or verified it
- blocked work resumed or was intentionally deferred
- relevant canonical files were updated
- the completed entry was removed

If the outcome is an important lasting choice, record that in `docs/design/decisions.md`.