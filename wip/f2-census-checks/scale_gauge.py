#!/usr/bin/env python3
"""scale_gauge.py -- audit check D (exact integer/Fraction arithmetic). Decides nothing for any round.

Question: under Gross's odd-q dictionary (the one F2-5 fixes), is the amplitude-scale relabelling of
the alphabet, (p, c) -> (a p, a c) per site (SM Sec. 2.7, the additive-automorphism gauge; Substratum
Theorem 24(i) scope remark and Stage 2(d)), a CP or at least positive map on the register?
Reduction [W, derived in the audit report]: a I = diag(a, a^-1) . diag(1, a^2); the first factor is
symplectic (a Clifford permutation |y> -> |a y>), so the question is that of M_d = Phi_{diag(1, d)}
with d = a^2, which acts on matrix entries as  M_d(rho)[a', b'] = rho[al a' + be b', be a' + al b'],
al = (1 + d)/2, be = (1 - d)/2  (from A(x, xi)[u, v] = [u + v = 2x] w^{xi (u - v)}).
Controls: M_1 = identity (CP); M_{-1} = transpose (positive, not CP); the q = 3 case is cross-checked
against F2-5's sweep (det -1 maps positive and not CP).
Tests: CP by the Choi matrix (0/1, exact LDL); positivity by the images of all real 0/1 vectors psi
(non-PSD image => not positive, an exact witness).
"""
from fractions import Fraction
from itertools import product

def psd(M):
    n = len(M); A = [[Fraction(x) for x in row] for row in M]
    idx = list(range(n))
    while idx:
        # pick a nonzero diagonal pivot
        piv = None
        for i in idx:
            if A[i][i] < 0: return False
            if A[i][i] > 0: piv = i; break
        if piv is None:
            # all remaining diagonal zero: PSD iff remaining block zero
            return all(A[i][j] == 0 for i in idx for j in idx)
        idx.remove(piv)
        p = A[piv][piv]
        for i in idx:
            if A[i][piv] != 0:
                f = A[i][piv] / p
                for j in idx:
                    A[i][j] -= f * A[piv][j]
        for i in idx:
            A[i][piv] = A[piv][i] = Fraction(0)
    return True

def entry_map(q, d):
    inv2 = pow(2, -1, q)
    al = (1 + d) * inv2 % q; be = (1 - d) * inv2 % q
    return lambda u, v: ((al * u + be * v) % q, (be * u + al * v) % q)

def apply(q, f, rho):
    return [[rho[f(u, v)[0]][f(u, v)[1]] for v in range(q)] for u in range(q)]

def choi(q, f):
    n = q * q; C = [[0] * n for _ in range(n)]
    for i in range(q):
        for j in range(q):
            E = [[1 if (r, s) == (i, j) else 0 for s in range(q)] for r in range(q)]
            img = apply(q, f, E)
            for k in range(q):
                for l in range(q):
                    C[i * q + k][j * q + l] = img[k][l]
    return C

def positive_on_real01(q, f):
    for psi in product((0, 1), repeat=q):
        if not any(psi): continue
        rho = [[psi[u] * psi[v] for v in range(q)] for u in range(q)]
        if not psd(apply(q, f, rho)):
            return False, psi
    return True, None

ok = True
for q in (3, 5, 7, 11, 13):
    squares = sorted({a * a % q for a in range(1, q)})
    rows = []
    for d in range(1, q):
        f = entry_map(q, d)
        cp = psd(choi(q, f))
        pos, wit = positive_on_real01(q, f)
        tag = 'square' if d in squares else 'non-square'
        rows.append((d, tag, cp, pos, wit))
        if d == 1: ok &= cp
        if d == q - 1: ok &= (not cp) and pos
    print('q=%2d  squares %s' % (q, squares))
    for d, tag, cp, pos, wit in rows:
        print('      d=%2d (%-10s) CP %-5s positive-on-real-0/1 %-5s %s' % (d, tag, cp, pos, '' if wit is None else 'witness psi=%s' % (wit,)))
    scale = sorted({a: (a * a % q) for a in range(1, q)}.items())
    bad = [a for a, d in scale if not dict((r[0], r[2]) for r in rows)[d]]
    print('      amplitude scalings a with no CP image (a^2 != 1): %s' % bad)
print('CHECK-D', 'PASS' if ok else 'FAIL', ': controls d = 1 (CP) and d = -1 (positive, not CP) behave as required')
