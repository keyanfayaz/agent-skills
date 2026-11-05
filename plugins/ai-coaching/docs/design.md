# help-me-ai — Design Spec

**Date:** 2026-10-19
**Status:** Approved 2026-10-19; first version built and tested
**Name:** `help-me-ai` · **Repo:** `keyanfayaz/agent-skills`

## 1. Purpose

A consultant sends a client one link. The client pastes one prompt (or uploads one zip), types `/help-me-ai`, and their own AI agent becomes a personal coach that gets to know how they work, makes a concrete improvement in the first session, and then guides them through a personal path of short sessions that set everything up and teach them to use AI better.

The insight behind it: the client's own agent is the best-placed assessor. In Claude Code and Codex it can read the client's real setup and session history and point to evidence ("you've pasted this checklist 9 times") instead of interrogating them.

## 2. Understanding

**What the consultant said:**
- Clients work in Claude Code, Codex, and/or the Claude chat app (claude.ai web/desktop/mobile). Often unknown up front.
- Clients are sometimes individuals, sometimes teams.
- The client may not know what they need; the agent leads and can eventually set everything up for them, offering further training sessions.
- Recommendations come from the agent's own judgment, not a house methodology.
- Results reach the consultant as a summary the client reviews and sends.
- Use open standards: Agent Skills (agentskills.io) and AGENTS.md.
- Named `help-me-ai`: easy to remember, and it appears when a client starts typing `/help`.

**Assumptions (confirmed or defaulted):**
- Clients may be non-technical: plain language, copy-paste install, no terminal knowledge required.
- Design for one person; keep every output in a fixed structure so team rollups are easy later.
- The repo is public and only ever contains generic skills; client data never enters it.

## 3. Success criteria

1. A non-technical client goes from link to first session in under 5 minutes, in any of the three surfaces, without installing git or anything else.
2. Every session ends with something changed and working (a file installed, a skill run once, a skill practised), not only a report.
3. The first session produces a visible quick win within roughly 10 minutes.
4. The client never has to choose a "mode" or learn internal vocabulary.
5. Nothing is read without consent and nothing is written without approval.
6. The consultant receives a client-approved summary in a fixed format.
7. Re-running `/help-me-ai` later picks up where the client left off and shows progress.

## 4. Concept

One skill. The client runs `/help-me-ai` (Claude Code), `$help-me-ai` (Codex), or asks for it in the chat app. The agent:

- **First run:** gets to know the client → delivers a quick win → proposes a personal **path** of 3–5 short sessions ordered by value.
- **Every later run:** runs the next session on the path and revises the path as it learns.

Sessions come in three kinds. These are internal; the client only ever hears outcomes ("let's turn your Friday update into one command").

| Kind | What happens |
|---|---|
| **Build** | The agent sets something up with the client: a skill (from repeated work), a connector, a folder/Project structure, routines. |
| **Train** | A 15–20 minute hands-on lesson on the client's real work, ending with the client doing it themselves. Targets a specific gap. Generated at run time from the gap and the tool's current docs. |
| **Checkup** | Re-assess against the rubric, show change since last time, update the path. |

Example path:

> 1. ✅ Teach me who you are *(done today)*
> 2. Turn your Friday client update into a one-command skill
> 3. Connect your calendar so I stop asking you about your schedule
> 4. Practice: hand off a whole research task, not just questions
> 5. Checkup: see what's changed

## 5. Client experience

### 5.1 Install (one step, no git required)

Every install uses one file: `help-me-ai.zip`, attached to each GitHub release. It always downloads from the same address: `https://github.com/keyanfayaz/agent-skills/releases/latest/download/help-me-ai.zip`.

**Claude Code / Codex: paste the prompt from the README.** The prompt tells the agent to work through these steps in order, stopping at the first that works:
1. **Download and unzip with what the computer already has.** macOS and Windows 10+ both include `curl` and `tar`. macOS also has `unzip`, and Windows has PowerShell's `Expand-Archive`. Then copy `help-me-ai/` into the personal skills folder: `~/.claude/skills/` for Claude Code, `~/.agents/skills/` for Codex. On Windows, the same folders sit under the user's home folder.
2. **If the agent can't reach the internet** (Codex's sandbox, a corporate network, a declined approval): the agent gives the client the download link to open in their browser. Then it installs from the client's Downloads folder.
3. **If a command needs approval** (Codex sandbox, Claude Code permission prompt): the agent explains in one plain sentence what the command does, so the client can approve with confidence.

The agent never needs git, Node or Python to install.

**Other routes:**
- **Technical clients with Node:** `npx skills add keyanfayaz/agent-skills --skill help-me-ai -g`.
- **Codex:** the built-in `$skill-installer` may also work from the repo URL (to verify; see section 13).
- **Chat app:** download `help-me-ai.zip` from the same link and upload it under Customize > Skills ("Code execution and file creation" must be on in Settings > Capabilities).

**Updating:** paste the same prompt again. Only the skill folder is replaced. `~/help-me-ai/` (profile, reports) is never touched.

### 5.2 Every run
1. **Look around (silently).** Identify the tool; determine the access level (5.3); check for an existing profile.
2. **Ask before looking.** State specifically what it wants to read (e.g. "your global instructions, your settings, and the last 60 days of session history — about 140 sessions"). The client answers *yes*, *pick some*, or *interview only*. Returning clients get a shorter version.
3. **Pick the session.**
   - No profile → first session (5.4).
   - Profile exists → next pending item on the path.
   - Path finished → checkup. If the last checkup was more than ~30 days ago, suggest a checkup first; the client may keep the planned session.
   - Client asks for something specific → the agent fits it in and updates the path.
4. **Run the session.**
5. **Wrap up.** Check today's change works (or note it to try in a new session), offer the consultant summary, then show the report, profile changes and any approved summary together and save them after one yes. Name the next session and suggest when to come back.

### 5.3 Access levels
| Level | Where | Evidence | Delivering changes |
|---|---|---|---|
| **Full** | Claude Code, Codex | Instructions, settings, installed skills/connectors, session history, `/insights` report if recent | Writes files directly (after approval) |
| **Partial** | Chat app with connectors or Projects | Connected tools, Project contents, conversation | Downloadable files + paste-ready text |
| **Conversation-only** | Plain chat | Interview covering the rubric areas | Paste-ready text + downloadable files |

### 5.4 First session
1. **Intake:** what to call them, then at most six questions, strictly one per message, multiple choice where possible, skipping anything the evidence already answered. Covers what they do, what they use AI for, what frustrates them, what they want from today, boundaries, and employer AI rules (its own question).
2. **Quick win:** one concrete improvement chosen from the evidence. Default: teach the agent who the client is via a personal instructions file (`~/.claude/CLAUDE.md` for Claude Code, Codex's global AGENTS.md, or paste-ready text for chat-app profile/Project instructions). If that already exists and is good, pick the next most valuable gap. If the client uses both Claude Code and Codex, write the same content to both files and record both in the profile's Setup section.
3. **Rubric snapshot:** levels across the six areas (section 7).
4. **Propose the path:** 3–5 sessions with one-line reasons. The client approves or reorders.
5. **Wrap up** as in 5.2.

### 5.5 Conversation rules
One question at a time; multiple choice where possible; plain language, no jargon unless the client uses it first; show every change before saving; lead with a recommendation rather than a menu.

## 6. Session details

### 6.1 Checkup
- **Reads (full access):** global and project instructions files; settings (permissions, hooks, model); installed skills, plugins, MCP servers/connectors; the last ~30–60 days of session history, sampled. If a recent Claude Code `/insights` report exists (`~/.claude/usage-data/report.html`), read it first. The agent cannot run `/insights` itself, but it may suggest the client does.
- **Looks for in history:** repeated requests; long instructions pasted repeatedly; corrections and re-explanations ("no, I meant…"); abandoned tasks; permission-prompt friction; tool errors.
- **Output:** what's working, the biggest gaps, and the **top 3 moves**, each ending with "I can do this now — want me to?" The path is updated to match.

### 6.2 Build: skill
- **Find candidates:** repeated requests in history, repeatedly pasted instructions, checklists or templates in the client's files, and "what do you do every week?"
- **Rank:** frequency × time saved × how stable the procedure is. Present the top 3–5 with evidence ("seen 9 times, e.g. …").
- **Triage honestly:** some candidates are better as one line in the instructions file, or as a connector, than as a skill. Say so.
- **Build:** the client picks 1–2. The agent captures the steps, inputs, quality bar and an example of good output, then drafts a standard `SKILL.md` with a description that triggers reliably. It shows the draft, installs it in the right place (or packages a zip for the chat app), and does a **test run on a real task with the client**, revising as needed.
- **Check first:** look at existing skills to avoid duplicates.

### 6.3 Build: setup
- **Conversation:** roles, recurring responsibilities, where information lives, weekly rhythm, goals, boundaries.
- **Builds only what will be used this week:**
  - the personal instructions file
  - a simple structure suited to the tool (folders for Code/Codex, Projects for the chat app)
  - connections to the apps they copy from, using built-in connectors only (the client signs in; nothing installed)
  - 2–3 routines, as skills or as scheduled tasks where the tool supports them
  - a "first week" list of 3 things to try
- Everything else goes into the path or the profile as "later".

### 6.4 Train
- One specific gap per lesson, 15–20 minutes, using the client's real work.
- Structure: why it matters for them → short demo on their task → the client does it themselves → recap plus one thing to try this week.
- Before teaching a product feature, the agent checks the tool's current official docs, since models are often out of date about their own product's newest features.
- At wrap-up, the agent may offer further training sessions; accepted ones are added to the path.

## 7. Rubric

A fixed list of areas so results can be compared across clients and over time. Recommendations stay the agent's judgment.

| Area | Question |
|---|---|
| **Context** | Does the agent know who they are and how they work? |
| **Reuse** | Is repeated work captured as skills or templates? |
| **Connections** | Are their tools and data connected, or copy-pasted? |
| **Delegation** | Do they hand off multi-step work, or only ask quick questions? |
| **Safety** | Permissions, secrets hygiene, reviewing output. |
| **Habits** | Breadth and frequency of use; where AI isn't used yet but could be. |

Levels: **Starting / Building / Strong**. Each level is defined per area in `references/rubric.md`. There are no numeric scores, which would suggest false precision.

## 8. Data and files

### 8.1 Location
`~/help-me-ai/` in the client's home folder. It is visible (not hidden) so non-technical clients can find it, and shared by Claude Code and Codex on the same machine.

```
~/help-me-ai/
  profile.md
  reports/YYYY-MM-DD-session-N.md
  for-consultant/YYYY-MM-DD-summary.md
  backups/            ← copies of any file before help-me-ai changed it
```

### 8.2 `profile.md`
Short, because it's read at the start of every session. YAML header for machine-readable fields, then fixed sections.

```yaml
---
schema: 1
name: <first name or alias the client chooses>
tools: [claude-code, codex, claude-chat]
access: computer | apps | chat
levels:
  - date: 2026-10-20
    context: starting
    reuse: starting
    connections: building
    delegation: starting
    safety: building
    habits: building
---
```

Sections:
- **About:** role, work, goals, boundaries, employer AI rules
- **Setup:** tools in use, plus everything help-me-ai installed and where
- **Path:** numbered sessions with status and a one-line reason
- **Log:** one line per session

`profile.md` is separate from the client's instructions file on purpose. The instructions file shapes everyday agent behaviour and stays short; the profile tracks the program.

### 8.3 Session report
One screen: what we did; what changed (every file created or modified, with its path); what you learned; what's next. The first report also includes the rubric snapshot and the path. Shown in chat and saved.

### 8.4 Consultant summary
Fixed template with a YAML header containing the rubric levels (for later team rollups).
- **Contains:** role (the client may anonymise it), tool and access level, levels before and after, what was built, progress along the path, blockers or questions for the consultant, and optional "anything you want your consultant to know?"
- **Never contains:** conversation content, file contents, third-party names, secrets.
- **Flow:** the agent drafts it → the client edits and approves → it's saved → **the client sends it**. The agent never sends anything.
- The consultant's name and contact are set once in the skill's `metadata` frontmatter, so the summary can say "send this to [consultant]".

### 8.5 Chat app (no file system)
The first session suggests creating a Claude Project named "Help Me AI". The agent produces `profile.md` as a downloadable file, and the client adds it to the Project's files. Later sessions run inside that Project. At wrap-up the client replaces the file with the updated version. The steps are spelled out every time.

## 9. Privacy and safety rules

These live in `SKILL.md` and apply to every session.

1. **Ask first, and be specific.** List exactly what will be read and how much. The client can exclude folders or projects. Nothing is read before a yes.
2. **Read-only until approved.** Show every change before saving it. Existing instructions files are added to, never overwritten. Back up to `~/help-me-ai/backups/` first.
3. **Nothing goes anywhere except to the AI they already use.** What the agent reads is processed by the client's own AI tool, as in any chat, and the agent says so plainly; nothing goes to the consultant or anyone else. Web access is only for checking official docs, and client details never go into queries.
4. **Never copy secrets.** API keys, tokens and passwords never appear in any output. An exposed secret is reported as a safety finding without repeating it.
5. **Summarise history; don't store it.** Quote briefly or paraphrase. Never copy transcripts into saved files.
6. **Security settings are the client's call.** Propose permission changes in plain language. Never quietly loosen them, and never recommend blanket "skip all approvals" modes as a shortcut.
7. **Everything is undoable.** Every install is recorded in the profile's Setup section, and "remove anything you added" always works.
8. **Respect boundaries.** The client's "never touch" list and employer AI rules are stored in the profile and honoured every session.

## 10. Packaging

Updated 2026-11-05: Help Me AI is a skill inside the `ai-coaching` plugin of the broader Agent Skills toolkit.

- Source: `plugins/ai-coaching/skills/help-me-ai/`.
- Coaching-specific contributor rules: `plugins/ai-coaching/AGENTS.md`.
- Plugin manifests support Codex and Claude Code; Claude's plugin command is `/ai-coaching:help-me-ai`.
- Existing standalone installs retain `/help-me-ai`, `$help-me-ai`, and `~/help-me-ai/` state.
- `scripts/build-zip.sh` still builds `help-me-ai.zip` with the skill folder at its top level.
- Existing `v*` release tags and the latest ZIP download URL remain reserved for this standalone skill.
- Client machines require no additional runtimes; toolkit maintenance and other plugins have separate requirements.

## 11. Testing

1. **Structure:** `python3 -m unittest discover tests` passes. This is a standard-library-only checker for the Agent Skills spec rules plus this repo's own rules. The reference `skills-ref` tool is demo-only and not packaged, so it isn't used.
2. **Scenario dry runs** against a pass/fail checklist in `tests/scenarios.md`. Personas:
   - A. Newcomer in the Claude chat app (conversation-only)
   - B. Heavy Claude Code user with months of history (full)
   - C. Codex user with light history (full)
   - D. Returning client on session 3 (profile exists)

   Checklist:
   - consent asked before any read
   - one question at a time
   - quick win delivered early
   - path proposed and saved
   - report and summary follow their templates
   - no secrets or transcript copies in any output
   - nothing written without approval
   - existing files backed up
   - no mode vocabulary shown to the client
3. **Install without git:** run the README prompt on a machine (or user account) without git or Node, in both Claude Code and Codex. Then test the browser-download fallback with the agent's internet access blocked. Use Windows too if a test machine is available.
4. **Dogfood:** the consultant runs it on their own setup first.
5. **Pilot:** first client; the consultant summary and the client's feedback drive revisions.

## 12. Out of scope for v1

- Team rollup tooling (the structure supports it later)
- Required dependencies on other plugins or toolkits
- Bundled scripts (e.g. a history extractor). Revisit if dry runs show history reading is too slow or unreliable.
- HTML reports
- Any automatic sending of data to the consultant
- A house methodology

## 13. To verify during implementation

Checked against official docs on 2026-10-19 and recorded in `references/environments.md`. The zip must contain the skill folder; chat-app uploads live under Customize > Skills; Codex asks for approval for network access and writes outside the workspace. Re-check these before each release:
- Codex global instructions file location (expected `~/.codex/AGENTS.md`) and session history location/format (expected `~/.codex/sessions/`).
- Claude Code session history format (`~/.claude/projects/**/*.jsonl`), the user-level skills folder (`~/.claude/skills/`), and whether new skills are picked up without a restart.
- Claude chat app: the exact settings path for uploading a skill zip; whether file downloads and Projects behave as section 8.5 assumes.
- The current `npx skills` flags for a global, single-skill install.
- That GitHub's `releases/latest/download/help-me-ai.zip` link works for the asset name used.
- The zip layout the Claude chat app expects (folder at the top level vs. files at the root).
- How Codex's sandbox handles network access and writing to `~/.agents/skills` (which approvals the client will see), and whether `$skill-installer` accepts an arbitrary GitHub repo.
- Personal skills folder locations on Windows for Claude Code and Codex.

**Consultant inputs (decided 2026-10-19):** skill name `help-me-ai`; repo `keyanfayaz/agent-skills`; the consultant summary says "send this to Keyan" (name only, set in `metadata`).

## 14. Decisions log

| Decision | Choice | Why |
|---|---|---|
| Packaging | One skill, sessions as reference files; repo as a collection | Shared rules live once; one install and name; unused parts cost no context |
| Client interface | Agent leads; no modes exposed | Clients often don't know what they need |
| Structure of work | Personal path of build/train/checkup sessions | Progressive setup at a digestible pace; there's always a clear next step |
| Recommendations | Agent judgment against a fixed rubric | No house method; the rubric keeps results comparable |
| Consultant view | Client-approved summary, client sends | Trust; no services or accounts |
| Install | One release zip at a fixed "latest" link; agent downloads with built-in OS tools, falls back to browser download | Clients may not have git or Node; one file serves every route |
| Storage | `~/help-me-ai/`, visible, shared across tools | Findable by non-technical clients; tool-agnostic |
| Name | `help-me-ai` | Memorable, sits next to `/help`; bare `start` collides with existing skills |
