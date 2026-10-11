#!/usr/bin/env python3
"""indep_checkC4.py -- the coordinator's independent check of the research/countermodels round-4 claims (C17-C19, C21).

Written 2026-10-11 (round-4 audit) before run 1.  Standalone: reads no thread file (the one external input is the
stage-6 reassessment table on the archive branch, an authorized read-only source, for X8); the thread's claimed values
are typed in below as the targets.  Exact arithmetic only (Fractions and Gaussian rationals Q(i)); no floating point;
no third-party import.  Group elements are 4 x 4 matrices with entries in Q(i), kept up to a scalar (canonical
representative: divided by the first nonzero entry); Ad(U) is computed as U M U^dag / (U U^dag)_00, which is
scalar-free; overlaps and |det Psi|^2 are normalized by the vector norms, so every quantity is scalar-free.

What is NOT checked here (stated once): the general written proofs of Lemmas C18-1, C18-2, C18-3 and of Theorem C19-1
(only their identities, signs and instances), the Lean content of CmSprime (read by the coordinator; its build is
read from the job log), Theorem S' itself (the self-duality of any surgery), H1 beyond the Schmidt-bound criterion,
the kappa cone (its gate flow is not re-derived), the FCC contraction, and the K-independent rows of Table A2.

DECISION RULE (fixed before run 1).  VERDICT INDEP-C4-FIXED iff X1-X8 all print PASS and CC1-CC5 each print
'COUNTER CCk fails as stated'; otherwise INDEP-C4-OPEN.

 X1  C19.2 the Clifford chain, as projective unitary groups generated in Q(i): |<CNOT, 1(x)S, 1(x)U_J>| = 384,
     |<G384, X(x)1>| = 768, |C2 = <CNOT, U_J(x)1, 1(x)U_J, S(x)1, 1(x)S>| = 11520; S(x)1 lies in G384; <G384, U_J(x)1> =
     <G768, U_J(x)1> = C2 (as sets); G384 is exactly the stabilizer of Z(x)1 in C2 and G768 exactly the stabilizer of
     +-Z(x)1.
 X2  C19.3 h* = (10, 2-2i, -1-3i, 3-i) along the chain: 192 rays under G384; 384 rays under G768 (stabilizer 2),
     minimum normalized |det Psi|^2 = 85/2048, pairwise squared overlaps in [1/1024, 13/16] (no orthogonal pair), at
     c = 10001/10000 both H1 (c lambda_max <= 1, through |det|^2_min >= (1/c)(1-1/c)) and (CC) (c^2 s_min >= 4(c-1))
     hold; under C2 the orbit has 5760 rays and h* has exactly two orthogonal partner rays (dies).
 X3  C19.4/C15.2 h_C = (-480+7i, 357+870i, 939+834i, 448+486i) at C2: 11520 rays (trivial stabilizer), minimum
     normalized |det Psi|^2 = 198406621629/9790484550625 (no product), pairwise squared overlaps in
     [164178929/3916193820250, 1560203344561/1566477528100] (no orthogonal pair); at c = 100001/100000 H1 and (CC) hold.
 X4  C19.1 Theorem instances: for psi = |0>(x)a + |1>(x)b the block element with U_0 = [[conj a0, conj a1], [-a1, a0]]
     (U_1 likewise from b) has U U^dag = |a|^2 I and det U = |a|^2 (so U/|a| is in SU(2)), carries a to |a|^2 e_0, and
     g psi has a vanishing 2 x 2 determinant (a product), at psi = (3, 4i, 0, 5) and at phi_0 = (1, 2, 3i, -1+i); the
     carried defect I - c P_{g psi} pairs 1 - c < 0 with the product P_{g psi}.
 X5  C18.1 Lemma C18-1: the pairing identity (1 - c_l s) + lambda (4 - c* - c_l + c* c_l s') = c*(1 - s) +
     (c* - c_l)(s + lambda) + lambda c* c_l s' with lambda = (c* - 1)/(4 - 2c*) on an exact grid; on the instance
     h = (2,1,0,0), h' = (1,-2,0,0), c* = 51/50: <y, d_h> = 0 for y = P_h + lambda d_{h'}, h'^dag y h'/|h'|^2 =
     lambda(1 - c*) < 0, <y, d_l> >= 0 and equal to the identity's value on sample defects with c_l in {51/50, 101/100},
     and <d_l, d_h> >= 4 - c_l - c* > 0.
 X6  C18.3 Lemma C18-2 instances: the 2-plane of the Bell pair (|00>+|11>, |01>+|10>) and of (3|00>+|11>, |01>+3|10>)
     each contain an exact product vector p (det of its coefficient matrix 0) with p^dag d p < 0 for
     d = I - (3/2)P_u - (3/2)P_v.
 X7  C21 by operation, for K384 (c = 401/400, Z = G384 . h*) and KC (c = 100001/100000, Z_C = C2 . h_C): invariances by
     group membership -- 1(x)S, 1(x)(I - iX) (target R_z(pi/2), R_x(pi/2)), S(x)1 in G384; X(x)1 in G768 \ G384;
     U_J(x)1 and (I - iX)(x)1 in C2 \ G768; SWAP in C2 \ G768 -- and MOVED witnesses: for g in {1(x)diag(1,(3+4i)/5)
     [target R_z(t0)], X(x)1 [control R_x(pi)], U_J(x)1 [control J], (2I - iX)(x)1 [control R_x(t0)]} the ray w = g h*
     has squared overlap <= 1/c with every ray of Z, so P_w lies in K384 and pairs 1 - c < 0 with g(d*): g moves K384;
     for g in {1(x)diag(1,(3+4i)/5), (2I - iX)(x)1} the same with h_C and Z_C for KC.
 X8  C21 R0: the stage-6 reassessment's Table A2 (research/archive @ 4dc0321c, sha256 1ff62ad6...) has 199 rows:
     118 SATISFIES, 68 NOT REACHED, 13 FAILS.
 CC1 "G768 has order 384" -- must fail (768).
 CC2 "h* survives C2: no orthogonal partner in its C2-orbit" -- must fail (partners exist).
 CC3 "h_C has an orthogonal partner at C2" -- must fail (minimum overlap > 0).
 CC4 "with lambda' = (c* - 1)/(4 - c*) in place of lambda, <y', d_h> = 0" -- must fail.
 CC5 "the finite G384 carries phi_0 = (1, 2, 3i, -1+i) to a product" -- must fail (minimum |det Psi|^2 = 5/256 > 0).

Usage: python3 -I -B indep_checkC4.py
"""
import hashlib
import itertools
import os
import sys
from fractions import Fraction as Fr

ARCHIVE_TABLE = '/home/user/wt-research/archive/research/archive/pt/R6/REASSESSMENT.md'


class G:
    __slots__ = ('r', 'i')

    def __init__(self, r=0, i=0):
        self.r = Fr(r)
        self.i = Fr(i)

    @staticmethod
    def c(o):
        return o if isinstance(o, G) else G(o, 0)

    def __add__(s, o):
        o = G.c(o)
        return G(s.r + o.r, s.i + o.i)

    __radd__ = __add__

    def __sub__(s, o):
        o = G.c(o)
        return G(s.r - o.r, s.i - o.i)

    def __mul__(s, o):
        o = G.c(o)
        return G(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)

    __rmul__ = __mul__

    def __neg__(s):
        return G(-s.r, -s.i)

    def __truediv__(s, o):
        o = G.c(o)
        d = o.r * o.r + o.i * o.i
        return G((s.r * o.r + s.i * o.i) / d, (s.i * o.r - s.r * o.i) / d)

    def conj(s):
        return G(s.r, -s.i)

    def abs2(s):
        return s.r * s.r + s.i * s.i

    def __eq__(s, o):
        o = G.c(o)
        return s.r == o.r and s.i == o.i

    def __hash__(s):
        return hash((s.r, s.i))

    def iszero(s):
        return s.r == 0 and s.i == 0

    def __repr__(s):
        return f'({s.r}{"+" if s.i >= 0 else "-"}{abs(s.i)}i)'


I_ = G(0, 1)


def mat(rows):
    return [[G.c(x) for x in r] for r in rows]


def eye(n):
    return [[G(1 if i == j else 0) for j in range(n)] for i in range(n)]


def zeros(n, m=None):
    m = n if m is None else m
    return [[G() for _ in range(m)] for _ in range(n)]


def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        for l in range(k):
            a = Ai[l]
            if a.iszero():
                continue
            Bl = B[l]
            oi = out[i]
            for j in range(m):
                b = Bl[j]
                if not b.iszero():
                    oi[j] = oi[j] + a * b
    return out


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def kron(A, B):
    n, m = len(A), len(A[0])
    p, q = len(B), len(B[0])
    return [[A[i // p][j // q] * B[i % p][j % q] for j in range(m * q)] for i in range(n * p)]


def tr(A):
    s = G()
    for i in range(len(A)):
        s = s + A[i][i]
    return s


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def smul(c, A):
    c = G.c(c)
    return [[c * x for x in r] for r in A]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mv(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v)) if not v[j].iszero()), G()) for i in range(len(A))]


def diag(*xs):
    n = len(xs)
    return [[G.c(xs[i]) if i == j else G() for j in range(n)] for i in range(n)]


def inner(z, w):
    return sum((z[k].conj() * w[k] for k in range(len(z))), G())


def norm2(z):
    return inner(z, z).r


def proj(h):
    """P_h = h h^dag / |h|^2 (exact)."""
    n2 = norm2(h)
    return [[h[i] * h[j].conj() / n2 for j in range(len(h))] for i in range(len(h))]


def ad(U, M):
    """Ad(U) M for U a scalar multiple of a unitary: U M U^dag / (U U^dag)_00."""
    UU = mm(U, dag(U))
    return smul(G(1) / UU[0][0], mm(mm(U, M), dag(U)))


def overlap2(z, w):
    return inner(z, w).abs2() / (norm2(z) * norm2(w))


def det2_norm(z):
    """Normalized |det Psi|^2 of z = (z00, z01, z10, z11) as the 2 x 2 matrix Psi[c][t]."""
    d = z[0] * z[3] - z[1] * z[2]
    return d.abs2() / (norm2(z) ** 2)


def pair(A, B):
    """Re tr(AB) (the trace pairing of Hermitian matrices)."""
    return tr(mm(A, B)).r


def canon_key_mat(U):
    piv = next(x for row in U for x in row if not x.iszero())
    return tuple((y / piv).r for row in U for y in row) + tuple((y / piv).i for row in U for y in row)


def canon_vec(v):
    piv = next(x for x in v if not x.iszero())
    return [x / piv for x in v]


def key_vec(v):
    v = canon_vec(v)
    return tuple(x.r for x in v) + tuple(x.i for x in v)


def closure_group(gens, cap=20000):
    start = eye(len(gens[0]))
    seen = {canon_key_mat(start): start}
    frontier = [start]
    while frontier:
        nxt = []
        for U in frontier:
            for g in gens:
                V = mm(g, U)
                k = canon_key_mat(V)
                if k not in seen:
                    seen[k] = V
                    nxt.append(V)
                    if len(seen) > cap:
                        return None
        frontier = nxt
    return seen


# ------------------------------------------------------------------------------------------------------- constants
I2 = eye(2)
X = mat([[0, 1], [1, 0]])
Y = mat([[0, G(0, -1)], [G(0, 1), 0]])
Z = mat([[1, 0], [0, -1]])
S = diag(1, I_)
UJ = mat([[G(Fr(1, 2), Fr(-1, 2)), G(Fr(-1, 2), Fr(-1, 2))],
          [G(Fr(1, 2), Fr(-1, 2)), G(Fr(1, 2), Fr(1, 2))]])  # (I - i(X+Y+Z))/2
CNOT = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # |c t> -> |c, t xor c>
SWAP = mat([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
P35 = diag(1, G(Fr(3, 5), Fr(4, 5)))          # R_z(t0) up to a phase, cos t0 = 3/5
RX90 = msub(I2, smul(I_, X))                   # I - iX  ~ R_x(pi/2) up to a scalar
RXT0 = msub(smul(2, I2), smul(I_, X))          # 2I - iX ~ R_x(t0) up to a scalar (cos t0 = 3/5)
H_STAR = [G(10), G(2, -2), G(-1, -3), G(3, -1)]
H_C = [G(-480, 7), G(357, 870), G(939, 834), G(448, 486)]
PHI0 = [G(1), G(2), G(0, 3), G(-1, 1)]

results = {}
counters = {}


def report(name, ok, detail):
    results[name] = bool(ok)
    print(f'{"PASS" if ok else "FAIL"} {name}: {detail}')


def counter(name, stated_holds, detail):
    counters[name] = not stated_holds
    print(f'COUNTER {name} {"fails as stated" if not stated_holds else "DOES NOT FAIL (defect)"}: {detail}')


def orbit_data(group, h):
    """Rays of the orbit of h under the group (dict), with the per-element overlaps and determinants."""
    rays = {}
    ov_nontrivial = []
    zero_partners = 0
    kh = key_vec(h)
    for U in group.values():
        w = mv(U, h)
        k = key_vec(w)
        if k not in rays:
            rays[k] = canon_vec(w)
        if k != kh:
            s = overlap2(h, w)
            ov_nontrivial.append(s)
            if s == 0:
                zero_partners += 1
    dets = [det2_norm(z) for z in rays.values()]
    return rays, ov_nontrivial, zero_partners, dets


# =============================================================================================================== X1
def X1():
    ok = True
    notes = []
    gens384 = [CNOT, kron(I2, S), kron(I2, UJ)]
    gens768 = gens384 + [kron(X, I2)]
    gensC2 = [CNOT, kron(UJ, I2), kron(I2, UJ), kron(S, I2), kron(I2, S)]
    G384 = closure_group(gens384)
    G768 = closure_group(gens768)
    C2 = closure_group(gensC2)
    n384 = None if G384 is None else len(G384)
    n768 = None if G768 is None else len(G768)
    nC2 = None if C2 is None else len(C2)
    ok &= n384 == 384 and n768 == 768 and nC2 == 11520
    notes.append(f'orders: G384 {n384}, G768 {n768}, C2 {nC2} (targets 384, 768, 11520)')
    if G384 and G768 and C2:
        sIn = canon_key_mat(kron(S, I2)) in G384
        A = closure_group(gens384 + [kron(UJ, I2)])
        B = closure_group(gens768 + [kron(UJ, I2)])
        eqA = A is not None and set(A.keys()) == set(C2.keys())
        eqB = B is not None and set(B.keys()) == set(C2.keys())
        ZI = kron(Z, I2)
        stab = {k for k, U in C2.items() if meq(ad(U, ZI), ZI)}
        stabpm = {k for k, U in C2.items() if meq(ad(U, ZI), ZI) or meq(ad(U, ZI), smul(-1, ZI))}
        s1 = stab == set(G384.keys())
        s2 = stabpm == set(G768.keys())
        sub = set(G384.keys()) <= set(G768.keys()) <= set(C2.keys())
        ok &= sIn and eqA and eqB and s1 and s2 and sub
        notes.append(f'S(x)1 in G384: {sIn}; <G384, U_J(x)1> = C2: {eqA}; <G768, U_J(x)1> = C2: {eqB}; '
                     f'G384 = Stab_C2(Z(x)1): {s1} ({len(stab)}); G768 = Stab_C2(+-Z(x)1): {s2} ({len(stabpm)}); chain nested: {sub}')
    report('X1', ok, '; '.join(notes))
    return G384, G768, C2


# =============================================================================================================== X2
def X2(G384, G768, C2):
    ok = True
    notes = []
    rays384, ov384, zp384, dets384 = orbit_data(G384, H_STAR)
    ok &= len(rays384) == 192
    notes.append(f'G384 orbit of h*: {len(rays384)} rays (target 192)')
    rays768, ov768, zp768, dets768 = orbit_data(G768, H_STAR)
    n = len(rays768)
    stab = Fr(len(G768), n) if n else None
    mind = min(dets768)
    smin, smax = min(ov768), max(ov768)
    c = Fr(10001, 10000)
    cc = c * c * smin >= 4 * (c - 1)
    h1 = mind >= (1 / c) * (1 - 1 / c)
    ok &= n == 384 and stab == 2 and mind == Fr(85, 2048) and smin == Fr(1, 1024) and smax == Fr(13, 16) and zp768 == 0 and cc and h1
    notes.append(f'G768 orbit: {n} rays (target 384), stabilizer {stab}, min |det|^2 {mind} (target 85/2048), overlaps in [{smin}, {smax}] '
                 f'(target [1/1024, 13/16]), orthogonal partners {zp768}; at c = 10001/10000 (CC) {cc}, H1 {h1}')
    raysC2, ovC2, zpC2, detsC2 = orbit_data(C2, H_STAR)
    nC = len(raysC2)
    stabC = Fr(len(C2), nC) if nC else None
    partner_rays = Fr(zpC2, stabC) if stabC else None
    ok &= nC == 5760 and partner_rays == 2
    notes.append(f'C2 orbit of h*: {nC} rays (target 5760), stabilizer {stabC}, zero-overlap group elements {zpC2} = {partner_rays} partner rays (target 2): dies')
    report('X2', ok, '; '.join(notes))
    return rays384, zpC2


# =============================================================================================================== X3
def X3(C2):
    ok = True
    notes = []
    rays, ov, zp, dets = orbit_data(C2, H_C)
    n = len(rays)
    mind = min(dets)
    smin, smax = min(ov), max(ov)
    c = Fr(100001, 100000)
    cc = c * c * smin >= 4 * (c - 1)
    h1 = mind >= (1 / c) * (1 - 1 / c)
    ok &= (n == 11520 and mind == Fr(198406621629, 9790484550625) and smin == Fr(164178929, 3916193820250)
           and smax == Fr(1560203344561, 1566477528100) and zp == 0 and smin > 0 and cc and h1)
    notes.append(f'C2 orbit of h_C: {n} rays (target 11520, trivial stabilizer), min |det|^2 {mind}, overlaps in [{smin}, {smax}], '
                 f'orthogonal partners {zp}; at c = 100001/100000 (CC) {cc} (c^2 s_min = {c * c * smin} vs 4(c-1) = {4 * (c - 1)}), H1 {h1}')
    report('X3', ok, '; '.join(notes))
    return rays, smin


# =============================================================================================================== X4
def block_element(a, b):
    """P0 (x) U0 + P1 (x) U1 with U0 = [[conj a0, conj a1], [-a1, a0]] (unnormalized by |a|), U1 likewise from b
    (the identity block when the vector is zero)."""
    def U_of(v):
        if all(x.iszero() for x in v):
            return eye(2)
        return mat([[v[0].conj(), v[1].conj()], [-v[1], v[0]]])
    U0, U1 = U_of(a), U_of(b)
    g = zeros(4)
    for i in range(2):
        for j in range(2):
            g[i][j] = U0[i][j]
            g[2 + i][2 + j] = U1[i][j]
    return g, U0, U1


def X4():
    ok = True
    notes = []
    for name, psi in (('psi = (3, 4i, 0, 5)', [G(3), G(0, 4), G(0), G(5)]), ('phi_0 = (1, 2, 3i, -1+i)', PHI0)):
        a, b = psi[:2], psi[2:]
        g, U0, U1 = block_element(a, b)
        good = True
        for U, v in ((U0, a), (U1, b)):
            n2 = norm2(v)
            if n2 == 0:
                continue
            UU = mm(U, dag(U))
            detU = U[0][0] * U[1][1] - U[0][1] * U[1][0]
            Uv = mv(U, v)
            good &= meq(UU, smul(n2, I2)) and detU == G(n2) and Uv[0] == G(n2) and Uv[1].iszero()
        gpsi = mv(g, psi)
        d = gpsi[0] * gpsi[3] - gpsi[1] * gpsi[2]
        prod = d.iszero()
        c = Fr(3, 2)
        Pg = proj(gpsi)
        dd = msub(eye(4), smul(c, Pg))
        pr = pair(dd, Pg)
        good &= prod and pr == 1 - c and pr < 0
        ok &= good
        notes.append(f'{name}: blocks scalar-unitary with det |a|^2, |b|^2, carrying a, b to multiples of e_0: {good}; g psi = {gpsi}, det = {d} (product {prod}); the carried defect pairs {pr} with P_(g psi)')
    report('X4', ok, '; '.join(notes))


# =============================================================================================================== X5
def X5():
    ok = True
    notes = []
    ident = True
    for cs in (Fr(11, 10), Fr(3, 2), Fr(19, 10), Fr(51, 50)):
        lam = (cs - 1) / (4 - 2 * cs)
        for cl in (cs, (1 + cs) / 2, 1 + (cs - 1) / 3):
            for s in (Fr(0), Fr(1, 4), Fr(1, 2), Fr(1)):
                for sp in (Fr(0), Fr(1, 4), Fr(1, 2), Fr(1)):
                    lhs = (1 - cl * s) + lam * (4 - cs - cl + cs * cl * sp)
                    rhs = cs * (1 - s) + (cs - cl) * (s + lam) + lam * cs * cl * sp
                    ident &= lhs == rhs
    ok &= ident
    notes.append(f'pairing identity on the grid: {ident}')
    h = [G(2), G(1), G(0), G(0)]
    hp = [G(1), G(-2), G(0), G(0)]
    cs = Fr(51, 50)
    lam = (cs - 1) / (4 - 2 * cs)
    Ph, Php = proj(h), proj(hp)
    dh = msub(eye(4), smul(cs, Ph))
    dhp = msub(eye(4), smul(cs, Php))
    y = madd(Ph, smul(lam, dhp))
    perp = inner(h, hp).iszero()
    ydh = pair(y, dh)
    val = inner(hp, mv(y, hp)).r / norm2(hp)
    ok &= perp and ydh == 0 and val == lam * (1 - cs) and val < 0
    notes.append(f'instance: h perp h\': {perp}; <y, d_h> = {ydh}; h\'^dag y h\'/|h\'|^2 = {val} = lambda(1 - c*) < 0: {val == lam * (1 - cs) and val < 0}')
    samples = [[G(1), G(0, 1), G(2), G(1, 1)], [G(3), G(1), G(0, -1), G(2)], [G(1), G(1), G(1), G(1)], [G(0), G(1), G(0, 2), G(-1)],
               [G(2), G(-1), G(0, 1), G(0, -1)], [G(1), G(0), G(0), G(0)]]
    allpos = True
    allid = True
    allpair = True
    for hl in samples:
        for cl in (Fr(51, 50), Fr(101, 100)):
            dl = msub(eye(4), smul(cl, proj(hl)))
            v = pair(y, dl)
            s = overlap2(h, hl)
            sp = overlap2(hp, hl)
            allpos &= v >= 0
            allid &= v == cs * (1 - s) + (cs - cl) * (s + lam) + lam * cs * cl * sp
            allpair &= pair(dl, dh) >= 4 - cl - cs > 0
    ok &= allpos and allid and allpair
    notes.append(f'{2 * len(samples)} sample defects: <y, d_l> >= 0 {allpos}, equal to the identity {allid}, <d_l, d_h> >= 4 - c_l - c* > 0 {allpair}')
    report('X5', ok, '; '.join(notes))
    return h, hp, cs, Ph, dhp, dh


# =============================================================================================================== X6
def X6():
    ok = True
    notes = []
    cases = [('Bell pair', [G(1), G(0), G(0), G(1)], [G(0), G(1), G(1), G(0)], [G(1), G(1), G(1), G(1)]),
             ('(3|00>+|11>, |01>+3|10>)', [G(3), G(0), G(0), G(1)], [G(0), G(1), G(3), G(0)], [G(3), G(1), G(3), G(1)])]
    for name, u, v, p in cases:
        d = msub(msub(eye(4), smul(Fr(3, 2), proj(u))), smul(Fr(3, 2), proj(v)))
        inplane = True  # p = u + v
        inplane &= all(p[k] == u[k] + v[k] for k in range(4))
        prod = (p[0] * p[3] - p[1] * p[2]).iszero()
        val = inner(p, mv(d, p)).r / norm2(p)
        good = inplane and prod and val < 0
        ok &= good
        notes.append(f'{name}: p = u + v is a product ({prod}), p^dag d p/|p|^2 = {val} < 0: {good}')
    report('X6', ok, '; '.join(notes))


# =============================================================================================================== X7
def X7(G384, G768, C2, rays384, raysC):
    ok = True
    notes = []
    k384, k768, kC2 = set(G384.keys()), set(G768.keys()), set(C2.keys())
    mem = {
        '1(x)S in G384': canon_key_mat(kron(I2, S)) in k384,
        '1(x)(I-iX) in G384': canon_key_mat(kron(I2, RX90)) in k384,
        'S(x)1 in G384': canon_key_mat(kron(S, I2)) in k384,
        'X(x)1 not in G384': canon_key_mat(kron(X, I2)) not in k384,
        'X(x)1 in G768': canon_key_mat(kron(X, I2)) in k768,
        'U_J(x)1 not in G768': canon_key_mat(kron(UJ, I2)) not in k768,
        'U_J(x)1 in C2': canon_key_mat(kron(UJ, I2)) in kC2,
        '(I-iX)(x)1 not in G768': canon_key_mat(kron(RX90, I2)) not in k768,
        '(I-iX)(x)1 in C2': canon_key_mat(kron(RX90, I2)) in kC2,
        'SWAP in C2': canon_key_mat(SWAP) in kC2,
        'SWAP not in G768': canon_key_mat(SWAP) not in k768,
    }
    ok &= all(mem.values())
    notes.append('memberships: ' + ', '.join(f'{k} {v}' for k, v in mem.items()))
    c384 = Fr(401, 400)
    ops384 = [('target R_z(t0)', kron(I2, P35)), ('control R_x(pi)', kron(X, I2)), ('control J', kron(UJ, I2)),
              ('control R_x(t0)', kron(RXT0, I2))]
    Z384 = list(rays384.values())
    d_star = msub(eye(4), smul(c384, proj(H_STAR)))
    for name, g in ops384:
        w = mv(g, H_STAR)
        mx = max(overlap2(w, z) for z in Z384)
        inK = mx <= 1 / c384
        v = pair(ad(g, d_star), proj(w))
        moved = inK and v == 1 - c384 and v < 0
        ok &= moved
        notes.append(f'K384 {name}: max overlap of g h* with Z = {mx} <= 1/c: {inK}; <g(d*), P_w> = {v}; MOVED {moved}')
    cC = Fr(100001, 100000)
    ZC = list(raysC.values())
    dC = msub(eye(4), smul(cC, proj(H_C)))
    for name, g in [('target R_z(t0)', kron(I2, P35)), ('control R_x(t0)', kron(RXT0, I2))]:
        w = mv(g, H_C)
        mx = max(overlap2(w, z) for z in ZC)
        inK = mx <= 1 / cC
        v = pair(ad(g, dC), proj(w))
        moved = inK and v == 1 - cC and v < 0
        ok &= moved
        notes.append(f'KC {name}: max overlap of g h_C with Z_C = {mx} <= 1/c: {inK}; <g(d_C), P_w> = {v}; MOVED {moved}')
    report('X7', ok, '; '.join(notes))


# =============================================================================================================== X8
def X8():
    ok = True
    notes = []
    if not os.path.exists(ARCHIVE_TABLE):
        report('X8', False, f'archive table not found at {ARCHIVE_TABLE}')
        return
    data = open(ARCHIVE_TABLE, 'rb').read()
    sha = hashlib.sha256(data).hexdigest()
    lines = data.decode('utf-8', errors='replace').split('\n')
    start = next((i for i, ln in enumerate(lines) if ln.startswith('### Table A2')), None)
    counts = {'SATISFIES': 0, 'NOT REACHED': 0, 'FAILS': 0, 'other': 0}
    nrows = 0
    if start is not None:
        for ln in lines[start + 1:]:
            if ln.startswith('### '):
                break
            if ln.startswith('| I'):
                cells = [c.strip() for c in ln.strip().strip('|').split('|')]
                if len(cells) < 4:
                    continue
                nrows += 1
                v = cells[3]
                if v.startswith('SATISFIES'):
                    counts['SATISFIES'] += 1
                elif v.startswith('NOT REACHED'):
                    counts['NOT REACHED'] += 1
                elif v.startswith('FAILS'):
                    counts['FAILS'] += 1
                else:
                    counts['other'] += 1
    ok &= sha.startswith('1ff62ad6') and nrows == 199 and counts == {'SATISFIES': 118, 'NOT REACHED': 68, 'FAILS': 13, 'other': 0}
    notes.append(f'sha256 {sha[:8]}... (target 1ff62ad6...); Table A2 rows {nrows} (target 199): {counts} (target 118 / 68 / 13)')
    report('X8', ok, '; '.join(notes))


# ====================================================================================================== countercontrols
def countercontrols(G384, G768, zpC2, sminC, h, hp, cs, Ph, dhp, dh):
    counter('CC1', len(G768) == 384, f'|G768| = {len(G768)}')
    counter('CC2', zpC2 == 0, f'zero-overlap elements for h* under C2: {zpC2}')
    counter('CC3', sminC == 0, f'minimum squared overlap on the C2-orbit of h_C: {sminC}')
    lam2 = (cs - 1) / (4 - cs)
    y2 = madd(Ph, smul(lam2, dhp))
    v2 = pair(y2, dh)
    counter('CC4', v2 == 0, f'<y\', d_h> with lambda\' = (c*-1)/(4-c*): {v2}')
    rays, ov, zp, dets = orbit_data(G384, PHI0)
    mind = min(dets)
    counter('CC5', mind == 0, f'G384 orbit of phi_0: {len(rays)} rays, minimum normalized |det Psi|^2 = {mind} (target 5/256)')


def main():
    print('indep_checkC4.py -- independent exact check of research/countermodels round-4 claims (C17-C19, C21)')
    G384, G768, C2 = X1()
    if not (G384 and G768 and C2):
        print('group closure failed; remaining checks skipped')
        print('VERDICT INDEP-C4-OPEN')
        return 1
    rays384, zpC2 = X2(G384, G768, C2)
    raysC, sminC = X3(C2)
    X4()
    h, hp, cs, Ph, dhp, dh = X5()
    X6()
    X7(G384, G768, C2, rays384, raysC)
    X8()
    countercontrols(G384, G768, zpC2, sminC, h, hp, cs, Ph, dhp, dh)
    n_pass = sum(1 for v in results.values() if v)
    n_cc = sum(1 for v in counters.values() if v)
    print(f'checks: {len(results)}, passed: {n_pass}, failures: {len(results) - n_pass}; countercontrols failing as stated: {n_cc}/{len(counters)}')
    verdict = 'INDEP-C4-FIXED' if n_pass == len(results) == 8 and n_cc == len(counters) == 5 else 'INDEP-C4-OPEN'
    print(f'VERDICT {verdict}')
    return 0 if verdict == 'INDEP-C4-FIXED' else 1


if __name__ == '__main__':
    sys.exit(main())
