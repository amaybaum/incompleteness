"""K2C P3 -- the reflection corollary and its neighbours, exact, in DIM-1 coordinates.

Decision rule (fixed before running):
  COROLLARY-ALGEBRA-EXACT iff (3.1) actT/actC are monoid homomorphisms (literal kernel definitions, symbolic maps),
  (3.2) for every S in O(3) with det S = -1 (S = -R(q), symbolic q) the map A := reflY S^T is in SO(3) and
  actT reflY = actT A . actT S, and (3.3) the landed chain value -1/2 is reproduced by this independent code.
  Items 3.4-3.8 are recorded facts with their own PASS/FAIL; they do not gate the corollary verdict but each is a
  separate finding (control-copy chain; global transpose; contracted reflections; T_refl; cnot').
Kernel-only layer: 3.1-3.5, 3.6a, 3.7a-c, 3.8a-c use only kernel definitions. Matrix-model layer [M]: 3.6b (Choi), 3.8d.

Usage: python -I p3_reflection.py <CompositeDimension.lean> <K2Guard.lean>
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k2clib import *  # noqa

CD, KG = sys.argv[1], sys.argv[2]
tabs = parse_tables(CD)
reflY = parse_diag_map(KG, 'reflY')
nflip = parse_diag_map(CD, 'nflip')
K = cnot_mat(tabs)
om = omega_symbols()
cn = lambda w: cnot_fun(tabs, w)
xplus, z3 = (1, 0, 0), (0, 0, 1)
p0 = prod_W(xplus, z3)
eX, eZ = sharpVec((-1, 0, 0)), sharpVec((0, 0, -1))
val = lambda w: pairval(eX, eZ, w)   # prodEffVal (sharpEff ![-1,0,0]) (sharpEff ![0,0,-1]) w

# 3.1 homomorphism (literal definitions)
A = sp.Matrix(3, 3, lambda i, j: sp.Symbol('A%d%d' % (i, j), real=True))
B = sp.Matrix(3, 3, lambda i, j: sp.Symbol('B%d%d' % (i, j), real=True))
v = sp.symbols('v0:4', real=True)
check('3.1a homMap A (homMap B v) = homMap (A.B) v', sp.expand(homMap_fun(A, list(homMap_fun(B, v))) - homMap_fun(A * B, v)) == sp.zeros(4, 1))
check('3.1b actT A (actT B w) = actT (A.B) w', sp.expand(actT_fun(A, actT_fun(B, om)) - actT_fun(A * B, om)) == sp.zeros(4, 4))
check('3.1c actC A (actC B w) = actC (A.B) w', sp.expand(actC_fun(A, actC_fun(B, om)) - actC_fun(A * B, om)) == sp.zeros(4, 4))
check('3.1d actT A (actC B w) = actC B (actT A w)', sp.expand(actT_fun(A, actC_fun(B, om)) - actC_fun(B, actT_fun(A, om))) == sp.zeros(4, 4))
check('3.1e actT id = id, actC id = id', actT_fun(sp.eye(3), om) == om and actC_fun(sp.eye(3), om) == om)

# 3.2 decomposition of an orientation-reversing orthogonal map
qs = sp.symbols('q0:4', real=True)
R = quat_R(qs)
S = -R
Aq = reflY * S.T
check('3.2a S = -R(q): S^T S = I, det S = -1', sp.simplify(S.T * S - sp.eye(3)) == sp.zeros(3, 3) and sp.simplify(S.det() + 1) == 0)
check('3.2b A := reflY S^T: A^T A = I, det A = 1', sp.simplify(Aq.T * Aq - sp.eye(3)) == sp.zeros(3, 3) and sp.simplify(Aq.det() - 1) == 0)
check('3.2c A . S = reflY', sp.simplify(Aq * S - reflY) == sp.zeros(3, 3))
check('3.2d actT reflY w = actT A (actT S w)  (symbolic q, w)', sp.simplify(actT_fun(Aq, actT_fun(S, om)) - actT_fun(reflY, om)) == sp.zeros(4, 4))
check('3.2e actC reflY w = actC A (actC S w)', sp.simplify(actC_fun(Aq, actC_fun(S, om)) - actC_fun(reflY, om)) == sp.zeros(4, 4))

# 3.3 landed chain, independent code
chainW = cn(actT_fun(reflY, cn(p0)))
check('3.3a cnot (actT reflY (cnot (prodState xplus z3))) = chainW (K2Guard.lean:104)',
      chainW == sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]))
check('3.3b value on sharpEff(-e1) (x) sharpEff(-e3) = -1/2', val(chainW) == sp.Rational(-1, 2), val(chainW))
check('3.3c control: with nflip the value is 0', val(cn(actT_fun(nflip, cn(p0)))) == 0)

# 3.4 the control-copy reflection: the same chain
chainC = cn(actC_fun(reflY, cn(p0)))
check('3.4 cnot (actC reflY (cnot (prodState xplus z3))) = chainW, value -1/2  (control-copy obstruction)',
      chainC == chainW and val(chainC) == sp.Rational(-1, 2))

# 3.5 global transpose (both copies reflected): chain returns to the product
tauf = lambda w: actC_fun(reflY, actT_fun(reflY, w))
check('3.5a cnot (tau (cnot p0)) = p0  (tau = actC reflY . actT reflY)', cn(tauf(cn(p0))) == p0)
check('3.5b tau commutes with cnot (symbolic w)', sp.expand(cn(tauf(om)) - tauf(cn(om))) == sp.zeros(4, 4))

# 3.6 contracted reflections D_c = c reflY (ball maps, not reversible for |c| < 1)
c = sp.Symbol('c', real=True)
Dc = c * reflY
vc = sp.expand(val(cn(actT_fun(Dc, cn(p0)))))
check('3.6a chain value with actT (c reflY) = (1 - 3c)/4  (negative iff c > 1/3)', sp.expand(vc - (1 - 3 * c) / 4) == 0, vc)
lam = sp.Symbol('lam')
choi = rho_of(actT_fun(Dc, cn(p0)))       # (id (x) Lambda_c)(Phi+) in the matrix model
cp = sp.factor(choi.charpoly(lam).as_expr())
check('3.6b [M] Choi state of the qubit map of c reflY has spectrum {(1+c)/4 x3, (1-3c)/4}  (CP iff -1 <= c <= 1/3)',
      sp.expand(choi.charpoly(lam).as_expr() - (lam - (1 + c) / 4) ** 3 * (lam - (1 - 3 * c) / 4)) == 0, cp)
d = sp.symbols('d1:4', real=True)
Dd = sp.diag(*d)
vd = sp.expand(val(cn(actT_fun(Dd, cn(p0)))))
choid = rho_of(actT_fun(Dd, cn(p0)))
evs = sorted([sp.expand(e) for e in choid.eigenvals().keys()], key=str)
print('3.6c chain value with actT diag(d1,d2,d3) =', vd, ' ; Choi eigenvalues =', evs)
check('3.6c the chain value equals one Choi eigenvalue of diag(d1,d2,d3) (the chain is a Choi-eigenvector test)',
      any(sp.expand(vd - e) == 0 for e in evs))

# 3.7 the native gate T_refl := actT reflY . cnot
Tr_ = lambda w: actT_fun(reflY, cn(w))
corner = lambda a: [z3, tuple(-t for t in z3)][a]
frame = all(Tr_(prod_W(corner(a), corner(bb))) == prod_W(corner(a), corner((a + bb) % 2)) for a in range(2) for bb in range(2))
check('3.7a T_refl frame on the four corners', frame)
check('3.7b T_refl relT: actT nflip (T (actT nflip w)) = T w', sp.expand(actT_fun(nflip, Tr_(actT_fun(nflip, om))) - Tr_(om)) == sp.zeros(4, 4))
check('3.7c T_refl relC: actC nflip (T (actC nflip w)) = actT nflip (T w)',
      sp.expand(actC_fun(nflip, Tr_(actC_fun(nflip, om))) - actT_fun(nflip, Tr_(om))) == sp.zeros(4, 4))
a_ = sp.symbols('a0:4', real=True)
b_ = sp.symbols('b0:4', real=True)
check('3.7d pairVal a b (actT N w) = pairVal a (H(N)^T b) w  (actT of a ball automorphism preserves maxCone [W])',
      sp.expand(pairval(a_, b_, actT_fun(A, om)) - pairval(a_, list(Hmat(A).T * sp.Matrix(b_)), om)) == 0)
check('3.7e T_refl (T_refl p0) has value -1/2: no candidate cone is invariant under T_refl alone',
      val(Tr_(Tr_(p0))) == sp.Rational(-1, 2), val(Tr_(Tr_(p0))))

# 3.8 the conjugated gate cnot' := actT reflY . cnot . actT reflY
cp_ = lambda w: actT_fun(reflY, cn(actT_fun(reflY, w)))
check("3.8a cnot' frame", all(cp_(prod_W(corner(a), corner(bb))) == prod_W(corner(a), corner((a + bb) % 2)) for a in range(2) for bb in range(2)))
check("3.8b cnot' relT and relC",
      sp.expand(actT_fun(nflip, cp_(actT_fun(nflip, om))) - cp_(om)) == sp.zeros(4, 4)
      and sp.expand(actC_fun(nflip, cp_(actC_fun(nflip, om))) - actT_fun(nflip, cp_(om))) == sp.zeros(4, 4))
check("3.8c cnot' != cnot (symbolic w) and cnot' p0 = idW", sp.expand(cp_(om) - cn(om)) != sp.zeros(4, 4) and cp_(p0) == sp.eye(4))
Rp = reflY * R * reflY
check("3.8d reflY R(q) reflY = R(q0,-q1,q2,-q3) in SO(3)  (so actT reflY '' Q3 is invariant under cnot' and local SO(3))",
      sp.simplify(Rp - quat_R((qs[0], -qs[1], qs[2], -qs[3]))) == sp.zeros(3, 3))

nf = summary()
core = all(cnd for nm, cnd in CHECKS if nm.split(' ')[0] in ('3.1a', '3.1b', '3.1c', '3.1d', '3.1e', '3.2a', '3.2b', '3.2c', '3.2d', '3.2e', '3.3a', '3.3b', '3.3c'))
print('VERDICT P3:', 'COROLLARY-ALGEBRA-EXACT' if core else 'NOT RENDERED')
sys.exit(nf)
