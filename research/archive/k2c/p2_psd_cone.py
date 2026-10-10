"""K2C P2 -- the positive witness: the PSD cone Q3 written in DIM-1 coordinates.

Q3 := { w in W 3 | S(w) is positive semidefinite },  S(w) := realify(rho(w)), an explicit real symmetric 8x8 matrix
whose entries are integer linear forms in w (divided by 4).  The predicate uses no complex number; the CHOICE of S is
taken from the matrix model [M].

Decision rule (fixed before running): POSITIVE-WITNESS-EXACT iff
  (i)  the realification identity, the congruence identities for cnot, actT R(q), actC R(q) (symbolic q in R^4 \\ 0)
       and the global transpose hold as exact polynomial identities;
  (ii) the instance checks (products in Q3, Q3 inside maxCone, strictness witnesses) all hold exactly;
  (iii) the countercontrol holds: the one-copy reflection actT reflY maps the Q3 point phiW outside Q3.
Steps that are literature-standard and NOT computed here are listed as [L] in the ledger (Kronecker of PSD is PSD;
Tr(PQ) >= 0 for PSD P, Q; realify preserves/reflects PSD; Euler-Rodrigues surjectivity SU(2) -> SO(3)).

Usage: python -I p2_psd_cone.py <CompositeDimension.lean> <K2Guard.lean>
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k2clib import *  # noqa

CD, KG = sys.argv[1], sys.argv[2]
tabs = parse_tables(CD)
reflY = parse_diag_map(KG, 'reflY')
K = cnot_mat(tabs)
om = omega_symbols()
S = S_of(om)

# 2.1 realification
u = sp.symbols('u0:4', real=True)
wv = sp.symbols('v0:4', real=True)
vc = sp.Matrix([u[i] + sp.I * wv[i] for i in range(4)])
uw = sp.Matrix(list(u) + list(wv))
lhs = sp.expand((vc.H * rho_of(om) * vc)[0, 0])
rhs = sp.expand((uw.T * S * uw)[0, 0])
check('2.1a v^H rho(w) v = [u;v]^T S(w) [u;v]  (symbolic in w, u, v)', sp.expand(lhs - rhs) == 0)
check('2.1b S(w) symmetric with real entries linear in w', S == S.T and all(sp.im(e) == 0 for e in S))
print('4*S(w) =')
for i in range(8):
    print('   ', [sp.expand(4 * S[i, j]) for j in range(8)])

# 2.2 products
x = sp.symbols('x1:4', real=True)
y = sp.symbols('y1:4', real=True)
lam = sp.Symbol('lam')
rx = (I2 + x[0] * SX + x[1] * SY + x[2] * SZ) / 2
check('2.2a charpoly rho(x) = lam^2 - lam + (1 - |x|^2)/4  [so rho(x) >= 0 iff |x| <= 1]',
      sp.expand(rx.charpoly(lam).as_expr() - (lam ** 2 - lam + (1 - x[0] ** 2 - x[1] ** 2 - x[2] ** 2) / 4)) == 0)
pts = [(0, 0, 0), (1, 0, 0), (0, 0, 1), (0, 0, -1), (sp.Rational(3, 5), 0, sp.Rational(4, 5)),
       (sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(-2, 3)), (sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(1, 2))]
ok = True
for p in pts:
    for r in pts:
        good, wit = is_psd_exact(S_of(prod_W(p, r)))
        ok = ok and good
check('2.2b S(prodState x y) PSD (exact principal minors) on 49 rational pairs incl. sphere points', ok)

# 2.3 Q3 inside maxCone: instance checks (the general step is [L]: Tr((E (x) F) rho) >= 0)
import random
rnd = random.Random(20261006)


def rand_gauss():
    return sp.Rational(rnd.randint(-5, 5), rnd.randint(1, 4)) + sp.I * sp.Rational(rnd.randint(-5, 5), rnd.randint(1, 4))


def rand_lor():
    v = [sp.Rational(rnd.randint(-6, 6), rnd.randint(1, 5)) for _ in range(3)]
    a0 = sp.sqrt(sum(t ** 2 for t in v))
    a0 = sp.ceiling(a0) if a0.is_irrational else a0
    return [a0] + v


ok = True
for _ in range(40):
    vs = [sp.Matrix([rand_gauss() for _ in range(4)]) for _ in range(rnd.randint(1, 3))]
    rho = sum((v * v.H for v in vs), sp.zeros(4, 4))
    w = q_of(rho)
    a, b = rand_lor(), rand_lor()
    ok = ok and pairval(a, b, w) >= 0
check('2.3 pairVal a b w >= 0 for 40 random rational PSD rho and Lor a, b (instances only)', ok)

# 2.4 invariance by congruence (symbolic)
CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
Oc = realify(CN)
Scn = S_of(unvec(K * vec(om)))
check('2.4a S(cnot w) = O_C S(w) O_C^T, O_C = realify(CNOT) a permutation matrix', sp.expand(Scn - Oc * S * Oc.T) == sp.zeros(8, 8))
qs = sp.symbols('q0:4', real=True)
n = sum(t ** 2 for t in qs)
R = quat_R(qs)
U = quat_U(qs)
OT = realify(kron(I2, U))
OC = realify(kron(U, I2))
ST = S_of(unvec(actT_mat(R) * vec(om)))
SC = S_of(unvec(actC_mat(R) * vec(om)))
check('2.4b |q|^2 S(actT R(q) w) = O_q S(w) O_q^T, O_q = realify(I (x) U~)  (polynomial identity in q, w)',
      sp.simplify(sp.expand(n * ST - OT * S * OT.T)) == sp.zeros(8, 8))
check('2.4c |q|^2 S(actC R(q) w) = O_q S(w) O_q^T, O_q = realify(U~ (x) I)',
      sp.simplify(sp.expand(n * SC - OC * S * OC.T)) == sp.zeros(8, 8))
J = sp.diag(1, 1, 1, 1, -1, -1, -1, -1)
Stau = S_of(unvec(actC_mat(reflY) * actT_mat(reflY) * vec(om)))
check('2.4d S(actC reflY (actT reflY w)) = J S(w) J, J = diag(I,-I)  (global transpose preserves Q3)',
      sp.expand(Stau - J * S * J) == sp.zeros(8, 8))
check('2.4e O_q^T O_q = |q|^2 I (O_q invertible for q != 0)', sp.expand(OT.T * OT - n * sp.eye(8)) == sp.zeros(8, 8))
tau = actC_mat(reflY) * actT_mat(reflY)
check('2.4f the global transpose commutes with cnot', tau * K == K * tau)

# 2.5 countercontrol: one-copy reflection
phiW = unvec(K * vec(prod_W((1, 0, 0), (0, 0, 1))))
check('2.5a cnot (prodState xplus z3) = phiW = diag(1,1,-1,1)', phiW == sp.diag(1, 1, -1, 1))
good, _ = is_psd_exact(S_of(phiW))
check('2.5b phiW in Q3 (exact principal minors)', good)
idW = actT_fun(reflY, phiW)
check('2.5c actT reflY phiW = idW = identity table', idW == sp.eye(4))
sing = sp.Matrix([0, 1, -1, 0])
val = (sing.H * rho_of(idW) * sing)[0, 0] / (sing.H * sing)[0, 0]
check('2.5d idW not in Q3: singlet expectation of rho(idW) = -1/2', val == sp.Rational(-1, 2), val)
check('2.5e actC reflY phiW = idW as well (the control-copy reflection gives the same point)', actC_fun(reflY, phiW) == sp.eye(4))

# 2.6 strictness: SEP < Q3 < maxCone
f = lambda w: w[0, 0] - w[1, 1] + w[2, 2] - w[3, 3]
fx = sp.expand(f(prod_W(x, y)))
check('2.6a f(prodState x y) = 1 - x . reflY(y)  (>= 0 on the ball by Cauchy-Schwarz [W])',
      sp.expand(fx - (1 - (x[0] * y[0] - x[1] * y[1] + x[2] * y[2]))) == 0)
check('2.6b f(phiW) = -2  (phiW in Q3, not in the separable cone)', f(phiW) == -2)
a = sp.symbols('a0:4', real=True)
b = sp.symbols('b0:4', real=True)
check('2.6c pairVal a b idW = a0 b0 + a.b  (>= 0 for Lor a, b by Cauchy-Schwarz [W]: idW in maxCone)',
      sp.expand(pairval(a, b, idW) - sum(a[i] * b[i] for i in range(4))) == 0)

# 2.7 duality bookkeeping: the Euclidean pairing of W is 4 x Hilbert-Schmidt
xi = sp.Matrix(4, 4, lambda m, v: sp.Symbol('k%d%d' % (m, v), real=True))
check('2.7 sum_{mu nu} w xi = 4 Tr(rho(w) rho(xi))  (so Q3 is self-dual for the W pairing [L: PSD self-dual])',
      sp.expand(sum(om[i, j] * xi[i, j] for i in range(4) for j in range(4)) - 4 * (rho_of(om) * rho_of(xi)).trace()) == 0)

nf = summary()
print('VERDICT P2:', 'POSITIVE-WITNESS-EXACT' if nf == 0 else 'NOT RENDERED')
sys.exit(nf)
