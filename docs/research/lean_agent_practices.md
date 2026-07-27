# Lean Thinking & AI-Agent Coding Practices — Research Report

*Scope: research into (A) lean at its source, (B) lean in software/docs, (C) best
practices for AI coding agents, (D) a project-type taxonomy — translated into
prioritized changes to this template kit. Written 2026-07-27.*

*Method note: primary/authoritative sources are cited inline. Where a claim rests
on a blog or aggregator it is flagged as weaker. Confidence is stated per
recommendation. The kit is evaluated impartially — cuts are proposed alongside
additions.*

---

## 1. Executive summary

1. **The kit's core philosophy is well-founded.** Lean-at-source, lean-software,
   and Anthropic's own context-engineering guidance all converge on the same
   thing the kit already encodes: minimize the token/inventory footprint, keep one
   canonical place per fact, limit work-in-progress to one stream, load context
   just-in-time. Change little at the level of *principle*.
2. **But the kit's headline slogan — "ship more than needed, prune later" —
   directly contradicts the strongest lean finding it cites.** Overproduction is
   the *root* waste in the Toyota system (it manufactures all the others), and
   pre-loading context is exactly what Anthropic warns against. Provisioning then
   pruning is push; lean is pull. This is the one place the kit's stated design
   fights its stated values.
3. **The lean resolution is "just-in-time," not "prune-later": default lean, add
   on demand from a canonical catalogue.** `--minimal` should arguably be the
   *default*, with the fuller payload available as an opt-in — because pruning is
   a cost that reliably gets skipped, while adding a named doc from `AGENTS.md`'s
   catalogue is cheap and happens exactly when the need is real.
4. **`export_project.py` is the clearest cut.** A 312-line "concatenate the repo
   into one text file to paste into an LLM" tool is shipped into *every* project,
   even `--minimal`. Modern coding agents read files directly and diff via git;
   this is inventory that no longer earns its carrying cost. High confidence.
5. **There is real duplication *inside the kit itself*** — session-start steps,
   prune rules, and the canonical-file list are restated across `AGENTS.md`,
   `PROMPT_START.md`, and `docs/workflow/agent_workflow.md`. That violates the
   kit's own "one canonical place" rule and is the highest-value tidy-up.
6. **`agent_workflow.md` is a self-described tombstone** ("Delete this file during
   bootstrap if `AGENTS.md` is enough"). A file whose own header tells you to
   delete it is scaffolding the reader must wade through. Fold its unique content
   into `AGENTS.md` and drop it.
7. **The `--type` overlay guardrail is exactly right and should be defended
   loudly.** "Only ignore-rules and fill-in-the-blank prose, never a live config
   with a baked-in tool/port" is the precise, evidence-backed line between "always
   common to the type" and "a project decision." Keep it; make it the documented
   contract for adding types.
8. **Do *not* adopt Diátaxis (or any product-doc taxonomy) for the doc tree.**
   Diátaxis organizes *end-user learning* material; the kit's docs are *operational
   agent memory* (state, decisions, handoffs). Different genre — stay flatter.
9. **The kit is, in agent terms, a "structured note-taking" system — and that is
   the single most validated pattern in current agent practice.** `current_feature.md`
   ≈ the recommended external `NOTES.md`; framing it that way (and keeping the
   session-start read-set tiny) is worth more than any new file.
10. **`AGENTS.md` as canonical + thin shims is now the industry-standard pattern**,
    formalized as an open spec and donated to the Linux Foundation. The kit picked
    the right convention; the main risk is the canonical file drifting *long*, not
    the shim strategy.

---

## 2. Findings by track

### Track A — Lean at its source (outside software)

**Toyota Production System (TPS).** Codified by Taiichi Ohno and Eiji Toyoda, TPS
aims to produce exactly what is needed, when needed, with minimum waste. Ohno's
taxonomy of *muda* (waste) is seven categories — overproduction, waiting,
transport, over-processing, inventory, motion, defects — later extended with an
eighth, unused human creativity. Critically, **overproduction is treated as the
worst waste because it generates the others** (excess inventory, extra motion,
hidden defects) ([Art of Lean — 7 Wastes](https://artoflean.com/reference/seven-wastes/);
[projectengineer.net](https://www.projectengineer.net/the-7-types-of-muda/)). TPS
also targets *mura* (unevenness) and *muri* (overburden) alongside muda. Its two
pillars are **just-in-time** (pull material only as consumed) and **jidoka**
("automation with a human touch" — stop the line the instant a defect appears)
([Toyota Forklifts / TPS](https://blog.toyota-forklifts.eu/toyota-production-system-principles-how-to-eliminate-waste-in-your-logistics);
[Symestic — two pillars](https://www.symestic.com/en-us/what-is/toyota-production-system)).
Supporting practices: *kaizen* (continuous small improvement), *genchi genbutsu*
("go and see" the real thing), *standardized work*, and the *5 Whys* for root cause.

**Lean Startup.** Eric Ries adapts lean to conditions of extreme uncertainty:
**build–measure–learn**, the **MVP** ("the fastest way to get through the
Build-Measure-Learn feedback loop with the minimum amount of effort" — Ries), and
**validated learning** ([leanstartup.co](https://leanstartup.co/the-lean-startup-online-course-with-eric-ries/)).
Agreement with manufacturing lean: both attack waste and shorten feedback loops.
Disagreement: manufacturing lean optimizes a *known, repeatable* process (variance
is the enemy); Lean Startup optimizes *learning* when the process/product is
unknown (variance is information). The mismatch matters for a scaffold: a template
is a repeatable process (favor standardized, minimal work), but each *generated
project* starts in Lean-Startup conditions (favor keeping options open).

**Adjacent complexity-cost ideas.**
- **YAGNI** ("You Aren't Gonna Need It") — don't build on speculation; the cost of
  a speculative feature is carried until (and often after) it's proven unneeded
  ([Fowler, *Yagni*](https://martinfowler.com/bliki/Yagni.html) — authoritative).
- **Essential vs accidental complexity** — Brooks divides difficulty into that
  *inherent* to the problem (essential) and that *we add ourselves* (accidental);
  removing accidental complexity is where tooling helps
  ([Brooks, *No Silver Bullet*, UNC TR 86-020](https://www.cs.unc.edu/techreports/86-020.pdf)
  — primary). Scaffolding a project doesn't need is accidental complexity.
- **"Worse is better"** — Gabriel argues implementation simplicity that ships and
  spreads beats a "correct," complete design that doesn't; priority order:
  simplicity > correctness > consistency > completeness
  ([Gabriel, *The Rise of Worse is Better*](https://www.jwz.org/doc/worse-is-better.html)
  — primary). A small scaffold that's actually used beats a complete one that's fought.
- **Theory of Constraints** — Goldratt: every system has ≥1 bottleneck; optimize
  the constraint, not everything ([TOC Institute](https://www.tocinstitute.org/theory-of-constraints.html)).
  For an agent, the binding constraint is the *attention/context budget* — so the
  scaffold should spend it only where it relieves that constraint.
- **Cost of inventory / WIP & option value of deciding late** — unfinished
  inventory is pure carrying cost; deferring a decision preserves option value
  *when* deferral is cheap. Note the tension the kit must resolve: option value
  argues for *not committing* (JIT add), **not** for provisioning-then-pruning
  (which is inventory you pay to carry *and* pay to remove).

**Implications for the kit.** The mapping to a documentation/scaffold is strong
for: overproduction-is-waste, JIT/pull, one-piece flow (→ one workstream),
standardized work (→ canonical file ownership), 5-Whys/genchi-genbutsu (→ read the
real file, don't assume). It maps *poorly* for: heavy statistical-variance
machinery (irrelevant), and any reading of "decide late" as "provision early."
**The honest conclusion: lean at source endorses almost everything the kit does
*except* its "ship extra, prune later" default, which is textbook overproduction.**

### Track B — Lean in software & documentation

**Lean software development.** Mary & Tom Poppendieck's seven principles:
*eliminate waste, amplify learning, decide as late as possible, deliver as fast as
possible, empower the team, build quality in, optimize the whole.* Their software
waste taxonomy — **partially-done work, extra features, relearning, handoffs, task
switching, delays, defects** — maps Ohno's seven onto knowledge work
([netsolutions summary](https://www.netsolutions.com/insights/7-principles-of-lean-software-development/);
Poppendieck, *Lean Software Development*, 2003). Two are directly relevant here:
**extra features** (≈ scaffolding a project won't use) and **relearning** (≈
context an agent must re-read because it's scattered).

**Lean/"just-enough" documentation & docs-as-code.**
- **ADRs** (Michael Nygard, 2011): capture *one* decision, why, and its
  consequences, in a lightweight 5-section note — "just enough" architecture
  history ([adr.github.io](https://adr.github.io/); [Nygard template](https://github.com/joelparkerhenderson/architecture-decision-record)).
  The kit's `docs/design/decisions.md` is the ADR idea in a single-file form.
- **README-driven development** (Tom Preston-Werner, 2010): write the README first
  to force clarity before code ([tom.preston-werner.com](https://tom.preston-werner.com/2010/08/23/readme-driven-development)).
  Mirrors the kit's bootstrap-before-code stance.
- **Docs-as-code / anti-rot**: keep docs *in the same commit* as the code they
  describe, treat stale docs as bugs, and **delete dead docs** because they
  actively mislead — "worse than no documentation"
  ([Google eng doc guide](https://github.com/google/styleguide/blob/gh-pages/docguide/best_practices.md)
  — authoritative; corroborated by multiple 2025–26 practitioner posts, individually weaker).

**Diátaxis.** Four documentation modes on two axes (action/knowledge ×
study/work): *tutorials, how-to guides, reference, explanation*; the cardinal sin
is mixing modes on one page ([diataxis.fr](https://diataxis.fr/);
[Canonical adoption](https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation)).
**Assessment:** Diátaxis governs *user-facing learning material*. The kit's docs
are operational agent memory — current state, decisions, bugs, handoffs — which is
none of the four Diátaxis modes. Adopting it would be a category error and would
*add* structure the kit is trying to avoid. Keep the doc tree flat and
purpose-named.

**Doc-specific waste** the kit should actively fight: duplication (same fact in
two files), staleness/rot, **tombstones** (resolved bugs / "this file may be
deleted" notes left in place), and "just-in-case" files. The kit already names
most of these — the gap is that it commits a couple of them itself (see §4).

**Implications for the kit.** The kit is squarely inside the "just-enough docs +
docs-as-code" tradition and its instinct to *delete* rather than archive is
correct and well-supported. The two improvements Track B suggests: (1) enforce
"one canonical place" *within the kit's own files* (it currently duplicates), and
(2) do **not** import Diátaxis — the flat, ownership-based tree is the right model
for agent memory.

### Track C — Best practices for AI coding agents

**The instruction-file convention.** `AGENTS.md` is now the cross-tool open
standard — "a README for agents": build/test commands, code style, conventions,
boundaries, "anything you'd tell a new teammate." It is plain Markdown with **no
required fields**, supports **nested files** (nearest wins — OpenAI's own monorepo
ships 88 of them), and is explicitly *complementary to* README (README for humans,
AGENTS for agents) ([agents.md](https://agents.md/)). It was formalized as an open
spec in Aug 2025 and donated to the Linux Foundation's Agentic AI Foundation in
Dec 2025, with 60k+ repos adopting it ([PRPM deep-dive](https://prpm.dev/blog/agents-md-deep-dive)
— secondary). **The kit's "AGENTS.md canonical + thin CLAUDE.md/GEMINI.md shims"
is exactly the emerging best practice.**

**Length/context discipline.** Claude Code's own guidance and community consensus:
keep `CLAUDE.md` **concise** — Anthropic's best-practices doc targets brevity, and
practitioners converge on "under ~200–300 lines," with HumanLayer running a root
file under 60 lines ([Claude Code best practices](https://code.claude.com/docs/en/best-practices);
[HumanLayer](https://www.humanlayer.dev/blog/writing-a-good-claude-md) — secondary).
Mechanism: **progressive disclosure** — keep the always-loaded file small; point to
detail files (with `file:line` references, not pasted code) that load only when
needed. The template `AGENTS.md` is 159 lines — inside the guidance, but with room
to tighten.

**Context engineering (Anthropic, primary).** "Context engineering is the art and
science of curating what will go into the limited context window." The goal is
**"the smallest possible set of high-signal tokens that maximize the likelihood of
some desired outcome."** LLMs have an **"attention budget"**; **context rot** means
recall degrades as tokens grow. Key techniques
([Anthropic — Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)):
- **Right altitude** for the system prompt: specific enough to guide, flexible
  enough not to be brittle. The template `AGENTS.md`'s "short and procedural,
  points to deeper docs" is precisely this.
- **Just-in-time retrieval**: hold lightweight references (paths/queries), load
  content at runtime — don't pre-load. Directly endorses the kit's "read narrowly,
  only what the task needs" session-start rule.
- **Tools should be surgical**; bloated tool sets create ambiguity.
- **Long-horizon**: *compaction*, ***structured note-taking*** (external
  `NOTES.md`-style memory persisted outside context), and *sub-agent architectures*
  with clean context returning condensed summaries.

**What good agent repos actually do** (synthesis): small always-on instruction
file; explicit build/test commands; a stated session-start routine; externalized,
structured memory for state/decisions; boundaries ("do not touch"); and pointers
rather than inlined detail. **Anti-patterns**: instruction bloat, contradictory
guidance across files, pasted code blocks, "just-in-case" sections, and docs that
go stale because nothing keeps them honest.

**Implications for the kit.** The kit is *already* an implementation of Anthropic's
long-horizon playbook: `current_feature.md`/`fixes_log.md`/`decisions.md` **are**
structured note-taking; the tiny session-start read-set **is** JIT context; one
workstream **is** WIP-limiting. The highest-leverage moves are therefore not new
files but: (a) name the pattern (so agents treat these files as their memory, not
paperwork), (b) kill internal duplication that inflates the always-read set, and
(c) resist the provisioning instinct that fights the token economy.

### Track D — Project-type taxonomy

The crux for `--type`: **what is *always* true of a type (safe to seed) vs. what is
a per-project decision (must not seed).** The reliable "always-true" surface is
narrow — essentially **(1) the VCS-ignore set** and **(2) the shape of the
agent/human handoff** — while build/run/test *commands*, framework, and structure
are project decisions. GitHub's canonical `github/gitignore` collection is the
authoritative anchor for (1) ([github/gitignore](https://github.com/github/gitignore)).

Survey (near-universal-to-type in **bold**, project-decision in *italics*):

| Type | Always-common ignores (seed) | Doc(s) that always help | Build/run/test shape | Handoff quirk |
|---|---|---|---|---|
| Web app / SPA | **`node_modules/`, build dir (`dist/`,`.next/`), `.env*`** | stack-notes stub | *bundler/framework*; dev-server + test runner | browser/manual UI check |
| Backend API/service | **`.env*`, build/artifact dirs, logs** | stack-notes; API surface | *framework*; run server + integration tests | secrets, migrations, deploy |
| Mobile | **`build/`, Pods/`.gradle`, signing files, `*.keystore`** | stack-notes | *native/RN/Flutter* | **device/simulator test + signing** |
| Desktop | **build dir, packaged installers** | stack-notes | *framework* | code-signing, per-OS test |
| Game engine (Unity/Godot/Unreal) | **`Library/`,`Temp/`,`.godot/`,`Binaries/`,`Intermediate/`** | stack-notes + **engine handoff** | *engine* | **editor GUI: scenes/prefabs; keep `.meta`** |
| CLI tool | **lang build/cache dirs** | stack-notes | *lang* | usually none |
| Library/package | **build/dist, coverage** | stack-notes; **public API** | *lang*; test + **publish** | registry publish is human |
| Data / ML / notebooks | **`.ipynb_checkpoints/`, data/model artifacts, `.env*`** | stack-notes | *stack*; notebook + pipeline | **notebook exec + large data/GPU** |
| Infra-as-code / DevOps | **`.terraform/`,`*.tfstate`, kube/secrets, `.env*`** | stack-notes | *tool*; plan/validate | **apply = privileged human action** |
| Browser extension | **build dir, packaged `.zip`** | stack-notes | *framework* | **store review/upload** |
| Embedded / firmware | **build/`.pio/`, toolchain output** | stack-notes | *toolchain* | **flash to hardware** |

**Findings:** (1) Every row's *safe* seed reduces to **ignore rules + a fill-in
stack stub**, exactly the kit's overlay contract — strong external validation of
the guardrail. (2) The one recurring *type-specific* payload beyond ignores is a
**handoff doc**, and only where the loop is unusual: **engine editors, on-device
testing, notebook execution, IaC apply, store review**. Unity already has this; by
the evidence, *mobile*, *data/ML*, and *IaC* are the next-best handoff-doc
candidates — and Godot/Unreal would share Unity's. (3) `.gitignore` fragments in
the kit *duplicate* `github/gitignore`, so they carry a small staleness risk.

**Implications for the kit.** The four current types (web/mobile/unity/python) are
a reasonable but slightly arbitrary cut that **mixes two axes** — *language*
(python) and *platform* (web/mobile/unity). Document that overlays compose across
axes (lang × platform) and that **the only two things an overlay may add are
ignore rules and a fill-in doc (stack stub and/or handoff)**. Expansion, if any,
should be handoff-driven (godot, iac, data) — not framework-driven.

---

## 3. Principles distilled (the guardrails the kit should encode)

1. **Overproduction is the primary waste.** Prefer *not shipping* a file over
   shipping-to-prune. (TPS; Poppendieck "extra features"; Anthropic token economy.)
2. **Pull, not push — just-in-time over just-in-case.** Add a doc from a canonical
   catalogue when the need is real; don't pre-provision and hope for a prune.
3. **Smallest set of high-signal tokens.** Every always-loaded line competes for
   the attention budget. (Anthropic.)
4. **One canonical place per fact — including inside the kit's own files.** No fact
   restated in two files. (DRY; anti-rot; the kit's own rule.)
5. **Right altitude.** Operating guide is short and procedural, points to detail;
   detail loads on demand. (Anthropic; progressive disclosure.)
6. **One active workstream (limit WIP).** Single-piece flow; optimize the
   constraint = attention. (TPS; Goldratt.)
7. **Externalize memory as structured notes.** Roadmap/fixes/decisions files *are*
   the agent's memory, not bureaucracy. (Anthropic structured note-taking.)
8. **Delete, don't archive; no tombstones.** Stale/dead docs mislead and are worse
   than none. (Docs-as-code anti-rot.)
9. **Seed only what is always true of a type: ignores + fill-in prose. Never a
   live config with a baked-in tool/port.** (Track D; the kit's existing contract.)
10. **AGENTS.md canonical; tool files are thin shims.** (agents.md open standard.)

---

## 4. Recommendations for the kit (prioritized)

Legend — **Effort:** S/M/L. **Confidence:** H/M/L.

| # | Recommendation | Rationale (source) | Touches | Type | Effort | Conf |
|---|---|---|---|---|---|---|
| 1 | **De-duplicate the always-read instruction set.** Make `AGENTS.md` the *only* home for session-start steps, prune rules, and the canonical-file list; have `PROMPT_START.md` and `agent_workflow.md` reference rather than restate them. | Same facts appear in ≥2 files today, violating the kit's own "one canonical place" and inflating the attention budget (Anthropic; DRY/anti-rot). | `AGENTS.md`, `PROMPT_START.md`, `agent_workflow.md` | change/cut | M | H |
| 2 | **Cut `agent_workflow.md`;** fold its few unique lines (verify/slice discipline) into `AGENTS.md`. | Its own header says delete it if `AGENTS.md` suffices — a self-tombstone; it largely restates `AGENTS.md` (extra-features + relearning waste). | `docs/workflow/agent_workflow.md`, `AGENTS.md`, generator `MINIMAL_KEEP` | cut | S | H |
| 3 | **Cut `export_project.py` from the default payload** (offer as an optional kit-root tool if wanted at all). | A 312-line repo→single-text-file "paste into an LLM" tool is obsolete for agents that read files directly and use git; it ships even under `--minimal`. Overproduction/YAGNI (TPS; Fowler). | `project_template/scripts/`, generator `MINIMAL_KEEP_PATHS`, README | cut | S | M‑H |
| 4 | **Reframe, don't just relax, the headline philosophy: default lean + add-on-demand from a catalogue, instead of "ship extra, prune later."** Consider making `--minimal` behavior the default and a `--full` opt-in. | "Ship-to-prune" is push/overproduction; the prune reliably gets skipped, so the waste persists. JIT-add is the lean resolution and matches Anthropic's JIT context. (TPS; Poppendieck; Anthropic.) | root `README.md`, `AGENTS.md` philosophy, `PROMPT_START.md`, generator defaults | change | M | M‑H |
| 5 | **Name the memory pattern.** State in `AGENTS.md` that `current_feature.md`/`fixes_log.md`/`decisions.md` are the agent's *structured external memory*, read first and written last each session. | Anthropic's most-endorsed long-horizon technique; framing changes agent behavior at ~zero token cost. | `AGENTS.md` | change | S | H |
| 6 | **Codify the overlay contract** in `AGENTS.md`/README: an overlay may add **only** (a) `.gitignore` rules and (b) fill-in prose (stack stub / handoff). No baked tool, framework, port, or live config. | This is precisely Track D's "always-common vs project-decision" line; make the guardrail explicit for future type authors. (Track D; github/gitignore.) | root `AGENTS.md`, README, `profiles/` note | change | S | H |
| 7 | **Reduce `.gitignore`-fragment staleness:** trim overlay fragments to the stable core and point to `github/gitignore` as the source of truth for the long tail. | Fragments duplicate a canonical, maintained upstream (anti-rot; single source of truth). | `profiles/*/gitignore.append` | change | S | M |
| 8 | **Add handoff docs only where the loop is genuinely unusual** — candidates: mobile (device/signing), data/ML (notebook/GPU), IaC (privileged apply); Godot/Unreal reuse Unity's. Do *not* add stack-only overlays for types that need nothing but ignores. | Track D shows the handoff doc is the one recurring type-specific payload; everything else is a project decision. | `profiles/<type>/files/docs/workflow/` | add (selective) | M | M |
| 9 | **Tighten `AGENTS.md` toward the short end** (~100–130 lines) via #1–#2; keep it procedural + pointer-based. | Length guidance + progressive disclosure (Claude Code best practices; HumanLayer). Currently 159 lines with duplicated content. | `AGENTS.md` | change | S | M |
| 10 | **Do NOT adopt Diátaxis** or restructure the doc tree into tutorials/how-to/reference/explanation. | Diátaxis is for user learning material; the kit's docs are operational memory — a category mismatch that would add structure without value. (diataxis.fr.) | — (decision to hold) | keep | — | M‑H |
| 11 | **Keep** the `--type` composability, the `--agent` shim model, and the `.claude/settings.json` seed. | All three match current best practice (agents.md standard; composable = lang×platform per Track D; the seed is small, read-only, and gated behind `--agent claude`). | — | keep | — | H |

---

## 5. Open questions / trade-offs for a human decision

- **Default lean vs. discoverability (Rec #4).** Making `--minimal` the default is
  the lean-correct move, but a fuller default *shows* new users what structure is
  available. Mitigation: keep the full catalogue *described* in `AGENTS.md` even
  when files aren't shipped, so JIT-add is a copy-from-catalogue, not an invention.
  Decision needed: flip the default, or keep full default and market `--minimal` harder?
- **Is `export_project.py` truly dead (Rec #3)?** It's obsolete for an agent with
  filesystem access, but retains niche value for pasting a repo into a *chat* UI
  with no tools. Keep as an optional root-level utility, or remove entirely?
- **How far to grow `--type`?** More types = more maintenance and more arbitrary
  language×platform cells. Hold to handoff-driven additions, or let it stay at four
  and document composition instead?
- **Nested `AGENTS.md` for larger generated projects** (monorepo pattern from the
  standard) is unaddressed. Worth a one-line note in `AGENTS.md`, or out of scope
  for a starter kit?
- **Source-disagreement flag:** the "<200–300 line" `CLAUDE.md` figure is
  community consensus, not a hard Anthropic number (their doc says "concise"
  without a line count). Treat as a heuristic, not a rule.

---

## 6. Sources

**Track A — lean at source**
- Art of Lean, *The Seven Wastes* — https://artoflean.com/reference/seven-wastes/
- ProjectEngineer, *The 7 Types of Muda* — https://www.projectengineer.net/the-7-types-of-muda/
- Toyota Forklifts, *TPS principles* — https://blog.toyota-forklifts.eu/toyota-production-system-principles-how-to-eliminate-waste-in-your-logistics
- Symestic, *TPS: two pillars* — https://www.symestic.com/en-us/what-is/toyota-production-system
- Lean Startup (Ries), official course — https://leanstartup.co/the-lean-startup-online-course-with-eric-ries/
- Fowler, *Yagni* — https://martinfowler.com/bliki/Yagni.html
- Brooks, *No Silver Bullet* (UNC TR 86-020, primary) — https://www.cs.unc.edu/techreports/86-020.pdf
- Gabriel, *The Rise of Worse is Better* (primary) — https://www.jwz.org/doc/worse-is-better.html
- Theory of Constraints Institute — https://www.tocinstitute.org/theory-of-constraints.html

**Track B — lean in software & docs**
- Poppendieck 7 principles (summary) — https://www.netsolutions.com/insights/7-principles-of-lean-software-development/
- ADRs — https://adr.github.io/ ; Nygard template — https://github.com/joelparkerhenderson/architecture-decision-record
- Preston-Werner, *README-Driven Development* — https://tom.preston-werner.com/2010/08/23/readme-driven-development
- Google engineering doc guide — https://github.com/google/styleguide/blob/gh-pages/docguide/best_practices.md
- Diátaxis — https://diataxis.fr/ ; Canonical adoption — https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation

**Track C — AI coding agents**
- AGENTS.md standard — https://agents.md/
- agents.md deep-dive (history/adoption, secondary) — https://prpm.dev/blog/agents-md-deep-dive
- Anthropic, *Effective context engineering for AI agents* (primary) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Claude Code best practices — https://code.claude.com/docs/en/best-practices
- HumanLayer, *Writing a good CLAUDE.md* (secondary) — https://www.humanlayer.dev/blog/writing-a-good-claude-md

**Track D — project-type taxonomy**
- github/gitignore (canonical templates) — https://github.com/github/gitignore
- Unity.gitignore — https://github.com/github/gitignore/blob/main/Unity.gitignore
- Godot.gitignore — https://github.com/github/gitignore/blob/main/Godot.gitignore
- github/gitignore game-engine templates (DeepWiki, secondary) — https://deepwiki.com/github/gitignore/6.4-game-development-engines
