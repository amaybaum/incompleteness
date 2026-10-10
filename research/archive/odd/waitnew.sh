#!/bin/sh
# usage: waitnew.sh <sha> <exclude-run-id>  -- wait for a new workflow_dispatch verify.yml run on sha, then summarize
SHA=$1; EX=$2; RUN=""
for i in $(seq 1 40); do
  RUN=$(gh api "repos/amaybaum/incompleteness/actions/runs?event=workflow_dispatch&head_sha=$SHA&per_page=10" --jq ".workflow_runs[] | select(.path==\".github/workflows/verify.yml\" and .id != $EX) | .id" | head -1)
  [ -n "$RUN" ] && break; sleep 15
done
echo "run=$RUN"; [ -z "$RUN" ] && exit 1
for i in $(seq 1 240); do
  S=$(gh api repos/amaybaum/incompleteness/actions/runs/$RUN --jq '"\(.status) \(.conclusion) attempt=\(.run_attempt) sha=\(.head_sha) event=\(.event)"')
  case "$S" in completed*) echo "$S"; break;; esac
  sleep 30
done
gh api "repos/amaybaum/incompleteness/actions/runs/$RUN/jobs?per_page=100" --jq '"jobs=\(.total_count)", ([.jobs[].conclusion] | group_by(.) | map("\(.[0]):\(length)") | join(" "))'
gh api "repos/amaybaum/incompleteness/actions/runs/$RUN/jobs?per_page=100" --jq '.jobs[] | select(.name|startswith("Numerical probes /")|not) | "  \(.id) \(.name) \(.conclusion)"'
