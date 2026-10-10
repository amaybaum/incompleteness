"""Sampled Level-2 replay: recompute selected Stage-A Level-2 jobs with the ORIGINAL simulator (record_analysis.py,
record_sim) and compare each result record field-by-field with fast_stageA_L2.json."""
import json
from record_analysis import analyze
R = json.load(open('fast_stageA_L2.json'))
key = lambda r: (r['rule'], tuple(map(tuple, r['kappa'])))
by = {key(r): r for r in R}
pick = []
for rule in ('linear', 'nonlinear', 'majority'):
    rr = sorted([r for r in R if r['rule'] == rule], key=lambda r: (r['rank'], r['kappa']))
    pick += [key(rr[0]), key(rr[-1])]
pick.append(('linear', next(key(r)[1] for r in R if r['rule'] == 'linear' and r['verdict'] == 'FAIL(dimC=3)')))
pick.append(('nonlinear', next(key(r)[1] for r in R if r['rule'] == 'nonlinear' and r['verdict'].startswith('INCON'))))
pick.append(('majority', next(key(r)[1] for r in R if r['rule'] == 'majority' and r['dimC'][-1] == 14)))
pick = list(dict.fromkeys(pick))
bad = 0
for rule, k in pick:
    o = analyze((rule, k, 3, 3, 'oifs', 'oimfs', 'imfs'))
    o['kappa'] = [list(k[0]), list(k[1])]
    same = json.dumps(o, sort_keys=True) == json.dumps(by[(rule, k)], sort_keys=True)
    bad += not same
    print('REPLAY-L2', rule, k, o['verdict'], 'rank', o['rank'], 'MATCH' if same else 'MISMATCH', flush=True)
print(f'REPLAY-L2 {len(pick)} jobs, mismatches {bad}', 'OK' if bad == 0 else 'FAILED')
