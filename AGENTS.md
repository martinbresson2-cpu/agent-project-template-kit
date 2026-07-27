# Template Maintenance Guide

This file governs work in the template-maintenance repository.

This root repo is not a normal generated project.
Its job is to maintain the reusable starter project in `project_template/`.

---

## Session start

Read only what is needed for the current task.

Usually:
1. `README.md`
2. `create_template_repo.py` if generation behavior matters
3. the specific file in `project_template/` being changed

Do not start by reading the full template payload unless the task requires it.

---

## Working mode

Work here in template maintenance mode:

- improve reusable scaffolding
- keep docs generic and lean
- optimize for repeated future use
- avoid project-specific assumptions

If the goal is to start or bootstrap a real project, create a fresh copy from `project_template/` and work there instead.

---

## Repository roles

- root files support maintaining and generating the template
- `project_template/` contains the files that ship into a new project
- `project_template/.agent_shims/` contains tool-specific compatibility entrypoints, plus the `claude_home/` `.claude/` config seed, promoted during generation
- `profiles/` contains composable per-type overlays (`web`, `mobile`, `unity`, `python`); each is a `gitignore.append` and/or a `files/` tree applied by `--type`

Project-facing docs such as `README.md`, `AGENTS.md`, and `PROMPT_START.md` belong in `project_template/`.

---

## Canonical instructions and compatibility shims

This template uses:

- `AGENTS.md` as the canonical agent instruction file
- thin tool-specific shim files such as `CLAUDE.md` or `GEMINI.md` as compatibility entrypoints

Shim files must stay short and point back to `AGENTS.md` rather than duplicating the full operating guide.

When adding support for another coding agent:
1. confirm the convention is real and worth supporting,
2. prefer a thin root-level shim if possible,
3. add it under `project_template/.agent_shims/`,
4. update the generator only if the support is stable enough to justify maintenance cost,
5. avoid speculative or weakly supported integrations.

---

## When to use the generator

To start a new project from this template, run for example:

```bash
python create_template_repo.py ../my_new_project
python create_template_repo.py ../my_new_project --agent generic
python create_template_repo.py ../my_new_project --agent claude
python create_template_repo.py ../my_new_project --agent gemini
python create_template_repo.py ../my_new_project --agent multi-agent
python create_template_repo.py ../my_new_project --agent claude --minimal
python create_template_repo.py ../my_new_project --type python,web
```

`--agent` selects which entrypoint shims (and the `.claude/` seed) ship;
`--type` applies composable per-type overlays; `--minimal` prunes the payload to
a lean core for small projects. All three are orthogonal and combine freely.

When adding or changing a type overlay, keep it to what is *always* common to
that type: ignore rules and fill-in-the-blank prose (a stack-notes stub, a
workflow doc). **An overlay must never ship a live config with a tool,
framework, or port baked in** — that is a decision the project makes, not the
template. A `files/` tree is a standing invitation to add "one more helpful
default"; resist it. If an overlay encodes a real decision, it is too precise.

Then open the new project folder and follow its local:
- `AGENTS.md`
- the relevant tool-specific shim if one was generated
- `PROMPT_START.md`

Do not bootstrap `project_template/` in place as if it were the real project.

---

## Working rules

- Keep the template lean.
- Prefer the minimum reusable structure.
- Do not add files that many projects will immediately delete unless they clearly earn their cost.
- Avoid duplicating guidance between root docs and template docs.
- If a change affects generated projects, edit the files inside `project_template/`.
- Keep `AGENTS.md` as the single source of truth for agent instructions.
- Do not create full duplicated instruction files for each tool unless absolutely necessary.

---

## Definition of done

A template change is done when:
- the reusable structure is clearer or more useful,
- the generated project remains coherent,
- token cost stays reasonable,
- and the change improves repeated use of the template.