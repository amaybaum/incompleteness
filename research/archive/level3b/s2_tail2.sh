#!/bin/sh
# S2 tail sequencer, revision 2 (detached): the H2 replays finish in minutes, the H1 replays in hours, so the
# remaining H1 cells (R_NL, R_5) start now on the two idle cores beside the running R_LL/R_LS H1 replays; the
# remaining H2 cells (R_NL, R_5) run once all four H1 replays have exited; V12 runs only if all eight exit 0.
# Each step is the frozen tool verbatim; this script only sequences.
set -u
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/level3b
LOG=$S/S2_tail.log
say() { echo "[$(date -u +%FT%TZ)] $*" >> "$LOG"; }
wait_markers() {
  for m in "$@"; do
    while ! grep -q "^V11-.* exit" "$S/V11_$m.out" 2>/dev/null; do sleep 60; done
    say "V11 $m: $(grep '^V11-.* exit' "$S/V11_$m.out" | tail -1)"
  done
}
say "sequencer 2 started; launching R_NL H1, R_5 H1"
sh "$S/v11_launch.sh" R_NL H1 &
sh "$S/v11_launch.sh" R_5 H1 &
wait_markers R_LL_H2 R_LS_H2 R_LL_H1 R_LS_H1 R_NL_H1 R_5_H1
say "launching R_NL H2, R_5 H2"
sh "$S/v11_launch.sh" R_NL H2 &
sh "$S/v11_launch.sh" R_5 H2 &
wait
wait_markers R_NL_H2 R_5_H2
FAILS=$(grep -h "^V11-.* exit" "$S"/V11_*.out | grep -vc "exit 0 ")
N=$(grep -h "^V11-.* exit" "$S"/V11_*.out | wc -l)
say "V11 complete: $N exit markers, non-zero exits: $FAILS"
if [ "$FAILS" = 0 ] && [ "$N" = 8 ]; then
  say "launching V12"
  sh "$S/v12.sh" > "$S/v12.out" 2>&1
  say "V12 done: $(tail -1 "$S/v12.out")"
else
  say "V11 failure(s) or missing markers; V12 not launched (stop condition)"
fi
say "sequencer 2 finished"
