#!/bin/sh
# EQ-D deterministic replay: rerun every script and require byte-identical output to the recorded .out files.
# Usage: sh replay.sh   (from any directory)
set -u
cd "$(dirname "$0")" || exit 2
export PYTHONDONTWRITEBYTECODE=1
status=0
for s in fa_lift:7 cm_class: m1_choi: teleport: qt_faces: mixc_corollary:; do
  name=${s%%:*}; arg=${s#*:}
  tmp=$(mktemp -p . "replay.${name}.XXXXXX")
  if [ -n "$arg" ]; then python3 "$name.py" "$arg" > "$tmp" 2>&1; else python3 "$name.py" > "$tmp" 2>&1; fi
  rc=$?
  if [ $rc -eq 0 ] && cmp -s "$tmp" "$name.out"; then
    echo "REPLAY-MATCH  $name  ($(grep -c '^PASS' "$name.out") PASS lines; $(tail -1 "$name.out" | cut -c1-60)...)"
  else
    echo "REPLAY-FAIL   $name  (exit $rc)"; diff "$tmp" "$name.out" | head -20; status=1
  fi
  rm -f "$tmp"
done
[ $status -eq 0 ] && echo "ALL REPLAYS MATCH" || echo "REPLAY MISMATCH — results void until resolved"
exit $status
