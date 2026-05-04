#!/usr/bin/env python3
"""
Mint a Google OAuth token for Drive/Docs access using a Codex-specific web client.

The OAuth client used for this bridge must be registered for:
    http://localhost:3456/oauth2callback

This helper uses that exact redirect URI instead of the generic localhost flow
that triggered the Google OAuth policy error.
"""

from __future__ import annotations

import argparse
import json
import os
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

DEFAULT_SECRETS = Path(r"C:\Users\tomew\.notebooklm-mcp-cli\codex-oauth.keys.json")
DEFAULT_TOKEN = Path(r"C:\Users\tomew\.notebooklm-mcp-cli\codex-gdrive-token.json")
DEFAULT_REDIRECT = "http://localhost:3456/oauth2callback"
DEFAULT_SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]


class _CallbackHandler(BaseHTTPRequestHandler):
    auth_code = None
    auth_error = None
    event = None

    def log_message(self, format, *args):  # noqa: A003
        return

    def do_GET(self):  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/oauth2callback":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")
            return

        params = parse_qs(parsed.query)
        if "error" in params:
            _CallbackHandler.auth_error = params["error"][0]
            body = f"Auth failed: {_CallbackHandler.auth_error}".encode("utf-8")
            self.send_response(400)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            _CallbackHandler.event.set()
            return

        code = params.get("code", [None])[0]
        if not code:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing authorization code")
            return

        _CallbackHandler.auth_code = code
        body = b"Authorization complete. You can close this tab."
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        _CallbackHandler.event.set()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--secrets", type=Path, default=DEFAULT_SECRETS)
    parser.add_argument("--token", type=Path, default=DEFAULT_TOKEN)
    parser.add_argument("--scope", action="append", dest="scopes")
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    if not args.secrets.exists():
        raise SystemExit(f"Missing secrets file: {args.secrets}")

    scopes = args.scopes or DEFAULT_SCOPES

    from google_auth_oauthlib.flow import Flow

    client_config = json.loads(args.secrets.read_text(encoding="utf-8"))
    flow = Flow.from_client_config(client_config, scopes=scopes)
    flow.redirect_uri = DEFAULT_REDIRECT
    auth_url, _ = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
    )

    _CallbackHandler.auth_code = None
    _CallbackHandler.auth_error = None
    _CallbackHandler.event = threading.Event()

    server = HTTPServer(("localhost", 3456), _CallbackHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    print("Open this URL in a browser if it does not open automatically:")
    print(auth_url)
    if not args.no_browser:
        webbrowser.open(auth_url, new=1, autoraise=True)

    try:
        _CallbackHandler.event.wait()
        if _CallbackHandler.auth_error:
            raise SystemExit(f"Auth error: {_CallbackHandler.auth_error}")
        if not _CallbackHandler.auth_code:
            raise SystemExit("No authorization code received")
        os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"
        flow.fetch_token(code=_CallbackHandler.auth_code)
        print(f"Token fetched. Writing to: {args.token}")
        args.token.write_text(flow.credentials.to_json(), encoding="utf-8")
        print("Done.")
        return 0
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    raise SystemExit(main())
