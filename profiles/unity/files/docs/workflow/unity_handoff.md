# Unity Handoff

> How work is split between the agent (writes files) and the human/Editor for a
> Unity project. This is the Unity-specific working model; the reusable
> **task-card format lives once** in `human_handoff.md` — use that, don't copy
> it here. Keep this file lean.

---

## The model

- **Agent writes files directly:** C# scripts, content data, tests, docs.
- **The Editor does the rest:** scenes, prefabs, serialized references, package
  imports, cameras, lighting, UI, Input System, Build/Play.

The agent reaches the Editor two ways:

**1. Bridge-first — via MCP (preferred when running).** When a Unity MCP bridge
is connected, the agent can inspect the hierarchy and components, read the
Console, run menu items, and enter/exit **Play mode** directly — no human clicks.
A Blender bridge similarly drives the asset pipeline (text/image → 3D). Confirm
the bridge responds before relying on it.

**2. Task-card fallback (bridge off / not installed).** When no bridge is
connected — or the step needs a physical device, signing, or a store upload —
hand it to the human as an **editor/GUI task card**: numbered exact steps
(menu-path precise) → what to verify → report back. If `human_handoff.md` is
present it carries the full reusable template; don't restate it here.

> Check the bridge first. Drop to a task card only when it is unavailable.

---

## Enabling the bridges (optional)

These are **not** shipped as live config — a fresh project has neither bridge
installed. If you want the MCP path, install the corresponding package + bridge,
then add a project `.mcp.json` like:

```json
{
  "mcpServers": {
    "UnityMCP": { "type": "http", "url": "http://127.0.0.1:8080/mcp" },
    "BlenderMCP": { "command": "uvx", "args": ["blender-mcp"] }
  }
}
```

Adjust the port/command to match your install. Until a bridge is actually
running, use task cards.

---

## Notes

- If a change needs both a script edit and Editor wiring, the agent writes the
  script first, then issues the task card (or drives the bridge) referencing it.
- Prefer serialized references wired in the Editor over `Find`/`Resources.Load`.
- Keep `.meta` files committed with their assets.
