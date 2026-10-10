#!/bin/sh
# usage: wait_bridge.sh RUN_ID ; polls the Mathlib bridge job once a minute until it concludes
run=$1
while true; do
  out=$(gh api "repos/amaybaum/incompleteness/actions/runs/$run/jobs?per_page=50" --jq '.jobs[] | select(.name=="Mathlib bridge") | "\(.id) \(.status) \(.conclusion)"' 2>/dev/null)
  case "$out" in
    *completed*) echo "BRIDGE $out"; break;;
  esac
  sleep 60
done
gh api "repos/amaybaum/incompleteness/actions/runs/$run" --jq '"RUN \(.status) \(.conclusion)"'
