#!/usr/bin/env bash
set -euo pipefail

# Install only the local native CLI. Do not prompt for OS permissions or operate apps.
if ! command -v agent-desktop >/dev/null 2>&1; then
  if ! command -v npm >/dev/null 2>&1; then
    printf 'Install npm or an official agent-desktop native release first.\n' >&2
    exit 1
  fi
  npm install -g agent-desktop
fi
agent-desktop version
printf '%s\n' 'CLI verified. Before interaction, read agent-desktop skills get desktop/platform and inspect status/permissions in the target graphical session.'
