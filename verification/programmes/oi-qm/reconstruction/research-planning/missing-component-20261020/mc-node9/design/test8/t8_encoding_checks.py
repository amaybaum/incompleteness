# Test-8 design, exact checks on one site of the two-valued alphabet.
# Run: python3 -I t8_encoding_checks.py > t8_encoding_checks.out
#
# Site configuration x = (p, c) in F2 x F2, p the previous value, c the current value,
# as in the kernel (SecondOrderCircuit.lean: shear (p,c) -> (F c - p, c), swapLayer (p,c) -> (c,p)).
# An encoding E sends configurations to qubit states; for E affine on distributions it is fixed by
# the four Bloch vectors r[x].  Covariance  E(F x) = U E(x) U^dag  reads  r[F x] = R_U r[x],
# R_U the Bloch rotation of U.  Everything is Fractions / Gaussian rationals; no floats.
from fractions import Fraction as Fr
from itertools import product

# ---------- Gaussian rationals and 2x2 matrices ----------
class G:
    __slots__ = ("re", "im")
    def __init__(s, re=0, im=0): s.re, s.im = Fr(re), Fr(im)
    def __add__(s, o): return G(s.re + o.re, s.im + o.im)
    def __sub__(s, o): return G(s.re - o.re, s.im - o.im)
    def __mul__(s, o): return G(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    def conj(s): return G(s.re, -s.im)
    def __eq__(s, o): return s.re == o.re and s.im == o.im
    def iszero(s): return s.re == 0 and s.im == 0
    def scale(s, f): return G(s.re*f, s.im*f)

def mm(A, B):
    n = len(A); return [[sum((A[i][k]*B[k][j] for k in range(n)), G()) for j in range(n)] for i in range(n)]
def dag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A))]
def msc(A, f): return [[a.scale(f) for a in row] for row in A]
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))
def isscalar(A):
    n = len(A); return all((A[i][j].iszero() if i != j else A[i][i] == A[0][0]) for i in range(n) for j in range(n))
def tr(A): return sum((A[i][i] for i in range(len(A))), G())

I2 = [[G(1), G()], [G(), G(1)]]
X = [[G(), G(1)], [G(1), G()]]
Y = [[G(), G(0, -1)], [G(0, 1), G()]]
Z = [[G(1), G()], [G(), G(-1)]]
PAULI = {"I": I2, "X": X, "Y": Y, "Z": Z}
# A unitary is stored as (M, k) with U = M / sqrt(k), M M^dag = k I.
Hm = ([[G(1), G(1)], [G(1), G(-1)]], 2)
Sm = ([[G(1), G()], [G(), G(0, 1)]], 1)
Sdm = ([[G(1), G()], [G(), G(0, -1)]], 1)

def umul(U, V): return (mm(U[0], V[0]), U[1]*V[1])
def ad(U, A): return msc(mm(mm(U[0], A), dag(U[0])), Fr(1, U[1]))
def bloch_rot(U, anti=False):
    # R[i][j] = 1/2 Tr(sigma_i Ad_U(sigma_j)); anti=True means rho -> U conj(rho) U^dag
    sig = [X, Y, Z]
    R = []
    for si in sig:
        row = []
        for sj in sig:
            sj2 = [[a.conj() for a in r] for r in sj] if anti else sj
            v = tr(mm(si, ad(U, sj2))).scale(Fr(1, 2))
            assert v.im == 0
            row.append(v.re)
        R.append(row)
    return R
def det3(R):
    return (R[0][0]*(R[1][1]*R[2][2]-R[1][2]*R[2][1]) - R[0][1]*(R[1][0]*R[2][2]-R[1][2]*R[2][0])
            + R[0][2]*(R[1][0]*R[2][1]-R[1][1]*R[2][0]))

# ---------- exact linear algebra ----------
def nullspace(rows, n):
    A = [list(map(Fr, r)) for r in rows]; piv = []; r = 0
    for c in range(n):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]; pv = A[r][c]; A[r] = [a/pv for a in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [a - f*b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
        if r == len(A): break
    free = [c for c in range(n) if c not in piv]; basis = []
    for f in free:
        v = [Fr(0)]*n; v[f] = Fr(1)
        for i, c in enumerate(piv): v[c] = -A[i][f]
        basis.append(v)
    return basis
def rank(vecs):
    if not vecs: return 0
    n = len(vecs[0]); return n - len(nullspace(vecs, n)) if True else 0
def rank_rows(rows):
    if not rows: return 0
    return len(rows[0]) - len(nullspace(rows, len(rows[0])))

CONF = [(p, c) for p in (0, 1) for c in (0, 1)]       # order 00,01,10,11 as (p,c)
idx = {x: i for i, x in enumerate(CONF)}
def var(x, k): return 3*idx[x] + k
swap = lambda x: (x[1], x[0])
shear_self = lambda x: ((x[1] - x[0]) % 2, x[1])      # F(c) = c  (centre term)
shear_free1 = lambda x: ((0 - x[0]) % 2, x[1])         # F = 0 on an isolated centre-free site: identity on F2
leap_self = lambda x: swap(shear_self(x))

def constraints(F, R):
    rows = []
    for x in CONF:
        for k in range(3):
            row = [Fr(0)]*12
            row[var(F(x), k)] += 1
            for j in range(3): row[var(x, j)] -= R[k][j]
            rows.append(row)
    return rows

def sign(F):
    perm = [idx[F(x)] for x in CONF]; s = 1; seen = set()
    for i in range(4):
        if i in seen: continue
        j, L = i, 0
        while j not in seen: seen.add(j); j = perm[j]; L += 1
        s *= (-1)**(L - 1)
    return s

def affine_rank(sol):
    # rank of the linear part of E: span of r[x] - r[00]
    r = [[sol[var(x, k)] for k in range(3)] for x in CONF]
    return rank_rows([[r[i][k] - r[0][k] for k in range(3)] for i in range(1, 4)])

def max_affine_rank(basis):
    best = 0
    for coeffs in product(range(-2, 3), repeat=min(len(basis), 5)):
        if len(basis) > 5: coeffs = coeffs + (1,)*(len(basis)-5)
        sol = [sum((c*b[i] for c, b in zip(coeffs, basis)), Fr(0)) for i in range(12)]
        best = max(best, affine_rank(sol))
        if best == 3: break
    return best

out = []
def say(*a): out.append(" ".join(str(x) for x in a))

say("== control: unitarity and Clifford relations")
for name, U in [("H", Hm), ("S", Sm), ("Sdag", Sdm)]:
    assert meq(mm(U[0], dag(U[0])), msc(I2, U[1]))
say("S^2 = Z:", meq(umul(Sm, Sm)[0], Z), "| S^2 scalar:", isscalar(umul(Sm, Sm)[0]))
say("H^2 scalar:", isscalar(umul(Hm, Hm)[0]))
for P in "IXYZ":
    L = umul(Sm, (PAULI[P], 1)) if P != "I" else Sm
    L2 = umul((PAULI[P], 1), Sm) if P != "I" else Sm
    say(f"lift S*{P}: square scalar {isscalar(umul(L, L)[0])}; diagonal {L[0][0][1].iszero() and L[0][1][0].iszero()}"
        f" | lift {P}*S: square scalar {isscalar(umul(L2, L2)[0])}")
say("label action of S: X ->", [ [str(a.re)+('+'+str(a.im)+'i' if a.im else '') for a in r] for r in ad(Sm, X)], "(= Y), Z -> Z:", meq(ad(Sm, Z), Z))
say("label action of H: X -> Z:", meq(ad(Hm, X), Z), "Z -> X:", meq(ad(Hm, Z), X), "Y -> -Y:", meq(ad(Hm, Y), msc(Y, -1)))

say("\n== node 1: shear and swap are involutions of the site configurations (kernel shear_shear, swapLayer_swapLayer)")
say("shear_self involution:", all(shear_self(shear_self(x)) == x for x in CONF),
    "| swap involution:", all(swap(swap(x)) == x for x in CONF),
    "| shear_free1 is identity on F2:", all(shear_free1(x) == x for x in CONF))
say("permutation signs on the 4 site configurations: swap", sign(swap), "shear_self", sign(shear_self),
    "leap_self", sign(leap_self))

say("\n== node 1/2: covariant affine encodings for every Pauli-coset lift, shear -> S.P, swap -> H.Q")
for P, Q in product("IXYZ", repeat=2):
    Ush = Sm if P == "I" else umul(Sm, (PAULI[P], 1))
    Usw = Hm if Q == "I" else umul(Hm, (PAULI[Q], 1))
    rows = constraints(shear_self, bloch_rot(Ush)) + constraints(swap, bloch_rot(Usw))
    B = nullspace(rows, 12)
    zvar = any(b[var((0, 0), 2)] != b[var((0, 1), 2)] or b[var((1, 0), 2)] != b[var((1, 1), 2)]
               or b[var((0, 0), 2)] != b[var((1, 1), 2)] for b in B)
    rows_pr = list(rows)
    for c in (0, 1):
        row = [Fr(0)]*12; row[var((0, c), 2)] = 1; row[var((1, c), 2)] = -1; rows_pr.append(row)
    Bpr = nullspace(rows_pr, 12)
    reads = any(b[var((0, 0), 2)] != b[var((0, 1), 2)] for b in Bpr)
    say(f"shear->S{P if P!='I' else ''} swap->H{Q if Q!='I' else ''}: position-reading solution exists: {reads};"
        f" solution dim {len(B)}"
        + (f", max affine rank {max_affine_rank(B)}, Z-statistics vary over configurations: {zvar}"
           if B else " (E constant = I/2)"))

say("\n== node 1: involution lemma with a spectator (2 x 2): commutant of {Z(x)I, X(x)I} in M_4(C)")
def kron(A, B):
    return [[A[i//2][j//2]*B[i % 2][j % 2] for j in range(4)] for i in range(4)]
ZI, XI = kron(Z, I2), kron(X, I2)
# unknown A = sum over 16 real pairs; commutator constraints as real linear system in 32 unknowns
def comm_rows(K):
    rows = []
    for i in range(4):
        for j in range(4):
            re = [Fr(0)]*32; im = [Fr(0)]*32
            for k in range(4):
                # (A K)_ij = A_ik K_kj ; (K A)_ij = K_ik A_kj
                for (a, b, coef) in [((i, k), None, K[k][j]), ((k, j), None, K[i][k].scale(-1))]:
                    t = 2*(4*a[0] + a[1])
                    # (x + i y) * (u + i v) = (xu - yv) + i (xv + yu)
                    re[t] += coef.re; re[t+1] -= coef.im
                    im[t] += coef.im; im[t+1] += coef.re
            rows += [re, im]
    return rows
Bc = nullspace(comm_rows(ZI) + comm_rows(XI), 32)
say("real dimension of commutant:", len(Bc), "(I (x) M_2 has real dimension 8)")

say("\n== node 2: swap alone, every unitary lift H.Q and the monomial control X; antiunitary countercontrol")
for name, U, anti in [("H", Hm, False), ("HX", umul(Hm, (X, 1)), False), ("HY", umul(Hm, (Y, 1)), False),
                      ("HZ", umul(Hm, (Z, 1)), False), ("X (monomial)", (X, 1), False),
                      ("I (identity)", (I2, 1), False), ("H.K (antiunitary)", Hm, True)]:
    R = bloch_rot(U, anti)
    B = nullspace(constraints(swap, R), 12)
    say(f"swap->{name}: det R = {det3(R)}, solution dim {len(B)}, max affine rank {max_affine_rank(B)}")

say("\n== node 2 positive control: the self-coupled one-step map (even, 3-cycle) with U = H.S")
R = bloch_rot(umul(Hm, Sm))
B = nullspace(constraints(leap_self, R), 12)
say(f"leap_self->HS: det R = {det3(R)}, solution dim {len(B)}, max affine rank {max_affine_rank(B)}")
R = bloch_rot(umul(Sm, Hm))
B = nullspace(constraints(leap_self, R), 12)
say(f"leap_self->SH: det R = {det3(R)}, solution dim {len(B)}, max affine rank {max_affine_rank(B)}")

say("\n== node 2: det of every single-qubit Clifford Bloch rotation (generated by H, S mod phase)")
seen = []; frontier = [bloch_rot((I2, 1))]
gens = [bloch_rot(Hm), bloch_rot(Sm)]
def m3(A, B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
while frontier:
    R = frontier.pop()
    if R in seen: continue
    seen.append(R)
    for g in gens: frontier.append(m3(g, R))
say("group order", len(seen), "| all det +1:", all(det3(R) == 1 for R in seen))

say("\n== node 3: swap -> H, position-reading solutions (z depends only on the current value c)")
RH = bloch_rot(Hm)
rows = constraints(swap, RH)
for c in (0, 1):                      # z(0,c) = z(1,c)
    row = [Fr(0)]*12; row[var((0, c), 2)] = 1; row[var((1, c), 2)] = -1; rows.append(row)
B = nullspace(rows, 12)
say("dim of position-reading-compatible solutions:", len(B))
ok_x = True; ok_fixed = True
for b in B:
    g = {c: b[var((0, c), 2)] for c in (0, 1)}
    for (p, c) in CONF:
        if b[var((p, c), 0)] != g[p]: ok_x = False          # x-component = g(previous)
    for v in (0, 1):
        if [b[var((v, v), k)] for k in range(3)] != [g[v], 0, g[v]]: ok_fixed = False
say("every such solution has x(p,c) = g(p), i.e. the previous value read in the X basis:", ok_x)
say("swap-fixed configurations (v,v) are sent to g(v)*(1,0,1):", ok_fixed,
    "-> |r|^2 = 2 g(v)^2 <= 1, so |g| <= 1/sqrt(2)")
say("rational witness g0=1/2, g1=-1/2, y=1/2 (Bloch vectors and squared norms):")
g0, g1, y = Fr(1, 2), Fr(-1, 2), Fr(1, 2)
W = {(0, 0): (g0, 0, g0), (1, 1): (g1, 0, g1), (0, 1): (g0, y, g1), (1, 0): (g1, -y, g0)}
for x, r in W.items():
    rr = [Fr(t) for t in r]
    RHr = [sum(RH[k][j]*rr[j] for j in range(3)) for k in range(3)]
    say(f"  r{x} = {tuple(str(t) for t in rr)}, |r|^2 = {sum(t*t for t in rr)}, covariance r[swap x] = R_H r[x]:",
        [Fr(t) for t in W[swap(x)]] == RHr)

say("\n== node 3: the previous value hidden from the read (E(p,c) = e(c)) + swap covariance, any lift")
for name, U, anti in [("H", Hm, False), ("HY", umul(Hm, (Y, 1)), False), ("X", (X, 1), False),
                      ("H.K", Hm, True)]:
    rows = constraints(swap, bloch_rot(U, anti))
    for c in (0, 1):
        for k in range(3):
            row = [Fr(0)]*12; row[var((0, c), k)] = 1; row[var((1, c), k)] = -1; rows.append(row)
    B = nullspace(rows, 12)
    nonconst = any(any(b[var(x, k)] != b[var((0, 0), k)] for x in CONF for k in range(3)) for b in B)
    say(f"swap->{name}: solution dim {len(B)}, some non-constant solution: {nonconst}")

print("\n".join(out))
