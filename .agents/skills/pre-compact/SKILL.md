---
name: pre-compact
description: Run before compacting or ending a long session. Ensure the session log is current and write a concise handoff centered on the latest working context so the next session can resume without re-deriving state.
---

# Pre-Compact

Use this skill when the session is about to compact or when Tom asks for a handoff before pausing.

## Workflow

Check context usage if visible. Tom prefers looking for a stopping point after about 50 percent used and logging/handoff by about 60 percent used.

Read the nearest relevant worklog:

- repo-wide setup or skills: `WORKLOG.md`
- NLM-specific work: `Projects/nlm/WORKLOG.md`

If anything notable completed since the last log entry, update the worklog first. Notable work includes new or modified skills, bridge/auth setup, repo clone/pull/push changes, branch changes, and any setup state that should survive compaction.

If the completed work should be backed up, update the repo before compacting:

1. Check `git status --short --branch`.
2. Review the diff for files changed in this session.
3. Commit the durable changes with a concise message.
4. Push the branch if a remote is configured and network access is available.
5. If commit or push needs user approval or should be delayed, write that explicitly in the handoff.

READ NOW: `references/handoff-template.md`

Then refresh the relevant handoff:

- repo-wide setup or skills: `HANDOFF.md`
- NLM-specific work: `Projects/nlm/HANDOFF.md`

The handoff should emphasize:

- what we are working on right now
- what was just completed
- the latest context that matters most after compact
- the next step, or an explicit note that no next step is queued
- whether durable changes were committed and pushed

## Rule

The handoff should be short, factual, and biased toward the most recent context. Do not write a broad summary of the whole project unless it is needed to understand the latest state.
