#!/bin/sh
# usage: waitruns.sh RUN [RUN...]; prints status of each when all complete
API=https://api.github.com/repos/amaybaum/incompleteness/actions/runs
while true; do
  done_all=1
  for R in "$@"; do
    s=$(curl -s "$API/$R" | python3 -c "import json,sys;print(json.load(sys.stdin).get('status'))")
    [ "$s" = completed ] || done_all=0
  done
  [ $done_all = 1 ] && break
  sleep 60
done
for R in "$@"; do
  curl -s "$API/$R" | python3 -c "import json,sys;r=json.load(sys.stdin);print('RUN',r['id'],r['status'],r['conclusion'],r['event'],r['head_sha'])"
  curl -s "$API/$R/jobs?per_page=100" | python3 -c "
import json,sys,collections;d=json.load(sys.stdin);js=d['jobs']
print(len(js),collections.Counter(j['conclusion'] for j in js))
for j in js:
  if j['name'] in ('Mathlib bridge','Lean kernel check','Numerical probes') or j['conclusion']!='success': print(j['id'],j['name'],j['conclusion'])"
done
