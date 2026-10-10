R=$1
while true; do
  B=$(curl -s "https://api.github.com/repos/amaybaum/incompleteness/actions/runs/$R/jobs?per_page=50" | python3 -c "
import json,sys;d=json.load(sys.stdin)
for j in d.get('jobs',[]):
  if j['name']=='Mathlib bridge': print(j['id'],j['status'],j['conclusion'])")
  case "$B" in *completed*) echo "BRIDGE $B"; break;; esac
  sleep 40
done
