"""Verification 4: explicit relaxed (diagonal-equivalence) factorizations, independent of the flat calculus.
For H and a structure, search alignments whose ratio matrix R_b(a,c) = mu_b(sigma_b(a),c) / mu_0(sigma_0(a),c) has rank one
(exact), build the row scaling D1 (row sigma_b(a) multiplied by R_b(a,0)^-1 R_b(0,0)... chosen so R becomes column-only), and
verify D1 H with the same alignment is a STRICT Dita product with flat unitary factors (v1's builder). Reports, per matrix, the
structures admitted strictly and up to diagonal equivalence (any alignment)."""
import itertools, sys, time
from v1_explicit import *

def relaxed_explicit(H, mn, cp, rows):
    m, n = mn
    for b in range(n):
        rep = rows[b][0]
        for r in rows[b][1:]:
            for c in range(m):
                j0 = cp[c][0]; q = H[r][j0] * ginv(H[rep][j0])
                if any(H[r][j] != q * H[rep][j] for j in cp[c]): return None
    def mu(b, r, c): return H[r][cp[c][0]] * ginv(H[rows[b][0]][cp[c][0]])
    s0 = list(rows[0])
    sig = [tuple(s0)]; scale = {r: ONE for r in range(16)}
    for b in range(1, n):
        found = None
        for perm in itertools.permutations(rows[b]):
            R = [[mu(b, perm[a], c) * ginv(mu(0, s0[a], c)) for c in range(m)] for a in range(m)]
            if all(R[a][c] * R[0][0] == R[a][0] * R[0][c] for a in range(1, m) for c in range(1, m)):
                found = (perm, R); break
        if found is None: return None
        perm, R = found; sig.append(perm)
        for a in range(m): scale[perm[a]] = R[0][0] * ginv(R[a][0])   # makes R column-only
    H2 = [[H[i][j] * scale[i] for j in range(16)] for i in range(16)]
    # strict check of H2 with the found alignment, via v1's builder restricted to that alignment
    rows2 = tuple(tuple(s) for s in sig)
    ex = explicit_factorizations(H2, mn, cp, rows2, limit=1)
    ok = [s for s, i, u_ in ex if i and u_ and all(tuple(s[b]) == rows2[b] for b in range(n))]
    diag_unimodular = all(scale[r].norm2() == 1 for r in range(16))
    return bool(ok) and diag_unimodular

if __name__ == '__main__':
    t0 = time.time()
    def gp(u, k):
        out = ONE
        for _ in range(abs(k)): out = out * (u if k > 0 else u.conj())
        return out
    Wm = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
    jobs = [('act 37 arc at u = -1', [Wm], [G(-1)]), ('act 37 arc at u = 1', [Wm], [ONE]), ('act 37 arc at u = (3+4i)/5', [Wm], [G(Fr(3, 5), Fr(4, 5))])]
    import pickle
    try:
        L = pickle.load(open(os.path.join(HERE, 'loci_af_snapshot.pkl'), 'rb'))
        from splitters import cells_to_mat
        Ms = [cells_to_mat(a) for a in L[4]['atoms']]
        u5 = G(Fr(3, 5), Fr(4, 5)); u17 = G(Fr(8, 17), Fr(15, 17))
        jobs += [('orbit 4 at (u, -1, v) (relaxed-only face)', Ms, [u5, G(-1), u17]), ('orbit 4 at (u, 1, v)', Ms, [u5, ONE, u17])]
    except Exception as e: print('orbit 4 skipped', e)
    for nm, pieces, u in jobs:
        H = [[SIG[i][j] * (lambda v: v)(ONE) for j in range(16)] for i in range(16)]
        for P, x in zip(pieces, u):
            H = [[H[i][j] * gp(x, P[i][j]) for j in range(16)] for i in range(16)]
        assert is_unitary16(H)
        HT = [list(c) for c in zip(*H)]
        OR = orientations_d(pieces); cands, _ = enumerate_candidates_d(OR, len(pieces))
        nS = nR = 0
        for (f, mn, cp, rows) in cands:
            M = H if f == 'column' else HT
            s = any(i and u_ for s_, i, u_ in explicit_factorizations(M, mn, cp, rows, limit=10 ** 6))
            r = relaxed_explicit(M, mn, cp, rows)
            nS += s; nR += bool(r)
        print('%-45s explicit structures: strict %d, up to diagonal equivalence %d   %.0fs' % (nm, nS, nR, time.time() - t0), flush=True)
