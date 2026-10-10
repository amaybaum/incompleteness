"""PREREG-3A section 6 items 4-5: field-by-field replay of selected jobs on the REFERENCE simulator (record3_sim.run3
driven through analysis3.analyze with RUN_ALL swapped), compared with the fast-evaluator artifact.

usage: replay3.py A   -> the nine fixed positions 0,18,...,142 of the frozen order, plus the first kappa in frozen
                        order of each verdict class not already covered (rule fixed before the output; outcome-blind)
       replay3.py B   -> kappa ((0,1),(0,1)) if it advanced, else the first advancing kappa in frozen order
"""
import sys
import os
import json
HERE = os.path.dirname(os.path.abspath(__file__))
import analysis3                                       # noqa: E402
from analysis3 import INTERFACES, HORIZON, kappa_key   # noqa: E402
from record3_sim import run3                           # noqa: E402

analysis3.RUN_ALL = lambda ps, rule, kappa: {p: run3(p, rule, kappa) for p in set(ps)}
stage = sys.argv[1]
R = json.load(open(os.path.join(HERE, f'fast3_stage{stage}_linear.json')))
by = {kappa_key(r): r for r in R}
if stage == 'A':
    pick = [INTERFACES[i] for i in (0, 18, 36, 54, 72, 90, 108, 126, 142)]
    seen = {by[k]['verdict'] for k in pick}
    for k in INTERFACES:
        if by[k]['verdict'] not in seen:
            pick.append(k)
            seen.add(by[k]['verdict'])
else:
    order = [k for k in INTERFACES if k in by]
    pick = [((0, 1), (0, 1))] if ((0, 1), (0, 1)) in by else order[:1]
Lp, Le = HORIZON[stage]
bad = 0
for k in pick:
    o = analysis3.analyze(('linear', k, Lp, Le, stage))
    same = json.dumps(o, sort_keys=True) == json.dumps(by[k], sort_keys=True)
    bad += not same
    print(f'REPLAY3-{stage}', k, o['verdict'], 'rank', o['rank'], 'MATCH' if same else 'MISMATCH', flush=True)
print(f'REPLAY3-{stage} {len(pick)} jobs, mismatches {bad}', 'OK' if bad == 0 else 'FAILED')
