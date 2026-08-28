#!/usr/bin/env python3
# source_lift_probes.py — b434 (2026-08-27)
#
# Where b405's finite-layer source non-identifiability actually lives.
#
# THE CLAIM UNDER TEST. b405 §5 offers a finite operational control for H-source-lift, in the
# framework's own fixed-basis language rather than in lattice gauge theory: U_theta = diag(1,
# e^{i theta}) has |U_theta^k|^2 = I at every integer horizon, so the whole passive law is
# independent of theta, while one coherent source loop R^{-1} U_theta R has a response that varies
# continuously with theta. b405 reads this as showing that the obstruction "already exists at the
# finite Q_fb layer". This file tests whether it exists there GENERICALLY.
#
# TWO FREEDOMS THAT MUST BE SEPARATED, because b405 §5 runs them together.
#   (A) The REPHASING GAUGE, X -> D X D^dag for diagonal unitary D. Every fixed-basis modulus
#       |<j|X|i>| is invariant under it, so it moves the passive law, the intervention's own
#       statistics and the coherent response TOGETHER. On its own it predicts nothing.
#   (B) GENUINE non-identifiability: two dynamics with the same passive law that are NOT related by
#       shift x rephasing x the antiunitary conjugate. b405's theta-family is of this kind -- no
#       diagonal D conjugates diag(0,0) to diag(0,theta), since diagonals commute -- and SL4
#       reproduces it exactly.
# The question (B) leaves open is where such families live. The phase-locking lemma (Main §3.4)
# excludes them at generic H under (G1)-(G3); b405's witness has V = I, so G3 fails at it.
#
# WHAT IS ACTUALLY MEASURED. The relative phase between the dynamics and the intervention is the
# thing at issue: the intervention generator has to be reconstructed from data too, and its own
# fixed-basis law is blind to its own rephasing (SL3). So the honest question is whether the JOINT
# source-loop data
#
#     p_{k,m}[j][i] = | <j| (R^m)^dag U^k (R^m) |i> |^2
#
# resolves R -> D R D^dag. Write S = R^m; the tangent to that family is dS = i(E_c o S) with
# E_c[a][b] = delta_{ac} - delta_{bc} (the same coboundary generators the phase-locking gauge uses),
# and the Jacobian rows are d_c p = 2 Re( conj(M) d_c M ), M = S^dag U^k S.
#
# THE ARGUMENT, and what each step needs:
#   1. rank <= n-1 IDENTICALLY. sum_c E_c = 0 pointwise, so the Jacobian rows sum to zero: the
#      uniform direction is D = e^{i phi} I, which acts trivially. SL2 checks the identity rather
#      than resting on the derivation.
#   2. U(n) x U(n) is a connected real algebraic group, hence IRREDUCIBLE, and the Jacobian entries
#      are polynomial in the real coordinates of (U, R).
#   3. rank is LOWER semi-continuous: {rank >= r} is open, so {rank <= n-2} is closed.
#   4. ONE EXACT WITNESS with rank = n-1 therefore confines the deficient locus to a proper closed
#      algebraic subset -- empty interior, Haar measure zero.
#   This is b433's argument with the semicontinuity running the other way: there an upper bound was
#   identical and a witness pinned the kernel from above; here an upper bound is identical and a
#   witness pins the rank from below. The METHOD transfers; no result of b433's is assumed here.
#
# THE ARITHMETIC. p = 1000003 is 3 mod 4, so x^2+1 is irreducible mod p and GF(p^2) = GF(p)[i];
# Gaussian rationals embed with i -> iota and re/im are genuine GF(p)-coordinates, which is what
# |z|^2 = z conj(z) and Re(.) need. (For p = 1 mod 4 this fails outright.) Soundness runs one way:
# rank_p <= rank_Q, so rank_p = n-1 forces rank_Q >= n-1, and step 1 gives rank_Q <= n-1; hence
# rank_Q = n-1 EXACTLY. A mod-p rank can fail to certify, but it cannot certify falsely.
#
# b435 (2026-08-27) EXTENDS THE STRATIFICATION to the framework's own idealized layer (SL7-SL9).
# The substratum's realization is neither generic nor coherently probed: the dynamics is a
# PERMUTATION unitary and the native instruments are PERMUTATIONS. Stratifying the rank by layer:
#
#     dynamics \ probes      permutation      real rotation       complex generic
#     permutation, c cycles   0 (all orders)   0 (first order)     n - c
#     diagonal                0                --                  0        (SL4)
#     generic                 --               n - 1               n - 1    (SL1)
#
#   - SL7: permutation dynamics probed by permutation instruments yields 0/1 tables invariant
#     under EVERY phase decoration, not just rephasings. The native instrument set carries no
#     coherent source information at any order. (The intervened form of the |U|^p
#     exponent-blindness recorded at check 6 of equivalence_recovery_probes.py.)
#   - SL8, THE CYCLE LAW: for permutation dynamics with c cycles and a generic coherent probe,
#     rank = n - c exactly. Upper bound: a diagonal D constant on the cycles commutes with the
#     permutation, so data(U, D R D^dag) = |D (R^dag U^k R) D^dag|^2 = data(U, R) -- an EXACT
#     symmetry, all orders; the c cycle-indicator directions are null identically, generalizing
#     SL2's global phase (a generic U has diagonal commutant = scalars, c = 1; a diagonal U has
#     all of them, c = n, which is SL4's collapse). Lower bound: one witness per shape, mod p.
#     A control shows the law tracks the DIAGONAL COMMUTANT and not the spectrum: a unitary with
#     a repeated eigenvalue but generic eigenvectors still has rank n - 1.
#     So the SINGLE-CYCLE permutation -- the framework's idealized hidden dynamics, with its
#     equally spaced eigenphases -- has NO deficit: G2 failure costs nothing for source-phase
#     identifiability, and each extra ergodic component costs exactly one direction, the relative
#     phase between dynamically disconnected sectors.
#   - SL9: if dynamics AND probe are both real, every Jacobian entry vanishes IDENTICALLY --
#     M is real, dM = i(E o S)-driven is purely imaginary, so 2 Re(conj(M) dM) = 0 entry by
#     entry. Real-amplitude superpositions are first-order blind to the relative phase;
#     sensitivity returns at second order, and one complex side restores rank n - 1.
#
# Together: the source-lift deficiency of the native layer lives ENTIRELY in the instruments, not
# in the idealized dynamics. What the lift needs is complex-phase-bearing coherent probes; it does
# not need generic dynamics, non-degenerate gaps, or anything beyond the single-cycle structure
# the framework already has.
#
# WHY EXACT AND NOT FLOATING POINT, beyond the usual reason. The rank being certified is a rank of
# a Jacobian whose true value at the interesting witnesses is ZERO. A floating-point second
# difference there returns entries of order 1e-10, and any rank test taken relative to the largest
# singular value then reports FULL rank on a matrix that is identically zero. A float scratch pass
# written while preparing this file did exactly that, and reported rank n at n = 2, 3, 4 for the
# diagonal dynamics whose rank is 0. Over GF(p^2) the zero is a zero.
#
# SCOPE, stated here because it is the whole difficulty of reading this round. What is tested is
# b405 §5 ALONE -- its finite operational control. b405 §3-§4 make a different claim, about a
# kappa-family of plaquette-dressed lattice operators with identical zero-source action and
# different second source derivative; that is a statement about needing a LIFT (a second derivative
# cannot be read off data at zero source), not about identifiability failing, and NOTHING here
# touches it. b426 recorded that the abstract operational setting and the lattice setting have no
# bridge; this file does not supply one and must not be read as one.
#
# Self-contained by the convention of this directory: none of its thirty probes imports another,
# which is what lets each be run alone from an archived copy.
import sys
import time
from fractions import Fraction as F

P = 1000003
assert P % 4 == 3, 'need p = 3 mod 4 so that GF(p^2) = GF(p)[i] and re/im are coordinates'
CHECKS = []

# ---------------------------------------------------------------- GF(p^2) = GF(p)[i]
def cadd(x, y): return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)
def csub(x, y): return ((x[0] - y[0]) % P, (x[1] - y[1]) % P)
def cmul(x, y): return ((x[0]*y[0] - x[1]*y[1]) % P, (x[0]*y[1] + x[1]*y[0]) % P)
def cconj(x):   return (x[0], (-x[1]) % P)
def cscale(k, x): return ((k * x[0]) % P, (k * x[1]) % P)
ZERO, ONE, IOTA = (0, 0), (1, 0), (0, 1)

def fr(q):
    return (int(q.numerator) * pow(int(q.denominator), P - 2, P)) % P

def gr(re, im=F(0)):
    return (fr(re), fr(im))

def eye(n):
    return [[ONE if r == c else ZERO for c in range(n)] for r in range(n)]

def matmul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    out = [[ZERO] * m for _ in range(n)]
    for r in range(n):
        Ar, Or = A[r], out[r]
        for t in range(k):
            a = Ar[t]
            if a == ZERO:
                continue
            Bt = B[t]
            for c in range(m):
                Or[c] = cadd(Or[c], cmul(a, Bt[c]))
    return out

def dagger(A):
    n = len(A)
    return [[cconj(A[c][r]) for c in range(n)] for r in range(n)]

def mpow(A, k):
    out = eye(len(A))
    for _ in range(k):
        out = matmul(out, A)
    return out

def modsq(A):
    """The fixed-basis table |A_ij|^2, as GF(p) scalars. This is what an observer reads."""
    return [[cmul(x, cconj(x))[0] for x in row] for row in A]

# Pythagorean rotations and unit-modulus phases over Q(i); the offsets make U and R independent.
PYTH = [(F(3,5), F(4,5)), (F(5,13), F(12,13)), (F(8,17), F(15,17)),
        (F(20,29), F(21,29)), (F(7,25), F(24,25)), (F(9,41), F(40,41))]
PHASE = [(F(3,5), F(4,5)), (F(5,13), F(12,13)), (F(8,17), F(15,17)), (F(20,29), F(21,29)),
         (F(7,25), F(24,25)), (F(9,41), F(40,41)), (F(28,53), F(45,53)), (F(33,65), F(56,65))]

def build_U(n, off):
    """An explicit unitary over Q(i). `off` picks a different member of the same family."""
    V = eye(n)
    k = off
    for p_ in range(n):
        for q in range(p_ + 1, n):
            c, s = PYTH[k % len(PYTH)]; k += 1
            G = eye(n)
            G[p_][p_] = gr(c); G[q][q] = gr(c)
            G[p_][q] = gr(F(0), s); G[q][p_] = gr(F(0), s)
            V = matmul(V, G)
    Dg = eye(n)
    for i in range(n):
        re, im = PHASE[(i + off) % len(PHASE)]
        Dg[i][i] = gr(re, im)
    return matmul(V, Dg)

def diag_phase(n, off):
    """A diagonal unitary over Q(i) — a concrete member of the rephasing gauge group."""
    D = eye(n)
    for i in range(n):
        re, im = PHASE[(i + off) % len(PHASE)]
        D[i][i] = gr(re, im)
    return D

def conj_by(D, A):
    return matmul(matmul(D, A), dagger(D))

def rank_mod_p(rows, ncols):
    rows = [r[:] for r in rows]; r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] % P), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], P - 2, P)
        rows[r] = [(x * inv) % P for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % P:
                f = rows[i][c]
                rows[i] = [(a - f * b) % P for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r

# ---------------------------------------------------------------- the Jacobian
def hadam(E, A, n):
    """E o A with E an integer matrix: the coboundary generator acting entrywise."""
    return [[cscale(E[r][c] % P, A[r][c]) for c in range(n)] for r in range(n)]

def jacobian(U, R, n, horizons, strengths):
    """Rows = the n relative-phase directions; columns = the joint source-loop data.

    R -> D R D^dag with D = diag(e^{i alpha}) gives, for S = R^m, dS = i (E_c o S) and likewise
    d(S^dag) = i (E_c o S^dag), since S^dag transforms the same way. Then M = S^dag U^k S and the
    observable is |M_ji|^2, whose derivative is 2 Re( conj(M) dM ).
    """
    rows = [[] for _ in range(n)]
    for m in strengths:
        S = mpow(R, m)
        Sd = dagger(S)
        for k in horizons:
            Uk = mpow(U, k)
            M = matmul(matmul(Sd, Uk), S)
            for c in range(n):
                E = [[(1 if r == c else 0) - (1 if q == c else 0) for q in range(n)]
                     for r in range(n)]
                dS = [[cmul(IOTA, x) for x in row] for row in hadam(E, S, n)]
                dSd = [[cmul(IOTA, x) for x in row] for row in hadam(E, Sd, n)]
                dM = [[cadd(a, b) for a, b in zip(r1, r2)] for r1, r2 in
                      zip(matmul(matmul(dSd, Uk), S), matmul(matmul(Sd, Uk), dS))]
                for r in range(n):
                    for q in range(n):
                        rows[c].append((2 * cmul(cconj(M[r][q]), dM[r][q])[0]) % P)
    return rows

def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)

# ---------------------------------------------------------------- SL1  the witnesses
SHAPES = (2, 3, 4, 5, 6)
print("SL1  at an explicit (U, R) over Q(i), the joint data resolves EVERY relative phase")
rows_out, t0 = [], time.time()
for n in SHAPES:
    U, R = build_U(n, 0), build_U(n, 3)
    assert matmul(dagger(U), U) == eye(n) and matmul(dagger(R), R) == eye(n), 'not unitary'
    J = jacobian(U, R, n, range(1, 2 * n + 1), (1, 2))
    rk = rank_mod_p(J, len(J[0]))
    rows_out.append((n, len(J[0]), rk))
    print(f"        n={n}  columns={len(J[0]):5d}  rank = {rk:2d}  n-1 = {n-1:2d}  "
          f"{'CERTIFIED' if rk == n - 1 else 'MISMATCH'}", flush=True)
check("SL1", all(rk == n - 1 for n, _, rk in rows_out),
      f"at n = {list(SHAPES)} the joint source-loop data resolves exactly n-1 relative-phase "
      f"directions, in {time.time()-t0:.1f} s of exact GF(p^2) arithmetic. With rank_p <= rank_Q "
      "this bounds the rational rank from BELOW, and SL2's identity bounds it from above, so these "
      "are exact rational statements rather than numerical ones")

# ---------------------------------------------------------------- SL2  the identity above
print("SL2  the uniform direction is exactly null, so rank <= n-1 everywhere")
ok2 = True
for n in SHAPES:
    U, R = build_U(n, 0), build_U(n, 3)
    J = jacobian(U, R, n, range(1, 2 * n + 1), (1, 2))
    ok2 &= all(sum(J[c][e] for c in range(n)) % P == 0 for e in range(len(J[0])))
check("SL2", ok2,
      "sum_c E_c = 0 pointwise, so the n Jacobian rows sum to zero at every shape: the uniform "
      "rephasing is D = e^{i phi} I, which conjugates trivially. This is the bound that makes the "
      "mod-p rank a certificate rather than a measurement — without it a rank of n-1 would say "
      "only that at least n-1 directions are resolved")

# ---------------------------------------------------------------- SL3  each law is blind alone
print("SL3  neither object's own passive law can see its own rephasing")
ok3 = True
for n in SHAPES:
    U, R = build_U(n, 0), build_U(n, 3)
    D = diag_phase(n, 1)
    for k in range(1, 2 * n + 1):
        ok3 &= modsq(mpow(U, k)) == modsq(mpow(conj_by(D, U), k))
        ok3 &= modsq(mpow(R, k)) == modsq(mpow(conj_by(D, R), k))
check("SL3", ok3,
      "|U^k|^2 and |R^k|^2 are unchanged, entry for entry, by X -> D X D^dag at every horizon and "
      "every shape. So the rephasing is a GAUGE of each object separately — which is why SL1 has "
      "to be about the JOINT datum, and why 'describe the intervention in the same gauge as the "
      "dynamics' would beg the question if asserted rather than measured")

# ---------------------------------------------------------------- SL4  b405 §5's own witness
print("SL4  b405 §5's witness, in exact arithmetic")
# U_theta = diag(1, omega) with omega = 3/5 + 4i/5 a Gaussian-rational phase; R the real rotation.
om = gr(F(3, 5), F(4, 5))
Uth = [[ONE, ZERO], [ZERO, om]]
U0 = [[ONE, ZERO], [ZERO, ONE]]
Rot = [[gr(F(3, 5)), gr(F(4, 5))], [gr(F(-4, 5)), gr(F(3, 5))]]
passive_same = all(modsq(mpow(Uth, k)) == modsq(mpow(U0, k)) for k in range(1, 21))
loop = lambda V: modsq(matmul(matmul(dagger(Rot), V), Rot))
response_differs = loop(Uth) != loop(U0)
# G3 asks that no eigenvector overlap vanish. A DIAGONAL unitary is already in its own eigenbasis,
# so its overlap matrix is the identity and EVERY off-diagonal overlap vanishes — G3 fails
# maximally, not marginally. Tested, not asserted: b91's header claimed a check no code performed,
# and this file is not going to repeat that.
is_diagonal = lambda A: all(A[r][c] == ZERO for r in range(len(A)) for c in range(len(A)) if r != c)
# and the collapse is not an n=2 artifact: diagonal dynamics kills the rank at every n, because
# D^dag U D = U for diagonal U and D, so M -> D M D^dag and every |M_ij|^2 is untouched.
diag_ranks = []
for n in (2, 3, 4):
    Ud = eye(n)
    for i in range(n):
        re, im = PHASE[i % len(PHASE)]
        Ud[i][i] = gr(re, im)
    Jd = jacobian(Ud, build_U(n, 3), n, range(1, 2 * n + 1), (1, 2))
    diag_ranks.append((n, rank_mod_p(Jd, len(Jd[0])), is_diagonal(Ud)))
Jw = jacobian(Uth, Rot, 2, range(1, 5), (1, 2))
rk_w = rank_mod_p(Jw, len(Jw[0]))
print(f"        passive law identical through horizon 20: {passive_same}")
print(f"        coherent response differs: {response_differs}")
print(f"        relative phases resolved by the joint data: {rk_w}  (n-1 = 1)")
print(f"        diagonal dynamics at n = 2,3,4: ranks {[r for _, r, _ in diag_ranks]} "
      f"(generic: {[n-1 for n, _, _ in diag_ranks]})")
check("SL4", (passive_same and response_differs and rk_w == 0 and is_diagonal(Uth)
              and all(r == 0 and d for _, r, d in diag_ranks)),
      "b405 §5's ambiguity is real and reproduced exactly — identical passive law through horizon "
      "20, different coherent response. But at that witness the joint data resolves ZERO relative "
      "phases against n-1 at a generic pair, and the collapse is not an n=2 artifact: diagonal "
      "dynamics gives rank 0 at n = 2, 3 and 4. The reason is structural — a diagonal U commutes "
      "with the gauge, so M -> D M D^dag and every |M_ij|^2 is untouched — and it is exactly a "
      "MAXIMAL G3 failure, the overlap matrix of a diagonal unitary being the identity")

# ---------------------------------------------------------------- SL5  how much G3 has to fail
print("SL5  a single vanishing overlap is NOT enough to collapse it")
# V = G12 @ G01 puts exactly one zero in the overlap matrix (row 0, column 2) and leaves the other
# eight entries nonzero; U = V diag(phases) V^dag then has that overlap structure by construction.
def one_zero_overlap():
    n = 3
    G01, G12 = eye(n), eye(n)
    c1, s1 = PYTH[0]
    G01[0][0] = gr(c1); G01[1][1] = gr(c1); G01[0][1] = gr(F(0), s1); G01[1][0] = gr(F(0), s1)
    c2, s2 = PYTH[1]
    G12[1][1] = gr(c2); G12[2][2] = gr(c2); G12[1][2] = gr(F(0), s2); G12[2][1] = gr(F(0), s2)
    V = matmul(G12, G01)
    Dg = eye(n)
    for i in range(n):
        re, im = PHASE[(i + 2) % len(PHASE)]
        Dg[i][i] = gr(re, im)
    return V, matmul(matmul(V, Dg), dagger(V))
Vp, Up = one_zero_overlap()
zeros = [(r, c) for r in range(3) for c in range(3) if Vp[r][c] == ZERO]
Jp = jacobian(Up, build_U(3, 3), 3, range(1, 7), (1, 2))
rk_p = rank_mod_p(Jp, len(Jp[0]))
print(f"        vanishing overlaps: {zeros}   rank = {rk_p}   (n-1 = 2)")
check("SL5", len(zeros) == 1 and rk_p == 2,
      "a unitary whose overlap matrix has exactly ONE zero still resolves all n-1 relative phases. "
      "So 'G3 fails' is too coarse a diagnosis of b405's witness: what collapses the rank is the "
      "MAXIMAL failure of a diagonal dynamics, not any failure. The deficient locus is smaller "
      "than the G3-violating locus, which makes the finite-layer obstruction rarer, not commoner, "
      "than the genericity clause alone would suggest")

# ---------------------------------------------------------------- SL6  what this settles
print("SL6  what the witnesses are for, and what they are not")
# Gated on the checks above: an unconditional True would print PASS beside a red control,
# and this verdict has no computation of its own — it summarizes the ones that do.
check("SL6", all(CHECKS),
      "one exact witness per n is what the genericity argument needs: U(n) x U(n) is a connected "
      "real algebraic group hence irreducible, the Jacobian entries are polynomial on it, rank is "
      "lower semi-continuous, and rank <= n-1 holds identically by SL2. So a single point with "
      "rank = n-1 confines the deficient locus to a proper closed algebraic subset. The argument "
      "is PER SHAPE and nothing here is uniform in n")

# ================================================================ b435: SL7-SL9
def perm_mat(p):
    n = len(p)
    M = [[ZERO] * n for _ in range(n)]
    for i, j in enumerate(p):
        M[j][i] = ONE
    return M

def cycles_of(p):
    n = len(p); seen = [False] * n; out = []
    for i in range(n):
        if not seen[i]:
            c, j = [], i
            while not seen[j]:
                seen[j] = True; c.append(j); j = p[j]
            out.append(c)
    return out

def build_O(n, off):
    """A REAL orthogonal matrix over Q — the coherent-but-phase-free probe of SL9."""
    V = eye(n); k = off
    for p_ in range(n):
        for q in range(p_ + 1, n):
            c, s = PYTH[k % len(PYTH)]; k += 1
            G = eye(n)
            G[p_][p_] = gr(c); G[q][q] = gr(c)
            G[p_][q] = gr(s); G[q][p_] = gr(-s)
            V = matmul(V, G)
    return V

def tables(U, R, horizons, strengths):
    """The joint source-loop data itself, as exact GF(p) tables."""
    out = []
    for m in strengths:
        S = mpow(R, m); Sd = dagger(S)
        for k in horizons:
            out.append(modsq(matmul(matmul(Sd, mpow(U, k)), S)))
    return out

# ---------------------------------------------------------------- SL7  native probes are blind
print("SL7  permutation dynamics probed by permutation instruments: no phase survives")
ok7 = True
for p_dyn, p_probe in (([1, 2, 3, 0], [2, 0, 3, 1]), ([1, 0, 3, 2], [3, 2, 1, 0])):
    n = len(p_dyn)
    Pm, Rp = perm_mat(p_dyn), perm_mat(p_probe)
    tb = tables(Pm, Rp, range(1, 2 * n + 1), (1, 2))
    ok7 &= all(v in (0, 1) for t in tb for row in t for v in row)
    # decorate the dynamics' support with arbitrary unit phases: the tables must not move
    Pph = [[cmul(Pm[r][c], gr(*PHASE[(r + 2 * c) % len(PHASE)])) if Pm[r][c] != ZERO else ZERO
            for c in range(n)] for r in range(n)]
    ok7 &= tables(Pph, Rp, range(1, 2 * n + 1), (1, 2)) == tb
    # and the relative rephasing of the probe: also invisible
    ok7 &= tables(Pm, conj_by(diag_phase(n, 1), Rp), range(1, 2 * n + 1), (1, 2)) == tb
check("SL7", ok7,
      "every table is 0/1 — the classical permutation table — and is unchanged by ARBITRARY unit "
      "phases painted on the dynamics' support, and by any rephasing of the probe. A product of "
      "permutation-supported matrices has one term per entry, so no path ever interferes with "
      "another: the native instrument set carries zero coherent source information at any order. "
      "This is the intervened form of the |U|^p blindness at check 6 of "
      "equivalence_recovery_probes.py")

# ---------------------------------------------------------------- SL8  the cycle law
print("SL8  the cycle law: coherent probes at permutation dynamics resolve exactly n - c phases")
PERMS = ([1, 0], [1, 2, 0], [1, 2, 3, 0], [1, 2, 3, 4, 0], [1, 2, 3, 4, 5, 0],   # single cycles
         [1, 0, 3, 2], [1, 2, 0, 3], [1, 0, 3, 4, 2], [1, 2, 0, 4, 5, 3],        # two cycles
         [1, 0, 3, 2, 5, 4], [1, 2, 0, 4, 3, 6, 5],                              # three cycles
         [0, 1, 2, 3])                                                           # identity: c = n
rows8, t8 = [], time.time()
for p_dyn in PERMS:
    n = len(p_dyn)
    cyc = cycles_of(p_dyn); c = len(cyc)
    Pm, R = perm_mat(p_dyn), build_U(n, 3)
    J = jacobian(Pm, R, n, range(1, 2 * n + 1), (1, 2))
    rk = rank_mod_p(J, len(J[0]))
    # upper bound, exactly: each cycle-indicator direction is null identically...
    null_ok = all(all(sum(J[a][e] for a in cyc_i) % P == 0 for e in range(len(J[0])))
                  for cyc_i in cyc)
    # ...because a D constant on the cycles is an exact symmetry of the data, at finite angle
    D = eye(n)
    for i, cyc_i in enumerate(cyc):
        for a in cyc_i:
            D[a][a] = gr(*PHASE[i % len(PHASE)])
    inv_ok = (tables(Pm, conj_by(D, R), range(1, 2 * n + 1), (1, 2))
              == tables(Pm, R, range(1, 2 * n + 1), (1, 2)))
    rows8.append((n, c, rk, null_ok, inv_ok))
    print(f"        n={n}  cycles={c}  rank = {rk}  n-c = {n - c}  "
          f"{'CERTIFIED' if rk == n - c and null_ok and inv_ok else 'MISMATCH'}", flush=True)
# the control that pins the mechanism: repeated EIGENVALUE, generic eigenvectors — still full rank
Vd = build_U(4, 5)
Dg = eye(4)
for i, ph in enumerate((0, 0, 1, 2)):        # the first eigenphase REPEATED
    Dg[i][i] = gr(*PHASE[ph])
Udeg = matmul(matmul(Vd, Dg), dagger(Vd))
Jdeg = jacobian(Udeg, build_U(4, 2), 4, range(1, 9), (1, 2))
rk_deg = rank_mod_p(Jdeg, len(Jdeg[0]))
print(f"        control: repeated eigenvalue, generic eigenvectors  rank = {rk_deg}  (n-1 = 3)")
check("SL8", all(rk == n - c and no and io for n, c, rk, no, io in rows8) and rk_deg == 3,
      f"rank = n - c at all {len(PERMS)} permutations in {time.time()-t8:.1f} s: the diagonal D "
      "constant on the cycles commutes with the dynamics, so the c cycle-indicator directions are "
      "an exact symmetry (checked at finite angle, not only infinitesimally) — generalizing SL2 "
      "(generic U: diagonal commutant = scalars, c = 1) and SL4 (diagonal U: everything commutes, "
      "c = n). The control shows the law tracks the diagonal COMMUTANT, not the spectrum: a "
      "repeated eigenvalue with generic eigenvectors still gives n-1. So the SINGLE-CYCLE "
      "permutation — the idealized hidden dynamics, equally spaced eigenphases and all — has NO "
      "deficit, and each extra ergodic component costs exactly the relative phase between "
      "dynamically disconnected sectors")

# ---------------------------------------------------------------- SL9  real probes at first order
print("SL9  a real probe of a real dynamics reads nothing at first order")
ok_zero = True
for n in (3, 4):
    Jr = jacobian(build_O(n, 0), build_O(n, 3), n, range(1, 2 * n + 1), (1, 2))
    ok_zero &= all(v % P == 0 for row in Jr for v in row)
# ...but only at first order: a finite rephasing moves the tables
O1, O2 = build_O(3, 0), build_O(3, 3)
moved = (tables(O1, conj_by(diag_phase(3, 1), O2), range(1, 7), (1, 2))
         != tables(O1, O2, range(1, 7), (1, 2)))
# one complex side restores everything: complex dynamics with the REAL probe
ranks9 = []
for n in (3, 4):
    Jc = jacobian(build_U(n, 0), build_O(n, 3), n, range(1, 2 * n + 1), (1, 2))
    ranks9.append(rank_mod_p(Jc, len(Jc[0])))
print(f"        real-real Jacobian identically zero at n = 3, 4: {ok_zero};  finite rephasing "
      f"still moves the tables: {moved}")
print(f"        complex dynamics, real probe: ranks {ranks9}  (n-1 = [2, 3])")
check("SL9", ok_zero and moved and ranks9 == [2, 3],
      "with dynamics and probe both real, every Jacobian entry is identically zero — M is real "
      "and dM = i(E o S)-driven is purely imaginary, so 2 Re(conj(M) dM) vanishes entry by entry "
      "— while a finite rephasing still moves the tables, so the blindness is first-order only, "
      "not an invariance. One complex side restores rank n-1: real dynamics with a complex probe "
      "is SL8's single-cycle row, and complex dynamics with a real probe is certified here. "
      "Coherent probing therefore means COMPLEX-phase-bearing probing; real-amplitude "
      "superpositions do not linearly resolve the relative phase")

print()
if not all(CHECKS):
    print("     [scope] VERDICT WITHHELD: a control above failed, so the statement below is not")
    print("     asserted. Fix the failing check before reading any conclusion from this run.")
else:
    print("     [scope] Settled: b405 §5's finite operational control does NOT exhibit a generic")
    print("     obstruction. At a generic (U, R) the joint coherent source-loop data resolves every")
    print("     relative phase between dynamics and intervention; at b405's own witness it resolves")
    print("     none. The collapse needs the dynamics to be DIAGONAL — a maximal G3 failure — and a")
    print("     single vanishing overlap does not produce it (SL5), so the deficient locus is smaller")
    print("     than the G3-violating one. The finite layer supplies no support for a source-lift")
    print("     obstruction that survives genericity.")
    print("     Also settled (b435): the deficiency of the NATIVE layer lives entirely in the")
    print("     instruments. Permutation probes are blind at every order (SL7); real probes are blind")
    print("     at first order (SL9); and once the probe is complex, permutation dynamics with c")
    print("     cycles resolves exactly n - c phases (SL8) — so the framework's single-cycle idealized")
    print("     dynamics has NO deficit, its equally spaced eigenphases notwithstanding. The unresolved")
    print("     directions are always the diagonal commutant of the dynamics: scalars generically,")
    print("     cycle indicators for permutations, everything for a diagonal U.")
    print("     NOT settled, and NOT touched: b405 §3-§4, the lattice kappa-family. That is a claim")
    print("     about needing a lift — a second source derivative cannot be read off zero-source data")
    print("     — not about identifiability failing, and b426 recorded that the lattice and operational")
    print("     settings have no bridge. Nothing here bridges them. Also not claimed: anything uniform")
    print("     in n, and anything about the antiunitary conjugate, which remains a genuine twofold")
    print("     ambiguity of transition data (Main §3.4) and is untouched by any rank computed here.")
print()
print("source_lift_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
