"""Diagnostic (not a verdict): C dims for the welldef-INCONCLUSIVE Level-2 nonlinear interfaces, computed without
the welldef gate. Restricted-row rank is a lower bound on the true dimension of each C_k."""
import json, sys
from multiprocessing import Pool
import record_analysis2 as ra
from rankbasis import reduce_basis
from itertools import product
from fractions import Fraction as Fr

orig_nullspace = ra.nullspace
def run(kappa):
    ra.nullspace = lambda rows: []          # skip the welldef gate only; nothing else changes
    out = ra.analyze(('nonlinear', kappa, 3, 3, 'oifs', 'oimfs', 'imfs'))
    return out
R = json.load(open('fast_stageA_L2.json'))
ks = [tuple(map(tuple, r['kappa'])) for r in R if r['verdict'].startswith('INCON')]
with Pool(2) as p:
    for o in p.map(run, ks):
        print(o['kappa'], o['rank'], o['invasive'], o['dimC'], o['verdict'])
