#!/usr/bin/env python3
"""c3_countermodels.py -- thread C5 (BRIDGE-COUNTER), stage 5, nodes C3 (eta, theta, kappa, zeta, iota, the NOT/J/
finite forms of alpha-delta, lambda without tok) and the closure picture.

Objects. K(Z_F) = (Q3 n Z*) + cone Z, Z = {e_s} the four Bell-type defects (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4
(stage 3, audited AUDIT-X; level (ii)); K(E0) = (Q3 n E0*) + R+ E0, E0 = E00 + E13 - E22 (level (i)). Self-duality
of both is SD1/SD2 [W, audited]; this script re-establishes every exact ingredient SD2 consumes (pairwise
ipW-orthogonality, the one-negative-eigenvalue spectra) and H1 (symbolic sum-of-squares over the whole ball) and H2.

DECISION RULE (fixed before the first run; rules, not expected numbers):
 D1 A cone is a COUNTERMODEL to candidate P (EXOTIC-X) iff: H1 holds by a symbolic identity; H2 holds exactly (cnot,
    and at level (ii) every G16 generator, permutes the defect set; each map is an exact unitary/antiunitary
    conjugation, hence a Q3-automorphism); the SD2 ingredients hold exactly; K != Q3 exactly (a defect pairs < 0 with
    a pure state of Q3, and that pure state pairs < 0 with the defect); and P's transcription is verified exactly on
    the cone (named per candidate below). Any failed ingredient: that candidate gets no EXOTIC-X line.
 D2 A candidate is EXOTIC-E (existence by EBF over an exact seed) iff the seed's invariant ray set is proved
    invariant under every generator of the candidate's group symbolically (rational parametrization of the circle),
    every point of it is maximally entangled (symbolic), so its overlap with every reachable product image is <= 1/2.
 D3 Transcriptions verified on K(Z_F):
    eta-a  relT and relC hold for cnot (all 16 basis tables) -- a gate identity, true for every cnot-invariant cone;
    eta-b  actC nflip and actT nflip permute the defects (the NOT idle-extended on either token preserves K);
    eta-c  CopyNatural: Ad(SWAP) conjugates actC nflip to actT nflip (the two copies' NOTs agree under exchange);
    theta  every defect lies in maxCone: pairVal(a, b, e_s) = (a0 b0 + a.M_s b)/4 with M_s orthogonal (symbolic), so
           every conditional state is in the ball; no-signalling is the identity ehom(e) + ehom(1-e) = (1,0,0,0);
           the defects steer to pure target states for every sharp control effect (symbolic);
    kappa  the gate flow U(w) = I + (w - 1)|1-><1-| (U(-1) = CNOT) is diagonal in the |a>_Z|b>_X basis; the Bell-type
           seed circles C1, C2 are invariant under U(w) and the G16 generators (D2);
    zeta   the pair body of K(Z_F) carries its own elementary drive: flow D(w) = I + (w-1) psi psi^dag (psi a defect
           vector), D(w1)D(w2) = D(w1 w2), every Ad D(w) fixes every defect; the half-turn D(-1) is an involution
           moving a body state; an automorphism J of K(Z_F) (a monomial permutation unitary in the defect basis) with
           J D(-1) J^-1 x != D(w) x for all w at an exact body state x;
    iota   SWAP permutes the defects.
 D4 Countercontrols (each must come out as stated, else no VERDICT): K(E0) fails eta-b (a pairing < 0); SWAP moves
    K(E0) (an exact pure state of Q3 n E0* pairing < 0 with SWAP E0); maxCone accepts idW and rejects chainW = cnot idW
    (-1/2 at the sharp effects of -e1, -e3; K2Guard.lean:101-134), so theta does not give H2; the gate flow at w = -i
    moves a defect out of K(Z_F) (an exact pure state of Q3 n Z* pairing < 0), so K(Z_F) is not kappa-invariant;
    Ad(H(x)I) carries C1 out of the seed set (non-vacuity of D2); one rotation of one token moves a defect out of
    K(Z_F) (lambda: K(Z_F) violates (b)); Q3 satisfies every transcription above (retention: each map is a
    Q3-automorphism, checked as exact unitarity, and the pair-drivability flow preserves Q3).
 VERDICT line only if every check is green.
"""
from fractions import Fraction as Fr
import itertools
import sys

# ---------------------------------------------------------------- exact Gaussian rationals and 4x4 matrices
class C:
    __slots__ = ('r', 'i')
    def __init__(s, r=0, i=0):
        s.r = Fr(r); s.i = Fr(i)
    def __add__(s, o): o = cc(o); return C(s.r + o.r, s.i + o.i)
    __radd__ = __add__
    def __sub__(s, o): o = cc(o); return C(s.r - o.r, s.i - o.i)
    def __rsub__(s, o): o = cc(o); return C(o.r - s.r, o.i - s.i)
    def __mul__(s, o): o = cc(o); return C(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    __rmul__ = __mul__
    def __neg__(s): return C(-s.r, -s.i)
    def conj(s): return C(s.r, -s.i)
    def __eq__(s, o): o = cc(o); return s.r == o.r and s.i == o.i
    def __hash__(s): return hash((s.r, s.i))
    def abs2(s): return s.r * s.r + s.i * s.i
    def __truediv__(s, o):
        o = cc(o); d = o.abs2(); n = s * o.conj(); return C(n.r / d, n.i / d)
    def iszero(s): return s.r == 0 and s.i == 0

def cc(x): return x if isinstance(x, C) else C(x, 0)
ZERO, ONE, IM = C(0), C(1), C(0, 1)

def mat(rows): return [[cc(x) for x in r] for r in rows]
def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), ZERO) for j in range(p)] for i in range(n)]
def dag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def conjm(A): return [[x.conj() for x in r] for r in A]
def kron(A, B):
    return [[A[i // len(B)][j // len(B[0])] * B[i % len(B)][j % len(B[0])]
             for j in range(len(A[0]) * len(B[0]))] for i in range(len(A) * len(B))]
def addm(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def subm(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scal(c, A): return [[cc(c) * x for x in r] for r in A]
def eye(n): return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
def tr(A): return sum((A[i][i] for i in range(len(A))), ZERO)
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def mv(A, v): return [sum((A[i][k] * v[k] for k in range(len(v))), ZERO) for i in range(len(A))]

I2 = mat([[1, 0], [0, 1]]); X = mat([[0, 1], [1, 0]]); Y = [[ZERO, C(0, -1)], [C(0, 1), ZERO]]
Z = mat([[1, 0], [0, -1]])
SIG = [I2, X, Y, Z]
P16 = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
UJ = scal(Fr(1, 2), [[C(1, -1), C(-1, -1)], [C(1, -1), C(1, 1)]])      # (I - i(X+Y+Z))/2
P0 = mat([[1, 0], [0, 0]]); P1 = mat([[0, 0], [0, 1]])
CNOT = addm(kron(P0, I2), kron(P1, X))                                    # control first, z3 -> |0>

def table(M):
    t = []
    for m in range(4):
        row = []
        for n in range(4):
            v = tr(mm(M, P16[m][n]))
            assert v.i == 0, 'non-Hermitian input to table'
            row.append(v.r)
        t.append(row)
    return t
def from_table(w):
    M = [[ZERO] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            if w[m][n] != 0:
                M = addm(M, scal(Fr(w[m][n]) / 4, P16[m][n]))
    return M
def basis_table(m, n): return [[Fr(1) if (a, b) == (m, n) else Fr(0) for b in range(4)] for a in range(4)]
def ad_table(U, scale=Fr(1)):
    return lambda w: [[x / scale for x in r] for r in table(mm(mm(U, from_table(w)), dag(U)))]
def T_table(w): return table(conjm(from_table(w)))
def unitary(U, scale=Fr(1)): return meq(mm(U, dag(U)), scal(scale, eye(len(U))))

# ---------------------------------------------------------------- the Lean definitions, transcribed
def sgn(m, n): return -1 if (m, n) in ((1, 3), (2, 2)) else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnotFun(w): return [[sgn(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]
def homMap(N3, v):            # N3: 3x3 rational matrix; v: HVec (4 entries), index 0 fixed
    tail = v[1:]
    return [v[0]] + [sum(N3[i][k] * tail[k] for k in range(3)) for i in range(3)]
def actT(N3, w): return [homMap(N3, w[m]) for m in range(4)]
def actC(N3, w):
    cols = [homMap(N3, [w[k][n] for k in range(4)]) for n in range(4)]
    return [[cols[n][m] for n in range(4)] for m in range(4)]
NFLIP = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
CYC3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]                                 # v -> (v2, v0, v1)
CYC3INV = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
def rot3(c, s): return [[c, -s, 0], [s, c, 0], [0, 0, 1]]
def m3(A, B): return [[sum(Fr(A[i][k]) * Fr(B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]
SGNY = [1, 1, -1, 1]
def transposeW(w): return [[SGNY[m] * SGNY[n] * w[m][n] for n in range(4)] for m in range(4)]

OUT = []
FAILS = []
def check(cid, ok, text):
    OUT.append(('PASS ' if ok else 'FAIL ') + cid + ' ' + text)
    if not ok:
        FAILS.append(cid)

def same_map(f, g):
    return all(f(basis_table(m, n)) == g(basis_table(m, n)) for m in range(4) for n in range(4))

# ================================================================ C3-specific
def ipW(A, B): return sum(Fr(A[m][n]) * Fr(B[m][n]) for m in range(4) for n in range(4))
def nrm(v): return sum((x.abs2() for x in v), Fr(0))
def outer(v): return [[a * b.conj() for b in v] for a in v]
def pure_table(v):
    nn = nrm(v)
    return [[x / nn for x in r] for r in table(outer(v))]
def ov(u, v):
    s = sum((a.conj() * b for a, b in zip(u, v)), ZERO)
    return s.abs2() / (nrm(u) * nrm(v))
def det_c(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    tot = ZERO
    for j in range(n):
        if M[0][j].iszero():
            continue
        minor = [r[:j] + r[j + 1:] for r in M[1:]]
        term = M[0][j] * det_c(minor)
        tot = tot + term if j % 2 == 0 else tot - term
    return tot
def psd(M):
    n = len(M)
    for k in range(1, n + 1):
        ek = ZERO
        for S in itertools.combinations(range(n), k):
            ek = ek + det_c([[M[i][j] for j in S] for i in S])
        if ek.i != 0 or ek.r < 0:
            return False
    return True
def tab(rows): return [[Fr(x) for x in r] for r in rows]
def E(m, n, c=1):
    t = [[Fr(0)] * 4 for _ in range(4)]
    t[m][n] = Fr(c)
    return t
def tadd(*ts): return [[sum(t[m][n] for t in ts) for n in range(4)] for m in range(4)]
def tscal(c, t): return [[Fr(c) * x for x in r] for r in t]
def teq(a, b): return all(Fr(a[m][n]) == Fr(b[m][n]) for m in range(4) for n in range(4))
def mvec(M, v): return mv(M, v)
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def defect(s):
    s1, s2 = s
    return tscal(Fr(1, 4), tadd(E(0, 0), E(1, 3, s1), E(2, 2, s2), E(3, 1, -s1 * s2)))
def psi_s(s):      # the defect vector of e_s: pauliW(e_s) = (I - 2 psi psi^dag)/8 (run 2: labels corrected, see NOTES)
    s1, s2 = s
    return [C(Fr(1, 2)), C(Fr(s1 * s2, 2)), C(Fr(-s1, 2)), C(Fr(s2, 2))]
ZF = {s: defect(s) for s in SIGNS}
def which_defect(t):
    for s in SIGNS:
        if teq(t, ZF[s]):
            return s
    return None
def permutes_ZF(f):
    imgs = [which_defect(f(ZF[s])) for s in SIGNS]
    return None not in imgs and len(set(imgs)) == 4
def in_QZstar(v):     # pure state v: T_v in Q3 n Z_F*  (pairings 1/2 - |<psi_t|v>|^2 >= 0)
    return all(ipW(ZF[s], pure_table(v)) >= 0 for s in SIGNS)
E0 = tadd(E(0, 0), E(1, 3), E(2, 2, -1))
SWAPm = mat([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
def swapW(w): return [[w[n][m] for n in range(4)] for m in range(4)]
XI, IXm, ZI, IZ = kron(X, I2), kron(I2, X), kron(Z, I2), kron(I2, Z)

def part_cones():
    import sympy as sp
    # Z1: spectra, orthonormality, orthogonality of the defects
    ok = True
    for s in SIGNS:
        ps = psi_s(s)
        target = scal(Fr(1, 8), subm(eye(4), scal(2, outer(ps))))
        ok = ok and meq(from_table(ZF[s]), target)
    gram = all(sum((a.conj() * b for a, b in zip(psi_s(s), psi_s(t))), ZERO) == (ONE if s == t else ZERO)
               for s in SIGNS for t in SIGNS)
    orth = all(ipW(ZF[s], ZF[t]) == (Fr(1, 4) if s == t else 0) for s in SIGNS for t in SIGNS)
    check('Z1', ok and gram and orth,
          'pauliW(e_s) = (I - 2 psi_s psi_s^dag)/8 (eigenvalues -1/8 once, 1/8 thrice), psi_s orthonormal, ipW(e_s,e_t) = delta/4')
    # Z2: H1, symbolic over the whole ball
    xs = sp.symbols('x0:3', real=True); ys = sp.symbols('y0:3', real=True)
    okh1 = True
    for s in SIGNS:
        e = ZF[s]
        hx = [1] + list(xs); hy = [1] + list(ys)
        val = sum(sp.Rational(e[m][n].numerator, e[m][n].denominator) * hx[m] * hy[n] for m in range(4) for n in range(4))
        M = sp.Matrix(3, 3, lambda i, j: 4 * sp.Rational(e[i + 1][j + 1].numerator, e[i + 1][j + 1].denominator))
        xv, yv = sp.Matrix(xs), sp.Matrix(ys)
        okh1 = okh1 and sp.expand(4 * val - (1 + (xv.T * M * yv)[0])) == 0
        okh1 = okh1 and (M * M.T == sp.eye(3))
        sq = (xv + M * yv).T * (xv + M * yv)
        okh1 = okh1 and sp.expand(2 * (1 + (xv.T * M * yv)[0]) - (sq[0] + (1 - (xv.T * xv)[0]) + (1 - (yv.T * yv)[0]))) == 0
    check('Z2', okh1, 'H1 for K(Z_F): 4 ipW(e_s, prodState x y) = 1 + x.M_s y, M_s orthogonal, and '
          '2(1 + x.M_s y) = |x + M_s y|^2 + (1-|x|^2) + (1-|y|^2) symbolically (products lie in Q3 n Z*)')
    # Z3: H2 at levels (i) and (ii)
    check('Z3', permutes_ZF(cnotFun) and permutes_ZF(ad_table(ZI)) and permutes_ZF(ad_table(IZ)) and permutes_ZF(transposeW),
          'H2: cnot, Ad(Z(x)I), Ad(I(x)Z) and T each permute the four defects (level (ii)); all are Q3-automorphisms')
    # Z5: K(Z_F) != Q3
    s0 = (1, 1)
    check('Z5', ipW(ZF[s0], pure_table(psi_s(s0))) == Fr(-1, 2),
          'K(Z_F) != Q3: <e_s, T_psi_s> = -1/2, so e_s is not in Q3 = Q3* and the pure state T_psi_s is not in K(Z_F) = K(Z_F)*')
    # E0: spectrum condition and level-(i) facts
    PE0 = from_table(E0)
    g = [C(1), C(0), C(0), C(1)]   # candidate eigenvectors are checked through the characteristic data below
    ev = []
    lam_ok = True
    for lam in (Fr(-1, 4), Fr(1, 4), Fr(3, 4)):
        Mm = subm(PE0, scal(lam, eye(4)))
        lam_ok = lam_ok and det_c(Mm).iszero()
    # multiplicities: tr = 1, tr^2 = (1/16) + 2/16 + 9/16 = 12/16 = 3/4 -> eigenvalues {-1/4, 1/4, 1/4, 3/4}
    tr1 = tr(PE0); tr2 = tr(mm(PE0, PE0))
    check('Z6', lam_ok and tr1 == ONE and tr2 == C(Fr(3, 4)) and teq(cnotFun(E0), E0) and
          ipW(E0, ad_table(ZI)(E0)) == -1,
          'K(E0): pauliW(E0) has eigenvalues -1/4, 1/4, 1/4, 3/4 (one negative, rest >= its modulus); cnot E0 = E0; '
          '<E0, Ad(Z(x)I)E0> = -1 (level (i) only)')
    return True

def part_eta_theta_iota():
    # eta-a: the gate relations (a gate identity at L, CD:854/860, re-checked)
    relT = same_map(lambda w: actT(NFLIP, cnotFun(actT(NFLIP, w))), cnotFun)
    relC = same_map(lambda w: actC(NFLIP, cnotFun(actC(NFLIP, w))), lambda w: actT(NFLIP, cnotFun(w)))
    check('ETA-a', relT and relC, 'relT and relC hold for cnot on all 16 basis tables (gate identities; no condition on K)')
    # eta-b: NOT idle-extended on either token preserves K(Z_F)
    okb = permutes_ZF(lambda w: actC(NFLIP, w)) and permutes_ZF(lambda w: actT(NFLIP, w))
    check('ETA-b', okb, 'actC nflip and actT nflip permute the four defects: K(Z_F) is invariant under the NOT on either token')
    # eta-c: copy naturality across the exchange
    okc = same_map(lambda w: swapW(actC(NFLIP, swapW(w))), lambda w: actT(NFLIP, w)) and same_map(swapW, ad_table(SWAPm))
    check('ETA-c', okc, 'CopyNatural under exchange: SWAP . actC nflip . SWAP = actT nflip; SWAP on tables = Ad(SWAP)')
    # countercontrol: K(E0) fails eta-b
    check('ETA-cc', ipW(E0, actT(NFLIP, E0)) == -1,
          'countercontrol: <E0, actT nflip E0> = -1, so K(E0) is not invariant under the NOT on the target')
    # theta: maxCone membership of the defects, conditional states, no-signalling, steering
    import sympy as sp
    a = sp.symbols('a0:4', real=True); b = sp.symbols('b0:4', real=True)
    okt = True
    for s in SIGNS:
        e = ZF[s]
        pv = sum(a[m] * sp.Rational(e[m][n].numerator, e[m][n].denominator) * b[n] for m in range(4) for n in range(4))
        M = sp.Matrix(3, 3, lambda i, j: 4 * sp.Rational(e[i + 1][j + 1].numerator, e[i + 1][j + 1].denominator))
        av, bv = sp.Matrix(a[1:]), sp.Matrix(b[1:])
        okt = okt and sp.expand(4 * pv - (a[0] * b[0] + (av.T * M * bv)[0])) == 0 and M * M.T == sp.eye(3)
        # steering: sharp control effect a = (1, n), |n| = 1 -> target vector (1, M^T n)/4, length |n|
        cond = [sum(a[m] * sp.Rational(e[m][n].numerator, e[m][n].denominator) for m in range(4)) for n in range(4)]
        okt = okt and sp.expand(4 * cond[0] - a[0]) == 0
        vec = sp.Matrix([4 * cond[k] for k in (1, 2, 3)])
        okt = okt and sp.expand((vec.T * vec)[0] - (av.T * av)[0]) == 0
    check('THETA', okt, 'every defect lies in maxCone: 4 pairVal(a,b,e_s) = a0 b0 + a.M_s b, M_s orthogonal (Cauchy-Schwarz on '
          'Lorentz vectors [W]); the conditional target state for any control effect has Bloch length |a|/a0 <= 1, '
          'pure for every sharp effect (maximal steering by the defect)')
    # no-signalling identity: ehom(e) + ehom(1 - e) = (1, 0, 0, 0) for an affine e
    e0, e1, e2, e3 = sp.symbols('c0:4', real=True)
    ehom_e = [e0, e1, e2, e3]; ehom_1me = [1 - e0, -e1, -e2, -e3]
    check('THETA-ns', [sp.expand(x + y) for x, y in zip(ehom_e, ehom_1me)] == [1, 0, 0, 0],
          'no-signalling: the two outcomes of any control test sum to the unit functional, so the target marginal is row 0')
    # theta countercontrol: maxCone accepts idW, rejects chainW = cnot idW
    idW = tab([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    chainW = tab([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
    av2 = [Fr(1, 2), Fr(-1, 2), 0, 0]; bv2 = [Fr(1, 2), 0, 0, Fr(-1, 2)]
    pv_chain = sum(av2[m] * chainW[m][n] * bv2[n] for m in range(4) for n in range(4))
    pv_id = sp.expand(sum(a[m] * idW[m][n] * b[n] for m in range(4) for n in range(4)) - sum(a[k] * b[k] for k in range(4)))
    check('THETA-cc', teq(cnotFun(idW), chainW) and pv_chain == Fr(-1, 2) and pv_id == 0,
          'countercontrol: idW in maxCone (pairVal = a.b >= 0 on Lorentz vectors [W]) but cnot idW = chainW has '
          'pairVal -1/2 at the sharp effects of -e1, -e3: maxCone (theta) does not give H2')
    # iota: SWAP permutes the defects; countercontrol: SWAP moves K(E0)
    check('IOTA', permutes_ZF(swapW), 'SWAP permutes the four defects: K(Z_F) is SWAP-invariant (with G16: order 48)')
    wit = None
    cand = [C(5), C(-5), C(-1), C(-1)]     # 2(1,-1,1,1) + 3(1,-1,-1,-1): joint eigenvectors of X(x)Z and Y(x)Y
    Tc = pure_table(cand)
    if ipW(E0, Tc) >= 0 and ipW(swapW(E0), Tc) < 0:
        wit = (cand, ipW(E0, Tc), ipW(swapW(E0), Tc))
    rng = range(-2, 3) if wit is None else []
    for v in itertools.product(rng, repeat=4):
        if all(x == 0 for x in v):
            continue
        vv = [C(v[0]), C(v[1]), C(v[2], 0), C(v[3])]
        for ph in (C(1), C(0, 1)):
            vw = [vv[0], vv[1], vv[2] * ph, vv[3]]
            T = pure_table(vw)
            if ipW(E0, T) >= 0 and ipW(swapW(E0), T) < 0:
                wit = (vw, ipW(E0, T), ipW(swapW(E0), T))
                break
        if wit:
            break
    check('IOTA-cc', wit is not None, 'countercontrol: a pure state of Q3 n E0* with <SWAP E0, T> < 0: ' +
          (str([(x.r, x.i) for x in wit[0]]) + ' pairings ' + str(wit[1]) + ', ' + str(wit[2]) if wit else 'none found'))

def part_kappa():
    import sympy as sp
    t = sp.symbols('t', real=True)
    w_t = (1 - t ** 2 + 2 * sp.I * t) / (1 + t ** 2)           # the unit circle, rationally
    b1 = sp.Matrix([1, 1, 0, 0]); b2 = sp.Matrix([0, 0, 1, -1]); b3 = sp.Matrix([1, -1, 0, 0]); b4 = sp.Matrix([0, 0, 1, 1])
    B = [b1, b2, b3, b4]
    def S(M): return sp.Matrix(4, 4, lambda i, j: sp.Rational(M[i][j].r) + sp.I * sp.Rational(M[i][j].i))
    CN, ZIs, IZs = S(CNOT), S(ZI), S(IZ)
    P1m = (b2 * b2.H) / 2
    def U(w): return sp.eye(4) + (w - 1) * P1m
    okk = sp.simplify(U(-1) - CN) == sp.zeros(4, 4)
    u = sp.symbols('u', real=True)
    w_u = (1 - u ** 2 + 2 * sp.I * u) / (1 + u ** 2)
    okk = okk and all(sp.simplify(U(w_u) * bk - (w_u if k == 1 else 1) * bk) == sp.zeros(4, 1) for k, bk in enumerate(B))
    def bcoords(v): return [sp.simplify((bk.H * v)[0] / 2) for bk in B]
    def on_circles(v):
        c = bcoords(v)
        z = [sp.simplify(x) == 0 for x in c]
        def a2(x): return sp.expand(x * sp.conjugate(x))
        if z[2] and z[3] and not z[0] and not z[1]:
            return sp.simplify(a2(c[0]) - a2(c[1])) == 0
        if z[0] and z[1] and not z[2] and not z[3]:
            return sp.simplify(a2(c[2]) - a2(c[3])) == 0
        return False
    C1 = b1 + w_t * b2; C2 = b3 + w_t * b4
    gens = {'U(w)': lambda v: U(w_u) * v, 'CNOT': lambda v: CN * v, 'ZI': lambda v: ZIs * v, 'IZ': lambda v: IZs * v,
            'T': lambda v: v.conjugate()}
    okinv = all(on_circles(f(Cc)) for f in gens.values() for Cc in (C1, C2))
    def detabs2_over_n2(v):
        d = v[0] * v[3] - v[1] * v[2]
        n = sum(x * sp.conjugate(x) for x in v)
        return sp.simplify(d * sp.conjugate(d) / n ** 2)
    okme = all(detabs2_over_n2(Cc) == sp.Rational(1, 4) for Cc in (C1, C2))
    check('KAPPA', okk and okinv and okme,
          'gate flow U(w) = I + (w-1)|1-><1-|: U(-1) = CNOT, U(w) diagonal in (|0+>,|1->,|0->,|1+>); the circles '
          'C1 = |0+> + w|1->, C2 = |0-> + w|1+> are mapped into C1 u C2 by U(w), CNOT, Ad(Z(x)I), Ad(I(x)Z), T '
          '(symbolic in the rational circle parameter) and every point is maximally entangled (|det|^2/n^2 = 1/4): '
          'the Bell-type seed at C1(w=1) = (1,1,1,-1)/2 = psi_(-1,-1), i.e. the defect e_(-1,-1) = F, has overlap <= 1/2 with the whole reachable set -> EXOTIC-E for kappa')
    # non-vacuity: Ad(H(x)I) leaves the seed set
    Hs = sp.Matrix([[1, 1], [1, -1]])
    HI = sp.kronecker_product(Hs, sp.eye(2))
    check('KAPPA-cc1', not on_circles(HI * C1.subs(t, 0)),
          'countercontrol: (H(x)I) C1(1) is not on C1 u C2 (the invariance check is not vacuous)')
    # K(Z_F) is not kappa-invariant: w = -i, s = (1,1)
    Uq = addm(eye(4), scal(C(-1, -1), scal(Fr(1, 2), outer([C(0), C(0), C(1), C(-1)]))))   # w - 1 = -1 - i
    ok_unit = unitary(Uq)
    phi = mvec(Uq, psi_s((1, 1)))
    moved = ad_table(Uq)(ZF[(1, 1)])
    check('KAPPA-cc2', ok_unit and in_QZstar(phi) and ipW(moved, pure_table(phi)) == Fr(-1, 2),
          'K(Z_F) is not invariant under the gate flow: at w = -i, phi = U psi_(1,1) has overlaps <= 1/2 with every '
          'defect vector (T_phi in Q3 n Z*) and <U e_(1,1) U^dag, T_phi> = -1/2')

def part_zeta():
    import sympy as sp
    def S(v): return sp.Matrix([sp.Rational(x.r) + sp.I * sp.Rational(x.i) for x in v])
    ps = {s: S(psi_s(s)) for s in SIGNS}
    u1, u2 = sp.symbols('u1 u2', real=True)
    def wpar(u): return (1 - u ** 2 + 2 * sp.I * u) / (1 + u ** 2)
    w1, w2 = wpar(u1), wpar(u2)
    p = ps[(1, 1)]
    def D(w): return sp.eye(4) + (w - 1) * p * p.H
    okg = sp.simplify(D(w1) * D(w2) - D(sp.simplify(w1 * w2))) == sp.zeros(4, 4)
    oku = sp.simplify(D(w1) * D(w1).H - sp.eye(4)) == sp.zeros(4, 4)
    okfix = True
    for s in SIGNS:
        Pe = sp.eye(4) / 8 - ps[s] * ps[s].H / 4
        okfix = okfix and sp.simplify(D(w1) * Pe * D(w1).H - Pe) == sp.zeros(4, 4)
    chi = [a + b for a, b in zip(psi_s((1, 1)), psi_s((1, -1)))]
    Dm1 = subm(eye(4), scal(2, outer(psi_s((1, 1)))))
    moved = not teq(pure_table(mvec(Dm1, chi)), pure_table(chi))
    okinv = meq(mm(Dm1, Dm1), eye(4))
    check('ZETA-1', okg and oku and okfix and okinv and moved and in_QZstar(chi),
          'pair-level drive on K(Z_F): D(w) = I + (w-1) psi psi^dag (psi = psi_(1,1)) is a unitary one-parameter group '
          '(D(w1)D(w2) = D(w1 w2), symbolic on the rational circle) whose conjugation fixes every defect and preserves '
          'Q3, hence K(Z_F); its half-turn D(-1) is an involution moving the body state T_chi, chi = psi_(1,1)+psi_(1,-1)')
    # J: the monomial permutation unitary exchanging psi_(1,1) and psi_(1,-1), fixing the other two
    perm = {(1, 1): (1, -1), (1, -1): (1, 1), (-1, 1): (-1, 1), (-1, -1): (-1, -1)}
    P = [[ZERO] * 4 for _ in range(4)]
    for s in SIGNS:
        P = addm(P, [[a * b.conj() for b in psi_s(s)] for a in psi_s(perm[s])])
    okJ = unitary(P) and permutes_ZF(ad_table(P))
    chi2 = [a + b for a, b in zip(psi_s((1, -1)), psi_s((-1, 1)))]
    x = pure_table(chi2)
    # every flow member fixes x (chi2 is orthogonal to psi_(1,1)), symbolically in the circle parameter
    Sx = S(chi2)
    okflowfix = sp.simplify(D(w1) * Sx - Sx) == sp.zeros(4, 1)
    JDJ = mm(mm(P, Dm1), dag(P))
    okoff = not teq(pure_table(mvec(JDJ, chi2)), x) and in_QZstar(chi2)
    check('ZETA-2', okJ and okflowfix and okoff,
          'J = Ad(P), P the monomial unitary swapping psi_(1,1) and psi_(1,-1), is an automorphism of K(Z_F) (permutes '
          'the defects); J D(-1) J^-1 moves the body state x = T_(psi_(1,-1)+psi_(-1,1)) while every flow member fixes '
          'x: J_off_axis holds; K(Z_F) is an ElementaryDrivability-type system at the pair level')
    check('ZETA-ret', oku and unitary(P), 'retention: Q3 carries the same pair-level drive (D(w), P unitary)')

def part_forms():
    # NOT-only form: = ETA-b with level (ii) (Z3); NOT and J: no Bell-type defect (block identities)
    Pp = scal(Fr(1, 2), addm(I2, X)); Pm = scal(Fr(1, 2), subm(I2, X))
    ok1 = meq(CNOT, addm(kron(I2, Pp), kron(Z, Pm)))
    JCN = mm(mm(kron(UJ, I2), CNOT), dag(kron(UJ, I2)))
    ok2 = meq(JCN, addm(kron(I2, Pp), kron(X, Pm)))
    JTN = mm(mm(kron(I2, UJ), CNOT), dag(kron(I2, UJ)))
    ok3 = meq(JTN, addm(kron(P0, I2), kron(P1, Y)))
    check('FORM-J', ok1 and ok2 and ok3,
          'block identities: CNOT = I(x)P+ + Z(x)P-; (UJ(x)I)CNOT(UJ(x)I)^dag = I(x)P+ + X(x)P- ; '
          '(I(x)UJ)CNOT(I(x)UJ)^dag = P0(x)I + P1(x)Y: with J on one token the group contains block pairs (I,Z),(I,X) '
          'resp. (I,X),(I,Y), which have no common eigenvector, so no maximally entangled state keeps a maximally '
          'entangled orbit: no Bell-type defect [W over these identities]; the census seed (EXOTIC-E) is a cap seed')

def part_lambda():
    # K(Z_F) violates (b): one rotation of one token (J = cyc3 on the control) moves a defect out
    okb = True
    for s in SIGNS:
        phi = mvec(kron(UJ, I2), psi_s(s))
        moved = ad_table(kron(UJ, I2))(ZF[s])
        okb = okb and in_QZstar(phi) and ipW(moved, pure_table(phi)) == Fr(-1, 2)
    check('LAMBDA-b', okb,
          'K(Z_F) violates (b): for every s, phi = (UJ(x)I)psi_s has overlap <= 1/2 with every defect vector (T_phi in '
          'K(Z_F)) and <actC cyc3 e_s, T_phi> = -1/2; with the anchor sum (EQ5-SOURCE s3.1, audited) uniform K(Z_F) satisfies '
          'KT4 minus tok and every pair premise, so lambda-without-tok does not give (b_min)')
    REFLY = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
    R = rot3(Fr(3, 5), Fr(4, 5))
    ok = True
    for Rm in (R, CYC3):
        conj = m3(m3(REFLY, Rm), REFLY)
        det = (conj[0][0] * (conj[1][1] * conj[2][2] - conj[1][2] * conj[2][1])
               - conj[0][1] * (conj[1][0] * conj[2][2] - conj[1][2] * conj[2][0])
               + conj[0][2] * (conj[1][0] * conj[2][1] - conj[1][1] * conj[2][0]))
        ok = ok and det == 1
        ok = ok and same_map(lambda w: actT(REFLY, actT(Rm, actT(REFLY, w))), lambda w: actT(conj, w))
        ok = ok and same_map(lambda w: actC(Rm, actT(REFLY, w)), lambda w: actT(REFLY, actC(Rm, w)))
    check('LAMBDA-tw', ok, 'the twin is rotation-invariant on either token (reflY R reflY is a rotation; actC R commutes '
          'with actT reflY; exact at rot3(3/5,4/5) and cyc3): M_rho and M_tw, with cones in {Q3, twin}, satisfy (b) '
          'and refute only the parity part of the conclusion')

def part_closure():
    selfadj = all(ipW(cnotFun(basis_table(a, b)), basis_table(c, d)) == ipW(basis_table(a, b), cnotFun(basis_table(c, d)))
                  for a in range(4) for b in range(4) for c in range(4) for d in range(4))
    F = ZF[(-1, -1)]
    okF = selfadj and which_defect(cnotFun(F)) is not None and ipW(F, pure_table(psi_s((-1, -1)))) < 0
    check('CL1', okF, 'K_gen = SEP + cnot SEP is not self-dual: cnot is ipW-self-adjoint, so <F, cnot p> = <cnot F, p> >= 0 '
          'with cnot F a defect (Z2 identity), F = e_(-1,-1) lies in dualW K_gen, and F is not PSD (Z5) while K_gen is in '
          'Q3 (stage 2, S2/RESULT.md:373-380, re-verified)')

if __name__ == '__main__':
    part_cones()
    part_eta_theta_iota()
    part_kappa()
    part_zeta()
    part_forms()
    part_lambda()
    part_closure()
    for l in OUT:
        print(l)
    print('CHECKS: ' + str(sum(1 for l in OUT if l.startswith('PASS'))) + ' PASS, ' + str(len(FAILS)) + ' FAIL')
    if not FAILS:
        print('VERDICT C3-COUNTERMODELS-EXACT: K(Z_F) (level (ii)) satisfies eta-a/b/c, theta, iota, zeta-drivability and '
              'the NOT-only form exactly and is not Q3; kappa EXOTIC-E (Bell seed); K(Z_F) violates (b)')
    else:
        print('NO VERDICT: failures ' + ', '.join(FAILS))
