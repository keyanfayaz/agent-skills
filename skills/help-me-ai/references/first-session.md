# First session

Goal: by the end, the client feels understood, has one thing that already works better, and knows what the next few sessions will do for them. Aim to finish in 30–45 minutes, with the quick win done within about 10 minutes of starting.

## Intake

Before your first question, read what the client agreed to let you see, using the Evidence lines for each of the six areas as your guide. Every question the evidence already answers is one you don't ask.

If you don't know their name yet, start by asking what they'd like you to call them. That doesn't count as one of the questions below.

Then ask at most six questions, exactly one per message — never join two with "and" — offering choices where you can, with "something else" always allowed. Skip any the evidence already answered:

1. **Their work:** "What's your job, in a sentence or two?"
2. **AI today:** "What do you use AI for at the moment?"
3. **The biggest annoyance:** "What's the most tedious or repetitive part of your week?"
4. **Today:** "What would make today's session worth it for you?"
5. **Boundaries:** "Is there anything AI should never touch for you?"
6. **Employer rules:** "Does your employer have rules about using AI tools (yes, no, not sure)?" Skip this if they work for themselves.

Say briefly why you're asking when it isn't obvious. Mirror their words back — you'll reuse them in their instructions and path. Record answers in the profile's About section, boundaries and employer rules included.

## Quick win

Pick the single most useful thing you can finish in about 10 minutes. Start from their answer to "what would make today's session worth it": if it can be done (or started) in 10 minutes, that is the quick win — their wish beats the default below. Otherwise use the evidence and their other answers.

**Default: teach the agent who they are.** Draft a short "About me and how I like to work" block, under 25 lines: who they are, what they work on and for whom, how they like answers (length, tone, format), tools they use, and their boundaries. Use their words. Mark any line you had to guess (tone, length, format) and ask them to confirm or fix those lines when they look at the draft. Show the draft and change it until they're happy. Then:

- Claude Code: add it to `~/.claude/CLAUDE.md`.
- Codex: add it to the personal instructions file Codex actually uses — usually `~/.codex/AGENTS.md`, but `AGENTS.override.md` if that one is in use, inside `CODEX_HOME` if it's set (see the per-tool facts).
- Both tools in use: add the same block to both.
- Chat app: give it as finished text to paste into their personal preferences in Claude's settings, and tell them exactly where that is. First ask whether that box already has text; if it does, have them add yours at the end instead of replacing what's there.

If the file already exists, back it up and add your block at the end. Never rewrite, reorder or remove what's there. If they didn't agree to you reading their instructions file, ask before opening it to add your block; if they'd rather you didn't, give them the text and tell them exactly where to paste it. Keep task procedures (a checklist or the steps for one particular job) out of personal instructions — those become a skill.

**If that's already strong,** take the biggest gap from the snapshot that fits in 10 minutes instead — for example, connecting the app they paste from most, a tiny skill for their most repeated request, or moving an exposed key out of their settings (tell them where it is; never repeat it).

Finish by letting them feel the difference: suggest one thing to try in a fresh chat that shows the change working ("start a new chat and ask for this week's update — notice it already knows who it's for").

## Snapshot

Give each of the six areas a level with one line of evidence each, in plain words. Rate things as they were before today's change: this is their starting point. Don't call it a rubric or a score; call it "where things stand". Lead with what's working before what's missing. Add the levels to the profile as a new dated entry.

If you had little to go on (interview only, or very little history), say so, and say the next checkup will be more precise.

## Propose the path

Propose 3–5 sessions, ordered by how much each will help them for the effort. Write each as an outcome in their words, with a one-line reason tied to evidence:

> 1. ✅ Teach me who you are (done today)
> 2. Turn your Friday client update into a one-command skill — you've asked for it 6 times this month
> 3. Connect your calendar so I stop asking about your schedule
> 4. Practice: hand off a whole research task, not just questions
> 5. Checkup: see what's changed

Rules:
- Each item is one session: something to build, a hands-on practice, or a checkup. Never show those labels as jargon; let the wording make it clear.
- The last item is always a checkup.
- Ask them to approve, reorder or swap items. Their order wins.
- Save the agreed path to the profile, with the kind of each item in brackets.

Then wrap up as the skill's main instructions describe.
