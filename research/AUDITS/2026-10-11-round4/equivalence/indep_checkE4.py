#!/usr/bin/env python3
"""indep_checkE4.py -- the coordinator's independent check of the research/equivalence round-4 claims (E15-E18).

Written 2026-10-11 (round-4 audit) before run 1.  Standalone: reads no thread file; the thread's claimed values are
typed in below as the targets.  Exact arithmetic only (Fractions and Gaussian rationals Q(i)); no floating point; no
third-party import.  Polynomial identities are checked by exact evaluation on grids large enough to determine the
polynomials (a bivariate polynomial of degree <= 3 in each variable on a 4 x 4 grid; a univariate polynomial of degree
<= 6 at seven points; a multilinear polynomial on {0,1}^k).

What is NOT checked here (stated once): the general written proofs of R-E16.1/R-E16.2 (only their trace identity and
its instances), the kernel-form clauses of Omega_h other than relC, the involution property, Entangling and the shape
facts (relT, the frame, positivity, SharpSeed, K-inf Act/V4 are not re-derived), the general self-duality of the hybrid
composite (instances only), the irrationality of theta_0/pi (Niven), Theorem S' of the countermodels thread, and the
kernel's definition of `cnot` (taken as Ad(CNOT) through the dictionary, the form the round-3 audit and the bridge's
BridgeDictionary D2 give it).

DECISION RULE (fixed before run 1).  VERDICT INDEP-E4-FIXED iff X1-X8 all print PASS and CC1-CC5 each print
'COUNTER CCk fails as stated'; otherwise INDEP-E4-OPEN.

 X1  E15 countercontrol (HO-24's cone, R-E15.2): the projective group <CNOT, 1 (x) diag(1,i), 1 (x) U_J> has order 384;
     the orbit Z of h = (10, 2-2i, -1-3i, 3-i) has 192 rays (BFS, and the same set under all 384 elements); the 18336
     pairwise squared overlaps lie in [25/2048, 13/16]; (CC) c^2 s >= 4(c-1) holds on every pair at c = 401/400; with
     R = 1 (x) diag(1, (3+4i)/5) the ray R h has squared overlap at most 1949/2048 < 400/401 with every ray of Z, and
     <Rh| R d R^dag |Rh> = -1/400 for d = I - c P_h (so P_{Rh} lies in PSD and in Z*, pairs negatively with R d R^dag,
     and R d R^dag is outside K* = (PSD cap Z*) + cone Z, d being in K*: K* is not invariant under R).
 X2  E16.1 trace count: for d = 1..7 and every non-identity diagonal sign involution N of R^d, with H = 1 (+) N,
     (d+1) tr H = (tr H)^2 holds exactly when tr N = -1 (d odd, N with (d-1)/2 eigenvalues +1); on built matrices
     (d <= 5) tr(H (x) 1) = (d+1) tr H and tr(H (x) H) = (tr H)^2; the instance (d, #+1 eigenvalues of H) list is
     {(1,1), (3,2), (5,3), (7,4)}; the derivation relC => G actC G^-1 = actC actT and relC itself hold exactly for
     G = Ad(CNOT) on W 3 with N = diag(1,-1,-1) (= Ad(X)) and with N = diag(-1,1,-1) (= Ad(Y)); relC fails for
     N = diag(-1,-1,1) (= Ad(Z)) although the count holds for it (the count is necessary, not sufficient).
 X3  E16.3 hybrid token Omega_h (two-sector qubit, chart (w, a, b) in R^7): the chart transport Phi; the gate
     G = Ad(CNOT on the qubit factors) is well defined on W 7, is an involution, satisfies relC on all 64 basis tables
     with N = 1 (+) nflip (+) nflip (nflip = diag(1,-1,-1)), tr H = 0 (d = 7 odd); G carries a product (sector 0, |+>)
     (x) (sector 0, |0>) to a non-product (table rank >= 2); the four states |s,q><s,q| lie in Omega_h and are
     perfectly distinguished by four effects; the effect t_1 (= P_1 (x) 1) is zero on two distinct states (K-inf Geom
     fails); the midpoint of |0,0><0,0| and |1,0><1,0| is a boundary point (a non-zero effect vanishes on it), so
     Omega_h is not strictly convex and not an ellipsoid; on an exact element of the composite K (sector-blockwise PSD)
     the gate and the drive rotation at cos t = 3/5 on one token preserve K, and Dict intertwines both with their
     unitaries on basis tables.
 X4  E17 finite stage: (a) every symmetric idempotent {0,1} matrix is diagonal, exhaustively for n = 2, 3, 4;
     (b) every {0,1} matrix V with (V^T V)^2 = V^T V has at most one 1 per column, exhaustively for n = 2, 3, 4;
     (c) for n = 2, 3 and every monomial unitary U = D P_sigma with phases in {1, i, -1, -i}: Ad(U) maps every matrix
     unit to a {0,1} matrix iff the phases are equal, and then Ad(U)(E_ab) = E_{sigma a, sigma b}; a non-monomial
     unitary in Q(i) ([[3,4],[-4,3]]/5) maps E_00 outside {0,1}.
 X5  E18 power cone PC = {(u,v,X): u,v >= 0, (sum X_i^2)^3 <= u^2 v^4}, B = uu'/3 + 2vv'/3 + X.X': the identities
     (a+2b)^3 - 27ab^2 = (a-b)^2 (a+8b), theta^6 - (6 theta - 5) = (theta-1)^2 (theta^4+2theta^3+3theta^2+4theta+5) and
     form_eq (R-E13.1's form in (T,S) equals B in (T+S, T-S)) hold; B >= 0 on every pair of an exact grid of PC points;
     the pair z = (1, 1/8, (1/4,0,0)), w = (1/8, 1, (-1/2,0,0)) is tight (B = 0); the converse witnesses pair
     negatively: u',v' > 0 at w = (1,1,(2,0,0)) and w = (2,1/2,(1,1,0)) (z = (v's, u's, -X'), s = theta S'/(u'v'),
     theta = (5+rho)/6, rho = u'^2 v'^4/S'^3, B = (theta-1) S'), u' = 0 at w = (0,1,(1,0,0)) and v' = 0 at
     w = (1,0,(1,0,0)) with the module's points; each z lies in PC exactly.
 X6  E15 section G intertwining (the module's statements on the 16 basis tables of W 3, exact in Q(i)):
     dict(actT(rotLin t) w) = (1 (x) P) dict(w) (1 (x) P)^dag with P = diag(1, cos t + i sin t) at cos t = 3/5 and at
     t = pi/2; dict(actT cycEquiv w) = (1 (x) U_J) dict(w) (1 (x) U_J)^dag with U_J = (I - i(X+Y+Z))/2 (cycMat as the
     module writes it, cycMat^dag = cycMatH); U_J is unitary.
 X7  E15 countercontrol, the remaining exact items of R-E15.2: the minimum over Z of the normalized |det Psi_z|^2 is
     85/2048 and is at least (1/c)(1 - 1/c) = 400/160801, so c lambda_max <= 1 and every defect admits every product
     of pure states (H1); d is not positive semidefinite (<h|d|h>/|h|^2 = -1/400); the table
     z* = E00/2 - (c/8) T_h has dictionary image d/8.
 X8  E16.4's Omega_4 witness: y = (5/6,0,0,5/6) lies in Omega_4 = {|x|^4 + s^4 <= 1} ((x.x)^2 + s^4 = 1250/1296) and
     (1,y).(1,-y) = -7/18 < 0 for the Euclidean form; the support of Omega_4 in e_0 and e_3 is 1; for the Euclidean
     4-ball the same pairing is nonnegative on the scaled points (Cauchy-Schwarz instance).
 CC1 "(CC) holds at c' = 301/300 on every pair" -- must fail (on the minimal-overlap pair).
 CC2 "R' h has squared overlap at most 1949/2048 with every ray of Z for R' = 1 (x) diag(1, i)" -- must fail (R' lies in
     the group, so R' h is a ray of Z: overlap 1).
 CC3 "the count (d+1) tr H = (tr H)^2 holds for the chart-4 tokens' NOT diag(-1,-1,1,1)" -- must fail (5 vs 1).
 CC4 "Ad(diag(1,i)) maps every matrix unit of M_2 to a {0,1} matrix" -- must fail (E_01 goes to -i E_01).
 CC5 "with the exponents swapped, PC' = {S^3 <= u^4 v^2}, B is nonnegative on pairs of PC'" -- must fail at
     z = (1, 27/64, (3/4,0,0)) and its X-negation (both in PC', B < 0).

Usage: python3 -I -B indep_checkE4.py

RUN HISTORY (appended after each run; the decision rule above is unchanged).
 run 1 (2026-10-11T05:46:34Z): 7/8, countercontrols 5/5; X2 FAILED on the harness's own expectation that relC holds for
   G = Ad(CNOT) with N = diag(-1,1,-1) (= Ad(Y)) as well as with Ad(X).  The exact computation is right and the
   expectation was a hand error: (Y (x) 1) CNOT (Y (x) 1) = CNOT (1 (x) X), while actT(Ad Y) o G = Ad((1 (x) Y) CNOT) =
   Ad(CNOT (Z (x) Y)); relC holds for Ad(X) only, among the three trace -1 diagonal involutions.  No thread claim is
   touched (the thread's C1 uses nflip, the kernel's NOT).  Expectation corrected to {Ad X: True, Ad Y: False,
   Ad Z: False}; run-1 outputs kept as indep_checkE4.run1.out/.err.
"""
import itertools
import sys
from fractions import Fraction as Fr

# ----------------------------------------------------------------------------------------------- Gaussian rationals
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

    def __rsub__(s, o):
        o = G.c(o)
        return G(o.r - s.r, o.i - s.i)

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
    return len(A) == len(B) and all(len(A[i]) == len(B[i]) and all(A[i][j] == B[i][j] for j in range(len(A[i])))
                                    for i in range(len(A)))


def mv(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v))), G()) for i in range(len(A))]


def diag(*xs):
    n = len(xs)
    return [[G.c(xs[i]) if i == j else G() for j in range(n)] for i in range(n)]


def inner(z, w):
    """<z|w> = sum conj(z_k) w_k."""
    return sum((z[k].conj() * w[k] for k in range(len(z))), G())


def norm2(z):
    return inner(z, z).r


def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    s = G()
    for j in range(n):
        if A[0][j].iszero():
            continue
        minor = [row[:j] + row[j + 1:] for row in A[1:]]
        term = A[0][j] * det(minor)
        s = s + term if j % 2 == 0 else s - term
    return s


def is_hermitian(A):
    return meq(A, dag(A))


def is_psd(A):
    """Hermitian A is PSD iff every principal minor is >= 0 (exact)."""
    n = len(A)
    if not is_hermitian(A):
        return False
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            d = det([[A[i][j] for j in S] for i in S])
            if d.i != 0 or d.r < 0:
                return False
    return True


# rational (real) matrices as lists of Fractions
def fr_mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[Fr(0)] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for l in range(k):
            a = Ai[l]
            if a == 0:
                continue
            Bl = B[l]
            oi = out[i]
            for j in range(m):
                if Bl[j] != 0:
                    oi[j] += a * Bl[j]
    return out


def fr_eye(n):
    return [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]


def fr_kron(A, B):
    n, m = len(A), len(A[0])
    p, q = len(B), len(B[0])
    return [[A[i // p][j // q] * B[i % p][j % q] for j in range(m * q)] for i in range(n * p)]


def fr_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def fr_tr(A):
    return sum(A[i][i] for i in range(len(A)))


def fr_inv(A):
    n = len(A)
    M = [row[:] + [Fr(1 if i == j else 0) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            raise ValueError('singular')
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [M[r][j] - f * M[c][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def fr_rank(A):
    M = [row[:] for row in A]
    n, m = len(M), len(M[0])
    rank, c = 0, 0
    for c in range(m):
        p = next((r for r in range(rank, n) if M[r][c] != 0), None)
        if p is None:
            continue
        M[rank], M[p] = M[p], M[rank]
        pv = M[rank][c]
        M[rank] = [x / pv for x in M[rank]]
        for r in range(n):
            if r != rank and M[r][c] != 0:
                f = M[r][c]
                M[r] = [M[r][j] - f * M[rank][j] for j in range(m)]
        rank += 1
    return rank


def fr_diag(*xs):
    n = len(xs)
    return [[Fr(xs[i]) if i == j else Fr(0) for j in range(n)] for i in range(n)]


def g_to_fr(A):
    """A Gaussian-rational matrix with zero imaginary parts, as a rational matrix (raises otherwise)."""
    for row in A:
        for x in row:
            if x.i != 0:
                raise ValueError('non-real entry')
    return [[x.r for x in row] for row in A]


def fr_to_g(A):
    return [[G(x) for x in row] for row in A]


# ------------------------------------------------------------------------------------------------------- Paulis
I2 = eye(2)
X = mat([[0, 1], [1, 0]])
Y = mat([[0, G(0, -1)], [G(0, 1), 0]])
Z = mat([[1, 0], [0, -1]])
SIG = [I2, X, Y, Z]
P0 = mat([[1, 0], [0, 0]])
P1 = mat([[0, 0], [0, 1]])


def pauli2(mu, nu):
    return kron(SIG[mu], SIG[nu])


def dict3(w):
    """The two-token dictionary: dict w = 1/4 sum w[mu][nu] sigma_mu (x) sigma_nu, control first."""
    out = zeros(4)
    for mu in range(4):
        for nu in range(4):
            if not G.c(w[mu][nu]).iszero():
                out = madd(out, smul(G.c(w[mu][nu]) * Fr(1, 4), pauli2(mu, nu)))
    return out


def coords3(H):
    """w[mu][nu] = tr(H sigma_mu (x) sigma_nu) -- the inverse of dict3 on Hermitian H (real entries)."""
    w = [[None] * 4 for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            t = tr(mm(H, pauli2(mu, nu)))
            if t.i != 0:
                raise ValueError('non-real coordinate')
            w[mu][nu] = t.r
    return w


def basis_table(mu, nu):
    return [[Fr(1 if (a, b) == (mu, nu) else 0) for b in range(4)] for a in range(4)]


def table_map_of_ad(U):
    """The 16 x 16 rational matrix of w -> dict^-1 (U dict(w) U^dag) in the vectorization index 4 mu + nu."""
    C = [[Fr(0)] * 16 for _ in range(16)]
    Ud = dag(U)
    for mu in range(4):
        for nu in range(4):
            M = mm(mm(U, smul(Fr(1, 4), pauli2(mu, nu))), Ud)
            w = coords3(M)
            for a in range(4):
                for b in range(4):
                    C[4 * a + b][4 * mu + nu] = w[a][b]
    return C


CNOT = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # |c t> -> |c, t xor c>, index 2c + t
UJ = mat([[G(Fr(1, 2), Fr(-1, 2)), G(Fr(-1, 2), Fr(-1, 2))],
          [G(Fr(1, 2), Fr(-1, 2)), G(Fr(1, 2), Fr(1, 2))]])  # (I - i(X+Y+Z))/2, the module's cycMat
UJH = mat([[G(Fr(1, 2), Fr(1, 2)), G(Fr(1, 2), Fr(1, 2))],
           [G(Fr(-1, 2), Fr(1, 2)), G(Fr(1, 2), Fr(-1, 2))]])  # the module's cycMatH
PHASE_I = diag(1, I_)
C35 = Fr(3, 5)
S45 = Fr(4, 5)
P35 = diag(1, G(C35, S45))

results = {}
counters = {}


def report(name, ok, detail):
    results[name] = bool(ok)
    print(f'{"PASS" if ok else "FAIL"} {name}: {detail}')


def counter(name, stated_holds, detail):
    """A countercontrol passes the audit iff the stated claim FAILS."""
    counters[name] = not stated_holds
    print(f'COUNTER {name} {"fails as stated" if not stated_holds else "DOES NOT FAIL (defect)"}: {detail}')


# ------------------------------------------------------------------------------------------------- group and orbit
def canon_key_mat(U):
    piv = next(x for row in U for x in row if not x.iszero())
    return tuple((y / piv).r for row in U for y in row) + tuple((y / piv).i for row in U for y in row)


def canon_vec(v):
    piv = next(x for x in v if not x.iszero())
    return [x / piv for x in v]


def key_vec(v):
    v = canon_vec(v)
    return tuple(x.r for x in v) + tuple(x.i for x in v)


def closure_group(gens, cap=1000):
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
    return list(seen.values())


def orbit_rays(gens, v0, cap=2000):
    seen = {key_vec(v0): canon_vec(v0)}
    frontier = [canon_vec(v0)]
    while frontier:
        nxt = []
        for v in frontier:
            for g in gens:
                w = mv(g, v)
                k = key_vec(w)
                if k not in seen:
                    seen[k] = canon_vec(w)
                    nxt.append(seen[k])
                    if len(seen) > cap:
                        return None
        frontier = nxt
    return seen


def overlap2(z, w):
    return inner(z, w).abs2() / (norm2(z) * norm2(w))


# =============================================================================================================== X1
def X1():
    gens = [CNOT, kron(I2, PHASE_I), kron(I2, UJ)]
    ok = True
    notes = []
    uj_unitary = meq(mm(UJ, dag(UJ)), I2) and meq(dag(UJ), UJH)
    ok &= uj_unitary
    notes.append(f'U_J unitary and cycMat^dag = cycMatH: {uj_unitary}')
    grp = closure_group(gens)
    n_grp = None if grp is None else len(grp)
    ok &= n_grp == 384
    notes.append(f'|<CNOT, 1(x)diag(1,i), 1(x)U_J>| projective = {n_grp} (target 384)')
    h = [G(10), G(2, -2), G(-1, -3), G(3, -1)]
    ok &= norm2(h) == 128
    orb = orbit_rays(gens, h)
    n_orb = None if orb is None else len(orb)
    ok &= n_orb == 192
    notes.append(f'|Z| by BFS = {n_orb} (target 192)')
    if grp is not None and orb is not None:
        orb2 = {key_vec(mv(U, h)) for U in grp}
        same = orb2 == set(orb.keys())
        ok &= same
        notes.append(f'orbit under all group elements equals the BFS orbit: {same}')
    rays = list(orb.values()) if orb else []
    ov = []
    for a in range(len(rays)):
        for b in range(a + 1, len(rays)):
            ov.append(overlap2(rays[a], rays[b]))
    lo, hi = (min(ov), max(ov)) if ov else (None, None)
    ok &= len(ov) == 18336 and lo == Fr(25, 2048) and hi == Fr(13, 16)
    notes.append(f'{len(ov)} pairs, squared overlaps in [{lo}, {hi}] (target [25/2048, 13/16])')
    c = Fr(401, 400)
    cc_all = all(c * c * s >= 4 * (c - 1) for s in ov)
    ok &= cc_all
    notes.append(f'(CC) c^2 s >= 4(c-1) at c = 401/400 on every pair: {cc_all}')
    R = kron(I2, P35)
    Rh = mv(R, h)
    mx = max(overlap2(Rh, z) for z in rays) if rays else None
    ok &= mx == Fr(1949, 2048) and mx < 1 / c
    notes.append(f'max squared overlap of R h with Z = {mx} (target 1949/2048), < 400/401: {mx is not None and mx < 1 / c}')
    Ph = smul(Fr(1, 128), [[h[i] * h[j].conj() for j in range(4)] for i in range(4)])
    d = msub(eye(4), smul(c, Ph))
    RdR = mm(mm(R, d), dag(R))
    val = inner(Rh, mv(RdR, Rh)) / norm2(Rh)
    ok &= val == G(Fr(-1, 400))
    notes.append(f'<Rh|R d R^dag|Rh>/|Rh|^2 = {val} (target -1/400); P_Rh in PSD cap Z*, so R d R^dag is outside K*')
    report('X1', ok, '; '.join(notes))
    return rays, h, d, Ph, ov, lo, c


# =============================================================================================================== X2
def X2():
    ok = True
    notes = []
    inst = []
    for dd in range(1, 8):
        for signs in itertools.product([1, -1], repeat=dd):
            if all(s == 1 for s in signs):
                continue
            trN = sum(signs)
            trH = 1 + trN
            holds = (dd + 1) * trH == trH * trH
            if holds != (trN == -1):
                ok = False
            if holds:
                inst.append((dd, 1 + signs.count(1)))
            if dd <= 5:
                H = fr_diag(1, *signs)
                Id = fr_eye(dd + 1)
                if fr_tr(fr_kron(H, Id)) != (dd + 1) * trH or fr_tr(fr_kron(H, H)) != trH * trH:
                    ok = False
    inst_set = sorted(set(inst))
    ok &= inst_set == [(1, 1), (3, 2), (5, 3), (7, 4)]
    notes.append(f'count holds iff tr N = -1 for d = 1..7 (built matrices d <= 5); instances (d, #+1 of H) = {inst_set}')
    # relC for Ad(CNOT) on W 3 with the three Bloch involutions of trace -1
    C = table_map_of_ad(CNOT)
    Cinv = fr_inv(C)
    I4 = fr_eye(4)
    # run 1 expected relC also for Ad(Y) = diag(-1,1,-1); the exact computation shows (Y(x)1) CNOT (Y(x)1) = CNOT (1(x)X)
    # while (1(x)Y) CNOT = CNOT (Z(x)Y), so relC holds for Ad(X) only (RUN HISTORY in the header); expectation corrected.
    expect = {(1, -1, -1): True, (-1, 1, -1): False, (-1, -1, 1): False}
    for signs, exp in expect.items():
        H = fr_diag(1, *signs)
        aC = fr_kron(H, I4)
        aT = fr_kron(I4, H)
        relC = fr_eq(fr_mm(aC, fr_mm(C, aC)), fr_mm(aT, C))
        derived = fr_eq(fr_mm(C, fr_mm(aC, Cinv)), fr_mm(aC, aT))
        count = 4 * fr_tr(H) == fr_tr(H) ** 2
        ok &= relC == exp and derived == exp and count
        notes.append(f'N = diag{signs}: relC {relC} (expected {exp}), G actC G^-1 = actC actT {derived}, count holds {count}')
    report('X2', ok, '; '.join(notes))
    return C


# =============================================================================================================== X3
def hybrid_T():
    """T[4s+mu][j]: the orthogonal-basis coordinate (P_s (x) sigma_mu, divided by tr = 2) of Phi(e_j);
    chart j: 0 = unit, 1 = w, 2..4 = a, 5..7 = b; t_s = (v0 +- w)/2, r_0 = (a+b)/2, r_1 = (a-b)/2,
    Phi(v) = sum_s P_s (x) (t_s I + r_s.sigma)/2."""
    T = [[Fr(0)] * 8 for _ in range(8)]
    for s in range(2):
        sg = 1 if s == 0 else -1
        T[4 * s + 0][0] = Fr(1, 4)
        T[4 * s + 0][1] = Fr(sg, 4)
        for k in range(3):
            T[4 * s + 1 + k][2 + k] = Fr(1, 4)
            T[4 * s + 1 + k][5 + k] = Fr(sg, 4)
    return T


HB = [kron(P0, SIG[mu]) for mu in range(4)] + [kron(P1, SIG[mu]) for mu in range(4)]  # orthogonal basis of V


def phi_of_chart(v):
    T = hybrid_T()
    c = [sum(T[a][j] * v[j] for j in range(8)) for a in range(8)]
    out = zeros(4)
    for a in range(8):
        if c[a] != 0:
            out = madd(out, smul(c[a], HB[a]))
    return out


def chart_of_state(s, q):
    """The chart vector (1, w, a, b) of the pure state |s,q><s,q|."""
    t0 = Fr(1) if s == 0 else Fr(0)
    t1 = Fr(1) - t0
    r = [Fr(0), Fr(0), Fr(1) if q == 0 else Fr(-1)]
    r0 = r if s == 0 else [Fr(0)] * 3
    r1 = r if s == 1 else [Fr(0)] * 3
    w = t0 - t1
    a = [r0[k] + r1[k] for k in range(3)]
    b = [r0[k] - r1[k] for k in range(3)]
    return [Fr(1), w] + a + b


def in_omega_h(v):
    v0, w = v[0], v[1]
    a, b = v[2:5], v[5:8]
    t0, t1 = (v0 + w) / 2, (v0 - w) / 2
    r0 = [(a[k] + b[k]) / 2 for k in range(3)]
    r1 = [(a[k] - b[k]) / 2 for k in range(3)]
    return t0 >= 0 and t1 >= 0 and sum(x * x for x in r0) <= t0 * t0 and sum(x * x for x in r1) <= t1 * t1


def dict_hybrid(w):
    """w: 64-vector (index 8 mu + nu) -> sum w[mu nu] Phi(e_mu) (x) Phi(e_nu), a 16 x 16 matrix (ordering (s1,q1,s2,q2))."""
    T = hybrid_T()
    TT = fr_kron(T, T)
    c = [sum(TT[A][j] * w[j] for j in range(64)) for A in range(64)]
    out = zeros(16)
    for A in range(64):
        if c[A] != 0:
            out = madd(out, smul(c[A], kron(HB[A // 8], HB[A % 8])))
    return out


def orth_coords_hybrid(M):
    """Coordinates of M in V (x) V in the basis HB_a (x) HB_b (tr((B(x)B)(B'(x)B')) = 4 delta)."""
    c = []
    for A in range(64):
        t = tr(mm(M, kron(HB[A // 8], HB[A % 8])))
        if t.i != 0:
            raise ValueError('non-real coordinate')
        c.append(t.r / 4)
    return c


def table_of_matrix_hybrid(M, TTinv):
    c = orth_coords_hybrid(M)
    return [sum(TTinv[j][A] * c[A] for A in range(64)) for j in range(64)]


def blocks_hybrid(M):
    """The four sector-pair blocks (s1, s2) of a 16 x 16 matrix in the ordering (s1,q1,s2,q2)."""
    out = {}
    for s1 in range(2):
        for s2 in range(2):
            idx = [4 * (2 * s1 + q1) + (2 * s2 + q2) for q1 in range(2) for q2 in range(2)]
            out[(s1, s2)] = [[M[i][j] for j in idx] for i in idx]
    return out


def X3():
    ok = True
    notes = []
    T = hybrid_T()
    Tinv = fr_inv(T)
    TT = fr_kron(T, T)
    TTinv = fr_kron(Tinv, Tinv)
    # the composite gate: CNOT on (q1 -> q2), identity on s1, s2; index 4(2 s1 + q1) + (2 s2 + q2)
    UG = zeros(16)
    for s1 in range(2):
        for q1 in range(2):
            for s2 in range(2):
                for q2 in range(2):
                    src = 4 * (2 * s1 + q1) + (2 * s2 + q2)
                    dst = 4 * (2 * s1 + q1) + (2 * s2 + (q2 ^ q1))
                    UG[dst][src] = G(1)
    # G in the orthogonal basis and then in the chart basis
    Gorth = [[Fr(0)] * 64 for _ in range(64)]
    for A in range(64):
        M = mm(mm(UG, kron(HB[A // 8], HB[A % 8])), dag(UG))
        col = orth_coords_hybrid(M)
        for A2 in range(64):
            Gorth[A2][A] = col[A2]
    Ge = fr_mm(TTinv, fr_mm(Gorth, TT))
    well = True  # Dict intertwines: Dict(Ge e_j) == UG Dict(e_j) UG^dag on a sample of basis tables
    for j in (0, 9, 18, 27, 36, 45, 63, 1, 8, 30):
        e = [Fr(1 if k == j else 0) for k in range(64)]
        Ge_e = [sum(Ge[r][k] * e[k] for k in range(64)) for r in range(64)]
        lhs = dict_hybrid(Ge_e)
        rhs = mm(mm(UG, dict_hybrid(e)), dag(UG))
        well &= meq(lhs, rhs)
    ok &= well
    notes.append(f'G = Ad(CNOT on the qubit factors) is a linear map of W 7 intertwined by Dict (10 basis tables): {well}')
    invol = fr_eq(fr_mm(Ge, Ge), fr_eye(64))
    ok &= invol
    notes.append(f'G involution: {invol}')
    H = fr_diag(1, 1, 1, -1, -1, 1, -1, -1)
    trH = fr_tr(H)
    aC = fr_kron(H, fr_eye(8))
    aT = fr_kron(fr_eye(8), H)
    relC = fr_eq(fr_mm(aC, fr_mm(Ge, aC)), fr_mm(aT, Ge))
    ok &= relC and trH == 0
    notes.append(f'relC on all 64 basis tables with N = 1 (+) nflip (+) nflip: {relC}; tr H = {trH}; d = 7 odd')
    # Entangling instance
    v_plus = [Fr(1), Fr(1), Fr(1), Fr(0), Fr(0), Fr(1), Fr(0), Fr(0)]   # sector 0, Bloch r0 = (1,0,0)
    v_zero = chart_of_state(0, 0)
    pure_plus = meq(phi_of_chart(v_plus), kron(P0, mat([[Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]])))
    w = [v_plus[mu] * v_zero[nu] for mu in range(8) for nu in range(8)]
    rank_before = fr_rank([[w[8 * mu + nu] for nu in range(8)] for mu in range(8)])
    Gw = [sum(Ge[r][k] * w[k] for k in range(64)) for r in range(64)]
    rank_after = fr_rank([[Gw[8 * mu + nu] for nu in range(8)] for mu in range(8)])
    ent = pure_plus and rank_before == 1 and rank_after >= 2
    ok &= ent
    notes.append(f'Entangling instance: product table rank {rank_before} -> after G rank {rank_after} (Phi(v_plus) is the pure state: {pure_plus})')
    # four perfectly distinguishable states, in Omega_h
    states = {(s, q): kron(P0 if s == 0 else P1, P0 if q == 0 else P1) for s in range(2) for q in range(2)}
    charts = {(s, q): chart_of_state(s, q) for s in range(2) for q in range(2)}
    mem = all(in_omega_h(charts[k]) for k in charts)
    transport = all(meq(phi_of_chart(charts[k]), states[k]) for k in charts)
    dist = all(tr(mm(states[k], states[k2])) == G(1 if k == k2 else 0) for k in states for k2 in states)
    ok &= mem and transport and dist
    notes.append(f'four states |s,q><s,q| in Omega_h: {mem}, transported by Phi: {transport}, distinguished by the four projector effects: {dist}')
    # K-inf Geom failure: the effect t_1 = P_1 (x) 1 vanishes on two distinct states
    e_t1 = kron(P1, I2)
    geom = (tr(mm(e_t1, states[(0, 0)])) == G(0) and tr(mm(e_t1, states[(0, 1)])) == G(0)
            and not meq(states[(0, 0)], states[(0, 1)]) and tr(mm(e_t1, states[(1, 0)])) == G(1))
    ok &= geom
    notes.append(f'effect t_1 is 0 on the two distinct states |0,0>, |0,1> and 1 on |1,0>: {geom}')
    # boundary segment: midpoint of |0,0><0,0| and |1,0><1,0|; the effect 1 (x) |1><1| vanishes on it
    m = smul(Fr(1, 2), madd(states[(0, 0)], states[(1, 0)]))
    f = kron(I2, P1)
    vm = [(charts[(0, 0)][k] + charts[(1, 0)][k]) / 2 for k in range(8)]
    seg = (tr(mm(f, m)) == G(0) and not meq(states[(0, 0)], states[(1, 0)]) and in_omega_h(vm)
           and tr(mm(f, states[(0, 1)])) == G(1))
    # the midpoint attains both constraints with equality
    t0 = (vm[0] + vm[1]) / 2
    t1 = (vm[0] - vm[1]) / 2
    r0 = [(vm[2 + k] + vm[5 + k]) / 2 for k in range(3)]
    r1 = [(vm[2 + k] - vm[5 + k]) / 2 for k in range(3)]
    tight = sum(x * x for x in r0) == t0 * t0 and sum(x * x for x in r1) == t1 * t1
    ok &= seg and tight
    notes.append(f'midpoint of |0,0>, |1,0> in Omega_h, on the boundary (effect 1(x)|1><1| vanishes; both ball constraints tight): {seg and tight} -> not strictly convex, not an ellipsoid')
    # composite K instance: blockwise PSD preserved by G and by the drive rotation on token 2
    bell = [G(1), G(0), G(0), G(1)]
    Pbell = smul(Fr(1, 2), [[bell[i] * bell[j].conj() for j in range(4)] for i in range(4)])
    rho00 = madd(smul(Fr(1, 2), Pbell), smul(Fr(1, 8), eye(4)))
    rho01 = kron(mat([[Fr(1, 2), Fr(1, 4)], [Fr(1, 4), Fr(1, 2)]]), mat([[Fr(3, 4), G(0, Fr(1, 4))], [G(0, Fr(-1, 4)), Fr(1, 4)]]))
    rho10 = kron(mat([[Fr(1), 0], [0, 0]]), mat([[Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]]))
    rho11 = smul(Fr(1, 4), eye(4))
    M = zeros(16)
    for (s1, s2), blk in {(0, 0): rho00, (0, 1): rho01, (1, 0): rho10, (1, 1): rho11}.items():
        idx = [4 * (2 * s1 + q1) + (2 * s2 + q2) for q1 in range(2) for q2 in range(2)]
        for i, ii in enumerate(idx):
            for j, jj in enumerate(idx):
                M[ii][jj] = M[ii][jj] + blk[i][j]
    blocks0 = blocks_hybrid(M)
    inK = all(is_psd(b) for b in blocks0.values())
    wM = table_of_matrix_hybrid(M, TTinv)
    roundtrip = meq(dict_hybrid(wM), M)
    GwM = [sum(Ge[r][k] * wM[k] for k in range(64)) for r in range(64)]
    inK_G = all(is_psd(b) for b in blocks_hybrid(dict_hybrid(GwM)).values())
    # the drive rotation at cos t = 3/5 on token 2: chart H_rot = diag(1, 1, R, 1, R, 1) in (w; a1,a2,a3; b1,b2,b3)
    Hrot = fr_eye(8)
    for base in (2, 5):
        Hrot[base][base] = C35
        Hrot[base][base + 1] = -S45
        Hrot[base + 1][base] = S45
        Hrot[base + 1][base + 1] = C35
    aTrot = fr_kron(fr_eye(8), Hrot)
    Urot = kron(eye(4), kron(I2, P35))
    inter = True
    for j in (0, 9, 18, 27, 45, 63, 11, 29):
        e = [Fr(1 if k == j else 0) for k in range(64)]
        ae = [sum(aTrot[r][k] * e[k] for k in range(64)) for r in range(64)]
        inter &= meq(dict_hybrid(ae), mm(mm(Urot, dict_hybrid(e)), dag(Urot)))
    rwM = [sum(aTrot[r][k] * wM[k] for k in range(64)) for r in range(64)]
    inK_rot = all(is_psd(b) for b in blocks_hybrid(dict_hybrid(rwM)).values())
    ok &= inK and roundtrip and inK_G and inter and inK_rot
    notes.append(f'composite K instance in K: {inK} (table round trip {roundtrip}); G preserves K: {inK_G}; drive rotation (cos t = 3/5) on token 2 intertwined by Dict (8 basis tables): {inter}, preserves K: {inK_rot}')
    report('X3', ok, '; '.join(notes))


# =============================================================================================================== X4
def X4():
    ok = True
    notes = []
    for n in (2, 3, 4):
        count_a = 0
        bad_a = 0
        for bits in range(1 << (n * n)):
            P = [[(bits >> (n * i + j)) & 1 for j in range(n)] for i in range(n)]
            if any(P[i][j] != P[j][i] for i in range(n) for j in range(i + 1, n)):
                continue
            PP = [[sum(P[i][k] * P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
            if PP != P:
                continue
            count_a += 1
            if any(P[i][j] != 0 for i in range(n) for j in range(n) if i != j):
                bad_a += 1
        count_b = 0
        bad_b = 0
        for bits in range(1 << (n * n)):
            V = [[(bits >> (n * i + j)) & 1 for j in range(n)] for i in range(n)]
            Gm = [[sum(V[k][i] * V[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
            GG = [[sum(Gm[i][k] * Gm[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
            if GG != Gm:
                continue
            count_b += 1
            if any(sum(V[i][j] for i in range(n)) > 1 for j in range(n)):
                bad_b += 1
        ok &= bad_a == 0 and bad_b == 0 and count_a == 2 ** n
        notes.append(f'n={n}: (a) {count_a} symmetric idempotent {{0,1}} matrices (= 2^n diagonal ones), {bad_a} non-diagonal; (b) {count_b} matrices with (V^T V)^2 = V^T V, {bad_b} with a column of two ones')
    phases = [G(1), I_, G(-1), G(0, -1)]
    for n in (2, 3):
        total = 0
        agree = True
        for perm in itertools.permutations(range(n)):
            for ph in itertools.product(range(4), repeat=n):
                U = zeros(n)
                for a in range(n):
                    U[perm[a]][a] = phases[ph[perm[a]]]
                all01 = True
                transport = True
                for a in range(n):
                    for b in range(n):
                        E = zeros(n)
                        E[a][b] = G(1)
                        Mx = mm(mm(U, E), dag(U))
                        for i in range(n):
                            for j in range(n):
                                x = Mx[i][j]
                                if not (x == G(0) or x == G(1)):
                                    all01 = False
                                exp = G(1 if (i, j) == (perm[a], perm[b]) else 0)
                                if all01 and x != exp:
                                    transport = False
                equal_ph = len(set(ph)) == 1
                total += 1
                if all01 != equal_ph or (all01 and not transport):
                    agree = False
        ok &= agree
        notes.append(f'n={n}: {total} monomial unitaries, Ad(U) maps all units to {{0,1}} iff phases equal, and then transports along sigma: {agree}')
    Unm = smul(Fr(1, 5), mat([[3, 4], [-4, 3]]))
    E00 = mat([[1, 0], [0, 0]])
    Mx = mm(mm(Unm, E00), dag(Unm))
    nonmono_fails = meq(mm(Unm, dag(Unm)), I2) and not all(x == G(0) or x == G(1) for row in Mx for x in row)
    ok &= nonmono_fails
    notes.append(f'non-monomial unitary [[3,4],[-4,3]]/5 maps E_00 outside {{0,1}}: {nonmono_fails} (image {Mx[0]}, {Mx[1]})')
    report('X4', ok, '; '.join(notes))


# =============================================================================================================== X5
def sq3(Xv):
    return sum(x * x for x in Xv)


def dot3(Xv, Yv):
    return sum(Xv[k] * Yv[k] for k in range(3))


def in_PC(z, swap=False):
    u, v, Xv = z
    S = sq3(Xv)
    return u >= 0 and v >= 0 and (S ** 3 <= (u ** 4 * v ** 2 if swap else u ** 2 * v ** 4))


def Bform(z, w):
    return z[0] * w[0] / 3 + 2 * z[1] * w[1] / 3 + dot3(z[2], w[2])


def X5():
    ok = True
    notes = []
    pts = [Fr(k, 3) for k in range(-3, 4)]  # 7 points
    amgm = all((a + 2 * b) ** 3 - 27 * a * b * b == (a - b) ** 2 * (a + 8 * b) for a in pts[:4] for b in pts[:4])
    bern = all(t ** 6 - (6 * t - 5) == (t - 1) ** 2 * (t ** 4 + 2 * t ** 3 + 3 * t ** 2 + 4 * t + 5) for t in pts)
    form = True
    for bits in itertools.product([Fr(0), Fr(1)], repeat=10):
        T_, S_, T2, S2 = bits[0], bits[1], bits[2], bits[3]
        Xv, Xw = list(bits[4:7]), list(bits[7:10])
        lhs = T_ * T2 + S_ * S2 - (T_ * S2 + S_ * T2) / 3 + dot3(Xv, Xw)
        rhs = Bform((T_ + S_, T_ - S_, Xv), (T2 + S2, T2 - S2, Xw))
        form &= lhs == rhs
    ok &= amgm and bern and form
    notes.append(f'identities: AM-GM {amgm}, Bernoulli-6 {bern}, form_eq (multilinear, {{0,1}}^10) {form}')
    dirs = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, -1, 1), (2, 1, -2), (-1, 2, 2), (3, -4, 0)]
    qs = [Fr(0), Fr(1, 8), Fr(1, 4), Fr(1, 2), Fr(1), Fr(2), Fr(4)]
    grid = []
    for u in (Fr(0), Fr(1, 2), Fr(1), Fr(2), Fr(3)):
        for v in (Fr(0), Fr(1, 2), Fr(1), Fr(2), Fr(3)):
            for D in dirs:
                best = None
                for q in qs:
                    Xv = [q * Fr(x) for x in D]
                    if in_PC((u, v, Xv)):
                        best = Xv
                if best is not None:
                    grid.append((u, v, best))
    grid = list({(z[0], z[1], tuple(z[2])) for z in grid})
    grid = [(u, v, list(Xv)) for (u, v, Xv) in grid]
    mins = min(Bform(z, w) for z in grid for w in grid)
    nonneg = mins >= 0
    ok &= nonneg
    notes.append(f'B >= 0 on all pairs of {len(grid)} exact PC points (min {mins}): {nonneg}')
    zt = (Fr(1), Fr(1, 8), [Fr(1, 4), Fr(0), Fr(0)])
    wt = (Fr(1, 8), Fr(1), [Fr(-1, 2), Fr(0), Fr(0)])
    tight = in_PC(zt) and in_PC(wt) and Bform(zt, wt) == 0
    ok &= tight
    notes.append(f'tight pair in PC with B = 0: {tight}')
    # converse witnesses, u', v' > 0
    for w in [(Fr(1), Fr(1), [Fr(2), Fr(0), Fr(0)]), (Fr(2), Fr(1, 2), [Fr(1), Fr(1), Fr(0)])]:
        u2, v2, X2v = w
        S2 = sq3(X2v)
        outside = not in_PC(w)
        rho = u2 ** 2 * v2 ** 4 / S2 ** 3
        theta = (5 + rho) / 6
        s = theta * S2 / (u2 * v2)
        z = (v2 * s, u2 * s, [-x for x in X2v])
        val = Bform(z, w)
        good = outside and in_PC(z) and val == (theta - 1) * S2 and val < 0
        ok &= good
        notes.append(f'w = ({u2}, {v2}, {X2v}) outside PC; z = (v\'s, u\'s, -X\') in PC pairs {val} = (theta-1) S\' < 0: {good}')
    # u' = 0
    w = (Fr(0), Fr(1), [Fr(1), Fr(0), Fr(0)])
    u2, v2, X2v = w
    S2 = sq3(X2v)
    z = ((v2 + 1) ** 2 * (S2 + 1) / S2, S2 / (v2 + 1), [-x for x in X2v])
    val = Bform(z, w)
    good0 = (not in_PC(w)) and in_PC(z) and val * (3 * (v2 + 1)) == -(S2 * (v2 + 3)) and val < 0
    ok &= good0
    notes.append(f'u\' = 0 witness: w = {w[:2]}, X\' = {X2v}; z in PC, B = {val} < 0: {good0}')
    # v' = 0
    w = (Fr(1), Fr(0), [Fr(1), Fr(0), Fr(0)])
    u2, v2, X2v = w
    S2 = sq3(X2v)
    b = S2 + (u2 + 1) ** 2 + 1
    z = (S2 / (u2 + 1), b, [-x for x in X2v])
    val = Bform(z, w)
    good1 = (not in_PC(w)) and in_PC(z) and val * (3 * (u2 + 1)) == -(S2 * (2 * u2 + 3)) and val < 0
    ok &= good1
    notes.append(f'v\' = 0 witness: w = {w[:2]}, X\' = {X2v}; z in PC, B = {val} < 0: {good1}')
    report('X5', ok, '; '.join(notes))


# =============================================================================================================== X6
def actT_table(H, w):
    """(actT w)[mu][alpha] = sum_beta H[alpha][beta] w[mu][beta]."""
    return [[sum(H[a][b] * w[mu][b] for b in range(4)) for a in range(4)] for mu in range(4)]


def X6():
    ok = True
    notes = []
    Hrot = [[Fr(1), Fr(0), Fr(0), Fr(0)], [Fr(0), C35, -S45, Fr(0)], [Fr(0), S45, C35, Fr(0)], [Fr(0), Fr(0), Fr(0), Fr(1)]]
    Hrot90 = [[Fr(1), Fr(0), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(-1), Fr(0)], [Fr(0), Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(0), Fr(1)]]
    Hcyc = [[Fr(1), Fr(0), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(0), Fr(1)], [Fr(0), Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(1), Fr(0)]]
    cases = [('rotLin at cos t = 3/5', Hrot, kron(I2, P35)), ('rotLin at t = pi/2', Hrot90, kron(I2, PHASE_I)),
             ('cycEquiv', Hcyc, kron(I2, UJ))]
    for name, H, U in cases:
        good = True
        for mu in range(4):
            for nu in range(4):
                w = basis_table(mu, nu)
                lhs = dict3(actT_table(H, w))
                rhs = mm(mm(U, dict3(w)), dag(U))
                good &= meq(lhs, rhs)
        ok &= good
        notes.append(f'{name}: dict(actT w) = U dict(w) U^dag on all 16 basis tables: {good}')
    uj = meq(mm(UJ, dag(UJ)), I2) and meq(mm(UJ, dag(UJ)), mm(dag(UJ), UJ)) and meq(dag(UJ), UJH)
    ok &= uj
    notes.append(f'U_J unitary, cycMat^dag = cycMatH: {uj}')
    report('X6', ok, '; '.join(notes))


# =============================================================================================================== X7
def X7(rays, h, d, Ph, c):
    ok = True
    notes = []
    dets = []
    for z in rays:
        Psi = [[z[0], z[1]], [z[2], z[3]]]
        dets.append(det(Psi).abs2() / (norm2(z) ** 2))
    mn = min(dets)
    bound = (1 / c) * (1 - 1 / c)
    ok &= mn == Fr(85, 2048) and mn >= bound
    notes.append(f'min normalized |det Psi_z|^2 over Z = {mn} (target 85/2048) >= (1/c)(1-1/c) = {bound}: {mn >= bound} -> c lambda_max <= 1 on every ray (H1 for every defect)')
    hdh = inner(h, mv(d, h)) / norm2(h)
    notpsd = (hdh == G(Fr(-1, 400))) and not is_psd(d)
    ok &= notpsd
    notes.append(f'<h|d|h>/|h|^2 = {hdh}; d not PSD: {notpsd}')
    Th = coords3(Ph)
    zstar = [[Fr(1, 2) * basis_table(0, 0)[a][b] - (c / 8) * Th[a][b] for b in range(4)] for a in range(4)]
    img = meq(dict3(zstar), smul(Fr(1, 8), d))
    ok &= img
    notes.append(f'dict(z*) = d/8 for z* = E00/2 - (c/8) T_h: {img}')
    report('X7', ok, '; '.join(notes))


# =============================================================================================================== X8
def X8():
    ok = True
    notes = []
    y = [Fr(5, 6), Fr(0), Fr(0), Fr(5, 6)]
    xx = sum(t * t for t in y[:3])
    val4 = xx * xx + y[3] ** 4
    inO4 = val4 <= 1
    pairing = 1 - sum(t * t for t in y)
    ok &= inO4 and val4 == Fr(1250, 1296) and pairing == Fr(-7, 18)
    notes.append(f'y = (5/6,0,0,5/6): (x.x)^2 + s^4 = {val4} <= 1: {inO4}; (1,y).(1,-y) = {pairing} (target -7/18)')
    # support of Omega_4 in e_0 and e_3 is 1: (x.x)^2 + s^4 <= 1 gives |x_0| <= 1 and |s| <= 1 with equality attained
    supp = all((sum(t * t for t in p[:3]) ** 2 + p[3] ** 4 <= 1) for p in ([Fr(1), 0, 0, 0], [0, 0, 0, Fr(1)]))
    ok &= supp
    notes.append(f'(1,0,0,0) and (0,0,0,1) lie in Omega_4 (support 1 attained): {supp}')
    # Euclidean 4-ball: the scaled points pair nonnegatively
    scale = Fr(1)
    yy = sum(t * t for t in y)
    # y lies outside the unit ball (yy = 25/18 > 1); scale into the ball by 3/5 (then |y'|^2 = 1/2)
    yb = [t * Fr(3, 5) for t in y]
    ball_pair = 1 - sum(t * t for t in yb)
    ok &= sum(t * t for t in yb) <= 1 and ball_pair >= 0
    notes.append(f'the scaled point (3/5) y lies in the 4-ball and pairs {ball_pair} >= 0 with its negative: {ball_pair >= 0}')
    report('X8', ok, '; '.join(notes))


# ====================================================================================================== countercontrols
def countercontrols(rays, h, ov, lo, c):
    c2 = Fr(301, 300)
    cc1 = all(c2 * c2 * s >= 4 * (c2 - 1) for s in ov)
    counter('CC1', cc1, f'(CC) at c\' = 301/300 on the minimal pair: c\'^2 s_min = {c2 * c2 * lo} vs 4(c\'-1) = {4 * (c2 - 1)}')
    R2 = kron(I2, PHASE_I)
    R2h = mv(R2, h)
    mx2 = max(overlap2(R2h, z) for z in rays)
    counter('CC2', mx2 <= Fr(1949, 2048), f'max squared overlap of (1 (x) diag(1,i)) h with Z = {mx2}')
    H4 = fr_diag(1, -1, -1, 1, 1)
    t = fr_tr(H4)
    cc3 = 5 * t == t * t
    counter('CC3', cc3, f'chart-4 tokens\' NOT: (d+1) tr H = {5 * t}, (tr H)^2 = {t * t}')
    E01 = mat([[0, 1], [0, 0]])
    Mx = mm(mm(PHASE_I, E01), dag(PHASE_I))
    cc4 = all(x == G(0) or x == G(1) for row in Mx for x in row)
    counter('CC4', cc4, f'Ad(diag(1,i))(E_01) = {Mx[0]}, {Mx[1]}')
    z = (Fr(1), Fr(27, 64), [Fr(3, 4), Fr(0), Fr(0)])
    zb = (Fr(1), Fr(27, 64), [Fr(-3, 4), Fr(0), Fr(0)])
    both = in_PC(z, swap=True) and in_PC(zb, swap=True)
    val = Bform(z, zb)
    counter('CC5', (not both) or val >= 0, f'swapped exponents: both points in PC\': {both}; B = {val}')


def main():
    print('indep_checkE4.py -- independent exact check of research/equivalence round-4 claims (E15-E18)')
    rays, h, d, Ph, ov, lo, c = X1()
    X2()
    X3()
    X4()
    X5()
    X6()
    X7(rays, h, d, Ph, c)
    X8()
    countercontrols(rays, h, ov, lo, c)
    n_pass = sum(1 for v in results.values() if v)
    n_cc = sum(1 for v in counters.values() if v)
    print(f'checks: {len(results)}, passed: {n_pass}, failures: {len(results) - n_pass}; countercontrols failing as stated: {n_cc}/{len(counters)}')
    verdict = 'INDEP-E4-FIXED' if n_pass == len(results) == 8 and n_cc == len(counters) == 5 else 'INDEP-E4-OPEN'
    print(f'VERDICT {verdict}')
    return 0 if verdict == 'INDEP-E4-FIXED' else 1


if __name__ == '__main__':
    sys.exit(main())
