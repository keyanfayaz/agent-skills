# Build: turn repeated work into a skill

Goal: by the end of the session, one (at most two) of the client's repeated tasks is a skill they have already used on real work.

## Find candidates

Look in three places:

- **History** — requests made again and again in similar words; the same long block of instructions pasted in; the same sequence of steps walked through by hand.
- **Their files** — checklists, templates, "how we do X" notes, standard emails or reports they reuse.
- **Asking** — "What do you do every week or month that follows the same steps?" and "What do you wish you only had to explain once?"

Before suggesting anything, list the skills they already have. Don't build a duplicate; improving an existing skill that isn't working is a fine outcome.

## Rank

Rank candidates by: how often it happens × how long it takes each time × how stable the steps are (the same every time is good; different every time is bad).

Show the top three to five as a short list, each with its evidence: a count and a paraphrased example ("asked for the Friday client update 6 times since September, usually pasting the same checklist"). Never quote content with other people's names, client details or secrets. Recommend one and say why, then let them choose.

## Triage

Not everything should be a skill. Say so plainly when something else fits better:

- **A preference that applies to everything** (tone, format, length) → one line in their personal instructions.
- **The pain is copying information out of an app** → connect that app.
- **The steps change every time, or it's rare** → leave it; it isn't worth a skill.
- **It should happen on a schedule** → a skill plus a scheduled task, where their tool supports scheduling.

## Capture the steps

Interview them, one question at a time:

1. What usually starts this task, and what do they say when they ask for it?
2. What goes in — information, files, apps — and where does each come from?
3. The steps, in order. Read them back and check.
4. What good output looks like. Ask for a real past example; it's worth more than any description.
5. What to avoid, and who sees the result.

If they already use a checklist or template for this task, keep every item in the skill, in their words; ask before dropping or merging any. Summarise the procedure in a few lines and get a yes before writing anything.

## Write the SKILL.md

A skill is a folder containing a file named `SKILL.md`: a short header, then plain instructions.

```markdown
---
name: weekly-client-update
description: Drafts the Friday client update from this week's notes and tasks, in the client's usual format and tone. Use when asked for the weekly update, the Friday update, or a client status email.
---

# Weekly client update
...steps, inputs, output format, quality checks, one example...
```

Rules:

- **Name:** lowercase letters, digits and single hyphens, at most 64 characters, the same as the folder name. Use their words so it's easy to remember.
- **Description:** at most 200 characters, so it works in every tool (the Claude app's limit). Say what it does, then "Use when …" followed by the phrases the client actually uses to ask for it. This is what makes it start on its own, so use their words, not yours.
- **Body:** under about 150 lines. The steps, the inputs and where they come from, the output format, a short quality checklist, and their good example (with names and private details replaced).
- **Plain files only.** No scripts, nothing to install. If there's long reference material (a style guide, a price list), put it in a second file inside the skill folder and say in `SKILL.md` when to read it.
- Show the complete draft and adjust it until they're happy before saving.

## Install

- **Claude Code:** save as `~/.claude/skills/<name>/SKILL.md`. They run it with `/<name>`.
- **Codex:** save as `~/.agents/skills/<name>/SKILL.md`. They run it with `$<name>`.
- **Both tools in use:** install it in both places.
- **Chat app:** make a ZIP that contains the skill's folder (folder at the top level, named exactly like the skill) and give it to them as a download. Then walk them through uploading it: Customize > Skills, "+", "+ Create skill", "Upload a skill". "Code execution and file creation" must be on in Settings > Capabilities.

Record the skill's name and location in the profile's Setup section so it can be found, changed or removed later.

## Test run

Use it on a real, current task with them — not a made-up one.

1. Have them start it by name.
2. Compare the result with their good example. Ask what's off, change the skill (show the change), and run it again until they're happy.
3. Check it starts on its own: in a fresh chat, have them ask for the task the way they normally would.
4. Tell them how to run it, and that they can ask you any time to change it.

If they'd like more skills, add the next candidate to their path.
