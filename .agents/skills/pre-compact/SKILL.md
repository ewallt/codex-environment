---
name: pre-compact
description: Run before compacting or ending a long session. Ensure the session log is current and write a concise handoff centered on the latest working context so the next session can resume without re-deriving state.
---

# Pre-Compact

Use this skill when the session is about to compact or when Tom asks for a handoff before pausing.

## Workflow

READ NOW: `C:\Users\tomew\Documents\codex-test\Projects\nlm\WORKLOG.md`

If anything notable completed since the last log entry, update the worklog first.

READ NOW: `references/handoff-template.md`

Then refresh `C:\Users\tomew\Documents\codex-test\Projects\nlm\HANDOFF.md` so it emphasizes:

- what we are working on right now
- what was just completed
- the latest context that matters most after compact
- the next step, or an explicit note that no next step is queued

## Rule

The handoff should be short, factual, and biased toward the most recent context. Do not write a broad summary of the whole project unless it is needed to understand the latest state.
