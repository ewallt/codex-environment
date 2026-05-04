# AGENTS.md

## Project Overview

This repo is the portable Codex environment for Tom's Mac and Windows machines. It stores durable setup context, local skills, bridge helpers, handoff notes, and NLM project documentation so future Codex sessions can resume without rediscovering the environment.

The Mac is becoming the primary development machine. Tom will be outside the United States for about five months and will mostly use the MacBook. The Windows machine is available for about one more week, then is expected to be shut down for those five months. Treat this Mac repo as the active source of truth for new development.

Tom has worked more extensively with Claude Code and has a similar setup there. Claude Code may be used to help create or refine Codex skills as needed, but durable Codex setup state should be captured in this repo.

## Source Of Truth

- GitHub repo: `ewallt/codex-environment`
- Primary local Mac checkout: `/Users/tom/Documents/codex-test/codex-environment`
- Default branch: `dev`
- Repo-wide current state: `HANDOFF.md`
- Repo-wide chronological log: `WORKLOG.md`
- NLM project state: `Projects/nlm/PROJECT.md`, `Projects/nlm/HANDOFF.md`, and `Projects/nlm/WORKLOG.md`
- Google Docs bridge: short cross-machine messages only, not durable project storage

When local files, Google Docs messages, and remembered context disagree, verify against the repo and current command output before answering.

## Setup

- Repo skills live in `.agents/skills/`.
- On Mac, installed skills should be available under both `/Users/tom/.agents/skills/` and `/Users/tom/.codex/skills/` so current and future Codex sessions can discover them.
- Google Docs bridge OAuth client and token paths on Mac:
  - `/Users/tom/.notebooklm-mcp-cli/codex-oauth.keys.json`
  - `/Users/tom/.notebooklm-mcp-cli/codex-gdrive-token.json`
- Do not commit OAuth client JSONs, token caches, browser profiles, or other secrets.

## Workflow

- Log notable setup, repo, skill, bridge, and project changes as they happen.
- Use top-level `WORKLOG.md` for repo-wide setup and skills.
- Use `Projects/nlm/WORKLOG.md` for NLM-specific source/video/dashboard/NotebookLM work.
- Keep `HANDOFF.md` current enough that a new session can restart from it.
- Tom prefers looking for a compaction opportunity once context is over about 50 percent used. By about 60 percent used, update logs and handoff before continuing unless the smallest coherent task step must be finished first.
- If completed work should be backed up, commit and push to the remote before compaction when possible.

## Skills

- Use `skill-creator` before creating or modifying any skill.
- If a task is about writing a new skill or editing an existing one, read the `skill-creator` skill first.
- After changing repo skills, sync them into the Mac installed skill directories when the current or future Codex sessions need to use them.
- Validate skills when practical. If full validation is blocked by missing dependencies, record the limitation in `WORKLOG.md` or `HANDOFF.md`.

## Google Docs Bridge

- Mac writes to `Codex-Mac-Outbox`.
- Windows writes to `Codex-Windows-Outbox`.
- Read the other side's outbox before replying.
- Keep messages short, dated, and action-focused.
- If a bridge message changes durable setup state, copy the result into repo files.

## Cautions

- Do not rely on chat memory for durable state.
- Do not revert user or other-agent changes unless Tom explicitly asks.
- Do not treat Windows-only paths as valid on Mac; translate paths intentionally.
- Windows Codex may have stale context as the Windows machine is being phased out. Verify important claims directly.
