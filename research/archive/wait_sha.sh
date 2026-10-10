#!/bin/sh
# usage: wait_sha.sh WORKTREE ; waits for the dispatch run on the worktree HEAD, then for its Mathlib bridge job
sha=$(git -C "$1" rev-parse HEAD)
run=""
while [ -z "$run" ]; do
  sleep 45
  run=$(gh api "repos/amaybaum/incompleteness/actions/runs?branch=claude/dim1-dev&event=workflow_dispatch&per_page=5" --jq ".workflow_runs[] | select(.head_sha==\"$sha\") | .id" 2>/dev/null | head -1)
done
echo "RUN_ID $run $sha"
while true; do
  out=$(gh api "repos/amaybaum/incompleteness/actions/runs/$run/jobs?per_page=50" --jq '.jobs[] | select(.name=="Mathlib bridge") | "\(.id) \(.status) \(.conclusion)"' 2>/dev/null)
  case "$out" in *completed*) echo "BRIDGE $out"; break;; esac
  sleep 60
done
