#!/bin/sh
# Build the KT4-PREM-1 predicted execution tree: a single-parent child of D carrying the record directory less the
# result note (drafting preregistration, frozen controls.py), the two frozen scripts and the workflow edit. Local only.
set -e
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/kt4prem
WT=$S/pred-wt
D=bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58
RD=verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit
cd /home/user/incompleteness
[ -d $WT ] && git worktree remove --force $WT
git worktree add --detach $WT $D >/dev/null 2>&1
cd $WT
mkdir -p $RD
cp $S/round/preregistration.md $RD/preregistration.md
cp $S/round/controls.py $RD/controls.py
git show e941e708:verification/lean/kt4_prem1_probe.py > verification/lean/kt4_prem1_probe.py
cp $S/../indep/indep_check.py verification/lean/kt4_prem1_indep_check.py
python3 $S/tools/mkworkflow.py $S/round/controls.py > .github/workflows/verify.yml
git add $RD verification/lean/kt4_prem1_probe.py verification/lean/kt4_prem1_indep_check.py .github/workflows/verify.yml
git -c user.name=Claude -c user.email=noreply@anthropic.com commit -S -q -F - <<'MSG'
KT4-PREM-1 predicted execution tree (disposable design evidence, not for landing)

A single-parent child of D bcbc516f carrying the predicted execution tree
less the result note: the preregistration in its drafting revision, the
frozen controls.py, the probe, the independent countermodel check and the
workflow edit. Not an execution stage.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1
MSG
P=$(git rev-parse HEAD)
echo "predicted $P  tree $(git rev-parse HEAD^{tree})"
echo "parents: $(git rev-list --parents -n1 $P | cut -d' ' -f2-)"
echo "delta(D, P):"; git diff --name-status $D $P
for f in $RD/preregistration.md $RD/controls.py verification/lean/kt4_prem1_probe.py verification/lean/kt4_prem1_indep_check.py .github/workflows/verify.yml; do
  echo "  $(git rev-parse $P:$f)  $f"; done
echo "$P" > $S/round/predicted_sha
