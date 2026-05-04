# Google Docs Bridge

Use Google Docs as a durable message bus for Codex on Windows and Codex on Mac.

## Auth

- Helper script: `C:\Users\tomew\Documents\codex-test\tools\google-drive-auth.py`
- Expected OAuth client JSON: `C:\Users\tomew\.notebooklm-mcp-cli\codex-oauth.keys.json`
- Expected token cache: `C:\Users\tomew\.notebooklm-mcp-cli\codex-gdrive-token.json`
- Redirect URI: `http://localhost:3456/oauth2callback`

## Shared Drive

- Suggested folder: `Agent Bridge`
- Suggested docs:
  - `Codex-Windows-Outbox.md`
  - `Codex-Mac-Outbox.md`

## Protocol

- Each Codex instance writes to its own outbox.
- The other instance reads the outbox and replies in its own doc.
- Keep the exchange flat until message volume makes archiving useful.
