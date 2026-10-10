"""Gate 4 (fixed before any Stage-B output): replay the Stage-B Level-2 job kappa = ((0,1),(0,1)), L_p = L_e = 4,
with the ORIGINAL simulator (record_analysis.py / record_sim) and compare field-by-field with fast_stageB_L2.json."""
import json
from record_analysis import analyze
k = ((0, 1), (0, 1))
R = json.load(open('fast_stageB_L2.json'))
ref = next(r for r in R if r['rule'] == 'linear' and r['kappa'] == [[0, 1], [0, 1]])
o = analyze(('linear', k, 4, 4, 'oifs', 'oimfs', 'imfs'))
o['kappa'] = [list(k[0]), list(k[1])]
same = json.dumps(o, sort_keys=True) == json.dumps(ref, sort_keys=True)
print('GATE4', o, 'MATCH' if same else 'MISMATCH', flush=True)
print('GATE4', 'OK' if same else 'FAILED')
