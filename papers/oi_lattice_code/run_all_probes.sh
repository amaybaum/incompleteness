#!/usr/bin/env bash
# run_all_probes.sh — the foundation certification battery, one command.
# Exit 0 iff all eleven suites pass. (b63; named in the seventh-review triage.)
set -u
cd "$(dirname "$0")/foundations" || exit 2
FAIL=0
for p in c1_cp_scope_probes c2_mixing_probes c3_dilation_probes \
         chirality_grading_probes process_dilation_probes review3_probes \
         c4_backflow_probes review4_probes hspin_labels_probes hchi_selectivity_probes intervention_probes hspin_kernel_probes; do
  if python3 "$p.py" >/dev/null 2>&1; then echo "PASS  $p"
  else echo "FAIL  $p"; FAIL=1; fi
done
[ $FAIL -eq 0 ] && echo "all twelve suites green" || echo "BATTERY FAILED"
exit $FAIL
