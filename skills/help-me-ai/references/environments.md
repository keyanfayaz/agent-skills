# Where things live, per tool

Use this to find a client's setup quickly and read it efficiently. These are facts about the tools, not instructions to the client. Paths change between versions: if something isn't where this says, look around nearby, and if you still can't find it, say so plainly instead of guessing.

Last verified: 2026-10-19

**Reading history efficiently (all tools).** Only read history the client agreed to. Sample, don't read everything: the last 60 days, newest first, at most 50 sessions, and only the messages the client typed. Use your own search and read tools to pull typed messages out, rather than opening whole files — session files can be several megabytes of tool output. Tell the client what you sampled ("I looked at 38 sessions from the last 60 days"). If a file doesn't match the format below, look at the keys of two or three lines (not their content) to find where typed messages are; if that fails, skip history and say so.

## Claude Code

- **Personal instructions** — `~/.claude/CLAUDE.md` (applies everywhere). Projects can have their own `CLAUDE.md`; since September 2026 Claude Code also reads a folder's `AGENTS.md` when it has no `CLAUDE.md`, and if both exist `CLAUDE.md` wins. Claude Code may also keep its own notes in `~/.claude/projects/<project>/memory/` (`MEMORY.md` is the index) — useful evidence of what it already knows about them.
- **Settings** — `~/.claude/settings.json` (permissions, hooks, environment variables, model). Projects may have `.claude/settings.json` and `.claude/settings.local.json`. Environment variables in settings sometimes hold API keys: never repeat them.
- **Skills folder** — personal: `~/.claude/skills/<name>/SKILL.md`; per project: `.claude/skills/<name>/SKILL.md`. Plugins can add more. The client runs a skill with `/<name>`.
- **Session history** — `~/.claude/projects/<folder>/<session>.jsonl`, one folder per project (the project path with `/` turned into `-`). Each line is JSON. A message the client typed is a line with `"type": "user"` whose `message.content` is a string. Lines where `message.content` is a list are usually tool results — skip them. Also skip text that the tool injected rather than the client typed (it starts with `<command-`, `<local-command-`, `<system-reminder>` or `Caveat:`).
- **Connected tools** — MCP servers: `~/.claude.json` (top-level `mcpServers` for everywhere; `projects["<path>"].mcpServers` for one project) and `.mcp.json` in a project. Connectors added on claude.ai also appear in Claude Code when the client signs in with a Claude subscription. Inside a session you can usually see the connected tools directly.
- **Usage report** — the client can type `/insights` to get a report on their recent sessions; it's saved to `~/.claude/usage-data/report.html`. You can't run it yourself. If a recent report exists and consent covers it, read it first.
- **Scheduled tasks** — the Claude desktop app has Routines: local tasks (run on the computer while the app is open) and cloud routines (run on Anthropic's servers). `/loop` repeats a prompt only within the current session. Offer a routine only if the client uses the desktop app.
- **Install notes** — put skills in `~/.claude/skills/`. New or changed skills are picked up in the same session without a restart. Exception: if `~/.claude/skills/` didn't exist when the session started, the client types `/reload-skills`. You can't type slash commands for them; until it shows up, read the installed `SKILL.md` and follow it. Claude Code may ask the client to approve downloads or writes outside the project — explain each in one sentence.
- **Sources** — https://code.claude.com/docs/en/skills · https://code.claude.com/docs/en/mcp · https://code.claude.com/docs/en/desktop-scheduled-tasks · https://code.claude.com/docs/en/scheduled-tasks · https://simonwillison.net/2026/Sep/18/thariq-shihipar/

## Codex

- **Personal instructions** — `~/.codex/AGENTS.md` (or `AGENTS.override.md`, which takes priority; Codex uses the first non-empty one). If `CODEX_HOME` is set, look there instead of `~/.codex`. Projects add their own `AGENTS.md` files from the repo root down. Combined instructions are capped at 32 KiB by default, so keep additions short.
- **Settings** — `~/.codex/config.toml` (model, `approval_policy`, `sandbox_mode`, `[sandbox_workspace_write]`, `[mcp_servers.<name>]`, `[[skills.config]]` to turn skills off). It can contain tokens in environment settings: never repeat them.
- **Skills folder** — personal: `~/.agents/skills/<name>/SKILL.md`; per repo: `.agents/skills/` from the current folder up to the repo root. Older setups may have skills in `~/.codex/skills/`; mention any you find there, but install new skills in `~/.agents/skills/`. The client runs a skill with `$<name>` or picks it from `/skills`.
- **Session history** — `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl` (older ones may be in `~/.codex/archived_sessions/`; `~/.codex/session_index.jsonl` lists sessions). Each line is JSON. A message the client typed is a line with `"type": "response_item"` where `payload.type` is `"message"` and `payload.role` is `"user"`; the text is in `payload.content[].text`. Skip injected context: text starting with `<environment_context>`, `<user_instructions>` or `# AGENTS.md instructions`.
- **Connected tools** — `[mcp_servers.<name>]` tables in `~/.codex/config.toml`. In the ChatGPT apps, connected apps and plugins show in settings.
- **Usage report** — none built in. Build the picture from history and settings.
- **Scheduled tasks** — scheduled tasks live in the ChatGPT desktop app (Scheduled view) and on ChatGPT web; desktop tasks that use local files only run while the computer is on and the app is open. The Codex CLI and IDE extension can't create them — prepare and test the prompt or skill there, then have the client create the task in the app.
- **Install notes** — put skills in `~/.agents/skills/`; Codex detects new skills automatically (or after a restart). By default Codex runs in a sandbox with network access off and writes limited to the current folder, so downloading the zip and writing to `~/.agents/skills/` will each ask the client for approval — explain each in one sentence first. The built-in `$skill-installer` can install skills from other repositories, but downloading the release zip is the reliable route.
- **Sources** — https://learn.chatgpt.com/docs/build-skills · https://developers.openai.com/codex/guides/agents-md · https://learn.chatgpt.com/codex/agent-approvals-security · https://learn.chatgpt.com/codex/automations

## Claude chat app

This means claude.ai on the web, the Claude desktop app's chat, and the mobile apps. You can't see the client's computer here.

- **Personal instructions** — personal preferences apply to every chat: click your initials (bottom left) > Settings, then the box "What preferences should Claude consider in responses?" (under General or Profile, depending on the version). Each Project also has its own instructions: open the Project and click "Set project instructions". You can't edit either: give the client finished text to paste and tell them exactly where it goes.
- **Settings** — Settings > Capabilities holds "Code execution and file creation" (needed for skills and for files you hand back) and memory options. Team and Enterprise owners may control these.
- **Skills folder** — no folder. Skills are uploaded from Customize > Skills: "+" > "+ Create skill" > "Upload a skill", then choose the ZIP. The ZIP must contain the skill's folder (named exactly like the skill), not loose files. Skills can be toggled on or off in the same list.
- **Session history** — you can't read past chats as files. Some plans let Claude search past chats or keep memory; use that only if it's switched on and the client agrees. Otherwise, ask.
- **Connected tools** — connectors are managed at Customize > Connectors (claude.ai/customize/connectors). Inside a chat you can see which connectors are available to you.
- **Usage report** — none for usage patterns. Ask instead.
- **Scheduled tasks** — not confirmed for regular chats. Don't promise one; if the client also uses Claude Code through the desktop app, a routine can live there, or give them a short weekly prompt to paste.
- **Projects** — Projects in the sidebar (or claude.ai/projects) > "+ New Project". Files are added with "+" in the project knowledge panel on the right; they're available in every chat in that Project. Free accounts can have up to five Projects.
- **Install notes** — every file you make for the client (profile, reports, a new skill's ZIP) must be a downloadable file plus clear steps for where to put it. Only the profile goes in the Help Me AI Project; reports and summaries are for the client to keep on their computer. For new skills, build the ZIP with the folder at the top level so it uploads cleanly.
- **Sources** — https://support.claude.com/en/articles/12512180-using-skills-in-claude · https://claude.com/docs/skills/how-to · https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features · https://support.claude.com/en/articles/9519177 · https://code.claude.com/docs/en/mcp

## Windows

- `~` means the user's home folder, `%USERPROFILE%` (for example `C:\Users\Sam`). So: `%USERPROFILE%\.claude\` (settings, `CLAUDE.md`, `skills\`, `projects\`), `%USERPROFILE%\.claude.json`, `%USERPROFILE%\.codex\` (`AGENTS.md`, `config.toml`, `sessions\`), `%USERPROFILE%\.agents\skills\`, and the client's data folder `%USERPROFILE%\help-me-ai\`.
- Windows 10 (1803 and later) and Windows 11 include `curl.exe` and `tar.exe`. In PowerShell, type `curl.exe`, not `curl` — plain `curl` there is a different command. `tar -xf file.zip` unzips; PowerShell's `Expand-Archive` works too.
- Skill commands that need bash fail without Git Bash; prefer your own file tools, and PowerShell when you need a shell.
