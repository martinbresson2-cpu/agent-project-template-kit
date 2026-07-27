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

Project-facing docs such as `README.md`, `CLAUDE.md`, and `PROMPT_START.md` belong in `project_template/`.

---

## When to use the generator

To start a new project from this template, run:

    python create_template_repo.py ../my_new_project

Then open the new project folder and follow its local:
- `CLAUDE.md`
- `PROMPT_START.md`

Do not bootstrap `project_template/` in place as if it were the real project.

---

## Working rules

- Keep the template lean.
- Prefer the minimum reusable structure.
- Do not add files that many projects will immediately delete unless they clearly earn their cost.
- Avoid duplicating guidance between root docs and template docs.
- If a change affects generated projects, edit the files inside `project_template/`.

---

## Definition of done

A template change is done when:
- the reusable structure is clearer or more useful,
- the generated project remains coherent,
- token cost stays reasonable,
- and the change improves repeated use of the template.