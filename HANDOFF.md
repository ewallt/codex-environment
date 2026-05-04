# Handoff

## Current State

- Mac has cloned `https://github.com/ewallt/codex-environment.git` at `/Users/tom/Documents/codex-test/codex-environment`.
- The repo is on branch `dev`; latest pushed setup commit is `1eadb3e Add Mac source-of-truth guidance`.
- Google Docs bridge auth is working on Mac with token cache at `/Users/tom/.notebooklm-mcp-cli/codex-gdrive-token.json`.
- Repo skills were installed to `/Users/tom/.agents/skills` and copied to `/Users/tom/.codex/skills` for Mac Codex discovery.
- Added a new repo-local skill: `.agents/skills/codex-environment/`.
- `AGENTS.md` has been replaced with repo-wide operating instructions.
- Tom will be outside the United States for about five months and will primarily use the MacBook.
- The Windows machine is available for about one more week, then is expected to be shut down for those five months.
- Treat this Mac checkout and `ewallt/codex-environment` as the active source of truth for new Codex development.
- Most work so far on Mac has been environment setup, not substantive NLM project execution.

## Next Steps

1. Validate that Mac Codex can do the NLM things.
   - Read `Projects/nlm/PROJECT.md`, `Projects/nlm/HANDOFF.md`, and recent `Projects/nlm/WORKLOG.md`.
   - Check whether the `nlm` CLI exists on Mac and whether auth is live.
   - Run the safest first check, likely `nlm notebook list`, with network approval if needed.
   - Verify whether the Mac has the required NotebookLM/browser/session setup or whether this still depends on Windows.
   - Identify Mac path translations for source docs, downloads, dashboard files, and playlist config.
2. If NLM validation succeeds, record the Mac-specific commands and paths in the repo.
3. If validation fails, write down the missing dependency/auth/session step and use Windows or Claude Code while the Windows machine is still available.
4. If skills are changed later, run full skill validation after installing the missing Python `yaml` dependency or using an environment that has it.
5. Keep using `WORKLOG.md` for repo-wide setup changes and `Projects/nlm/WORKLOG.md` for NLM-specific work.

## Files Touched

- `.agents/skills/codex-environment/SKILL.md`
- `.agents/skills/codex-environment/references/logging-and-compaction.md`
- `AGENTS.md`
- `HANDOFF.md`
- `README.md`
- `WORKLOG.md`

## Commands/Checks

- `git clone --branch dev https://github.com/ewallt/codex-environment.git /Users/tom/Documents/codex-test/codex-environment`
- `bash bootstrap/install-skills.sh`
- Copied installed skills into `/Users/tom/.codex/skills`.
- Basic new-skill frontmatter checks passed.
- Full `skill-creator` validation did not run because `yaml` is missing from the local Python environment.
- Committed and pushed setup state to `origin/dev` at `1eadb3e`.
