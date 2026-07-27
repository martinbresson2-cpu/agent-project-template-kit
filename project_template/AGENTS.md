# Agent Operating Guide

This file is the main operating contract for AI-assisted work in this repository.

It is intentionally short and procedural. It should point to deeper docs rather than duplicate them.

---

## Session start — do this first every time

1. Read `docs/roadmap/current_feature.md`
2. Read `docs/fixes/fixes_log.md`
3. Skim `docs/roadmap/next_phase.md`
4. Read any additional file only if the current task requires it
5. Do not start broad exploratory reading unless explicitly asked

Your roadmap, fixes, and decisions docs are your **structured memory**, not
paperwork: read them first at session start, and write the new truth back to
them last before finishing. Reconstruct state from these files — never from
chat history.

If this is a **new project created from the template**, also read:
- `PROMPT_START.md`
- `README.md`

---

## Template bootstrap rule

This repository may begin as a copy of a generic template.

If so, the first setup pass must:
1. identify which template files/folders are actually useful for this project,
2. keep and fill the needed ones,
3. **delete the unnecessary ones**.

Do not leave irrelevant template scaffolding in place "just in case".

Reason:
- it wastes tokens,
- creates context noise,
- makes navigation worse,
- increases maintenance burden.

When deleting template leftovers, preserve only what the project realistically needs.

---

## Context discipline

Tokens are a resource. Spend them carefully.

### Reading rules
- Read narrowly, not broadly.
- Prefer the smallest file that answers the question.
- Do not repeatedly reread the same long documents in full.
- Do not inspect files "just in case".
- For structured data questions, prefer targeted inspection over full-file reading when possible.

### Writing rules
- Lead with the answer or result.
- Be concise unless detail is needed.
- Avoid repeating the same fact in multiple docs.
- Update the canonical file for a fact instead of scattering the same information around the repo.

---

## Canonical file ownership

Use these files consistently.

- `docs/roadmap/current_feature.md`  
  The single active workstream, current status, exact next actions, open blockers.

- `docs/roadmap/next_phase.md`  
  Milestones, queued work, future phases.

- `docs/roadmap/archive.md`  
  Completed/shipped items only.

- `docs/fixes/fixes_log.md`  
  Outstanding bugs/issues only. Remove resolved items rather than keeping long tombstones.

- `docs/design/architecture.md`  
  Current system design, technical structure, boundaries.

- `docs/design/decisions.md`  
  Important decisions and why they were made.

- `docs/workflow/human_handoff.md`  
  Manual actions required from the human.

If a fact belongs somewhere, record it once in the correct place.

Not every file above ships in every project — a minimal setup starts with only
the roadmap and fixes docs. When a fact needs a home that does not exist yet,
create that canonical file at the path above rather than scattering it elsewhere.

---

## Working style and loop

- Prefer one active workstream at a time; break large work into explicit phases.
- Work in the smallest coherent slice: one clear outcome, only the files it
  needs, verifiable, leaving the repo valid. Avoid speculative abstraction and
  unrelated cleanup.
- Keep implementation aligned with the written architecture and roadmap.
- Resolve uncertainty by kind:
  - **Technical** — investigate narrowly (relevant source, nearby tests, config,
    a targeted search), don't guess.
  - **Product / UX / scope** — ask the human; do not silently decide.
  - **Architectural** (boundaries, ownership, interfaces, long-term constraints)
    — state the options and trade-offs, get approval if needed, then record it
    in `docs/design/decisions.md` and update `docs/design/architecture.md`.
  - **Low-risk and reversible** — pick the simplest reasonable default.
- Verify with the narrowest relevant check first (targeted tests, a focused run,
  lint/type). If something cannot be verified, say what was not checked, why, the
  remaining risk, and any human action needed.
- Surface uncertainty early.

---

## Hard rules

1. Do not silently make major product decisions.
2. Do not mark work as shipped without explicit user signoff.
3. Do not duplicate the same status narrative across multiple files.
4. Do not leave resolved bugs cluttering the fixes log.
5. Do not preserve template files that the project clearly does not need.
6. Do not mix authored source-of-truth files with generated artifacts.
7. If architecture changes, update `docs/design/architecture.md`.
8. If priorities change, update `docs/roadmap/current_feature.md` and, if needed, `docs/roadmap/next_phase.md`.
9. If a manual step is required, write it clearly in `docs/workflow/human_handoff.md` or provide a task card in chat.
10. Prefer deterministic, testable changes wherever practical.

---

## Definition of done

A task or feature is not done until, as appropriate:

- implementation is complete,
- tests pass,
- docs are updated,
- manual steps are documented,
- the current feature file reflects the new truth,
- and the user has signed off if this is a milestone or visible feature completion.

Do not self-upgrade "implemented" into "shipped".

---

## Commit discipline

If the user wants commit-driven progress tracking, commit at meaningful checkpoints:
- after a coherent feature slice,
- after a milestone step,
- after a roadmap/doc state change paired with code changes.

Keep commit messages specific and useful.

If commit behavior should be automatic in this repo, document that explicitly in this file or in project-specific workflow docs.

---

## If this is a brand-new project from the template

Your first job is not coding — it is to bootstrap: understand the project, prune
the template (see **Template bootstrap rule** above), establish the roadmap and
architecture skeleton, define the first active feature, then begin
implementation. `PROMPT_START.md` is the step-by-step first prompt.