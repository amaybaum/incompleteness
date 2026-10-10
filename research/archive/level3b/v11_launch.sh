#!/bin/sh
# Launch one frozen V11 replay (replay3b.py H <cell> <H> [sealed]) detached from the harness, so the 2-hour
# background limit does not interrupt it. Output: scratchpad/level3b/V11_<cell>_<H>.out, exit marker appended.
# The gate itself (positions, comparisons, OK line) is entirely replay3b.replay_H; this wrapper only runs it.
set -u
CELL=$1; H=$2; SEALED=${3:-}
CODE=/home/user/incompleteness/verification/programmes/oi-qm/interface/round-l3b-orthogonal-rule-controls/code/level3b
OUT=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/level3b/V11_${CELL}_${H}.out
cd "$CODE" || exit 2
{
  echo "[$(date -u +%FT%TZ)] V11 launch: python3 replay3b.py H $CELL $H $SEALED"
  python3 replay3b.py H "$CELL" "$H" $SEALED
  echo "V11-$CELL-$H exit $? [$(date -u +%FT%TZ)]"
} > "$OUT" 2>&1
