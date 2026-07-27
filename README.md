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
├── AGENTS.md                # Instructions for agents working on the template repository itself
├── create_template_repo.py  # Generates a new project from project_template/
└── project_template/        # Complete starter payload copied into each generated project
    ├── README.md            # Starting README to customize for the generated project
    ├── AGENTS.md            # Canonical operating instructions for generated projects
    ├── PROMPT_START.md      # Initial prompt for bootstrapping and pruning the generated project
    ├── .agent_shims/        # Internal tool-specific compatibility files promoted at generation time
    ├── docs/
    │   ├── design/          # Architecture, data model, and technical decisions
    │   ├── fixes/           # Outstanding bugs and defects
    │   ├── product/         # Product vision and scope
    │   ├── roadmap/         # Active workstream, future phases, and completed work
    │   └── workflow/        # Agent workflow and human handoffs
    └── scripts/             # Scripts copied into generated projects
```

### Root files versus project template files

The similarly named files serve different scopes:

- **Root `README.md`:** Explains how to use, maintain, and improve the shared template repository.
- **Root `AGENTS.md`:** Guides agents modifying the template system, generator, or starter payload.
- **`project_template/README.md`:** Becomes the README of each generated project and must be customized during bootstrap.
- **`project_template/AGENTS.md`:** Becomes the canonical operating guide for agents implementing the generated project.

Changes at the root affect how the template repository is maintained.

Changes inside `project_template/` affect the default contents of future generated projects.

## Canonical agent instructions and supported shims

This template uses:

- **`AGENTS.md`** as the canonical agent instruction file
- optional tool-specific shim files as compatibility entrypoints

### Currently supported compatibility shims

The generator currently supports these agent profiles:

- **`generic`** — generates the project with `AGENTS.md` only
- **`claude`** — generates the project with `AGENTS.md` and `CLAUDE.md`
- **`gemini`** — generates the project with `AGENTS.md` and `GEMINI.md`
- **`multi-agent`** — generates the project with `AGENTS.md` and all currently available shim files

### Supported shim files today

- `CLAUDE.md`
- `GEMINI.md`

These shim files are intentionally short and point back to `AGENTS.md` rather than duplicating full operating instructions.

This keeps the template:

- easier to maintain
- less likely to drift across tools
- more portable between coding agents

## Start a new project

From the repository root, run one of the following:

```bash
python create_template_repo.py ../my_new_project
python create_template_repo.py ../my_new_project --agent claude
python create_template_repo.py ../my_new_project --agent gemini
python create_template_repo.py ../my_new_project --agent multi-agent
```

### What each option does

- **Default / `--agent generic`**
  - Creates a new project with the canonical `AGENTS.md`
  - Does not add tool-specific root shim files

- **`--agent claude`**
  - Creates a new project with `AGENTS.md`
  - Adds `CLAUDE.md` as a compatibility entrypoint

- **`--agent gemini`**
  - Creates a new project with `AGENTS.md`
  - Adds `GEMINI.md` as a compatibility entrypoint

- **`--agent multi-agent`**
  - Creates a new project with `AGENTS.md`
  - Adds all currently available root-level shim files

Tool-specific shim files are stored in `project_template/.agent_shims/` and are promoted into the generated project root only when needed. The internal shim folder should not remain in the final generated project.

## After generation

Open the generated project folder with your coding agent, then:

1. Read `AGENTS.md`, or the relevant tool-specific shim if one was generated
2. Read `PROMPT_START.md`
3. Adapt and prune the generated structure before implementation

### If your coding agent supports something newer than this template currently provides

If the generated project is being used with a coding agent or repo-instruction convention not yet supported here, the agent or human may add the needed compatibility file(s) directly inside the generated project.

Rules for doing that:

- keep `AGENTS.md` as the canonical source of truth
- make new compatibility files thin entrypoints whenever possible
- avoid duplicating the full operating guide unless there is a strong tool-specific reason
- prefer adding new support in the generated project first, then upstreaming it to this template if it proves broadly useful

If a new compatibility convention becomes reliably useful across projects, it should later be added back to this template in a generalized way.

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
Read AGENTS.md or selected shim
        |
        v
Use PROMPT_START.md
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