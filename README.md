# Agent Project Template Kit

A reusable kit for creating AI-agent coding projects from a lean, structured starting point.

The repository has two layers:

1. **Root level** — tooling to maintain the template and generate projects.
2. **`project_template/`** — the starter payload copied into each generated project.

```text
agent-project-template-kit/
├── README.md                # This guide: maintaining and using the kit
├── AGENTS.md                # Instructions for agents working on the kit itself
├── create_template_repo.py  # Generates a new project from project_template/
└── project_template/        # Starter payload copied into each generated project
    ├── README.md            # Starting README to customize per project
    ├── AGENTS.md            # Canonical operating instructions for generated projects
    ├── PROMPT_START.md      # Bootstrap prompt for a freshly generated project
    ├── .agent_shims/        # Tool-specific entrypoints promoted at generation time
    ├── docs/                # design / fixes / product / roadmap / workflow docs
    └── scripts/             # Scripts copied into generated projects
```

The similarly named root and template files serve different scopes:

- **Root `README.md` / `AGENTS.md`** govern the kit — how it is maintained and how generation behaves.
- **`project_template/README.md` / `AGENTS.md`** become the generated project's own files. `AGENTS.md` is its canonical operating guide; the README is customized during bootstrap.

## Canonical instructions and compatibility shims

`AGENTS.md` is the single canonical agent-instruction file. Optional tool-specific shims (`CLAUDE.md`, `GEMINI.md`) are thin entrypoints that point back to `AGENTS.md` instead of duplicating it. This keeps the template easy to maintain, portable between agents, and unlikely to drift across tools. Shims live in `project_template/.agent_shims/` and are promoted into the project root only when a matching profile is selected; the internal shim folder is never left in a generated project.

## Start a new project

From the repository root:

```bash
python create_template_repo.py ../my_new_project
python create_template_repo.py ../my_new_project --agent claude
python create_template_repo.py ../my_new_project --agent gemini
python create_template_repo.py ../my_new_project --agent multi-agent
python create_template_repo.py ../my_new_project --agent claude --minimal
```

### `--agent` — which entrypoints ship

| Profile | Result |
| --- | --- |
| `generic` (default) | `AGENTS.md` only, no tool-specific shims |
| `claude` | `AGENTS.md` + `CLAUDE.md` |
| `gemini` | `AGENTS.md` + `GEMINI.md` |
| `multi-agent` | `AGENTS.md` + every available shim |

### `--minimal` — for small projects

`--minimal` prunes the payload down to a lean core so small projects start with less to read and delete:

```text
.gitignore  README.md  AGENTS.md  PROMPT_START.md
docs/roadmap/current_feature.md  docs/roadmap/next_phase.md  docs/fixes/fixes_log.md
```

It deletes the `design/`, `product/`, `workflow/`, `roadmap/archive.md`, and `scripts/` scaffolding — files a small project would otherwise prune by hand. Any promoted agent shim is kept, so `--minimal` combines freely with `--agent`. Create those extra docs later, from their canonical description in `AGENTS.md`, if and when the project grows into them.

## After generation

Open the generated project with your coding agent, then:

1. Read `AGENTS.md` (or the tool-specific shim, if one was generated).
2. Read `PROMPT_START.md`.
3. Adapt and prune the structure before implementation.

### Supporting a newer agent convention

If a generated project uses an agent or repo-instruction convention this kit does not yet support, add the needed file directly in that project, following these rules:

- keep `AGENTS.md` as the canonical source of truth,
- make the new file a thin entrypoint whenever possible,
- avoid duplicating the full operating guide unless there is a strong tool-specific reason,
- add support in the generated project first, then upstream it here if it proves broadly useful.

> [!IMPORTANT]
> Do not build a real product inside this kit. Generate a separate project folder first.

## Working in the kit

Work **at the root** to improve the template structure, bootstrap instructions, generation behavior, or reusable docs. Work **inside `project_template/`** to change what future generated projects receive. Work **inside a generated project** to build a real product.

Improvements discovered while building a real project do not flow back automatically. When one proves reusable: validate it in the real project, confirm it generalizes, then add the generalized version to `project_template/` — without copying project-specific assumptions into the shared template.

## Design principles

- **Lean documentation** — keep entry-point files concise and direct.
- **One canonical place per concern** — record each fact once, in the file that owns it.
- **One active workstream** — keep current execution focused in `docs/roadmap/current_feature.md`.
- **Explicit human–agent handoff** — record actions needing a human in `docs/workflow/human_handoff.md`.
- **Structured project memory** — use roadmap, fixes, architecture, and decision files instead of chat history.
- **Token-conscious operation** — read narrowly, write concisely, prune irrelevant context.

The starter intentionally ships more than every project needs. The first agent on a generated project understands the real project, keeps and fills the useful files, and **deletes the rest** rather than retaining scaffolding "just in case" — which is exactly what `--minimal` does up front for projects known to be small.

## Typical workflow

```text
Maintain the template → Generate a project → Read AGENTS.md (or shim) →
Use PROMPT_START.md → Understand the real project → Prune scaffolding →
Populate core docs → Define the first workstream → Begin implementation
```
