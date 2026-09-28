"""Verification 1 (independent of the monomial/flat calculus): explicit Dita factorizations in exact Gaussian rationals.

For a concrete 16x16 matrix H (entries Gaussian rationals, scaled by 4) and a structure (cp, P) of shape m x n, search the
alignments sigma_b by exact equality of entry ratios, then BUILD X (m x m), D (m x n), Y_c (n x n) and verify
  H[sigma_b(a), cp[c][d]] = X[a][c] * D[c][b] * Y_c[b][d]      for all 256 entries (exact),
  X, every Y_c flat unitary (all |entries|^2 equal, rows orthogonal), |D| = 1.
Row form: the same on the transpose."""
import itertools, sys, time
from align import *

def flat_unitary(M):
    k = len(M); v = M[0][0].norm2()
    if any(x.norm2() != v for r in M for x in r): return False
    for i in range(k):
        for j in range(i + 1, k):
            s = ZERO
            for l in range(k): s = s + M[i][l] * M[j][l].conj()
            if s != ZERO: return False
    return True
def ginv(x):
    n = x.norm2(); return G(x.a / n, -x.b / n)
def explicit_factorizations(H, mn, cp, rows, limit=4):
    """all (up to limit) alignments with an exact verified factorization; returns list of (sigmas, X, D, Y)"""
    m, n = mn
    # proportionality within classes on blocks (exact)
    for b in range(n):
        rep = rows[b][0]
        for r in rows[b][1:]:
            for c in range(m):
                j0 = cp[c][0]; q = H[r][j0] * ginv(H[rep][j0])
                if any(H[r][j] != q * H[rep][j] for j in cp[c]): return []
    def mu(b, r, c): return H[r][cp[c][0]] * ginv(H[rows[b][0]][cp[c][0]])
    s0 = list(rows[0])
    per_b = []
    for b in range(1, n):
        opts = []
        for perm in itertools.permutations(rows[b]):
            if all(mu(b, perm[a], c) * ginv(mu(b, perm[0], c)) == mu(0, s0[a], c) for a in range(1, m) for c in range(m)):
                opts.append(perm)
                if len(opts) >= limit: break
        if not opts: return []
        per_b.append(opts)
    out = []
    for choice in itertools.islice(itertools.product(*per_b), limit):
        sig = [tuple(s0)] + list(choice)
        # build: Y_c[b][d] = H[sigma_b(0), cp[c][d]]; X[a][c] = H[sigma_0(a), cp[c][0]] / H[sigma_0(0), cp[c][0]];
        # D[c][b] = ratio needed: H[sigma_b(a), cp[c][d]] = X[a][c] D[c][b] Y_c[b][d]  with D = 1 (Y carries it)
        Y = [[[H[sig[b][0]][cp[c][d]] for d in range(n)] for b in range(n)] for c in range(m)]
        X = [[H[s0[a]][cp[c][0]] * ginv(H[s0[0]][cp[c][0]]) for c in range(m)] for a in range(m)]
        D = [[ONE] * n for _ in range(m)]
        ident = all(H[sig[b][a]][cp[c][d]] == X[a][c] * D[c][b] * Y[c][b][d] for a in range(m) for b in range(n) for c in range(m) for d in range(n))
        fu = flat_unitary(X) and all(flat_unitary(Yc) for Yc in Y)
        out.append((sig, ident, fu))
    return out

if __name__ == '__main__':
    t0 = time.time()
    S0 = [[SIGE[i][j] for j in range(16)] for i in range(16)]
    OR = orientations_d([], S0); cands, _ = enumerate_candidates_d(OR, 0)
    SIGT = [list(c) for c in zip(*SIG)]
    census = set()
    for nm, f, mn, cp, rows in NAMED20: census.add((f, mn, frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows))))
    extra = []
    for (f, mn, cp, rows) in cands:
        key = (f, mn, frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows)))
        free = bool(locus_alignfree(OR, f, mn, cp, rows, False, 0))
        srt = solve_d(conditions_d(OR, f, mn, cp, rows, False), 0) is not None
        M = SIG if f == 'column' else SIGT
        ex = explicit_factorizations(M, mn, cp, rows)
        verified = any(i and u for s, i, u in ex)
        tag = 'census' if key in census else 'NOT IN CENSUS'
        print('%-6s %s %-13s align-free %s sorted %s explicit-verified %s  %s' % (f, mn, tag, free, srt, verified, '' if key in census else 'blocks %s classes %s' % (cp, rows)))
        if key not in census and verified: extra.append((f, mn, cp, rows, ex[0][0]))
    print('structures of SIG outside act 37 census with an explicit exact factorization:', len(extra))
    for f, mn, cp, rows, sig in extra: print('  ', f, mn, 'blocks', cp, '\n      classes', rows, '\n      alignment', sig)
    print('%.0fs' % (time.time() - t0))
