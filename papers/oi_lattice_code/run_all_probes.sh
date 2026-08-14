#!/usr/bin/env bash
# run_all_probes.sh — the foundation certification battery, one command.
# Exit 0 iff all twenty-three suites and the citation guard pass. (b63; named in the seventh-review triage.)
set -u
cd "$(dirname "$0")/foundations" || exit 2
FAIL=0
for p in c1_cp_scope_probes c2_mixing_probes c3_dilation_probes \
         chirality_grading_probes process_dilation_probes review3_probes \
         c4_backflow_probes review4_probes hspin_labels_probes hchi_selectivity_probes intervention_probes hspin_kernel_probes hspin4d_probes hchiprime_probes translation_probes condensate_space_probes phaselock_probes lg_comb_probes tdilate_probes repconsistency_probes fastbath_probes primitive_probes tuple_probes; do
  if python3 "$p.py" >/dev/null 2>&1; then echo "PASS  $p"
  else echo "FAIL  $p"; FAIL=1; fi
done
if python3 ../citation_check.py >/dev/null 2>&1; then echo "PASS  citation_check"
else echo "FAIL  citation_check"; FAIL=1; fi
[ $FAIL -eq 0 ] && echo "all twenty-three suites green (+ citation guard)" || echo "BATTERY FAILED"
exit $FAIL
