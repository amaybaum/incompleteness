"""Countercontrol census (post-run, outcome-blind, complete): at Level 2, for every one of the 143 linear interfaces,
re-run the G2 check with the non-selective letter m implemented with the branch maps exchanged (not the forgetful
sum). The single fixed countercontrol kappa ((1,3),(0,2)) is operationally non-invasive for linear at Level 2, so
there it is vacuous; this census reports for how many linear kappa the countercontrol bites."""
import json, collections
from multiprocessing import Pool
import record_fast, layers
from record_analysis2 import INTERFACES
orig = record_fast.step
def bad(st, s, rule, kappa, la):
    if s == 'm':
        return orig(st, 'm', rule, (kappa[1], kappa[0]), la)
    return orig(st, s, rule, kappa, la)
def job(k):
    record_fast.step = bad
    return layers.check(('linear', k, 'oifs', 'oimfs', 3))
if __name__ == '__main__':
    with Pool(3) as p:
        res = p.map(job, INTERFACES, chunksize=1)
    inv = {tuple(map(tuple, r['kappa'])): r.get('invasive') for r in json.load(open('fast_stageA_L2.json')) if r['rule'] == 'linear'}
    c = collections.Counter((inv[tuple(map(tuple, r['kappa']))], r['G2']) for r in res)
    print('CC-CENSUS L2 linear (invasive, G2 under mutation):', dict(c))
    print('CC-CENSUS bites on', sum(1 for r in res if not r['G2']), 'of', len(res))
