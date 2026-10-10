R=36962242718
while true; do
  J=$(curl -s "https://api.github.com/repos/amaybaum/incompleteness/actions/runs/$R/jobs?per_page=50")
  B=$(echo "$J" | python3 -c "
import json,sys;d=json.load(sys.stdin)
for j in d.get('jobs',[]):
  if 'Mathlib' in j['name']: print(j['id'],j['status'],j['conclusion'])")
  S=$(curl -s "https://api.github.com/repos/amaybaum/incompleteness/actions/runs/$R" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['status'],d['conclusion'])")
  case "$B" in *completed*) echo "BRIDGE $B"; echo "RUN $S"; break;; esac
  case "$S" in completed*) echo "RUN $S"; break;; esac
  sleep 30
done
