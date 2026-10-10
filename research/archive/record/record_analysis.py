"""RECORD analysis per (rule, interface): exactly the criteria frozen in FREEZE.md.

usage: record_analysis.py STAGE LEVEL [procs]      STAGE in {A, B}; LEVEL in {1, 2}
  Stage A runs all 143 admissible interfaces x 3 rules; Stage B reads the advancing set from Stage A's output.
"""
import sys
import json
import hashlib
from fractions import Fraction as Fr
from itertools import product
from multiprocessing import Pool

sys.path.insert(0, '../quotient')
sys.path.insert(0, '../rank')
from record_sim import run, PASSIVE                                     # noqa: E402
from rankbasis import greedy_modp, certify, nullspace, reduce_basis, in_span   # noqa: E402

RULES = ('linear', 'nonlinear', 'majority')
INJ = [(x, y) for x in range(4) for y in range(4) if x != y]
INTERFACES = [(k0, k1) for k0 in INJ for k1 in INJ if (k0, k1) != PASSIVE]
assert len(INTERFACES) == 143


def protocols(alph, L):
    return [''.join(p) for l in range(L + 1) for p in product(alph, repeat=l)]


def analyze(job):
    rule, kappa, Lp, Le, palph, ealph, gens = job
    cache = {}

    def J(s):
        if s not in cache:
            cache[s] = run(s, rule, kappa)
        return cache[s]
    effs = [(pe, re) for pe in protocols(ealph, Le) for re in range(1 << pe.count('o'))]
    preps, cols, scales = [], [], []
    for pp in protocols(palph, Lp):
        base, tot = J(pp)
        k1 = pp.count('o')
        for r in range(1 << k1):
            if base[r] == 0:
                continue
            col = []
            for (pe, re) in effs:
                c, t = J(pp + pe)
                col.append(Fr(c[(r << pe.count('o')) | re], t))
            preps.append((pp, r))
            cols.append(col)
    # integer columns at a common denominator (column scaling changes no relation among effect rows)
    D = 1
    for col in cols:
        for x in col:
            D = max(D, x.denominator)
    icols = [[int(x * D) for x in col] for col in cols]
    out = {'rule': rule, 'kappa': kappa, 'preps': len(preps), 'effects': len(effs)}
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
    drow = [T[idx[e]] for e in dom]
    rels = nullspace(drow)
    well = all(all(sum((c[i] * T[idx[(g + dom[i][0], dom[i][1])]][j] for i in range(nd) if c[i] != 0), Fr(0)) == 0
                   for j in range(len(kept))) for g in gens for c in rels)
    out['welldef'] = well
    if not well:
        out['verdict'] = 'INCONCLUSIVE(welldef)'
        return out
    out['invasive'] = any(T[idx[('m' + e[0], e[1])]] != T[idx[('i' + e[0], e[1])]] for e in dom)
    unit = T[idx[('', 0)]]
    dims, Cspan = [], []
    for k in range(Le):
        rows = [unit] + [T[idx[(''.join(w) + 'o', 1)]] for l in range(k + 1) for w in product(gens, repeat=l)]
        B = reduce_basis(rows)
        dims.append(len(B))
        Cspan.append(B)
    out['dimC'] = dims
    stab = len(dims) >= 2 and dims[-1] == dims[-2]
    out['stabilized'] = stab
    if not out['invasive']:
        out['verdict'] = 'NOT-INVASIVE'
    elif stab and dims[-1] == 4:
        out['verdict'] = 'C4'
    elif stab:
        out['verdict'] = f'FAIL(dimC={dims[-1]})'
    else:
        out['verdict'] = f'FAIL(no stabilization; dims {dims})'
    return out


def jobs_for(stage, level, advancing=None):
    if level == 1:
        palph, ealph, gens = 'oi', 'oim', 'im'
    else:
        palph, ealph, gens = 'oifs', 'oimfs', 'imfs'
    Lp, Le = (3, 3) if stage == 'A' else (4, 4)
    out = []
    for rule in RULES:
        for kappa in INTERFACES:
            if advancing is not None and [rule, [list(kappa[0]), list(kappa[1])]] not in advancing:
                continue
            out.append((rule, kappa, Lp, Le, palph, ealph, gens))
    return out


if __name__ == '__main__':
    stage, level = sys.argv[1], int(sys.argv[2])
    procs = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    adv = None
    if stage == 'B':
        prev = json.load(open(f'stageA_L{level}.json'))
        adv = [[r['rule'], [list(r['kappa'][0]), list(r['kappa'][1])]] for r in prev
               if r.get('stabilized') and r.get('invasive') and r['dimC'][-1] <= 4]
        print(f'STAGE B L{level}: {len(adv)} advancing (rule, interface) pairs', flush=True)
    jobs = jobs_for(stage, level, adv)
    with Pool(procs) as pool:
        res = pool.map(analyze, jobs, chunksize=1)
    res = [{**r, 'kappa': [list(r['kappa'][0]), list(r['kappa'][1])]} for r in res]
    blob = json.dumps(res, sort_keys=True, indent=0)
    open(f'stage{stage}_L{level}.json', 'w').write(blob)
    print(f'STAGE {stage} L{level}: {len(res)} runs; sha256 {hashlib.sha256(blob.encode()).hexdigest()}')
    for rule in RULES:
        rr = [r for r in res if r['rule'] == rule]
        tally = {}
        for r in rr:
            tally[r['verdict']] = tally.get(r['verdict'], 0) + 1
        print(f'TALLY {stage} L{level} {rule}: ' + ', '.join(f'{k}: {v}' for k, v in sorted(tally.items())))
