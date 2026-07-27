# Agent Project Template Kit

A reusable kit for creating AI-agent coding projects with a lean, structured starting point.

This repository is meant to be shared and reused.
It contains both:
- the maintained template system
- the starter project that gets copied into new projects

## Repository structure

The repo has two layers:

- root level — maintenance and generation
- `project_template/` — the actual starter project payload :

   - create_template_repo.py      # creates a new project from the template
   - project_template/            # copied into each new project
    - README.md
    - CLAUDE.md
    - PROMPT_START.md
    -  docs/
    -  scripts/

## How to start a new project

Create a fresh project copy:

    python create_template_repo.py ../my_new_project

This creates a new folder from `project_template/`.

Then open the new project folder with your coding agent and start from:
- `CLAUDE.md`
- `PROMPT_START.md`

Do not build your real project inside this root repository.

## What this repo is for

Use this repository to:
- share a reusable AI-agent project template
- maintain and improve that template over time
- generate clean starting points for new projects

## Maintenance scope

Work at the root level when you want to:
- improve the template structure
- refine bootstrap docs
- update generation behavior
- keep the default starter lean and useful

Work inside a generated project when you want to build a real product.

## Design intent

The starter template is intentionally a little over-provisioned at the beginning.

When a new project is created from it, the first agent should:
- understand the real project
- keep only useful files
- delete unnecessary template scaffolding
- define the first active workstream
- only then begin implementation