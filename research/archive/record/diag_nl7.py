"""Diagnostic (outside FREEZE's advance rule): the seven Level-1 nonlinear interfaces with certified dim C_2 = 4,
C_1 = 3, run at the Stage-B horizon L_p = L_e = 4 with the Stage-B criteria."""
import json
from multiprocessing import Pool
from record_analysis2 import analyze
R = json.load(open('fast_stageA_L1.json'))
ks = [tuple(map(tuple, r['kappa'])) for r in R if r['rule'] == 'nonlinear' and r['dimC'] == [2, 3, 4]]
assert len(ks) == 7
with Pool(1) as p:
    res = p.map(analyze, [('nonlinear', k, 4, 4, 'oi', 'oim', 'im') for k in ks])
for o in res:
    print(o['kappa'], 'rank', o['rank'], 'cert', o['certified'], 'welldef', o.get('welldef'), 'dimC', o.get('dimC'), o['verdict'], flush=True)
