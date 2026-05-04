# NLM Worklog

## 2026-05-03 - Post-Compact Skill Created

- Created a new `post-compact` skill at `C:\Users\tomew\.agents\skills\post-compact\`.
- The skill tells Codex to read `HANDOFF.md`, then `WORKLOG.md`, then `PROJECT.md` before resuming work.
- Added a reorientation template so post-compact restarts focus on the current objective, the latest changes, and the next step.

## 2026-05-03 - Pre-Compact Skill Created

- Created a new `pre-compact` skill at `C:\Users\tomew\.agents\skills\pre-compact\`.
- The skill instructs Codex to update `WORKLOG.md` first, then refresh `HANDOFF.md` with the latest context before compaction.
- Added a small handoff template reference so the next session can resume from the most recent working state.

## 2026-05-03 - Google Docs Bridge Skill Created

- Created a new Codex skill at `C:\Users\tomew\.agents\skills\google-docs-bridge\`.
- The skill uses JIT references for setup, read/write operations, shared message protocol, and troubleshooting.
- The skill records the Codex Google OAuth client path, token cache path, redirect URI, and shared `Agent Bridge` Drive folder details.

## 2026-05-03 - Codex OAuth JSON Copied to Google Doc

- Created a Drive doc titled `Codex OAuth Client JSON for Mac`.
- The doc contains the exact Codex OAuth client JSON from `C:\Users\tomew\.notebooklm-mcp-cli\codex-oauth.keys.json` so the Mac setup can copy/paste it.
- Doc ID: `1gwx8aMwaJxLCd6wLPoyARffngHrOXTSM5rC5uOr7vw8`

## 2026-05-03 - Google Docs Bridge Setup Doc Created

- Created a Google Doc titled `Codex to Codex Google Docs Bridge Setup`.
- Moved it into a dedicated Drive folder named `Agent Bridge`.
- The doc explains the Codex OAuth client, redirect URI, token flow, Drive verification, and a simple two-doc message protocol.

## 2026-05-03 - Google OAuth Scope Mismatch Sent to CC

- Reported that the Google OAuth callback works on port `3456`, but token exchange fails at `flow.fetch_token()`.
- The returned token scopes include YouTube scopes even though the helper requested only Drive and Docs scopes.
- Asked CC for the exact code change needed so oauthlib accepts and writes the token successfully.

## 2026-05-03 - Redirect URI Completion Check Sent to CC

- Asked Claude Code to confirm whether the Google Cloud Console OAuth redirect URI update to `http://localhost:3456/oauth2callback` is actually finished.
- The message asks for the exact field that should show the change and the fastest confirmation check.
- This is the remaining uncertainty in the Google Docs bridge setup.

## 2026-05-03 - Google Docs Auth Troubleshooting Sent to CC

- Replaced the Google Docs bridge setup question with a concrete auth failure report for Claude Code.
- The message now asks CC to troubleshoot why the browser consent completes but the token file is not refreshed.
- Verified files mentioned in the report:
  - `C:\Users\tomew\.notebooklm-mcp-cli\codex-oauth.keys.json`
  - `C:\Users\tomew\Documents\codex-test\tools\google-drive-auth.py`
  - `C:\Users\tomew\.notebooklm-mcp-cli\gdrive-token.json`

## 2026-05-03 - Google Docs Bridge Setup Written Down

- Added a Codex-specific Google Docs bridge section to `Projects/nlm/PROJECT.md`.
- Added `Projects/nlm/docs/google-docs-bridge.md` with the auth path, redirect URI, shared Drive folder name, and inbox/outbox protocol.
- Updated `tools/google-drive-auth.py` to use Codex-specific default client paths and the existing Drive token cache path:
  - `C:\Users\tomew\.notebooklm-mcp-cli\codex-oauth.keys.json`
  - `C:\Users\tomew\.notebooklm-mcp-cli\codex-gdrive-token.json`
- Switched the callback port to `3456` to avoid a localhost conflict and added explicit token-write logging.
- The remaining blocker is a Codex-specific OAuth client JSON file created in Google Cloud Console.

## 2026-05-03 - Google Docs Bridge Question Sent

- Wrote a bridge note asking Claude Code how Codex on Windows should be set up to read and write Google Docs.
- The message asks for the best access path, setup steps, storage location, protocol shape, and caveats.
- This is the first step toward using Google Docs as a Codex-to-Codex message bus.

## 2026-05-03 - Bridge Protocol Clarified

- Replaced the Claude Code bridge note with a plain explanation of how Codex and Claude Code communicate.
- The bridge now says messages live in `agent-bridge\codex\ForCodex.md` and `agent-bridge\claude-code\ForClaudeCode.md`.
- The note also states that durable state belongs in `PROJECT.md`, `HANDOFF.md`, and `WORKLOG.md`, not in session memory.

## 2026-04-28 - Handoff Refreshed

- Updated `Projects/nlm/HANDOFF.md` to reflect the latest state of the NLM workflow.
- The handoff now records the bridge setup, the three Geography Potpourri source uploads, and the three in-progress videos.

## 2026-04-28 - Three Geography Potpourri Videos Started

- Started video generation for:
  - `Surtsey: The Island That Didn't Exist Yesterday`
  - `The River That Belongs to Two Worlds`
  - `The Lake That Exists Only After the Rain`
- Updated the shared dashboard to `status: nlm` for all three.

## 2026-04-28 - Scene Writer Focus Prompt Rules Updated

- Added Geography Potpourri focus prompt rules to `C:\Users\tomew\.agents\skills\scene-writer\SKILL.md`.
- The rules now say to lead with the angle, state the hook explicitly, keep the prompt to 3-5 sentences, and place tone language after the hook.

## 2026-04-28 - Geography Potpourri Batch Uploaded

- Uploaded three new Geography Potpourri sources to NotebookLM:
  - `Surtsey: The Island That Didn't Exist Yesterday`
  - `The River That Belongs to Two Worlds`
  - `The Lake That Exists Only After the Rain`
- Updated the shared dashboard to mark the three topics as `source_ready`.

## 2026-04-28 - Brasilia Video Started

- Started a cinematic NLM video from `Projects/nlm/sources/brasilia-the-city-decided-before-it-was-built.md`.
- NotebookLM artifact ID: `1e614835-515f-4221-a452-ca326268ac32`.
- Updated the shared dashboard to `status: nlm`.

## 2026-04-28 - Brasilia Source Uploaded

- Uploaded `Projects/nlm/sources/brasilia-the-city-decided-before-it-was-built.md` to Geography Potpourri.
- Source title: `Brasília: The City Decided Before It Was Built`.
- Source ID: `d575fe7f-9c27-41cb-adad-3f179cda34c5`.

## 2026-04-28 - Brasilia Scene Draft Sent

- Wrote `Projects/nlm/sources/brasilia-the-capital-built-in-the-empty-middle.md` using the scene-writer structure.
- Sent the source doc to Claude Code through the agent bridge for review comments.

## 2026-04-28 - AGENTS Skill Rule Added

- Updated `C:\Users\tomew\Documents\codex-test\AGENTS.md` to require `skill-creator` before creating or modifying any skill.
- This makes the skill-creation routing rule durable for future Codex sessions.

## 2026-04-28 - Skill Creator Encoding Rule Added

- Updated `C:\Users\tomew\.agents\skills\skill-creator\SKILL.md` to require UTF-8 without BOM for new or rewritten `SKILL.md` files.
- This is meant to prevent the skill loader from skipping skills because the YAML frontmatter delimiter is no longer at byte 1.

## 2026-04-28 - Playlist Ideas Skill Created

- Created a Codex-side `playlist-ideas` skill at `C:\Users\tomew\.agents\skills\playlist-ideas\SKILL.md`.
- The skill generates playlist topic ideas by checking the dashboard for existing videos, choosing underrepresented structural angles, and filtering duplicates.

## 2026-04-28 - Agent Messaging Protocol Added

- Added a bridge-folder recommendation to `Projects/nlm/README.md`.
- Recommended `C:\Users\tomew\Documents\agent-bridge\` with separate `claude-code\` and `codex\` inboxes.

## 2026-04-28 - YouTube Publish Setup Added

- Added a YouTube publish setup section to `Projects/nlm/README.md`.
- Asked Claude Code where Codex should keep `youtube-upload.py`, the gitignored credential files, and the `youtube-publish` skill.

## 2026-04-28 - Remaining Skill Clarified

- Clarified in `Projects/nlm/README.md` that the only remaining named NLM skill in the project docs is `youtube-publish`.
- Noted that the current docs do not define any additional missing NLM skill names.

## 2026-04-28 - README Refreshed

- Rewrote `Projects/nlm/README.md` to contain only the current ForCodex response.
- Removed older coordination notes from the README so it reflects the active NLM backup state only.

## 2026-04-27 - Handoff Written

- Wrote `Projects/nlm/HANDOFF.md` to capture what the NLM work is, what has been done, and the next step.
- Next step recorded in the handoff: implement the remaining NLM skills; `scene-writer` JIT refactor is deferred.

## 2026-04-27 - Scene Writer Test Passed

- Ran the scene-writer rubric against the Pheasant Island source doc and the test trace.
- The run passed flow compliance, output compliance, and drift checks.
- Current recommendation: scene-writer works, but should still be refactored to the JIT layout before heavy reuse.

## 2026-04-27 - Pheasant Island Source Uploaded

- Uploaded `Projects/nlm/sources/the-island-that-changes-countries-every-six-months.md` to Geography Potpourri.
- Notebook ID: `ee05b643-fa50-45d8-b1b7-ecbb04138895`.
- Source ID: `15f07c92-b392-43bd-ac46-6ef0d0f03793`.
- Upload completed with status `ready`.

## 2026-04-27 - Scene Writer Test Source Drafted

- Used `scene-writer` to draft `Projects/nlm/sources/the-island-that-changes-countries-every-six-months.md`.
- Topic: Pheasant Island for Geography Potpourri.
- Verified core facts with web sources before writing because Tom requested no guessing.
- Created test trace at `Projects/nlm/tmp/scene-writer-test-trace.md`.

## 2026-04-27 - Scene Writer Test Mode Added

- Added temporary Test Mode instructions to `C:\Users\tomew\.agents\skills\scene-writer\SKILL.md`.
- Test trace path is `Projects\nlm\tmp\scene-writer-test-trace.md`.
- Remove the Test Mode section after the scene-writer test passes.

## 2026-04-27 - Skill Creator JIT Implemented

- Updated user-installed `skill-creator` at `C:\Users\tomew\.agents\skills\skill-creator\SKILL.md`.
- Added `C:\Users\tomew\.agents\skills\skill-creator\references\jit-instruction-delivery.md`.
- Replaced the external Claude-side JIT experiment pointer with a local self-contained reference.
- Future multi-step skills should use `SKILL.md` as orchestrator and `READ NOW: references/<file>.md` for phase-specific instructions.

## 2026-04-27 - Geography Potpourri Guidance

- Added `Geography Potpourri` playlist guidance to `PROJECT.md`.
- Scope includes strange places, geographic extremes, borders, rivers, climate zones, migration routes, cities, physical geography, human geography, and map-based stories.
- Scene-writer output should use a YouTube-ready title up front and target at least Point Nemo length, with up to roughly 8 scenes acceptable for testing.

## 2026-04-27 - Scene Writer Example Added

- Added Tom's Point Nemo source document as `C:\Users\tomew\.agents\skills\scene-writer\references\point-nemo-example.md`.
- Updated `scene-writer` skill to reference the example when scene density, tone, or structure is uncertain.

## 2026-04-27 - Scene Writer Setup

- Created `Projects/nlm/sources/` for generated NLM source documents.
- Updated `PROJECT.md` with corrected NLM pipeline commands, dashboard card rules, title-key rule, and YouTube boundaries.
- Created `scene-writer` skill at `C:\Users\tomew\.agents\skills\scene-writer\SKILL.md`.
- Updated `HANDOFF.md`; next step is testing the `scene-writer` skill on a source-document request.

## 2026-04-27 - Project Folder Created

- Created `Projects/nlm/` for durable NLM project context.
- Added stubs for project overview, handoff, worklog, setup notes, troubleshooting, and command reference.
- Noted that the installed NLM skill lives outside the project folder at `C:\Users\tomew\.agents\skills\nlm-skill\SKILL.md`.
