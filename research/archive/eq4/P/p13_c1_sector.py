"""EQ4-P probe p13 -- the c = 1 sector problem has a solution: the cone K_tw, exact.  Research only.

Usage:  python3 -I -B p13_c1_sector.py <base>/verification/lean-mathlib/OIBridge
Imports only the own library eq4_lib.py.

c = 1 sector (NOTES N3.8).  For c = 1, K3 = K3* (Euclidean), B_tw = cone{PT_j(sigma_ij) (x) rho_k} <= K3, K3 is LU-
invariant and S3-symmetric.  Every element of the GHZ stabilizer group is a real local Pauli product, so the twirl
commutes with every PT_j; PT_j maps the GHZ-diagonal sector GD into itself.  Hence twirl(K3) = K3 n GD is a G-invariant
Euclidean self-dual cone containing S_tw = twirl(B_tw).  Written: for a cut ij|k, twirl(Sep_{ij|k}) is the cone of
pair sums inside each of the two blocks {fibres b, b + d_k} (d_k the fibre shift of X on token k) -- the GHZ states
of a block are the Bell states of a logical qubit of (i, j) with token k, and a state separable across ij|k has Bell
fidelities at most 1/2 inside each block; the pair sums are attained by product states and by
Phi+ (x) |+><+| + Phi- (x) |-><-| (p11 S1).  So S_tw = cone(G-orbits of PT_j(e_0 + e_1) = e_0 + e_1 and of
t = PT_2(e_0 + e_2) = (1,1,1,1,1,-1,1,-1)).  Candidate (exploration x14):
    K_tw = cone( p_b = e_{+b} + e_{-b},  t-orbit (24),  k_j = 1 - 2 e_j + 2 e_{j'} (j' the partner of j) ),
36 generators.  In (P, C) coordinates K_tw* = {P >= 0, |C_c| + |C_d| <= P_a + P_b for every split {a,b}|{c,d} of the
four fibres, |C_b| <= (sum P)/2}.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `P13-C1-SECTOR-EXACT` iff all:
  K  transcription control.
  B  (B1) PT_j maps every GHZ projector into GD (j = 1, 2, 3) and the twirl commutes with PT_j on all 64 units;
     (B2) twirl(PT_2(Phi+_12) (x) |+><+| + PT_2(Phi-_12) (x) |-><-|) has eigenvalue vector t/2, and twirl of
     |000><000| is (e_0 + e_1)/2; (B3) cross-check of the written block argument: for 30 random exact B_tw generators
     PT_j(sigma_ij) (x) rho_k (random PSD sigma, rho, random cut and j) the twirl lies in cone(S_tw) (it pairs
     nonnegatively with every extreme ray of S_tw*, computed by exact double description).
  T  (T1) the 36 generators of K_tw are G-invariant as a set and pairwise >= 0; (T2) exact double description of
     K_tw* in two constraint orders returns the same rays, each in K_tw* with a tight set of rank 7, and the ray set
     equals the generator set; (T3) independent cross-check: 300 random exact points of K_tw* (rejection-sampled
     against all 36 constraints) are each written as a nonnegative combination of the generators by an exact phase-I
     simplex (Bland's rule), verified by exact reconstruction; (T4) S_tw <= K_tw, W3 = (-1, 1^7) in cone(S_tw),
     GHZ+ = e_0 not in K_tw, F = (-2, 2, 1^6) (p10's F) not in K_tw (it pairs negatively with a generator).
"""
import random
import sys
from fractions import Fraction as Fr
from itertools import permutations, product
from math import gcd

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("p13_c1_sector")
rng = random.Random(20261009 + 13)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])
X3 = (0, 1, 2)


def idx(x, y, z):
    return 4 * x + 2 * y + z


PJ = []
for b in range(4):
    b1, b2 = b >> 1, b & 1
    for t in range(2):
        v = [0] * 8
        v[idx(0, b1, b2)] = 1
        v[idx(1, 1 - b1, 1 - b2)] = 1 if t == 0 else -1
        PJ.append(L.ket_op(v, X3).scale(Fr(1, 2)))


def coords(Xop):
    return [L.pair(Xop, P) for P in PJ]


def pin(Xop):
    out = L.Op(X3, {})
    for P in PJ:
        out = out + P.scale(L.pair(Xop, P))
    return out


def mm2(A, B):
    return [[sum((L.G.of(A[i][k]) * L.G.of(B[k][j]) for k in range(2)), L.ZERO) for j in range(2)] for i in range(2)]


def powm(M, e):
    return M if e else L.S0


Hgrp = []
for a in (0, 1):
    for bb in (0, 1):
        for c in (0, 1):
            Hgrp.append(L.tensor(L.op(mm2(powm(L.SX, a), powm(L.SZ, bb)), (0,)),
                                 L.op(mm2(mm2(powm(L.SX, a), powm(L.SZ, bb)), powm(L.SZ, c)), (1,)),
                                 L.op(mm2(powm(L.SX, a), powm(L.SZ, c)), (2,))))


def twirl(Xop):
    out = L.Op(X3, {})
    for h in Hgrp:
        out = out + L.ad(h, Xop)
    return out.scale(Fr(1, 8))


def prim(v):
    den = 1
    for x in v:
        den = den * Fr(x).denominator // gcd(den, Fr(x).denominator)
    w = [int(Fr(x) * den) for x in v]
    g = 0
    for x in w:
        g = gcd(g, abs(x))
    return tuple(x // g for x in w) if g else tuple(w)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


GR = []
for perm in permutations(range(4)):
    for eps in product((0, 1), repeat=4):
        if sum(eps) % 2 == 0:
            GR.append(tuple(2 * perm[b] + (t ^ eps[b]) for b in range(4) for t in range(2)))


def act(g, v):
    w = [0] * 8
    for i in range(8):
        w[g[i]] = v[i]
    return tuple(w)


def orbit(v):
    return sorted(set(act(g, v) for g in GR))


def rank(rows):
    if not rows:
        return 0
    M = [[Fr(x) for x in r] for r in rows]
    rk = 0
    ncol = len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]
                M[i] = [M[i][j] - f * M[rk][j] for j in range(ncol)]
        rk += 1
    return rk


def inverse_cols(B):
    n = len(B)
    M = [[Fr(x) for x in B[i]] + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[c][j] for j in range(2 * n)]
    inv = [row[n:] for row in M]
    return [prim([inv[i][j] for i in range(n)]) for j in range(n)]


def extreme_rays(A, n=8):
    rows = [tuple(a) for a in A]
    basis = []
    for i, a in enumerate(rows):
        if rank([rows[k] for k in basis] + [a]) > len(basis):
            basis.append(i)
        if len(basis) == n:
            break
    assert len(basis) == n
    rays = list(inverse_cols([rows[k] for k in basis]))
    Z = []
    for j in range(n):
        mask = 0
        for k in range(n):
            if k != j:
                mask |= 1 << basis[k]
        Z.append(mask)
    bset = set(basis)
    for i, a in enumerate(rows):
        if i in bset:
            continue
        vals = [dot(a, r) for r in rays]
        pos = [k for k in range(len(rays)) if vals[k] > 0]
        neg = [k for k in range(len(rays)) if vals[k] < 0]
        zer = [k for k in range(len(rays)) if vals[k] == 0]
        nr = [rays[k] for k in pos] + [rays[k] for k in zer]
        nz = [Z[k] for k in pos] + [Z[k] | (1 << i) for k in zer]
        for p in pos:
            for q in neg:
                common = Z[p] & Z[q]
                if common.bit_count() < n - 2:
                    continue
                if all(not (r != p and r != q and (Z[r] & common) == common) for r in range(len(rays))):
                    nr.append(prim(tuple(vals[p] * rays[q][t] - vals[q] * rays[p][t] for t in range(n))))
                    nz.append(common | (1 << i))
        rays, Z = nr, nz
    return sorted(set(rays))


# ------------------------------------------------------------------------------------------------ B
ok_b1 = True
for j in X3:
    for P in PJ:
        Y = L.ptranspose(P, [j])
        ok_b1 &= pin(Y) == Y
    for _, U in L.units(X3):
        ok_b1 &= twirl(L.ptranspose(U, [j])) == L.ptranspose(twirl(U), [j])
rep.check("B1 PT_j maps GD into GD and commutes with the twirl (j = 1, 2, 3; all 64 units)", ok_b1)
phim = L.ket_op([1, 0, 0, -1], (0, 1)).scale(Fr(1, 2))
plus = L.ket_op([1, 1], (2,)).scale(Fr(1, 2))
minus = L.ket_op([1, -1], (2,)).scale(Fr(1, 2))
btw = L.tensor(L.ptranspose(L.phi_plus(0, 1), [1]), plus) + L.tensor(L.ptranspose(phim, [1]), minus)
tvec = (1, 1, 1, 1, 1, -1, 1, -1)
ok_b2 = coords(twirl(btw)) == [L.G(Fr(x, 2)) for x in tvec]
ok_b2 &= coords(twirl(L.ket_op(L.basis_vec([0, 0, 0]), X3))) == [L.G(Fr(1, 2)), L.G(Fr(1, 2))] + [L.ZERO] * 6
rep.check("B2 twirl(PT_2(Phi+) (x) |+><+| + PT_2(Phi-) (x) |-><-|) = t/2, t = %s; twirl(|000><000|) = (e_0 + e_1)/2"
          % (tvec,), ok_b2)
STW = sorted(set(orbit((1, 1, 0, 0, 0, 0, 0, 0)) + orbit(tvec)))
extSTW = extreme_rays(STW)
ok_b3 = True
for _ in range(30):
    i, j, k = rng.choice(list(permutations(X3)))
    sig = L.rand_psd(rng, (i, j), rank=rng.choice((1, 2)))
    rho = L.rand_psd(rng, (k,), rank=1)
    gen = L.reorder(L.tensor(L.ptranspose(sig, [j]), rho), X3)
    lam = [v.re for v in coords(twirl(gen))]
    ok_b3 &= all(v.im == 0 for v in coords(twirl(gen))) and all(dot(lam, z) >= 0 for z in extSTW)
rep.check("B3 30 random B_tw generators PT_j(sigma_ij) (x) rho_k: twirls lie in cone(S_tw) (pair >= 0 with all %d "
          "extreme rays of S_tw*)" % len(extSTW), ok_b3)

# ------------------------------------------------------------------------------------------------ T
KAP = sorted(set(orbit((-1, 3, 1, 1, 1, 1, 1, 1))))
GEN = sorted(set(STW + KAP))
gset = set(GEN)
inv_ok = all(act(g, v) in gset for v in GEN for g in GR)
sp_ok = all(dot(a, b) >= 0 for a in GEN for b in GEN)
rep.check("T1 %d generators (4 p_b, %d t, %d k_j); G-invariant set %s; pairwise >= 0 %s"
          % (len(GEN), len(STW) - 4, len(KAP), inv_ok, sp_ok), len(GEN) == 36 and inv_ok and sp_ok)
ext1 = extreme_rays(GEN)
o2 = list(GEN)
rng.shuffle(o2)
ext2 = extreme_rays(o2)
in_dual = all(all(dot(z, w) >= 0 for w in GEN) for z in ext1)
extreme = all(rank([w for w in GEN if dot(z, w) == 0]) == 7 for z in ext1)
rep.check("T2 exact double description: %d rays, two orders agree %s, all in K_tw* %s, all extreme %s, ray set = "
          "generator set %s" % (len(ext1), ext1 == ext2, in_dual, extreme, set(ext1) == gset),
          ext1 == ext2 and in_dual and extreme and set(ext1) == gset)


def lp_member(cols, x):
    """exact phase-I simplex (Bland): nonnegative c with sum c_j cols_j = x, or None."""
    m, n = len(x), len(cols)
    T = []
    for i in range(m):
        s = -1 if x[i] < 0 else 1
        T.append([Fr(s * cols[j][i]) for j in range(n)] + [Fr(int(i == k)) for k in range(m)] + [Fr(s * x[i])])
    basis = [n + i for i in range(m)]
    obj = [-sum(T[i][j] for i in range(m)) for j in range(n)] + [Fr(0)] * m + [-sum(T[i][-1] for i in range(m))]
    for _ in range(10000):
        enter = next((j for j in range(n + m) if obj[j] < 0), None)
        if enter is None:
            break
        rows = [i for i in range(m) if T[i][enter] > 0]
        if not rows:
            return None
        r = min(rows, key=lambda i: (T[i][-1] / T[i][enter], basis[i]))
        pv = T[r][enter]
        T[r] = [v / pv for v in T[r]]
        for i in range(m):
            if i != r and T[i][enter] != 0:
                f = T[i][enter]
                T[i] = [T[i][k] - f * T[r][k] for k in range(n + m + 1)]
        f = obj[enter]
        obj = [obj[k] - f * T[r][k] for k in range(n + m + 1)]
        basis[r] = enter
    if obj[-1] != 0:
        return None
    c = [Fr(0)] * n
    for i, bv in enumerate(basis):
        if bv < n:
            c[bv] = T[i][-1]
    return c


def in_star(x):
    return all(dot(x, w) >= 0 for w in GEN)


ok_t3 = True
nneg = 0
for _ in range(300):
    while True:
        P = [Fr(rng.randint(0, 12), rng.choice((1, 2, 3))) for _ in range(4)]
        C = [Fr(rng.randint(-12, 12), rng.choice((1, 2, 3))) for _ in range(4)]
        lam = []
        for b in range(4):
            lam += [(P[b] + C[b]) / 2, (P[b] - C[b]) / 2]
        x = prim(lam)
        if any(x) and in_star(x):
            break
    nneg += int(min(x) < 0)
    c = lp_member(GEN, x)
    if c is None or any(v < 0 for v in c) or [sum(c[j] * GEN[j][i] for j in range(len(GEN))) for i in range(8)] != list(x):
        ok_t3 = False
        break
rep.check("T3 independent cross-check: 300 random exact points of K_tw* (%d with a negative entry) are nonnegative "
          "combinations of the generators (exact phase-I simplex, reconstruction verified)" % nneg, ok_t3 and nneg >= 100)
W3v = (-1, 1, 1, 1, 1, 1, 1, 1)
Fv = (-2, 2, 1, 1, 1, 1, 1, 1)
e0 = (1, 0, 0, 0, 0, 0, 0, 0)
w3_in = all(dot(W3v, z) >= 0 for z in extSTW)
e0_out = any(dot(e0, w) < 0 for w in GEN)
F_out = any(dot(Fv, w) < 0 for w in GEN)
rep.check("T4 S_tw <= K_tw (generators) %s; W3 in cone(S_tw) %s; GHZ+ = e_0 not in K_tw %s; F not in K_tw %s"
          % (set(STW) <= gset, w3_in, e0_out, F_out), set(STW) <= gset and w3_in and e0_out and F_out)

rep.verdict("P13-C1-SECTOR-EXACT")
