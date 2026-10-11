"""b16_preflight.py — research/bridge, round 4, node B16: exact checks for BridgeReachDim.lean.

S0 (written 2026-10-11T05:31:29Z, NOTES-B16, before this script's first run). Checks P1-P5 as listed there: exact
arithmetic over the Gaussian rationals (pairs of Fractions), random data from a fixed seed (replayable); P2 symbolic
(sympy, exact).
Run from experiments/:  python3 -I -B b16_preflight.py > b16_preflight.out 2> b16_preflight.err
"""
import random
from fractions import Fraction as Fr

import sympy as sp

Z = (Fr(0), Fr(0))
ONE = (Fr(1), Fr(0))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cconj(a):
    return (a[0], -a[1])


def cinv(a):
    d = a[0] * a[0] + a[1] * a[1]
    return (a[0] / d, -a[1] / d)


def cdiv(a, b):
    return cmul(a, cinv(b))


def idx(i, j):
    return 2 * i + j


def kron2(a, b):
    return [cmul(a[i], b[j]) for i in range(2) for j in range(2)]


def chart0(x):
    return [cmul(ONE if i == 0 else x[0], x[1] if j == 0 else x[2]) for i in range(2) for j in range(2)]


def chart1(x):
    return [cmul(Z if i == 0 else ONE, x[1] if j == 0 else x[2]) for i in range(2) for j in range(2)]


def prodDet(v):
    return csub(cmul(v[idx(0, 0)], v[idx(1, 1)]), cmul(v[idx(0, 1)], v[idx(1, 0)]))


def mmul(A, B):
    n = len(A)
    return [[sum_c([cmul(A[i][k], B[k][j]) for k in range(n)]) for j in range(n)] for i in range(n)]


def mvec(A, v):
    return [sum_c([cmul(A[i][k], v[k]) for k in range(len(v))]) for i in range(len(A))]


def sum_c(xs):
    s = Z
    for x in xs:
        s = cadd(s, x)
    return s


def dag(A):
    return [[cconj(A[j][i]) for j in range(len(A))] for i in range(len(A))]


def ident(n):
    return [[ONE if i == j else Z for j in range(n)] for i in range(n)]


def inverse(A):  # Gauss-Jordan over Q(i)
    n = len(A)
    M = [list(A[i]) + list(ident(n)[i]) for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != Z)
        M[c], M[p] = M[p], M[c]
        iv = cinv(M[c][c])
        M[c] = [cmul(x, iv) for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != Z:
                f = M[r][c]
                M[r] = [csub(x, cmul(f, y)) for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]


def cayley(rng, n):  # exact unitary (1 - A)(1 + A)^(-1), A skew-Hermitian with Gaussian rational entries
    A = [[Z] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = (Fr(0), Fr(rng.randint(-5, 5), rng.randint(1, 4)))
        for j in range(i + 1, n):
            z = (Fr(rng.randint(-5, 5), rng.randint(1, 4)), Fr(rng.randint(-5, 5), rng.randint(1, 4)))
            A[i][j] = z
            A[j][i] = (-z[0], z[1])  # -conj(z)
    I_ = ident(n)
    num = [[csub(I_[i][j], A[i][j]) for j in range(n)] for i in range(n)]
    den = [[cadd(I_[i][j], A[i][j]) for j in range(n)] for i in range(n)]
    return mmul(num, inverse(den))


def rq(rng):
    return (Fr(rng.randint(-9, 9), rng.randint(1, 6)), Fr(rng.randint(-9, 9), rng.randint(1, 6)))


def main():
    rng = random.Random(20261011)
    checks = []
    # P1: the two charts cover the products, with the proof's parameters
    ok1 = True
    for _ in range(40):
        a = [rq(rng), rq(rng)]
        b = [rq(rng), rq(rng)]
        if a[0] != Z:
            x = [cdiv(a[1], a[0]), cmul(a[0], b[0]), cmul(a[0], b[1])]
            ok1 &= kron2(a, b) == chart0(x)
        a0 = [Z, a[1]]
        x1 = [Z, cmul(a[1], b[0]), cmul(a[1], b[1])]
        ok1 &= kron2(a0, b) == chart1(x1)
    checks.append(('P1 every product lies in chart0 (a0 != 0) or chart1 (a0 = 0), 40 + 40 exact cases', ok1))
    # P2: the controlled-phase control, symbolic
    t = sp.symbols('t', real=True)
    e = sp.cos(t) + sp.I * sp.sin(t)
    v = [1, 2, 3, 5 * e]                      # diag(1, 1, 1, e) (1, 2, 3, 5)
    pd = sp.expand(v[0] * v[3] - v[1] * v[2])
    target = sp.expand(5 * e - 6)
    re_pd = sp.simplify(sp.re(pd))
    print('P2 prodDet =', pd, '; real part =', re_pd)
    checks.append(('P2 prodDet(diag(1,1,1,e^{it}) (1,2,3,5)) = 5 e^{it} - 6', sp.simplify(pd - target) == 0))
    checks.append(('P2b its real part 5 cos t - 6 <= -1 < 0 for every t', sp.simplify(re_pd - (5 * sp.cos(t) - 6)) == 0))
    # P3: countercontrol — the block-diagonal SU(2) x SU(2) carries every vector to a product
    ok3 = True
    dets = []
    for _ in range(30):
        w = [rq(rng) for _ in range(4)]
        al, be = (w[0], w[1]), (w[2], w[3])
        M0 = [[cconj(al[0]), cconj(al[1])], [(-al[1][0], -al[1][1]), al[0]]]
        M1 = [[cconj(be[0]), cconj(be[1])], [(-be[1][0], -be[1][1]), be[0]]]
        H = [[Z] * 4 for _ in range(4)]
        for a in range(2):
            M = M0 if a == 0 else M1
            for b in range(2):
                for b2 in range(2):
                    H[idx(a, b)][idx(a, b2)] = M[b][b2]
        img = mvec(H, w)
        ok3 &= prodDet(img) == Z and img[idx(0, 1)] == Z and img[idx(1, 1)] == Z
        n0 = cadd(cmul(al[0], cconj(al[0])), cmul(al[1], cconj(al[1])))
        dets.append(csub(cmul(M0[0][0], M0[1][1]), cmul(M0[0][1], M0[1][0])) == n0)
    checks.append(('P3 block-diagonal elements carry 30 random vectors to products; each block has det |alpha|^2 '
                   '(so the normalized element lies in SU(2) x SU(2))', ok3 and all(dets)))
    # P4: the coset identities, on exact unitaries
    ok4 = True
    for _ in range(4):
        K = cayley(rng, 4)
        h = cayley(rng, 4)
        unit = mmul(dag(K), K) == ident(4) and mmul(dag(h), h) == ident(4)
        prod = mmul(mmul(dag(K), dag(h)), mmul(h, K)) == ident(4)
        vv = [rq(rng) for _ in range(4)]
        p = mvec(mmul(h, K), [cconj(x) for x in vv])
        back = [cconj(x) for x in mvec(dag(K), mvec(dag(h), p))]
        ok4 &= unit and prod and back == vv
    checks.append(('P4 K* h^-1 (h K) = 1 and v = conj(K* h^-1 (h K conj v)) on exact Cayley unitaries', ok4))
    # P5: the dimension count
    rows = [(d, d + 6, d + 6 < 8) for d in range(5)]
    print('P5 dimension count (d = dim of identity component, d + 6 vs 8):', rows)
    checks.append(('P5 1 + 2*3 = 7 < 8 = 2*4, and d + 6 < 8 iff d <= 1',
                   1 + 2 * 3 == 7 and 2 * 4 == 8 and [r[2] for r in rows] == [True, True, False, False, False]))
    print('\nCHECKS')
    for nm, ok in checks:
        print(('PASS ' if ok else 'FAIL ') + nm)
    print('VERDICT B16-PREFLIGHT: ' + ('all checks green' if all(ok for _, ok in checks) else 'a check failed'))


main()
