#!/bin/sh
# usage: waitrun.sh <sha> [event]   -- find the verify.yml run on <sha> (default event workflow_dispatch), wait, summarize
SHA=$1; EV=${2:-workflow_dispatch}
RUN=""
for i in $(seq 1 30); do
  RUN=$(gh api "repos/amaybaum/incompleteness/actions/runs?event=$EV&head_sha=$SHA&per_page=5" --jq '.workflow_runs[] | select(.path==".github/workflows/verify.yml") | .id' | head -1)
  [ -n "$RUN" ] && break
  sleep 20
done
echo "run=$RUN"
[ -z "$RUN" ] && { echo "NO_RUN_FOUND"; exit 1; }
for i in $(seq 1 240); do
  S=$(gh api repos/amaybaum/incompleteness/actions/runs/$RUN --jq '"\(.status) \(.conclusion) attempt=\(.run_attempt) sha=\(.head_sha)"')
  case "$S" in completed*) echo "$S"; break;; esac
  sleep 30
done
gh api "repos/amaybaum/incompleteness/actions/runs/$RUN/jobs?per_page=100" --jq '[.jobs[].conclusion] | group_by(.) | map("\(.[0]):\(length)") | join(" ")'
gh api "repos/amaybaum/incompleteness/actions/runs/$RUN/jobs?per_page=100" --jq '.jobs[] | "  \(.id) \(.name) \(.conclusion)"'
