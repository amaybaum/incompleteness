#!/bin/sh
# Gate V12 (preregistration section 7.3): byte-identical rerun of Stage A of R_5 after every other stage; the
# artifact's sha256 unchanged. The rerun is the frozen driver verbatim (driver3b.py A R_5 4) with a fresh,
# empty checkpoint root (L3B_CKPT), so every one of the 143 kappa is recomputed. Before the rerun the sealed
# artifact and the sealed S1 Stage-A log are copied aside; after it the rerun's sha256 is compared with the
# sealed one. The driver appends its progress lines to logs/stageA_R_5.log (the S1 log sealed at 3524bb3b);
# those lines are captured on stdout, written into logs/V12.log, and the S1 log is restored to its sealed
# content so that no S1 boundary artifact changes. On a mismatch the rerun artifact is preserved in the
# scratchpad as evidence and the sealed artifact is restored: a stop condition, not a repair.
set -u
ROUND=/home/user/incompleteness/verification/programmes/oi-qm/interface/round-l3b-orthogonal-rule-controls
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/level3b/v12
CK=$HOME/.l3b_ckpt_v12
SEALED=dcf04f62d4de5c7748cfda979d562b22eaa2b3f0f84c3e87c4f717b63800229b
mkdir -p "$S"
if [ -e "$CK" ]; then echo "checkpoint root $CK already exists; refusing"; exit 2; fi
cp "$ROUND/results/stageA_R_5.json" "$S/sealed_stageA_R_5.json"
cp "$ROUND/logs/stageA_R_5.log" "$S/sealed_stageA_R_5.log"
H0=$(sha256sum "$S/sealed_stageA_R_5.json" | cut -c1-64)
cd "$ROUND/code/level3b" || exit 2
V="$ROUND/logs/V12.log"
{
  echo "V12 byte-identical rerun of Stage A, R_5 (after every other stage of S1 and S2)"
  echo "command: L3B_CKPT=$CK python3 driver3b.py A R_5 4   (fresh, empty checkpoint root: all 143 kappa recomputed)"
  echo "sealed artifact stageA_R_5.json (S1, commit 3524bb3b) sha256 $H0"
  echo "frozen expectation (preregistration section 7.3, V12): sha256 $SEALED unchanged"
  echo "driver output follows (the same lines the driver appended to logs/stageA_R_5.log, which is restored to its sealed content):"
} > "$V"
L3B_CKPT=$CK python3 driver3b.py A R_5 4 > "$S/v12_driver.out" 2>&1
RC=$?
cat "$S/v12_driver.out" >> "$V"
H1=$(sha256sum "$ROUND/results/stageA_R_5.json" | cut -c1-64)
cp "$S/sealed_stageA_R_5.log" "$ROUND/logs/stageA_R_5.log"
echo "driver exit $RC; rerun artifact sha256 $H1" >> "$V"
if [ "$RC" = 0 ] && [ "$H1" = "$SEALED" ] && [ "$H0" = "$SEALED" ]; then
  echo "GATE V12 OK" >> "$V"
else
  cp "$ROUND/results/stageA_R_5.json" "$S/mismatch_stageA_R_5.json"
  cp "$S/sealed_stageA_R_5.json" "$ROUND/results/stageA_R_5.json"
  echo "rerun artifact preserved at $S/mismatch_stageA_R_5.json; sealed artifact restored" >> "$V"
  echo "GATE V12 FAILED" >> "$V"
fi
tail -3 "$V"
