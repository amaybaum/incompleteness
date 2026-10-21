#!/bin/sh
# Regenerates every output in this directory (exact arithmetic; deterministic). Run from anywhere.
# p41_local.py imports the reviewer engine from ../review/eng.py.
set -e
export PYTHONDONTWRITEBYTECODE=1
cd "$(dirname "$0")"
: > corr.out
for L in 2 3 4; do python3 corr.py "$L" >> corr.out; done
for s in corr2 corr3 lifts local local2 survivors nosb p41_local; do
  python3 "$s.py" > "$s.out"
done
