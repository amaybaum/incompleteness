"""Exact common-invariant-subspace problem at finite horizon.

Effect functionals: protocols over an alphabet (default 'oifs') of length <= Le, each observation branch a
singleton record; evaluated (exactly) on preparations of length <= Lp.  Dual maps a* : e -> a.e (prefix)
for a in the generator set G (default W = 'i', F = 'f', S = 's'), defined on effects of length <= Le-1.

1. Check a* is well defined on the evaluated span (every evaluation relation among length <= Le-1 effects
   is preserved).  If not, the preparations are too shallow for this horizon: report and stop.
2. Compute the largest subspace U of V_{Le-1} with a* U <= U for all a in G (iterated preimages).
   Any true invariant effect space of the completion whose effects have length <= Le-1 lies inside U.
3. Report dim U, whether the unit is in U, and the dimension of the minimal invariant subspaces containing
   the unit and each single observer effect (cyclic submodules), i.e. the seed-orbit dimensions inside U.
"""
import sys
from fractions import Fraction as Fr
from itertools import product
sys.path.insert(0, '.')
sys.path.insert(0, '../rank')
from quotient import joint, preparations           # noqa: E402
from oistage_helpers import rank, nullspace        # noqa: E402


def effects(Le, alph):
    out = []
    for l in range(Le + 1):
        for pp in product(alph, repeat=l):
            pr = ''.join(pp)
            for r in range(1 << pr.count('o')):
                out.append((pr, r))
    return out


def table(preps, effs, rule):
    """rows: effects, cols: preparations; conditional probabilities, exact."""
    cache = {}
    T = []
    for (pe, re_) in effs:
        row = []
        for (pp, rp, w) in preps:
            key = pp + '|' + pe
            if key not in cache:
                cache[key] = joint(pp + pe, rule)
            j = cache[key]
            k2 = pe.count('o')
            row.append(j[(rp << k2) | re_] / w)
        T.append(row)
    return T


def reduce_basis(rows):
    """Row-reduce; return (pivot rows as basis, coordinates function)."""
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


def coords(v, basis_rows):
    """Solve v = sum c_i basis_rows[i] exactly (basis independent); return c or None."""
    n = len(basis_rows)
    if n == 0:
        return [] if all(x == 0 for x in v) else None
    m = len(v)
    A = [[basis_rows[i][j] for i in range(n)] + [v[j]] for j in range(m)]
    r, c = 0, 0
    piv = []
    while r < m and c < n:
        k = next((i for i in range(r, m) if A[i][c] != 0), None)
        if k is None:
            c += 1
            continue
        A[r], A[k] = A[k], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        c += 1
    for i in range(r, m):
        if A[i][n] != 0:
            return None
    sol = [Fr(0)] * n
    for i, pc in enumerate(piv):
        sol[pc] = A[i][n]
    return sol


if __name__ == '__main__':
    rule = sys.argv[1]
    Le = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    Lp = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    ealph = sys.argv[4] if len(sys.argv) > 4 else 'oifs'
    palph = sys.argv[5] if len(sys.argv) > 5 else 'oifs'
    gens = sys.argv[6] if len(sys.argv) > 6 else 'ifs'
    preps = preparations(Lp, rule, palph)
    effs = effects(Le, ealph)
    print(f'SETUP {rule}: Le={Le} ({ealph}), Lp={Lp} ({palph}), gens={gens}: {len(effs)} effects, {len(preps)} preparations', flush=True)
    T = table(preps, effs, rule)
    idx = {e: i for i, e in enumerate(effs)}
    print(f'RANK {rule}: effect span dim on these preparations = {rank(T)}', flush=True)
    dom = [e for e in effs if len(e[0]) <= Le - 1]
    dom_rows = [T[idx[e]] for e in dom]
    # 1. well-definedness of a* on span(dom)
    rels = nullspace([row for row in dom_rows])  # vectors c with sum_e c_e * row_e = 0
    well = True
    for a in gens:
        for c in rels:
            img = [sum((c[i] * T[idx[(a + e[0], e[1])]][j] for i, e in enumerate(dom)), Fr(0)) for j in range(len(preps))]
            if any(x != 0 for x in img):
                well = False
                break
        if not well:
            break
    print(f'WELLDEF {rule}: a* well defined on span(effects <= {Le-1}) for gens {gens}: {well}  ({len(rels)} relations checked)', flush=True)
    if not well:
        print('STOP: preparations too shallow for this effect horizon')
        sys.exit(0)
    # 2. largest invariant subspace U of span(dom): iterate U <- {e in U : a* e in U}
    #    represent U by a basis of coefficient vectors over dom (formal), modulo evaluation kernel handled by rows.
    #    Work with evaluated rows: U_rows basis; membership tests via in_span on rows.
    Ubasis = reduce_basis(dom_rows)
    Urows = [b for (_, b) in Ubasis]
    # formal generators: we need a* on arbitrary elements of U: keep U as formal combos of dom
    # Simplest exact route: U as a subspace of the formal space Q^dom containing the relation space;
    # condition e in U with a*e in U, where a* acts on formal coords by index shift and evaluated via T.
    nd = len(dom)
    formal = [[Fr(int(i == j)) for j in range(nd)] for i in range(nd)]   # standard basis
    # current U given by formal basis vectors (list of coefficient vectors)
    Uf = formal
    def evalrow(cvec):
        return [sum((cvec[i] * dom_rows[i][j] for i in range(nd)), Fr(0)) for j in range(len(preps))]
    def astar_row(cvec, a):
        return [sum((cvec[i] * T[idx[(a + dom[i][0], dom[i][1])]][j] for i in range(nd)), Fr(0)) for j in range(len(preps))]
    it = 0
    while True:
        it += 1
        Urows = [evalrow(c) for c in Uf]
        UB = reduce_basis(Urows)
        dimU = len(UB)
        # find subspace of U (formal) whose a*-images lie in span(Urows): linear condition
        # For each basis vector c_k of Uf, compute a* image row; condition: sum_k t_k astar(c_k) in span(U)
        # => solve: image rows modulo span(U) must vanish.  Reduce each image row mod UB, then find kernel.
        keep_conds = []
        for a in gens:
            reduced = []
            for c in Uf:
                v = astar_row(c, a)
                for (piv, b) in UB:
                    if v[piv] != 0:
                        f = v[piv] / b[piv]
                        v = [x - f * y for x, y in zip(v, b)]
                reduced.append(v)
            keep_conds.append(reduced)
        # kernel of t -> sum_k t_k reduced_k (stacked over a)
        cols = []
        for k in range(len(Uf)):
            cols.append(sum((keep_conds[gi][k] for gi in range(len(gens))), []))
        ker = nullspace(cols) if cols else []
        newUf = [[sum((t[k] * Uf[k][i] for k in range(len(Uf))), Fr(0)) for i in range(nd)] for t in ker]
        newrows = [evalrow(c) for c in newUf]
        dimNew = len(reduce_basis(newrows))
        print(f'ITER {rule} {it}: dim U = {dimU} -> {dimNew}', flush=True)
        if dimNew == dimU:
            break
        # keep only independent formal generators (mod evaluation): reduce formal vectors by evaluated rows
        Uf = []
        B = []
        for c, r in zip(newUf, newrows):
            if not in_span(r, B):
                Uf.append(c)
                B = reduce_basis([b for (_, b) in B] + [r])
        if dimNew == 0:
            break
    Urows = [evalrow(c) for c in Uf]
    UB = reduce_basis(Urows)
    unit = [Fr(1)] * len(preps)
    print(f'INV {rule}: largest invariant subspace of effects(<= {Le-1}) under {gens}: dim = {len(UB)}; unit in U: {in_span(unit, UB)}', flush=True)
    # 3. seed orbits inside U: for each single observer effect e in dom that lies in U, the cyclic submodule
    #    dimension (orbit under words of length <= Le-1-len(e)) -- bounded by what the table can see.
    seen = set()
    for e in dom:
        row = T[idx[e]]
        if not in_span(row, UB):
            continue
        if len(e[0]) > Le - 2:
            continue
        orbit = [unit, row]
        for l in range(1, Le - len(e[0])):
            for w in product(gens, repeat=l):
                orbit.append(T[idx[(''.join(w) + e[0], e[1])]])
        d = rank(orbit)
        key = (e, d)
        print(f'SEED {rule}: effect {e[0] or "()"}/{e[1]} in U; span(unit, words<= {Le-1-len(e[0])} . seed) dim = {d}')
