#!/bin/sh
# S2 tail sequencer (detached): waits for the R_5 hidden-law chain to finish, then runs V11 for the eight Block-2
# cells in the frozen cell order (two waves of four concurrent single-process replays on the four cores), then
# V12 only if all eight V11 replays exited 0. Each step is the frozen tool verbatim; this script only sequences.
set -u
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/level3b
SEALED3A=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/level3/fast3_stageA_linear.json
LOG=$S/S2_tail.log
say() { echo "[$(date -u +%FT%TZ)] $*" >> "$LOG"; }
say "sequencer started; waiting for S2-CHAIN-4 exit"
while ! grep -q "S2-CHAIN-4 exit" "$S/S2_chain4.log"; do sleep 60; done
RC=$(grep "S2-CHAIN-4 exit" "$S/S2_chain4.log" | tail -1 | awk '{print $3}')
say "S2-CHAIN-4 exit $RC"
[ "$RC" = 0 ] || { say "chain failed; not launching V11"; exit 1; }
wait_markers() {
  for m in "$@"; do
    while ! grep -q "^V11-.* exit" "$S/V11_$m.out" 2>/dev/null; do sleep 60; done
    say "V11 $m: $(grep '^V11-.* exit' "$S/V11_$m.out" | tail -1)"
  done
}
say "wave 1: R_LL H1, R_LL H2, R_LS H1, R_LS H2"
sh "$S/v11_launch.sh" R_LL H1 "$SEALED3A" &
sh "$S/v11_launch.sh" R_LL H2 "$SEALED3A" &
sh "$S/v11_launch.sh" R_LS H1 &
sh "$S/v11_launch.sh" R_LS H2 &
wait
wait_markers R_LL_H1 R_LL_H2 R_LS_H1 R_LS_H2
say "wave 2: R_NL H1, R_NL H2, R_5 H1, R_5 H2"
sh "$S/v11_launch.sh" R_NL H1 &
sh "$S/v11_launch.sh" R_NL H2 &
sh "$S/v11_launch.sh" R_5 H1 &
sh "$S/v11_launch.sh" R_5 H2 &
wait
wait_markers R_NL_H1 R_NL_H2 R_5_H1 R_5_H2
FAILS=$(grep -h "^V11-.* exit" "$S"/V11_*.out | grep -vc "exit 0 ")
say "V11 complete; non-zero exits: $FAILS"
if [ "$FAILS" = 0 ]; then
  say "launching V12"
  sh "$S/v12.sh" > "$S/v12.out" 2>&1
  say "V12 done: $(tail -1 "$S/v12.out")"
else
  say "V11 failure(s); V12 not launched (stop condition)"
fi
say "sequencer finished"
