"""Level 3A analysis per (rule, interface): exactly the criteria of PREREG-3A.md sections 4-5.

usage: analysis3.py STAGE [procs] [RULE]    STAGE in {A, B, C}; RULE defaults to linear (the only 3A rule).
  Stage A: all 143 kappa, L_p = L_e = 3.          Advance rule: invasive and certified dim C_2 <= 4.
  Stage B: advancing kappa, L_p = L_e = 4.         Verdict stage.
  Stage C: first three AT-RANK kappa and the first UNDER-RANK kappa in frozen order, L_p = 4, L_e = 5.
Alphabets: preparations 'oifsc', effects 'oimfsc', non-selective generators 'imfsc'.  Seed r = (o, outcome 1).
Rank, WELLDEF, invasiveness and the dims C_k are computed for every kappa at every stage (no early exit; a guard
failure gates only positive claims).  Exact over Q; rank certified by the rank-basis method of QUOTIENT.
"""
import sys
import os
import json
import hashlib
from fractions import Fraction as Fr
from itertools import product
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'record'))
sys.path.insert(0, os.path.join(HERE, '..', 'quotient'))
from record_sim import PASSIVE                                               # noqa: E402
from rankbasis import greedy_modp, certify, nullspace, reduce_basis          # noqa: E402
import record3_fast                                                           # noqa: E402

INJ = [(x, y) for x in range(4) for y in range(4) if x != y]
INTERFACES = [(k0, k1) for k0 in INJ for k1 in INJ if (k0, k1) != PASSIVE]    # frozen order (as RECORD)
assert len(INTERFACES) == 143
PALPH, EALPH, GENS = 'oifsc', 'oimfsc', 'imfsc'
HORIZON = {'A': (3, 3), 'B': (4, 4), 'C': (4, 5)}
RUN_ALL = record3_fast.run_all3          # replay scripts swap this for the reference simulator


def protocols(alph, L):
    return [''.join(p) for l in range(L + 1) for p in product(alph, repeat=l)]


def analyze(job):
    rule, kappa, Lp, Le, stage = job
    effs = [(pe, re) for pe in protocols(EALPH, Le) for re in range(1 << pe.count('o'))]
    pps, pes = protocols(PALPH, Lp), protocols(EALPH, Le)
    J = RUN_ALL([a + b for a in pps for b in pes], rule, kappa)
    # integer columns at the common denominator D = max total mass (all masses are powers of 4); a global column
    # scaling, which changes no relation among effect rows
    D = max(t for (_, t) in J.values())
    preps, icols = [], []
    for pp in pps:
        base, tot = J[pp]
        for r in range(1 << pp.count('o')):
            if base[r] == 0:
                continue
            col = []
            for (pe, re) in effs:
                c, t = J[pp + pe]
                col.append(c[(r << pe.count('o')) | re] * (D // t))
            preps.append((pp, r))
            icols.append(col)
    out = {'rule': rule, 'kappa': [list(kappa[0]), list(kappa[1])], 'stage': stage, 'Lp': Lp, 'Le': Le,
           'preps': len(preps), 'effects': len(effs)}
    kept = greedy_modp(icols)
    ok, why = certify(icols, kept)
    out['rank'] = len(kept)
    out['certified'] = ok
    if not ok:
        out['verdict'] = 'INCONCLUSIVE(rank)'
        return out
    idx = {e: i for i, e in enumerate(effs)}
    T = [[Fr(icols[k][i]) for k in kept] for i in range(len(effs))]
    dom = [e for e in effs if len(e[0]) <= Le - 1]
    nd = len(dom)
    rels = nullspace([T[idx[e]] for e in dom])
    well = all(all(sum((c[i] * T[idx[(g + dom[i][0], dom[i][1])]][j] for i in range(nd) if c[i] != 0), Fr(0)) == 0
                   for j in range(len(kept))) for g in GENS for c in rels)
    out['welldef'] = well
    out['invasive'] = any(T[idx[('m' + e[0], e[1])]] != T[idx[('i' + e[0], e[1])]] for e in dom)
    unit = T[idx[('', 0)]]
    dims = []
    for k in range(Le):
        rows = [unit] + [T[idx[(''.join(w) + 'o', 1)]] for l in range(k + 1) for w in product(GENS, repeat=l)]
        dims.append(len(reduce_basis(rows)))
    out['dimC'] = dims
    out['over_rank'] = out['rank'] > 4 or max(dims) > 4
    out['equal_last'] = dims[-1] == dims[-2]
    if not out['invasive']:
        out['verdict'] = f'NOT-INVASIVE(rank {out["rank"]})'
    elif stage == 'A':
        out['verdict'] = f'OVER-RANK(dims {dims})' if max(dims) > 4 else f'ADVANCE(dims {dims})'
    elif out['over_rank']:
        out['verdict'] = f'OVER-RANK(rank {out["rank"]}, dims {dims})'
    elif stage == 'C':
        out['verdict'] = f'C-CONSISTENT(dims {dims})'
    elif dims[-1] == 4 and out['equal_last']:
        out['verdict'] = 'AT-RANK' if well else 'INCONCLUSIVE(welldef; dimension 4 observed)'
    elif dims[-1] == 4:
        out['verdict'] = 'AT-RANK(unequal)'
    else:
        out['verdict'] = f'UNDER-RANK(dims {dims})'
    return out


def kappa_key(r):
    return tuple(map(tuple, r['kappa']))


def jobs_for(stage, rule):
    Lp, Le = HORIZON[stage]
    if stage == 'A':
        ks = INTERFACES
    elif stage == 'B':
        prev = json.load(open(os.path.join(HERE, f'fast3_stageA_{rule}.json')))
        adv = {kappa_key(r) for r in prev if r.get('invasive') and r.get('dimC') and r['dimC'][-1] <= 4}
        ks = [k for k in INTERFACES if k in adv]
        print(f'STAGE B: {len(ks)} advancing kappa', flush=True)
    else:
        prev = json.load(open(os.path.join(HERE, f'fast3_stageB_{rule}.json')))
        by = {kappa_key(r): r for r in prev}
        at = [k for k in INTERFACES if k in by and by[k]['verdict'] == 'AT-RANK'][:3]
        under = [k for k in INTERFACES if k in by and by[k]['verdict'].startswith('UNDER-RANK')][:1]
        ks = at + under
        print(f'STAGE C: {len(ks)} kappa {ks}', flush=True)
    return [(rule, k, Lp, Le, stage) for k in ks]


if __name__ == '__main__':
    stage = sys.argv[1]
    procs = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    rule = sys.argv[3] if len(sys.argv) > 3 else 'linear'
    jobs = jobs_for(stage, rule)
    with Pool(procs) as pool:
        res = pool.map(analyze, jobs, chunksize=1)
    blob = json.dumps(res, sort_keys=True, indent=0)
    fn = os.path.join(HERE, f'fast3_stage{stage}_{rule}.json')
    open(fn, 'w').write(blob)
    print(f'STAGE {stage} {rule}: {len(res)} runs; sha256 {hashlib.sha256(blob.encode()).hexdigest()}')
    tally = {}
    for r in res:
        tally[r['verdict']] = tally.get(r['verdict'], 0) + 1
    for k, v in sorted(tally.items()):
        print(f'TALLY {stage} {rule}: {k}: {v}')
