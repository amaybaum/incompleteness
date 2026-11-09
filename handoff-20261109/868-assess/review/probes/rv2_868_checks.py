"""Independent review of ASSESS-868 r2: exact generic checks (WIP / UNVERIFIED; reviewer probe).

Generic 2x2 / 4x4 / 3x3 matrices and generic correlation tables only. No OI update rule, encoding,
record law or mechanism is simulated or enumerated. Imports no earlier probe (writer's or r1 reviewer's).
The kernel gate flow `unit g t = 1 + (exp(i pi t) - 1) * (1 - g)/2` (SecondOrderCircuit.lean:356,
LiftAudit.lean:47 at fd539e15) is re-typed by hand for Fin 2, g = permMat swap = X.
Run: python3 -I rv2_868_checks.py

Table convention: w[k][l] = <s_k (x) s_l>, s = (I, X, Y, Z); effect a = (1, a)/2-direction, product value
ahat^T w bhat; herald of wing B by A-effect ahat is ahat^T w.

A  native form of Lemma H (dual of Pauli sharp effects = cube; octahedron in cube; w3)
B  the (1, 1, 1, 1/2) law: NS, CHSH 5/2, not quantum (Gram-matrix minors; TLM arcsine control); PR box
C  validity is not quantumness (node-10 table; Phi+ forced; swap)
D  scope of "J3 needs the phase (O1)": non-real operations without any phase gate reach y and x states
E  reconstruction of the writer's run-1 V4 failure (float vs Rational), expectations unchanged
"""
import itertools
import sympy as sp

R = sp.Rational
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
PAU = [I2, X, Y, Z]
kron = sp.kronecker_product
res = []

def chk(name, cond):
    res.append((name, bool(cond)))

def table(rho):
    return [[sp.nsimplify(sp.simplify((rho * kron(PAU[k], PAU[l])).trace())) for l in range(4)] for k in range(4)]

def herA(w, a):  # herald of wing B by A-effect direction a
    ah = [1] + list(a)
    return [sp.expand(sum(ah[k] * w[k][l] for k in range(4))) for l in range(4)]

def herB(w, b):  # herald of wing A by B-effect direction b
    bh = [1] + list(b)
    return [sp.expand(sum(w[k][l] * bh[l] for l in range(4))) for k in range(4)]

PAULI_DIRS = [tuple(s if j == i else 0 for j in range(3)) for i in range(3) for s in (1, -1)]
in_cube = lambda h: all(h[0] - abs(x) >= 0 for x in h[1:])
in_oct = lambda h: h[0] - sum(abs(x) for x in h[1:]) >= 0
in_lor = lambda h: h[0] >= 0 and h[0] ** 2 - sum(x * x for x in h[1:]) >= 0

# ---- A: native form ----
# A1 the dual of {(1, +-e_i)}: (t,v) with t + s v_i >= 0 for all i, s. Every cube vertex (1, +-1, +-1, +-1)
# is in it with exactly 3 tight effects (a facet-defining description of the cube); (1, 1 + 1/100, 0, 0) is not.
eff = [(1,) + d for d in PAULI_DIRS]
pair = lambda e, h: sum(e[k] * h[k] for k in range(4))
cube_verts = [(1,) + s for s in itertools.product((1, -1), repeat=3)]
chk('A1 cube vertices in dual of Pauli effects, 3 tight each',
    all(all(pair(e, h) >= 0 for e in eff) and sum(1 for e in eff if pair(e, h) == 0) == 3 for h in cube_verts))
chk('A1c control: (1, 101/100, 0, 0) outside the dual', not all(pair(e, (1, R(101, 100), 0, 0)) >= 0 for e in eff))
# A2 octahedron vertices (1, +-e_i) lie in the cube cone; the cube vertex (1,1,1,1) is outside the octahedron and Lor
chk('A2 octahedron inside cube (vertices)', all(in_cube((1,) + d) for d in PAULI_DIRS))
chk('A2c cube vertex outside octahedron and outside Lor', (not in_oct((1, 1, 1, 1))) and (not in_lor((1, 1, 1, 1))))
# A3 w3: zero marginals, <XX> = <XY> = 1. Heralds by all 12 one-wing Pauli effects (both wings) are in the cube
w3 = [[0] * 4 for _ in range(4)]; w3[0][0] = 1; w3[1][1] = 1; w3[1][2] = 1
hA = [herA(w3, d) for d in PAULI_DIRS]; hB = [herB(w3, d) for d in PAULI_DIRS]
chk('A3 w3: all 36 Pauli product values >= 0',
    all(sum(([1] + list(a))[k] * w3[k][l] * ([1] + list(b))[l] for k in range(4) for l in range(4)) >= 0
        for a in PAULI_DIRS for b in PAULI_DIRS))
chk('A3 w3: every Pauli herald on either wing is in the cube cone', all(in_cube(h) for h in hA + hB))
chk('A3 w3: +x herald = (1,1,1,0), outside octahedron and Lor',
    hA[0] == [1, 1, 1, 0] and not in_oct(hA[0]) and not in_lor(hA[0]))
# A3c w3 is not in maxCone(eball 3): a = +x, b = -(1,1,0)/sqrt2 gives 1 - sqrt2 < 0 (so validity on native
# tests is strictly weaker than full-ball validity here too)
b = (-1 / sp.sqrt(2), -1 / sp.sqrt(2), 0)
v = sp.simplify(sum(hA[0][l] * ([1] + list(b))[l] for l in range(4)))
chk('A3c w3 fails a full-ball product test (value 1 - sqrt2)', sp.simplify(v - (1 - sp.sqrt(2))) == 0 and v < 0)
# A4 self-dual control on eball: Phi+ table heralds (1, a1, -a2, a3) lie in Lor for |a| <= 1
phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2); wphi = table(phi * phi.H)
a1, a2, a3 = sp.symbols('a1 a2 a3', real=True)
hphi = herA(wphi, (a1, a2, a3))
chk('A4 control: Phi+ heralds = (1, a1, -a2, a3)', [sp.simplify(x) for x in hphi] == [1, a1, -a2, a3])

# ---- B: the (1,1,1,1/2) law ----
c = {(0, 0): sp.Integer(1), (0, 1): sp.Integer(1), (1, 0): sp.Integer(1), (1, 1): R(1, 2)}
p = lambda a, bb, xy: (1 + a * bb * c[xy]) / 4
chk('B1 p >= 0 and zero marginals both wings (NS)',
    all(p(a, bb, xy) >= 0 for xy in c for a in (1, -1) for bb in (1, -1))
    and all(sum(p(a, bb, xy) for bb in (1, -1)) == R(1, 2) for xy in c for a in (1, -1))
    and all(sum(p(a, bb, xy) for a in (1, -1)) == R(1, 2) for xy in c for bb in (1, -1)))
forms = [s for s in itertools.product((1, -1), repeat=4) if s[0] * s[1] * s[2] * s[3] == -1]
vals = [abs(s[0] * c[(0, 0)] + s[1] * c[(0, 1)] + s[2] * c[(1, 0)] + s[3] * c[(1, 1)]) for s in forms]
chk('B2 all 8 CHSH forms <= 5/2, max = 5/2 < 2 sqrt2', len(forms) == 8 and max(vals) == R(5, 2) and R(5, 2) < 2 * sp.sqrt(2))
# B3 not quantum (Tsirelson vector form: c_xy = u_x . v_y, Gram of (u0,u1,v0,v1) PSD). Two 3x3 principal minors:
q = sp.symbols('q', real=True); pp = sp.symbols('pp', real=True)
G = sp.Matrix([[1, pp, 1, 1], [pp, 1, 1, R(1, 2)], [1, 1, 1, q], [1, R(1, 2), q, 1]])
m1 = sp.factor(G.extract([0, 2, 3], [0, 2, 3]).det()); m2 = sp.factor(G.extract([1, 2, 3], [1, 2, 3]).det())
chk('B3 minors -(q-1)^2 and -(q-1/2)^2: no q makes both >= 0',
    sp.simplify(m1 + (q - 1) ** 2) == 0 and sp.simplify(m2 + (q - R(1, 2)) ** 2) == 0)
# B3c independent control (TLM arcsine): 3 asin(1) - asin(1/2) = 4pi/3 > pi; Tsirelson point (1/sqrt2) sits at pi
chk('B3c TLM: 4pi/3 > pi; Tsirelson point equals pi',
    sp.simplify(3 * sp.asin(1) - sp.asin(R(1, 2)) - 4 * sp.pi / 3) == 0
    and sp.simplify(4 * sp.asin(1 / sp.sqrt(2)) - sp.pi) == 0)
pr = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): -1}
chk('B4 PR box S = 4 > 2 sqrt2', pr[(0, 0)] + pr[(0, 1)] + pr[(1, 0)] - pr[(1, 1)] == 4)

# ---- C: validity is not quantumness ----
T = (kron(I2, I2) + kron(X, X) + kron(Z, Z)) / 4
wT = table(T); hT = herA(wT, (a1, a2, a3))
chk('C1 node-10 table: herald (1,a1,0,a3); 1 - a1^2 - a3^2 = (1-|a|^2) + a2^2',
    [sp.simplify(x) for x in hT] == [1, a1, 0, a3]
    and sp.expand((1 - a1 ** 2 - a3 ** 2) - ((1 - a1 ** 2 - a2 ** 2 - a3 ** 2) + a2 ** 2)) == 0)
chk('C1 eigenvalue -1/4', R(-1, 4) in T.eigenvals())
P = (kron(I2, I2) + kron(X, X)) * (kron(I2, I2) + kron(Z, Z)) / 4
chk('C2 <XX>=<ZZ>=1 forces the rank-1 projector Phi+ with <YY> = -1',
    P.rank() == 1 and sp.simplify(P - phi * phi.H) == sp.zeros(4, 4)
    and sp.simplify((P * kron(Y, Y)).trace()) == -1)
SW = sp.Matrix(4, 4, lambda r, cc: 1 if (r, cc) in {(0, 0), (1, 2), (2, 1), (3, 3)} else 0)
wS = table(SW); hS = herA(wS, (a1, a2, a3))
chk('C3 swap table = 2 I4 (heralds 2(1,a) in Lor), eigenvalue -1',
    [sp.simplify(x) for x in hS] == [2, 2 * a1, 2 * a2, 2 * a3] and -1 in SW.eigenvals())

# ---- D: scope of "J3 needs the phase (O1)" ----
def bloch(psi):
    rho = psi * psi.H
    return [sp.simplify((rho * s).trace()) for s in (X, Y, Z)]
t = sp.symbols('t', real=True)
unit = lambda g, tt: sp.eye(g.shape[0]) + (sp.exp(sp.pi * sp.I * tt) - 1) * (sp.eye(g.shape[0]) - g) / 2
U = sp.simplify(unit(X, R(1, 2)))
k0 = sp.Matrix([1, 0])
chk('D1 kernel gate flow unit(X,1/2): unitary, non-monomial, fixes (1,1), not diagonal',
    sp.simplify(U * U.H) == I2 and all(x != 0 for x in U) and sp.simplify(U * sp.Matrix([1, 1]) - sp.Matrix([1, 1])) == sp.zeros(2, 1))
chk('D1 unit(X,1/2) |0> has Bloch vector (0, -1, 0): a y-axis state with no phase gate', bloch(U * k0) == [0, -1, 0])
chk('D1 general t: <Y> = -sin(pi t), <X> = 0',
    [sp.simplify(sp.expand_complex(x)) for x in bloch(sp.simplify(unit(X, t)) * k0)][:2] == [0, -sp.sin(sp.pi * t)])
# D1c countercontrols: real non-monomial H keeps <Y> = 0; the quarter phase moves the all-ones ray, the flow does not
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2); Sg = sp.diag(1, sp.I)
chk('D1c real H|0>: <Y> = 0; S(1,1) = (1,i) not parallel to (1,1)',
    bloch(H * k0)[1] == 0 and sp.Matrix.hstack(Sg * sp.Matrix([1, 1]), sp.Matrix([1, 1])).rank() == 2)
# D2 phase-free richness (GR:250-258): drives exp(-i s X_ab) and exchanges only, on three states a=|00>, b=|10>,
# c=|11> of the 4-state level (index = 2*first + second). From |10>: drive(a,b,pi/4), drive(b,c,pi/2), exchange(b,c)
# gives x+ (x) z+ up to global phase. No phase gate is used.
def drive_exact(i, j, s, n=4):
    M = sp.eye(n); M[i, i] = sp.cos(s); M[j, j] = sp.cos(s); M[i, j] = -sp.I * sp.sin(s); M[j, i] = -sp.I * sp.sin(s)
    return M
def exch(i, j, n=4):
    M = sp.eye(n); M[i, i] = 0; M[j, j] = 0; M[i, j] = 1; M[j, i] = 1
    return M
ia, ib, ic = 0, 2, 3
psi = sp.zeros(4, 1); psi[ib] = 1
psi = exch(ib, ic) * drive_exact(ib, ic, sp.pi / 2) * drive_exact(ia, ib, sp.pi / 4) * psi
target = kron(sp.Matrix([1, 1]) / sp.sqrt(2), sp.Matrix([1, 0]))
rho = psi * psi.H
chk('D2 drives + exchange (no phase gate) prepare x+ (x) z+ exactly', sp.simplify(rho - target * target.H) == sp.zeros(4, 4))
chk('D2c control: each drive is unitary and non-monomial on its pair',
    sp.simplify(drive_exact(ia, ib, sp.pi / 4) * drive_exact(ia, ib, sp.pi / 4).H) == sp.eye(4))

# ---- E: the writer's run-1 V4 failure ----
cf = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 1 / 2}  # Python ints and a float, as run 1 is described
ns_f = all(sum((1 + a * bb * cf[xy]) / 4 for bb in (1, -1)) == R(1, 2) for xy in cf for a in (1, -1))
chsh_f = max(abs(s[0] * cf[(0, 0)] + s[1] * cf[(0, 1)] + s[2] * cf[(1, 0)] + s[3] * cf[(1, 1)]) for s in forms)
chk('E1 float coefficients: same numbers (0.5, 2.5) but strict sympy comparisons fail',
    chsh_f == 2.5 and (not ns_f) and (chsh_f == R(5, 2)) is False)
chk('E1c exact coefficients: the same comparisons hold', max(vals) == R(5, 2))

for n, ok_ in res:
    print(('PASS ' if ok_ else 'FAIL ') + n)
print('%d checks, %d failures' % (len(res), sum(1 for _, o in res if not o)))
raise SystemExit(0 if all(o for _, o in res) else 1)
