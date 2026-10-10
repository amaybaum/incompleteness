#!/bin/sh
# coordinator replay of the EQ3-P exact probes and float explorations; compares stdout with the thread's .out files
cd /tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/eqreview/replayEQ3
CD=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/eq/base/verification/lean-mathlib/OIBridge/CompositeDimension.lean; K2=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/eq/base/verification/lean-mathlib/OIBridge/K2Guard.lean; P=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/eq3/P
for s in "p1_four_copy_links.py $CD $K2" "p2_audit_twists_foils.py $CD $K2" "p3_general_links.py $CD" "p4_cone_ladder.py" "p5_six_copy.py $CD" "p6_cheap_foils.py $CD" "x1_slocc_orbit_float.py" "x2_sector_float.py"; do
  set -- $s; f=$1; shift
  python3 -I -B $f "$@" > ${f%.py}.out 2> ${f%.py}.err; rc=$?
  if cmp -s ${f%.py}.out $P/${f%.py}.out; then same=identical; else same=DIFFERENT; fi
  echo "$f rc=$rc stderr=$(wc -c < ${f%.py}.err) $same sha=$(sha256sum ${f%.py}.out | cut -c1-16)"
done
