#!/bin/sh
# Regenerates every output in this directory (exact arithmetic; deterministic). Run from anywhere.
# corr_main.py writes fd_full.pkl and alph.py writes alph.pkl; later scripts read them. Both are
# intermediate files and are removed at the end. corr_main.py's last line is a wall-clock time,
# which is dropped from corr_main.out so that the output is byte-reproducible.
set -e
export PYTHONDONTWRITEBYTECODE=1
cd "$(dirname "$0")"
python3 classify_n1.py > classify_n1.out
python3 lift_check.py > lift_check.out
python3 corr_main.py > corr_main.raw
grep -v '^time ' corr_main.raw > corr_main.out
for s in exact_e direct_ctrl alph ident subfam extra; do
  python3 "$s.py" > "$s.out"
done
# Pre-freeze review of the H-LOC draft (REVIEW-HLOC-1860b961): lift algebra and n = 2 checks only;
# none computes an n = 3 word, an n = 3 distribution or a re-costed metric.
for s in lifts_b1 restrict kg1_local nearmiss; do
  python3 "$s.py" > "$s.out"
done
rm -f corr_main.raw fd_full.pkl alph.pkl
