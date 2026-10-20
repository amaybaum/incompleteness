#!/bin/sh
# controls.sh -- live and omission controls for the tranche-2 pilot, each in its own isolated disposable clone.
# Usage: sh controls.sh <empty-work-dir> <source-repo> <oid>
# Clones are made with --no-local --no-hardlinks (no --shared, no alternates, no linked worktree); the full history
# of main is fetched from the public repository because the source checkout may be shallow.
set -u
W=$1; SRC=$2; OID=$3
HERE=$(cd "$(dirname "$0")" && pwd)
MAIN=92de3143046b26d7fa2ce3b13ce3ea4b1e18a37a
A=verification/audits/evidence-retention
mkdir -p "$W/out"
git clone -q --no-hardlinks --no-local --single-branch --branch main "$SRC" "$W/base" || exit 2
git -C "$W/base" fetch -q --unshallow https://github.com/amaybaum/incompleteness.git refs/heads/main || exit 2
test "$(git -C "$W/base" rev-parse HEAD)" = "$MAIN" || { echo "base HEAD is not $MAIN"; exit 2; }
test "$(git -C "$W/base" rev-parse --is-shallow-repository)" = false || exit 2
for v in LIVE N1 N2 N3; do
  d="$W/$v"
  git clone -q --no-hardlinks --no-local "$W/base" "$d" || exit 2
  git -C "$d" checkout -q --detach "$MAIN" || exit 2
  test ! -e "$d/.git/objects/info/alternates" || { echo "alternates in $d"; exit 2; }
  if [ "$v" != LIVE ]; then python3 -I -B "$HERE/omit.py" "$d" "$OID" "$v" > "$W/out/$v.edit.txt" || exit 2; fi
  git -C "$d" status --short > "$W/out/$v.status.txt"
  git -C "$d" diff --stat -- '*.py' > "$W/out/$v.pydiff.txt"
  ( cd "$d" &&
    python3 -I -B $A/check_objects.py > "$W/out/$v.objects-tree.txt" 2>&1; echo "objects-tree $?" ;
    python3 -I -B $A/check_objects.py --reconstitute > "$W/out/$v.objects-history.txt" 2>&1; echo "objects-history $?" ;
    python3 -I -B $A/check_retention.py > "$W/out/$v.retention.txt" 2>&1; echo "retention $?" ) > "$W/out/$v.exit.txt"
  echo "== $v"; cat "$W/out/$v.exit.txt"
  grep -h '^FAIL\|FAILED\|HOLDS\|check_objects: OK' "$W/out/$v.objects-tree.txt" "$W/out/$v.objects-history.txt" "$W/out/$v.retention.txt" | sort | uniq -c
done
