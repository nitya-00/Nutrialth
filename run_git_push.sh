#!/bin/bash
set -euo pipefail
REPO_DIR="/Users/apple/Nutrialth"
cd "$REPO_DIR"
if [ "${DRY_RUN:-0}" = "1" ]; then
  echo "DRY_RUN=1; git status --porcelain:"
  git status --porcelain
  exit 0
fi
git add .
if ! git diff --cached --quiet; then
  git commit -m "auto update $(date)"
  git push origin main
else
  echo "No changes to commit."
fi
