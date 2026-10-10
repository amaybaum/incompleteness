#!/usr/bin/env python3
"""Independent exact check of two countermodels for OIBridge.FourCopy.kt4_forward_ie1.

  M_cl : K = int(Q3) u (SEP + cnot(SEP)) at all four pairs, N = cnot, locals = id
  M_max: K = maxCone (eball 3)            at all four pairs, N = cnot, locals = id

Every definition is transcribed here directly from the Lean sources
(CompositeDimension, K2Guard, FourCopyDefs, FourCopyCore, FourCopyHeadline, EffectSpace,
KInfFoundations, TransitiveBody, Mathlib finProdFinEquiv).  No code is shared with any other
checker.  Arithmetic is exact: fractions.Fraction, the exact Gaussian-rational class `C` below,
python ints, and sympy for polynomial identities.  No floating point enters any decision.
Run:  python3 -I indep_check.py
"""
import itertools
import random
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

T0 = time.time()
CHECKS = []


def rec(tag, cond, info=''):
    cond = bool(cond)
    CHECKS.append((tag, cond))
    print(('  ok   ' if cond else '  FAIL ') + tag + (('  [' + str(info) + ']') if info != '' else ''),
          flush=True)
    return cond


def passed(*prefixes):
    """every prefix must match at least one recorded check, and every matching check must pass."""
    for p in prefixes:
        if not any(t.startswith(p) for t, _ in CHECKS):
            return False
    return all(c for t, c in CHECKS if any(t.startswith(p) for p in prefixes))


def hdr(s):
    print('\n== %s  (t=%.1fs)' % (s, time.time() - T0), flush=True)


R3, R4 = range(3), range(4)

# =====================================================================================
# §1  Transcription of the Lean definitions
# =====================================================================================
# CompositeDimension: HVec d = Fin (d+1) -> R ; W d = Fin (d+1) -> Fin (d+1) -> R (index 0 = unit)


def hom(x):                                   # hom x = vecCons 1 x
    return [1] + list(x)


def homMap(N, v):                             # vecCons (v 0) (N (vecTail v)); N = matrix of toLin'
    t = list(v[1:])
    return [v[0]] + [sum(N[i][j] * t[j] for j in R3) for i in R3]


def prodState(x, y):                          # fun mu nu => hom x mu * hom y nu
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in R4] for m in R4]


def tens(X, Y):
    return [[X[m] * Y[n] for n in R4] for m in R4]


def pairVal(a, b, w):                         # sum mu nu, a mu * w mu nu * b nu
    return sum(a[m] * w[m][n] * b[n] for m in R4 for n in R4)


# an affine functional on R^k is stored as (e0, [E_0..E_{k-1}]) : x |-> e0 + sum_j E_j x_j
def affval(e, x):
    return e[0] + sum(e[1][j] * x[j] for j in range(len(x)))


def ehom(e):                                  # vecCons (e 0) (j |-> e.linear (single j 1))
    return [e[0]] + list(e[1])


def affOf(v):                                 # x |-> v 0 + sum_j v (j+1) * x j
    return (v[0], list(v[1:]))


def prodEffVal(e, f, w):
    return pairVal(ehom(e), ehom(f), w)


def actT(N, w):                               # fun mu => homMap N (w mu)
    return [homMap(N, w[m]) for m in R4]


def actC(N, w):                               # fun mu nu => homMap N (fun k => w k nu) mu
    cols = [homMap(N, [w[k][n] for k in R4]) for n in R4]
    return [[cols[n][m] for n in R4] for m in R4]


def sgn(m, n):                                # -1 at (1,3) and (2,2)
    return -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1


_PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
_PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot(w):                                  # cnotFun w mu nu = sgn mu nu * w (pc mu nu) (pt mu nu)
    return [[sgn(m, n) * w[_PC[m][n]][_PT[m][n]] for n in R4] for m in R4]


phiW = [[(-1 if m == 2 else 1) if m == n else 0 for n in R4] for m in R4]
xplus, z3 = [1, 0, 0], [0, 0, 1]
idW = [[1 if m == n else 0 for n in R4] for m in R4]                     # K2Guard.idW
chainW = [[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]       # K2Guard.chainW
rotW = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]]
rotChainW = [[1, 0, 0, -1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]


def diag3(a, b, c):
    return [[a, 0, 0], [0, b, 0], [0, 0, c]]


reflY, nflip, ID3 = diag3(1, -1, 1), diag3(1, -1, -1), diag3(1, 1, 1)
R_H = [[0, 0, 1], [0, -1, 0], [1, 0, 0]]


def sharpVec(b, half=Fr(1, 2)):               # vecCons (1/2) (j |-> b j / 2)
    return [half] + [bj * half for bj in b]


def sharpEff(b, half=Fr(1, 2)):
    return affOf(sharpVec(b, half))


# FourCopyDefs
def tabMul(A, B):
    return [[sum(A[m][k] * B[k][n] for k in R4) for n in R4] for m in R4]


def tabT(A):
    return [[A[n][m] for n in R4] for m in R4]


def ipW(E, X):
    return sum(E[m][n] * X[m][n] for m in R4 for n in R4)


def famI_val(X, Y, E, F):                     # ipW X (tabMul (tabMul E Y) (tabT F))
    return ipW(X, tabMul(tabMul(E, Y), tabT(F)))


def famII_val(L, Lp, e, f):                   # ipW e (tabMul (tabMul L f) (tabT L'))
    return ipW(e, tabMul(tabMul(L, f), tabT(Lp)))


# FourCopyCore
def fourVal(X, Y, E, F):
    return sum(X[a][b] * Y[c][d] * E[a][c] * F[b][d]
               for a in R4 for b in R4 for c in R4 for d in R4)


def fpf(m, n):                                # Mathlib finProdFinEquiv: (x1, x2) |-> x2 + 4 * x1
    return n + 4 * m


def fpf_symm(i):                              # (divNat, modNat)
    return (i // 4, i % 4)


def flatW(w):                                 # flatW w i = w (fpf.symm i).1 (fpf.symm i).2
    return [w[fpf_symm(i)[0]][fpf_symm(i)[1]] for i in range(16)]


def tabCoord(m, n, sig=fpf):                  # coord (fpf (m, n))
    return (0, [1 if i == sig(m, n) else 0 for i in range(16)])


def corner(z, a):
    return list(z) if a == 0 else [-t for t in z]


def mm3(A, B):
    return [[sum(A[i][k] * B[k][j] for k in R3) for j in R3] for i in R3]


def tr3(A):
    return [[A[j][i] for j in R3] for i in R3]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def isOrth3(M):                               # toMatrix' M in orthogonalGroup
    return mm3(tr3(M), M) == ID3 and mm3(M, tr3(M)) == ID3


def isRot3(M):                                # toMatrix' M in specialOrthogonalGroup
    return isOrth3(M) and det3(M) == 1


def orient(A, B):                             # decide (det A * det B = -1)
    return det3(A) * det3(B) == -1


def EvenCycle4(t01, t23, t02, t13):           # (toNat sum) % 2 = 0
    return (int(t01) + int(t23) + int(t02) + int(t13)) % 2 == 0


def EvenCycle(tau):
    return EvenCycle4(tau['p01'], tau['p23'], tau['p02'], tau['p13'])


def NClass_relation_holds(N, A, B, Ap, Bp, w):  # N w = actC A (actT B (cnot (actC A' (actT B' w))))
    return N(w) == actC(A, actT(B, cnot(actC(Ap, actT(Bp, w)))))


def unitTab(m, n):
    return [[1 if (i, j) == (m, n) else 0 for j in R4] for i in R4]


def tadd(A, B):
    return [[A[i][j] + B[i][j] for j in R4] for i in R4]


def tsc(c, A):
    return [[c * A[i][j] for j in R4] for i in R4]


# =====================================================================================
# §2  Exact Gaussian rationals, matrices, the Pauli map rho
# =====================================================================================
class C:
    __slots__ = ('r', 'i')

    def __init__(self, r=0, i=0):
        self.r = r if type(r) is Fr else Fr(r)
        self.i = i if type(i) is Fr else Fr(i)

    def __add__(s, o):
        if not isinstance(o, C):
            o = C(o)
        return C(s.r + o.r, s.i + o.i)

    __radd__ = __add__

    def __sub__(s, o):
        if not isinstance(o, C):
            o = C(o)
        return C(s.r - o.r, s.i - o.i)

    def __rsub__(s, o):
        return C(o) - s

    def __mul__(s, o):
        if isinstance(o, C):
            return C(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
        o = Fr(o)
        return C(s.r * o, s.i * o)

    __rmul__ = __mul__

    def __neg__(s):
        return C(-s.r, -s.i)

    def conj(s):
        return C(s.r, -s.i)

    def inv(s):
        d = s.r * s.r + s.i * s.i
        return C(s.r / d, -s.i / d)

    def __eq__(s, o):
        if not isinstance(o, C):
            o = C(o)
        return s.r == o.r and s.i == o.i

    def __hash__(s):
        return hash((s.r, s.i))

    def iszero(s):
        return s.r == 0 and s.i == 0

    def __repr__(s):
        return '(%s%+si)' % (s.r, s.i) if s.i else str(s.r)


def cz(n):
    return [[C() for _ in range(n)] for _ in range(n)]


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            s = C()
            for t in range(k):
                a = A[i][t]
                if not a.iszero():
                    b = B[t][j]
                    if not b.iszero():
                        s = s + a * b
            row.append(s)
        out.append(row)
    return out


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msc(c, A):
    return [[A[i][j] * c for j in range(len(A[0]))] for i in range(len(A))]


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def mtr(A):
    s = C()
    for i in range(len(A)):
        s = s + A[i][i]
    return s


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def kron(A, B):
    p, q = len(A), len(B)
    return [[A[i // q][j // q] * B[i % q][j % q] for j in range(p * q)] for i in range(p * q)]


def cdet(M):
    n = len(M)
    A = [row[:] for row in M]
    d = C(1)
    for k in range(n):
        p = next((r for r in range(k, n) if not A[r][k].iszero()), None)
        if p is None:
            return C(0)
        if p != k:
            A[k], A[p] = A[p], A[k]
            d = -d
        d = d * A[k][k]
        iv = A[k][k].inv()
        for r in range(k + 1, n):
            if not A[r][k].iszero():
                fct = A[r][k] * iv
                for c in range(k, n):
                    A[r][c] = A[r][c] - fct * A[k][c]
    return d


def is_herm(M):
    return meq(M, dag(M))


def psd_exact(M):
    """Hermitian M is PSD iff every principal minor is >= 0 (exact)."""
    assert is_herm(M)
    n = len(M)
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            d = cdet([[M[i][j] for j in S] for i in S])
            assert d.i == 0
            if d.r < 0:
                return False
    return True


def pd_exact(M):
    """Sylvester: Hermitian M is PD iff every leading principal minor is > 0 (exact)."""
    assert is_herm(M)
    for k in range(1, len(M) + 1):
        d = cdet([row[:k] for row in M[:k]])
        assert d.i == 0
        if d.r <= 0:
            return False
    return True


def quad(M, v):
    s = C()
    for i in range(len(v)):
        for j in range(len(v)):
            s = s + v[i].conj() * M[i][j] * v[j]
    assert s.i == 0
    return s.r


def neg_witness(M):
    """Search v with entries in {0,+-1,+-i} minimising v^dag M v (exact); return (value, v)."""
    vals = [C(0), C(1), C(-1), C(0, 1), C(0, -1)]
    best = None
    for v in itertools.product(vals, repeat=len(M)):
        if all(t.iszero() for t in v):
            continue
        q = quad(M, list(v))
        if best is None or q < best[0]:
            best = (q, list(v))
    return best


I2 = [[C(1), C(0)], [C(0), C(1)]]
SX = [[C(0), C(1)], [C(1), C(0)]]
SY = [[C(0), C(0, -1)], [C(0, 1), C(0)]]
SZ = [[C(1), C(0)], [C(0), C(-1)]]
SIG = [I2, SX, SY, SZ]                         # sigma_0..3 = I, X, Y, Z
SS = [[kron(SIG[m], SIG[n]) for n in R4] for m in R4]
U_CNOT = [[C(1 if (i, j) in ((0, 0), (1, 1), (2, 3), (3, 2)) else 0) for j in range(4)] for i in range(4)]
I4 = [[C(1 if i == j else 0) for j in range(4)] for i in range(4)]


def rho(w):
    """rho(w) = (1/4) sum_{mu nu} w_{mu nu} sigma_mu (x) sigma_nu  (first factor = first index)."""
    M = cz(4)
    for m in R4:
        for n in R4:
            c = Fr(w[m][n]) / 4
            if c:
                S = SS[m][n]
                for i in range(4):
                    for j in range(4):
                        if not S[i][j].iszero():
                            M[i][j] = M[i][j] + S[i][j] * c
    return M


def wOf(Rm):
    """inverse of rho: w_{mu nu} = Tr(rho sigma_mu (x) sigma_nu); asserts reality."""
    w = [[None] * 4 for _ in R4]
    for m in R4:
        for n in R4:
            t = mtr(mmul(Rm, SS[m][n]))
            assert t.i == 0, 'non-real Pauli coefficient'
            w[m][n] = t.r
    return w


def ptB(M):
    """partial transpose on the second qubit: PT[(i,k),(j,l)] = M[(i,l),(j,k)]."""
    return [[M[2 * (r // 2) + (c % 2)][2 * (c // 2) + (r % 2)] for c in range(4)] for r in range(4)]


def opOf(a):
    """sum_mu a_mu sigma_mu (single qubit)."""
    M = [[C(), C()], [C(), C()]]
    for m in R4:
        M = madd(M, msc(Fr(a[m]), SIG[m]))
    return M


def isPSDtab(w):
    return psd_exact(rho(w))


# =====================================================================================
hdr('§3 replay of kernel lemmas (transcription controls)')
# =====================================================================================
rec('cnot_prodState_xplus_z3: cnot (prodState xplus z3) = phiW', cnot(prodState(xplus, z3)) == phiW)
rec('actT_reflY_phiW: actT reflY phiW = idW', actT(reflY, phiW) == idW)
rec('cnot_idW: cnot idW = chainW', cnot(idW) == chainW)
rec('chain_eq: cnot (actT reflY (cnot (prodState xplus z3))) = chainW',
    cnot(actT(reflY, cnot(prodState(xplus, z3)))) == chainW)
rec('chain_value = -1/2', prodEffVal(sharpEff([-1, 0, 0]), sharpEff([0, 0, -1]), chainW) == Fr(-1, 2),
    prodEffVal(sharpEff([-1, 0, 0]), sharpEff([0, 0, -1]), chainW))
rec('sharpVec_negX = [1/2,-1/2,0,0]', sharpVec([-1, 0, 0]) == [Fr(1, 2), Fr(-1, 2), 0, 0])
rec('sharpVec_negZ = [1/2,0,0,-1/2]', sharpVec([0, 0, -1]) == [Fr(1, 2), 0, 0, Fr(-1, 2)])
rec('actT_nflip_phiW = rotW', actT(nflip, phiW) == rotW)
rec('cnot_rotW = rotChainW', cnot(rotW) == rotChainW)
rec('rotation_chain_value = 0',
    prodEffVal(sharpEff([-1, 0, 0]), sharpEff([0, 0, -1]),
               cnot(actT(nflip, cnot(prodState(xplus, z3))))) == 0)
rec('pc_pc, pt_pt, sgn_mul_sgn (16 cases)',
    all(_PC[_PC[m][n]][_PT[m][n]] == m and _PT[_PC[m][n]][_PT[m][n]] == n
        and sgn(m, n) * sgn(_PC[m][n], _PT[m][n]) == 1 for m in R4 for n in R4))
rec('cnot_frame (a,b in Fin 2)',
    all(cnot(prodState(corner(z3, a), corner(z3, b))) == prodState(corner(z3, a), corner(z3, (a + b) % 2))
        for a in (0, 1) for b in (0, 1)))
rec('det_reflY = -1, det_nflip = 1', det3(reflY) == -1 and det3(nflip) == 1)

# =====================================================================================
hdr('§4 exhaustive exact identities of the Pauli map (basis enumeration)')
# =====================================================================================
BASIS = [(m, n) for m in R4 for n in R4]
RHO_B = {mn: rho(unitTab(*mn)) for mn in BASIS}
rec('E0 rho is injective onto Herm(4): wOf(rho(e_mn)) = e_mn for all 16 basis tables',
    all(wOf(RHO_B[mn]) == unitTab(*mn) for mn in BASIS))
rec('E1 ipW(E,X) = 4 Tr(rho E rho X) on all 256 basis pairs',
    all(ipW(unitTab(*p), unitTab(*q)) == 4 * mtr(mmul(RHO_B[p], RHO_B[q])) for p in BASIS for q in BASIS))
rec('E2 pairVal(a,b,w) = Tr(rho(w) (A^ (x) B^)), A^ = sum a_mu sigma_mu, on 16x4x4 basis',
    all(pairVal([1 if k == ka else 0 for k in R4], [1 if k == kb else 0 for k in R4], unitTab(*mn))
        == mtr(mmul(RHO_B[mn], kron(SIG[ka], SIG[kb])))
        for mn in BASIS for ka in R4 for kb in R4))
rec('E3 rho(cnot w) = U rho(w) U^dag (U = CNOT, control = first index) on 16 basis tables',
    all(meq(rho(cnot(unitTab(*mn))), mmul(mmul(U_CNOT, RHO_B[mn]), dag(U_CNOT))) for mn in BASIS))
rec('E4 rho(actT reflY w) = partial transpose_B rho(w) on 16 basis tables',
    all(meq(rho(actT(reflY, unitTab(*mn))), ptB(RHO_B[mn])) for mn in BASIS))
rec('E5 rho(tens(e_m, e_n)) = (sigma_m/2) (x) (sigma_n/2) on 16 basis pairs',
    all(meq(rho(tens([1 if k == m else 0 for k in R4], [1 if k == n else 0 for k in R4])),
            kron(msc(Fr(1, 2), SIG[m]), msc(Fr(1, 2), SIG[n]))) for m in R4 for n in R4))
rec('E6 Tr rho(w) = w_00 on 16 basis tables', all(mtr(RHO_B[mn]) == (1 if mn == (0, 0) else 0) for mn in BASIS))


# four-qubit identity: fourVal(X,Y,E,F) = 16 Tr[(rho X (x) rho Y) . Pi (rho E (x) rho F) Pi^dag]
# X on qubits (0,1), Y on (2,3), E on (0,2), F on (1,3); Pi reorders (q0,q2,q1,q3) -> (q0,q1,q2,q3).
def sparse(M):
    return {(i, j): v for i, row in enumerate(M) for j, v in enumerate(row) if not v.iszero()}


def skron(A, B, nB):
    return {(i * nB + k, j * nB + l): a * b for (i, j), a in A.items() for (k, l), b in B.items()}


def perm0213(s):
    i0, i1, i2, i3 = (s >> 3) & 1, (s >> 2) & 1, (s >> 1) & 1, s & 1
    return 8 * i0 + 4 * i2 + 2 * i1 + i3


def four_trace(rX, rY, rE, rF):
    A = skron(sparse(rX), sparse(rY), 4)
    M = skron(sparse(rE), sparse(rF), 4)
    B = {(perm0213(s), perm0213(t)): v for (s, t), v in M.items()}
    tot = C()
    for (s, t), a in A.items():
        b = B.get((t, s))
        if b is not None:
            tot = tot + a * b
    return tot


t1 = time.time()
SPR = {mn: sparse(RHO_B[mn]) for mn in BASIS}
A_ = {(p, q): skron(SPR[p], SPR[q], 4) for p in BASIS for q in BASIS}
B_ = {}
for p in BASIS:
    for q in BASIS:
        M = skron(SPR[p], SPR[q], 4)
        B_[(p, q)] = {(perm0213(s), perm0213(t)): v for (s, t), v in M.items()}
bad = 0
for p in BASIS:            # X = e_p
    Xt = unitTab(*p)
    for q in BASIS:        # Y = e_q
        Yt = unitTab(*q)
        A = A_[(p, q)]
        for r in BASIS:    # E = e_r
            Et_ = unitTab(*r)
            for s in BASIS:  # F = e_s
                Bm = B_[(r, s)]
                tot = C()
                for (i, j), a in A.items():
                    b = Bm.get((j, i))
                    if b is not None:
                        tot = tot + a * b
                fv = fourVal(Xt, Yt, Et_, unitTab(*s))
                if not (16 * tot == fv):
                    bad += 1
rec('E7 fourVal(X,Y,E,F) = 16 Tr[(rho X (x) rho Y) Pi(rho E (x) rho F)Pi^dag] on all 65536 basis quadruples',
    bad == 0, 'mismatches=%d, %.1fs' % (bad, time.time() - t1))

# =====================================================================================
hdr('§5 symbolic identities (sympy, generic symbols)')
# =====================================================================================
HALF = sp.Rational(1, 2)


def symtab(nm):
    return [[sp.Symbol('%s%d%d' % (nm, m, n)) for n in R4] for m in R4]


def symvec(nm, k):
    return [sp.Symbol('%s%d' % (nm, i)) for i in range(k)]


def zero(e):
    return sp.expand(e) == 0


Xs, Ys, Es, Fs = symtab('X'), symtab('Y'), symtab('E'), symtab('F')
rec('S1 famI literal form ipW X (E Y F^T) = fourVal X Y E F', zero(famI_val(Xs, Ys, Es, Fs) - fourVal(Xs, Ys, Es, Fs)))
rec('S2 famII literal form ipW e (L f L\'^T) = fourVal e f L L\'',
    zero(famII_val(Es, Fs, Xs, Ys) - fourVal(Xs, Ys, Es, Fs)))
u1, u2, v1, v2 = symvec('u', 4), symvec('v', 4), symvec('p', 4), symvec('q', 4)
rec('S3a famI on separable effect tables factorises: fourVal(X,Y,u1u2^T,v1v2^T) = pairVal(u1,v1,X) pairVal(u2,v2,Y)',
    zero(famI_val(Xs, Ys, tens(u1, u2), tens(v1, v2)) - pairVal(u1, v1, Xs) * pairVal(u2, v2, Ys)))
rec('S3b famII on separable effect tables factorises: famII(L,L\',u1u2^T,v1v2^T) = pairVal(u1,v1,L) pairVal(u2,v2,L\')',
    zero(famII_val(Xs, Ys, tens(u1, u2), tens(v1, v2)) - pairVal(u1, v1, Xs) * pairVal(u2, v2, Ys)))
xs3, ys3 = symvec('x', 3), symvec('y', 3)
ws = symtab('w')
rec('S4 ipW(prodState x y, w) = pairVal(hom x, hom y, w)', zero(ipW(prodState(xs3, ys3), ws) - pairVal(hom(xs3), hom(ys3), ws)))
es = (sp.Symbol('e0'), symvec('E', 3))
fs = (sp.Symbol('f0'), symvec('F', 3))
rec('S5 prodEffVal e f (prodState x y) = e x * f y', zero(prodEffVal(es, fs, prodState(xs3, ys3)) - affval(es, xs3) * affval(fs, ys3)))
rec('S6 cnot is an involution (generic w)', all(zero(a - b) for ra, rb in zip(cnot(cnot(ws)), ws) for a, b in zip(ra, rb)))
rec('S7 NClass relation with A=B=A\'=B\'=id: cnot w = actC id (actT id (cnot (actC id (actT id w))))',
    all(zero(a - b) for ra, rb in zip(cnot(ws), actC(ID3, actT(ID3, cnot(actC(ID3, actT(ID3, ws)))))) for a, b in zip(ra, rb)))
Rs = [[sp.Symbol('R%d%d' % (i, j)) for j in R3] for i in R3]
Ss = [[sp.Symbol('S%d%d' % (i, j)) for j in R3] for i in R3]
as4, bs4 = symvec('a', 4), symvec('b', 4)
rec('S8a pairVal(a,b,actC R w) = pairVal(homMap R^T a, b, w) (generic R)',
    zero(pairVal(as4, bs4, actC(Rs, ws)) - pairVal(homMap(tr3(Rs), as4), bs4, ws)))
rec('S8b pairVal(a,b,actT R w) = pairVal(a, homMap R^T b, w) (generic R)',
    zero(pairVal(as4, bs4, actT(Rs, ws)) - pairVal(as4, homMap(tr3(Rs), bs4), ws)))
rec('S8c actC R (actC S w) = actC (R S) w and actT R (actT S w) = actT (R S) w',
    all(zero(a - b) for ra, rb in zip(actC(Rs, actC(Ss, ws)), actC(mm3(Rs, Ss), ws)) for a, b in zip(ra, rb))
    and all(zero(a - b) for ra, rb in zip(actT(Rs, actT(Ss, ws)), actT(mm3(Rs, Ss), ws)) for a, b in zip(ra, rb)))
rec('S8d ehom(e o R) = homMap R^T (ehom e): e(Rx) = e0 + (R^T E).x',
    zero(affval(es, [sum(Rs[i][j] * xs3[j] for j in R3) for i in R3])
         - (es[0] + sum(homMap(tr3(Rs), ehom(es))[j + 1] * xs3[j] for j in R3))))
bv, cv = symvec('B', 3), symvec('Cc', 3)
one3 = (1, [0, 0, 0])
neg = lambda v: [-t for t in v]
rec('S9a prodEffVal(1,1,w) = w00', zero(prodEffVal(one3, one3, ws) - ws[0][0]))
rec('S9b sum_{s,t=+-} prodEffVal(sharpEff(s b), sharpEff(t c), w) = w00',
    zero(sum(prodEffVal(sharpEff(sb, HALF), sharpEff(tc, HALF), ws) for sb in (bv, neg(bv)) for tc in (cv, neg(cv))) - ws[0][0]))
rec('S9c sum_{s,t} s t prodEffVal(sharpEff(s b), sharpEff(t c), w) = b^T w\' c (w\' = 3x3 block)',
    zero(sum(s * t * prodEffVal(sharpEff([s * q for q in bv], HALF), sharpEff([t * q for q in cv], HALF), ws)
             for s in (1, -1) for t in (1, -1)) - sum(bv[i] * ws[i + 1][j + 1] * cv[j] for i in R3 for j in R3)))
rec('S9d prodEffVal(sharpEff b,1,w) - prodEffVal(sharpEff(-b),1,w) = sum_j b_j w_{j+1,0}; same in the 2nd slot',
    zero(prodEffVal(sharpEff(bv, HALF), one3, ws) - prodEffVal(sharpEff(neg(bv), HALF), one3, ws)
         - sum(bv[j] * ws[j + 1][0] for j in R3))
    and zero(prodEffVal(one3, sharpEff(bv, HALF), ws) - prodEffVal(one3, sharpEff(neg(bv), HALF), ws)
             - sum(bv[j] * ws[0][j + 1] for j in R3)))
rec('S10 actT reflY (prodState x y) = prodState x (reflY y)',
    all(zero(a - b) for ra, rb in zip(actT(reflY, prodState(xs3, ys3)), prodState(xs3, [ys3[0], -ys3[1], ys3[2]]))
        for a, b in zip(ra, rb)))
rec('S11 prodEffVal e f idW = e0 f0 + E.F', zero(prodEffVal(es, fs, idW) - (es[0] * fs[0] + sum(es[1][j] * fs[1][j] for j in R3))))
rec('S12 sharpEff b x = 1/2 + b.x/2', zero(affval(sharpEff(bv, HALF), xs3) - (HALF + sum(bv[j] * xs3[j] for j in R3) / 2)))

# =====================================================================================
hdr('§6 the KT4Core carrier V = R^{17x17} x R^{17x17}')
# =====================================================================================


def carrier(sig):
    """sig: the bijection Fin4 x Fin4 -> Fin16 used for X_ab = x_sig(a,b) inside the carrier."""
    def tab(x):
        return [[x[sig(a, b)] for b in R4] for a in R4]

    def Et(e):
        return [[e[1][sig(a, b)] + (e[0] if (a, b) == (0, 0) else 0) for b in R4] for a in R4]

    def eh(e):
        return [e[0]] + list(e[1])

    def outer(x, y):
        xh, yh = [1] + list(x), [1] + list(y)
        return [[xh[i] * yh[j] for j in range(17)] for i in range(17)]

    def stA(x, y):
        return (outer(x, y), None)

    def stB(x, y):
        return (None, outer(x, y))

    def bil(u, M, v):
        if M is None:
            return 0
        return sum(u[i] * M[i][j] * v[j] for i in range(17) if u[i] != 0 for j in range(17) if v[j] != 0)

    def effA(e, f, V):
        P, Q = V
        s = bil(eh(e), P, eh(f))
        if Q is not None:
            Ee, Ff = Et(e), Et(f)
            s = s + sum(Ee[a][b] * Ff[c][d] * Q[1 + sig(a, c)][1 + sig(b, d)]
                        for a in R4 for b in R4 if Ee[a][b] != 0 for c in R4 for d in R4 if Ff[c][d] != 0)
        return s

    def effB(e, f, V):
        P, Q = V
        s = bil(eh(e), Q, eh(f))
        if P is not None:
            Ee, Ff = Et(e), Et(f)
            s = s + sum(Ee[a][c] * Ff[b][d] * P[1 + sig(a, b)][1 + sig(c, d)]
                        for a in R4 for c in R4 if Ee[a][c] != 0 for b in R4 for d in R4 if Ff[b][d] != 0)
        return s

    return dict(tab=tab, Et=Et, eh=eh, stA=stA, stB=stB, effA=effA, effB=effB)


sig_T = lambda a, b: a + 4 * b
_perm = list(range(16))
random.Random(7).shuffle(_perm)
sig_R = lambda a, b: _perm[4 * a + b]
x16, y16 = symvec('x', 16), symvec('y', 16)
e16 = (sp.Symbol('e0'), symvec('E', 16))
f16 = (sp.Symbol('f0'), symvec('F', 16))
for nm, sig in (('fpf', fpf), ('transposed', sig_T), ('randperm', sig_R)):
    K = carrier(sig)
    SA, SB = K['stA'](x16, y16), K['stB'](x16, y16)
    tc = lambda m, n: tabCoord(m, n, sig)
    rec('K1[%s] effA_apply: effA e f (stA x y) = e x * f y' % nm,
        zero(K['effA'](e16, f16, SA) - affval(e16, x16) * affval(f16, y16)))
    rec('K2[%s] effB_apply: effB e f (stB x y) = e x * f y' % nm,
        zero(K['effB'](e16, f16, SB) - affval(e16, x16) * affval(f16, y16)))
    rec('K3[%s] tokA for all 256 (a,b,c,d)' % nm,
        all(zero(K['effA'](tc(a, b), tc(c, d), SA) - K['effB'](tc(a, c), tc(b, d), SA))
            for a in R4 for b in R4 for c in R4 for d in R4))
    rec('K4[%s] tokB for all 256 (a,b,c,d)' % nm,
        all(zero(K['effA'](tc(a, b), tc(c, d), SB) - K['effB'](tc(a, c), tc(b, d), SB))
            for a in R4 for b in R4 for c in R4 for d in R4))
    rec('K5[%s] effB e f (stA x y) = famI literal form at X=tab x, Y=tab y, E=Et e, F=Et f' % nm,
        zero(K['effB'](e16, f16, SA) - famI_val(K['tab'](x16), K['tab'](y16), K['Et'](e16), K['Et'](f16))))
    rec('K6[%s] effA e f (stB x y) = famII literal form at L=tab x, L\'=tab y, e=Et e, f=Et f' % nm,
        zero(K['effA'](e16, f16, SB) - famII_val(K['tab'](x16), K['tab'](y16), K['Et'](e16), K['Et'](f16))))
    rec('K7[%s] e(x) = ipW(Et e, tab x) on the slice x_sig(0,0) = 1' % nm,
        zero((affval(e16, x16) - ipW(K['Et'](e16), K['tab'](x16))).subs(x16[sig(0, 0)], 1)))
    flat_sig = [None] * 16
    for a in R4:
        for b in R4:
            flat_sig[sig(a, b)] = ws[a][b]
    rec('K7b[%s] sig is a bijection and tab(flat_sig w) = w (chart consistency)' % nm,
        None not in flat_sig and K['tab'](flat_sig) == ws)
# the Lean chart: flatW / tabCoord use fpf; check K7 against flatW directly
Kf = carrier(fpf)
rec('K7c Lean chart: tab(flatW w) = w (fpf) and tabCoord m n (flatW w) = w m n',
    Kf['tab'](flatW(ws)) == ws and all(affval(tabCoord(m, n), flatW(ws)) == ws[m][n] for m in R4 for n in R4))
# bilinearity (Lean: effA : A ->l A ->l (V ->a R)), generic V
Pg = [[sp.Symbol('P%d_%d' % (i, j)) for j in range(17)] for i in range(17)]
Qg = [[sp.Symbol('Q%d_%d' % (i, j)) for j in range(17)] for i in range(17)]
P2 = [[sp.Symbol('PP%d_%d' % (i, j)) for j in range(17)] for i in range(17)]
Q2 = [[sp.Symbol('QQ%d_%d' % (i, j)) for j in range(17)] for i in range(17)]
lam, mu = sp.Symbol('lam'), sp.Symbol('mu')
g16 = (sp.Symbol('g0'), symvec('G', 16))
lin = lambda e, g: (e[0] + lam * g[0], [a + lam * b for a, b in zip(e[1], g[1])])
for nm in ('effA', 'effB'):
    F_ = Kf[nm]
    rec('K8[%s] linear in e (generic V)' % nm,
        zero(F_(lin(e16, g16), f16, (Pg, Qg)) - F_(e16, f16, (Pg, Qg)) - lam * F_(g16, f16, (Pg, Qg))))
    rec('K8[%s] linear in f (generic V)' % nm,
        zero(F_(e16, lin(f16, g16), (Pg, Qg)) - F_(e16, f16, (Pg, Qg)) - lam * F_(e16, g16, (Pg, Qg))))
    VV = ([[Pg[i][j] + mu * P2[i][j] for j in range(17)] for i in range(17)],
          [[Qg[i][j] + mu * Q2[i][j] for j in range(17)] for i in range(17)])
    rec('K8[%s] linear (hence affine) in V' % nm,
        zero(F_(e16, f16, VV) - F_(e16, f16, (Pg, Qg)) - mu * F_(e16, f16, (P2, Q2))))
# countercontrol: carrier index convention mismatched with the Lean chart -> tokA must fail
Kbad = carrier(sig_T)
SAb = Kbad['stA'](x16, y16)
nbad = sum(1 for a in R4 for b in R4 for c in R4 for d in R4
           if not zero(Kbad['effA'](tabCoord(a, b), tabCoord(c, d), SAb) - Kbad['effB'](tabCoord(a, c), tabCoord(b, d), SAb)))
rec('CC-tok countercontrol: carrier with 4b+a against Lean tabCoord (4a+b) breaks tokA', nbad > 0, '%d/256 index tuples fail' % nbad)

# =====================================================================================
hdr('§7 exact instance generators')
# =====================================================================================
rng = random.Random(20261009)


def gi(k=2):
    return C(rng.randint(-k, k), rng.randint(-k, k))


def gram_state(rank, k=2):
    while True:
        B = [[gi(k) for _ in range(rank)] for _ in range(4)]
        M = mmul(B, dag(B))
        t = mtr(M).r
        if t != 0:
            Rm = msc(Fr(1) / t, M)
            return wOf(Rm), Rm


def pure_entangled():
    while True:
        w, Rm = gram_state(1)
        if cdet(ptB(Rm)).r < 0:            # det of partial transpose < 0  => NPT => entangled
            return w


def pd_state():
    while True:
        w, Rm = gram_state(4)
        if pd_exact(Rm):
            return w


def ball_pt():
    if rng.random() < 0.5:
        u = Fr(rng.randint(-6, 6), rng.randint(1, 5))
        v = Fr(rng.randint(-6, 6), rng.randint(1, 5))
        s = u * u + v * v + 1
        p = [2 * u / s, 2 * v / s, (u * u + v * v - 1) / s]
        rng.shuffle(p)
    else:
        while True:
            p = [Fr(rng.randint(-5, 5), 5) for _ in R3]
            if sum(t * t for t in p) <= 1:
                break
    assert sum(t * t for t in p) <= 1
    return p


def sep_elem(k=None):
    k = k or rng.randint(1, 3)
    out = [[Fr(0)] * 4 for _ in R4]
    for _ in range(k):
        out = tadd(out, tsc(Fr(rng.randint(1, 4), rng.randint(1, 4)), prodState(ball_pt(), ball_pt())))
    return out


def normalize(w):
    return tsc(Fr(1) / Fr(w[0][0]), w)


# 24 rotations of the cube (signed permutation matrices with det +1)
CUBE = []
for perm in itertools.permutations(R3):
    for signs in itertools.product((1, -1), repeat=3):
        M = [[signs[i] if j == perm[i] else 0 for j in R3] for i in R3]
        if det3(M) == 1:
            CUBE.append(M)
rec('cube rotation group: 24 elements, all IsRot3', len(CUBE) == 24 and all(isRot3(M) for M in CUBE))
BELLS = [actT(M, phiW) for M in CUBE]                      # maximally entangled pure states
BELLS_T = [actT(reflY, b) for b in BELLS]                  # their partial transposes (block-positive)
AX = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
PRODS = [prodState(a, b) for a in AX for b in AX]          # 36 pure product stabilizer states
rec('BELLS are rank-1 projectors, entangled (det PT_B < 0); BELLS_T outside Q3',
    all(meq(mmul(rho(b), rho(b)), rho(b)) and mtr(rho(b)) == 1 and cdet(ptB(rho(b))).r < 0 for b in BELLS)
    and all(not isPSDtab(b) for b in BELLS_T))
singlet = [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
rec('singlet table is a rank-1 projector', meq(mmul(rho(singlet), rho(singlet)), rho(singlet)) and mtr(rho(singlet)) == 1)

# =====================================================================================
hdr('§8 model M_cl : K = int(Q3) u (SEP + cnot SEP), N = cnot, locals = id')
# =====================================================================================
# hcls
rec('Mcl.hcls IsOrth3 id', isOrth3(ID3))
# (S7 already gives the gate relation for generic w)
# hadm: product states in K (by definition, SEP contains them, 0 in cnot SEP); K subset maxCone via Q3 subset maxCone
rec('Mcl.hadm prodState in Q3 on 200 exact ball pairs (control of SEP subset Q3)',
    all(isPSDtab(prodState(ball_pt(), ball_pt())) for _ in range(200)))
rec('Mcl.hadm SEP + cnot(SEP) elements are PSD (60 exact instances, control of SEP + cnot SEP subset Q3)',
    all(isPSDtab(tadd(sep_elem(), cnot(sep_elem()))) for _ in range(60)))
# Q3 subset maxCone: E2 + PSD of effect operators; sampled control
okq = True
for _ in range(60):
    w, _r = gram_state(rng.randint(1, 4))
    for _ in range(10):
        if pairVal(hom(ball_pt()), hom(ball_pt()), w) < 0:
            okq = False
rec('Mcl.hadm sampled control: pairVal(hom u, hom v, w) >= 0 for w in Q3 (600 exact samples)', okq)
# hgate on int(Q3): cnot maps PD to PD (E3 + unitary invariance); instances
rec('Mcl.hgate cnot maps 40 exact PD states to PD states', all(pd_exact(rho(cnot(pd_state()))) for _ in range(40)))
s_, sp_ = sep_elem(), sep_elem()
rec('Mcl.hgate cnot(s + cnot s\') = cnot s + s\' (exact instance; S6 gives it generically)',
    cnot(tadd(s_, cnot(sp_))) == tadd(cnot(s_), sp_))
# the witness w_H = actT R_H phiW
wH = actT(R_H, phiW)
rhoH = rho(wH)
print('     w_H = actT R_H phiW =', wH)
print('     cnot w_H =', cnot(wH))
rec('Mcl.IE1 R_H is a rotation (IsRot3: orthogonal, det 1)', isRot3(R_H), 'det=%s' % det3(R_H))
Hm = madd(SX, SZ)  # sqrt2 * Hadamard
IH = kron(I2, Hm)
rec('Mcl.w_H cross-check: rho(w_H) = (I (x) H) rho(phiW) (I (x) H)^dag (Hadamard on token 2)',
    meq(rhoH, msc(Fr(1, 2), mmul(mmul(IH, rho(phiW)), dag(IH)))))
rec('Mcl.w_H rho(w_H) is a rank-1 projector (Hermitian, P^2 = P, Tr P = 1)',
    is_herm(rhoH) and meq(mmul(rhoH, rhoH), rhoH) and mtr(rhoH) == 1)
rec('Mcl.w_H not in int(Q3): det rho(w_H) = 0', cdet(rhoH).iszero())
nw1 = neg_witness(ptB(rhoH))
rec('Mcl.w_H NPT: exact v with v^dag PT_B(rho w_H) v < 0 (no positive multiple of w_H is in SEP)', nw1[0] < 0,
    'value %s at v=%s' % (nw1[0], nw1[1]))
rhoCH = rho(cnot(wH))
nw2 = neg_witness(ptB(rhoCH))
rec('Mcl.w_H cnot(w_H) is a rank-1 projector and NPT (no positive multiple of cnot w_H is in SEP)',
    meq(mmul(rhoCH, rhoCH), rhoCH) and mtr(rhoCH) == 1 and nw2[0] < 0, 'value %s' % nw2[0])
# SEP subset PPT: product states' partial transposes are product states (S10 + E4) -> PSD; instance control
rec('Mcl.control PPT test does not flag product states (100 exact instances: PT_B rho(prodState) PSD)',
    all(psd_exact(ptB(rho(prodState(ball_pt(), ball_pt())))) for _ in range(100)))
rec('Mcl.control PPT test does not flag SEP elements (40 exact mixtures)', all(psd_exact(ptB(rho(sep_elem(3)))) for _ in range(40)))
# closure: rho(w_H + t e00) = rho(w_H) + (t/4) I, leading minors positive for every t > 0
tt = sp.Symbol('t', positive=True)
fr2sp = lambda q: sp.Rational(q.numerator, q.denominator)
Ms = sp.Matrix(4, 4, lambda i, j: fr2sp(rhoH[i][j].r) + sp.I * fr2sp(rhoH[i][j].i)) + (tt / 4) * sp.eye(4)
mins = [sp.Poly(sp.expand(Ms[:k, :k].det()), tt) for k in range(1, 5)]
rec('Mcl.hcl w_H + t*e00 in int(Q3) for every t > 0 (leading minors = nonzero polys in t with coefficients >= 0)',
    all(all(c >= 0 for c in p.all_coeffs()) and not p.is_zero and all(sp.im(c) == 0 for c in p.all_coeffs()) for p in mins),
    '; '.join(str(p.as_expr()) for p in mins))
rec('Mcl.hcl rho(w + t e00) = rho(w) + (t/4) I (exact, t = 1/1000)',
    meq(rho(tadd(wH, tsc(Fr(1, 1000), unitTab(0, 0)))), madd(rhoH, msc(Fr(1, 4000), I4))))
rec('Mcl.IE1 phiW in K_cl: phiW = cnot(prodState xplus z3) in cnot(SEP)', cnot(prodState(xplus, z3)) == phiW)
rec('Mcl.IE1 phiW rank-1 (also not in int Q3; its membership is via cnot SEP)', cdet(rho(phiW)).iszero())

# =====================================================================================
hdr('§9 model M_max : K = maxCone (eball 3), N = cnot, locals = id')
# =====================================================================================
rec('Mmax.hgate idW in maxCone: idW = actT reflY phiW with rho(phiW) PSD (partial transpose of a PSD table is block-positive)',
    actT(reflY, phiW) == idW and isPSDtab(phiW))
rec('Mmax.hgate idW not PSD (so idW is in maxCone \\ Q3)', not isPSDtab(idW))
okid = all(prodEffVal(sharpEff(ball_pt()), sharpEff(ball_pt()), idW) >= 0 for _ in range(400))
rec('Mmax.hgate sampled control: prodEffVal(sharpEff b, sharpEff c, idW) >= 0 (400 exact samples)', okid)
rec('Mmax.hgate cnot idW = chainW and prodEffVal(sharpEff(-e1), sharpEff(-e3), chainW) = -1/2 < 0',
    cnot(idW) == chainW and prodEffVal(sharpEff([-1, 0, 0]), sharpEff([0, 0, -1]), chainW) == Fr(-1, 2))
rec('Mmax.hgate sharpEff(-e1), sharpEff(-e3) take values 0 and 1 at -+b (unit b; effects by Cauchy-Schwarz)',
    all(affval(sharpEff(b), b) == 1 and affval(sharpEff(b), neg(b)) == 0 for b in ([-1, 0, 0], [0, 0, -1])))
rec('Mmax.hadm product states in maxCone: prodEffVal e f (prodState x y) = e x f y (S5) - instance',
    all(prodEffVal(sharpEff(ball_pt()), sharpEff(ball_pt()), prodState(ball_pt(), ball_pt())) >= 0 for _ in range(100)))

# =====================================================================================
hdr('§10 FourCopyCoherent at exact instances (famI, famII literal forms)')
# =====================================================================================


def states_Q3(n):
    out = []
    for i in range(n):
        r = i % 4
        if r == 0:
            out.append(pure_entangled())
        elif r == 1:
            out.append(pd_state())
        elif r == 2:
            out.append(gram_state(2)[0])
        else:
            out.append(rng.choice(BELLS))
    return out


def states_max(n):
    out = []
    while len(out) < n:
        q2 = pure_entangled()
        alpha = rng.choice([Fr(0), Fr(1, 20), Fr(1, 7), Fr(1, 3)])
        X = tadd(tsc(alpha, gram_state(rng.randint(1, 4))[0]), actT(reflY, q2))
        out.append(X)
    return out


def states_Kcl(n):
    out = []
    for i in range(n):
        r = i % 3
        if r == 0:
            out.append(pd_state())
        elif r == 1:
            out.append(tadd(sep_elem(), cnot(sep_elem())))
        else:
            out.append(rng.choice([phiW, cnot(prodState(ball_pt(), ball_pt()))]))
    return out


t1 = time.time()
SQ = states_Q3(40)
EQ = states_Q3(40)
nent = sum(1 for w in SQ if cdet(ptB(rho(w))).r < 0)
rec('inst Q3 family: all PSD, %d of 40 certified entangled (det PT_B < 0)' % nent,
    all(isPSDtab(w) for w in SQ + EQ) and nent >= 10)
SM = states_max(40)
nout = sum(1 for w in SM if not isPSDtab(w))
rec('inst maxCone family: %d of 40 certified outside Q3 (negative principal minor)' % nout, nout >= 10)
ES = [sep_elem() for _ in range(40)]
SK = states_Kcl(39)
rec('inst K_cl family: every element PSD (PD ones certified by Sylvester)', all(isPSDtab(w) for w in SK))


def run_fam(label, Sx, Ex, n=600):
    worst1, worst2 = None, None
    for _ in range(n):
        X, Y = rng.choice(Sx), rng.choice(Sx)
        E, F = rng.choice(Ex), rng.choice(Ex)
        v1 = famI_val(X, Y, E, F)
        v2 = famII_val(X, Y, E, F)
        worst1 = v1 if worst1 is None or v1 < worst1 else worst1
        worst2 = v2 if worst2 is None or v2 < worst2 else worst2
    rec('%s famI >= 0 on %d exact tuples' % (label, n), worst1 >= 0, 'min %s' % worst1)
    rec('%s famII >= 0 on %d exact tuples' % (label, n), worst2 >= 0, 'min %s' % worst2)


run_fam('inst uniform Q3 (states, effects in Q3 = dualW Q3)', SQ, EQ)
run_fam('inst uniform K_cl (states in K_cl, effects in Q3 = dualW K_cl)', SK, EQ)
run_fam('inst uniform maxCone (states in maxCone incl. non-PSD, effects in SEP = dualW maxCone)', SM + [idW], ES)
print('     instance families done in %.1fs' % (time.time() - t1))


# structured exhaustive families (integer tables)
def exhaustive(label, XS, YS, ES_, FS_):
    t2 = time.time()
    mn = None
    cnt = 0
    nneg = 0
    for X in XS:
        for Y in YS:
            for F in FS_:
                T = tabMul(tabMul(X, F), tabT(Y))   # (X F Y^T)_{ac} = sum_{bd} X_ab F_bd Y_cd
                for E in ES_:
                    v = ipW(E, T)                  # = fourVal(X,Y,E,F)
                    cnt += 1
                    if v < 0:
                        nneg += 1
                    if mn is None or v < mn:
                        mn = v
    return cnt, nneg, mn, time.time() - t2


# re-check the fast form against the literal forms on a few tuples
rec('fast form ipW(E, X F Y^T) = famI literal (exact spot checks)',
    all(ipW(E, tabMul(tabMul(X, F), tabT(Y))) == famI_val(X, Y, E, F)
        for X, Y, E, F in [(rng.choice(BELLS), rng.choice(BELLS_T), rng.choice(PRODS), rng.choice(BELLS)) for _ in range(50)]))
c, ng, mn_, dt = exhaustive('Q3', BELLS, BELLS, BELLS, BELLS)
rec('exh uniform Q3: famI >= 0 on all 24^4 Bell-variant tuples (X,Y,E,F all maximally entangled)', ng == 0,
    'n=%d min=%s %.1fs' % (c, mn_, dt))
c, ng, mn_, dt = exhaustive('Q3p', BELLS, PRODS[:18], BELLS, PRODS[:18])
rec('exh uniform Q3: famI >= 0 on 24x18x24x18 Bell/product tuples', ng == 0, 'n=%d min=%s %.1fs' % (c, mn_, dt))
c, ng, mn_, dt = exhaustive('max', BELLS_T, BELLS_T, PRODS, PRODS)
rec('exh uniform maxCone: famI >= 0 for X,Y in PT_B(Bells) (non-PSD), E,F in 36 product stabilizers', ng == 0,
    'n=%d min=%s %.1fs' % (c, mn_, dt))
# famII for maxCone on the same structured family: famII(L,L',e,f) = fourVal(e,f,L,L')
c, ng, mn_, dt = exhaustive('maxII', PRODS, PRODS, BELLS_T, BELLS_T)
rec('exh uniform maxCone: famII >= 0 for L,L\' in PT_B(Bells), e,f in 36 product stabilizers', ng == 0,
    'n=%d min=%s %.1fs' % (c, mn_, dt))

# countercontrols: the families are discriminating
c, ng, mn_, dt = exhaustive('ccQ3', BELLS_T, BELLS, BELLS, BELLS)
rec('CC-Q3: X outside Q3 (PT_B Bells) with Y,E,F in Q3 gives negative famI values', ng > 0, '%d/%d negative, min %s' % (ng, c, mn_))
# note: with X and Y BOTH partial transposes the value equals a pairing of PSD operators (the two
# transposes move onto F as a full transpose), so that family cannot discriminate; mix them instead.
c, ng, mn_, dt = exhaustive('ccMax0', BELLS_T, BELLS_T, BELLS, BELLS)
rec('CC-max design note: X,Y both PT_B(Bells), E,F Bells gives no negatives (double transpose cancels)', ng == 0,
    '%d/%d negative, min %s' % (ng, c, mn_))
c, ng, mn_, dt = exhaustive('ccMax', BELLS_T, BELLS + BELLS_T, BELLS, BELLS)
rec('CC-max: effects outside SEP (Bells) with X,Y in maxCone gives negative famI values', ng > 0, '%d/%d negative, min %s' % (ng, c, mn_))
v_cc = famI_val(idW, singlet, phiW, phiW)
rec('CC-explicit: famI_val(idW, singlet, phiW, phiW) = -2 (idW in maxCone\\Q3, phiW in Q3\\SEP)', v_cc == -2, v_cc)

# =====================================================================================
hdr('§11 KT4Core posBA / posAB end-to-end through the carrier (exact instances)')
# =====================================================================================


def effect_from_table(T, sig=fpf):
    """an affine e on R^16 with Et(e) = T, with the constant split at random between e0 and E_sig(0,0)."""
    e0 = Fr(rng.randint(-3, 3), rng.randint(1, 4))
    E = [Fr(0)] * 16
    for a in R4:
        for b in R4:
            E[sig(a, b)] = Fr(T[a][b])
    E[sig(0, 0)] -= e0
    return (e0, E)


def e2e(label, bodyA, bodyB, effs, n=150):
    worstBA, worstAB = None, None
    for _ in range(n):
        T1, T2 = rng.choice(effs), rng.choice(effs)
        e, f = effect_from_table(T1), effect_from_table(T2)
        assert Kf['Et'](e) == [[Fr(t) for t in row] for row in T1]
        X, Y = normalize(rng.choice(bodyA)), normalize(rng.choice(bodyA))
        x, y = flatW(X), flatW(Y)
        assert x[0] == 1 and y[0] == 1
        # e is an effect (>= 0) on the bodies: check at these points
        assert affval(e, x) >= 0 and affval(f, y) >= 0
        vBA = Kf['effB'](e, f, Kf['stA'](x, y))
        L, Lp = normalize(rng.choice(bodyB)), normalize(rng.choice(bodyB))
        vAB = Kf['effA'](e, f, Kf['stB'](flatW(L), flatW(Lp)))
        worstBA = vBA if worstBA is None or vBA < worstBA else worstBA
        worstAB = vAB if worstAB is None or vAB < worstAB else worstAB
    rec('%s posBA: effB e f (stA x y) >= 0 (%d exact tuples)' % (label, n), worstBA >= 0, 'min %s' % worstBA)
    rec('%s posAB: effA e f (stB x y) >= 0 (%d exact tuples)' % (label, n), worstAB >= 0, 'min %s' % worstAB)


e2e('e2e M_cl', SK, SK, [tsc(Fr(1, 4), normalize(w)) for w in EQ])
e2e('e2e M_max', SM + [idW], SM + [idW], [tsc(Fr(1, 4), normalize(w)) for w in ES])

# =====================================================================================
hdr('§12 conclusion: orient / EvenCycle')
# =====================================================================================
tau = {p: orient(ID3, ID3) for p in ('p01', 'p23', 'p02', 'p13')}
rec('orient id id = false (det id * det id = 1 /= -1)', tau['p01'] is False and det3(ID3) == 1)
rec('EvenCycle (fun p => orient (A p) (B p)) holds with A = B = id', EvenCycle(tau))
tau_bad = dict(tau)
tau_bad['p02'] = orient(reflY, ID3)
rec('CC-parity: one reflected post-local (det -1) makes the cycle odd', tau_bad['p02'] is True and not EvenCycle(tau_bad))

# =====================================================================================
hdr('§13 verdicts (generated from the checks above)')
# =====================================================================================
allok = all(c for _, c in CHECKS)
T = lambda *prefixes: [t for t, _ in CHECKS if any(t.startswith(p) for p in prefixes)]
common_sym = T('S', 'E')
carrier_tags = T('K1[', 'K2[', 'K3[', 'K4[', 'K5[', 'K6[', 'K7', 'K8[', 'CC-tok')
fam_Q = T('inst uniform Q3', 'exh uniform Q3', 'inst Q3 family', 'CC-Q3', 'CC-explicit')
fam_K = T('inst uniform K_cl', 'inst K_cl family')
fam_M = T('inst uniform maxCone', 'exh uniform maxCone', 'inst maxCone family', 'CC-max')
rows = [
    ('M_cl', 'hcls', passed('S7', 'Mcl.hcls'), 'holds', 'exact symbolic identity (S7) + exact matrix check'),
    ('M_cl', 'hadm', passed('Mcl.hadm', 'E2', 'E3', 'E5'), 'holds',
     'written argument (Q3 subset maxCone via E2; PD+PSD is PD) + exact identities + instance controls'),
    ('M_cl', 'hcl', passed('Mcl.hcl', 'Mcl.w_H', 'Mcl.control', 'E3', 'E4', 'E5', 'S10'), 'FAILS',
     'exact witness w_H (rank-1, NPT, cnot w_H NPT) + written extreme-ray argument; closure via exact t-polynomials'),
    ('M_cl', 'hgate', passed('Mcl.hgate', 'E3', 'S6'), 'holds', 'exact identity rho(cnot w)=U rho U^dag on basis + written'),
    ('M_cl', 'H (KT4Core)', passed(*carrier_tags, *fam_Q, *fam_K, 'E1', 'E7', 'S1', 'S2', 'S9', 'e2e M_cl'),
     'holds', 'exact symbolic identities (carrier) + exhaustive 4-qubit identity + written PSD argument'),
    ('M_cl', 'IE1', passed('Mcl.IE1', 'Mcl.w_H', 'Mcl.control'), 'FAILS', 'exact witness: phiW in K, actT R_H phiW not in K'),
    ('M_cl', 'EvenCycle', passed('orient', 'EvenCycle', 'CC-parity'), 'holds', 'exact evaluation'),
    ('M_max', 'hcls', passed('S7', 'Mcl.hcls'), 'holds', 'exact symbolic identity (S7)'),
    ('M_max', 'hadm', passed('S5', 'Mmax.hadm'), 'holds', 'exact identity S5 + written (intersection of half-spaces)'),
    ('M_max', 'hcl', True, 'holds', 'written: intersection of closed half-spaces'),
    ('M_max', 'hgate', passed('Mmax.hgate', 'chain_value', 'cnot_idW'), 'FAILS', 'exact witness idW -> chainW, value -1/2'),
    ('M_max', 'H (KT4Core)', passed(*carrier_tags, *fam_M, 'S3a', 'S3b', 'S4', 'S9', 'e2e M_max'),
     'holds', 'exact symbolic identities + written bipolar argument (dualW maxCone = SEP)'),
    ('M_max', 'IE1', passed('S8a', 'S8b', 'S8c', 'S8d'), 'holds', 'exact symbolic adjoint identities + written'),
    ('M_max', 'EvenCycle', passed('orient', 'EvenCycle', 'CC-parity'), 'holds', 'exact evaluation'),
]
for mdl, hyp, ok_, verdict, layer in rows:
    print('  %-6s %-12s %-6s %s' % (mdl, hyp, verdict if ok_ else 'VOID', layer))
nfail = sum(1 for _, c in CHECKS if not c)
print('\nFINAL: %d exact checks, %d failed; claims %s; %.1fs'
      % (len(CHECKS), nfail, 'AGREE' if nfail == 0 and all(r[2] for r in rows) else 'DISAGREE', time.time() - T0))
sys.exit(0 if nfail == 0 else 1)
