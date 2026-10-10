#!/bin/sh
# Rebuild the simulated KT4-PREM-1 chain (F, C1, S1, S2) from D in a detached worktree and run every stage check
# and countercontrol. Local only; nothing is pushed.
set -e
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/kt4prem
WT=$S/sim-wt
D=bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58
RD=verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit
cd /home/user/incompleteness
[ -d $WT ] && git worktree remove --force $WT
git worktree add --detach $WT $D >/dev/null 2>&1
cd $WT
TR='

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1'
G="git -c user.name=Claude -c user.email=noreply@anthropic.com"
mkdir -p $RD
cp $S/round/preregistration.md $RD/preregistration.md
git add $RD/preregistration.md && $G commit -S -q -m "KT4-PREM-1: preregistration (candidate F)$TR"
F=$(git rev-parse HEAD)
cp $S/round/controls.py $RD/controls.py
git add $RD/controls.py && $G commit -S -q -m "KT4-PREM-1 C1: frozen controls.py$TR"
C1=$(git rev-parse HEAD)
git show e941e708:verification/lean/kt4_prem1_probe.py > verification/lean/kt4_prem1_probe.py
cp $S/../indep/indep_check.py verification/lean/kt4_prem1_indep_check.py
python3 $S/tools/mkworkflow.py $S/round/controls.py > $S/round/verify.yml.edited
cp $S/round/verify.yml.edited .github/workflows/verify.yml
git add verification/lean/kt4_prem1_probe.py verification/lean/kt4_prem1_indep_check.py .github/workflows/verify.yml
$G commit -S -q -m "KT4-PREM-1 S1: the probe, the independent check and their workflow shard$TR"
S1=$(git rev-parse HEAD)
cp $S/round/result.md $RD/result.md
git add $RD/result.md && $G commit -S -q -m "KT4-PREM-1 S2: result note (candidate E)$TR"
S2=$(git rev-parse HEAD)
printf 'F %s\nC1 %s\nS1 %s\nS2 %s\n' $F $C1 $S1 $S2 | tee $S/round/sim_ids
PB=$(git rev-parse $F:$RD/preregistration.md); CB=$(git rev-parse $C1:$RD/controls.py)
echo "prereg blob $PB  controls blob $CB  result blob $(git rev-parse $S2:$RD/result.md)  indep blob $(git rev-parse $S1:verification/lean/kt4_prem1_indep_check.py)  workflow blob $(git rev-parse $S1:.github/workflows/verify.yml)"
grep -q "blob \`$CB\`" $RD/preregistration.md && echo "C1: controls blob is the frozen blob recorded in the preregistration" \
  || { echo "C1: MISMATCH -- the preregistration does not record $CB"; exit 1; }
[ "$(git rev-list --parents -n1 $F | cut -d' ' -f2-)" = "$D" ] && echo "F: single parent D"
set +e
echo "== check S1";  python3 $RD/controls.py check $S1 --freeze $F
echo "== self-test"; python3 $RD/controls.py --self-test
echo "== check S2";  python3 $RD/controls.py check $S2 --freeze $F
echo "== verdict S2"; python3 $RD/controls.py verdict $S2
CTL=$WT/$RD/controls.py
mut() {
  name=$1; want=$2; snippet=$3
  git checkout -q --detach $S2
  python3 -c "$snippet"
  git add -A >/dev/null 2>&1
  $G commit -q --no-gpg-sign -m "countercontrol $name" >/dev/null
  out=$(python3 $CTL check $(git rev-parse HEAD) --freeze $F 2>&1)
  got=$(echo "$out" | sed -n 's/^controls: FAILED \([A-Z0-9]*\):.*/\1/p')
  if [ "$got" = "$want" ]; then echo "PASS countercontrol $name -> FAILED $got"; else echo "FAIL countercontrol $name: wanted $want, got: $out"; fi
}
R=$RD/result.md
mut extra-token V1 "p='$R'; s=open(p).read(); open(p,'w').write(s+'\nAlso MAXCONE-MODEL-NOT-ESTABLISHED.\n')"
mut earned-altered V2 "p='$R'; s=open(p).read(); t=s.replace('the closedness foil satisfies hcls','the closedness foil satisfies hcl',1); assert t!=s; open(p,'w').write(t)"
mut rule-missing V3 "p='$R'; s=open(p).read(); i=s.index('## The non-inference rule'); j=s.index('## Evidence'); open(p,'w').write(s[:i]+s[j:])"
mut summary-missing V4 "p='$R'; s=open(p).read(); t=s.replace('kt4_prem1_probe: OK -- 79 checks','kt4_prem1_probe: OK'); assert t!=s; open(p,'w').write(t)"
mut phrase-PH PH "p='$R'; s=open(p).read(); open(p,'w').write(s+'\nHence hgate can be dropped.\n')"
mut prereg-after-F F "p='$RD/preregistration.md'; s=open(p).read(); open(p,'w').write(s+'\n')"
mut roadmap-touched G "p='verification/ROADMAP.md'; s=open(p).read(); open(p,'w').write(s+'\n')"
mut workflow-test-line W "p='.github/workflows/verify.yml'; s=open(p).read(); t='          test \"\${KT4PREM1_RESULT}\" = success\n'; assert s.count(t)==1; open(p,'w').write(s.replace(t,''))"
mut probe-witness P "p='verification/lean/kt4_prem1_probe.py'; s=open(p).read(); a=\"chainW) == Q(-1, 2), 'witness')\"; assert s.count(a)==1; open(p,'w').write(s.replace(a,a.replace('Q(-1, 2)','Q(-1, 3)')))"
mut extra-record-file R "open('$RD/notes.md','w').write('x\n')"
mut indep-witness P "p='verification/lean/kt4_prem1_indep_check.py'; s=open(p).read(); a=\"('M_cl', 'H (KT4Core)', passed(\"; assert s.count(a)==1; open(p,'w').write(s.replace(a, \"('M_cl', 'H (KT4Core)', not passed(\"))"
mut final-missing V4 "p='$R'; s=open(p).read(); t=s.replace('FINAL: 124 exact checks, 0 failed; claims AGREE','FINAL: 124 exact checks'); assert t!=s; open(p,'w').write(t)"
mut ind-token-negated V1 "p='$R'; s=open(p).read(); t=s.replace('INDEPENDENT-REPLICATION-VERIFIED','INDEPENDENT-REPLICATION-NOT-ESTABLISHED'); assert t!=s; open(p,'w').write(t)"
mut lean-source-changed G "p='verification/lean-mathlib/OIBridge/K2Guard.lean'; s=open(p).read(); open(p,'w').write(s+'\n')"
git checkout -q --detach $S2
