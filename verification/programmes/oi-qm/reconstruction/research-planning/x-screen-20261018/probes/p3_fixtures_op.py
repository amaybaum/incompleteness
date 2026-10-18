#!/usr/bin/env python3
"""p3_fixtures_op.py -- exact certificates (SymPy; symbolic where a family is claimed).
Research only; decides no round.

Clauses screened on the common pair domain SEP <= K <= maxCone (closed convex):
  OP-ex   purification existence: every token state is the token-1 marginal of a pure (extreme) state of K.
  OP-un   purifier uniqueness: two pure states of K with equal token-1 marginal are related by a
          reversible local map id(x)g on token 2 that is an automorphism of K.
  PC      the native CNOT preserves K.
  MI      native premeasurement: CNOT(rho (x) |0><0|) lies in K for every token state rho.
Universal statements are written arguments [W] (stated in REPORT.md); this script checks the exact
certificates they cite.  A failed certificate voids the corresponding row.

Fixtures: K_B = SEP + R+ B (#820); K(Z_F) = (Q3 n Z_F*) + cone(Z_F) (#820, stage 6);
maxCone (= Q3 + Gamma(Q3) for two qubits, Stormer-Woronowicz [L]); SEP; classical diagonal;
positive control Q3; Gamma(Q3).
"""
import sympy as sp
from itertools import product, combinations

I = sp.I
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -I], [I, 0]]); Z = sp.diag(1, -1); I2 = sp.eye(2)
kr = sp.kronecker_product
def pt2(M):
    R = sp.zeros(4, 4)
    for a, b, c, d in product(range(2), repeat=4):
        R[2*a+d, 2*c+b] = M[2*a+b, 2*c+d]
    return R
def psd(M):
    n = M.shape[0]
    for k in range(1, n+1):
        for S in combinations(range(n), k):
            m = sp.simplify(M.extract(list(S), list(S)).det())
            if not (m.is_real and m >= 0): return False
    return True
def m1(M):
    return sp.simplify(sp.Matrix(2, 2, lambda a, c: sum(M[2*a+b, 2*c+b] for b in range(2))))
def m2(M):
    return sp.simplify(sp.Matrix(2, 2, lambda b, d: sum(M[2*a+b, 2*a+d] for a in range(2))))
res = []
def chk(name, c):
    res.append((name, bool(c))); print(('PASS ' if c else 'FAIL ') + name)

CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
s2 = sp.sqrt(2)
phi = sp.Matrix([1, 0, 0, 1])/s2; B = phi*phi.H

# ---------------- K(Z_F)
def e(s, t): return (sp.eye(4) + s*kr(X, Z) + t*kr(Y, Y) - s*t*kr(Z, X))/16
defs = {(s, t): e(s, t) for s in (1, -1) for t in (1, -1)}
img = {k: sp.simplify(CN*v*CN.T) for k, v in defs.items()}
perm = {k: [k2 for k2, v2 in defs.items() if img[k] == v2] for k in defs}
chk('ZF  CNOT permutes the four defects (=> CNOT preserves Z_F*, cone Z_F, Q3, hence K(Z_F)) [PC holds]',
    all(len(v) == 1 for v in perm.values()) and len({v[0] for v in perm.values()}) == 4)
z = {k: 4*v for k, v in defs.items()}
chk('ZF  each normalized defect z has eigenvalues {1/2:3, -1/2:1}', all(sp.Matrix(v).eigenvals() == {sp.Rational(1, 2): 3, sp.Rational(-1, 2): 1} for v in z.values()))
chk('ZF  each defect has both marginals I/2', all(m1(v) == I2/2 and m2(v) == I2/2 for v in z.values()))
chk('ZF  det z = -1/16 (so every congruence image Ad_{I(x)M} z has det |det M|^4 det z < 0: not PSD)',
    all(sp.simplify(v.det()) == sp.Rational(-1, 16) for v in z.values()))
chk('ZF  Gamma(z) is a rank-one PSD projector (defects are Gamma-images of entangled pure states)',
    all(sp.simplify(pt2(v)*pt2(v)) == sp.simplify(pt2(v)) and pt2(v).trace() == 1 and psd(pt2(v)) for v in z.values()))
a, b = sp.symbols('a b', positive=True)
chi = sp.Matrix([a, 0, 0, b]); C = chi*chi.T
pair_ok = all(sp.expand(16*(C*v).trace() - (a - t*b)**2) == 0 for (s, t), v in defs.items())
chk('ZF  chi_ab = a|00>+b|11> pairs with e_{s,t} as (a - t b)^2/16 >= 0: chi_ab in Q3 n Z_F*, all a,b>0', pair_ok)
F = (a**2 + b**2)*sp.eye(4) - C
chk('ZF  extremality certificate F=(a^2+b^2)I-chi chi^T: F chi = 0', sp.expand(F*chi) == sp.zeros(4, 1))
chk('ZF  F PSD (eigenvalues 0, a^2+b^2 x3)', sp.Matrix(F).eigenvals() == {0: 1, a**2 + b**2: 3})
tr_ok = all(sp.expand((F*v).trace() - ((a**2 + b**2)/2 + (a + t*b)**2/4)) == 0 for (s, t), v in z.items())
chk('ZF  Tr(F z_{s,t}) = (a^2+b^2)/2 + (a+tb)^2/4 > 0 (F in K(Z_F)*, strictly positive on defects)', tr_ok)
evG = sp.Matrix(pt2(C)).eigenvals()
chk('ZF  Gamma(chi chi^T) has eigenvalue -ab (entangled for all a,b>0)', -a*b in evG)
chk('ZF  marginal of chi_ab on token 1 is diag(a^2,b^2) [OP-ex witness family]', m1(C) == sp.diag(a**2, b**2))
Cphi = C.subs({a: 1, b: 1})/2
chk('ZF  Phi+ (a=b) is a pure state of K(Z_F) with marginals I/2', Cphi == B and m1(B) == I2/2)

# weak OP (relations only, no automorphism requirement): some reversible token-2 map g = Ad_u o T
# sends a defect to Phi+.  Gamma(z) is a maximally entangled projector psi psi^dag; with
# psi = (I (x) M) Phi+, M_{ba} = sqrt2 psi_{ab}, u = M^dag gives (I (x) u) psi = Phi+ up to phase.
zz = z[(1, 1)]; Gz = pt2(zz)
evecs = [v for val, mult, vs in Gz.eigenvects() if val == 1 for v in vs]
psi = sp.simplify(evecs[0] / sp.sqrt((evecs[0].H * evecs[0])[0]))
M = sp.Matrix(2, 2, lambda bb, aa: s2 * psi[2*aa + bb])
chk('WEAK Gamma(z_{1,1}) is a rank-one projector onto a maximally entangled psi (M unitary)', sp.simplify(M.H*M) == I2)
u_w = M.H
gz = sp.simplify(kr(I2, u_w) * Gz * kr(I2, u_w).H)
chk('WEAK OP-un relation holds in K(Z_F) at the I/2 pair: (id (x) Ad_u T) z_{1,1} = Phi+ exactly', gz == B)
gchi = sp.simplify(kr(I2, u_w) * pt2(C) * kr(I2, u_w).H)
chk('WEAK the relating map is not an automorphism: it sends chi_ab (in K(Z_F)) to a matrix with det < 0',
    sp.simplify(gchi.det() + (a*b)**4) == 0 and sp.simplify(pt2(C).det()) == -(a*b)**4)
chk('WEAK det(Gamma(chi_ab)) = -(ab)^4 is the full inertia certificate (one negative eigenvalue -ab)',
    sp.Matrix(pt2(C)).eigenvals() == {a**2: 1, b**2: 1, a*b: 1, -a*b: 1})

# ---------------- K_B
chk('KB  Bell generator B has marginals I/2 (the only non-product extreme ray)', m1(B) == I2/2 and m2(B) == I2/2)
Ssing = sp.Matrix([0, 1, -1, 0]); Wb = pt2(Ssing*Ssing.T/2 + sp.diag(1, 0, 0, 0))
chk('KB  W = Gamma(singlet + |00><00|) is block-positive by construction and Tr(W B) = 0', sp.simplify((Wb*B).trace()) == 0)
chiq = sp.Matrix([sp.Rational(1, 2), 0, 0, sp.sqrt(3)/2])
chk('KB  Tr(W chi chi^T) = 1/4 - sqrt(3)/4 < 0 for the QM purification of diag(1/4,3/4): excluded from K_B',
    sp.simplify((Wb*chiq*chiq.T).trace() - (sp.Rational(1, 4) - sp.sqrt(3)/4)) == 0)
pi = sp.Matrix([1, I])/s2; o = CN*kr(pi, sp.Matrix([1, 0])); Wn = pt2(sp.Matrix([0, 1, -I, 0])*sp.Matrix([0, 1, -I, 0]).H/2)
chk('KB  PC fails: CNOT((|0>+i|1>)|0>) pairs with the #820 separator W as -1/2', sp.simplify((Wn*o*o.H).trace()) == sp.Rational(-1, 2))

# ---------------- maxCone
SW = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
chk('MC  Gamma(Phi+) = SWAP/2 (a maxCone element outside Q3)', pt2(B) == SW/2 and not psd(SW/2))
Yc = CN*(SW/2)*CN.T
kets = [sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([1, 1])/s2, sp.Matrix([1, -1])/s2, sp.Matrix([1, I])/s2, sp.Matrix([1, -I])/s2]
neg = [(i, j, sp.simplify((Yc*kr(x*x.H, y*y.H)).trace())) for i, x in enumerate(kets) for j, y in enumerate(kets)]
negs = [n for n in neg if n[2] < 0]
chk('MC  PC fails: CNOT Gamma(Phi+) CNOT has a negative product pairing (exact witness)', len(negs) > 0)
if negs: print('     witness product (ket indices, pairing):', negs[0])
chk('MC  MI holds: CNOT(rho(x)|0><0|) is PSD for the |+i> input (Q3 <= maxCone)', psd(o*o.H))

# ---------------- Q3 / Gamma(Q3) controls
u = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])*sp.diag(1, I)
Cq = C.subs({a: 1, b: 2})/5
Cq2 = kr(I2, u)*Cq*kr(I2, u).H
chk('Q3  POS OP-un instance: chi and (I(x)u)chi have equal token-1 marginals, related by local Ad_u', m1(Cq) == m1(Cq2))
chk('Q3  POS PC and MI (unitary conjugation preserves PSD; CNOT|+0> = Phi+ PSD)', psd(CN*kr(kets[2]*kets[2].H, sp.diag(1, 0))*CN.T))
chk('GQ  Gamma(Q3) fails MI: CNOT(|+><+|(x)|0><0|) = B and Gamma(B) not PSD', not psd(pt2(CN*kr(kets[2]*kets[2].H, sp.diag(1, 0))*CN.T)))
# mutation: a 'defect' that is PSD must defeat the inertia certificate
zmut = (sp.eye(4) + kr(X, Z) + kr(Y, Y) + kr(Z, X))/4
chk('MUT a PSD sign pattern (+st) has det >= 0, so the inertia test can fail', sp.simplify(zmut.det()) >= 0)

nf = sum(1 for _, c in res if not c)
print('SUMMARY checks=%d failed=%d' % (len(res), nf))
print('VERDICT', 'CERTIFICATES-GREEN (see REPORT for the written arguments they support)' if nf == 0 else 'VOID')
