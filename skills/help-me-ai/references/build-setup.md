# Build: get organized around AI

Goal: a simple setup that fits how the client actually works — something they'll use this week, not a system to maintain. Build only what they'll use in the next seven days; everything else goes on their path as "later".

## Conversation

One question at a time, skipping anything already in the profile:

- **Roles** — the hats they wear (for example: running the business, client work, family admin).
- **Recurring responsibilities** — what comes round every day, week, month.
- **Where information lives** — email, calendar, documents, notes apps, chat tools, paper.
- **Rhythm** — when they plan, when they do focused work, when things pile up.
- **Goals** — what they'd most like AI to take off their plate.
- **Boundaries** — what AI must never touch; employer rules.

Play back a short picture of their week in their words and check it before building anything.

## Instructions file

Make sure their personal instructions reflect the picture you just agreed: roles, priorities, how they like results, boundaries. Add to the existing file (back it up first); never rewrite or reorder what's there. Keep your addition short, because the file is read in every session. If their file is already long, don't trim it; at most, suggest what could go.

- Claude Code: `~/.claude/CLAUDE.md`. Codex: the personal instructions file it actually uses — usually `~/.codex/AGENTS.md` (see the per-tool facts for the exceptions). Both if they use both.
- Chat app: finished text for their personal preferences, plus separate text for each Project's instructions.

## Structure

Give their AI work a simple home that matches their roles — at most one place per role.

- **Claude Code or Codex:** a few clearly named folders (for example `~/ai/clients/`, `~/ai/admin/`), each with a short instructions file (`CLAUDE.md` for Claude Code, `AGENTS.md` for Codex) saying what that work is and how they like it done. Starting a session in that folder then brings the right context automatically.
- **Chat app:** one Project per role, each with instructions and the few reference files they keep pasting in.

Show the proposed structure as a short list first. Create it only after they agree, and record every folder or Project in the profile's Setup section.

## Connect an app

If they keep copying things out of one tool (calendar, email, documents, a project tracker), connecting it lets the AI read it directly.

- **Use built-in connectors only:** in the Claude app, Customize > Connectors (these also appear in Claude Code when they sign in with a Claude subscription); in Codex and the ChatGPT apps, the apps and plugins in settings. Never suggest anything that has to be installed or run on their computer.
- **Explain before they connect:** say in plain words what it will be able to read and change, and check it fits their boundaries and employer rules. Connecting is their decision.
- **They sign in themselves.** Never ask for or handle their password or keys.
- **Test it** with one real question that needs the connection ("what's on my calendar tomorrow?"), and record the connection in the profile's Setup section.

## Routines

Pick two or three recurring moments where AI can carry the load — for example Monday planning, a daily inbox sweep, the Friday client update. For each, decide with them:

- **A skill** they start by name when the moment comes — build it the same way as any other skill, keeping it short.
- **A scheduled task**, if their tool can run one on a schedule and the job needs no input from them. Explain where it runs and what it can reach before setting it up.
- **A pasted prompt** they keep handy, if neither of the above fits their tool.

Try each routine once with them before moving on.

## First week

End with a list of three small things to try this week, each tied to something you just set up ("Monday: start your planning session in the admin folder"). Save the list in the session report. Put everything you didn't build today on their path as "later", with a reason.
