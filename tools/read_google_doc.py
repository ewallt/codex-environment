#!/usr/bin/env python3
from __future__ import annotations

import argparse

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


DEFAULT_TOKEN = r"C:\Users\tomew\.notebooklm-mcp-cli\codex-gdrive-token.json"
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]


def extract_text(doc: dict) -> str:
    parts = []
    for block in doc.get("body", {}).get("content", []):
        paragraph = block.get("paragraph")
        if not paragraph:
            continue
        for element in paragraph.get("elements", []):
            text_run = element.get("textRun")
            if text_run and "content" in text_run:
                parts.append(text_run["content"])
    return "".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--doc-id", required=True)
    args = parser.parse_args()

    creds = Credentials.from_authorized_user_file(DEFAULT_TOKEN, SCOPES)
    docs = build("docs", "v1", credentials=creds)
    doc = docs.documents().get(documentId=args.doc_id).execute()
    print(extract_text(doc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
