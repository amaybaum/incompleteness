#!/bin/sh
# usage: waitjob.sh <job-id> -- wait until a job completes, print its conclusion
for i in $(seq 1 240); do
  S=$(gh api repos/amaybaum/incompleteness/actions/jobs/$1 --jq '"\(.status) \(.conclusion)"')
  case "$S" in completed*) echo "$S"; exit 0;; esac
  sleep 30
done
echo timeout
