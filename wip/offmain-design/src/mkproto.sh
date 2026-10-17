#!/bin/sh
# Build a local prototype checkout: main + the layout, committed in a scratch repository with no remote. Never pushed.
set -e
O=$1; MAIN=66a981d5a9cab35b9ebd253aa0e610c0afbfefb6; W=$O/work/proto-wt
rm -rf $W && git init -q $W && echo $O/work/main.git/objects > $W/.git/objects/info/alternates
cd $W && git checkout -q --detach $MAIN 2>/dev/null || { git update-ref refs/heads/base $MAIN; git checkout -q --detach $MAIN; }
cp -r $O/layout/verification/audits/evidence-retention/. verification/audits/evidence-retention/
git add verification/audits/evidence-retention/objects verification/audits/evidence-retention/check_objects.py
GIT_AUTHOR_NAME=proto GIT_AUTHOR_EMAIL=proto@example.invalid GIT_COMMITTER_NAME=proto GIT_COMMITTER_EMAIL=proto@example.invalid \
GIT_AUTHOR_DATE='2026-10-17T00:00:00Z' GIT_COMMITTER_DATE='2026-10-17T00:00:00Z' git commit -q -m 'prototype: retained off-main objects (local only, never pushed)'
git rev-parse HEAD
