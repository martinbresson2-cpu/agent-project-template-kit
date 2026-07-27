# Stack Notes — Web App

> Type-level facts common to a web app. Fill in the blanks for this project.
> Project-specific structure and boundaries live in `architecture.md`;
> this file just captures the stack and the everyday commands.

---

## Stack

- **Framework:** `<Next.js / Vite + React / SvelteKit / …>`
- **Language:** `<TypeScript / JavaScript>`
- **Package manager:** `<npm / pnpm / yarn>`
- **Styling:** `<Tailwind / CSS modules / …>`
- **Backend/API:** `<same app / separate service / none>`
- **Data:** `<Postgres / SQLite / external API / none>`

## Everyday commands

- Install: `<npm install>`
- Run dev server: `<npm run dev>`
- Build: `<npm run build>`
- Test: `<npm test>`
- Lint / typecheck: `<npm run lint>` / `<tsc --noEmit>`

## Layout (typical)

    src/            application code
    public/         static assets
    tests/ or e2e/  tests

## Common gotchas

- Keep secrets in `.env.local` (git-ignored) — never commit real keys.
- Distinguish server-only vs client-exposed env vars.
- Keep generated build output (`dist/`, `.next/`) out of source control.

## Verify a change

- Dev server renders the affected route without console errors.
- Typecheck and lint pass.
- Relevant unit/e2e tests pass.
