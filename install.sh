#!/usr/bin/env bash
set -euo pipefail

REPO="${REPO:-ehsantarighat/hyperreal-ai-image-skill}"
BRANCH="${BRANCH:-main}"
SKILL_NAME="${SKILL_NAME:-hyperreal-ai-image-skill}"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.claude/skills}"
TARGET_DIR="$INSTALL_DIR/$SKILL_NAME"
TMP_DIR="$(mktemp -d)"
ZIP_PATH="$TMP_DIR/skill.zip"
ARCHIVE_URL="https://github.com/$REPO/archive/refs/heads/$BRANCH.zip"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Error: '$1' is required but not installed." >&2
    exit 1
  fi
}

need_cmd curl
need_cmd unzip
need_cmd find
need_cmd mkdir
need_cmd cp

printf "Installing %s from %s (%s)...\n" "$SKILL_NAME" "$REPO" "$BRANCH"

mkdir -p "$INSTALL_DIR"

curl -fsSL "$ARCHIVE_URL" -o "$ZIP_PATH"
unzip -q "$ZIP_PATH" -d "$TMP_DIR"

SOURCE_DIR="$(find "$TMP_DIR" -type d -name "$SKILL_NAME" | head -n 1 || true)"

if [ -z "$SOURCE_DIR" ]; then
  echo "Error: Could not find skill directory '$SKILL_NAME' inside repository archive." >&2
  echo "Make sure the repository contains: $SKILL_NAME/SKILL.md" >&2
  exit 1
fi

if [ ! -f "$SOURCE_DIR/SKILL.md" ]; then
  echo "Error: $SOURCE_DIR exists but does not contain SKILL.md." >&2
  exit 1
fi

rm -rf "$TARGET_DIR"
cp -R "$SOURCE_DIR" "$TARGET_DIR"

printf "✅ Installed %s to %s\n" "$SKILL_NAME" "$TARGET_DIR"
printf "Restart Claude Code to load the skill.\n"
