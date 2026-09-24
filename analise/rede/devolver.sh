#!/usr/bin/env bash
# Commit do resultado da coleta no mesmo ramo (usado por .github/workflows/buscar-fontes.yml).
set -u
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add dados/fontes_web dados/externos
if git diff --cached --quiet; then
  echo "Nada novo."
  exit 0
fi
git commit -q -m "buscar-fontes: ${1:-coleta} (${GITHUB_RUN_ID:-local})"
for i in 1 2 3; do
  git pull -q --rebase origin "${GITHUB_REF_NAME}" && git push -q origin "HEAD:${GITHUB_REF_NAME}" && exit 0
  sleep 5
done
exit 1
