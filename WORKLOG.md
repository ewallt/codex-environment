# Codex Environment Worklog

## 2026-05-03 - Handoff Set To NLM Validation

- Refreshed `HANDOFF.md` after Mac setup was committed and pushed.
- Recorded that the next objective is validating whether Mac Codex can run the NLM workflow.
- The next session should check the Mac `nlm` CLI, NotebookLM auth, network access, and Mac path translations for source docs, downloads, dashboard files, and playlist config.
- If Mac NLM validation fails, record the missing dependency or auth step and use Windows/Claude Code while the Windows machine is still available.

## 2026-05-03 - AGENTS Source Of Truth Context Added

- Replaced the stub `AGENTS.md` with repo-wide operating instructions.
- Recorded that Tom will be outside the United States for about five months and will primarily use the MacBook.
- Recorded that the Windows machine is available for about one more week, then is expected to be shut down for those five months.
- Established the Mac checkout and `ewallt/codex-environment` repo as the active source of truth for new Codex development.
- Noted that Claude Code may help create or refine Codex skills, but durable Codex setup state should be captured in this repo.

## 2026-05-03 - Pre-Compact Backup Rule Added

- Updated the repo `pre-compact` skill to be cross-platform instead of Windows/NLM-only.
- Added Tom's rule that meaningful work should be logged before compaction.
- Added an explicit repo-backup step: when completed work should be preserved, check status, review the diff, commit durable changes, and push the branch if a remote/network is available.
- Noted that if commit or push is delayed or needs approval, the handoff should say that explicitly.

## 2026-05-03 - Mac Setup And Repo Skill Added

- Cloned `https://github.com/ewallt/codex-environment.git` to `/Users/tom/Documents/codex-test/codex-environment`.
- Confirmed the repo is on branch `dev` and clean against `origin/dev`.
- Read `README.md`, `bootstrap/macos-setup.md`, `AGENTS.md`, `Projects/nlm/HANDOFF.md`, `Projects/nlm/WORKLOG.md`, and `Projects/nlm/PROJECT.md`.
- Installed repo skills to `/Users/tom/.agents/skills`.
- Copied repo skills to `/Users/tom/.codex/skills` so future Mac Codex sessions can discover them.
- Added the repo-local `codex-environment` skill with logging, bridge, skill-install, and compaction guidance.
- Added the user preference that context should be logged and prepared for compaction after about 50 percent used, and by about 60 percent used.
- Basic frontmatter checks passed for the new skill. The full `skill-creator` `quick_validate.py` check could not run because this Mac Python environment does not have `yaml` installed.
