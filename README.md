# Codex Environment

This repository is the portable Codex setup for Windows and Mac.

It contains:

- standing instructions in `AGENTS.md`
- session state in `HANDOFF.md`, `WORKLOG.md`, and `Projects/nlm/WORKLOG.md`
- the NLM project docs under `Projects/nlm/`
- shared bridge docs and tools
- the local Codex skills in `.agents/skills/`

## Purpose

The goal is to let Codex on a Mac recreate the same working environment without having to rediscover the setup.

## What Mac Codex Should Do First

1. Clone or copy this repository.
2. Read `AGENTS.md`.
3. Read `Projects/nlm/HANDOFF.md`.
4. Read `Projects/nlm/WORKLOG.md`.
5. Install the local skills from `.agents/skills/`.
6. Use the Google Docs bridge docs to connect to the shared `Agent Bridge` workflow.

## Skills Included

- `codex-environment`
- `google-docs-bridge`
- `pre-compact`
- `post-compact`
- `skill-creator`
- `nlm-skill`
- `scene-writer`
- `playlist-ideas`
- `youtube-publish`

## Bootstrap

See `bootstrap/macos-setup.md` for the recommended setup sequence.
Use `bootstrap/install-skills.sh` to copy the skills into `~/.agents/skills` on Mac.

## Notes

- No secrets or live tokens should be committed here.
- Keep `main` stable once this is pushed to GitHub.
- Use a working branch for changes and promote only when the repo is ready.
