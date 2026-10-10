"""Layer-G checks of ADDENDUM-LAYERS.md (G2 forgetful sum, G3 normalization + trailing-idle consistency), exact.

usage: layers.py LEVEL [procs]   -> layers_L{LEVEL}.json and a per-rule summary
"""
import sys
import json
import hashlib
from fractions import Fraction as Fr
from multiprocessing import Pool
from record_fast import run_all
from record_analysis2 import INTERFACES, RULES, protocols


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
    J = run_all(sorted(need), rule, kappa)
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
    level = int(sys.argv[1])
    procs = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    palph, ealph = ('oi', 'oim') if level == 1 else ('oifs', 'oimfs')
    jobs = [(r, k, palph, ealph, 3) for r in RULES for k in INTERFACES]
    with Pool(procs) as pool:
        res = pool.map(check, jobs, chunksize=1)
    blob = json.dumps(res, sort_keys=True, indent=0)
    open(f'layers_L{level}.json', 'w').write(blob)
    print(f'LAYERS L{level}: {len(res)} runs; sha256 {hashlib.sha256(blob.encode()).hexdigest()}')
    for rule in RULES:
        rr = [r for r in res if r['rule'] == rule]
        print(f'G L{level} {rule}: G2 {sum(r["G2"] for r in rr)}/{len(rr)}, G3norm {sum(r["G3norm"] for r in rr)}/{len(rr)}, '
              f'G3idle {sum(r["G3idle"] for r in rr)}/{len(rr)}')
