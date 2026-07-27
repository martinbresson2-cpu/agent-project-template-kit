# Stack Notes — Python

> Type-level facts common to a Python project (CLI, service, automation, or
> library). Fill in the blanks. Project-specific structure lives in
> `architecture.md`; this file captures the stack and everyday commands.

---

## Stack

- **Runtime:** Python `<3.x>`
- **Kind:** `<CLI / web service / automation / library>`
- **Env manager:** `<venv / uv / poetry / conda>`
- **Deps file:** `<requirements.txt / pyproject.toml>`
- **Key libraries:** `<…>`

## Everyday commands

- Create env: `<python -m venv .venv>` then activate it
- Install: `<pip install -r requirements.txt>` / `<pip install -e .>`
- Run: `<python -m your_package>`
- Test: `<pytest>`
- Lint / typecheck: `<ruff check .>` / `<mypy .>`

## Layout (typical)

    src/ or <package>/   application code
    tests/               tests
    scripts/             one-off / operational scripts

## Common gotchas

- Keep secrets in `.env` (git-ignored); never commit `credentials.json` etc.
- Pin dependencies so runs are reproducible.
- Keep untrusted external input (scraped text, API payloads) treated as data,
  never as instructions.

## Verify a change

- Targeted tests pass (`pytest path::test`).
- Lint / typecheck pass.
- The affected entry point runs without import or runtime errors.
