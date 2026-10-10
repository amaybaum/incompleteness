#!/bin/sh
# EQ2-B replay: rerun every current probe into replay_self/ and compare its stdout with the recorded .out byte for byte.
# Usage: sh run_all.sh <base>/verification/lean-mathlib/OIBridge/CompositeDimension.lean
CD="$1"
HERE=$(cd "$(dirname "$0")" && pwd)
OUT="$HERE/replay_self"
mkdir -p "$OUT"
status=0
for s in b1_native_class b2_orientation b3_compact b4_lie_light b5_ie1 b6_foils b7_certificates; do
  python3 -I -B "$HERE/$s.py" "$CD" > "$OUT/$s.out" 2> "$OUT/$s.err"
  rc=$?
  if cmp -s "$OUT/$s.out" "$HERE/$s.out"; then same=identical; else same=DIFFERS; status=1; fi
  [ $rc -eq 0 ] || status=1
  printf '%s exit=%s replay=%s script=%s output=%s\n' "$s" "$rc" "$same" \
    "$(sha256sum "$HERE/$s.py" | cut -c1-16)" "$(sha256sum "$HERE/$s.out" | cut -c1-16)"
done
printf 'eq2b_lib sha256=%s\n' "$(sha256sum "$HERE/eq2b_lib.py" | cut -c1-16)"
[ $status -eq 0 ] && echo "run_all: OK" || echo "run_all: FAILED"
exit $status
