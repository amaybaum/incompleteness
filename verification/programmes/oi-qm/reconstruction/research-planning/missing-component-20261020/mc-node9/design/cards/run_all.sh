#!/bin/sh
# Regenerates every output in this directory; run twice and compare for deterministic replay.
set -e
D=$(dirname "$0"); cd "$D"
python3 exactlp.py > exactlp.out
python3 -I extract_check.py > extract_check.out
node node_check.mjs "${CARD_TABLE:?set CARD_TABLE to a checkout of amaybaum/card-table at 17115cc}/src/engine.js" > node_check.out
for v in BASE NDP VIS VISNOSWAP MARK CSWAP SPECT; do python3 run_m1.py $v > run_m1.$v.out; done
python3 run_extra.py > run_extra.out
python3 run_sepdeck_large.py > run_sepdeck_large.out
python3 run_sepdeck_large2.py > run_sepdeck_large2.out
python3 run_budget_strict.py NDP VIS SPECT MARK BASE > run_budget_strict.out
python3 run_pur.py > run_pur.out
python3 witnesses.py > witnesses.out
python3 controls.py > controls.out
