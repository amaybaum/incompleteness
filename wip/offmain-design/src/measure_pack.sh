#!/bin/sh
# Simulate the PR commit (main + layout) in a scratch repository and measure what it adds to a pack. Never pushed.
O=$1; MAIN=66a981d5a9cab35b9ebd253aa0e610c0afbfefb6
cd $O/work && rm -rf pr-sim.git pr-sim.index && git init -q --bare pr-sim.git && echo $O/work/main.git/objects > pr-sim.git/objects/info/alternates
export GIT_DIR=$O/work/pr-sim.git GIT_WORK_TREE=$O/layout GIT_INDEX_FILE=$O/work/pr-sim.index
git read-tree $MAIN && git add -A verification/audits/evidence-retention && T=$(git write-tree)
C=$(GIT_AUTHOR_NAME=proto GIT_AUTHOR_EMAIL=proto@example.invalid GIT_COMMITTER_NAME=proto GIT_COMMITTER_EMAIL=proto@example.invalid \
    GIT_AUTHOR_DATE='2026-10-17T00:00:00Z' GIT_COMMITTER_DATE='2026-10-17T00:00:00Z' git commit-tree $T -p $MAIN -m 'prototype layout (never pushed)')
git update-ref refs/heads/proto $C
echo "commit $C"
echo "new objects $(git rev-list --objects proto --not $MAIN | wc -l)"
git rev-list --objects proto --not $MAIN | git pack-objects --stdout -q > $O/work/sim-default.pack
git rev-list --objects proto --not $MAIN | git pack-objects --window=250 --depth=50 --stdout -q > $O/work/sim-aggr.pack
echo "pack default $(wc -c < $O/work/sim-default.pack)  aggressive $(wc -c < $O/work/sim-aggr.pack)"
