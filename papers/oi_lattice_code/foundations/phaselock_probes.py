#!/usr/bin/env python3
# phaselock_probes.py — b91 (2026-08-13), completed b433 (2026-08-27)
#
# Exact certificate for the ancilla-marginal phase-locking lemma (Main §3.4), and the witnesses
# that turn its genericity statement into a proof.
#
# THE STATEMENT. Fix n and m_a, D = n*m_a. Let F be the set of families (M_1..M_n) of orthogonal
# projectors on C^D, each of rank m_a, summing to I. For real antisymmetric theta put
# K_i = i(theta o M_i) (Hadamard) and
#
#     L(theta) = ( M_i K_i M_i , Q_i K_i Q_i )_i ,      Q_i = I - M_i.
#
# The coboundaries B = {theta_ab = alpha_a - alpha_b}, of dimension D-1, lie in ker L for EVERY
# family (Main §3.4, by telescoping). The claim is that generically they exhaust it.
#
# THE PROOF, and what each step needs:
#   1. dim ker L >= D-1 everywhere, since B is always in the kernel.
#   2. F is IRREDUCIBLE. By the spectral theorem F is exactly the orbit {V^H P V : V in U(D)} of
#      the base family P of block projectors -- the whole of F, not a subset. U(D) is a connected
#      real algebraic group, hence irreducible, and the orbit map is polynomial in the real
#      coordinates of V, so its image is irreducible.
#   3. dim ker L is UPPER SEMI-CONTINUOUS on F: the entries of L are polynomial in the family, and
#      {rank <= r} is closed (vanishing of all (r+1)-minors).
#   4. ONE EXACT WITNESS with dim ker L = D-1 therefore confines {dim ker L > D-1} to a proper
#      closed algebraic subset of F. Being proper and closed in an irreducible variety, it has
#      empty interior and measure zero for the pushforward of Haar measure on U(D).
#   Hence ker L = B off a proper closed algebraic subset -- for generic families, at each shape.
#
#   The freedom V -> V*Diag(d) sends M -> D^H M D, an entrywise phase change that commutes with
#   theta o (.) because D is diagonal; so K -> D^H K D, the constraint set is preserved, and
#   dim ker L descends to U(D)/T. That is why genericity in the family is genericity in the
#   dilated Hamiltonian's eigenbasis.
#
# LIMIT, stated rather than glossed: the argument is PER SHAPE. Each (n, m_a) needs its own
# witness, and the witnesses below cover seven shapes. Nothing here is uniform in D.
#
# THE ARITHMETIC, and why mod p is legitimate here. p = 1000003 is 3 mod 4, so x^2+1 is
# irreducible mod p and GF(p^2) = GF(p)[i]; Gaussian rationals embed with i -> iota and the
# real/imaginary parts the constraint needs are exactly the GF(p)-coordinates. (For p = 1 mod 4
# this would fail: re/im would not be well defined.) Soundness: rank_p <= rank_Q, so
# ker_p >= ker_Q; step 1 gives ker_Q >= D-1; so ker_p == D-1 forces ker_Q == D-1 EXACTLY. A mod-p
# rank can fail to certify, but it cannot certify falsely. This replaces b91's sympy computation,
# which could not run in the gate (CI installs numpy and scipy only) and covered two shapes by
# default in 27 s; the port covers seven in under five seconds using the standard library alone.
#
# THE JOIN TO THE PROSE. Main §3.4 writes the constraint as the triple sum
# sum_b (theta_ab + theta_bc) M_i[a,b] M_i[b,c] = theta_ac M_i[a,c]; this file computes with the
# sandwiched pair above. The two agree -- delta(M^2) = delta(M) reads K M + M K = K, and
# sandwiching by M and by Q gives M K M = 0 and Q K Q = 0 while the cross terms are identities --
# but PL2 CHECKS the agreement at every shape rather than resting on that derivation. b91's header
# asserted the same equivalence and no code in it tested one.
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
ZERO, ONE = (0, 0), (1, 0)

def fr(q):
    return (int(q.numerator) * pow(int(q.denominator), P - 2, P)) % P

def gr(re, im=F(0)):
    return (fr(re), fr(im))

def eye(D):
    return [[ONE if r == c else ZERO for c in range(D)] for r in range(D)]

def matmul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    out = [[ZERO] * m for _ in range(n)]
    for r in range(n):
        Ar = A[r]; Or = out[r]
        for t in range(k):
            a = Ar[t]
            if a == ZERO:
                continue
            Bt = B[t]
            for c in range(m):
                Or[c] = cadd(Or[c], cmul(a, Bt[c]))
    return out

def dagger(A):
    D = len(A)
    return [[cconj(A[c][r]) for c in range(D)] for r in range(D)]

# Pythagorean rotations and unit-modulus phases, all over Q(i) — b91's explicit witness family.
PYTH = [(F(3,5), F(4,5)), (F(5,13), F(12,13)), (F(8,17), F(15,17)),
        (F(20,29), F(21,29)), (F(7,25), F(24,25)), (F(9,41), F(40,41))]
PHASE = [(F(3,5), F(4,5)), (F(5,13), F(12,13)), (F(8,17), F(15,17)), (F(20,29), F(21,29)),
         (F(7,25), F(24,25)), (F(9,41), F(40,41)), (F(28,53), F(45,53)), (F(33,65), F(56,65))]

def build_V(D):
    V = eye(D); k = 0
    for p_ in range(D):
        for q in range(p_ + 1, D):
            c, s = PYTH[k % len(PYTH)]; k += 1
            G = eye(D)
            G[p_][p_] = gr(c); G[q][q] = gr(c)
            G[p_][q] = gr(F(0), s); G[q][p_] = gr(F(0), s)
            V = matmul(V, G)
    Dg = eye(D)
    for i in range(D):
        re, im = PHASE[i % len(PHASE)]
        Dg[i][i] = gr(re, im)
    return matmul(V, Dg)

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

def projector_family(n, ma):
    """The witness family: an explicit U(D) rotation of the block projectors."""
    D = n * ma
    V = build_V(D)
    Vh = dagger(V)
    assert matmul(Vh, V) == eye(D), 'V is not unitary — the witness must lie in F'
    out = []
    for i in range(n):
        Pi = [[ONE if (r == c and i * ma <= r < (i + 1) * ma) else ZERO for c in range(D)]
              for r in range(D)]
        out.append(matmul(matmul(Vh, Pi), V))
    return D, out

def khat(th, M, D):
    """K = i (theta o M), the linearised per-pair rephasing."""
    return [[cmul((0, 1), ((th[r][c] * M[r][c][0]) % P, (th[r][c] * M[r][c][1]) % P))
             for c in range(D)] for r in range(D)]

def columns(Ms, D, idx, form):
    """One column per basis theta, entries = the constraint's real coordinates.

    form='reform': the pair (M_i K_i M_i, Q_i K_i Q_i) — the system this probe certifies.
    form='triple': the sum as WRITTEN in Main §3.4,
                   sum_b (theta_ab + theta_bc) M_i[a,b] M_i[b,c] - theta_ac M_i[a,c].
    The two are equivalent -- delta(M^2) = delta(M) reads KM + MK = K, and sandwiching by M
    and by Q gives MKM = 0 and QKQ = 0 while the cross terms are identities -- but the
    equivalence is CHECKED below rather than asserted, because it is the join between the
    written constraint and the computed one.
    """
    cols = []
    for (a0, b0) in idx:
        th = [[0] * D for _ in range(D)]
        th[a0][b0] = 1; th[b0][a0] = -1
        vec = []
        for M in Ms:
            if form == 'reform':
                K = khat(th, M, D)
                Q = [[csub(ONE if r == c else ZERO, M[r][c]) for c in range(D)]
                     for r in range(D)]
                mats = (matmul(matmul(M, K), M), matmul(matmul(Q, K), Q))
            else:
                E = [[ZERO] * D for _ in range(D)]
                for a in range(D):
                    for c in range(D):
                        acc = ZERO
                        for b in range(D):
                            t = th[a][b] + th[b][c]
                            if t:
                                term = cmul(M[a][b], M[b][c])
                                acc = cadd(acc, (t * term[0] % P, t * term[1] % P))
                        t = th[a][c]
                        E[a][c] = csub(acc, (t * M[a][c][0] % P, t * M[a][c][1] % P))
                mats = (E,)
            for X in mats:
                for r in range(D):
                    for c in range(D):
                        vec.append(X[r][c][0]); vec.append(X[r][c][1])
        cols.append(vec)
    return cols

def as_rows(cols, npar):
    return [[cols[j][e] for j in range(npar)] for e in range(len(cols[0]))]

def certificate(n, ma):
    """Returns (D, #params, dim ker_p, coboundaries-in-kernel, written-form-agrees)."""
    D, Ms = projector_family(n, ma)
    idx = {}
    k = 0
    for a in range(D):
        for b in range(a + 1, D):
            idx[(a, b)] = k; k += 1
    npar = len(idx)
    A = as_rows(columns(Ms, D, idx, 'reform'), npar)
    kd = npar - rank_mod_p(A, npar)
    # The written triple sum must cut out the SAME subspace: equal ranks separately and
    # stacked is equality of row spaces, hence of kernels.
    T = as_rows(columns(Ms, D, idx, 'triple'), npar)
    ra, rt = rank_mod_p(A, npar), rank_mod_p(T, npar)
    ok_same = (ra == rt == rank_mod_p(A + T, npar))
    cob = []
    for aa in range(D):
        v = [0] * npar
        for (a, b), j in idx.items():
            v[j] = (1 if a == aa else 0) - (1 if b == aa else 0)
        cob.append(v)
    ok_cob = all(sum(row[j] * v[j] for j in range(npar)) % P == 0
                 for row in A + T for v in cob)
    return D, npar, kd, ok_cob, ok_same

def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)

def verdict(label, ok, msg):
    """A TERMINAL SUMMARY: it has no computation of its own, it only states what the checks above
    have established. Gating the label is not enough -- check() prints its msg whatever the label
    says, so a bare gate renders the entire verdict text under a FAIL heading, which is the thing
    the gate exists to prevent. The message itself is therefore withheld when a control has failed."""
    check(label, ok, msg if ok else
          "WITHHELD — a prerequisite control above failed, so this summary is not asserted")

# ---------------------------------------------------------------- the witnesses
SHAPES = ((2, 2), (3, 2), (2, 3), (4, 2), (2, 4), (3, 3), (3, 4))
print("PL1  exact witnesses: at an explicit V over Q(i), the kernel IS the coboundary space")
rows, t0 = [], time.time()
for n, ma in SHAPES:
    D, npar, kd, okc, oks = certificate(n, ma)
    rows.append((n, ma, D, npar, kd, okc, oks))
    print(f"        (n,m_a)=({n},{ma})  D={D:3d}  params={npar:3d}  ker = {kd:3d}  "
          f"coboundary dim = {D-1:3d}  {'CERTIFIED' if kd == D - 1 and okc else 'MISMATCH'}",
          flush=True)
check("PL1", all(kd == D - 1 and okc for _, _, D, _, kd, okc, _ in rows),
      f"at all {len(SHAPES)} shapes the coboundaries lie in the kernel and the kernel has "
      f"dimension exactly D-1, in {time.time()-t0:.1f} s of exact GF(p^2) arithmetic. Since "
      "rank_p <= rank_Q the mod-p kernel bounds the rational one from ABOVE, and the coboundary "
      "bounds it from below, so these are exact rational statements, not numerical ones")

print("PL2  the computed system is the one the manuscript writes down")
check("PL2", all(oks for *_, oks in rows),
      "the triple sum of Main §3.4, sum_b (theta_ab + theta_bc) M_i[a,b] M_i[b,c] = theta_ac "
      "M_i[a,c], and the sandwiched pair (M_i K_i M_i, Q_i K_i Q_i) have the same row space at "
      "every shape, hence the same kernel. b91's header claimed this equivalence; no code in it "
      "checked it, so a reformulation error would have gone unseen")

print("PL3  the shapes the manuscript cites are covered")
cited = {(3, 4), (2, 3), (4, 2), (3, 3), (2, 4)}
check("PL3", cited <= set(SHAPES),
      f"Main §3.4 cites (n,m_a) = {sorted(cited)} as verified; all are certified here in exact "
      "arithmetic, together with (2,2) and (3,2). b91's sympy version ran (2,2) and (3,2) by "
      "default and (2,3) behind an environment flag — one of the five cited shapes, at most")

print("PL4  what the witnesses are for")
# Gated on the checks above: an unconditional True would print PASS beside a red control,
# and this verdict has no computation of its own — it summarizes the ones that do.
verdict("PL4", all(CHECKS),
      "one exact witness per shape is what the genericity argument needs: the families of n "
      "rank-m_a projectors summing to I form a single U(D) orbit, hence an irreducible variety; "
      "dim ker L is upper semi-continuous on it; the coboundary is in the kernel everywhere. So a "
      "single point with dim ker = D-1 confines the excess locus to a proper closed algebraic "
      "subset. The argument is PER SHAPE and nothing here is uniform in D")

print()
if not all(CHECKS):
    print("     [scope] VERDICT WITHHELD: a control above failed, so the statement below is not")
    print("     asserted. Fix the failing check before reading any conclusion from this run.")
else:
    print("     [scope] Proved: for each shape above, generic families have ker L = coboundaries, so")
    print("     the pair-phase gauge reduces to the diagonal one and the marginal data fix the")
    print("     dilated Hamiltonian and the configuration projectors up to the stated freedoms.")
    print("     NOT proved: any statement uniform in D. Each shape rests on its own witness.")
print()
print("phaselock_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
