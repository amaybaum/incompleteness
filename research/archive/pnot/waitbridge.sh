#!/bin/sh
SHA=$1
for i in $(seq 1 30); do
  RUN=$(gh api "repos/amaybaum/incompleteness/actions/runs?event=workflow_dispatch&head_sha=$SHA&per_page=5" --jq '.workflow_runs[] | select(.path==".github/workflows/verify.yml") | .id' | head -1)
  [ -n "$RUN" ] && break; sleep 20
done
echo "run=$RUN"
for i in $(seq 1 240); do
  J=$(gh api "repos/amaybaum/incompleteness/actions/runs/$RUN/jobs?per_page=100" --jq '.jobs[] | select(.name=="Mathlib bridge") | "\(.id) \(.status) \(.conclusion)"')
  case "$J" in *completed*) echo "bridge $J"; break;; esac
  sleep 30
done
