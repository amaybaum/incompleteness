#!/bin/sh
# usage: waitpush.sh <sha> -- wait for the push-event verify.yml run on sha (branch main), then summarize
SHA=$1; RUN=""
for i in $(seq 1 40); do
  RUN=$(gh api "repos/amaybaum/incompleteness/actions/runs?event=push&head_sha=$SHA&per_page=10" --jq '.workflow_runs[] | select(.path==".github/workflows/verify.yml" and .head_branch=="main") | .id' | head -1)
  [ -n "$RUN" ] && break; sleep 15
done
echo "run=$RUN"; [ -z "$RUN" ] && exit 1
for i in $(seq 1 240); do
  S=$(gh api repos/amaybaum/incompleteness/actions/runs/$RUN --jq '"\(.status) \(.conclusion) attempt=\(.run_attempt) sha=\(.head_sha) event=\(.event) branch=\(.head_branch)"')
  case "$S" in completed*) echo "$S"; break;; esac
  sleep 30
done
gh api "repos/amaybaum/incompleteness/actions/runs/$RUN/jobs?per_page=100" --jq '"jobs=\(.total_count)", ([.jobs[].conclusion] | group_by(.) | map("\(.[0]):\(length)") | join(" "))'
gh api "repos/amaybaum/incompleteness/actions/runs/$RUN/jobs?per_page=100" --jq '.jobs[] | select(.name|startswith("Numerical probes /")|not) | "  \(.id) \(.name) \(.conclusion)"'
