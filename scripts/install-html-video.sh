#!/usr/bin/env bash
set -euo pipefail

# Download upstream source for local reference; dependency build and rendering are separate explicit steps.
html_video_repo_dir="${DESIGNME_HTML_VIDEO_REPO_DIR:-${HOME}/.agents/tools/html-video}"
html_video_upstream='https://github.com/nexu-io/html-video.git'
mkdir -p "$(dirname "$html_video_repo_dir")"
if [[ -e "$html_video_repo_dir" ]]; then
  if [[ ! -d "$html_video_repo_dir/.git" ]]; then
    printf 'html-video destination exists but is not a Git checkout: %s\n' "$html_video_repo_dir" >&2
    exit 1
  fi
  html_video_origin="$(git -C "$html_video_repo_dir" remote get-url origin)"
  case "$html_video_origin" in
    https://github.com/nexu-io/html-video|https://github.com/nexu-io/html-video.git|git@github.com:nexu-io/html-video.git) ;;
    *) printf 'html-video checkout has an unexpected origin: %s\n' "$html_video_repo_dir" >&2; exit 1 ;;
  esac
else
  git clone --depth 1 "$html_video_upstream" "$html_video_repo_dir"
fi
# Verify the download and preserve existing checkouts without pulling or resetting.
git -C "$html_video_repo_dir" rev-parse --verify HEAD
printf 'html-video source ready: %s\n' "$html_video_repo_dir"
