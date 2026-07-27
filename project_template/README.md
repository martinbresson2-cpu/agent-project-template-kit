# README.md

# AI Agent Coding Project Template

A reusable template repo for starting and running projects with Claude or other coding agents.

This template is not tied to a specific domain. Its purpose is to provide:
- a clean project structure
- operating instructions for the agent
- roadmap and fix tracking
- architecture and workflow docs
- a low-noise, token-efficient way of working

## What this template is for

Use this when starting a new project where an AI coding agent will help design, plan, implement, debug, and document the work.

The template is designed to:
- keep the agent focused on one active workstream at a time
- separate live execution docs from reference docs
- reduce repeated explanations across sessions
- make progress visible and auditable
- preserve context without forcing the agent to reread the whole repo every time

## Important template rule

This template intentionally contains more files and folders than any one project will need.

The first setup pass for a new project should:
1. keep the useful structure,
2. fill in the important files,
3. delete any template files or folders that are not needed for that specific project.

This improves both clarity and token efficiency.

## Recommended startup flow

When creating a new project from this template:

1. Open this project with the coding agent.
2. Read `CLAUDE.md`.
3. Give the agent the contents of `PROMPT_START.md`.
4. Let the agent:
   - understand the new project,
   - prune unnecessary template files,
   - fill in the core docs,
   - propose the first milestone and active feature,
   - only then begin implementation.

## Core files

- `CLAUDE.md` — main operating instructions for the agent
- `PROMPT_START.md` — first prompt for bootstrap
- `docs/roadmap/current_feature.md` — the single active workstream
- `docs/roadmap/next_phase.md` — upcoming milestones
- `docs/roadmap/archive.md` — completed work
- `docs/fixes/fixes_log.md` — outstanding bugs and issues
- `docs/design/architecture.md` — technical structure and boundaries
- `docs/design/decisions.md` — important decisions and rationale
- `docs/workflow/human_handoff.md` — required manual human actions

## Template philosophy

This template favors:
- one source of truth per topic
- one active workstream at a time
- lean docs over long manuals
- explicit human and agent boundaries
- progress tracking by file, not by chat history