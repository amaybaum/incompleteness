"""Rank-basis replacement for the exhaustive invsub runs (effects <= Le-1 under W, F, S; preparations <= Lp).

Same effect family (protocols over 'oifs' of length <= Le, singleton records), same preparations (protocols over
'oifs' of length <= Lp with positive-probability records), same generators W = 'i', F = 'f', S = 's'.

  build   : exhaustive integer table J[e][x] = joint count of (prep x, effect e) at the common scale 2^22, for every
            effect and every positive-weight preparation; saved with its sha256.
  analyze : (1) greedy selection of preparation columns in the fixed enumeration order, keeping a column iff it
            raises the rank over F_p;
            (2) CERTIFY over Q: the selected columns are independent, and every other column lies in their span
                (exact integer arithmetic) => rank_Q(full) = rank_Q(reduced) = |S|;
            (3) WELLDEF: every relation among the domain effects (length <= Le-1) detected on the reduced columns is
                preserved by each generator's dual map, on the reduced columns;
            (4) the largest common invariant subspace of span(domain effects) under the generators, exactly over Q,
                on the reduced columns; unit membership; structure (basis, induced W characteristic polynomial).
  replay  : recompute the selected columns from scratch (independent of the saved table) and compare; rerun
            analyze from the saved table; outputs must be byte-identical.
Column scaling by 1/weight is omitted throughout: it changes no linear relation among effect rows.
"""
import sys
import os
import pickle
import hashlib
import math
from fractions import Fraction as Fr
from itertools import product
from multiprocessing import Pool
import numpy as np

sys.path.insert(0, '.')
sys.path.insert(0, '../rank')
from quotient import run_mid          # noqa: E402

SCALE_BITS = 22
PR = 2147483647


def effects(Le, alph='oifs'):
    out = []
    for l in range(Le + 1):
        for pp in product(alph, repeat=l):
            pr = ''.join(pp)
            for r in range(1 << pr.count('o')):
                out.append((pr, r))
    return out


def counts(s, rule, cache):
    if s not in cache:
        cnt, den = run_mid(s, rule)
        mult = 1 << (SCALE_BITS - (den.bit_length() - 1))
        cache[s] = [int(c) * mult for c in cnt]
    return cache[s]


def prep_columns(args):
    """All preparations (pp, r) with positive weight, and their full columns over the effect family."""
    pp, rule, Le = args
    effs = effects(Le)
    cache = {}
    k1 = pp.count('o')
    base = counts(pp, rule, cache)
    out = []
    for r in range(1 << k1):
        if base[r] == 0:
            continue
        col = []
        for (pe, re_) in effs:
            j = counts(pp + pe, rule, cache)
            col.append(j[(r << pe.count('o')) | re_])
        out.append(((pp, r), col))
    return out


def build(rule, Le, Lp, procs):
    prots = [''.join(p) for l in range(Lp + 1) for p in product('oifs', repeat=l)]
    with Pool(procs) as pool:
        parts = pool.map(prep_columns, [(pp, rule, Le) for pp in prots], chunksize=1)
    preps, cols = [], []
    for part in parts:
        for (x, col) in part:
            preps.append(x)
            cols.append(col)
    return preps, cols


def greedy_modp(cols, p=PR):
    """Columns kept in order iff they raise the rank over F_p (row-echelon basis of kept columns)."""
    basis = []   # list of (pivot index, normalized vector mod p)
    kept = []
    for k, c in enumerate(cols):
        v = np.array([x % p for x in c], dtype=np.int64)
        for (piv, b) in basis:
            if v[piv]:
                v = (v - v[piv] * b) % p
        nz = np.nonzero(v)[0]
        if len(nz):
            piv = int(nz[0])
            inv = pow(int(v[piv]), p - 2, p)
            basis.append((piv, (v * inv) % p))
            kept.append(k)
    return kept


def certify(cols, kept):
    """Exact: kept columns independent over Q, and every column in their span over Q."""
    m = len(cols[0])
    A = [[Fr(cols[k][i]) for k in kept] for i in range(m)]   # m x r
    r = len(kept)
    # row-reduce A to find r pivot rows with A[P, :] invertible
    M = [row[:] for row in A]
    piv_rows, piv_cols = [], []
    used = [False] * m
    for c in range(r):
        i = next((i for i in range(m) if not used[i] and M[i][c] != 0), None)
        if i is None:
            return False, 'kept columns dependent over Q'
        used[i] = True
        piv_rows.append(i)
        piv_cols.append(c)
        for i2 in range(m):
            if i2 != i and M[i2][c] != 0:
                f = M[i2][c] / M[i][c]
                M[i2] = [a - f * b for a, b in zip(M[i2], M[i])]
    # invert B = A[P, :] exactly
    B = [[A[i][c] for c in range(r)] for i in piv_rows]
    aug = [B[i] + [Fr(int(i == j)) for j in range(r)] for i in range(r)]
    for c in range(r):
        k = next(i for i in range(c, r) if aug[i][c] != 0)
        aug[c], aug[k] = aug[k], aug[c]
        f = aug[c][c]
        aug[c] = [x / f for x in aug[c]]
        for i in range(r):
            if i != c and aug[i][c] != 0:
                g = aug[i][c]
                aug[i] = [x - g * y for x, y in zip(aug[i], aug[c])]
    Binv = [row[r:] for row in aug]
    keptset = set(kept)
    Kcols = [cols[k] for k in kept]
    for idx, col in enumerate(cols):
        if idx in keptset:
            continue
        rhs = [Fr(col[i]) for i in piv_rows]
        coef = [sum((Binv[a][b] * rhs[b] for b in range(r)), Fr(0)) for a in range(r)]
        D = 1
        for c in coef:
            D = D * c.denominator // math.gcd(D, c.denominator)
        ic = [int(c * D) for c in coef]
        for i in range(m):
            if sum(ic[a] * Kcols[a][i] for a in range(r)) != D * col[i]:
                return False, f'column {idx} not in the span of the kept columns'
    return True, 'ok'


def reduce_basis(rows):
    B = []
    for r in rows:
        v = list(r)
        for (piv, b) in B:
            if v[piv] != 0:
                f = v[piv] / b[piv]
                v = [x - f * y for x, y in zip(v, b)]
        p = next((i for i, x in enumerate(v) if x != 0), None)
        if p is not None:
            B.append((p, v))
    return B


def in_span(v, B):
    v = list(v)
    for (piv, b) in B:
        if v[piv] != 0:
            f = v[piv] / b[piv]
            v = [x - f * y for x, y in zip(v, b)]
    return all(x == 0 for x in v)


def nullspace(vecs):
    """Basis of {c : sum_k c_k vecs[k] = 0}."""
    n = len(vecs)
    m = len(vecs[0])
    A = [[vecs[k][i] for k in range(n)] for i in range(m)]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    out = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fc]
        out.append(v)
    return out


def analyze(rule, Le, Lp, preps, cols, gens='ifs'):
    lines = []
    say = lambda s: (lines.append(s), print(s, flush=True))
    effs = effects(Le)
    idx = {e: i for i, e in enumerate(effs)}
    say(f'SETUP {rule}: effects <= {Le} ({len(effs)}), preparations <= {Lp} ({len(preps)} with positive weight), '
        f'generators {gens}')
    kept = greedy_modp(cols)
    say(f'GREEDY {rule}: {len(kept)} columns kept (rank over F_p of the full table = {len(kept)})')
    ok, why = certify(cols, kept)
    say(f'CERTIFY {rule}: rank_Q(full table) == rank_Q(reduced) == {len(kept)}: {ok} ({why})')
    if not ok:
        say('INCONCLUSIVE: full effect rank not certified')
        return lines
    say(f'REDUCED {rule}: selected preparations = ' + ' '.join(f'{preps[k][0] or "()"}/{preps[k][1]}' for k in kept))
    T = [[Fr(cols[k][i]) for k in kept] for i in range(len(effs))]   # rows: effects, cols: reduced preps
    dom = [e for e in effs if len(e[0]) <= Le - 1]
    nd = len(dom)
    drow = [T[idx[e]] for e in dom]
    img = {a: [T[idx[(a + e[0], e[1])]] for e in dom] for a in gens}
    rels = nullspace(drow)
    well = all(all(sum((c[i] * img[a][i][j] for i in range(nd)), Fr(0)) == 0 for j in range(len(kept)))
               for a in gens for c in rels)
    say(f'WELLDEF {rule}: every generator dual map preserves all {len(rels)} relations among the {nd} domain '
        f'effects on the reduced columns: {well}')
    if not well:
        say('INCONCLUSIVE: an action is not well defined on the reduced quotient')
        return lines
    ev = lambda c: [sum((c[i] * drow[i][j] for i in range(nd) if c[i] != 0), Fr(0)) for j in range(len(kept))]
    av = lambda c, a: [sum((c[i] * img[a][i][j] for i in range(nd) if c[i] != 0), Fr(0)) for j in range(len(kept))]
    Uf = [[Fr(int(i == j)) for j in range(nd)] for i in range(nd)]
    it = 0
    while True:
        it += 1
        UB = reduce_basis([ev(c) for c in Uf])
        dimU = len(UB)
        conds = []
        for c in Uf:
            stacked = []
            for a in gens:
                v = av(c, a)
                for (piv, b) in UB:
                    if v[piv] != 0:
                        f = v[piv] / b[piv]
                        v = [x - f * y for x, y in zip(v, b)]
                stacked += v
            conds.append(stacked)
        ker = nullspace(conds)
        newUf = [[sum((t[k] * Uf[k][i] for k in range(len(Uf)) if t[k] != 0), Fr(0)) for i in range(nd)] for t in ker]
        sel, B = [], []
        for c in newUf:
            rr = ev(c)
            if not in_span(rr, B):
                sel.append(c)
                B = reduce_basis([b for (_, b) in B] + [rr])
        dimNew = len(B)
        say(f'ITER {rule} {it}: dim U = {dimU} -> {dimNew}')
        Uf = sel
        if dimNew == dimU or dimNew == 0:
            break
    UB = reduce_basis([ev(c) for c in Uf])
    unit = T[idx[('', 0)]]
    say(f'INV {rule}: largest {{{",".join(gens)}}}-invariant subspace of span(effects <= {Le - 1}): dim = {len(UB)}; '
        f'unit in U: {in_span(unit, UB)}')
    for k, c in enumerate(Uf):
        terms = [(dom[i], c[i]) for i in range(nd) if c[i] != 0]
        say(f'UBASIS {rule} {k}: ' + ' + '.join(f'({co})*[{e[0] or "()"}/{e[1]}]' for e, co in terms[:10])
            + (' ...' if len(terms) > 10 else ''))
    return lines


if __name__ == '__main__':
    mode, rule = sys.argv[1], sys.argv[2]
    Le, Lp = int(sys.argv[3]), int(sys.argv[4])
    tag = f'{rule}_{Le}_{Lp}'
    if mode == 'build':
        procs = int(sys.argv[5]) if len(sys.argv) > 5 else 2
        preps, cols = build(rule, Le, Lp, procs)
        blob = pickle.dumps((preps, cols), protocol=4)
        open(f'table_{tag}.pkl', 'wb').write(blob)
        print(f'BUILD {rule}: {len(preps)} preparations x {len(cols[0])} effects; sha256 '
              f'{hashlib.sha256(blob).hexdigest()}')
    elif mode == 'analyze':
        preps, cols = pickle.loads(open(f'table_{tag}.pkl', 'rb').read())
        lines = analyze(rule, Le, Lp, preps, cols)
        open(f'analysis_{tag}.txt', 'w').write('\n'.join(lines) + '\n')
    elif mode == 'replay':
        preps, cols = pickle.loads(open(f'table_{tag}.pkl', 'rb').read())
        kept = greedy_modp(cols)
        fresh = []
        for k in kept:
            pp, r = preps[k]
            for (x, col) in prep_columns((pp, rule, Le)):
                if x == (pp, r):
                    fresh.append(col)
        same = len(fresh) == len(kept) and all(fresh[i] == cols[k] for i, k in enumerate(kept))
        print(f'REPLAY {rule}: {len(kept)} selected columns recomputed from scratch, identical to the table: {same}')
        lines = analyze(rule, Le, Lp, preps, cols)
        again = '\n'.join(lines) + '\n'
        prev = open(f'analysis_{tag}.txt').read()
        print(f'REPLAY {rule}: analysis byte-identical to the first run: {again == prev}')
