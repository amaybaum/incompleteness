"""Diagnostic, continued: the depth-4 well-definedness guard fails for all seven, so C dims are computed with the
guard skipped. Restricted-row rank of each C_k is a lower bound on its true dimension, independent of that guard."""
import json
from multiprocessing import Pool
import record_analysis2 as ra

def run(k):
    ra.nullspace = lambda rows: []
    return ra.analyze(('nonlinear', k, 4, 4, 'oi', 'oim', 'im'))
R = json.load(open('fast_stageA_L1.json'))
ks = [tuple(map(tuple, r['kappa'])) for r in R if r['rule'] == 'nonlinear' and r['dimC'] == [2, 3, 4]]
with Pool(1) as p:
    for o in p.map(run, ks):
        print(o['kappa'], 'rank', o['rank'], 'dimC', o['dimC'], flush=True)
