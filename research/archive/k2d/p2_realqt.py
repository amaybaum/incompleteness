"""P2 — real quantum theory (two rebits) as the countercontrol for local tomography in DIM-1, exact.

Preregistered decision rule.
  (a) The real two-rebit composite (body = real symmetric PSD 4x4 of trace 1, carrier Sym(4), dim 10) with the real
      CNOT, the rebit NOT N = Ad(X) and corner axis z (Bloch Z) satisfies, AS OPERATOR IDENTITIES ON ITS OWN CARRIER:
      the frame, relT, relC, the involution/flip/unit of IsNot, and the entangling image; and d = 2 (even).
  (b) Its product-test map q : Sym(4) -> W 2 (coordinates Tr((s_mu (x) s_nu) .), s in {I, X, Z}) has rank 9 with
      kernel span(Y(x)Y): LT fails.
  (c) PTQ (the gate descends to the product-test quotient) FAILS for the real CNOT: an exact pair rho, rho' of PSD
      states with equal product-test tables whose CNOT images have different tables.
  (d) Which reversible real gates satisfy PTQ: the normalizer of span(Y(x)Y) in O(4).  (Pre-run expectation
      recorded honestly: a first draft expected an entangling PTQ gate to exist; the first run refuted that draft,
      see the ledger probe log.)
Verdict text is generated from the checks: if (a),(b),(c) all PASS, real QT is a composite satisfying every DIM-1
hypothesis on its own carrier except LT/PTQ, with d = 2 contradicting DIM-1's conclusion, so the transfer premise is
load-bearing.
"""
import sys
import sympy as sp
from k2lib import *

B = [I2, SX, SZ]          # real symmetric 2x2 basis (rebit), index 0 unit, 1 = X, 2 = Z
YY = kron(SY, SY)
check('P2.0 Y(x)Y is real symmetric', YY == YY.T and all(sp.im(e) == 0 for e in YY))


def q(r):
    return sp.Matrix(3, 3, lambda m, v: sp.nsimplify((kron(B[m], B[v]) * r).trace()))


# (b) rank of q on Sym(4)
symbasis = []
for i in range(4):
    for j in range(i, 4):
        E = sp.zeros(4, 4)
        E[i, j] = 1
        E[j, i] = 1
        symbasis.append(E)
Q = sp.Matrix.hstack(*[vec(q(E)) for E in symbasis])
check('P2.1 dim Sym(4) = 10, rank q = 9 (LT fails)', len(symbasis) == 10 and Q.rank() == 9, Q.rank())
check('P2.2 q(Y(x)Y) = 0 (the locally invisible direction)', q(YY) == sp.zeros(3, 3))

# (a) rebit structure
def rb(x1, x2):
    return (I2 + x1 * SX + x2 * SZ) / 2
N = sp.diag(1, -1)  # Ad(X) on Bloch (x1 = X, x2 = Z)
check('P2.3 Ad(X) acts on rebit Bloch coordinates as diag(1,-1)',
      all(SX * rb(a, c) * SX == rb(*(N * sp.Matrix([a, c]))) for a, c in [(1, 0), (0, 1), (sp.Rational(3, 5), sp.Rational(4, 5))]))
# IsNot: unit z = (0,1); invol; preserves disk (isometry); flips z
z = sp.Matrix([0, 1])
check('P2.4 IsNot fields: unit, invol, isometry (preserves disk), flips', (z.T * z)[0] == 1 and N * N == sp.eye(2)
      and N.T * N == sp.eye(2) and N * z == -z)
C = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
corner = {0: rb(0, 1), 1: rb(0, -1)}
check('P2.5 frame: C (z_a (x) z_b) C^T = z_a (x) z_{a+b}',
      all(C * kron(corner[a], corner[b]) * C.T == kron(corner[a], corner[(a + b) % 2]) for a in (0, 1) for b in (0, 1)))
IX = kron(I2, SX)
XI = kron(SX, I2)
check('P2.6 relT as operator identity: (I(x)X) C (I(x)X) = C', IX * C * IX == C)
check('P2.7 relC as operator identity: (X(x)I) C (X(x)I) = (I(x)X) C', XI * C * XI == IX * C)
check('P2.8 C real orthogonal (Ad C preserves the real PSD body both ways)', C * C.T == sp.eye(4))
out = C * kron(rb(1, 0), rb(0, 1)) * C.T
phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
check('P2.9 entangling: C (|+><+| (x) |0><0|) C^T = |Phi+><Phi+| (rank 1, real)', out == phi * phi.T)
om = q(out)
check('P2.10 its product-test table has operator-Schmidt rank 3 > 1 (not a product)', om.rank() == 3, om)

# (c) PTQ fails for the real CNOT
rho = (sp.eye(4) / 4 + phi * phi.T) / 2
rho2 = rho + YY / 8
ok1, w1 = is_psd_exact(rho)
ok2, w2 = is_psd_exact(rho2)
check('P2.11 rho, rho\' are PSD, trace 1, real symmetric', ok1 and ok2 and rho.trace() == 1 and rho2.trace() == 1
      and rho == rho.T and rho2 == rho2.T, (w1, w2))
check('P2.12 q(rho) = q(rho\') (indistinguishable by every product test)', q(rho) == q(rho2))
d = q(C * rho2 * C.T) - q(C * rho * C.T)
check('P2.13 q(C rho\' C^T) != q(C rho C^T) (PTQ fails for the real CNOT)', d != sp.zeros(3, 3), d)
check('P2.14 C maps the invisible direction Y(x)Y to a visible one: q(C YY C^T) != 0', q(C * YY * C.T) != sp.zeros(3, 3),
      q(C * YY * C.T))

# (d) which reversible real gates satisfy PTQ?  Normalizer of span(Y(x)Y) in O(4): U YY U^T = +-YY.
#     Lie algebra: antisymmetric A with [A, YY] = 0 (the identity component).  Expect dim 2 = local so(2)+so(2).
Asyms = sp.symbols('A0:6')
A = sp.zeros(4, 4)
k = 0
for i in range(4):
    for j in range(i + 1, 4):
        A[i, j] = Asyms[k]
        A[j, i] = -Asyms[k]
        k += 1
sol = sp.solve(list(A * YY - YY * A), Asyms, dict=True)
free = set(Asyms) - set(sol[0].keys()) if sol else set(Asyms)
J = sp.Matrix([[0, 1], [-1, 0]])
loc = [kron(J, I2), kron(I2, J)]
Agen = A.subs(sol[0]) if sol else A
psim = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)
psip = sp.Matrix([0, 1, 1, 0]) / sp.sqrt(2)
span_ok = sp.Matrix.hstack(vec(loc[0]), vec(loc[1])).rank() == 2 and all(sp.simplify(L * YY - YY * L) == sp.zeros(4, 4) for L in loc)
check('P2.15 identity component of the PTQ normalizer: Lie algebra dim 2, spanned by local J(x)I, I(x)J',
      len(free) == 2 and span_ok, (len(free), Agen))
# component representatives: (reflections in the two YY-eigenspaces) x (eigenspace exchange Z(x)I)
D1 = sp.eye(4) - 2 * psim * psim.T          # reflection in E- fixing Phi+, flipping Psi-
D2 = sp.eye(4) - 2 * psip * psip.T          # reflection in E+ fixing Phi-, flipping Psi+
ZI = kron(SZ, I2)
reps = []
for r1 in (sp.eye(4), D1):
    for r2 in (sp.eye(4), D2):
        for r3 in (sp.eye(4), ZI):
            reps.append(sp.simplify(r1 * r2 * r3))
a0, a1, b0, b1 = sp.symbols('a0 a1 b0 b1', real=True)
allok = True
for R in reps:
    ok_norm = sp.simplify(R * R.T) == sp.eye(4) and (sp.simplify(R * YY * R.T - YY) == sp.zeros(4, 4) or
                                                     sp.simplify(R * YY * R.T + YY) == sp.zeros(4, 4))
    v = R * kron(sp.Matrix([a0, a1]), sp.Matrix([b0, b1]))
    det = sp.expand(v[0] * v[3] - v[1] * v[2])
    allok = allok and ok_norm and det == 0
check('P2.16 the 8 component representatives are orthogonal, normalize span(YY), and map every real product '
      'vector to a product vector (coefficient determinant identically 0): no PTQ-respecting entangling gate',
      allok)
print('VERDICT:', 'real QT satisfies frame, relT, relC, IsNot, two-sided positivity and entangling on its own carrier '
      'with d = 2 even; LT fails and PTQ fails for its CNOT; every PTQ-respecting reversible gate there is '
      'non-entangling (identity component local, written component count)'
      if all(c for _, c in CHECKS) else 'NOT RENDERED (a check failed)')
sys.exit(summary())
