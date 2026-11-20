#!/usr/bin/env python3
"""UNIV-1 exact checks (paper-only unit; small exact cases).

All lattice computations are exact integer arithmetic (numpy int64; every
intermediate value is below 7 * 2**16). No floating-point value certifies any
statement. Rules:

  Q   published rounded rule, SM section 4.2, on the representatives 0..q-1:
        x_{t+1}(i) = floor((sum_{j~i} x_t(j) + 1)/3) - x_{t-1}(i)   mod q,  q = 2**16
  RZ  the same recurrence on signed integers (no reduction)
  LIN exact linear member  x_{t+1}(i) = sum_{j~i} x_t(j) - x_{t-1}(i)  mod q
  BBM Margolus billiard-ball block rule (countercontrol)

Run:   python3 -I univ_checks.py            controls and block checks (a few seconds)
       python3 -I univ_checks.py --search   also the bounded negative searches S1-S4 (about 90 s)
Exit status 0 iff every check holds.
"""
import itertools
import sys
from collections import Counter

import numpy as np

q = 2 ** 16
c = 2 ** 15
RESULTS = []
COMPUTED = {"Q_blocks": {}}   # inputs of the classifier (F2), filled by the checks themselves
INV3 = pow(3, -1, q)          # the coupling 1/d for d = 3 exists in Z/2^16 (3 does not divide q)


def check(name, ok, info=""):
    RESULTS.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}{('  ' + info) if info else ''}")


def nbsum(x):
    return sum(np.roll(x, sh, ax) for ax in range(x.ndim) for sh in (1, -1))


def stepQ(xp, x):
    return x, ((nbsum(x) + 1) // 3 - xp) % q


def stepZ(yp, y):
    return y, np.floor_divide(nbsum(y) + 1, 3) - yp


def stepLIN(xp, x):
    return x, (nbsum(x) - xp) % q


def additive_test(step, mod, seed, shape=(4, 4, 4), n=10):
    """True iff step(a+b) == step(a)+step(b) (mod `mod`) on n random pairs of two-slice states."""
    rng = np.random.RandomState(seed)
    for _ in range(n):
        a = [rng.randint(0, mod, shape).astype(np.int64) for _ in range(2)]
        b = [rng.randint(0, mod, shape).astype(np.int64) for _ in range(2)]
        sm = [(a[0] + b[0]) % mod, (a[1] + b[1]) % mod]
        fa, fb, fs = step(*a), step(*b), step(*sm)
        if not all(np.array_equal((fa[k] + fb[k]) % mod, fs[k] % mod) for k in (0, 1)):
            return False
    return True


def poly_mul(f, g, mod):
    h = {}
    for e1, c1 in f.items():
        for e2, c2 in g.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            h[e] = (h.get(e, 0) + c1 * c2) % mod
    return {e: v for e, v in h.items() if v}


def poly_pow(f, n, mod):
    r = {tuple(0 for _ in next(iter(f))): 1}
    b = dict(f)
    while n:
        if n & 1:
            r = poly_mul(r, b, mod)
        b = poly_mul(b, b, mod)
        n >>= 1
    return r


def runQ(xp, x, T):
    for _ in range(T):
        xp, x = stepQ(xp, x)
    return xp, x


# ------------------------------------------------------------------ A. the rule
def checks_A():
    # A1: q = 2 specialisation is U2 of DELIVER-1: g(s) = floor((s+1)/3) mod 2, subtraction = XOR
    ok = all(((s + 1) // 3 - p) % 2 == ((((s + 1) // 3) % 2) ^ p) for s in range(7) for p in (0, 1))
    ok &= [((s + 1) // 3) % 2 for s in range(7)] == [0, 0, 1, 1, 1, 0, 0]
    check("A1 q=2 member equals U2", ok)

    # A2: linear members are additive (pair-state map is a group endomorphism): Main 3.2 (q=2),
    # SM exact linear rule (q=2^16, coupling 1) and the coupling-1/3 member (q=2^16, alpha = 3^{-1} mod q)
    lin2 = additive_test(lambda xp, x: (x, (nbsum(x) - xp) % 2), 2, 1)
    linq = additive_test(lambda xp, x: (x, (nbsum(x) - xp) % q), q, 2)
    lina = additive_test(lambda xp, x: (x, (INV3 * nbsum(x) - xp) % q), q, 3)
    COMPUTED["LIN_additive"] = lin2 and linq and lina
    check("A2 linear members additive (q=2; q=2^16 with alpha=1 and alpha=3^-1)", lin2 and linq and lina)

    # L1: the Frobenius step of Theorem L: S = Q0^(p^(k-1)) satisfies S(X)^p = S(X^p) mod p^k (p = 2),
    # for Q0 = 1 - alpha*A*T*prod(X) + T^2*prod(X)^2 after the light-cone substitution (d = 1 and d = 3)
    def q0(d, alpha, mod):
        f = {tuple([0] * (d + 1)): 1}
        for j in range(d):
            for sq in (2, 0):                      # alpha * (X_j^2 + 1) * prod_{k != j} X_k * T
                e = [1] * d + [1]
                e[j] = sq
                f[tuple(e)] = (f.get(tuple(e), 0) - alpha) % mod
        f[tuple([2] * d + [2])] = 1
        return {e: v % mod for e, v in f.items() if v % mod}
    ok = True
    for d, ks in ((1, (1, 2, 3, 4)), (3, (1, 2))):
        for k in ks:
            mod = 2 ** k
            for alpha in (1, pow(3, -1, mod)):
                S = poly_pow(q0(d, alpha, mod), 2 ** (k - 1), mod)
                lhs = poly_mul(S, S, mod)
                rhs = {tuple(2 * a for a in e): v for e, v in S.items()}
                ok &= lhs == rhs
    check("L1 Theorem L Frobenius step S(X)^2 = S(X^2) mod 2^k (d=1: k<=4; d=3: k<=2; alpha = 1, 3^-1)", ok)

    # A3: Q is not additive: F(z+z) != F(z)+F(z) for z = one unit at the origin (current slice)
    z = (np.zeros((4, 4, 4), np.int64), np.zeros((4, 4, 4), np.int64))
    z[1][0, 0, 0] = 1
    fz = stepQ(*z)
    zz = (z[0], 2 * z[1])
    fzz = stepQ(*zz)
    ok = not np.array_equal((2 * fz[1]) % q, fzz[1])
    COMPUTED["Q_additive"] = additive_test(stepQ, q, 4)
    ok &= not COMPUTED["Q_additive"]
    check("A3 rounded rule violates additivity", ok, f"F(z)[nbr]={int(fz[1][1,0,0])}, F(2z)[nbr]={int(fzz[1][1,0,0])}")

    # A4: fixed points on the invariant subgroup V1 (period 4 along e1, constant along e2,e3,
    # symmetric under i1 -> 1 - i1; values (a,a,b,b)): each a-site has neighbour sum 5a + b.
    def count_round():
        cnt = 0
        for a in range(q):
            base = 5 * a + 1
            lo, hi = base // 3, (base + (q - 1)) // 3
            m = lo + ((2 * a - lo) % q)
            while m <= hi:
                for r in range(3):
                    b = 3 * m + r - base
                    if 0 <= b < q and (b + base) // 3 == m and ((a + 5 * b + 1) // 3 - 2 * b) % q == 0:
                        cnt += 1
                m += q
        return cnt

    nr = count_round()
    nl = sum(1 for a in range(q) if ((-3 * a) % q + 3 * a) % q == 0 and (a + 3 * ((-3 * a) % q)) % q == 0)
    pow2 = lambda n: n > 0 and (n & (n - 1)) == 0
    check("A4 rounded rule: fixed points on V1 neither 0 nor a power of 2 (not affine under any relabelling)",
          nr == 196606 and not pow2(nr), f"count={nr}")
    check("A4b countercontrol: linear rule fixed points on V1 a power of 2", pow2(nl), f"count={nl}")


# ------------------------------------------------------------- C. vacuum q = 2^16
def checks_C():
    n = 48
    xp = np.zeros((n, n, n), np.int64)
    x = xp.copy()
    x[0, 0, 0] = 2
    xp2, x2 = stepQ(xp, x)
    nb = [x2[1, 0, 0], x2[-1, 0, 0], x2[0, 1, 0], x2[0, -1, 0], x2[0, 0, 1], x2[0, 0, -1]]
    check("C1 a single symbol 2 in the vacuum reaches all six neighbours in one step", all(v == 1 for v in nb))
    xp = np.zeros((n, n, n), np.int64)
    x = xp.copy()
    x[0, 0, 0] = 1
    idx = np.indices((n, n, n))
    dist = sum(np.minimum(idx[k], n - idx[k]) for k in range(3))
    rad = []
    for t in range(1, 21):
        xp, x = stepQ(xp, x)
        nz = x != 0
        rad.append(int(dist[nz].max()) if nz.any() else -1)
    check("C2 seed (0,1) in the vacuum: support radius t-2 for t=3..20 (light-cone growth)",
          rad[2:] == list(range(1, 19)), f"radii={rad}")

    # C3: a slab |x1 - 24| <= 12 held at c=2^15 inside uniform noise is eroded:
    # the centre plane, 13 sites from the noise, first deviates at t = 15 (light-cone bound: 13)
    rng = np.random.RandomState(11)
    L, n = 48, 6
    xp = rng.randint(0, q, (L, n, n)).astype(np.int64)
    x = rng.randint(0, q, (L, n, n)).astype(np.int64)
    xp[12:37] = c
    x[12:37] = c
    hit = None
    for t in range(1, 30):
        xp, x = stepQ(xp, x)
        if (x[24] != c).any() or (xp[24] != c).any():
            hit = t
            break
    check("C3 mid-background slab in uniform noise (one seeded instance): centre plane deviates at t = 15", hit == 15,
          f"t={hit}")

    # A5: the quadratic energy of the linear wave (coupling 1/3) is not conserved by RZ:
    # E = sum y_t^2 + sum y_{t-1}^2 - (1/3) sum_i y_t(i) sum_{j~i} y_{t-1}(j); seed y_0 = 2 at one site
    from fractions import Fraction as Fr
    yp = np.zeros((5, 5, 5), np.int64)
    y = yp.copy()
    y[2, 2, 2] = 2
    E = lambda a, b: Fr(int((b * b).sum() + (a * a).sum())) - Fr(int((b * nbsum(a)).sum()), 3)
    E0 = E(yp, y)
    yp, y = stepZ(yp, y)
    E1 = E(yp, y)
    check("A5 linear-wave energy not conserved by RZ", E0 == 4 and E1 == 6, f"E0={E0}, E1={E1}")


# ----------------------------------------------------- D. mid-alphabet embedding
def checks_D():
    rng = np.random.RandomState(7)
    ok = True
    mx = 0
    for _ in range(5):
        yp = rng.randint(-3, 4, (6, 6, 6)).astype(np.int64)
        y = rng.randint(-3, 4, (6, 6, 6)).astype(np.int64)
        xp, x = (c + yp) % q, (c + y) % q
        for _ in range(30):
            yp, y = stepZ(yp, y)
            xp, x = stepQ(xp, x)
            mx = max(mx, int(np.abs(y).max()))
            ok &= mx < c and np.array_equal(x, (c + y) % q)
    check("D1 Q at background c=2^15 equals c + RZ while |y| < 2^15", ok, f"max|y|={mx}")


# ------------------------------------------------------------------- E. blocks
def wire_W1(L, n, o=30):
    yp = np.zeros((L, n, n), np.int64)
    y = yp.copy()
    yp[1::2, 0, 0] = -1
    yp[o + 3, 0, 0] = 1
    y[o + 2, 0, 0] = -1
    y[o + 4, 0, 0] = 1
    return yp, y


def line_W2(L, o=24):
    bp = np.zeros(L, np.int64)
    bc = np.zeros(L, np.int64)
    bp[1::2] = np.tile([-1, 1], L // 4)
    bc[0::2] = np.tile([-1, 1], L // 4)
    D = [-1, -1, -1, 1, -1, -1, -1, 1]
    bp[[o + 1, o + 3, o + 5, o + 7]] = D[:4]
    bc[[o, o + 2, o + 4, o + 6]] = D[4:]
    return bp, bc


def checks_E():
    # E1: W1 glider (uniform oscillating line, a=-1, b=0) in the full 3D rule Q
    L, n = 60, 8
    yp, y = wire_W1(L, n)
    xp, x = (c + yp) % q, (c + y) % q
    x0p, x0 = xp.copy(), x.copy()
    ok = True
    for t in range(1, 61):
        xp, x = stepQ(xp, x)
        off = x.copy()
        off[:, 0, 0] = c
        ok &= bool((off == c).all() and (np.abs(x - c) <= 1).all())
        if t % 6 == 0:
            d = t // 3
            ok &= np.array_equal(np.roll(x0p, d, 0), xp) and np.array_equal(np.roll(x0, d, 0), x)
    check("E1 W1 signal: translation +2 every 6 ticks for 60 ticks, off-line sites at c, |y|<=1", ok)
    COMPUTED["Q_blocks"]["wire"] = ok

    # E1b countercontrol: the same pattern on the vacuum c=0 (values -1 -> q-1) does not translate
    xp, x = yp % q, y % q
    a0p, a0 = xp.copy(), x.copy()
    xp, x = runQ(xp, x, 6)
    off = x.copy()
    off[:, 0, 0] = 0
    check("E1b countercontrol: on the vacuum 0 the pattern leaks off the line", off.any()
          and not np.array_equal(np.roll(a0, 2, 0), x))

    # E2: W2 glider (staggered line) in 3D: shift -1 with negation every 3 ticks
    L = 48
    bp, bc = line_W2(L)
    Yp = np.zeros((L, n, n), np.int64)
    Y = Yp.copy()
    Yp[:, 0, 0] = bp
    Y[:, 0, 0] = bc
    xp, x = (c + Yp) % q, (c + Y) % q
    ok = True
    for t in range(1, 61):
        xp, x = stepQ(xp, x)
        off = x.copy()
        off[:, 0, 0] = c
        ok &= bool((off == c).all() and (np.abs(x - c) <= 1).all())
        if t % 3 == 0:
            k = t // 3
            sg = (-1) ** k
            ok &= np.array_equal((c + sg * np.roll(Yp, -k, 0)) % q, xp) and np.array_equal((c + sg * np.roll(Y, -k, 0)) % q, x)
    check("E2 W2 signal: shift -1 with negation every 3 ticks for 60 ticks", ok)
    COMPUTED["Q_blocks"]["wire"] &= ok

    # E3: memory. An isolated site (a,b) in {-1,0,1}^2 runs (a,b)->(b,-a)->(-a,-b)->(-b,a)
    ok = True
    for a, b in itertools.product((-1, 0, 1), repeat=2):
        xp = np.full((5, 5, 5), c, np.int64)
        x = xp.copy()
        xp[2, 2, 2] += a
        x[2, 2, 2] += b
        seq = []
        for _ in range(4):
            xp, x = stepQ(xp, x)
            seq.append((int(xp[2, 2, 2] - c), int(x[2, 2, 2] - c)))
            m = x.copy()
            m[2, 2, 2] = c
            ok &= bool((m == c).all())
        ok &= seq == [(b, -a), (-a, -b), (-b, a), (a, b)]
    # frozen staggered line (-1,1)/(0,0): period 4, off-line untouched
    L = 24
    Yp = np.zeros((L, 6, 6), np.int64)
    Y = Yp.copy()
    Yp[1::2, 0, 0] = np.tile([-1, 1], L // 4)
    xp, x = (c + Yp) % q, (c + Y) % q
    s0 = (xp.copy(), x.copy())
    seen = []
    for t in range(1, 9):
        xp, x = stepQ(xp, x)
        seen.append(np.array_equal(xp, s0[0]) and np.array_equal(x, s0[1]))
        off = x.copy()
        off[:, 0, 0] = c
        ok &= bool((off == c).all())
    ok &= seen == [False, False, False, True, False, False, False, True]
    check("E3 memory: isolated trits period 4; frozen staggered line period 4", ok)
    COMPUTED["Q_blocks"]["memory"] = ok

    # E4: crossing in Q. W1 along e1 at (.,0,0), signal starting at x=8 (at x=38 by t=90);
    # W2 along e2 at (24,.,z), signal starting at y=4 (moves -1 per 3 ticks, through y=0 and on).
    # Separation z=3: the joint Q orbit is the superposition of the two solo orbits for 90 ticks.
    # Countercontrol z=2: the site (24,0,1) neighbours both wires and superposition fails.
    def crossing(zsep, T=90):
        Lx, Ly, nz = 60, 48, 8
        A = wire_W1(Lx, 1, o=8)
        Ap = np.zeros((Lx, Ly, nz), np.int64)
        Ac = Ap.copy()
        Ap[:, 0, 0] = A[0][:, 0, 0]
        Ac[:, 0, 0] = A[1][:, 0, 0]
        bp, bc = line_W2(Ly, o=4)
        Bp = np.zeros((Lx, Ly, nz), np.int64)
        Bc = Bp.copy()
        Bp[24, :, zsep] = bp
        Bc[24, :, zsep] = bc
        sA, sB, sAB = [((c + u) % q, (c + v) % q) for u, v in ((Ap, Ac), (Bp, Bc), (Ap + Bp, Ac + Bc))]
        A0, B0 = (sA[0].copy(), sA[1].copy()), (sB[0].copy(), sB[1].copy())
        first_fail = None
        tern = True
        for t in range(1, T + 1):
            sA, sB, sAB = stepQ(*sA), stepQ(*sB), stepQ(*sAB)
            tern &= bool((np.abs(sAB[1] - c) <= 1).all())
            if first_fail is None and not np.array_equal(sA[1] + sB[1] - c, sAB[1]):
                first_fail = t
        moved = np.array_equal(np.roll(A0[1], 30, 0), sA[1]) and np.array_equal(np.roll(B0[1], -30, 1), sB[1])
        return first_fail, tern, moved

    f3, t3, m3 = crossing(3)
    f2, _, _ = crossing(2)
    ok = f3 is None and t3 and m3 and f2 is not None
    check("E4 crossing in Q: separation 3 superposes for 90 ticks with both signals traversing the crossing; "
          "separation 2 does not", ok, f"separation 2 first fails at t={f2}")
    COMPUTED["Q_blocks"]["crossing"] = ok

    # E5: plain 90-degree corners on a rectangular loop (12+12+12+12), compared with the 1D ring
    def loop_mismatch(pv, cv, defect, T):
        K = 12
        path = ([(4 + i, 4, 0) for i in range(K)] + [(4 + K, 4 + j, 0) for j in range(K)]
                + [(4 + K - i, 4 + K, 0) for i in range(K)] + [(4, 4 + K - j, 0) for j in range(K)])
        Lp = len(path)
        P = 2 * len(pv)
        bp = np.zeros(Lp, np.int64)
        bc = np.zeros(Lp, np.int64)
        bp[1::2] = np.tile(pv, Lp // P)
        bc[0::2] = np.tile(cv, Lp // P)
        if defect:
            bp[[5, 7, 9, 11]] = defect[:4]
            bc[[4, 6, 8, 10]] = defect[4:]
        N = 2 * K + 12
        Yp = np.zeros((N, N, 3), np.int64)
        Y = Yp.copy()
        for k, s in enumerate(path):
            Yp[s] = bp[k]
            Y[s] = bc[k]
        pi = np.array(path)
        yp, y = bp.copy(), bc.copy()
        for t in range(1, T + 1):
            yp, y = y, np.floor_divide(np.roll(y, 1) + np.roll(y, -1) + 1, 3) - yp
            Yp, Y = stepZ(Yp, Y)
            onp = Y[pi[:, 0], pi[:, 1], pi[:, 2]]
            off = Y.copy()
            off[pi[:, 0], pi[:, 1], pi[:, 2]] = 0
            if not np.array_equal(onp, y) or off.any():
                return t
        return None

    m1 = loop_mismatch([-1, 1], [-1, 1], None, 200)
    m2 = loop_mismatch([-1], [0], None, 200)
    m3 = loop_mismatch([-1, 1], [-1, 1], [-1, -1, -1, 1, -1, -1, -1, 1], 200)
    check("E5 plain corners: staggered background transparent; uniform background leaks; W2 signal not transparent",
          m1 is None and m2 == 2 and m3 is not None, f"first mismatch: bg-stag={m1}, bg-unif={m2}, stag+signal={m3}")

    # E6: a finite W2 segment is frozen (period 4, stays in the line sector for 240 ticks);
    # a W2 signal that reaches a segment end leaves the line sector
    L, n = 64, 8

    def seg(a, with_signal):
        bp, bc = line_W2(L) if with_signal else line_W2(L)
        if not with_signal:
            bp = np.zeros(L, np.int64)
            bc = np.zeros(L, np.int64)
            bp[1::2] = np.tile([-1, 1], L // 4)
            bc[0::2] = np.tile([-1, 1], L // 4)
        bp[:a] = 0
        bc[:a] = 0
        bp[56:] = 0
        bc[56:] = 0
        Yp = np.zeros((L, n, n), np.int64)
        Y = Yp.copy()
        Yp[:, 0, 0] = bp
        Y[:, 0, 0] = bc
        for t in range(1, 241):
            Yp, Y = stepZ(Yp, Y)
            off = Y.copy()
            off[:, 0, 0] = 0
            if off.any() or np.abs(Y).max() > 1:
                return t
        return None

    def seg_W1(a):
        Yp = np.zeros((L, n, n), np.int64)
        Y = Yp.copy()
        Yp[1::2, 0, 0] = -1
        Yp[:a, 0, 0] = 0
        Yp[56:, 0, 0] = 0
        for t in range(1, 241):
            Yp, Y = stepZ(Yp, Y)
            off = Y.copy()
            off[:, 0, 0] = 0
            if off.any() or np.abs(Y).max() > 1:
                return t
        return None

    w1 = [seg_W1(a) for a in (8, 9, 10, 11)]
    check("E6a finite W1 segments leave the line sector (the W1 background needs an unbounded line)",
          all(v is not None for v in w1), f"leave times: {w1}")
    frozen = [seg(a, False) for a in (8, 9, 10, 11)]
    leak = [seg(a, True) for a in (8, 9, 10, 11)]
    check("E6 finite W2 segments frozen; a W2 signal at a segment end leaves the line sector",
          all(v is None for v in frozen) and all(v is not None for v in leak), f"leave times with signal: {leak}")
    COMPUTED["Q_blocks"]["memory"] &= all(v is None for v in frozen)


# ----------------------------------------------------------- F. countercontrols
def bbm_step(g, t):
    o = t % 2
    g = np.roll(g, (-o, -o), (0, 1))
    a, b, cc, d = g[0::2, 0::2], g[0::2, 1::2], g[1::2, 0::2], g[1::2, 1::2]
    cnt = a + b + cc + d
    na, nb, nc, nd = a.copy(), b.copy(), cc.copy(), d.copy()
    one = cnt == 1
    na[one], nb[one], nc[one], nd[one] = d[one], cc[one], b[one], a[one]
    d1 = (cnt == 2) & (a == 1) & (d == 1)
    d2 = (cnt == 2) & (b == 1) & (cc == 1)
    na[d1], nd[d1], nb[d1], nc[d1] = 0, 0, 1, 1
    nb[d2], nc[d2], na[d2], nd[d2] = 0, 0, 1, 1
    h = np.zeros_like(g)
    h[0::2, 0::2], h[0::2, 1::2], h[1::2, 0::2], h[1::2, 1::2] = na, nb, nc, nd
    return np.roll(h, (o, o), (0, 1))


def bbm_run(g, T, t0=0):
    for t in range(t0, t0 + T):
        g = bbm_step(g, t)
    return g


def checks_F():
    n = 32
    blocks = {}
    # glider
    g = np.zeros((n, n), np.int64)
    g[4, 4] = 1
    pos = []
    for t in range(8):
        pos.append(tuple(np.argwhere(g)[0]))
        g = bbm_step(g, t)
    blocks["wire"] = pos == [(4 + t, 4 + t) for t in range(8)]
    # interaction gate: A from (4,4) moving (+,+); B from (13,13) moving (-,-); 12 ticks
    table = {}
    for A, B in itertools.product((0, 1), repeat=2):
        g = np.zeros((n, n), np.int64)
        if A:
            g[4, 4] = 1
        if B:
            g[13, 13] = 1
        h = bbm_run(g, 12)
        table[(A, B)] = (int(h[16, 16]), int(h[1, 1]), int(h[1, 16]), int(h[16, 1]), int(h.sum()))
    gate = all(table[(A, B)] == (A & (1 - B), (1 - A) & B, A & B, A & B, A + B) for A, B in table)
    blocks["gate"] = gate
    # fan-out: the gate with B = 1 gives A on both deflected outputs and NOT A on B's straight output
    blocks["fanout"] = all(table[(A, 1)][2] == A and table[(A, 1)][3] == A and table[(A, 1)][1] == 1 - A
                           for A in (0, 1))
    # reflection: a particle meeting a horizontal wall (row 12) returns along its path; wall unchanged
    g = np.zeros((n, n), np.int64)
    g[12, :] = 1
    g[4, 4] = 1
    traj = []
    for t in range(16):
        traj.append(tuple(int(a) for a in [v for v in np.argwhere(g) if v[0] != 12][0]))
        g = bbm_step(g, t)
    reflect = traj[:8] == [(4 + t, 4 + t) for t in range(8)] and traj[8:16] == [(11 - t, 11 - t) for t in range(8)]
    reflect &= bool(g[12, :].all()) and g.sum() == n + 1
    # turn: with a supplied constant particle (B = 1) a signal A leaves on a path at 90 degrees (gate table)
    blocks["turn"] = reflect and table[(1, 1)][2] == 1 and table[(1, 1)][3] == 1 and table[(1, 1)][0] == 0
    # memory: a particle between two walls returns to its initial state
    g0 = np.zeros((n, n), np.int64)
    g0[2, :] = 1
    g0[12, :] = 1
    g0[4, 4] = 1
    g = g0.copy()
    per = None
    for t in range(1, 400):
        g = bbm_step(g, t - 1)
        if t % 2 == 0 and np.array_equal(g, g0):
            per = t
            break
    blocks["memory"] = per is not None
    # crossing: two particles on crossing diagonals at different times do not interact
    gA = np.zeros((n, n), np.int64)
    gA[4, 4] = 1
    gB = np.zeros((n, n), np.int64)
    gB[8, 21] = 1   # top-right of its block: moves (+1,-1); its path crosses A's at a different time
    hA, hB, hAB = bbm_run(gA, 20), bbm_run(gB, 20), bbm_run(gA + gB, 20)
    blocks["crossing"] = np.array_equal(hA + hB, hAB)
    rng = np.random.RandomState(5)
    add = True
    for _ in range(10):
        g1 = rng.randint(0, 2, (n, n)).astype(np.int64)
        g2 = rng.randint(0, 2, (n, n)).astype(np.int64)
        add &= np.array_equal((bbm_step(g1, 0) + bbm_step(g2, 0)) % 2, bbm_step((g1 + g2) % 2, 0))
    COMPUTED["BBM_additive"] = bool(add)
    check("F1 countercontrol BBM: wire, turn (by collision), crossing, interaction gate, fan-out, memory all verified",
          all(blocks.values()), f"{blocks}; gate table={table}; memory period={per}")
    return blocks


def classify(additive, blocks):
    need = ["wire", "turn", "crossing", "gate", "fanout", "memory"]
    if additive:
        return "not universal (Theorem L)"
    missing = [b for b in need if not blocks.get(b)]
    return "universal (all blocks verified)" if not missing else "undecided; missing " + ",".join(missing)


# ------------------------------------------------------------- S. searches
def search_S1():
    """corner gadgets: 3 sites (inner corner X, outer O1, O2), two-slice values in {-1,0,1}."""
    def run(pv, cv, defect, direction):
        K = 20
        path = ([(3 + i, 3, 3) for i in range(K)] + [(3 + K, 3 + j, 3) for j in range(K)]
                + [(3 + K - i, 3 + K, 3) for i in range(K)] + [(3, 3 + K - j, 3) for j in range(K)])
        Lp = len(path)
        P = 2 * len(pv)
        start = K - 14 if direction > 0 else K + 6
        bp = np.zeros(Lp, np.int64)
        bc = np.zeros(Lp, np.int64)
        bp[1::2] = np.tile(pv, Lp // P)
        bc[0::2] = np.tile(cv, Lp // P)
        bp[[start + 1, start + 3, start + 5, start + 7]] = defect[:4]
        bc[[start, start + 2, start + 4, start + 6]] = defect[4:]
        ref = []
        yp, y = bp.copy(), bc.copy()
        T = 90
        for _ in range(T):
            yp, y = y, np.floor_divide(np.roll(y, 1) + np.roll(y, -1) + 1, 3) - yp
            ref.append(y.copy())
        bg_p = np.zeros(Lp, np.int64)
        bg_c = np.zeros(Lp, np.int64)
        bg_p[1::2] = np.tile(pv, Lp // P)
        bg_c[0::2] = np.tile(cv, Lp // P)
        ref_bg = []
        yp, y = bg_p.copy(), bg_c.copy()
        for _ in range(T):
            yp, y = y, np.floor_divide(np.roll(y, 1) + np.roll(y, -1) + 1, 3) - yp
            ref_bg.append(y.copy())
        C = path[K]
        gad = [(C[0] - 1, C[1] + 1, C[2]), (C[0] + 1, C[1], C[2]), (C[0], C[1] - 1, C[2])]
        far = np.array([abs(k - K) > 4 for k in range(Lp)])
        pi = np.array(path)
        def passes(gv, with_signal):
            Yp = np.zeros((K + 8, K + 8, 7), np.int64)
            Y = Yp.copy()
            for k, s_ in enumerate(path):
                Yp[s_] = bp[k] if with_signal else bg_p[k]
                Y[s_] = bc[k] if with_signal else bg_c[k]
            for gs, (u, v) in zip(gad, zip(gv[0::2], gv[1::2])):
                Yp[gs] = u
                Y[gs] = v
            r = ref if with_signal else ref_bg
            for t in range(T):
                Yp, Y = stepZ(Yp, Y)
                if np.abs(Y).max() > 1 or not np.array_equal(Y[pi[:, 0], pi[:, 1], pi[:, 2]][far], r[t][far]):
                    return False
            return True

        bg_ok = passes((0,) * 6, False)
        plain = passes((0,) * 6, True)
        good = sum(passes(gv, True) for gv in itertools.product((-1, 0, 1), repeat=6))
        return bg_ok, plain, good

    # W2 only: on this loop the W1 background alone leaves {-1,0,1} at the plain corners (E5), so a W1
    # corner search would be vacuous. Pass criterion: the 1D-ring evolution reproduced, undelayed and
    # unsigned, at every path site farther than 4 from the gadget corner, with all values in {-1,0,1}.
    bg_ok, plain, good = run([-1, 1], [-1, 1], [-1, -1, -1, 1, -1, -1, -1, 1], -1)
    COMPUTED["Q_blocks"]["turn"] = good > 0
    check("S1 W2 corner gadgets (729): background control passes, plain corner fails, no gadget passes the signal",
          bg_ok and not plain and good == 0, f"background control={bg_ok}, plain corner={plain}, passing={good}")


def search_S2():
    """two parallel staggered wires (y=0, y=3; second wire negated) and a 2-site bridge at x0."""
    Lx, ny, nz = 48, 8, 5
    D = [-1, -1, -1, 1, -1, -1, -1, 1]

    def build(x0, gv, with_defect):
        Yp = np.zeros((Lx, ny, nz), np.int64)
        Y = Yp.copy()
        bp, bc = line_W2(Lx, o=x0 + 10) if with_defect else line_W2(Lx, o=x0 + 10)
        if not with_defect:
            bp = np.zeros(Lx, np.int64)
            bc = np.zeros(Lx, np.int64)
            bp[1::2] = np.tile([-1, 1], Lx // 4)
            bc[0::2] = np.tile([-1, 1], Lx // 4)
        cp = np.zeros(Lx, np.int64)
        cc = np.zeros(Lx, np.int64)
        cp[1::2] = -np.tile([-1, 1], Lx // 4)
        cc[0::2] = -np.tile([-1, 1], Lx // 4)
        Yp[:, 0, 0], Y[:, 0, 0], Yp[:, 3, 0], Y[:, 3, 0] = bp, bc, cp, cc
        Yp[x0, 1, 0], Y[x0, 1, 0], Yp[x0, 2, 0], Y[x0, 2, 0] = gv
        return Yp, Y

    out = Counter()
    for x0 in (20, 21, 22, 23):
        for gv in itertools.product((-1, 0, 1), repeat=4):
            s = build(x0, gv, False)
            s0 = build(x0, (0, 0, 0, 0), False)
            r = build(x0, gv, True)
            transp = True
            hist_r, hist_s = [], []
            for _ in range(72):
                s, s0, r = stepZ(*s), stepZ(*s0), stepZ(*r)
                transp &= np.array_equal(s[1][:, 0, 0], s0[1][:, 0, 0]) and np.array_equal(s[1][:, 3, 0], s0[1][:, 3, 0])
                hist_r.append(r)
                hist_s.append(s)
            if not transp:
                out["bridge disturbs the wires"] += 1
                continue
            if max(int(np.abs(h[1]).max()) for h in hist_r) > 1:
                out["leaves {-1,0,1}"] += 1
                continue
            dB = any(not np.array_equal(hr[1][:, 3, 0], hs[1][:, 3, 0]) for hr, hs in zip(hist_r, hist_s))
            out["signal reaches second wire" if dB else "no effect on second wire"] += 1
    COMPUTED["Q_blocks"]["gate"] = out["signal reaches second wire"] > 0
    check("S2 bridge survey (4 positions x 81): no bridge moves a signal onto the second wire",
          out["signal reaches second wire"] == 0, str(dict(out)))


def search_S3():
    """RZ vacuum: all seeds in a 2x1x1 or 3x1x1 box with two-slice values in {-1,0,1}; horizon 40."""
    n = 16
    tally = Counter()
    for shape in ((2, 1, 1), (3, 1, 1)):
        k = int(np.prod(shape))
        for pv in itertools.product((-1, 0, 1), repeat=k):
            for cv in itertools.product((-1, 0, 1), repeat=k):
                if not any(pv) and not any(cv):
                    continue
                yp = np.zeros((n, n, n), np.int64)
                y = yp.copy()
                sl = tuple(slice(n // 2, n // 2 + s) for s in shape)
                yp[sl] = np.array(pv).reshape(shape)
                y[sl] = np.array(cv).reshape(shape)
                p0, c0 = yp.copy(), y.copy()
                kind = "undecided"
                for t in range(1, 41):
                    yp, y = stepZ(yp, y)
                    nz = np.argwhere((yp != 0) | (y != 0))
                    if (nz.max(0) - nz.min(0)).max() > n - 6:
                        kind = "grows"
                        break
                    hit = None
                    for d in itertools.product(range(-3, 4), repeat=3):
                        if np.array_equal(np.roll(p0, d, (0, 1, 2)), yp) and np.array_equal(np.roll(c0, d, (0, 1, 2)), y):
                            hit = d
                            break
                    if hit is not None:
                        kind = "oscillator" if hit == (0, 0, 0) else "glider"
                        break
                tally[(shape, kind)] += 1
    check("S3 RZ vacuum seeds (2x1x1, 3x1x1; {-1,0,1}): no glider", all(k[1] != "glider" for k in tally),
          str(dict(tally)))


def search_S4():
    """line sector, zero line background: windows of width 10, values kept in {-1,0,1}; horizon 60."""
    L, w = 48, 10
    ev = [i for i in range(w) if i % 2 == 0]
    od = [i for i in range(w) if i % 2 == 1]
    allv = np.array(list(itertools.product((-1, 0, 1), repeat=w)), np.int64)
    N = len(allv)
    yp = np.zeros((N, L), np.int64)
    y = yp.copy()
    yp[:, od] = allv[:, :len(od)]
    y[:, ev] = allv[:, len(od):]
    p0, c0 = yp.copy(), y.copy()
    alive = np.ones(N, bool)
    found = np.zeros(N, bool)
    for t in range(1, 61):
        yp, y = y, np.floor_divide(np.roll(y, 1, 1) + np.roll(y, -1, 1) + 1, 3) - yp
        alive &= (np.abs(y) <= 1).all(1)
        for d in range(-12, 13):
            if d == 0 or (t + d) % 2:
                continue
            found |= alive & (np.roll(p0, d, 1) == yp).all(1) & (np.roll(c0, d, 1) == y).all(1)
    nontriv = (allv != 0).any(1)
    check("S4 line sector on the zero line: no moving localized pattern (window 10)",
          not (found & nontriv).any(), f"states={N}, staying ternary={int(alive.sum())}")


def main():
    checks_A()
    checks_C()
    checks_D()
    checks_E()
    bb = checks_F()
    if "--search" in sys.argv:
        search_S1()
        search_S2()
        search_S3()
        search_S4()
    # F2: every classifier input is a value computed above (additivity tests A2, A3, F1; block checks
    # E1-E6, F1; S1, S2 with --search). Blocks never tested (fan-out in Q) count as not verified.
    cl_lin = classify(COMPUTED["LIN_additive"], {})
    cl_bbm = classify(COMPUTED["BBM_additive"], bb)
    cl_q = classify(COMPUTED["Q_additive"], COMPUTED["Q_blocks"])
    check("F2 classifier on computed inputs: linear -> not universal; BBM -> universal; rounded Q -> undecided",
          cl_lin.startswith("not universal") and cl_bbm.startswith("universal") and cl_q.startswith("undecided"),
          f"LIN: {cl_lin} | BBM: {cl_bbm} | Q: {cl_q} | Q blocks: {COMPUTED['Q_blocks']}")
    bad = [n for n, ok in RESULTS if not ok]
    print(f"{len(RESULTS) - len(bad)}/{len(RESULTS)} checks pass")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
