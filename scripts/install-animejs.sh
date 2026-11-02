#!/usr/bin/env bash
set -euo pipefail

# Download upstream source for local reference; project runtime uses npm animejs@4.
animejs_repo_dir="${DESIGNME_ANIMEJS_REPO_DIR:-${HOME}/.agents/tools/animejs}"
animejs_upstream='https://github.com/juliangarnier/anime.git'
mkdir -p "$(dirname "$animejs_repo_dir")"
if [[ -e "$animejs_repo_dir" ]]; then
  if [[ ! -d "$animejs_repo_dir/.git" ]]; then
    printf 'Anime.js destination exists but is not a Git checkout: %s\n' "$animejs_repo_dir" >&2
    exit 1
  fi
  animejs_origin="$(git -C "$animejs_repo_dir" remote get-url origin)"
  case "$animejs_origin" in
    https://github.com/juliangarnier/anime|https://github.com/juliangarnier/anime.git|git@github.com:juliangarnier/anime.git) ;;
    *) printf 'Anime.js checkout has an unexpected origin: %s\n' "$animejs_repo_dir" >&2; exit 1 ;;
  esac
else
  git clone --depth 1 "$animejs_upstream" "$animejs_repo_dir"
fi
# Verify the download and preserve existing checkouts without pulling or resetting.
git -C "$animejs_repo_dir" rev-parse --verify HEAD
printf 'Anime.js source ready: %s\n' "$animejs_repo_dir"
