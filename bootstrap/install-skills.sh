#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dest="${HOME}/.agents/skills"

mkdir -p "$dest"

for skill_dir in "$repo_root/.agents/skills"/*; do
  [ -d "$skill_dir" ] || continue
  name="$(basename "$skill_dir")"
  rm -rf "$dest/$name"
  cp -R "$skill_dir" "$dest/$name"
done

echo "Installed Codex skills to $dest"
