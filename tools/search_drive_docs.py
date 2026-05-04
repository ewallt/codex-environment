#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


DEFAULT_TOKEN = r"C:\Users\tomew\.notebooklm-mcp-cli\codex-gdrive-token.json"
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--order-by", default="modifiedTime desc")
    args = parser.parse_args()

    creds = Credentials.from_authorized_user_file(DEFAULT_TOKEN, SCOPES)
    drive = build("drive", "v3", credentials=creds)
    resp = drive.files().list(
        q=args.query,
        pageSize=50,
        orderBy=args.order_by,
        fields="files(id,name,modifiedTime,mimeType,parents)",
    ).execute()
    print(json.dumps(resp, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
