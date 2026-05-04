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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--file", required=True, type=Path)
    parser.add_argument("--folder-id", required=True)
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8")
    creds = Credentials.from_authorized_user_file(str(DEFAULT_TOKEN), SCOPES)
    drive = build("drive", "v3", credentials=creds)
    docs = build("docs", "v1", credentials=creds)

    created = drive.files().create(
        body={
            "name": args.title,
            "mimeType": "application/vnd.google-apps.document",
            "parents": [args.folder_id],
        },
        fields="id,name",
    ).execute()

    doc_id = created["id"]
    docs.documents().batchUpdate(
        documentId=doc_id,
        body={
            "requests": [
                {
                    "insertText": {
                        "location": {"index": 1},
                        "text": text,
                    }
                }
            ]
        },
    ).execute()

    print(doc_id)
    print(f"https://docs.google.com/document/d/{doc_id}/edit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
