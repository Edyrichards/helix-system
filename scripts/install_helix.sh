#!/usr/bin/env bash
# install_helix.sh — install Helix into a target project or user-level tool locations.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-.}"
MODE="${2:-project}"

usage() {
  cat <<'EOF'
Usage:
  scripts/install_helix.sh [target-project] [mode]

Modes:
  project   Generate CLAUDE.md and copy Helix source skills into .claude/skills (default)
  claude    Same as project, optimized for Claude Code/Cursor project usage
  hermes    Sync this checkout into ~/.hermes/skills/helix-system

Examples:
  scripts/install_helix.sh /path/to/my-app
  scripts/install_helix.sh . claude
  scripts/install_helix.sh . hermes
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

case "$MODE" in
  project|claude)
    mkdir -p "$TARGET/.claude/skills"
    python "$ROOT/scripts/helix_init.py" "$TARGET" --write
    cp "$ROOT"/source-skills/*.skill.md "$TARGET/.claude/skills/"
    mkdir -p "$TARGET/.helix"
    cp "$ROOT/master-claude-project-instructions.md" "$TARGET/.helix/"
    cp "$ROOT/PERSONA_CATALOG.md" "$TARGET/.helix/"
    cp "$ROOT/GO_TO_MARKET.md" "$TARGET/.helix/" 2>/dev/null || true
    echo "Helix installed into $TARGET"
    echo "Next: paste .helix/master-claude-project-instructions.md into Claude Project Instructions if using Claude Projects."
    ;;
  hermes)
    DEST="${HERMES_HOME:-$HOME/.hermes}/skills/helix-system"
    mkdir -p "$DEST"
    rsync -a --delete \
      --exclude '.git' \
      --exclude 'evals/runs' \
      --exclude 'evals/swarms' \
      "$ROOT/" "$DEST/"
    if [[ -f "$DEST/agent.md" ]]; then cp "$DEST/agent.md" "$DEST/SKILL.md"; fi
    echo "Helix synced to Hermes skill dir: $DEST"
    ;;
  *)
    echo "Unknown mode: $MODE" >&2
    usage
    exit 1
    ;;
esac
