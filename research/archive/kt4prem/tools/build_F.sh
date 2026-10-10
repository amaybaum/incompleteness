#!/bin/sh
# Build candidate F for KT4-PREM-1: a single-parent child of D adding the preregistration alone, on the local
# branch claude/kt4-prem-1. Local only; pushing is a separate step.
set -e
S=/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/kt4prem
WT=$S/f-wt
D=bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58
RD=verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit
cd /home/user/incompleteness
[ -d $WT ] && git worktree remove --force $WT
git branch -D claude/kt4-prem-1 2>/dev/null || true
git worktree add -b claude/kt4-prem-1 $WT $D >/dev/null 2>&1
cd $WT
mkdir -p $RD
cp $S/round/preregistration.md $RD/preregistration.md
git add $RD/preregistration.md
git -c user.name=Claude -c user.email=noreply@anthropic.com commit -S -q -F - <<'MSG'
KT4-PREM-1: preregistration (candidate F)

Control plane of the native round KT4-PREM-1, a premise audit of the
Pauli-free four-copy theorem kt4_forward_ie1: countermodels hypothesis
by hypothesis, an independent exact replication, the pair-level
completion and action route, and the source map. Drafted from D
bcbc516f; delta(D, F) is this preregistration alone. Candidate F, not
designated.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1
MSG
F=$(git rev-parse HEAD)
echo "F $F  tree $(git rev-parse HEAD^{tree})"
echo "parents: $(git rev-list --parents -n1 $F | cut -d' ' -f2-)"
echo "delta(D, F):"; git diff --name-status $D $F
echo "prereg blob $(git rev-parse $F:$RD/preregistration.md)  scratch $(git hash-object $S/round/preregistration.md)"
echo "$F" > $S/round/F_sha
