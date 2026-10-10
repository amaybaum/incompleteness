#!/usr/bin/env python3
"""Round KT4-PREM-1 -- exact checks behind the premise audit of the Pauli-free four-copy theorem.

The audited statement has five hypotheses on four pair cones K_p in the table carrier W 3 = R^{4x4}
(p = 01, 23, 02, 13), gates N_p and one-copy linear maps A_p, B_p, A'_p, B'_p:

  hcls   N_p = actC A_p . actT B_p . cnot . actC A'_p . actT B'_p with the four maps orthogonal (N-CLASS);
  hadm   K_p contains prodState x y for all x, y in eball 3, lies in maxCone (eball 3), and is a convex cone;
  hcl    K_p is closed;
  hgate  N_p maps K_p into K_p;
  H      a KT4Core structure on (K_01, K_23, K_02, K_13) over some real normed carrier V;

and its conclusion C: every K_p is invariant under actC R and actT R for every rotation R (IE1), and the number of
pairs with det A_p * det B_p = -1 is even (EvenCycle).

Exact arithmetic only: sympy Rationals, Gaussian rationals and polynomial identities. No floating point, no
randomness, no time-dependence; every point at which anything is tested is fixed in this file. The script reads
two landed Lean sources, CompositeDimension.lean and K2Guard.lean, read-only, to check its transcription of the
landed tables on which its computations rest. It runs every check and prints one PASS or FAIL line for each. It ends
with 'kt4_prem1_probe: OK -- N checks' when all pass; otherwise it ends with 'kt4_prem1_probe: FAILED -- ...', naming
the failed checks, and exits 1. These statements are exact arithmetic replayed in CI; they are not kernel-certified.

Each check carries its kind:
  [identity]        an exact symbolic identity (decisive for the universal claim it encodes);
  [witness]         an exact witness for an existential or negative claim (decisive for that claim);
  [enumerate]       an exhaustive exact enumeration of a finite set (decisive);
  [source]          a transcription or citation check against the landed Lean sources;
  [sample]          an exact check at fixed points (evidence only for the universal claim it instantiates);
  [countercontrol]  a mutated object or construction that must give the opposite verdict.
Lines printed as NOTE [written] record a written step beside the exact checks; they are not checks and are not
counted. A written step that rests on a standard result names it.

Conventions (transcribed from CompositeDimension.lean and K2Guard.lean, and checked in section S0):
  tables W 3: index 0 is the unit, 1..3 the coordinates; hom x = (1, x); prodState x y = hom x hom y^T;
  homMap R = diag(1, R); actC R w = homMap R . w (first token); actT R w = w . homMap R^T (second token);
  cnot w (m, n) = sgn(m, n) w(pc(m, n), pt(m, n)); pairVal a b w = a^T w b; ipW E X = sum E_mn X_mn;
  maxCone (eball 3) = {w : a^T w b >= 0 for all a, b in L}, L = {a : a_0 >= |(a_1, a_2, a_3)|};
  pauliW w = (1/4) sum w_mn s_m (x) s_n with s = (I, X, Y, Z); Q3 = {w : pauliW w is positive semidefinite};
  twin = actT reflY Q3, reflY = diag(1, -1, 1).

Sections.
  S0  transcription of the landed tables.
  S1  the quantum dictionary: cnot is conjugation by CNOT, local rotations are conjugations by SU(2), the pairings.
  S2  an explicit four-copy carrier on which FCC gives KT4Core: evaluation laws, token coherence, cross values.
  S3  FCC for uniform Q3 and for uniform maxCone, and a countercontrol in which FCC fails (-1/8).
  S4  model M_cl (the closedness foil): hcls, hadm, hgate, H hold; hcl and IE1 fail.
  S5  model M_max (uniform maxCone): hcls, hadm, hcl, H and C hold; hgate fails.
  S6  models M_Q, M_D, M_refl, M_id, M_class, M_mix, M_int.
  S7  the token clauses: an anchor carrier, models M_tok and M_tokC.
  S8  the finite steps of the classification argument (hcls, hadm, hgate, IE1 give Q3 or the twin).
  S9  the composite interface: a non-closed composite body, and the landed composite bodies cnot does not preserve.
  S10 countercontrols.
"""
import re
import sys
from itertools import product
from pathlib import Path

import sympy as sp

Q = sp.Rational
iu = sp.I
R4 = range(4)

CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def note(cid, text):
    print(f"NOTE [written] {cid}  -- {text}", flush=True)


def section(title):
    print()
    print(f"== {title}", flush=True)


def ex(v):
    return sp.expand(v)


def zero(v):
    return ex(v) == 0


def mzero(M):
    return all(ex(v) == 0 for v in M)


# ---------------------------------------------------------------------------------------------------------------
# The landed tables (transcribed; checked against the Lean sources in S0).

PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def sgn(m, n):
    return -1 if (m, n) in NEG else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
reflY = sp.diag(1, -1, 1)
I3 = sp.eye(3)
xplus = [1, 0, 0]
z3 = [0, 0, 1]
O3 = [0, 0, 0]
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = R
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def prodState(x, y):
    return hom(x) * hom(y).T


def pairVal(a, b, w):
    return (sp.Matrix(a).T * w * sp.Matrix(b))[0, 0]


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


def fourVal(X, Y, E, F):
    return sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d] for a, b, c, d in product(R4, repeat=4))


def famII_val(e, f, L, Lp):
    return sum(e[a, b] * f[c, d] * L[a, c] * Lp[b, d] for a, b, c, d in product(R4, repeat=4))


def refl_pow(k):
    return reflY if k % 2 else I3


def det_orient(A, B):
    return sp.Matrix(A).det() * sp.Matrix(B).det() == -1


E00 = prodState(O3, O3)
SHARP_NEGX = [Q(1, 2), Q(-1, 2), 0, 0]      # sharpVec ![-1, 0, 0]
SHARP_NEGZ = [Q(1, 2), 0, 0, Q(-1, 2)]      # sharpVec ![0, 0, -1]

# ---------------------------------------------------------------------------------------------------------------
# Pauli matrices and the quantum dictionary.

S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def kron(*Ms):
    out = Ms[0]
    for M in Ms[1:]:
        out = sp.kronecker_product(out, M)
    return out


SS = [[kron(S[m], S[n]) for n in R4] for m in R4]


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * SS[m][n]
    return out / 4


def opW(E):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if E[m, n] != 0:
                out += E[m, n] * SS[m][n]
    return out


def opV(a):
    return sum((a[m] * S[m] for m in R4), sp.zeros(2, 2))


def dag(M):
    return M.conjugate().T


def trace_prod(A, B):
    n = A.shape[0]
    return sum(A[i, j] * B[j, i] for i in range(n) for j in range(n))


CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


def rho1(x):
    return (S[0] + sum((x[i] * S[i + 1] for i in range(3)), sp.zeros(2, 2))) / 2


def symtab(name):
    return sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'{name}{m}{n}', real=True))


def symvec(name, k):
    return [sp.Symbol(f'{name}{i}', real=True) for i in range(k)]


def is_psd_projector(P):
    return mzero(P - dag(P)) and mzero(P * P - P)


# ===============================================================================================================
section('S0  transcription of the landed tables')

LEAN = Path(__file__).resolve().parents[1] / 'lean-mathlib' / 'OIBridge'


def lean_src(name):
    return (LEAN / name).read_text(encoding='utf-8')


CD = lean_src('CompositeDimension.lean')
KG = lean_src('K2Guard.lean')

msg = re.search(r'^def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) '
                r'then -1 else 1$', CD, re.M)
neg_src = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))} if msg else None
chk('S0.sgn', 'sgn: the landed sign is -1 exactly at (1, 3) and (2, 2)', neg_src == NEG, 'source')


def lean_table(nm):
    mm = re.search(rf'^def {nm} : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){{4}})', CD, re.M)
    if not mm:
        return None
    T = [[None] * 4 for _ in R4]
    for a, b, v in re.findall(r'\|\s*(\d),\s*(\d)\s*=>\s*(\d)', mm.group(1)):
        T[int(a)][int(b)] = int(v)
    return T


chk('S0.pc', 'pc: the landed control-index table', lean_table('pc') == PC, 'source')
chk('S0.pt', 'pt: the landed target-index table', lean_table('pt') == PT, 'source')
chk('S0.phiW', 'phiW: the landed definition is diag(1, 1, -1, 1)',
    'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD, 'source')


def lean_matrix(nm):
    mm = re.search(rf'^def {nm} : W 3 := !\[(.*)\]$', KG, re.M)
    if not mm:
        return None
    rows = re.findall(r'!\[([^\]]*)\]', mm.group(1))
    return sp.Matrix([[int(v) for v in r.split(',')] for r in rows])


chk('S0.idW', 'idW: the landed table is the identity', lean_matrix('idW') == idW, 'source')
chk('S0.chainW', 'chainW: the landed table', lean_matrix('chainW') == chainW, 'source')
chk('S0.reflY', 'reflY: the landed map is diag(1, -1, 1)',
    'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i' in KG, 'source')

# ===============================================================================================================
section('S1  the quantum dictionary')

Wsym = symtab('w')
chk('D1', 'pauliW (cnot w) = CNOT pauliW(w) CNOT^dagger for a symbolic table w (cnot is conjugation by CNOT)',
    mzero(pauliW(cnot(Wsym)) - CNOT * pauliW(Wsym) * dag(CNOT)), 'identity')
chk('D2', 'cnot . cnot = id on a symbolic table', mzero(cnot(cnot(Wsym)) - Wsym), 'identity')

Esym = symtab('E')
chk('D3', 'ipW E X = tr(opW(E) pauliW(X)) for symbolic E, X (the Euclidean pairing is the trace pairing)',
    zero(ipW(Esym, Wsym) - trace_prod(opW(Esym), pauliW(Wsym))), 'identity')

asym = symvec('a', 4)
bsym = symvec('b', 4)
chk('D4', 'pairVal a b w = tr((opV a (x) opV b) pauliW(w)) for symbolic a, b, w',
    zero(pairVal(asym, bsym, Wsym) - trace_prod(kron(opV(asym), opV(bsym)), pauliW(Wsym))), 'identity')

xs = symvec('x', 3)
ys = symvec('y', 3)
chk('D5', 'pauliW (prodState x y) = rho(x) (x) rho(y), rho(x) = (I + x.s)/2, for symbolic x, y',
    mzero(pauliW(prodState(xs, ys)) - kron(rho1(xs), rho1(ys))), 'identity')
A2 = opV(asym)
chk('D6', 'opV a is Hermitian with trace 2 a0 and determinant a0^2 - |a|^2 (opV a >= 0 iff a in L)',
    mzero(A2 - dag(A2)) and zero(A2.trace() - 2 * asym[0])
    and zero(A2.det() - (asym[0] ** 2 - asym[1] ** 2 - asym[2] ** 2 - asym[3] ** 2)), 'identity')

qw, qx, qy, qz = sp.symbols('qw qx qy qz', real=True)
Ut = qw * S[0] - iu * (qx * S[1] + qy * S[2] + qz * S[3])
nq = qw ** 2 + qx ** 2 + qy ** 2 + qz ** 2
Mq = sp.Matrix(3, 3, lambda i, k: ex((S[i + 1] * Ut * S[k + 1] * dag(Ut)).trace() / 2))
ok_q = mzero(Ut * dag(Ut) - nq * S[0]) and mzero(Mq - Mq.conjugate())
ok_q = ok_q and all(mzero(Ut * S[k + 1] * dag(Ut) - sum((Mq[i, k] * S[i + 1] for i in range(3)), sp.zeros(2, 2)))
                    for k in range(3))
ok_q = ok_q and mzero(Mq.T * Mq - nq ** 2 * I3) and zero(Mq.det() - nq ** 3)
Hn = sp.diag(nq, 1, 1, 1)
Hn[1:4, 1:4] = Mq
rhoW = pauliW(Wsym)
ok_q = ok_q and mzero(pauliW(Hn * Wsym) - kron(Ut, S[0]) * rhoW * dag(kron(Ut, S[0])))
ok_q = ok_q and mzero(pauliW(Wsym * Hn.T) - kron(S[0], Ut) * rhoW * dag(kron(S[0], Ut)))
chk('D7', 'for a symbolic quaternion q, U = q0 I - i q.s gives U s_k U^dagger = sum_i M_ik s_i with M^T M = |q|^4 I, '
    'det M = |q|^6, and pauliW(diag(|q|^2, M) w) = (U (x) I) pauliW(w) (U (x) I)^dagger (and on the second token)',
    ok_q, 'identity')
note('D7.W', 'at |q| = 1, M is a rotation and actC M = Ad(U (x) I), actT M = Ad(I (x) U); every U in SU(2) is of '
     'this form, and every rotation is M for some unit quaternion (the standard double cover SU(2) -> SO(3)). So '
     'actC R and actT R for rotations R are exactly the conjugations by local unitaries, and Q3, int Q3 are '
     'invariant under them.')
note('D.W', 'by D3 and the self-duality of the positive semidefinite cone under the trace pairing, '
     'dualW Q3 = {E : opW E >= 0}; by D4 and D6, Q3 lies in maxCone (opV a (x) opV b >= 0 for a, b in L); by D5 and '
     'D6, every prodState x y with x, y in eball 3 lies in Q3; by D1, cnot maps Q3 onto Q3 and int Q3 onto int Q3.')

# ===============================================================================================================
section('S2  an explicit carrier for KT4Core')

note('S2.def', 'V = R^{17x17} x R^{17x17}. For x in R^16 let xh = (1, x) and X the table X_ab = x_{4a+b}; for an '
     'affine e(x) = e0 + E.x let eh = (e0, E) and Et the table Et_ab = E_{4a+b} + e0 [a = b = 0]. '
     'stA x y = (xh yh^T, 0), stB x y = (0, xh yh^T); '
     'effA e f (P, Q) = eh^T P fh + sum_abcd Et_ab Ft_cd Q[1 + (4a+c), 1 + (4b+d)]; '
     'effB e f (P, Q) = eh^T Q fh + sum_abcd Et_ac Ft_bd P[1 + (4a+b), 1 + (4c+d)]. '
     'Both are linear in (P, Q) and bilinear in (e, f). The index map (a, b) -> 4a + b stands for the bijection '
     'flatW and tabCoord use; the identities below hold for any fixed bijection used consistently.')


def idx(a, b):
    return 4 * a + b


def hat17(v):
    return sp.Matrix([1] + list(v))


def tab_of(v):
    return sp.Matrix(4, 4, lambda a, b: v[idx(a, b)])


def eh17(e):
    return sp.Matrix([e[0]] + list(e[1]))


def Etil(e):
    T = tab_of(e[1])
    T[0, 0] += e[0]
    return T


def aff(e, v):
    return e[0] + sum(e[1][i] * v[i] for i in range(16))


def stA(x, y):
    return (hat17(x) * hat17(y).T, sp.zeros(17, 17))


def stB(x, y):
    return (sp.zeros(17, 17), hat17(x) * hat17(y).T)


def effA(e, f, V):
    P, Qm = V
    Et, Ft = Etil(e), Etil(f)
    return (eh17(e).T * P * eh17(f))[0, 0] + sum(
        Et[a, b] * Ft[c, d] * Qm[1 + idx(a, c), 1 + idx(b, d)] for a, b, c, d in product(R4, repeat=4))


def effB(e, f, V):
    P, Qm = V
    Et, Ft = Etil(e), Etil(f)
    return (eh17(e).T * Qm * eh17(f))[0, 0] + sum(
        Et[a, c] * Ft[b, d] * P[1 + idx(a, b), 1 + idx(c, d)] for a, b, c, d in product(R4, repeat=4))


def coord(a, b):
    return (0, [1 if i == idx(a, b) else 0 for i in range(16)])


def symaff(name):
    return (sp.Symbol(f'{name}c', real=True), symvec(name, 16))


eS, fS, gS = symaff('e'), symaff('f'), symaff('g')
xS, yS = symvec('x', 16), symvec('y', 16)
XS, YS = tab_of(xS), tab_of(yS)

chk('H1', 'effA e f (stA x y) = e(x) f(y) for symbolic affine e, f and symbolic x, y in R^16',
    zero(effA(eS, fS, stA(xS, yS)) - aff(eS, xS) * aff(fS, yS)), 'identity')
chk('H2', 'effB e f (stB x y) = e(x) f(y) for symbolic affine e, f and symbolic x, y in R^16',
    zero(effB(eS, fS, stB(xS, yS)) - aff(eS, xS) * aff(fS, yS)), 'identity')

Psym = sp.Matrix(17, 17, lambda i, j: sp.Symbol(f'P{i}_{j}', real=True))
Qsym = sp.Matrix(17, 17, lambda i, j: sp.Symbol(f'Q{i}_{j}', real=True))
al, be = sp.symbols('al be', real=True)


def lin(e, g):
    return (al * e[0] + be * g[0], [al * e[1][i] + be * g[1][i] for i in range(16)])


Vsym = (Psym, Qsym)
ok_bil = zero(effA(lin(eS, gS), fS, Vsym) - al * effA(eS, fS, Vsym) - be * effA(gS, fS, Vsym))
ok_bil = ok_bil and zero(effA(fS, lin(eS, gS), Vsym) - al * effA(fS, eS, Vsym) - be * effA(fS, gS, Vsym))
ok_bil = ok_bil and zero(effB(lin(eS, gS), fS, Vsym) - al * effB(eS, fS, Vsym) - be * effB(gS, fS, Vsym))
ok_bil = ok_bil and zero(effB(fS, lin(eS, gS), Vsym) - al * effB(fS, eS, Vsym) - be * effB(fS, gS, Vsym))
chk('H3', 'effA and effB are linear in each effect argument, on a symbolic element of V', ok_bil, 'identity')

stAxy, stBxy = stA(xS, yS), stB(xS, yS)
tokA_bad = [(a, b, c, d) for a, b, c, d in product(R4, repeat=4)
            if not zero(effA(coord(a, b), coord(c, d), stAxy) - effB(coord(a, c), coord(b, d), stAxy))]
chk('H4', 'tokA: effA (tabCoord a b) (tabCoord c d) (stA x y) = effB (tabCoord a c) (tabCoord b d) (stA x y), '
    'all 256 index quadruples, symbolic x, y', not tokA_bad, 'identity', f'{256 - len(tokA_bad)}/256')
tokB_bad = [(a, b, c, d) for a, b, c, d in product(R4, repeat=4)
            if not zero(effA(coord(a, b), coord(c, d), stBxy) - effB(coord(a, c), coord(b, d), stBxy))]
chk('H5', 'tokB: the same with stB x y, all 256 index quadruples, symbolic x, y', not tokB_bad, 'identity',
    f'{256 - len(tokB_bad)}/256')

EtS, FtS = Etil(eS), Etil(fS)
chk('H6', 'effB e f (stA x y) = fourVal X Y Et Ft (the cross value of grouping 02|13 effects on 01|23 states)',
    zero(effB(eS, fS, stAxy) - fourVal(XS, YS, EtS, FtS)), 'identity')
chk('H7', 'effA e f (stB x y) = sum Et_ab Ft_cd X_ac Y_bd (the cross value of 01|23 effects on 02|13 states)',
    zero(effA(eS, fS, stBxy) - famII_val(EtS, FtS, XS, YS)), 'identity')

Xg, Yg, Eg, Fg = symtab('X'), symtab('Y'), symtab('E'), symtab('F')
chk('H8', 'fourVal X Y E F = ipW X (tabMul (tabMul E Y) (tabT F)) = ipW E (X F Y^T) for symbolic tables '
    '(famI is the positivity of this value)',
    zero(fourVal(Xg, Yg, Eg, Fg) - ipW(Xg, (Eg * Yg) * Fg.T)) and zero(fourVal(Xg, Yg, Eg, Fg) - ipW(Eg, Xg * Fg * Yg.T)),
    'identity')
chk('H9', 'sum e_ab f_cd L_ac L\'_bd = ipW e (tabMul (tabMul L f) (tabT L\')) for symbolic tables (the famII form)',
    zero(famII_val(Eg, Fg, Xg, Yg) - ipW(Eg, (Xg * Fg) * Yg.T)), 'identity')
xn = list(xS)
xn[idx(0, 0)] = 1
chk('H10', 'e(flat X) = ipW Et X when X_00 = 1, symbolic e and X (an effect on a pair body is its table on the slice)',
    zero(aff(eS, xn) - ipW(EtS, tab_of(xn))), 'identity')
note('H.W', 'let K02, K13 lie in maxCone and be closed under nonnegative scaling. If e is an effect on pairBody K02 '
     'then Et lies in dualW K02: a nonzero w in K02 has w_00 > 0 (in maxCone, w_00 >= 0, and w_00 = 0 forces w = 0, '
     'from a^T w b at a = (1, u), b = (1, v)), and ipW Et w = w_00 e(flat(w / w_00)) >= 0 by H10. Then posBA is famI '
     'at (X, Y, Et, Ft) by H6 and H8, and posAB is famII by H7 and H9. Together with H1, H2, H4, H5 and H3: '
     'FCC, the maxCone bound and nonnegative scaling of the four cones give KT4Core on this V. Conversely Lemma B1 '
     '(fourCopyCoherent_of_kt4Core, kernel-checked in the design module FourCopyBridge) gives FCC from KT4Core and '
     'the same two clauses. Under hadm the hypothesis H is therefore equivalent to FCC, by separately named '
     'arguments in each direction.')

# ===============================================================================================================
section('S3  FCC for uniform Q3 and for uniform maxCone')

# the qubit order (0, 2, 1, 3) -> (0, 1, 2, 3): basis |i0 i2 i1 i3> -> |i0 i1 i2 i3>
Pi = sp.zeros(16, 16)
for i0, i1, i2, i3 in product(range(2), repeat=4):
    old = i0 * 8 + i2 * 4 + i1 * 2 + i3
    new = i0 * 8 + i1 * 4 + i2 * 2 + i3
    Pi[new, old] = 1
chk('F0', 'Pi is a permutation matrix (Pi Pi^T = I)', Pi * Pi.T == sp.eye(16), 'identity')
chk('F1', 'tr(s_m s_n) = 2 delta_mn for the four Pauli matrices',
    all(zero((S[m] * S[n]).trace() - (2 if m == n else 0)) for m in R4 for n in R4), 'enumerate', '16 pairs')
op4 = Pi * kron(opW(Eg), opW(Fg)) * Pi.T
rho4 = kron(pauliW(Xg), pauliW(Yg))
chk('F2', 'fourVal X Y E F = tr( Pi (opW E (x) opW F) Pi^T (pauliW X (x) pauliW Y) ), symbolic X, Y, E, F '
    '(E on tokens 0, 2; F on 1, 3; X on 0, 1; Y on 2, 3)',
    zero(fourVal(Xg, Yg, Eg, Fg) - trace_prod(op4, rho4)), 'identity')
op4b = kron(opW(Eg), opW(Fg))
rho4b = Pi * kron(pauliW(Xg), pauliW(Yg)) * Pi.T
chk('F3', 'sum e_ab f_cd L_ac L\'_bd = tr( (opW e (x) opW f) Pi (pauliW L (x) pauliW L\') Pi^T ), symbolic '
    '(the famII form, L on tokens 0, 2 and L\' on 1, 3)',
    zero(famII_val(Eg, Fg, Xg, Yg) - trace_prod(op4b, rho4b)), 'identity')
sing4 = sp.diag(1, -1, -1, -1)
Tpsi0 = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
statesQ = [phiW, Tpsi0, sing4, E00]
effectsQ = [phiW / 4, sing4 / 4, E00, Tpsi0 / 4]


def psd_exact(M):
    return mzero(M - dag(M)) and all(ev >= 0 for ev in M.eigenvals())


chk('F2v', 'sample inputs: pauliW of each of phiW, T_psi, diag(1,-1,-1,-1), E00 and opW of each of phiW/4, '
    'diag(1,-1,-1,-1)/4, E00, T_psi/4 are positive semidefinite (exact eigenvalues)',
    all(psd_exact(pauliW(w)) for w in statesQ) and all(psd_exact(opW(E)) for E in effectsQ), 'sample')
vals = [fourVal(X_, Y_, E_, F_) for X_ in statesQ for Y_ in statesQ for E_ in effectsQ for F_ in effectsQ]
chk('F2s', 'sample: fourVal X Y E F >= 0 at the 256 quadruples of these entangled and product states of Q3 and '
    'entangled and product effects of dualW Q3', min(vals) >= 0, 'sample', f'minimum {min(vals)}')
note('F.Q3', 'FCC for uniform Q3: for X, Y in Q3 and E, F in dualW Q3, opW E, opW F, pauliW X, pauliW Y are '
     'positive semidefinite (S1); the Kronecker product of positive semidefinite matrices is positive semidefinite '
     '(Mathlib Matrix.PosSemidef.kronecker), conjugation by the permutation Pi preserves this, and the trace of a '
     'product of two positive semidefinite matrices is nonnegative. By F2 famI holds, by F3 famII holds.')

av, bv, uv, vv = symvec('a', 4), symvec('b', 4), symvec('u', 4), symvec('v', 4)
chk('F4', 'pairVal a b (X F Y^T) = ipW F ((X^T a)(Y^T b)^T), symbolic', zero(
    pairVal(av, bv, Xg * Fg * Yg.T) - ipW(Fg, (Xg.T * sp.Matrix(av)) * (Yg.T * sp.Matrix(bv)).T)), 'identity')
chk('F5', 'pairVal a b (u v^T) = (a.u)(b.v), symbolic', zero(
    pairVal(av, bv, sp.Matrix(uv) * sp.Matrix(vv).T)
    - sum(av[i] * uv[i] for i in R4) * sum(bv[i] * vv[i] for i in R4)), 'identity')
chk('F6', 'Lagrange: |a|^2 |u|^2 - (a.u)^2 = sum_{i<j} (a_i u_j - a_j u_i)^2 in R^3 (Cauchy-Schwarz)', zero(
    (av[1] ** 2 + av[2] ** 2 + av[3] ** 2) * (uv[1] ** 2 + uv[2] ** 2 + uv[3] ** 2)
    - (av[1] * uv[1] + av[2] * uv[2] + av[3] * uv[3]) ** 2
    - sum((av[i] * uv[j] - av[j] * uv[i]) ** 2 for i in range(1, 4) for j in range(i + 1, 4))), 'identity')
note('F.max', 'FCC for uniform maxCone: the homogeneous coefficient vector of an effect on eball 3 lies in L, and '
     'every vector of L is a positive multiple of one, so maxCone = {w : a^T w b >= 0 for a, b in L}. L is '
     'self-dual for the Euclidean pairing (F6). For X, Y in maxCone and a, b in L: u = X^T a and v = Y^T b lie in '
     'L, so u v^T lies in maxCone (F5) and a^T (X F Y^T) b = ipW F (u v^T) >= 0 for F in dualW maxCone (F4). So '
     'X F Y^T lies in maxCone, and fourVal X Y E F = ipW E (X F Y^T) >= 0 for E in dualW maxCone (H8): famI. famII '
     'is the same argument for (L, F, L\') (H9).')

# countercontrol: (Q3, Q3, Q3, twin) violates famI
Ecc = phiW / 4
Fcc = sp.diag(1, -1, 1, -1) / 4
chk('F7', 'opW(phiW/4) is a rank-one projector, so phiW/4 lies in dualW Q3', is_psd_projector(opW(Ecc))
    and opW(Ecc).rank() == 1, 'witness')
chk('F8', 'ipW F (actT reflY w) = ipW (actT reflY F) w (symbolic), and opW(actT reflY F) is a rank-one projector '
    'for F = diag(1, -1, 1, -1)/4, so F lies in dualW twin',
    zero(ipW(Fg, actT(reflY, Wsym)) - ipW(actT(reflY, Fg), Wsym))
    and is_psd_projector(opW(actT(reflY, Fcc))) and opW(actT(reflY, Fcc)).rank() == 1, 'witness')
chk('F9', 'pauliW phiW is a rank-one projector (phiW in Q3)', is_psd_projector(pauliW(phiW))
    and pauliW(phiW).rank() == 1, 'witness')
v_cc = fourVal(phiW, phiW, Ecc, Fcc)
chk('F10', 'famI fails for the cones (Q3, Q3, Q3, twin): fourVal phiW phiW (phiW/4) F = -1/8', v_cc == Q(-1, 8),
    'countercontrol', f'value {v_cc}')

# ===============================================================================================================
section('S4  model M_cl: K_p = int Q3 u cone(SEP u cnot SEP), N_p = cnot, every local the identity')

note('M_cl.def', 'SEP is the convex cone generated by the product states prodState x y (x, y in eball 3); '
     'K_cl = int Q3 u (SEP + cnot SEP), the same cone at all four pairs.')
ok_hcls = mzero(actC(I3, Wsym) - Wsym) and mzero(actT(I3, Wsym) - Wsym)
ok_hcls = ok_hcls and mzero(cnot(Wsym) - actC(I3, actT(I3, cnot(actC(I3, actT(I3, Wsym)))))) and I3.T * I3 == I3
chk('M_cl.1', 'hcls: actC I = actT I = id, so cnot = actC I . actT I . cnot . actC I . actT I, I orthogonal',
    ok_hcls, 'identity')
note('M_cl.2', 'hadm: every product state lies in SEP; K_cl lies in Q3 (int Q3 does; SEP does by D5, D6; cnot SEP '
     'does by D1) and Q3 lies in maxCone (S1). K_cl is a convex cone: SEP + cnot SEP is one; a positive definite '
     'plus a positive semidefinite matrix is positive definite, so int Q3 + Q3 lies in int Q3; positive scaling '
     'preserves each part and 0 lies in SEP.')
note('M_cl.3', 'hgate: cnot is conjugation by a unitary (D1), so it maps int Q3 onto int Q3; it is an involution '
     '(D2), so it maps SEP + cnot SEP onto cnot SEP + SEP. Since cnot is an involution the inverse gate also '
     'preserves K_cl: two-sided gate invariance holds.')
note('M_cl.4', 'H: Q3 is a closed convex cone whose interior contains E00 (pauliW E00 = I/4), so Q3 = cl int Q3 and '
     'cl K_cl = Q3. A dual cone is unchanged by closure, so dualW K_cl = dualW Q3, and FCC for K_cl follows from '
     'FCC for Q3 (S3) because K_cl lies in Q3. With M_cl.2, S2 gives KT4Core on the carrier V of S2.')
Tpsi = actT(RH, phiW)
chk('M_cl.5', 'R_H = [[0,0,1],[0,-1,0],[1,0,0]] is a rotation', RH.T * RH == I3 and RH.det() == 1, 'witness')
chk('M_cl.6', 'T_psi = actT R_H phiW = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]',
    Tpsi == sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]), 'witness')
psi = sp.Matrix([1, 1, 1, -1]) / 2
chk('M_cl.7', 'pauliW T_psi = psi psi^dagger with psi = (1, 1, 1, -1)/2: a rank-one state, in Q3 and not in int Q3',
    mzero(pauliW(Tpsi) - psi * dag(psi)) and pauliW(Tpsi).det() == 0, 'witness')
tt, lam = sp.symbols('t lam')
cp = pauliW(Tpsi + tt * E00).charpoly(lam).as_expr()
chk('M_cl.8', 'charpoly of pauliW(T_psi + t E00) is (lam - 1 - t/4)(lam - t/4)^3: positive definite for t > 0, so '
    'T_psi lies in the closure of int Q3', zero(cp - (lam - 1 - tt / 4) * (lam - tt / 4) ** 3), 'witness')
chk('M_cl.9', 'T_psi has table rank 4 and cnot T_psi has table rank 4; T_psi_00 = 1 (it is normalized)',
    Tpsi.rank() == 4 and cnot(Tpsi).rank() == 4 and Tpsi[0, 0] == 1,
    'witness', f'ranks {Tpsi.rank()}, {cnot(Tpsi).rank()}')
note('M_cl.9W', 'a pure state is an extreme ray of the positive semidefinite cone: if pauliW T_psi = sum of '
     'positive semidefinite terms, each is a nonnegative multiple of it. The terms of an element of SEP + cnot SEP '
     'are pauliW of product states and their cnot images. So T_psi in SEP + cnot SEP would make T_psi or cnot T_psi '
     'a positive multiple of a product table, of table rank 1 (M_cl.9 excludes both). With M_cl.7, T_psi is not in '
     'K_cl; with M_cl.8 it lies in cl K_cl. hcl fails.')
R0 = sp.Matrix([[Q(3, 5), Q(-4, 5), 0], [Q(4, 5), Q(3, 5), 0], [0, 0, 1]])
cc0 = cnot(actC(R0, phiW))
chk('M_cl.10', 'rank test control: for the rotation R0 about the third axis, cnot (actC R0 phiW) = '
    'prodState (R0 xplus) z3 has table rank 1, so actC R0 phiW lies in cnot SEP',
    R0.T * R0 == I3 and R0.det() == 1 and cc0.rank() == 1 and cc0 == prodState(list(R0 * sp.Matrix(xplus)), z3),
    'countercontrol')
chk('M_cl.11', 'phiW = cnot (prodState xplus z3) lies in cnot SEP, so in K_cl (landed cnot_prodState_xplus_z3)',
    cnot(prodState(xplus, z3)) == phiW, 'witness')
note('M_cl.11W', 'IE1 fails at every pair: phiW lies in K_cl and its image T_psi under actT R_H does not, so '
     'actT R_H maps K_cl onto a set different from K_cl.')
chk('M_cl.12', 'EvenCycle holds: det I * det I = 1, so every orientation bit is false',
    not det_orient(I3, I3), 'identity')
note('M_cl.R', 'M_cl satisfies hcls, hadm, hgate and H, and fails hcl and IE1. It refutes '
     '"hcls, hadm, hgate and H imply C": hcl cannot be dropped from the theorem. Two-sided gate invariance also '
     'holds in M_cl, so closedness is not replaceable by the inverse-gate clause.')

# ===============================================================================================================
section('S5  model M_max: K_p = maxCone (eball 3), N_p = cnot, every local the identity')

note('M_max.1', 'hcls as M_cl.1.')
chk('M_max.2', 'pairVal a b (prodState x y) = (a.hom x)(b.hom y), symbolic (products lie in maxCone; landed '
    'prodState_mem_maxCone)', zero(pairVal(av, bv, prodState(xs, ys))
                                   - (av[0] + sum(av[i + 1] * xs[i] for i in range(3)))
                                   * (bv[0] + sum(bv[i + 1] * ys[i] for i in range(3)))), 'identity')
note('M_max.2W', 'hadm: products lie in maxCone; maxCone is a convex cone, the pairing being bilinear. hcl: maxCone '
     'is an intersection of closed half-spaces.')
chk('M_max.3', 'pairVal a b idW = a0 b0 + a1 b1 + a2 b2 + a3 b3, symbolic (with F6, idW lies in maxCone)',
    zero(pairVal(av, bv, idW) - sum(av[i] * bv[i] for i in R4)), 'identity')
chk('M_max.4', 'cnot idW = chainW (landed cnot_idW), and pairVal at the sharp effects of -e1, -e3 is -1/2 '
    '(landed chain_value): chainW is not in maxCone', cnot(idW) == chainW
    and pairVal(SHARP_NEGX, SHARP_NEGZ, chainW) == Q(-1, 2), 'witness')
note('M_max.4W', 'hgate fails at every pair: idW lies in maxCone and cnot idW does not.')
note('M_max.5', 'H: FCC for maxCone (S3), the maxCone bound and scaling give KT4Core on the carrier of S2.')
Rg = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'R{i}{j}', real=True))
chk('M_max.6', 'pairVal a b (actC R w) = pairVal (homMap R^T a) b w and pairVal a b (actT R w) = '
    'pairVal a (homMap R^T b) w, symbolic R, a, b, w',
    zero(pairVal(av, bv, actC(Rg, Wsym)) - pairVal(list(homMap(Rg.T) * sp.Matrix(av)), bv, Wsym))
    and zero(pairVal(av, bv, actT(Rg, Wsym)) - pairVal(av, list(homMap(Rg.T) * sp.Matrix(bv)), Wsym)), 'identity')
note('M_max.6W', 'IE1: for a rotation R, homMap R^T preserves L, so actC R and actT R map maxCone into itself, and '
     'R^-1 = R^T is a rotation, so the images are equal. EvenCycle as M_cl.12.')
note('M_max.R', 'M_max satisfies hcls, hadm, hcl, H and C, and fails hgate. It refutes "hcls, hadm, hcl, H and C '
     'imply hgate": hgate is not necessary relative to the other four hypotheses and the conclusion. It does not '
     'show that hcls, hadm, hcl and H imply C; M_D below refutes that implication.')

# ===============================================================================================================
section('S6  the other models')

note('M_Q', 'uniform Q3, N_p = cnot, every local the identity: hcls (M_cl.1), hadm (S1), hcl, hgate (D1), H (S3, S2) '
     'and C (D7, M_cl.12) all hold. The hypothesis set is satisfiable with its conclusion.')
singlet = sp.Matrix([0, 1, -1, 0])
chk('M_D.1', 'M_D: N_13 = actT reflY . cnot is the N-CLASS form with B_13 = reflY (orthogonal) and the other '
    'locals I; N_13 maps prodState xplus z3 (in Q3) to actT reflY phiW = idW (landed actT_reflY_phiW), and '
    'pauliW idW takes -1 on the unnormalized singlet (0, 1, -1, 0), so idW is not in Q3',
    reflY.T * reflY == I3 and mzero(actT(reflY, cnot(Wsym)) - actC(I3, actT(reflY, cnot(actC(I3, actT(I3, Wsym))))))
    and actT(reflY, cnot(prodState(xplus, z3))) == idW and (dag(singlet) * pauliW(idW) * singlet)[0, 0] == -1,
    'witness')
chk('M_D.2', 'M_D: orient(I, reflY) is true and every other orientation bit false: EvenCycle fails',
    det_orient(I3, reflY) and not det_orient(I3, I3), 'witness')
note('M_D.R', 'M_D (uniform Q3, N = cnot at 01, 23, 02 and actT reflY . cnot at 13) satisfies hcls, hadm, hcl and H, '
     'fails hgate at 13, and fails EvenCycle. It refutes "hcls, hadm, hcl and H imply C": hgate cannot be dropped.')

chk('M_refl.1', 'M_refl: with A_13 = reflY and N_13 = cnot, the N-CLASS identity fails at prodState xplus z3 '
    '(cnot gives phiW, actC reflY (cnot .) gives idW)',
    cnot(prodState(xplus, z3)) == phiW and actC(reflY, cnot(prodState(xplus, z3))) == idW and phiW != idW, 'witness')
note('M_refl.R', 'M_refl (uniform Q3, N = cnot, A_13 = reflY, other locals I) satisfies hadm, hcl, hgate and H, '
     'fails hcls at 13 and fails EvenCycle (orient(reflY, I) true at 13 only). It refutes "hadm, hcl, hgate and H '
     'imply C": hcls cannot be dropped.')

A3s = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'A{i}{j}', real=True))
B3s = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'B{i}{j}', real=True))
chk('M_id.1', 'det (actC A (actT B phiW)) = -det A det B, symbolic A, B (nonzero for orthogonal A, B)',
    zero(actC(A3s, actT(B3s, phiW)).det() + A3s.det() * B3s.det()), 'identity')
note('M_id.1W', 'an N-CLASS gate with orthogonal locals maps the product state prodState (A\'^T xplus) (B\'^T z3) to '
     'actC A (actT B phiW), of table rank 4 (M_id.1, M_cl.11); the identity maps every product state to a table of '
     'rank 1. So N = id is N-CLASS for no choice of locals.')
note('M_id.R', 'M_id (uniform Q3, N = id, every local I) satisfies hadm, hcl, hgate, H and C, and fails hcls. It '
     'refutes "hadm, hcl, hgate, H and C imply hcls": hcls is not necessary.')

cls_gens = [prodState([0, 0, s1], [0, 0, t1]) for s1 in (1, -1) for t1 in (1, -1)]
chk('M_class.1', 'M_class: cnot permutes the four classical products prodState (s z3) (t z3), s, t = +-1',
    sorted([tuple(cnot(g)) for g in cls_gens]) == sorted([tuple(g) for g in cls_gens])
    and all(cnot(prodState([0, 0, s1], [0, 0, t1])) == prodState([0, 0, s1], [0, 0, s1 * t1])
            for s1 in (1, -1) for t1 in (1, -1)), 'witness')
ok_cls = True
for s1, t1, s2, t2 in product((1, -1), repeat=4):
    Xc, Yc = prodState([0, 0, s1], [0, 0, t1]), prodState([0, 0, s2], [0, 0, t2])
    ok_cls = ok_cls and zero(fourVal(Xc, Yc, Eg, Fg)
                             - ipW(Eg, prodState([0, 0, s1], [0, 0, s2])) * ipW(Fg, prodState([0, 0, t1], [0, 0, t2])))
    ok_cls = ok_cls and zero(famII_val(Eg, Fg, Xc, Yc)
                             - ipW(Eg, prodState([0, 0, s1], [0, 0, s2])) * ipW(Fg, prodState([0, 0, t1], [0, 0, t2])))
chk('M_class.2', 'M_class: at every pair of generators X, Y, fourVal X Y E F and the famII value factor as '
    'ipW E (generator) * ipW F (generator), symbolic E, F (16 sign choices)', ok_cls, 'identity')
note('M_class.2W', 'with E, F in dualW K_class both factors are nonnegative, and bilinearity extends FCC from the '
     'generators to K_class. K_class lies in maxCone and is a closed convex cone, so S2 gives KT4Core.')
pxx = prodState(xplus, xplus)
chk('M_class.3', 'M_class: prodState xplus xplus has entry (1, 1) = 1 while every element of K_class vanishes off '
    'the entries {0, 3} x {0, 3}: hadm fails', pxx[1, 1] == 1
    and all(g[m, n] == 0 for g in cls_gens for m in R4 for n in R4 if not (m in (0, 3) and n in (0, 3))), 'witness')
chk('M_class.4', 'M_class: actT R_H (prodState z3 z3) = prodState z3 xplus, with entry (3, 1) = 1: IE1 fails',
    actT(RH, prodState(z3, z3)) == prodState(z3, xplus) and prodState(z3, xplus)[3, 1] == 1, 'witness')
note('M_class.R', 'M_class (K = the cone of the four classical products, N = cnot, locals I) satisfies hcls, hcl, '
     'hgate and H, fails the product clause of hadm, and fails IE1. It refutes "hcls, hcl, hgate and H imply C": '
     'hadm cannot be dropped.')

chk('M_mix.1', 'M_mix: cnot E00 = E00, actC R E00 = actT R E00 = E00 for symbolic R, and fourVal E00 E00 E F = '
    'E_00 F_00 (symbolic E, F)', cnot(E00) == E00 and mzero(actC(Rg, E00) - E00) and mzero(actT(Rg, E00) - E00)
    and zero(fourVal(E00, E00, Eg, Fg) - Eg[0, 0] * Fg[0, 0]) and zero(famII_val(Eg, Fg, E00, E00) - Eg[0, 0] * Fg[0, 0]),
    'identity')
note('M_mix.R', 'M_mix (K = the ray of E00, N = cnot, locals I) satisfies hcls, hcl, hgate, H (dualW K = '
     '{E : E_00 >= 0}) and C, and fails hadm (prodState xplus xplus is not on the ray). It refutes "hcls, hcl, '
     'hgate, H and C imply hadm": hadm is not necessary. (K = {0} is a degenerate model of the same kind.)')

chk('M_int.1', 'M_int: pairVal (1,1,0,0) (1,-1,0,0) idW = 0 (idW is on the boundary of maxCone) and idW is not in Q3 '
    '(singlet value -1)', pairVal([1, 1, 0, 0], [1, -1, 0, 0], idW) == 0
    and (dag(singlet) * pauliW(idW) * singlet)[0, 0] == -1, 'witness')
chk('M_int.2', 'M_int: pairVal a b (idW + E00) = 2 a0 b0 + a1 b1 + a2 b2 + a3 b3 (symbolic), cnot E00 = E00, and '
    'cnot (idW + E00) takes -1/4 at the sharp pair of M_max.4', zero(
        pairVal(av, bv, idW + E00) - (2 * av[0] * bv[0] + av[1] * bv[1] + av[2] * bv[2] + av[3] * bv[3]))
    and cnot(idW + E00) == chainW + E00 and pairVal(SHARP_NEGX, SHARP_NEGZ, cnot(idW + E00)) == Q(-1, 4), 'witness')
note('M_int.R', 'M_int (K = int maxCone u Q3, N = cnot, locals I): idW + E00 lies in int maxCone (a^T w b >= a0 b0 > '
     '0 on nonzero a, b in L, M_int.2 and F6) and cnot maps it out of maxCone, so hgate fails; idW lies in '
     'cl K = maxCone and not in K (M_int.1), so hcl fails; hcls, hadm, H (cl K = maxCone, S3) and C (both parts are '
     'rotation invariant) hold. It refutes "hcls, hadm, H and C imply hcl": a proof that hcl is necessary must use '
     'hgate.')

# ===============================================================================================================
section('S7  the token clauses: an anchor carrier')

note('T.def', 'the anchor carrier: V and stA, stB as in S2; effA_anc e f (P, Q) = eh^T P fh + e(l0) f(l1) Q[0, 0]; '
     'effB_anc e f (P, Q) = eh^T Q fh + e(x0) f(y0) P[0, 0], with every anchor the flattened product state '
     'prodState z3 z3, which lies in every pair body considered here.')
anc = [prodState(z3, z3)[m, n] for m in R4 for n in R4]


def effA_anc(e, f, V):
    P, Qm = V
    return (eh17(e).T * P * eh17(f))[0, 0] + aff(e, anc) * aff(f, anc) * Qm[0, 0]


def effB_anc(e, f, V):
    P, Qm = V
    return (eh17(e).T * Qm * eh17(f))[0, 0] + aff(e, anc) * aff(f, anc) * P[0, 0]


chk('T1', 'anchor carrier: evaluation laws effA_anc e f (stA x y) = e(x) f(y), effB_anc e f (stB x y) = e(x) f(y), '
    'symbolic', zero(effA_anc(eS, fS, stAxy) - aff(eS, xS) * aff(fS, yS))
    and zero(effB_anc(eS, fS, stBxy) - aff(eS, xS) * aff(fS, yS)), 'identity')
chk('T2', 'anchor carrier: the cross values are e(anchor) f(anchor), independent of x and y, symbolic',
    zero(effB_anc(eS, fS, stAxy) - aff(eS, anc) * aff(fS, anc))
    and zero(effA_anc(eS, fS, stBxy) - aff(eS, anc) * aff(fS, anc)), 'identity')
note('T2W', 'so posBA and posAB hold on the anchor carrier for any cones whose pair bodies contain the anchor: '
     'effects take values in [0, 1] at the anchor.')
x00 = [E00[m, n] for m in R4 for n in R4]
stA00 = stA(x00, x00)
lhs_t = effA_anc(coord(0, 0), coord(0, 3), stA00)
rhs_t = effB_anc(coord(0, 0), coord(0, 3), stA00)
chk('T3', 'anchor carrier: tokA fails at (a, b, c, d) = (0, 0, 0, 3) and x = y = flat E00 (values 0 and 1)',
    lhs_t == 0 and rhs_t == 1, 'witness', f'{lhs_t} vs {rhs_t}')
cnotTw = (lambda w: actT(reflY, cnot(actT(reflY, w))))
chk('T4', 'M_tok: cnotTw = actT reflY . cnot . actT reflY is N-CLASS with B = B\' = reflY, maps actT reflY w to '
    'actT reflY (cnot w), and orient(I, reflY) is true (EvenCycle fails with the bit at 13 alone)',
    mzero(cnotTw(actT(reflY, Wsym)) - actT(reflY, cnot(Wsym))) and mzero(actT(reflY, actT(reflY, Wsym)) - Wsym)
    and det_orient(I3, reflY), 'identity')
note('M_tok.R', 'M_tok (cones Q3, Q3, Q3, twin; gates cnot, cnot, cnot, cnotTw; B_13 = B\'_13 = reflY) on the anchor '
     'carrier satisfies hcls, hadm, hcl, hgate (twin = actT reflY Q3 and T4) and every field of KT4Core except tokA '
     'and tokB, and fails EvenCycle. It refutes "hcls, hadm, hcl, hgate and KT4Core without its token clauses imply '
     'C": the token clauses cannot be dropped. F10 shows FCC fails for these cones, so by Lemma B1 no carrier '
     'carries KT4Core for them.')
note('M_tokC.R', 'M_tokC (uniform Q3, cnot, locals I) on the anchor carrier satisfies hcls, hadm, hcl, hgate, every '
     'other field of KT4Core and C, and fails tokA (T3). It refutes "the other hypotheses and C imply the token '
     'clauses of the given data". By S2 and Lemma B1, under hadm the existence of a carrier with KT4Core is '
     'equivalent to FCC: the cone-level content of the token clauses together with posBA and posAB is FCC.')

# ===============================================================================================================
section('S8  the finite steps of the classification argument')


def Tfull(w):
    return actC(reflY, actT(reflY, w))


chk('C1', 'the full reflection T = actC reflY . actT reflY commutes with cnot, symbolic',
    mzero(cnot(Tfull(Wsym)) - Tfull(cnot(Wsym))), 'identity')
orders = []
ok_c2 = True
for al_, be_, al2, be2 in product(range(2), repeat=4):
    def N0(w, al_=al_, be_=be_, al2=al2, be2=be2):
        return actC(refl_pow(al_), actT(refl_pow(be_), cnot(actC(refl_pow(al2), actT(refl_pow(be2), w)))))
    img = N0(Wsym)
    perm = set()
    for m in R4:
        for n in R4:
            v = img[m, n]
            hits = [(k, l) for k in R4 for l in R4 if v in (Wsym[k, l], -Wsym[k, l])]
            ok_c2 = ok_c2 and len(hits) == 1
            perm.update(hits)
    ok_c2 = ok_c2 and len(perm) == 16
    w, k = N0(Wsym), 1
    while w != Wsym and k <= 8:
        w, k = N0(w), k + 1
    orders.append(k)
    ok_c2 = ok_c2 and k <= 8
chk('C2', 'each of the 16 reflection-pattern gates actC refl^a actT refl^b cnot actC refl^a\' actT refl^b\' is a '
    'signed permutation of the 16 entries of finite order', ok_c2, 'enumerate', f'orders {sorted(set(orders))}')
mixed_ok = True
for a_, b_ in ((0, 1), (1, 0)):
    def M(w, a_=a_, b_=b_):
        return actC(refl_pow(a_), actT(refl_pow(b_), cnot(w)))
    mixed_ok = mixed_ok and M(prodState(xplus, z3)) == idW and M(idW) == chainW
chk('C3', 'mixed patterns: M = actC refl^a actT refl^b . cnot with a + b = 1 sends prodState xplus z3 to idW and idW '
    'to chainW (outside maxCone, M_max.4): no admissible cone is invariant', mixed_ok, 'witness')
PTW = sp.Matrix(4, 4, lambda i, j: 0)
rhoS = pauliW(Wsym)
for i1, j1, i2, j2 in product(range(2), repeat=4):          # partial transpose on the second qubit
    PTW[2 * i1 + i2, 2 * j1 + j2] = rhoS[2 * i1 + j2, 2 * j1 + i2]
chk('C4', 'pauliW (T w) = pauliW(w)^T and pauliW (actT reflY w) = (pauliW w)^{T_2}, symbolic: T maps Q3 onto Q3, '
    'and the twin is the partial-transpose image of Q3',
    mzero(pauliW(Tfull(Wsym)) - rhoS.T) and mzero(pauliW(actT(reflY, Wsym)) - PTW), 'identity')
ZZ = kron(S[3], S[3])
chk('C5', 'CNOT (I (x) Z) CNOT^dagger = Z (x) Z', CNOT * kron(S[0], S[3]) * dag(CNOT) == ZZ, 'identity')
gens = [iu * kron(S[k], S[0]) for k in (1, 2, 3)] + [iu * kron(S[0], S[k]) for k in (1, 2, 3)] + [iu * ZZ]


def realvec(M):
    return [sp.re(v) for v in M] + [sp.im(v) for v in M]


basis = []


def add_if_new(M):
    cand = basis + [realvec(M)]
    if sp.Matrix(cand).rank() > len(basis):
        basis.append(realvec(M))
        return True
    return False


elems = []
for g in gens:
    if add_if_new(g):
        elems.append(g)
changed = True
while changed:
    changed = False
    for A_ in list(elems):
        for B_ in list(elems):
            Cm = (A_ * B_ - B_ * A_).applyfunc(sp.expand)
            if any(v != 0 for v in Cm) and add_if_new(Cm):
                elems.append(Cm)
                changed = True
chk('C6', 'the real Lie algebra generated by i s_k (x) I, i I (x) s_k and i Z (x) Z has dimension 15 = dim su(4)',
    len(basis) == 15, 'enumerate', f'dimension {len(basis)}')
note('C.W', 'the classification argument (written; it uses no H and no hcl). Write each local as a rotation times '
     'reflY^k. IE1 absorbs the rotations, so hgate gives N0 K in K for a reflection-pattern gate N0, and by C2 '
     'N0 K = K. Conjugating by the pre-local reflections reduces N0 to M = actC refl^a actT refl^b . cnot on a cone '
     'K\' that still satisfies hadm and IE1. Mixed patterns are impossible (C3). In the matched patterns K\' is '
     'invariant under Ad(U (x) V) for U, V in SU(2) (D7) and under M, hence under the conjugates of '
     'Ad(I (x) exp(-i t Z/2)) by M, which are Ad(exp(-+ i t Z (x) Z/2)) (C5, and C4 for the full reflection T, '
     'which conjugates Ad(V) to Ad(conj V)). The group generated by these one-parameter groups is SU(4), since their '
     'generators span a Lie algebra of dimension 15 (C6; the subgroup generated by one-parameter subgroups is the '
     'connected Lie subgroup of the generated Lie algebra, a standard result of Lie theory). So K\' is unitarily '
     'invariant; it contains the product states, hence every pure state and Q3; and it lies in maxCone, so it lies '
     'in Q3 (a non-positive direction phi would be rotated to |00>, where the pairing with the sharp effects of '
     'e3, e3 is negative, D4). So K\' = Q3 and K is Q3 or the twin (C4), both closed. Hence hcls, hadm, hgate and IE1 '
     'imply hcl: relative to the other hypotheses and the conclusion, hcl is necessary. This is a written proof with '
     'one standard input from Lie theory; it is not kernel-checked, and C1-C6 check its finite steps only.')

# ===============================================================================================================
section('S9  the composite interface (COMP-1) and the completion route')

uvec = [1, 0, 0, 0]
amu = [sp.Symbol(f'am{i}', real=True) for i in R4]
bmu = [sp.Symbol(f'bm{i}', real=True) for i in R4]
Wn = Wsym.copy()
Wn[0, 0] = 1
comp = (pairVal(amu, bmu, Wn) + pairVal([uvec[i] - amu[i] for i in R4], bmu, Wn)
        + pairVal(amu, [uvec[i] - bmu[i] for i in R4], Wn)
        + pairVal([uvec[i] - amu[i] for i in R4], [uvec[i] - bmu[i] for i in R4], Wn))
chk('I1', 'for w with w_00 = 1 the four product-effect values of e, 1 - e and f, 1 - f sum to 1, and the unit '
    'pairing is w_00, symbolic', zero(comp - 1) and zero(pairVal(uvec, uvec, Wsym) - Wsym[0, 0]), 'identity')
note('I1W', 'so on a normalized subset of maxCone every product of effects takes values in [0, 1]. The normalized '
     'slice of K_cl is convex, contains the product states, lies in maxCone, and has unit pairing 1: it satisfies '
     'every field of PreComposite over the coordinate model data of COMP-1, and the field lt holds by the argument '
     'of the landed minComposite and maxComposite (prodEff_eq_of_eff_eq with modelData_ext). It is a Composite '
     'whose body is not closed (M_cl.7-M_cl.9) and not invariant under local rotations (M_cl.11W), while cnot '
     'preserves it.')
Fw = lambda w: w[0, 0] - w[1, 1] + w[2, 2] - w[3, 3]
Dm = sp.diag(1, -1, 1)
xv, yv = sp.Matrix(xs), sp.Matrix(ys)
chk('I2', 'F(w) = w00 - w11 + w22 - w33 satisfies F(prodState x y) = |x - D y|^2/2 + (1 - |x|^2)/2 + (1 - |y|^2)/2 '
    'with D = diag(1, -1, 1), symbolic, and F(phiW) = -2', zero(
        Fw(prodState(xs, ys)) - ((xv - Dm * yv).dot(xv - Dm * yv) / 2 + (1 - xv.dot(xv)) / 2 + (1 - yv.dot(yv)) / 2))
    and Fw(phiW) == -2, 'witness')
note('I2W', 'F is nonnegative on every product of ball points, hence on the minimal body, and negative at '
     'phiW = cnot (prodState xplus z3): cnot does not preserve the body of the landed ball3MinComposite. By M_max.3, '
     'M_max.4 and F6, idW lies in the body of the landed ball3MaxComposite (idW_00 = 1) and cnot idW does not: cnot '
     'does not preserve that body either. The landed no_candidateCone_cnot_reflY shows that no candidate cone is '
     'invariant under both cnot and actT reflY.')
note('Q2.W', 'the landed completion layer is typed for one directed system of stages: StageCompletion.body is the '
     'closed convex hull of the preparation vectors (CompletionAction.body_isClosed), and an operation datum with '
     'an inverse datum induces a body-preserving affine equivalence of the chart (preservesBody_inducedEquiv). No '
     'landed declaration constructs a directed system for a pair of systems, an operation datum for a pair gate, or '
     'a map from the table carrier W 3 to a completion chart. A pair-level route therefore needs (P-STAGE2) the pair '
     'system as a directed system whose completion chart is W 3 with chart body the normalized slice of K, which '
     'gives hcl, and (P-ACT2) the gate N as an operation datum on it with an inverse datum, inducing N on the chart, '
     'which gives hgate. P-ACT2 states gate preservation on the preparations (OpDatum.mem_body). Building the datum '
     'for N = actC A . actT B . cnot . actC A\' . actT B\' from one-copy data needs idle extension of the local maps '
     'to the pair; for local rotations idle extension is IE1 itself, and for reflY it is refuted on cnot-invariant '
     'candidate cones by no_candidateCone_cnot_reflY.')

# ===============================================================================================================
section('S10 countercontrols')


def cnot_mut(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in {(1, 3)} else 1) * w[PC[m][n], PT[m][n]])


chk('X1', 'a cnot with the sign at (2, 2) flipped is not conjugation by CNOT (D1 fails for it)',
    not mzero(pauliW(cnot_mut(Wsym)) - CNOT * pauliW(Wsym) * dag(CNOT)), 'countercontrol')


def effA_mut(e, f, V):
    P, Qm = V
    Et, Ft = Etil(e), Etil(f)
    return (eh17(e).T * P * eh17(f))[0, 0] + sum(
        Et[a, b] * Ft[c, d] * Qm[1 + idx(a, b), 1 + idx(c, d)] for a, b, c, d in product(R4, repeat=4))


bad_mut = [(a, b, c, d) for a, b, c, d in product(R4, repeat=4)
           if not zero(effA_mut(coord(a, b), coord(c, d), stBxy) - effB(coord(a, c), coord(b, d), stBxy))]
chk('X2', 'a carrier whose cross term reads the 02|13 state in the 01|23 order fails tokB', len(bad_mut) > 0,
    'countercontrol', f'{len(bad_mut)} of 256 quadruples fail')
Rrot = sp.Matrix([[Q(3, 5), Q(-4, 5), 0], [Q(4, 5), Q(3, 5), 0], [0, 0, 1]])
chk('X3', 'the rotation covariance with homMap R in place of homMap R^T fails for a non-symmetric rotation',
    not zero(pairVal(av, bv, actC(Rrot, Wsym)) - pairVal(list(homMap(Rrot) * sp.Matrix(av)), bv, Wsym)),
    'countercontrol')
chk('X4', 'without the normalization w_00 = 1 the four product-effect values sum to w_00, not 1', not zero(
    pairVal(amu, bmu, Wsym) + pairVal([uvec[i] - amu[i] for i in R4], bmu, Wsym)
    + pairVal(amu, [uvec[i] - bmu[i] for i in R4], Wsym)
    + pairVal([uvec[i] - amu[i] for i in R4], [uvec[i] - bmu[i] for i in R4], Wsym) - 1), 'countercontrol')
chk('X5', 'F10 with F replaced by phiW/4 (in dualW Q3): the value at the same states is 1/4 >= 0, so the sign '
    'of F10 comes from the twin effect', fourVal(phiW, phiW, Ecc, Ecc) == Q(1, 4), 'countercontrol')
Ysing = sp.diag(1, -1, -1, -1)
chk('X6', 'maxCone with an effect outside its dual: idW and diag(1,-1,-1,-1) lie in maxCone, phiW is not in '
    'dualW maxCone (ipW phiW diag(1,-1,1,-1) = -2 with diag(1,-1,1,-1) = actT reflY diag(1,-1,-1,-1) in maxCone), '
    'and fourVal idW diag(1,-1,-1,-1) phiW phiW = -2: the product form of dualW maxCone is load-bearing in F.max',
    is_psd_projector(pauliW(Ysing)) and actT(reflY, Ysing) == sp.diag(1, -1, 1, -1)
    and ipW(phiW, sp.diag(1, -1, 1, -1)) == -2 and fourVal(idW, Ysing, phiW, phiW) == -2, 'countercontrol')

# ===============================================================================================================
print()
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'witness', 'enumerate', 'source', 'sample', 'countercontrol')),
      flush=True)
failed = [c[0] for c in CHECKS if not c[2]]
if failed:
    print(f"kt4_prem1_probe: FAILED -- {len(failed)} of {len(CHECKS)} checks: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'kt4_prem1_probe: OK -- {len(CHECKS)} checks', flush=True)
