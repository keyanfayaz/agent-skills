# help-me-ai

A personal AI coach that lives inside the AI tool you already use: Claude Code, Codex or the Claude app.

- For the plugin edition, install `ai-coaching@keyan-agent-skills`; its Claude Code command is `/ai-coaching:help-me-ai`. The standalone routes below keep their original commands.

## What this is

Type `/help-me-ai` and your own AI gets to know how you work. In the first session it makes one real improvement straight away, then suggests a short path of sessions to help you get much more out of AI. That can mean teaching it who you are, turning work you repeat into one-word commands, connecting the apps you copy and paste from, and hands-on practice on your own tasks.

It asks before it looks at anything, shows you every change before making it, and keeps your progress in a folder on your computer.

## Install

Pick the one that matches where you use AI. You only do this once.

### Claude Code or Codex

Copy everything in the box below, paste it into Claude Code or Codex, and press Enter:

```text
Please install the "help-me-ai" skill for me, then start it.

1. Download https://github.com/keyanfayaz/agent-skills/releases/latest/download/help-me-ai.zip using tools already on this computer (curl on a Mac; curl.exe or PowerShell on Windows). Don't install anything new — git isn't needed.
2. Unzip it and put the help-me-ai folder in my personal skills folder:
   - Claude Code: ~/.claude/skills/
   - Codex: ~/.agents/skills/
   If a help-me-ai folder is already there, replace only that folder. Never touch ~/help-me-ai/ — that's where my progress is saved.
3. If you can't download it, give me the link to open in my browser, then install it from my Downloads folder (if my browser already unzipped it, use the help-me-ai folder there).
4. Before running any command that needs my approval, tell me in one plain sentence what it does.
5. When it's installed, start help-me-ai. If it doesn't show up yet, read the SKILL.md file inside the folder you just installed and follow it.
```

It may ask you to approve a download or a change to a folder. That's expected. It will tell you what each one does first.

If you use both Claude Code and Codex, paste it into each one.

### Claude app (claude.ai)

1. Download [help-me-ai.zip](https://github.com/keyanfayaz/agent-skills/releases/latest/download/help-me-ai.zip). Don't unzip it.
2. In Claude, open **Settings > Capabilities** and make sure **Code execution and file creation** is on.
3. Open **Customize > Skills**, click **+**, then **+ Create skill**, then **Upload a skill**, and choose the zip.
4. Create a Project called **Help Me AI** and start a chat in it.

On a work account, your administrator may need to allow skills first.

### For technical users

If you have Node installed:

```bash
npx skills add keyanfayaz/agent-skills --skill help-me-ai -g
```

## Start

- **Claude Code:** type `/help-me-ai`
- **Codex:** type `$help-me-ai`
- **Claude app:** in your Help Me AI Project, say "help me get better at using AI"

Come back the same way for your next session. It remembers where you left off.

## What it will and won't do

- It **asks first** before reading anything, says exactly what and how much, and you can say no to any of it.
- It **shows you every change** before making it, and backs up any file it changes.
- It **never copies passwords or keys**, and keeps your progress on your computer in a folder called `help-me-ai` in your home folder.
- It **shares nothing with anyone** beyond the AI you're already using. At the end of a session it can write a short summary for your consultant, which you review and send yourself if you want to.

## Update or remove

- **Update:** paste the same install prompt again. Only the skill is replaced; your progress stays.
- **Remove:** ask your AI to "remove the help-me-ai skill", or delete the `help-me-ai` folder inside `~/.claude/skills/` or `~/.agents/skills/`. In the Claude app, turn it off or delete it under Customize > Skills.
- **Your progress** is in the `help-me-ai` folder in your home folder. It's yours to keep or delete.

## For maintainers

How the repo is organised, its rules and how to release: [AGENTS.md](AGENTS.md). Why it works the way it does: [docs/design.md](docs/design.md).
