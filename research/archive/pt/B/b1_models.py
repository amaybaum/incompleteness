#!/usr/bin/env python3
"""Thread B (PAIR-ACT), script b1_models -- the weaker gate clauses against exact countermodels, and the orientation
obstruction.  Research only.

Exact arithmetic only (sympy Rationals, Gaussian rationals, rational functions); no floating point, no randomness, no
time-dependence in stdout.  Run as:  python3 -I -B b1_models.py <pt-root>   (reads base/ Lean sources only).

OBJECTS (pair-level data (K, N, A, B, A', B') with N = actC A . actT B . cnot . actC A' . actT B')
  gates  g_cnot = cnot (all locals I);  g_D = actT reflY . cnot (B = reflY);  g_pre = cnot . actT reflY (B' = reflY);
         g_Tw = actT reflY . cnot . actT reflY (B = B' = reflY)
  cones  Q3, twin = actT reflY Q3, maxCone = maxCone (eball 3), SEP = cone of the product states, Kint = int maxCone u Q3
  clauses (all relative to one pair; a family satisfies a clause iff all four pairs do)
    hgate   N K <= K
    PREC    N . actC C . actT D maps K into K for some orthogonal C, D        (hgate up to a pre-local correction)
    SECT    N SEP <= K n dualW K                    = SECTst and SECTef
    SECTst  N (prodState x y) in K for x, y in eball 3                         (the 'product-state' half; P-PROD)
    SECTef  N SEP <= dualW K, equivalently N^-1 K <= maxCone                   (the 'product-effect' half)
    OQ1     SECTst and BD                                                       (result.md open question 1)
    CONS    (L) and BD: the clause the design proof consumes (b1_consumed)
    BS, BD  bellOf A B in K, in dualW K
    PRP     N and N^-1 map product states into K                               (EQ5-PREM's product-level reversibility)
    TBP     N K <= maxCone and N^-1 K <= maxCone                                (DIM-1's two-sided positivity, lifted to K)
    SECT'   N^-1 SEP <= K n dualW K                                            (the mirror of SECT)
  models (four pairs 01, 23, 02, 13; gate g_cnot and cone as stated unless a pair is named)
    M_Q uniform Q3 | M_D uniform Q3, g_D at 13 | M_max uniform maxCone | M_SEP uniform SEP | M_maxD uniform maxCone,
    g_D at 13 | M_maxT uniform maxCone, g_Tw at 13 | M_SEPD uniform SEP, g_D at 13 | M_pre uniform Q3, g_pre at 13 |
    M_DD cones (Q3, twin, Q3, twin), g_D at 23 and 13 | TWIN uniform twin | M_int uniform Kint

KINDS OF CHECKS
  identity  an exact symbolic identity; witness  an exact value at fixed objects decisive for an existential or a
  failure; enumerate  an exhaustive finite enumeration; sample  exact values at fixed points (evidence only);
  countercontrol  a mutated object that must give the opposite verdict (PASS iff the mutated object fails).

MATRIX AND DECISION RULE (fixed before the first run)
  Each matrix cell (model, clause) records a value (holds / fails) and the check ids it rests on, with its basis:
  X = decided by an exact witness or identity in this script; W = a written reduction (stated in the cell note) whose
  exact ingredients are the listed checks; K = a landed fact replayed (landed_replay/).  A cell is valid iff every
  check it lists passed.  The hypothesis column H0 = hcls and hadm and hcl and H, and C = IE1 and EvenCycle.
  Rules, applied mechanically to the valid cells:
   R1 'strictly weaker than hgate (relative to H0)':  clause X is reported so iff some model has H0, X and not hgate.
   R2 'insufficient (relative to H0)':                 iff some model has H0, X and not C.
   R3 'fails where H0 holds and C fails':              iff X fails in every model with H0 and not C.
   R4 the value of X at M_max and at M_D is reported as measured.
   R5 obstruction consistency: for each clause shown sigma-invariant (S6) and each model all of whose cones are
      actT reflY-invariant (maxCone, SEP), a clause reported sufficient elsewhere must fail there (else the script
      reports an INCONSISTENCY and no verdict).
  VERDICT lines print only if every check passed (all controls green, every countercontrol gave the opposite
  verdict).  Otherwise the script prints 'b1_models: NO VERDICT' and exits 1.
"""
import re
import sys
from itertools import product
from pathlib import Path

import sympy as sp

Q = sp.Rational
iu = sp.I
R4 = range(4)
CHECKS = {}
ORDER = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    assert cid not in CHECKS, cid
    CHECKS[cid] = (kind, ok)
    ORDER.append(cid)
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def section(t):
    print()
    print(f'== {t}', flush=True)


def z(v):
    return sp.cancel(sp.together(sp.expand(v))) == 0


def mzero(M):
    return all(z(v) for v in M)


if len(sys.argv) != 2:
    print('usage: b1_models.py <pt-root>')
    sys.exit(2)
ROOT = Path(sys.argv[1]).resolve()
LEAN_BASE = ROOT / 'base' / 'verification' / 'lean-mathlib' / 'OIBridge'

# ---------------------------------------------------------------------------------------------------------------
# conventions (own transcription; S0 checks them against the landed sources)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def sgn(m, n):
    return -1 if (m, n) in NEG else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


def pairVal(a, b, w):
    return (sp.Matrix(a).T * w * sp.Matrix(b))[0, 0]


def dg(p, q, r, s):
    return sp.diag(p, q, r, s)


def fourVal(X, Y, E, F):
    return sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d] for a, b, c, d in product(R4, repeat=4))


def famII(e, f, L, Lp):
    return sum(e[a, b] * f[c, d] * L[a, c] * Lp[b, d] for a, b, c, d in product(R4, repeat=4))


phiW = dg(1, 1, -1, 1)
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
E00 = dg(1, 0, 0, 0)
reflY = sp.diag(1, -1, 1)
I3 = sp.eye(3)
xplus = [1, 0, 0]
z3 = [0, 0, 1]
SHARP_NEGX = [Q(1, 2), Q(-1, 2), 0, 0]
SHARP_NEGZ = [Q(1, 2), 0, 0, Q(-1, 2)]

S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def kron(A, B):
    return sp.kronecker_product(A, B)


SS = [[kron(S[m], S[n]) for n in R4] for m in R4]


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * SS[m][n]
    return out / 4


def dag(M):
    return M.conjugate().T


def ptrans2(M):
    out = sp.zeros(4, 4)
    for i1, j1, i2, j2 in product(range(2), repeat=4):
        out[2 * i1 + i2, 2 * j1 + j2] = M[2 * i1 + j2, 2 * j1 + i2]
    return out


CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


def rho1(x):
    return (S[0] + sum((x[i] * S[i + 1] for i in range(3)), sp.zeros(2, 2))) / 2


def is_psd(M):
    """exact: a Hermitian matrix is PSD iff all of its principal minors are >= 0"""
    n = M.shape[0]
    if not mzero(M - dag(M)):
        return False
    for k in range(1, n + 1):
        for idx in __import__('itertools').combinations(range(n), k):
            d = sp.expand(M.extract(list(idx), list(idx)).det())
            if sp.im(d) != 0 or sp.re(d) < 0:
                return False
    return True


def inQ3(w):
    return is_psd(pauliW(w))


def quad(M, v):
    v = sp.Matrix(v)
    return sp.expand((dag(v) * M * v)[0, 0])


def in_L(a):
    return a[0] >= 0 and a[0] ** 2 - a[1] ** 2 - a[2] ** 2 - a[3] ** 2 >= 0


def symtab(nm):
    return sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'{nm}{m}{n}', real=True))


def symmat3(nm):
    return sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'{nm}{i}{j}', real=True))


def symvec(nm, k):
    return [sp.Symbol(f'{nm}{i}', real=True) for i in range(k)]


def nclass(A, B, Ap, Bp, w):
    return actC(A, actT(B, cnot(actC(Ap, actT(Bp, w)))))


def Rz(c, s):
    return sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def Rx(c, s):
    return sp.Matrix([[1, 0, 0], [0, c, -s], [0, s, c]])


# the four gates: (N, inverse, A, B, A', B')
GATES = {
    'g_cnot': (lambda w: cnot(w), lambda w: cnot(w), I3, I3, I3, I3),
    'g_D': (lambda w: actT(reflY, cnot(w)), lambda w: cnot(actT(reflY, w)), I3, reflY, I3, I3),
    'g_pre': (lambda w: cnot(actT(reflY, w)), lambda w: actT(reflY, cnot(w)), I3, I3, I3, reflY),
    'g_Tw': (lambda w: actT(reflY, cnot(actT(reflY, w))), lambda w: actT(reflY, cnot(actT(reflY, w))),
             I3, reflY, I3, reflY),
}


def orient(A, B):
    return sp.Matrix(A).det() * sp.Matrix(B).det() == -1


W = symtab('w')
Eg, Xg, Yg, Fg = symtab('E'), symtab('X'), symtab('Y'), symtab('F')
xs, ys = symvec('x', 3), symvec('y', 3)
a4, b4 = symvec('a', 4), symvec('b', 4)

# ===============================================================================================================
section('S0  transcription of the landed tables')
CD = (LEAN_BASE / 'CompositeDimension.lean').read_text(encoding='utf-8')
KG = (LEAN_BASE / 'K2Guard.lean').read_text(encoding='utf-8')
msg = re.search(r'^def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) '
                r'then -1 else 1$', CD, re.M)
neg_src = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))} if msg else None


def lean_table(nm):
    mm = re.search(rf'^def {nm} : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){{4}})', CD, re.M)
    if not mm:
        return None
    T = [[None] * 4 for _ in R4]
    for a, b, v in re.findall(r'\|\s*(\d),\s*(\d)\s*=>\s*(\d)', mm.group(1)):
        T[int(a)][int(b)] = int(v)
    return T


def lean_w3(nm):
    mm = re.search(rf'^def {nm} : W 3 := !\[(.*)\]$', KG, re.M)
    if not mm:
        return None
    rows = re.findall(r'!\[([^\]]*)\]', mm.group(1))
    return sp.Matrix([[int(v) for v in r.split(',')] for r in rows])


chk('S0.tables', 'landed sgn, pc, pt, phiW, idW, chainW, reflY match this script\'s transcription',
    neg_src == NEG and lean_table('pc') == PC and lean_table('pt') == PT
    and 'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD
    and lean_w3('idW') == idW and lean_w3('chainW') == chainW
    and 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i' in KG, 'source')

# ===============================================================================================================
section('S1  the dictionary facts the reductions use (re-derived here; the landed probe replay covers D1-D7, F0-F10)')
chk('D1', 'pauliW (cnot w) = CNOT pauliW(w) CNOT^dagger, symbolic w', mzero(pauliW(cnot(W)) - CNOT * pauliW(W) * dag(CNOT)),
    'identity')
chk('D5', 'pauliW (prodState x y) = rho(x) (x) rho(y), symbolic', mzero(pauliW(prodState(xs, ys)) - kron(rho1(xs), rho1(ys))),
    'identity')
r_ = rho1(xs)
chk('D6', 'rho(x) is Hermitian with trace 1 and det (1 - |x|^2)/4 (so PSD iff |x| <= 1)',
    mzero(r_ - dag(r_)) and z(r_.trace() - 1) and z(r_.det() - (1 - xs[0] ** 2 - xs[1] ** 2 - xs[2] ** 2) / 4), 'identity')
chk('Dpt', 'pauliW (actT reflY w) = partial transpose (second qubit) of pauliW(w), symbolic: twin = PT2(Q3)',
    mzero(pauliW(actT(reflY, W)) - ptrans2(pauliW(W))), 'identity')
chk('Dtr', 'pauliW (actC reflY (actT reflY w)) = pauliW(w)^T, symbolic (full transpose; so actC reflY Q3 = '
    'transpose(actT reflY Q3) = twin)', mzero(pauliW(actC(reflY, actT(reflY, W))) - pauliW(W).T), 'identity')
Rg = symmat3('R')
chk('Dmax', 'pairVal a b (actT R w) = pairVal a (homMap R^T b) w and pairVal a b (actC R w) = pairVal (homMap R^T a) b w, '
    'symbolic R (orthogonal R preserve the Lorentz cone L, so maxCone is invariant under actC R, actT R)',
    z(pairVal(a4, b4, actT(Rg, W)) - pairVal(a4, list(homMap(Rg.T) * sp.Matrix(b4)), W))
    and z(pairVal(a4, b4, actC(Rg, W)) - pairVal(list(homMap(Rg.T) * sp.Matrix(a4)), b4, W)), 'identity')
rb = homMap(reflY) * sp.Matrix(b4)
chk('DL', 'homMap reflY preserves the Lorentz form b0^2 - |b|^2 and b0 (so it maps L onto L)',
    z(rb[0] - b4[0]) and z(rb[0] ** 2 - rb[1] ** 2 - rb[2] ** 2 - rb[3] ** 2
                         - (b4[0] ** 2 - b4[1] ** 2 - b4[2] ** 2 - b4[3] ** 2)), 'identity')
chk('Dadj', 'ipW (actT reflY E) X = ipW E (actT reflY X), symbolic (so dualW (actT reflY K) = actT reflY (dualW K))',
    z(ipW(actT(reflY, Eg), Xg) - ipW(Eg, actT(reflY, Xg))), 'identity')
chk('Dsep', 'actT reflY (prodState x y) = prodState x (reflY y) and |reflY y|^2 = |y|^2 (SEP is actT reflY-invariant; '
    'so is the ball)', mzero(actT(reflY, prodState(xs, ys)) - prodState(xs, list(reflY * sp.Matrix(ys))))
    and z(sum(v ** 2 for v in reflY * sp.Matrix(ys)) - sum(v ** 2 for v in ys)), 'identity')
Mg, Ng = symmat3('M'), symmat3('N')
chk('Dloc', 'actC M (actT M\' (prodState x y)) = prodState (M x) (M\' y), symbolic M, M\' (local maps send products to '
    'products; orthogonal ones keep the ball, so they preserve SEP)', mzero(actC(Mg, actT(Ng, prodState(xs, ys)))
    - prodState(list(Mg * sp.Matrix(xs)), list(Ng * sp.Matrix(ys)))), 'identity')
chk('Dorth', '|R^T b|^2 = b^T (R R^T) b, symbolic R, b (so orthogonal R keep the Lorentz cone L; with Dmax every local '
    'orthogonal map preserves maxCone)', z(sum(v ** 2 for v in Rg.T * sp.Matrix(b4[1:])) - (sp.Matrix(b4[1:]).T * Rg * Rg.T * sp.Matrix(b4[1:]))[0, 0]),
    'identity')
chk('Dpv', 'pairVal a b w = ipW (a b^T) w, symbolic: SEP* = maxCone and maxCone* = SEP read through tables',
    z(pairVal(a4, b4, W) - ipW(sp.Matrix(a4) * sp.Matrix(b4).T, W)), 'identity')

# ===============================================================================================================
section('S2  the four gates: N-CLASS form, inverse, orientation bit')
for gname, (N, Ninv, A, B, Ap, Bp) in GATES.items():
    ok_form = mzero(N(W) - nclass(A, B, Ap, Bp, W))
    ok_inv = mzero(Ninv(N(W)) - W) and mzero(N(Ninv(W)) - W)
    ok_orth = all(M.T * M == I3 for M in (A, B, Ap, Bp))
    chk(f'G.{gname}', f'{gname}: N = actC A actT B cnot actC A\' actT B\' with orthogonal locals; the stated inverse '
        f'is a two-sided inverse; orient(A, B) = {orient(A, B)}', ok_form and ok_inv and ok_orth, 'identity')
chk('G.orient', 'orientation bits: g_cnot false, g_D true, g_pre false, g_Tw true',
    [orient(GATES[g][2], GATES[g][3]) for g in ('g_cnot', 'g_D', 'g_pre', 'g_Tw')] == [False, True, False, True],
    'enumerate')
chk('G.cc', 'countercontrol: actT reflY . cnot is not of N-CLASS form with B = I (the post-local is read)',
    not mzero(actT(reflY, cnot(W)) - nclass(I3, I3, I3, I3, W)), 'countercontrol')

# ===============================================================================================================
section('S3  membership witnesses (decisive for every "fails" cell)')
singlet = sp.Matrix([0, 1, -1, 0])
chk('W1', 'phiW in Q3 (pauliW phiW is PSD: all principal minors >= 0)', inQ3(phiW), 'witness')
chk('W2', 'idW not in Q3: the singlet value of pauliW idW is -1', quad(pauliW(idW), singlet) == -1, 'witness')
chk('W2t', 'idW in twin: actT reflY idW = phiW in Q3', actT(reflY, idW) == phiW and inQ3(actT(reflY, idW)), 'witness')
chk('W3', 'phiW not in twin: actT reflY phiW = idW, not in Q3 (W2)', actT(reflY, phiW) == idW, 'witness')
okL = in_L(SHARP_NEGX) and in_L(SHARP_NEGZ)
chk('W4', 'chainW not in maxCone: pairVal at the sharp effects of -e1, -e3 (both in L) is -1/2',
    okL and pairVal(SHARP_NEGX, SHARP_NEGZ, chainW) == Q(-1, 2), 'witness')
chk('W5', 'dg(1,-1,1,-1) in maxCone (pairVal = a0 b0 - a1 b1 + a2 b2 - a3 b3 >= a0 b0 - |a||b| >= 0 by Cauchy-Schwarz) '
    'and ipW phiW dg(1,-1,1,-1) = -2: phiW not in dualW maxCone',
    z(pairVal(a4, b4, dg(1, -1, 1, -1)) - (a4[0] * b4[0] - a4[1] * b4[1] + a4[2] * b4[2] - a4[3] * b4[3]))
    and ipW(phiW, dg(1, -1, 1, -1)) == -2, 'witness')
chk('W6', 'dg(1,-1,-1,-1) in Q3 (pauliW = singlet projector, PSD) and ipW idW dg(1,-1,-1,-1) = -2: idW not in dualW Q3',
    inQ3(dg(1, -1, -1, -1)) and ipW(idW, dg(1, -1, -1, -1)) == -2, 'witness')
xv, yv = sp.Matrix(xs), sp.Matrix(ys)
Dp = sp.diag(1, -1, 1)
chk('W7', 'phiW not in SEP: F = dg(1,-1,1,-1) has ipW F (prodState x y) = |x - D y|^2/2 + (1-|x|^2)/2 + (1-|y|^2)/2 '
    '(>= 0 on the ball; D = diag(1,-1,1)) and ipW F phiW = -2',
    z(ipW(dg(1, -1, 1, -1), prodState(xs, ys))
      - ((xv - Dp * yv).dot(xv - Dp * yv) / 2 + (1 - xv.dot(xv)) / 2 + (1 - yv.dot(yv)) / 2))
    and ipW(dg(1, -1, 1, -1), phiW) == -2, 'witness')
chk('W8', 'idW not in SEP: F\' = dg(1,-1,-1,-1) has ipW F\' (prodState x y) = |x - y|^2/2 + (1-|x|^2)/2 + (1-|y|^2)/2 '
    'and ipW F\' idW = -2', z(ipW(dg(1, -1, -1, -1), prodState(xs, ys))
                              - ((xv - yv).dot(xv - yv) / 2 + (1 - xv.dot(xv)) / 2 + (1 - yv.dot(yv)) / 2))
    and ipW(dg(1, -1, -1, -1), idW) == -2, 'witness')
chk('W9', 'phiW and idW lie in maxCone = SEP*: pairVal a b phiW = a0b0 + a1b1 - a2b2 + a3b3 and pairVal a b idW = '
    'a0b0 + a.b, each >= a0 b0 - |a||b| >= 0 (Cauchy-Schwarz)',
    z(pairVal(a4, b4, phiW) - (a4[0] * b4[0] + a4[1] * b4[1] - a4[2] * b4[2] + a4[3] * b4[3]))
    and z(pairVal(a4, b4, idW) - sum(a4[i] * b4[i] for i in R4)), 'identity')
chk('W10', 'dg(2,-1,1,-1) = E00 + dg(1,-1,1,-1) lies in int maxCone (pairVal >= a0 b0 > 0 on nonzero L x L) and '
    'ipW phiW dg(2,-1,1,-1) = -1: phiW not in dualW Kint',
    z(pairVal(a4, b4, dg(2, -1, 1, -1)) - (a4[0] * b4[0] + pairVal(a4, b4, dg(1, -1, 1, -1))))
    and ipW(phiW, dg(2, -1, 1, -1)) == -1, 'witness')
chk('W11', 'prodState xplus z3 lies in twin: actT reflY fixes it (reflY z3 = z3) and it lies in Q3 (D5, D6)',
    actT(reflY, prodState(xplus, z3)) == prodState(xplus, z3) and inQ3(prodState(xplus, z3)), 'witness')
gD, gDi = GATES['g_D'][0], GATES['g_D'][1]
gP, gPi = GATES['g_pre'][0], GATES['g_pre'][1]
gT = GATES['g_Tw'][0]
pxz = prodState(xplus, z3)
chk('W12', 'chains: cnot idW = chainW; actT reflY chainW = chainW; g_D: pxz -> idW -> chainW; g_pre: pxz -> phiW -> '
    'chainW; g_Tw: phiW -> chainW; g_D^-1 phiW = chainW; g_pre^-1 pxz = idW',
    cnot(idW) == chainW and actT(reflY, chainW) == chainW and gD(pxz) == idW and gD(idW) == chainW
    and gP(pxz) == phiW and gP(phiW) == chainW and gT(phiW) == chainW and gDi(phiW) == chainW
    and gPi(pxz) == idW, 'witness')
chk('W13', 'the M_D gate puts the M_Q Bell table off Q3: bellOf(I, reflY) = actT reflY phiW = idW (W2)',
    actC(I3, actT(reflY, phiW)) == idW, 'witness')
chk('W14', 'pre-corrections: g_D . actT reflY = g_Tw and g_pre . actT reflY = cnot (symbolic); cnot pxz = phiW',
    mzero(gD(actT(reflY, W)) - gT(W)) and mzero(gP(actT(reflY, W)) - cnot(W)) and cnot(pxz) == phiW, 'identity')
chk('W.cc', 'countercontrol: the twin Bell table idW is in twin (W2t) while the Q3 Bell table phiW is not (W3): the cone '
    'and the post-local must match', inQ3(actT(reflY, idW)) and not inQ3(actT(reflY, phiW)), 'countercontrol')

# ===============================================================================================================
section('S4  gate images of product states and the link family (reductions for the "holds" cells)')
chk('P1', 'g_D (prodState x y) = actT reflY (cnot (prodState x y)) and g_D^-1 (prodState x y) = cnot (prodState x (reflY y))',
    mzero(gD(prodState(xs, ys)) - actT(reflY, cnot(prodState(xs, ys))))
    and mzero(gDi(prodState(xs, ys)) - cnot(prodState(xs, list(reflY * yv)))), 'identity')
chk('P2', 'g_pre (prodState x y) = cnot (prodState x (reflY y)) and g_pre^-1 = actT reflY . cnot',
    mzero(gP(prodState(xs, ys)) - cnot(prodState(xs, list(reflY * yv))))
    and mzero(gPi(W) - actT(reflY, cnot(W))), 'identity')
chk('P3', 'g_Tw (prodState x y) = actT reflY (cnot (prodState x (reflY y))) and g_Tw is an involution',
    mzero(gT(prodState(xs, ys)) - actT(reflY, cnot(prodState(xs, list(reflY * yv))))) and mzero(gT(gT(W)) - W),
    'identity')
m1, m2 = sp.symbols('m1 m2', real=True)
c1, s1 = (1 - m1 ** 2) / (1 + m1 ** 2), 2 * m1 / (1 + m1 ** 2)
c2, s2 = (1 - m2 ** 2) / (1 + m2 ** 2), 2 * m2 / (1 + m2 ** 2)
RZ, RX = Rz(c1, s1), Rx(c2, s2)
LINK = actC(RZ * RX, phiW)
chk('L1', 'link tables with post-locals (I, I): actC (Rz Rx) phiW = cnot (prodState (Rz xplus) (Rx z3)), symbolic angles '
    '(so they lie in Q3 by D1, D5, D6)', mzero(cnot(prodState(list(RZ * sp.Matrix(xplus)), list(RX * sp.Matrix(z3))))
                                          - LINK), 'identity')
chk('L2', 'link tables with post-locals (I, reflY): actC (Rz Rx) (actT reflY phiW) = actT reflY (actC (Rz Rx) phiW) '
    '(so they lie in twin)', mzero(actC(RZ * RX, actT(reflY, phiW)) - actT(reflY, LINK)), 'identity')
LINKs = LINK.subs({m1: Q(1, 2), m2: Q(1, 3)})
chk('L3', 'sample: at m1 = 1/2, m2 = 1/3 the (I, I) link table is in Q3 and its actT reflY image is in twin (exact PSD)',
    inQ3(LINKs) and inQ3(actT(reflY, actT(reflY, LINKs))), 'sample')
chk('L.cc', 'countercontrol: at the same sample the (I, reflY) link table is not in Q3 (it is in twin only)',
    not inQ3(actT(reflY, LINKs)), 'countercontrol')

# ===============================================================================================================
section('S5  four-copy interface: transports and uniform SEP')
r = reflY
chk('F.t3', 'token-3 chart: fourVal X (actT r Y) E (actT r F) = fourVal X Y E F and famII e (actT r f) L (actT r L\') = '
    'famII e f L L\', symbolic (FCC(Q3,twin,Q3,twin) <=> FCC(Q3,Q3,Q3,Q3), with Dadj for the duals)',
    z(fourVal(Xg, actT(r, Yg), Eg, actT(r, Fg)) - fourVal(Xg, Yg, Eg, Fg))
    and z(famII(Eg, actT(r, Fg), Xg, actT(r, Yg)) - famII(Eg, Fg, Xg, Yg)), 'identity')
chk('F.t12', 'tokens-1,2 chart: fourVal (actT r X) (actC r Y) (actT r E) (actC r F) = fourVal X Y E F and the famII form '
    'likewise, symbolic (uniform twin <=> uniform Q3, with Dtr: actC reflY Q3 = twin)',
    z(fourVal(actT(r, Xg), actC(r, Yg), actT(r, Eg), actC(r, Fg)) - fourVal(Xg, Yg, Eg, Fg))
    and z(famII(actT(r, Eg), actC(r, Fg), actT(r, Xg), actC(r, Yg)) - famII(Eg, Fg, Xg, Yg)), 'identity')
chk('F.cc', 'countercontrol: transporting Y but not F (token 3 read on one side only) breaks the identity',
    not z(fourVal(Xg, actT(r, Yg), Eg, Fg) - fourVal(Xg, Yg, Eg, Fg)), 'countercontrol')
xp, yp = symvec('p', 3), symvec('q', 3)
chk('F.sep', 'uniform SEP: fourVal (prodState x x\') (prodState y y\') E F = (x^ E y^)(x\'^ F y\'^) and the famII value '
    'on products factors the same way, symbolic (with E, F in SEP* = maxCone both factors are >= 0)',
    z(fourVal(prodState(xs, xp), prodState(ys, yp), Eg, Fg)
      - pairVal(hom(xs), hom(ys), Eg) * pairVal(hom(xp), hom(yp), Fg))
    and z(famII(Eg, Fg, prodState(xs, xp), prodState(ys, yp))
          - pairVal(hom(xs), hom(ys), Eg) * pairVal(hom(xp), hom(yp), Fg)), 'identity')

# ===============================================================================================================
section('S6  the orientation obstruction: sigma and tau, and the 16 patterns on orientation-blind cones')
A, B, Ap, Bp = symmat3('A'), symmat3('B'), symmat3('P'), symmat3('S')
chk('O1', 'sigma: actT reflY . N(A,B,A\',B\') = N(A, reflY B, A\', B\'), symbolic locals (post-composition stays N-CLASS)',
    mzero(actT(reflY, nclass(A, B, Ap, Bp, W)) - nclass(A, reflY * B, Ap, Bp, W)), 'identity')
chk('O2', 'det(reflY B) = -det B, symbolic: sigma flips orient(A, B)', z((reflY * B).det() + B.det()), 'identity')
chk('O3', 'tau: actT reflY . N(A,B,A\',B\') . actT reflY = N(A, reflY B, A\', B\' reflY), symbolic',
    mzero(actT(reflY, nclass(A, B, Ap, Bp, actT(reflY, W))) - nclass(A, reflY * B, Ap, Bp * reflY, W)), 'identity')
chk('O4', '(L) and the Bell table under sigma: actC (A Rz Rx) (actT (reflY B) phiW) = actT reflY (actC (A Rz Rx) (actT B '
    'phiW)), symbolic (CONS, OQ1, SECT, PREC, hgate are sigma-invariant on actT reflY-invariant cones, with Dmax, Dsep, '
    'Dadj)', mzero(actC(A * RZ * RX, actT(reflY * B, phiW)) - actT(reflY, actC(A * RZ * RX, actT(B, phiW)))), 'identity')
chk('O.cc', 'countercontrol: sigma on the control side (actC reflY) changes A, not B: actC reflY . N(A,B,..) differs from '
    'N(A, reflY B, ..)', not mzero(actC(reflY, nclass(A, B, Ap, Bp, W)) - nclass(A, reflY * B, Ap, Bp, W)), 'countercontrol')
pairs = ('p01', 'p23', 'p02', 'p13')
even = 0
odd = 0
for pat in product(('g_cnot', 'g_D'), repeat=4):
    bits = [orient(GATES[g][2], GATES[g][3]) for g in pat]
    if sum(bits) % 2 == 0:
        even += 1
    else:
        odd += 1
chk('O5', 'the 16 gate patterns in {g_cnot, g_D}^4 on uniform maxCone (or SEP): hcls, hadm, hcl, H and IE1 do not read '
    'the gates beyond N-CLASS, and EvenCycle holds for exactly the even patterns', (even, odd) == (8, 8), 'enumerate',
    f'{even} even, {odd} odd')
chk('O6', 'the obstruction does not reach Q3: phiW in Q3 and actT reflY phiW = idW not in Q3 (Q3 is not actT '
    'reflY-invariant)', inQ3(phiW) and not inQ3(actT(reflY, phiW)), 'witness')

# ===============================================================================================================
section('S7  the matrix')

# H0 bases (written reductions over landed facts and S1/S5 identities)
H0_BASIS = {
    'Q3': 'W[landed D1-D7, F2, H1-H10 replayed; D5, D6]',
    'maxCone': 'W[landed F4-F6, M_max.2, H1-H10 replayed]',
    'SEP': 'W[F.sep; landed prodState_mem_maxCone; H1-H10 replayed]',
    'twin-mix': 'W[F.t3 or F.t12, Dtr, Dpt, Dadj; uniform Q3]',
}
# each model: cones per pair, gates per pair, H0 basis key, C value and basis
MODELS = {
    'M_Q': (('Q3',) * 4, ('g_cnot',) * 4, 'Q3'),
    'M_D': (('Q3',) * 4, ('g_cnot', 'g_cnot', 'g_cnot', 'g_D'), 'Q3'),
    'M_max': (('maxCone',) * 4, ('g_cnot',) * 4, 'maxCone'),
    'M_SEP': (('SEP',) * 4, ('g_cnot',) * 4, 'SEP'),
    'M_maxD': (('maxCone',) * 4, ('g_cnot', 'g_cnot', 'g_cnot', 'g_D'), 'maxCone'),
    'M_maxT': (('maxCone',) * 4, ('g_cnot', 'g_cnot', 'g_cnot', 'g_Tw'), 'maxCone'),
    'M_SEPD': (('SEP',) * 4, ('g_cnot', 'g_cnot', 'g_cnot', 'g_D'), 'SEP'),
    'M_pre': (('Q3',) * 4, ('g_cnot', 'g_cnot', 'g_cnot', 'g_pre'), 'Q3'),
    'M_DD': (('Q3', 'twin', 'Q3', 'twin'), ('g_cnot', 'g_D', 'g_cnot', 'g_D'), 'twin-mix'),
    'TWIN': (('twin',) * 4, ('g_cnot',) * 4, 'twin-mix'),
    'M_int': (('Kint',) * 4, ('g_cnot',) * 4, 'maxCone'),
}
IE1_OF = {'Q3': True, 'twin': True, 'maxCone': True, 'SEP': True, 'Kint': True}


def evencycle(gates):
    return sum(orient(GATES[g][2], GATES[g][3]) for g in gates) % 2 == 0


# per (cone, gate) pair-level clause values with their check ids; 'W' = written reduction with exact ingredients
# (value, basis, ids, note)
PAIR = {}


def setp(cone, gate, clause, val, basis, ids, note=''):
    PAIR[(cone, gate, clause)] = (val, basis, tuple(ids), note)


# --- (Q3, g_cnot): everything holds (hgate by D1)
for cl in ('hgate', 'PREC', 'SECT', 'SECTst', 'SECTef', 'OQ1', 'CONS', 'BS', 'BD', 'PRP', 'TBP', "SECT'"):
    setp('Q3', 'g_cnot', cl, True, 'W', ('D1', 'D5', 'D6', 'W1', 'L1'), 'cnot is conjugation by CNOT; Q3 self-dual')
# --- (Q3, g_D): M_D's twisted pair
setp('Q3', 'g_D', 'hgate', False, 'X', ('W12', 'W2', 'W1'), 'g_D pxz = idW not in Q3')
setp('Q3', 'g_D', 'PREC', False, 'W', ('W12', 'W2', 'W2t', 'W4', 'Dpt', 'Dtr', 'D1', 'landed:D7'),
     'N . L maps Q3 to actT reflY cnot (L Q3); L Q3 in {Q3, twin} (chart rule: D7, Dpt, Dtr): g_D Q3 contains '
     'idW not in Q3, and cnot twin contains chainW')
for cl in ('SECT', 'SECTst', 'OQ1', 'CONS', 'BS', 'PRP'):
    setp('Q3', 'g_D', cl, False, 'X', ('W12', 'W2', 'W13'), 'g_D pxz = bellOf(I, reflY) = idW not in Q3')
setp('Q3', 'g_D', 'BD', False, 'X', ('W6', 'W13'), 'idW not in dualW Q3')
setp('Q3', 'g_D', 'SECTef', False, 'X', ('W1', 'W12', 'W4'), 'phiW in Q3 and g_D^-1 phiW = chainW not in maxCone')
setp('Q3', 'g_D', 'TBP', False, 'X', ('W1', 'W12', 'W4'), 'phiW in Q3 and g_D^-1 phiW = chainW not in maxCone')
setp('Q3', 'g_D', "SECT'", True, 'W', ('P1', 'Dsep', 'D1', 'D5', 'D6', 'Dmax', 'DL', 'Dpt'),
     'g_D^-1 (products) = cnot (products) in Q3 = Q3*; g_D Q3 = twin in maxCone')
# --- (maxCone, g_cnot): M_max
setp('maxCone', 'g_cnot', 'hgate', False, 'X', ('W9', 'W12', 'W4'), 'idW in maxCone, cnot idW = chainW')
setp('maxCone', 'g_cnot', 'PREC', False, 'W', ('W9', 'W12', 'W4', 'Dmax', 'Dorth'),
     'L maxCone = maxCone for local orthogonal L, so PREC = hgate here')
setp('maxCone', 'g_cnot', 'SECTst', True, 'K', ('landed:cnot_prodState_mem_maxCone',), 'CD:1152')
setp('maxCone', 'g_cnot', 'PRP', True, 'K', ('landed:cnot_prodState_mem_maxCone',), 'cnot involution')
setp('maxCone', 'g_cnot', 'BS', True, 'X', ('W9',), 'phiW in maxCone')
for cl in ('BD', 'CONS', 'OQ1', 'SECT'):
    setp('maxCone', 'g_cnot', cl, False, 'X', ('W5',), 'phiW not in dualW maxCone (landed X6)')
setp('maxCone', 'g_cnot', 'SECTef', False, 'X', ('W9', 'W12', 'W4'), 'cnot^-1 idW = chainW not in maxCone')
setp('maxCone', 'g_cnot', 'TBP', False, 'X', ('W9', 'W12', 'W4'), 'same witness')
setp('maxCone', 'g_cnot', "SECT'", False, 'X', ('W9', 'W12', 'W4'), 'N maxCone not in maxCone')
# --- (maxCone, g_D) and (maxCone, g_Tw): one twisted pair on maxCone
for g in ('g_D', 'g_Tw'):
    setp('maxCone', g, 'hgate', False, 'X', ('W9', 'W12', 'W4'), 'g(idW) or g(phiW) = chainW')
    setp('maxCone', g, 'SECTst', True, 'W', ('P1', 'P3', 'Dmax', 'DL', 'Dsep', 'landed:cnot_prodState_mem_maxCone'),
         'g(prodState x y) = actT reflY cnot(prodState x y\'), maxCone actT reflY-invariant')
    setp('maxCone', g, 'PRP', True, 'W', ('P1', 'P3', 'Dmax', 'DL', 'Dsep', 'landed:cnot_prodState_mem_maxCone'),
         'inverse images of products likewise')
    setp('maxCone', g, 'BD', False, 'X', ('W13', 'W8', 'Dpv'), 'bellOf = idW not in SEP = maxCone*')
    setp('maxCone', g, 'BS', True, 'X', ('W13', 'W9'), 'bellOf = idW in maxCone')
    for cl in ('CONS', 'OQ1', 'SECT'):
        setp('maxCone', g, cl, False, 'X', ('W13', 'W8'), 'BD fails')
# --- (SEP, g_cnot): M_SEP
for cl in ('hgate', 'PREC', 'SECTst', 'SECT', 'OQ1', 'CONS', 'BS', 'PRP', "SECT'"):
    setp('SEP', 'g_cnot', cl, False, 'X', ('W14', 'W7', 'Dsep', 'Dloc'), 'cnot pxz = phiW not in SEP (L SEP = SEP for local '
         'orthogonal L)')
setp('SEP', 'g_cnot', 'BD', True, 'X', ('W9',), 'phiW in maxCone = SEP*')
setp('SEP', 'g_cnot', 'SECTef', True, 'W', ('D1', 'D5', 'D6', 'W9'), 'cnot SEP in Q3 in maxCone')
setp('SEP', 'g_cnot', 'TBP', True, 'W', ('D1', 'D5', 'D6'), 'cnot^{+-1} SEP in Q3 in maxCone')
# --- (SEP, g_D): one twisted pair on SEP
setp('SEP', 'g_D', 'BD', True, 'X', ('W9', 'W13'), 'bellOf(I, reflY) = idW in maxCone = SEP*')
setp('SEP', 'g_D', 'SECTef', True, 'W', ('P1', 'Dsep', 'D1', 'D5', 'D6'), 'g_D^-1 SEP = cnot SEP in Q3 in maxCone')
setp('SEP', 'g_D', 'TBP', True, 'W', ('P1', 'Dsep', 'Dpt', 'Dmax', 'DL', 'D1', 'D5', 'D6'),
     'g_D SEP in twin in maxCone; g_D^-1 SEP in Q3')
for cl in ('hgate', 'SECTst', 'SECT', 'OQ1', 'CONS', 'BS'):
    setp('SEP', 'g_D', cl, False, 'X', ('W12', 'W8', 'W13'), 'g_D pxz = idW not in SEP')
# --- (Q3, g_pre): M_pre's pair
setp('Q3', 'g_pre', 'hgate', False, 'X', ('W1', 'W12', 'W4'), 'phiW in Q3, g_pre phiW = chainW not in maxCone')
setp('Q3', 'g_pre', 'PREC', True, 'W', ('W14', 'D1'), 'g_pre . actT reflY = cnot preserves Q3')
setp('Q3', 'g_pre', 'SECTst', True, 'W', ('P2', 'Dsep', 'D1', 'D5', 'D6'), 'g_pre(products) = cnot(products) in Q3')
setp('Q3', 'g_pre', 'SECTef', True, 'W', ('P2', 'D1', 'Dpt', 'Dmax', 'DL'), 'g_pre^-1 Q3 = actT reflY cnot Q3 = twin')
setp('Q3', 'g_pre', 'SECT', True, 'W', ('P2', 'D1', 'D5', 'D6', 'Dpt', 'Dmax', 'DL'), 'both halves')
for cl in ('OQ1', 'CONS', 'BS', 'BD'):
    setp('Q3', 'g_pre', cl, True, 'W', ('W1', 'L1', 'D1', 'D5', 'D6', 'P2'),
         'post-locals (I, I): the same tables as M_Q')
setp('Q3', 'g_pre', 'PRP', False, 'X', ('W12', 'W2'), 'g_pre^-1 pxz = idW not in Q3')
setp('Q3', 'g_pre', 'TBP', False, 'X', ('W1', 'W12', 'W4'), 'g_pre phiW = chainW')
setp('Q3', 'g_pre', "SECT'", False, 'X', ('W12', 'W2'), 'g_pre^-1 pxz = idW not in Q3')
# --- (twin, g_D): M_DD's twisted pairs
setp('twin', 'g_D', 'hgate', False, 'X', ('W12', 'W4', 'W2t'), 'idW in twin, g_D idW = chainW')
setp('twin', 'g_D', 'PREC', True, 'W', ('W14', 'G.g_Tw', 'D1', 'Dpt'),
     'g_D . actT reflY = g_Tw = actT reflY cnot actT reflY preserves twin = actT reflY Q3')
for cl in ('SECT', 'SECTst', 'SECTef'):
    setp('twin', 'g_D', cl, True, 'W', ('P1', 'Dsep', 'D1', 'D5', 'D6', 'Dpt', 'Dadj'),
         'g_D SEP = actT reflY cnot SEP in twin = twin*; g_D^-1 twin = cnot Q3 = Q3 in maxCone')
for cl in ('OQ1', 'CONS', 'BS', 'BD'):
    setp('twin', 'g_D', cl, True, 'W', ('L2', 'W2t', 'Dadj', 'Dpt', 'D1', 'D5', 'D6'),
         'link tables actT reflY (Q3 link tables) in twin; bellOf = idW in twin = twin*')
# --- (twin, g_cnot): TWIN, and M_DD's untwisted? (M_DD has Q3 at 01, 02 with g_cnot)
setp('twin', 'g_cnot', 'hgate', False, 'X', ('W14', 'W11', 'W3'), 'pxz in twin, cnot pxz = phiW not in twin')
setp('twin', 'g_cnot', 'PREC', False, 'W', ('W11', 'W3', 'W12', 'W4', 'Dpt', 'Dtr', 'landed:D7'),
     'cnot L twin: L twin in {Q3, twin}; cnot Q3 = Q3 not in twin (phiW), cnot twin contains chainW')
for cl in ('CONS', 'OQ1', 'SECT', 'SECTst', 'BS'):
    setp('twin', 'g_cnot', cl, False, 'X', ('W14', 'W3', 'W11'), 'phiW = cnot pxz not in twin')
# --- (Kint, g_cnot): M_int
for cl in ('BD', 'CONS', 'OQ1', 'SECT'):
    setp('Kint', 'g_cnot', cl, False, 'X', ('W10',), 'phiW not in dualW Kint = dualW maxCone')
setp('Kint', 'g_cnot', 'hgate', False, 'K', ('landed:M_int.2',), 'landed')

CLAUSES = ('hgate', 'PREC', 'SECT', 'SECTst', 'SECTef', 'OQ1', 'CONS', 'BS', 'BD', 'PRP', 'TBP', "SECT'")


def family_value(model, clause):
    cones, gates, _ = MODELS[model]
    vals = []
    for k, g in zip(cones, gates):
        key = (k, g, clause)
        if key not in PAIR:
            return None
        vals.append(PAIR[key])
    ok_ids = all(i in CHECKS and CHECKS[i][1] for v in vals for i in v[2] if not i.startswith('landed:'))
    if not ok_ids:
        return ('INVALID', None)
    value = all(v[0] for v in vals)
    bases = sorted(set(v[1] for v in vals if v[0] == value))
    return (value, ''.join(bases))


def model_C(model):
    cones, gates, _ = MODELS[model]
    return all(IE1_OF[k] for k in cones) and evencycle(gates)


# H0 holds in every model listed (written; bases in H0_BASIS); hcls is G.* for each gate used
H0 = {m: all(CHECKS[f'G.{g}'][1] for g in MODELS[m][1]) and all(CHECKS[i][1] for i in ('D1', 'D5', 'D6', 'F.sep', 'F.t3',
                                                                                       'F.t12', 'Dtr', 'Dpt', 'Dadj'))
      for m in MODELS}
H0['M_int'] = False   # hcl fails: idW lies in cl Kint = maxCone and not in Kint (landed M_int.1, replayed)

hdr = 'model    H0  C   ' + ' '.join(f'{c:>7}' for c in CLAUSES)
print(hdr)
TABLE = {}
for m in MODELS:
    row = []
    for c in CLAUSES:
        fv = family_value(m, c)
        TABLE[(m, c)] = fv
        if fv is None:
            row.append('      -')
        elif fv[0] == 'INVALID':
            row.append('INVALID')
        else:
            row.append(f"{('Y' if fv[0] else 'n') + '/' + fv[1]:>7}")
    print(f"{m:<8} {'Y' if H0[m] else 'n':>2}  {'Y' if model_C(m) else 'n':<2}  " + ' '.join(row))
print('legend: Y holds, n fails; basis X exact witness/identity, W written reduction over listed exact checks, K landed '
      'fact; - not evaluated.  H0 bases: ' + '; '.join(f'{k}: {v}' for k, v in H0_BASIS.items()))
for (k, g, c), (v, b, ids, note) in sorted(PAIR.items()):
    print(f'  cell ({k}, {g}) {c}: {"holds" if v else "fails"} [{b}: {", ".join(ids)}] {note}')

# ===============================================================================================================
print()
failed = [c for c in ORDER if not CHECKS[c][1]]
invalid = [k for k, v in TABLE.items() if v is not None and v[0] == 'INVALID']
kinds = ('identity', 'witness', 'enumerate', 'sample', 'source', 'countercontrol')
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in ORDER if CHECKS[c][0] == k)}" for k in kinds), flush=True)
if failed or invalid:
    print(f"b1_models: NO VERDICT -- failed checks: {', '.join(failed)}; invalid cells: {invalid}")
    sys.exit(1)


def val(m, c):
    fv = TABLE[(m, c)]
    return None if fv is None else fv[0]


SUFFICIENT_BY_DERIVATION = ('hgate', 'PREC', 'SECT', 'OQ1', 'CONS')   # written derivations (RESULT section 1)
BLIND = ('M_max', 'M_SEP', 'M_maxD', 'M_maxT', 'M_SEPD')               # every cone actT reflY-invariant
incons = [(m, c) for c in SUFFICIENT_BY_DERIVATION for m in BLIND if val(m, c) is True]
if incons:
    print(f'b1_models: INCONSISTENCY -- a clause derived sufficient holds on an orientation-blind family: {incons}')
    print('b1_models: NO VERDICT')
    sys.exit(1)
for c in CLAUSES:
    weaker = [m for m in MODELS if H0[m] and val(m, c) is True and val(m, 'hgate') is False]
    insuff = [m for m in MODELS if H0[m] and val(m, c) is True and not model_C(m)]
    bad = [m for m in MODELS if H0[m] and not model_C(m)]
    fails_all_bad = all(val(m, c) is False for m in bad if val(m, c) is not None)
    parts = []
    if c != 'hgate':
        parts.append(f"H0 and {c} and not hgate in: {weaker if weaker else 'none of these models'}")
    none_txt = 'none in this matrix (survives these countermodels; sufficiency is not measured here)'
    cm_txt = str(insuff) if insuff else none_txt
    parts.append(f"countermodel to the theorem with {c} in place of hgate (H0 and {c} and not C): {cm_txt}")
    parts.append(f"fails in every H0-and-not-C model of the matrix: {fails_all_bad}")
    parts.append(f"at M_max: {val('M_max', c)}; at M_D: {val('M_D', c)}")
    print(f'VERDICT B1-{c}: ' + '; '.join(parts))
print('VERDICT B1-NOTE: this script measures countermodels and separations only; sufficiency of hgate, PREC, SECT, OQ1 '
      'and CONS is the step-by-step written derivation of RESULT section 1 (b1_consumed S1-S3 and b1_steps), not a '
      'measurement of this script')
print('VERDICT B1-OBSTRUCTION: every clause derived sufficient (' + ', '.join(SUFFICIENT_BY_DERIVATION)
      + ') fails on each orientation-blind family ' + str(list(BLIND)) + ', as sigma-invariance (O1-O4) and sufficiency '
      'require; EvenCycle splits the 16 patterns on such cones ' + f'{even}/{odd} (O5)')
print(f'b1_models: OK -- {len(ORDER)} checks')
