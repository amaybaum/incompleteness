"""PREREG-3A section 6 item 6: G identities on the Stage-A tables (G2 forgetful sum, G3 normalization, G3 trailing-
idle consistency), exact, for all 143 kappa (layers.py of RECORD with the Level-3A alphabets). With --cc, the
exchanged-branch countercontrol census: m implemented with the branch maps exchanged (not the forgetful sum).

usage: layers3.py [procs] [--cc]   -> layers3_linear.json or cc3_census.json and a summary line
"""
import sys
import os
import json
import hashlib
from fractions import Fraction as Fr
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'record'))
import record3_fast                                   # noqa: E402
from record3_fast import run_all3, step3              # noqa: E402
from analysis3 import INTERFACES, protocols           # noqa: E402

CC = '--cc' in sys.argv


def step_cc(st, s, rule, kappa, la):
    if s == 'm':
        return step3(st, 'm', rule, (kappa[1], kappa[0]), la)
    return step3(st, s, rule, kappa, la)


def check(job):
    rule, kappa, palph, ealph, L = job
    pps, pes = protocols(palph, L), protocols(ealph, L)
    need = set()
    for a in pps:
        for b in pes:
            need.add(a + b)
            need.add(a + b + 'i')
            if 'm' in b:
                k = b.index('m')
                need.add(a + b[:k] + 'o' + b[k + 1:])
    J = run_all3(sorted(need), rule, kappa, step=step_cc if CC else None)
    g2 = g3n = g3i = True
    for a in pps:
        for b in pes:
            p = a + b
            c, t = J[p]
            g3n &= sum(c) == t
            ci, ti = J[p + 'i']
            g3i &= all(Fr(x, t) == Fr(y, ti) for x, y in zip(c, ci))
            if 'm' in b:
                k = b.index('m')
                q = a + b[:k] + 'o' + b[k + 1:]
                cq, tq = J[q]
                j = (a + b[:k]).count('o')          # position of the inserted bit, most significant first
                n = p.count('o')                    # record length of p
                for r in range(1 << n):
                    hi, lo = r >> (n - j), r & ((1 << (n - j)) - 1)
                    s = sum(cq[(((hi << 1) | bb) << (n - j)) | lo] for bb in (0, 1))
                    g2 &= Fr(c[r], t) == Fr(s, tq)
    return {'rule': rule, 'kappa': [list(kappa[0]), list(kappa[1])], 'G2': g2, 'G3norm': g3n, 'G3idle': g3i}


if __name__ == '__main__':
    procs = int([a for a in sys.argv[1:] if not a.startswith('--')][0]) if len([a for a in sys.argv[1:] if not a.startswith('--')]) else 2
    jobs = [('linear', k, 'oifsc', 'oimfsc', 3) for k in INTERFACES]
    with Pool(procs) as pool:
        res = pool.map(check, jobs, chunksize=1)
    blob = json.dumps(res, sort_keys=True, indent=0)
    fn = os.path.join(HERE, 'cc3_census.json' if CC else 'layers3_linear.json')
    open(fn, 'w').write(blob)
    tag = 'CC3-CENSUS' if CC else 'LAYERS3'
    print(f'{tag}: {len(res)} runs; sha256 {hashlib.sha256(blob.encode()).hexdigest()}')
    print(f'{tag} linear: G2 {sum(r["G2"] for r in res)}/{len(res)}, G3norm {sum(r["G3norm"] for r in res)}/{len(res)}, '
          f'G3idle {sum(r["G3idle"] for r in res)}/{len(res)}')
    if CC:
        A = json.load(open(os.path.join(HERE, 'fast3_stageA_linear.json')))
        inv = {tuple(map(tuple, r['kappa'])): r.get('invasive') for r in A}
        import collections
        cnt = collections.Counter((inv[tuple(map(tuple, r['kappa']))], r['G2']) for r in res)
        print('CC3-CENSUS (invasive, G2 under mutation):', dict(cnt), '; bites on', sum(1 for r in res if not r['G2']), 'of', len(res))
