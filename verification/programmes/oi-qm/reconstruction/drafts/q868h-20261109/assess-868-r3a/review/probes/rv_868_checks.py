"""Reviewer's independent exact checks for REVIEW-868 (does not import the writer's probe).

Generic objects only: 2x2 / 4x4 matrices, the kernel's own W 3 table conventions and the kernel's
signed-permutation `cnot` (OIBridge/CompositeDimension.lean at fd539e15, lines 741-775), re-typed
here.  No OI update rule, encoding, record law or mechanism is simulated.  Each check is a control
on a statement in ASSESS-868.md or in REVIEW-868.md.
"""
import itertools
import sympy as sp

R = []


def chk(name, ok, detail=""):
    ok = bool(ok)
    R.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + str(detail)) if detail else ""))


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
S = [I2, X, Y, Z]
kr = sp.kronecker_product


def tab(rho):
    """Kernel W 3 convention for states: w[mu][nu] = tr(rho s_mu (x) s_nu); w[0][0] = tr rho."""
    return sp.Matrix(4, 4, lambda m, n: sp.nsimplify(sp.simplify((rho * kr(S[m], S[n])).trace())))


def untab(w):
    return sum((w[m, n] * kr(S[m], S[n]) for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4


def pv(u, v, w):
    """Kernel pairVal (CompositeDimension.lean:164): sum_mu sum_nu u_mu w_mu_nu v_nu."""
    return sp.simplify((sp.Matrix(u).T * w * sp.Matrix(v))[0, 0])


def hat(a):
    return [1] + list(a)


# ---- kernel cnot (CompositeDimension.lean:741-758), re-typed --------------------------------
def sgn(m, n):
    return -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def kcnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def actT(diag3, w):
    """actT N for a diagonal one-copy map N = diag(diag3): acts on the target (second) index."""
    D = sp.diag(1, *diag3)
    return w * D  # w[mu][nu] -> w[mu][nu] * D[nu][nu]


CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# =============================================================================================
# R1. Lemma H on eball 3, each direction separately (symbolic).
t = sp.symbols('t', real=True)
v = sp.symbols('v1:4', real=True)
b = sp.symbols('b1:4', real=True)
vv = sum(x ** 2 for x in v)
bb = sum(x ** 2 for x in b)
vb = sum(v[i] * b[i] for i in range(3))
lag = sum((v[i] * b[j] - v[j] * b[i]) ** 2 for i in range(3) for j in range(i + 1, 3))
chk("R1a (<=) core: Lagrange identity |v|^2|b|^2 - (v.b)^2 = sum (v_i b_j - v_j b_i)^2, so v.b >= -|v||b|",
    sp.expand(vv * bb - vb ** 2 - lag) == 0)
nv = sp.sqrt(vv)
bstar = [-x / nv for x in v]
chk("R1b (=>) witness: b* = -v/|v| has |b*|^2 = 1 and t + v.b* = t - |v|",
    sp.simplify(sum(x ** 2 for x in bstar) - 1) == 0 and sp.simplify(t + sum(v[i] * bstar[i] for i in range(3)) - (t - nv)) == 0)
c = sp.symbols('c', real=True)
u = sp.symbols('u1:4', real=True)
nu = sp.sqrt(sum(x ** 2 for x in u))
chk("R1c effect reduction: e = c + u.x at x = -u/|u| equals c - |u| (so nonnegativity on the ball forces c >= |u|)",
    sp.simplify(c + sum(u[i] * (-u[i] / nu) for i in range(3)) - (c - nu)) == 0)

# =============================================================================================
# R2. The writer's quantum-matrix surrogate equals the kernel's table `cnot` (all 16 Pauli inputs),
#     and the K2-GUARD-1 chain is reproduced entrywise with the kernel's own tables.
ok = True
for m in range(4):
    for n in range(4):
        P = kr(S[m], S[n])
        if sp.simplify(kcnot(tab(P)) - tab(CN * P * CN)) != sp.zeros(4, 4):
            ok = False
chk("R2a kernel cnot (signed permutation) = table of quantum CNOT conjugation on all 16 Pauli products", ok)
xplus, z3 = [1, 0, 0], [0, 0, 1]
prod = sp.Matrix(4, 4, lambda m, n: hat(xplus)[m] * hat(z3)[n])
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
chk("R2b cnot(prodState xplus z3) = phiW (kernel cnot_prodState_xplus_z3)", kcnot(prod) == phiW)
chk("R2c actT reflY phiW = idW (kernel actT_reflY_phiW)", actT([1, -1, 1], phiW) == idW)
chk("R2d cnot idW = chainW (kernel cnot_idW)", kcnot(idW) == chainW)
sx = [sp.Rational(1, 2), -sp.Rational(1, 2), 0, 0]
sz = [sp.Rational(1, 2), 0, 0, -sp.Rational(1, 2)]
chk("R2e chain_value: pairVal(sharpVec(-e1), sharpVec(-e3), chainW) = -1/2; with hats (1,a),(1,b) it is -2",
    pv(sx, sz, chainW) == sp.Rational(-1, 2) and pv(hat([-1, 0, 0]), hat([0, 0, -1]), chainW) == -2)
herald = chainW * sp.Matrix(sz)
chk("R2f kernel orientation: toOp chainW (sharpVec -e3) = (0, 1, 0, 0), outside Lor (lor_toOp_of_maxCone's conclusion fails)",
    list(herald) == [0, 1, 0, 0])
nfl = kcnot(actT([1, -1, -1], kcnot(prod)))
chk("R2g kernel control: with nflip (det +1) in place of reflY the same pair of effects gives 0",
    pv(sx, sz, nfl) == 0)

# =============================================================================================
# R3. Non-self-dual case: octahedron body with Pauli (sharp-axis) tests.  Validity on the available
#     family does NOT imply that heralds stay in the cone over the octahedron.
w3 = sp.zeros(4, 4)
w3[0, 0] = 1
w3[1, 1] = 1  # <XX> = 1
w3[1, 2] = 1  # <XY> = 1
axes = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
vals = [pv(hat(p), hat(q), w3) for p in axes for q in axes]
chk("R3a table w3 (<XX> = <XY> = 1, rest 0) is nonnegative on all 36 Pauli product tests", min(vals) >= 0, sorted(set(vals)))
h = list((sp.Matrix(hat([1, 0, 0])).T * w3))
chk("R3b herald of w3 by the A-test +x is (1, 1, 1, 0)", h == [1, 1, 1, 0])
chk("R3c that herald is outside the cone over the octahedron (|v|_1 = 2 > t = 1) and outside Lor (|v|^2 = 2 > 1)",
    sum(abs(x) for x in h[1:]) > h[0] and sum(x ** 2 for x in h[1:]) > h[0] ** 2)
chk("R3d that herald is inside the dual cone of the Pauli tests (the cube: max |v_i| <= t)", max(abs(x) for x in h[1:]) <= h[0])
bneg = [-1 / sp.sqrt(2), -1 / sp.sqrt(2), 0]
chk("R3e w3 is outside maxCone(eball 3): pairVal((1,e1),(1,b)) = 1 - sqrt 2 < 0 for b = -(1,1,0)/sqrt2",
    sp.simplify(pv(hat([1, 0, 0]), hat(bneg), w3) - (1 - sp.sqrt(2))) == 0)
octv = axes
chk("R3f converse direction: every octahedron vertex lies in the cube cone (octahedron closure => Pauli validity)",
    all(max(abs(x) for x in p) <= 1 for p in octv))

# =============================================================================================
# R4. Node-10 correlators.  Non-quantumness does not depend on the unreported cross terms;
#     full-ball maxCone membership does.
A = (sp.eye(4) - kr(X, X)) + (sp.eye(4) - kr(Z, Z))
ev = A.eigenvals()
phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
chk("R4a (I-XX)+(I-ZZ) is PSD with one-dimensional kernel spanned by Phi+",
    min(ev) >= 0 and ev.get(0, 0) == 1 and A * phi == sp.zeros(4, 1), ev)
chk("R4b <Phi+|YY|Phi+> = -1, so every PSD unit-trace rho with <XX> = <ZZ> = 1 has <YY> = -1 (any completion)",
    sp.simplify((phi.T * kr(Y, Y) * phi)[0, 0]) == -1)
aa = sp.symbols('a1:4', real=True)
bs = sp.symbols('b1:4', real=True)
T = (sp.eye(4) + kr(X, X) + kr(Z, Z)) / 4
wT = tab(T)
hT = list(sp.Matrix(hat(aa)).T * wT)
chk("R4c zero completion T: herald by A-hat (1,a) is (1, a1, 0, a3), in Lor whenever |a| <= 1 (Lemma H (<=) gives T in maxCone)",
    [sp.simplify(x) for x in hT] == [1, aa[0], 0, aa[2]])
cc = sp.Rational(1, 2)
wTc = wT.copy()
wTc[1, 3] = cc  # add <XZ> = 1/2
valsc = [pv(hat(p), hat(q), wTc) for p in axes for q in axes]
ap = [1 / sp.sqrt(2), 0, 1 / sp.sqrt(2)]
chk("R4d completion with <XZ> = 1/2 keeps all 36 Pauli products >= 0 but leaves maxCone(eball 3) (value -1/4 at a=(1,0,1)/sqrt2, b=-a)",
    min(valsc) >= 0 and sp.simplify(pv(hat(ap), hat([-x for x in ap]), wTc) + sp.Rational(1, 4)) == 0)

# =============================================================================================
# R5. "J9 => M20; not <=": the PR box is not an M20 witness (it violates Tsirelson); a
#     zero-marginal NS law within |S| <= 2 sqrt 2 that is not quantum is.
pr = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): -1}
Spr = pr[0, 0] + pr[0, 1] + pr[1, 0] - pr[1, 1]
chk("R5a PR box: S = 4 > 2 sqrt 2, so it fails Tsirelson soundness and cannot witness M20 =/=> J9", Spr == 4 and Spr ** 2 > 8)
cw = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): sp.Rational(1, 2)}
probs_ok = all((1 + s * cw[k]) / 4 >= 0 for k in cw for s in (1, -1))
chsh = []
for signs in itertools.product((1, -1), repeat=4):
    if signs.count(-1) % 2 == 1:
        chsh.append(abs(sum(sg * cw[k] for sg, k in zip(signs, [(0, 0), (0, 1), (1, 0), (1, 1)]))))
chk("R5b law c = (1,1,1,1/2), zero marginals: p(ab|xy) = (1 + ab c_xy)/4 >= 0, NS, max over the 8 CHSH forms = 5/2 < 2 sqrt 2",
    probs_ok and max(chsh) == sp.Rational(5, 2) and max(chsh) ** 2 < 8, max(chsh))
# Non-quantumness (hand proof, recorded in the review): for +-1 observables ||A psi - B psi||^2 = 2 - 2<AB>;
# c00 = c01 = c10 = 1 give A0 psi = B0 psi = B1 psi... and A1 psi = B0 psi, hence <A1 B1> = 1.  Control of the identity:
th = sp.symbols('th', real=True)
psi = sp.Matrix([sp.cos(th), 0, 0, sp.sin(th)])
Aop, Bop = kr(X, I2), kr(I2, X)
lhs = sp.simplify(((Aop * psi - Bop * psi).T * (Aop * psi - Bop * psi))[0, 0])
rhs = sp.simplify(2 - 2 * (psi.T * Aop * Bop * psi)[0, 0])
chk("R5c control of the identity ||A psi - B psi||^2 = 2 - 2<AB> on a generic real family", sp.simplify(lhs - rhs) == 0)

# =============================================================================================
# R6. G7 re-derived: monomial maps, configuration-basis Lueders projections and partial trace keep
#     diagonal matrices diagonal (4-state carrier = 2 x 2 composite); control: Hadamard does not.
d4 = sp.symbols('p0:4', real=True)
Dg = sp.diag(*d4)
ph = sp.symbols('q0:4')
alld = True
for perm in itertools.permutations(range(4)):
    M = sp.zeros(4, 4)
    for i, j in enumerate(perm):
        M[i, j] = ph[i]
    out = sp.expand(M * Dg * M.H)
    alld &= all(out[i, j] == 0 for i in range(4) for j in range(4) if i != j)
proj_ok = all((sp.diag(*[1 if k == j else 0 for k in range(4)]) * Dg * sp.diag(*[1 if k == j else 0 for k in range(4)])).is_diagonal() for j in range(4))
ptr = sp.Matrix(2, 2, lambda i, j: sum(Dg[2 * i + k, 2 * j + k] for k in range(2)))
chk("R6a monomial Kraus maps, Lueders projections and partial trace keep diagonal matrices diagonal", alld and proj_ok and ptr.is_diagonal())
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
o = kr(H, I2) * sp.diag(1, 0, 0, 0) * kr(H, I2).T
chk("R6b control: a non-monomial operator creates an off-diagonal entry", any(o[i, j] != 0 for i in range(4) for j in range(4) if i != j))
# The same non-monomial operator is real, and the real (rebit) composite is not locally tomographic:
Hr = kr(H, H)
chk("R6c witness 'non-monomial operation =/=> local tomography': H (x) H is real and non-monomial, and (I + YY)/4, (I - YY)/4 "
    "agree on every real product effect", all(((kr(Y, Y)) * kr(P, Q)).trace() == 0 for P in [I2, X, Z] for Q in [I2, X, Z])
    and all(sum(1 for j in range(4) if Hr[i, j] != 0) > 1 for i in range(4)))

# R6d. Full-ball single-token states need a non-{0, pi} phase as well as a non-monomial operation:
#      real (orthogonal or monomial-real) operations keep a real symmetric rho real, where <Y> = 0;
#      the monomial phase S after the real non-monomial H reaches y+ (<Y> = 1).
r = sp.symbols('r0:3', real=True)
rho_r = sp.Matrix([[r[0], r[1]], [r[1], r[2]]])
Sph = sp.diag(1, sp.I)
yplus = Sph * H * sp.diag(1, 0) * H.T * Sph.H
chk("R6d real symmetric rho has <Y> = 0 (no y-component from real operations); S H |0><0| H S^dag has <Y> = 1",
    sp.simplify((rho_r * Y).trace()) == 0 and sp.simplify((yplus * Y).trace()) == 1)

print()
nf = sum(1 for _, k in R if not k)
print("checks: %d, failures: %d" % (len(R), nf))
