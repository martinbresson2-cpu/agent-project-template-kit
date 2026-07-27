# First Prompt for New Projects Based on This Template

Use this prompt when starting a brand-new project from this template.

---

You are working in a new project that was created from a generic AI-agent coding template.

Your job is to bootstrap the project correctly before writing much code.

## Your goals

1. Understand the actual project I want to build.
2. Adapt this template to the project.
3. Delete template files/folders that are not needed.
4. Fill in the important core docs.
5. Propose the first milestone and the first active feature.
6. Only then begin implementation.

## Very important template rule

This template intentionally contains **more files and folders than the project may need**.

You must actively prune it.

Do not keep unnecessary template files "for later" unless there is a strong reason.
Reducing irrelevant files saves tokens and keeps the repo easier to operate.

If you are unsure whether something is needed:
- ask,
- or keep it temporarily but explicitly mark it as provisional and list it for review.

## First tasks

Please do the following in order:

### 1. Read only the minimum required files
Start with:
- `README.md`
- `AGENTS.md`
- `docs/roadmap/current_feature.md`
- `docs/roadmap/next_phase.md`

Then stop and ask me the minimum set of questions needed to understand:
- what the project is,
- what kind of output/product it should become,
- whether there are technical constraints,
- whether there is existing code/content to integrate,
- what files/folders from the template are probably unnecessary.

Do not start broad repo reading at this stage.

### 2. Clarify the project
From my answers, establish:
- project purpose
- scope
- likely architecture shape
- likely workflow shape
- what parts of the template are useful vs unnecessary

### 3. Prune the template
Once the project is understood:
- propose a list of files/folders to delete,
- delete them after confirmation, or directly if they are clearly irrelevant and low-risk,
- keep the structure lean.

### 4. Fill the core files
Create or update at least:
- `README.md`
- `AGENTS.md`
- `docs/roadmap/current_feature.md`
- `docs/roadmap/next_phase.md`
- `docs/fixes/fixes_log.md`

Also update these if relevant:
- `docs/design/architecture.md`
- `docs/design/decisions.md`
- `docs/product/vision.md`
- `docs/product/scope.md`
- `docs/workflow/human_handoff.md`

### 5. Establish the first execution plan
Define:
- the current active feature/workstream
- the next milestone(s)
- known open questions
- what not to work on yet

### 6. Then begin implementation
Only after the above is done should you begin coding.

## Working style requirements

- Be concise.
- Read narrowly.
- Avoid duplicating information across docs.
- Put each fact in its canonical file.
- Ask before making product or UX decisions that are not obvious.
- Do not mark anything as shipped without explicit signoff.

## Expected output from your first pass

After the bootstrap pass, I want:
- a cleaned project structure,
- core docs populated,
- a clear current feature,
- a clear next-phase roadmap,
- and a short explanation of what you kept, what you deleted, and why.