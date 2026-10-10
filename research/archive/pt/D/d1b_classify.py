#!/usr/bin/env python3
"""Thread D, certified script d1b -- the exact steps of the N-CLASS route (RESULT.md section 1, D1.0-D1.3).

Conventions are DIM-1's (CompositeDimension.lean), checked against the landed sources in C0: tables w in W 3 = R^{4x4},
index 0 the unit, 1..3 the ball coordinates (x, y, z); hom x = (1, x); prodState x y = hom x hom y^T;
homMap R = diag(1, R); actC R w = homMap R . w (first token, the control); actT R w = w . homMap R^T (second token);
pairVal a b w = a^T w b; maxCone (eball 3) = {w : pairVal a b w >= 0 for all a, b in L}, L = {a : a0 >= |(a1,a2,a3)|}.
HN = homMap nflip = diag(1, 1, -1, -1). S: Y -> (Y1, Y0, 0, 0). T: Y -> (0, 0, -Y3, Y2). J' = [[0, -1], [1, 0]].

The normalized family G(a, b), for 2x2 real matrices a, b (the frame M0 = id, M1 = nflip of the written route):
  G(hom z3 (x) Y) = hom z3 (x) Y;  G(hom(-z3) (x) Y) = hom(-z3) (x) HN Y;
  G(e_j (x) Y) = sum_{i=1,2} e_i (x) (a[i][j] S Y + b[i][j] T Y)   for j = 1, 2 (control coherence directions).

DECISION RULES (fixed before the first run; rules, not expected numbers). Each check prints PASS or FAIL.
  C0  [source] every transcribed landed definition must match the Lean text at L.
  C1  M_refl: cnot must satisfy frame, relT, relC as exact identities; NClass(cnot, reflY, I, I, I) must FAIL at
      prodState xplus z3 and NClass(cnot, I, I, I, I) must hold identically.
  C2  the family: G(I, J') = cnot; frame for symbolic a, b; the pairing identity
      pairVal(hom u, b, G(prodState x y)) = 2 p_u p_x <b,Y> + 2 q_u q_x <b, HN Y> + u'^T (sigma a + tau b) x'
      (p = (1 + third coordinate)/2, q = 1 - p, u' = first two coordinates, sigma = b^T S Y, tau = b^T T Y);
      G(a, b)^-1 = G(a^-1, -b^-1) for symbolic invertible a, b.
  C3  test points: at b = Y = (1,1,0,0) and u, x on the equator the pairing must equal 2 + 2 u'^T a x'; at
      b = (1,0,1,0), Y = (1,0,0,1) it must equal 1 - u'^T b x' (symbolic a, b, u', x').
  C4  the null-pair identity <b,Y><b,HN Y> - sigma^2 - tau^2 = (b0^2-b1^2)(Y0^2-Y1^2) - (b2^2+b3^2)(Y2^2+Y3^2) must
      hold symbolically; two rational null pairs must have Delta = 0 and sigma*tau of opposite signs.
  C5  for U in O(2) (rotation and reflection parametrizations, modulo c^2 + s^2 = 1):
      (sigma I + tau U)^T (sigma I + tau U) = (sigma^2 + tau^2) I + sigma tau (U + U^T) must hold.
  C6  G(a, +-a J') = actC(diag(a, 1)) . G(I, +-J') for symbolic a; G(I, -J') = actC reflY . cnot . actC reflY.
  C7  relC for G(a, b) must hold exactly when a is diagonal and b antidiagonal; each of the 8 diagonal sign patterns
      with s1 s2 t1 t2 = -1 must equal actC D . cnot . actC D' for diagonal sign D, D'; each of the 8 with product +1
      must have an exact rational point (u, x in the ball, b, Y in L) where the pairing is negative (posFwd fails).
  C8  positive control: actC(Rot_z(3/5, 4/5)) . cnot satisfies the frame and FAILS relC, and is G(Rot, Rot J').
  C9  orientation: det homMap(a) = det a; det(actC a (actT b w)) = det a det b det w (symbolic); det phiW = -1;
      det cnot(prodState x y) = -(x0^2+x1^2)(1-x2^2)(1-y0^2)(y1^2+y2^2) (symbolic, hence <= 0 on ball x ball).
  C10 minimality countermodels, each must satisfy the stated clauses and must FAIL N-CLASS form:
      G(I/2, J'/2): frame, relC, relT, the posFwd decomposition identity; posInv fails at an exact witness;
      not ipW-orthogonal (N-CLASS gates are ipW-orthogonal: cnot and homMap of an orthogonal map preserve ipW).
      G(2I, 2J') = its inverse: posFwd fails at an exact witness, posInv holds (inverse is G(I/2, J'/2)).
      id with z = 0: frame holds trivially (unit fails); id with z = z3: frame FAILS at an exact witness. id is not
      N-CLASS: det(actC A (actT B phiW)) = -det A det B (symbolic) while id maps every product to a rank-1 table.
      improper control: the controlled-(id, diag(1,1,-1)) map with any coherence built from the forms that vanish on
      its zero set annihilates e1 (x) e3 (not injective).
  A VERDICT line is printed only if every check passes and every countercontrol behaves as stated.
Exact arithmetic only (sympy and fractions). No floating point, no randomness, no timing in stdout.
"""
import re
import sys
from fractions import Fraction as Fr
from itertools import product
from pathlib import Path

import sympy as sp

CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


def section(t):
    print()
    print(f'== {t}', flush=True)


R4 = range(4)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def sgn(m, k):
    return -1 if (m, k) in NEG else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, k: sgn(m, k) * w[PC[m][k], PT[m][k]])


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def hom(x):
    return sp.Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def pairVal(a, b, w):
    return (sp.Matrix(a).T * w * sp.Matrix(b))[0, 0]


def ipW(E, X):
    return sum(E[m, k] * X[m, k] for m in R4 for k in R4)


I3 = sp.eye(3)
NFLIP = sp.diag(1, -1, -1)
REFLY = sp.diag(1, -1, 1)
HN = homMap(NFLIP)
z3 = [0, 0, 1]
mz3 = [0, 0, -1]
xplus = [1, 0, 0]
phiW = sp.diag(1, 1, -1, 1)
Smat = sp.zeros(4, 4); Smat[0, 1] = 1; Smat[1, 0] = 1
Tmat = sp.zeros(4, 4); Tmat[2, 3] = -1; Tmat[3, 2] = 1
Jp = sp.Matrix([[0, -1], [1, 0]])
I2 = sp.eye(2)
E = [sp.Matrix([1 if k == m else 0 for k in R4]) for m in R4]
HZ = sp.Matrix([1, 0, 0, 1])
HMZ = sp.Matrix([1, 0, 0, -1])


def corner(a):
    return z3 if a == 0 else mz3


def G_family(a, b):
    a = sp.Matrix(a); b = sp.Matrix(b)

    def G(w):
        out = sp.zeros(4, 4)
        for mu in R4:
            row = w[mu, :].T
            if mu == 0:
                out += (HZ * row.T + HMZ * (HN * row).T) / 2
            elif mu == 3:
                out += (HZ * row.T - HMZ * (HN * row).T) / 2
            else:
                j = mu - 1
                for i in range(2):
                    out += E[i + 1] * (a[i, j] * Smat * row + b[i, j] * Tmat * row).T
        return out
    return G


def frame_holds(G, zc=None):
    zc = zc if zc is not None else (z3, mz3)
    cor = {0: list(zc[0]), 1: list(zc[1])}
    return all(sp.expand(G(prodState(cor[p], cor[q])) - prodState(cor[p], cor[(p + q) % 2])) == sp.zeros(4, 4)
               for p in (0, 1) for q in (0, 1))


Wsym = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'w{i}{j}', real=True))


def is_zero_mat(M):
    return all(sp.simplify(v) == 0 for v in M)


# =====================================================================================================================
section('C0  transcription of the landed definitions at L (read-only)')
BASE = Path('/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt/base')
INP = Path('/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt/inputs')
CD = (BASE / 'verification/lean-mathlib/OIBridge/CompositeDimension.lean').read_text(encoding='utf-8')
KG = (BASE / 'verification/lean-mathlib/OIBridge/K2Guard.lean').read_text(encoding='utf-8')
RSB = (BASE / 'verification/lean-mathlib/OIBridge/RelcSelectBlock.lean').read_text(encoding='utf-8')
FCC = (INP / 'fourcopy/FourCopyCore.lean').read_text(encoding='utf-8')

msg = re.search(r'^def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1$',
                CD, re.M)
chk('C0.sgn', 'sgn is -1 exactly at (1,3) and (2,2)',
    msg is not None and {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))} == NEG, 'source')


def lean_table(nm):
    mm = re.search(rf'^def {nm} : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){{4}})', CD, re.M)
    if not mm:
        return None
    Tb = [[None] * 4 for _ in R4]
    for x1, x2, v in re.findall(r'\|\s*(\d),\s*(\d)\s*=>\s*(\d)', mm.group(1)):
        Tb[int(x1)][int(x2)] = int(v)
    return Tb


chk('C0.pc', 'pc table', lean_table('pc') == PC, 'source')
chk('C0.pt', 'pt table', lean_table('pt') == PT, 'source')
chk('C0.cnotFun', 'cnotFun w = sgn * w (pc, pt)',
    'def cnotFun (ω : W 3) : W 3 := fun μ ν => sgn μ ν * ω (pc μ ν) (pt μ ν)' in CD, 'source')
chk('C0.nflip', 'nflip = diag(1, -1, -1)', 'toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i' in CD, 'source')
chk('C0.z3', 'z3 = (0, 0, 1)', 'def z3 : Fin 3 → ℝ := ![0, 0, 1]' in CD, 'source')
chk('C0.reflY', 'reflY = diag(1, -1, 1)', 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i' in KG, 'source')
chk('C0.phiW', 'phiW = diag(1, 1, -1, 1)',
    'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD, 'source')
chk('C0.acts', 'actT N w = fun mu => homMap N (w mu); actC N w mu nu = homMap N (fun k => w k nu) mu',
    'def actT (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : W d := fun μ => homMap N (ω μ)' in CD
    and 'fun μ ν => homMap N (fun κ => ω κ ν) μ' in CD, 'source')
chk('C0.prod', 'prodState x y = hom x mu * hom y nu',
    'def prodState (x y : Fin d → ℝ) : W d := fun μ ν => hom x μ * hom y ν' in CD, 'source')
chk('C0.isNot', 'IsNot fields: unit, invol, preserves, flips',
    all(s in CD for s in ('unit : ∑ j, z j ^ 2 = 1', 'invol : ∀ x, N (N x) = x', 'preserves : ∀ x ∈ Ω, N x ∈ Ω',
                          'flips : N z = -z')), 'source')
chk('C0.ctrl', 'CtrlGate (RelcSelectBlock) fields: frame, posFwd, posInv, relC and no relT',
    re.search(r'structure CtrlGate[\s\S]*?frame : ∀ a b : Fin 2,\n\s*G \(prodState \(corner z a\) \(corner z b\)\) = '
              r'prodState \(corner z a\) \(corner z \(a \+ b\)\)\n\s*posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G \(prodState x y\) ∈ '
              r'maxCone Ω\n\s*posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G\.symm \(prodState x y\) ∈ maxCone Ω\n\s*relC : ∀ ω, actC N '
              r'\(G \(actC N ω\)\) = actT N \(G ω\)\n\ntheorem', RSB) is not None, 'source')
chk('C0.nclass', 'NClass (design FourCopyCore): four IsOrth3 clauses and N w = actC A (actT B (cnot (actC A\' (actT B\' w))))',
    "IsOrth3 A ∧ IsOrth3 B ∧ IsOrth3 A' ∧ IsOrth3 B' ∧\n    ∀ ω, N ω = actC A (actT B (cnot (actC A' (actT B' ω))))" in FCC,
    'source')
chk('C0.corner_form', 'corner_form (CD) hypotheses: unit z, the fixing frame at corner z, product positivity of a linear map',
    re.search(r'theorem corner_form \{z : Fin d → ℝ\} \(hz : ∑ j, z j \^ 2 = 1\) \{G\' : W d →ₗ\[ℝ\] W d\}\n\s*\(hframe : '
              r'∀ b : Fin 2, G\' \(prodState z \(corner z b\)\) = prodState z \(corner z b\)\)\n\s*\(hpos : ∀ x ∈ eball d, '
              r'∀ y ∈ eball d, G\' \(prodState x y\) ∈ maxCone \(eball d\)\) \(Y : HVec d\) :\n\s*G\' \(tens \(hom z\) Y\) = '
              r'tens \(hom z\) \(cornerMap z G\' Y\)', CD) is not None, 'source')

# =====================================================================================================================
section('C1  M_refl: the gate is cnot; the supplied post-local reflY is not a decomposition local')
chk('C1.frame', 'cnot satisfies the frame at z3 (exact)', frame_holds(cnot), 'identity')
chk('C1.rel', 'cnot satisfies relT and relC with nflip (symbolic table)',
    is_zero_mat(actT(NFLIP, cnot(actT(NFLIP, Wsym))) - cnot(Wsym))
    and is_zero_mat(actC(NFLIP, cnot(actC(NFLIP, Wsym))) - actT(NFLIP, cnot(Wsym))), 'identity')
chk('C1.idlocals', 'NClass(cnot, I, I, I, I): cnot w = actC I (actT I (cnot (actC I (actT I w)))) (symbolic)',
    is_zero_mat(cnot(Wsym) - actC(I3, actT(I3, cnot(actC(I3, actT(I3, Wsym)))))), 'identity')
p0 = prodState(xplus, z3)
chk('C1.mrefl', 'NClass(cnot, reflY, I, I, I) fails at prodState xplus z3: cnot gives phiW, the claimed form gives '
    'actC reflY phiW = idW', cnot(p0) == phiW and actC(REFLY, cnot(p0)) == sp.eye(4) and phiW != sp.eye(4), 'witness')

# =====================================================================================================================
section('C2  the normalized family G(a, b)')
a11, a12, a21, a22, b11, b12, b21, b22 = sp.symbols('a11 a12 a21 a22 b11 b12 b21 b22', real=True)
Aa = sp.Matrix([[a11, a12], [a21, a22]])
Bb = sp.Matrix([[b11, b12], [b21, b22]])
Gab = G_family(Aa, Bb)
chk('C2.cnot', 'G(I, J\') = cnot (symbolic table)', is_zero_mat(G_family(I2, Jp)(Wsym) - cnot(Wsym)), 'identity')
chk('C2.frame', 'every G(a, b) satisfies the frame at z3 (symbolic a, b)', frame_holds(Gab), 'identity')
Ysym = sp.Matrix(sp.symbols('Y0:4', real=True))
chk('C2.slices', 'G(a, b)(hom z3 (x) Y) = hom z3 (x) Y and G(a, b)(hom(-z3) (x) Y) = hom(-z3) (x) HN Y (symbolic Y)',
    is_zero_mat(Gab(HZ * Ysym.T) - HZ * Ysym.T) and is_zero_mat(Gab(HMZ * Ysym.T) - HMZ * (HN * Ysym).T), 'identity')
u = sp.symbols('u0:3', real=True); xs = sp.symbols('x0:3', real=True)
bs = sp.symbols('b0:4', real=True); ys = sp.symbols('y0:3', real=True)
Yv = hom(ys); bv = sp.Matrix(bs)
lhs = pairVal(hom(u), bv, Gab(prodState(xs, ys)))
pu, qu, px, qx = (1 + u[2]) / 2, (1 - u[2]) / 2, (1 + xs[2]) / 2, (1 - xs[2]) / 2
sig = (bv.T * Smat * Yv)[0, 0]; tau = (bv.T * Tmat * Yv)[0, 0]
Lam = sig * Aa + tau * Bb
rhs = 2 * pu * px * (bv.T * Yv)[0, 0] + 2 * qu * qx * (bv.T * HN * Yv)[0, 0] \
    + (sp.Matrix([u[0], u[1]]).T * Lam * sp.Matrix([xs[0], xs[1]]))[0, 0]
chk('C2.pairing', 'pairVal(hom u, b, G(a,b)(prodState x y)) = 2 p_u p_x <b,Y> + 2 q_u q_x <b,HN Y> + u\'^T(sigma a + '
    'tau b) x\' (symbolic u, x, b, y, a, b)', sp.expand(lhs - rhs) == 0, 'identity')
Ginv = G_family(Aa.inv(), -Bb.inv())
chk('C2.inverse', 'G(a, b) . G(a^-1, -b^-1) = id = G(a^-1, -b^-1) . G(a, b) (symbolic invertible a, b)',
    is_zero_mat(Gab(Ginv(Wsym)) - Wsym) and is_zero_mat(Ginv(Gab(Wsym)) - Wsym), 'identity')

# =====================================================================================================================
section('C3  the test points that bound a and b')
up = sp.symbols('v0:2', real=True); xp = sp.symbols('t0:2', real=True)
va = pairVal(hom([up[0], up[1], 0]), [1, 1, 0, 0], Gab(prodState([xp[0], xp[1], 0], [1, 0, 0])))
chk('C3.a', 'at b = Y = (1,1,0,0), u = (u\', 0), x = (x\', 0): pairing = 2 + 2 u\'^T a x\' (symbolic)',
    sp.expand(va - (2 + 2 * (sp.Matrix(up).T * Aa * sp.Matrix(xp))[0, 0])) == 0, 'identity')
vb = pairVal(hom([up[0], up[1], 0]), [1, 0, 1, 0], Gab(prodState([xp[0], xp[1], 0], z3)))
chk('C3.b', 'at b = (1,0,1,0), Y = hom z3, u = (u\', 0), x = (x\', 0): pairing = 1 - u\'^T b x\' (symbolic)',
    sp.expand(vb - (1 - (sp.Matrix(up).T * Bb * sp.Matrix(xp))[0, 0])) == 0, 'identity')
chk('C3.L', 'the effect vectors used are in L: (1,1,0,0), (1,0,1,0), hom of unit vectors (u\', 0)',
    all(v[0] >= 0 and v[0] ** 2 >= v[1] ** 2 + v[2] ** 2 + v[3] ** 2 for v in ([1, 1, 0, 0], [1, 0, 1, 0])), 'witness')

# =====================================================================================================================
section('C4  null pairs')
B0 = (bv.T * Yv)[0, 0]; B1 = (bv.T * HN * Yv)[0, 0]
Yg = sp.Matrix(sp.symbols('g0:4', real=True))
B0g = (bv.T * Yg)[0, 0]; B1g = (bv.T * HN * Yg)[0, 0]
sg = (bv.T * Smat * Yg)[0, 0]; tg = (bv.T * Tmat * Yg)[0, 0]
Dg = (bs[0] ** 2 - bs[1] ** 2) * (Yg[0] ** 2 - Yg[1] ** 2) - (bs[2] ** 2 + bs[3] ** 2) * (Yg[2] ** 2 + Yg[3] ** 2)
chk('C4.id', '<b,Y><b,HN Y> - sigma^2 - tau^2 = (b0^2-b1^2)(Y0^2-Y1^2) - (b2^2+b3^2)(Y2^2+Y3^2) (symbolic b, Y)',
    sp.expand(B0g * B1g - sg ** 2 - tg ** 2 - Dg) == 0, 'identity')
NULLW = [([3, 2, 2, 1], [3, 1, 2, 2]), ([3, 2, 2, 1], [3, 1, -2, -2])]
vals = []
for bb, YY in NULLW:
    sb = {**{bs[i]: bb[i] for i in R4}, **{Yg[i]: YY[i] for i in R4}}
    vals.append((Dg.subs(sb), sg.subs(sb), tg.subs(sb), B0g.subs(sb), B1g.subs(sb)))
print('   null witnesses (Delta, sigma, tau, B0, B1):', vals)
chk('C4.w', 'two rational null pairs in L x L with Delta = 0 and sigma*tau of opposite signs',
    all(v[0] == 0 for v in vals) and vals[0][1] * vals[0][2] * vals[1][1] * vals[1][2] < 0
    and all(bb[0] ** 2 == sum(t ** 2 for t in bb[1:]) and YY[0] ** 2 == sum(t ** 2 for t in YY[1:]) for bb, YY in NULLW),
    'witness')

# =====================================================================================================================
section('C5  orthogonal U')
cth, sth, sgm, ta = sp.symbols('cth sth sgm ta', real=True)
Urot = sp.Matrix([[cth, -sth], [sth, cth]])
Uref = sp.Matrix([[cth, sth], [sth, -cth]])
ok5 = True
for U in (Urot, Uref):
    M = sgm * I2 + ta * U
    diff = (M.T * M - (sgm ** 2 + ta ** 2) * I2 - sgm * ta * (U + U.T)).applyfunc(
        lambda v: sp.expand(sp.expand(v).subs(sth ** 2, 1 - cth ** 2)))
    ok5 = ok5 and diff == sp.zeros(2, 2)
chk('C5.id', '(sigma I + tau U)^T (sigma I + tau U) = (sigma^2+tau^2) I + sigma tau (U + U^T) for rotations and '
    'reflections U (mod c^2 + s^2 = 1)', ok5, 'identity')
chk('C5.cases', 'U + U^T = 2 cos(theta) I for rotations; for reflections U + U^T = 2U has eigenvalues +2 and -2',
    sp.expand(Urot + Urot.T - 2 * cth * I2) == sp.zeros(2, 2)
    and sp.expand(((Uref + Uref.T) ** 2 - 4 * I2).subs(sth ** 2, 1 - cth ** 2)) == sp.zeros(2, 2)
    and sp.expand((Uref + Uref.T).trace()) == 0, 'identity')

# =====================================================================================================================
section('C6  identification of the survivors')
Rs = sp.Matrix([[a11, a12], [a21, a22]])


def diag_a1(a):
    M = sp.zeros(3, 3)
    M[0:2, 0:2] = a
    M[2, 2] = 1
    return M


ok6 = True
for sgn_ in (1, -1):
    Gs = G_family(Rs, sgn_ * Rs * Jp)
    G0 = G_family(I2, sgn_ * Jp)
    ok6 = ok6 and is_zero_mat(Gs(Wsym) - actC(diag_a1(Rs), G0(Wsym)))
chk('C6.post', 'G(a, +-a J\') = actC(diag(a, 1)) . G(I, +-J\') for symbolic a', ok6, 'identity')
chk('C6.minus', 'G(I, -J\') = actC reflY . cnot . actC reflY (symbolic table)',
    is_zero_mat(G_family(I2, -Jp)(Wsym) - actC(REFLY, cnot(actC(REFLY, Wsym)))), 'identity')

# =====================================================================================================================
section('C7  with relC: the CtrlGate classification in the normalized frame')
relc = actC(NFLIP, Gab(actC(NFLIP, Wsym))) - actT(NFLIP, Gab(Wsym))
eqs = [sp.expand(v) for v in relc if sp.expand(v) != 0]
coeff_eqs = set()
for e_ in eqs:
    for mon, cf in zip(sp.Poly(e_, *list(Wsym)).monoms(), sp.Poly(e_, *list(Wsym)).coeffs()):
        coeff_eqs.add(sp.expand(cf))
solrel = sp.solve(list(coeff_eqs), [a11, a12, a21, a22, b11, b12, b21, b22], dict=True)
print('   relC solution for (a, b):', solrel)
chk('C7.relC', 'relC for G(a, b) holds iff a12 = a21 = 0 and b11 = b22 = 0 (a diagonal, b antidiagonal)',
    len(solrel) == 1 and solrel[0] == {a12: 0, a21: 0, b11: 0, b22: 0}, 'identity')
chk('C7.relT', 'relT holds for every G(a, b) (symbolic)',
    is_zero_mat(actT(NFLIP, Gab(actT(NFLIP, Wsym))) - Gab(Wsym)), 'identity')

# exact witness search for the 8 sign patterns with s1 s2 t1 t2 = +1 (fractions; direct evaluation of the gate)


def fr_family_eval(s1, s2, t1, t2, u3, x3, b4, y3):
    """pairVal(hom u, b, G(prodState x y)) computed directly from the definition with Fractions."""
    Y = [Fr(1)] + [Fr(v) for v in y3]
    X = [Fr(1)] + [Fr(v) for v in x3]
    U = [Fr(1)] + [Fr(v) for v in u3]
    bb = [Fr(v) for v in b4]
    HNY = [Y[0], Y[1], -Y[2], -Y[3]]
    SY = [Y[1], Y[0], Fr(0), Fr(0)]
    TY = [Fr(0), Fr(0), -Y[3], Y[2]]
    out = [[Fr(0)] * 4 for _ in R4]
    # control row 0 and row 3 contributions (w = hom x (x) Y, so control row mu has weight X[mu])
    for mu in (0, 3):
        for k in R4:
            hz_part = Y[k]
            hmz_part = HNY[k]
            if mu == 0:
                out[0][k] += X[0] * (hz_part + hmz_part) / 2
                out[3][k] += X[0] * (hz_part - hmz_part) / 2
            else:
                out[0][k] += X[3] * (hz_part - hmz_part) / 2
                out[3][k] += X[3] * (hz_part + hmz_part) / 2
    a = [[s1, 0], [0, s2]]
    bm = [[0, t1], [t2, 0]]
    for j in range(2):
        for i in range(2):
            for k in R4:
                out[i + 1][k] += X[j + 1] * (a[i][j] * SY[k] + bm[i][j] * TY[k])
    return sum(U[m] * out[m][k] * bb[k] for m in R4 for k in R4)


# cross-check the fraction evaluator against the sympy family at a few exact points
xchk = True
for s1, s2, t1, t2 in ((1, 1, -1, 1), (1, -1, 1, 1), (-1, 1, 1, 1)):
    Gx = G_family(sp.diag(s1, s2), sp.Matrix([[0, t1], [t2, 0]]))
    for (uu, xx, bb, yy) in (((Fr(2, 3), Fr(-2, 3), Fr(-1, 3)), (Fr(1, 3), Fr(2, 3), Fr(2, 3)), (3, 2, 2, 1),
                              (Fr(1, 3), Fr(2, 3), Fr(2, 3))),
                             ((0, Fr(3, 5), Fr(4, 5)), (Fr(4, 5), 0, Fr(-3, 5)), (5, 3, 0, 4), (Fr(3, 5), Fr(4, 5), 0))):
        v1 = fr_family_eval(s1, s2, t1, t2, uu, xx, bb, yy)
        v2 = pairVal(hom([sp.Rational(c) for c in uu]), list(bb), Gx(prodState([sp.Rational(c) for c in xx],
                                                                               [sp.Rational(c) for c in yy])))
        xchk = xchk and sp.Rational(v1.numerator, v1.denominator) == v2
chk('C7.eval', 'the fraction evaluator agrees with the sympy family at 6 exact points', xchk, 'identity')

QUADS = [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11), (6, 6, 7, 11), (3, 4, 12, 13)]
SPH = set()
for (p, q, r, d) in QUADS:
    for perm in ((p, q, r), (p, r, q), (q, p, r), (q, r, p), (r, p, q), (r, q, p)):
        for sgs in product((1, -1), repeat=3):
            SPH.add(tuple(Fr(sgs[k] * perm[k], d) for k in range(3)))
SPH = sorted(SPH)
NULL_Y = [(Fr(1, 3), Fr(2, 3), Fr(2, 3)), (Fr(1, 3), Fr(-2, 3), Fr(-2, 3))]
NULL_B = (3, 2, 2, 1)
ok_bad = True
ok_good_sample = True
bad_report = []
for s1, s2, t1, t2 in product((1, -1), repeat=4):
    best = None
    for yy in NULL_Y:
        for uu in SPH:
            for xx in SPH:
                v = fr_family_eval(s1, s2, t1, t2, uu, xx, NULL_B, yy)
                if best is None or v < best[0]:
                    best = (v, uu, xx, yy)
    if s1 * s2 * t1 * t2 == 1:
        ok_bad = ok_bad and best[0] < 0
        bad_report.append(((s1, s2, t1, t2), str(best[0]), tuple(str(c) for c in best[1]), tuple(str(c) for c in best[2]),
                           tuple(str(c) for c in best[3])))
    else:
        ok_good_sample = ok_good_sample and best[0] >= 0
for line in bad_report:
    print('   pattern', line[0], 'min pairing', line[1], 'at u =', line[2], 'x =', line[3], 'y =', line[4],
          'b = (3,2,2,1)')
chk('C7.bad', 'each of the 8 sign patterns with s1 s2 t1 t2 = +1 has an exact point with negative pairing (posFwd fails)',
    ok_bad and len(bad_report) == 8, 'witness')
chk('C7.goodsample', 'sample: the 8 patterns with product -1 have no negative pairing on the same 2 x 216 x 216 grid',
    ok_good_sample, 'sample')
ok_ncl = True
for s1, s2, t1, t2 in product((1, -1), repeat=4):
    if s1 * s2 * t1 * t2 != -1:
        continue
    found = False
    for d1, d2, e1, e2 in product((1, -1), repeat=4):
        D = sp.diag(d1, d2, 1); Dp = sp.diag(e1, e2, 1)
        Gx = G_family(sp.diag(s1, s2), sp.Matrix([[0, t1], [t2, 0]]))
        if is_zero_mat(Gx(Wsym) - actC(D, cnot(actC(Dp, Wsym)))):
            found = True
            break
    ok_ncl = ok_ncl and found
chk('C7.ncl', 'each of the 8 sign patterns with product -1 equals actC D . cnot . actC D\' for diagonal sign D, D\' '
    '(orthogonal; fixing z3)', ok_ncl, 'identity')

# =====================================================================================================================
section('C8  positive control: a frame-and-positivity gate outside CtrlGate')
Rz = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])


def Gctl(w):
    return actC(Rz, cnot(w))


chk('C8.frame', 'actC(Rot_z(3/5,4/5)) . cnot satisfies the frame at z3', frame_holds(Gctl), 'identity')
chk('C8.relC', 'countercontrol: actC(Rot_z(3/5,4/5)) . cnot FAILS relC with nflip',
    not is_zero_mat(actC(NFLIP, Gctl(actC(NFLIP, Wsym))) - actT(NFLIP, Gctl(Wsym))), 'countercontrol')
Rot2 = Rz[0:2, 0:2]
chk('C8.fam', 'it is G(Rot, Rot J\') of the family (so the frame-and-positivity route covers it)',
    is_zero_mat(Gctl(Wsym) - G_family(Rot2, Rot2 * Jp)(Wsym)), 'identity')

# =====================================================================================================================
section('C9  orientation is a gate invariant (exact steps)')
A3 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'A{i}{j}', real=True))
B3 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'B{i}{j}', real=True))
chk('C9.hom', 'det homMap(a) = det a (symbolic 3x3)', sp.expand(homMap(A3).det() - A3.det()) == 0, 'identity')
chk('C9.mult', 'det(actC a (actT b w)) = det a det b det w (symbolic a, b, w)',
    sp.expand(actC(A3, actT(B3, Wsym)).det() - A3.det() * B3.det() * Wsym.det()) == 0, 'identity')
chk('C9.phiW', 'det phiW = -1', phiW.det() == -1, 'witness')
dprod = cnot(prodState(xs, ys)).det()
chk('C9.cnotprod', 'det cnot(prodState x y) = -(x0^2+x1^2)(1-x2^2)(1-y0^2)(y1^2+y2^2) (symbolic; each factor is >= 0 on '
    'the ball, so the determinant is <= 0)',
    sp.expand(dprod + (xs[0] ** 2 + xs[1] ** 2) * (1 - xs[2] ** 2) * (1 - ys[0] ** 2) * (ys[1] ** 2 + ys[2] ** 2)) == 0,
    'identity')
chk('C9.mrefl', 'M_refl\'s supplied locals at 13 give orient(reflY, I) = true, while det(actC reflY (actT I phiW)) = +1 > 0 '
    'is attained by no N-CLASS decomposition of cnot (whose images of products have det <= 0, C9.cnotprod)',
    REFLY.det() * I3.det() == -1 and actC(REFLY, actT(I3, phiW)).det() == 1, 'witness')

# =====================================================================================================================
section('C10 minimality countermodels (each satisfies the stated clauses and is NOT N-CLASS)')
Ghalf = G_family(I2 / 2, Jp / 2)
Gtwo = G_family(2 * I2, 2 * Jp)
chk('C10.inv', 'G(2I, 2J\') is the inverse of G(I/2, J\'/2) (C2.inverse with a = I/2, b = J\'/2: -(J\'/2)^-1 = 2J\')',
    is_zero_mat(Gtwo(Ghalf(Wsym)) - Wsym) and is_zero_mat(Ghalf(Gtwo(Wsym)) - Wsym), 'identity')
chk('C10.h.frame', 'G(I/2, J\'/2) satisfies the frame, relC and relT',
    frame_holds(Ghalf) and is_zero_mat(actC(NFLIP, Ghalf(actC(NFLIP, Wsym))) - actT(NFLIP, Ghalf(Wsym)))
    and is_zero_mat(actT(NFLIP, Ghalf(actT(NFLIP, Wsym))) - Ghalf(Wsym)), 'identity')
dec = Ghalf(prodState(xs, ys)) - (cnot(prodState(xs, ys)) / 2
                                  + ((1 + xs[2]) / 2 * prodState(z3, ys) + (1 - xs[2]) / 2 * prodState(mz3, list(NFLIP * sp.Matrix(ys)))) / 2)
chk('C10.h.posFwd', 'G(I/2, J\'/2)(prodState x y) = (1/2) cnot(prodState x y) + (1/2)(p_x prodState z3 y + q_x prodState '
    '(-z3) (nflip y)) (symbolic): a convex combination of maxCone members (landed cnot_prodState_mem_maxCone, '
    'prodState_mem_maxCone), so posFwd holds', is_zero_mat(dec), 'identity')
wv = pairVal(hom([-1, 0, 0]), [1, 1, 0, 0], Gtwo(prodState(xplus, z3)))
chk('C10.h.posInv', f'G(I/2, J\'/2)^-1 (prodState xplus z3) pairs to {wv} < 0 with hom(-1,0,0), (1,1,0,0) in L: posInv '
    'fails', wv < 0, 'witness')
e10 = sp.zeros(4, 4); e10[1, 0] = 1
chk('C10.h.notN', f'G(I/2, J\'/2) is not ipW-orthogonal: ipW(G e10, G e10) = {ipW(Ghalf(e10), Ghalf(e10))} != 1 = ipW(e10, e10)',
    ipW(Ghalf(e10), Ghalf(e10)) != ipW(e10, e10), 'witness')
Wsym2 = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'v{i}{j}', real=True))
chk('C10.orth', 'N-CLASS gates are ipW-orthogonal: cnot preserves ipW (symbolic) and homMap(A)^T homMap(A) = '
    'homMap(A^T A) (symbolic A), so actC A, actT A preserve ipW for orthogonal A',
    sp.expand(ipW(cnot(Wsym), cnot(Wsym2)) - ipW(Wsym, Wsym2)) == 0
    and sp.expand(homMap(A3).T * homMap(A3) - homMap(A3.T * A3)) == sp.zeros(4, 4), 'identity')
wv2 = pairVal(hom([-1, 0, 0]), [1, 1, 0, 0], Gtwo(prodState(xplus, z3)))
chk('C10.t.posFwd', f'G(2I, 2J\') fails posFwd at the same witness (value {wv2}); its posInv is G(I/2, J\'/2)\'s posFwd; '
    f'ipW(G e10, G e10) = {ipW(Gtwo(e10), Gtwo(e10))} != 1', wv2 < 0 and ipW(Gtwo(e10), Gtwo(e10)) != 1, 'witness')
chk('C10.id0', 'id with z = 0: the frame holds trivially (both corners are 0), the unit clause fails; id with z = z3: '
    'the frame FAILS at prodState(-z3, z3)',
    prodState([0, 0, 0], [0, 0, 0]) == prodState([0, 0, 0], [0, 0, 0])
    and prodState(mz3, z3) != prodState(mz3, mz3), 'witness')
chk('C10.idnotN', 'id is not N-CLASS: det(actC A (actT B phiW)) = -det A det B (symbolic; nonzero for orthogonal A, B), '
    'while id maps prodState x y to a table of rank 1 (symbolic x, y)',
    sp.expand(actC(A3, actT(B3, phiW)).det() + A3.det() * B3.det()) == 0 and prodState(xs, ys).rank() == 1, 'identity')
# improper control
dimp = sp.diag(1, 1, -1)
HM1 = homMap(dimp)
c_a, c_b, c_c = sp.symbols('ca cb cc_', real=True)
F1 = sp.zeros(4, 4); F1[0, 1] = 1; F1[1, 0] = 1
F2 = sp.zeros(4, 4); F2[0, 2] = 1; F2[2, 0] = 1
F3 = sp.zeros(4, 4); F3[1, 2] = -1; F3[2, 1] = 1


def G_imp(w):
    out = sp.zeros(4, 4)
    for mu in R4:
        row = w[mu, :].T
        if mu == 0:
            out += (HZ * row.T + HMZ * (HM1 * row).T) / 2
        elif mu == 3:
            out += (HZ * row.T - HMZ * (HM1 * row).T) / 2
        else:
            for i in range(2):
                Acoh = sp.Symbol(f'p{i}{mu}') * F1 + sp.Symbol(f'q{i}{mu}') * F2 + sp.Symbol(f'r{i}{mu}') * F3
                out += E[i + 1] * (Acoh * row).T
    return out


e13 = sp.zeros(4, 4); e13[1, 3] = 1
chk('C10.imp', 'improper control: controlled-(id, diag(1,1,-1)) with any coherence from its zero-set forms maps e1 (x) e3 '
    'to 0 (not injective)', is_zero_mat(G_imp(e13)), 'identity')
chk('C10.imp.cc', 'countercontrol: the proper family G(a, b) does NOT annihilate e1 (x) e3 for a = I, b = J\'',
    not is_zero_mat(G_family(I2, Jp)(e13)), 'countercontrol')

print()
fails = [c for c, k, ok in CHECKS if not ok]
print(f'd1b_classify: {len(CHECKS)} checks, {len(fails)} failed')
if not fails:
    print('VERDICT D1-EXACT-STEPS-HOLD: the normalized family, its bounds, the orthogonal-U step and the identification '
          'with actC(diag(a,1)) . cnot (or its reflY conjugate) are exact; relC selects the 8 diagonal patterns of '
          'actC D . cnot . actC D\'; orientation is read off det of product images; the four minimality countermodels '
          'satisfy their clauses and are not N-CLASS; M_refl\'s gate is cnot (N-CLASS) and its supplied locals are not a '
          'decomposition')
    sys.exit(0)
print('NO VERDICT: failed checks ' + ', '.join(fails))
sys.exit(1)
