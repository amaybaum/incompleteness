#!/bin/sh
L=20aa54803df5d74e6c67a1341ca022dee340a65b
RUN=""
for i in $(seq 1 30); do
  RUN=$(gh api "repos/amaybaum/incompleteness/actions/runs?branch=main&event=push&head_sha=$L&per_page=5" --jq '.workflow_runs[] | select(.path==".github/workflows/verify.yml") | .id' | head -1)
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
gh api "repos/amaybaum/incompleteness/actions/runs/$RUN/jobs?per_page=100" --jq '.jobs[] | select(.conclusion!="success") | "  \(.id) \(.name) \(.conclusion)"'
