# NLM Project

## Purpose

Automated video pipeline: write source documents -> upload to NotebookLM notebook -> generate cinematic video -> download -> publish to YouTube. Videos are organized into playlists. One notebook per playlist topic.

## CLI

- **Command:** `nlm` on PATH or `C:\Users\tomew\.local\bin\nlm.EXE`
- **Always prefix:** `$env:PYTHONIOENCODING="utf-8"`
- **Version:** v0.6.0
- **Network:** `nlm` makes direct HTTPS calls to `notebooklm.google.com`. In this Codex setup, sandboxed PowerShell blocks outbound HTTPS; run NLM commands with escalated/out-of-sandbox execution when network is required.
- **Account:** ewalltom@gmail.com

## Key Paths

| Item | Path |
|------|------|
| Source docs | `C:\Users\tomew\Documents\codex-test\Projects\nlm\sources\` |
| Google Docs bridge notes | `C:\Users\tomew\Documents\codex-test\Projects\nlm\docs\google-docs-bridge.md` |
| Videos (downloaded) | `C:\Users\tomew\Videos\[playlist]\Not Yet in YouTube\` |
| Video dashboard | `C:\Users\tomew\Documents\agent-test\documents\video-dashboard-data.json` |
| YouTube playlists config | `C:\Users\tomew\Documents\agent-test\documents\youtube-playlists.json` |

## Active Notebooks

| Playlist | Notebook ID |
|----------|-------------|
| History Potpourri | `6e7fae88-0e36-48a2-b04a-a8187b683dbe` |
| Geography Potpourri | `ee05b643-fa50-45d8-b1b7-ecbb04138895` |
| World War Two | `dc673f24-f901-4f9d-bd72-47016c90ca6f` |
| Movements in Modern Art | `6537a3fb-cf88-48cc-9c70-f6a69f132aa8` |
| Big Ideas | `1dbe88d0-ca46-4a0a-b02e-5d1401af380e` |
| Tips for Healthy Aging | `e165ae6b-2e83-4965-b7e3-c34cb5e6cec4` |
| The Everlasting Covenant | `62ca1cd4-11db-4c58-9936-7d42241ee4ea` |

## Playlist Guidance

### Geography Potpourri

- Scope is broad: strange places, geographic extremes, borders, rivers, climate zones, migration routes, cities, physical geography, human geography, and map-based stories are all valid.
- Adapt tone to the topic for best cinematic results; it does not need to match Point Nemo's mood if another tone fits better.
- Use the Point Nemo example as the minimum target size: roughly 6 scenes. For testing, slightly larger is acceptable, up to about 33% more, usually around 8 scenes.
- Use a YouTube-ready title up front, not a temporary working title.

## CLI Gotchas

- **`nlm source add`** - file path is a flag, not positional:
  - Correct: `nlm source add <notebook-id> --file path\to\file.md --title "Title" --wait`
  - Incorrect: `nlm source add <notebook-id> path\to\file.md`
- **`--source-ids`** - requires full UUID, not 8-char prefix. Short form silently fails.
- **`--format`** - always pass `--format cinematic` explicitly; default is `explainer` (deprecated).
- **`--style`** - do not use with cinematic format; ignored and may cause issues.
- **Single quotes in `--focus`** - avoid apostrophes inside focus strings; they can be mangled by the shell and silently truncate the prompt.
- **Artifact status** - use `nlm studio status <notebook-id> --json` to list studio artifacts and resolve the full artifact UUID.

## Standing Rules

- Before any NLM operation, verify auth is live: `nlm notebook list`. If it errors, re-auth before continuing.
- Use `--wait` on source uploads so each completes before proceeding.
- Use `--confirm` on video creation to skip the interactive prompt.
- Never use 8-char short IDs where full UUIDs are required (`--source-ids`, download commands).
- After downloading a video, move it from `Not Yet in YouTube\` to the playlist root once uploaded.
- For multi-step or unclear NLM tasks, especially those touching NotebookLM, the dashboard, and YouTube, confirm the plan before executing.

## Normal Pipeline

1. Upload source doc:

```powershell
$env:PYTHONIOENCODING="utf-8"; nlm source add <notebook-id> --file "C:\Users\tomew\Documents\codex-test\Projects\nlm\sources\<filename>.md" --title "<Title>" --wait
```

2. Generate video:

```powershell
$env:PYTHONIOENCODING="utf-8"; nlm video create <notebook-id> --format cinematic --focus "<focus prompt>" --source-ids "<full-source-uuid>" --confirm
```

3. Check status and resolve full artifact UUID:

```powershell
$env:PYTHONIOENCODING="utf-8"; nlm studio status <notebook-id> --json
```

4. Download video:

```powershell
$env:PYTHONIOENCODING="utf-8"; nlm download video <notebook-id> --id <full-artifact-uuid> --output "C:\Users\tomew\Videos\<playlist>\Not Yet in YouTube\<nlmTitle>.mp4"
```

## Dashboard Rules

- Dashboard file: `C:\Users\tomew\Documents\agent-test\documents\video-dashboard-data.json`.
- Do not edit `video-dashboard.html`.
- The dashboard is keyed by `title`; this is the human-readable YouTube title and must be unique.
- Do not use filename or `nlmTitle` as the card key.

Required card shape:

```json
{
  "title": "Human-readable YouTube title",
  "notebook": "Notebook Name matching the playlist",
  "status": "source_ready",
  "skipYt": false,
  "artifactId": null,
  "notes": "",
  "focusPrompt": "The focus prompt used to generate the video",
  "playlist": "Playlist Name",
  "nlmTitle": null,
  "dateAdded": "2026-04-27"
}
```

Status updates:

- Source uploaded: add card with `status: "source_ready"`, `dateAdded`, `notebook`, `playlist`, and all fields above.
- Video created in NLM: set `status: "nlm"`, `artifactId` to the first 8 chars of artifact UUID, `nlmTitle`, and `focusPrompt`.
- Video downloaded: set `status: "downloaded"`.
- Video uploaded to YouTube: set `status: "youtube"`.
- File moved from `Not Yet in YouTube\` to playlist root: no dashboard change.
- Tom manually drags cards to `published` after posting to social; Codex must not do that step.

## YouTube Boundary

- No Codex `youtube-publish` skill is installed yet.
- Treat YouTube publishing as out of scope unless Tom explicitly asks to follow the manual procedure.
- Never flip a YouTube video from Private to Public; Tom does that manually.
- If uploading is requested, use `--private`.

## Google Docs Bridge

- Goal: use Google Docs as a durable message bus for Codex on Windows and Codex on Mac.
- Auth helper: `C:\Users\tomew\Documents\codex-test\tools\google-drive-auth.py`
- Expected Codex OAuth client file: `C:\Users\tomew\.notebooklm-mcp-cli\codex-oauth.keys.json`
- Expected token cache: `C:\Users\tomew\.notebooklm-mcp-cli\codex-gdrive-token.json`
- Required redirect URI: `http://localhost:3456/oauth2callback`
- Suggested shared Drive folder name: `Agent Bridge`
- Suggested docs:
  - `Codex-Windows-Outbox.md`
  - `Codex-Mac-Outbox.md`
- Use the two-doc inbox/outbox pattern unless the volume of messages later requires an archive.
