#!/bin/sh
# Regenerates every output in this directory (exact arithmetic; deterministic).
set -e
cd "$(dirname "$0")"
for s in controls a_classify b_lifts d_witness alt oi_real oi_z4family predictions; do
  python3 "$s.py" > "$s.out"
done
