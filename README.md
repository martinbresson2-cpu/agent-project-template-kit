# Agent Project Template Kit

A reusable kit for creating AI-agent coding projects from a lean, structured starting point.

This repository is designed to be shared, maintained, and reused. It contains:

- the tooling used to maintain and generate projects
- the starter project copied into each new project

## Repository structure

The repository has two layers:

1. **Root level:** Template maintenance and project generation
2. **`project_template/`:** The starter project payload copied into new projects

```text
agent-project-template-kit/
├── README.md                # Guide for maintaining and using this template repository
├── CLAUDE.md                # Instructions for agents working on the template repository itself
├── create_template_repo.py  # Generates a new project from project_template/
└── project_template/        # Complete starter payload copied into each generated project
    ├── README.md            # Starting README to customize for the generated project
    ├── CLAUDE.md            # Operating instructions for agents building the generated project
    ├── PROMPT_START.md      # Initial prompt for bootstrapping and pruning the generated project
    ├── docs/
    │   ├── design/          # Architecture, data model, and technical decisions
    │   ├── fixes/           # Outstanding bugs and defects
    │   ├── product/         # Product vision and scope
    │   ├── roadmap/         # Active workstream, future phases, and completed work
    │   └── workflow/        # Agent workflow and human handoffs
    ├── scripts/             # Scripts copied into generated projects
    └── templates/           # Reusable document templates for generated projects
```

### Root files versus project template files

The similarly named files serve different scopes:

- **Root `README.md`:** Explains how to use, maintain, and improve the shared template repository.
- **Root `CLAUDE.md`:** Guides agents modifying the template system, generator, or starter payload.
- **`project_template/README.md`:** Becomes the README of each generated project and must be customized during bootstrap.
- **`project_template/CLAUDE.md`:** Becomes the operating guide for agents implementing the generated project.

Changes at the root affect how the template repository is maintained.

Changes inside `project_template/` affect the default contents of future generated projects.

### Root-level responsibility

The repository root contains the files used to maintain and distribute the template.

- `create_template_repo.py` creates a new project from the contents of `project_template/`.
- `project_template/` contains the complete starter project copied to the destination folder.

### Starter project responsibility

The `project_template/` directory contains the files an AI coding agent uses when starting and operating a real project.

Key files include:

- `README.md` for project-level orientation
- `CLAUDE.md` for agent operating rules
- `PROMPT_START.md` for the initial project bootstrap
- `docs/` for roadmap, fixes, architecture, product, and workflow documentation
- `scripts/` for project-specific utility scripts
- `templates/` for reusable documentation templates

## Start a new project

From the repository root, run:

```bash
python create_template_repo.py ../my_new_project
```

This creates a new project folder using the contents of `project_template/`.

Then:

1. Open the generated project folder with your coding agent.
2. Read `CLAUDE.md`.
3. Use `PROMPT_START.md` to begin the bootstrap process.
4. Adapt and prune the generated structure before implementation.

> [!IMPORTANT]
> Do not build a real product directly inside this template repository. Generate a separate project folder first.

## What this repository is for

Use this repository to:

- share a reusable AI-agent coding template
- maintain and improve the template over time
- standardize project bootstrapping
- generate clean starting points for new projects
- reduce repeated setup work across projects
- support token-conscious agent workflows

## Maintenance scope

Work at the repository root when you want to:

- improve the template structure
- refine bootstrap instructions
- update project generation behavior
- improve reusable documentation
- keep the default starter lean and practical

Work inside `project_template/` when you want to change what future generated projects receive.

Work inside a generated project when you want to build a real product.

## Design principles

The template follows these principles:

- **Lean root documentation:** Keep entry-point files concise and direct.
- **One canonical place per concern:** Avoid duplicating the same information across files.
- **One active workstream:** Keep current execution focused in `docs/roadmap/current_feature.md`.
- **Explicit human-agent handoff:** Record actions requiring human input in `docs/workflow/human_handoff.md`.
- **Structured project memory:** Use roadmap, fixes, architecture, and decision files instead of relying on chat history.
- **Token-conscious operation:** Read narrowly, write concisely, and remove irrelevant context.

## Intentional over-provisioning

The starter template intentionally includes more files and folders than every project will need.

When a new project is generated, the first agent must:

1. understand the real project and its constraints
2. identify which template files and folders are useful
3. delete unnecessary template scaffolding
4. populate the retained core documentation
5. define the first active workstream
6. begin implementation only after the bootstrap is complete

Unused files should not be retained “just in case.”

Pruning unnecessary scaffolding:

- reduces token usage
- removes context noise
- improves repository navigation
- prevents stale documentation
- lowers long-term maintenance cost

## Typical workflow

```text
Maintain the template
        |
        v
Generate a new project
        |
        v
Understand the real project
        |
        v
Prune unnecessary scaffolding
        |
        v
Populate the core documentation
        |
        v
Define the first active workstream
        |
        v
Begin implementation
```

## Template maintenance rule

Changes made in a generated project do not automatically update this template.

When a reusable improvement is discovered:

1. validate it in the real project
2. confirm that it applies across projects
3. add the generalized improvement to `project_template/`
4. avoid copying project-specific assumptions into the shared template

The template should remain broad enough to reuse, but lean enough to operate efficiently.