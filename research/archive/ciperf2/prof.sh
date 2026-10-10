#!/bin/sh
# usage: prof.sh <tag> <part> [noprof]
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/ciperf2
export PYTHONDONTWRITEBYTECODE=1
cd $S/wt/verification/lean
if [ "$3" = noprof ]; then
python3 $S/tm.py python3 dita_support_minimality_probe.py --part $2 > $S/$1.log 2> $S/$1.time
else
python3 $S/tm.py python3 -m cProfile -o $S/$1.prof dita_support_minimality_probe.py --part $2 > $S/$1.log 2> $S/$1.time
fi
