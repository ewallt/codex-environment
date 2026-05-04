#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


DEFAULT_TOKEN = Path(r"C:\Users\tomew\.notebooklm-mcp-cli\codex-gdrive-token.json")
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]


CONTENT = """Codex to Codex Google Docs Bridge Setup

Purpose

Use Google Docs as a durable message bus between Codex on Windows and Codex on Mac. Each instance writes to a shared inbox/outbox document in Drive. Tom can use the docs as a handoff layer without copy/pasting between terminals.

What to create in Google Cloud Console

1. Create or choose a Google Cloud project for the Codex bridge.
2. Enable Google Drive API and Google Docs API.
3. Configure the OAuth consent screen.
4. Create a new OAuth client ID for this bridge.
5. Use the Web application client type.
6. Add this exact redirect URI:
   http://localhost:3456/oauth2callback
7. Download the client JSON and save it on the machine running Codex.

Files and paths on the Codex machine

- OAuth client JSON: C:\\Users\\tomew\\.notebooklm-mcp-cli\\codex-oauth.keys.json
- Token cache: C:\\Users\\tomew\\.notebooklm-mcp-cli\\codex-gdrive-token.json
- Auth helper: C:\\Users\\tomew\\Documents\\codex-test\\tools\\google-drive-auth.py

How to mint the token

1. Run the auth helper.
2. Sign in in the browser when prompted.
3. Confirm the browser says the authorization is complete.
4. The helper should write the token file.
5. Re-run the helper only if the token file is missing or stale.

How to verify access

After the token exists, run a minimal Drive API read. If the call returns file metadata, the bridge is live.

Suggested Drive layout

- Shared folder: Agent Bridge
- Codex Windows inbox/outbox doc: Codex-Windows-Outbox
- Codex Mac inbox/outbox doc: Codex-Mac-Outbox

Simple protocol

1. Each agent reads the other agent's most recent message before replying.
2. Each agent overwrites its own outbox with one fresh message.
3. Keep the message short and task-focused.
4. If a message needs to persist as a record, copy it into a separate archive doc.

Recommended message format

Header
Date
Short topic line
Bulleted action items or decisions

What to avoid

- Do not rely on chat memory for durable state.
- Do not reuse the Claude Code bridge docs for this channel.
- Do not let the shared token file drift back to the older NotebookLM/Claude Code setup.

Practical first test

After setup, have one Codex instance write a short note into its outbox and have the other instance read it back and respond.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", default="Codex to Codex Google Docs Bridge Setup")
    args = parser.parse_args()

    creds = Credentials.from_authorized_user_file(str(DEFAULT_TOKEN), SCOPES)
    docs = build("docs", "v1", credentials=creds)

    created = docs.documents().create(body={"title": args.title}).execute()
    doc_id = created["documentId"]

    requests = [
        {
            "insertText": {
                "location": {"index": 1},
                "text": CONTENT,
            }
        }
    ]
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()

    print(doc_id)
    print(f"https://docs.google.com/document/d/{doc_id}/edit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
