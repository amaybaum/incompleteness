#!/bin/sh
# Local simulation of the RELC-SELECT-1 execution chain on candidate F: local objects only, no refs, nothing pushed.
set -e
cd /home/user/incompleteness
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/rcs
D=e2426ba4109dcd719d518aefbd3c417b7c6fdc5b
F=1003b029b4949516e615cea8fbf0531c0ced583b
P=da295a1be51e7d7e2013307b85b0c5f44a9c897a
R=verification/programmes/oi-qm/reconstruction/round-relc-select-1
L=verification/lean-mathlib
X="-c user.name=sim -c user.email=sim@localhost"
export GIT_INDEX_FILE=$S/sim/idx
mk() { t=$(git write-tree); GIT_AUTHOR_DATE='2026-10-08T00:00:00Z' GIT_COMMITTER_DATE='2026-10-08T00:00:00Z' git $X commit-tree --no-gpg-sign $t -p $1 -m "$2"; }
git read-tree $F
git update-index --add --cacheinfo 100644,8cafc140b519495d1687a5507846d320c3c3295f,$R/controls.py
C1=$(mk $F 'sim C1')
for p in $L/OIBridge/RelcSelectParity.lean $L/OIBridge/RelcSelectBlock.lean $L/OIBridge/RelcSelectSqueeze.lean $L/OIBridge/RelcSelectC5.lean $L/OIBridge.lean verification/lean-manuscript-census.json; do
  git update-index --add --cacheinfo 100644,$(git rev-parse $P:$p),$p
done
S1=$(mk $C1 'sim S1')
fill() { sed -e "s/@@PR@@/0/; s/@@F@@/$F/; s/@@PREREG@@/7b9c608b1947e24b94007cadb19114abe3c50b2a/; s/@@FRUN@@/0/; s/@@C1@@/$C1/g; s/@@CONTROLS@@/8cafc140b519495d1687a5507846d320c3c3295f/g; s/@@S1@@/$S1/g" "$1"; }
fill $S/result.skeleton.md > $S/sim/result.md
grep -c '@@' $S/sim/result.md || true
git update-index --add --cacheinfo 100644,$(git hash-object -w $S/sim/result.md),$R/result.md
S2=$(mk $S1 'sim S2')
for n in 1 2; do
  git read-tree $S1
  fill $S/neg$n.md > $S/sim/neg$n.md
  git update-index --add --cacheinfo 100644,$(git hash-object -w $S/sim/neg$n.md),$R/result.md
  eval NEG$n=$(mk $S1 "sim S2 neg$n")
done
unset GIT_INDEX_FILE
echo "C1=$C1 S1=$S1 S2=$S2 NEG1=$NEG1 NEG2=$NEG2"
echo "C1 parents: $(git log -1 --format=%P $C1)  delta(F,C1): $(git diff --name-only $F $C1 | tr '\n' ' ')"
echo "S1 delta(C1,S1): $(git diff --name-only $C1 $S1 | wc -l) paths; tree(S1) less prereg == tree(P) less prereg: $( [ "$(git diff --name-only $P $S1)" = "$R/preregistration.md" ] && echo yes || echo NO)"
C=$S/controls.frozen.py
for spec in "S1:$S1" "S2:$S2" "P:$P" "NEG1:$NEG1" "NEG2:$NEG2"; do
  name=${spec%%:*}; sha=${spec#*:}
  python3 -I $C check $sha --freeze $F > $S/sim/check_$name.txt 2>&1 && rc=0 || rc=$?
  echo "check $name --freeze F: exit=$rc :: $(tail -1 $S/sim/check_$name.txt)"
  grep -E '^\s*FAIL' $S/sim/check_$name.txt | cut -c1-150 || true
done
python3 -I $C verdict $S2 > $S/sim/verdict_S2.txt 2>&1; grep VERDICT $S/sim/verdict_S2.txt
