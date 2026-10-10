#!/bin/sh
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/a30
cd /home/user/incompleteness
G=verification/lean/edge_rigidity_probe.py
for combo in "retired admits" "retired restricts" "retired D" "D admits" "D restricts"; do
  set -- $combo
  if [ "$1" = retired ]; then cp $S/guard-retired.py $G; else cp $S/guard-D.py $G; fi
  cp $S/road-$2.md verification/ROADMAP.md
  python3 $G > $S/gm-$1-$2.txt 2>&1
  echo "$1 $2 exit=$? pass=$(grep -cE '^\s*PASS' $S/gm-$1-$2.txt) fail=$(grep -cE '^\s*FAIL' $S/gm-$1-$2.txt)"
done
git checkout -- $G verification/ROADMAP.md
git status --short
