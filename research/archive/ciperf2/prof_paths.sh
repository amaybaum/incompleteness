#!/bin/sh
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/ciperf2
export PYTHONDONTWRITEBYTECODE=1
cd $S/wt/verification/lean/a42
python3 $S/tm.py python3 -m cProfile -o $S/r2a.prof r2a_landed.py > $S/r2a.log 2> $S/r2a.time
python3 $S/tm.py python3 -m cProfile -o $S/r2b2.prof r2b2_census.py > $S/r2b2.log 2> $S/r2b2.time
