# Stack Notes — Unity Game

> Type-level facts common to a Unity project. Fill in the blanks. Game design
> and system-specific structure live in `architecture.md` (or a GDD); this file
> captures the engine setup and the agent/editor working model.

---

## Stack

- **Engine:** Unity `<6.x>` (`<URP / HDRP / Built-in>`)
- **Perspective:** `<2D / top-down 3D / first-person / …>`
- **Language:** C# (`<.NET / Mono>`)
- **Input:** `<Input System / legacy>`
- **Data:** `<ScriptableObjects / JSON in StreamingAssets / …>`

## Working model

The agent writes files (C#, data, tests, docs); the Editor (via a human or an
MCP bridge) does scenes, prefabs, wiring, and Play. The full model — bridge-first
vs task-card fallback, and how to enable the optional Unity/Blender bridges —
lives in `docs/workflow/unity_handoff.md`. Don't restate it here.

## Common gotchas

- Keep `Library/`, `Temp/`, `*.csproj`, `*.sln` out of source control
  (the type `.gitignore` fragment handles this).
- `.meta` files matter — commit them alongside their assets.
- Greybox first: mechanics before art unless a milestone calls for real assets.

## Verify a change

- Project compiles in the Editor with no console errors.
- The affected system behaves as expected in Play mode (human-reported).
