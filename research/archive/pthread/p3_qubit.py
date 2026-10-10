"""P3: the reverse direction on finite QM (qubit), exact (sympy rationals / symbols, no floats).

  Q1  Bloch dictionary: tr(rho(r) P(n)) = 1/2 + n.r/2 = sharpEff n r, so the qubit body with its
      projective effects is eball 3 with the sharp directional effects (EFF-1's objects).
  Q2  Choi matrix of the identity channel on M_2 (and M_3) has rank one: the mechanism of the kernel's
      PassiveObservation.passive_branch_scalar, so every passive CP readout is uninformative (NIWD),
      hence no passive readout separates (PI) and no record reconstructs (NRR).
  Q3  Measure-and-prepare along the computational basis is the dephasing map, not the identity
      (the record of the Z readout does not reconstruct |+>).
  Q4  Incompatibility: the joint element of sigma_z / sigma_x readouts forced by the marginal
      constraints is G11 = I/4 + (sigma_x + sigma_z)/4, which has the negative eigenvalue (1 - sqrt 2)/4.
  Q5  PBIN: for every effect E = a I + b.sigma and every Bloch vector w orthogonal to b, the pure states
      rho(w), rho(-w) are distinct and give E the same probability.
  Q6  Classical control (diagonal subalgebra = the classical bit): the pinching readout is passive on
      diagonal states and separates them (kernel PassiveObservation.pinching_passive_on_diagonal).
"""
import sympy as sp

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
r1, r2, r3, n1, n2, n3 = sp.symbols('r1 r2 r3 n1 n2 n3', real=True)


def rho(r):
    return (I2 + r[0] * sx + r[1] * sy + r[2] * sz) / 2


# Q1
lhs = sp.expand((rho((r1, r2, r3)) * rho((n1, n2, n3)) * 2).trace() / 2)
rhs = sp.Rational(1, 2) + (n1 * r1 + n2 * r2 + n3 * r3) / 2
chk("Q1 tr(rho(r) P(n)) = 1/2 + n.r/2 (sharpEff on eball 3)", sp.simplify(lhs - rhs) == 0)
chk("Q1 rho(r) has eigenvalues (1 +- |r|)/2: char poly", sp.expand((rho((r1, r2, r3)).charpoly().as_expr()) -
    sp.expand((sp.Symbol('lambda') - sp.Rational(1, 2)) ** 2 - (r1**2 + r2**2 + r3**2) / 4)) == 0)


# Q2
def choi_id(n):
    """Choi(id) = sum_ij E_ij (x) id(E_ij), built entrywise."""
    C = sp.zeros(n * n, n * n)
    for i in range(n):
        for j in range(n):
            # (E_ij (x) E_ij)[(i,a),(j,b)] = delta_{a i} delta_{b j}
            C[i * n + i, j * n + j] += 1
    return C


for n in (2, 3):
    C = choi_id(n)
    chk(f"Q2 Choi(id) on M_{n} has rank 1 (passive CP branches are scalar: kernel passive_branch_scalar)", C.rank() == 1)

# Q3
P0 = sp.Matrix([[1, 0], [0, 0]])
P1 = sp.Matrix([[0, 0], [0, 1]])
plus = rho((1, 0, 0))
mp = (plus * P0).trace() * P0 + (plus * P1).trace() * P1
chk("Q3 measure-and-prepare along Z sends |+><+| to I/2 (record does not reconstruct)", mp == I2 / 2 and mp != plus)

# Q4: forced joint element for e = P_z+ , f = P_x+ ; Bloch-affine g11 = 1/4 + (r1 + r3)/4  (P2 eball forcing)
G11 = I2 / 4 + (sx + sz) / 4
ev = G11.eigenvals()
chk("Q4 forced joint element has eigenvalues (1 +- sqrt 2)/4", set(ev.keys()) == {(1 - sp.sqrt(2)) / 4, (1 + sp.sqrt(2)) / 4})
chk("Q4 (1 - sqrt 2)/4 < 0 (sympy exact relational)", bool(((1 - sp.sqrt(2)) / 4) < 0))
# and G11 is indeed what the marginals force: tr(G11 rho(r)) = 1/4 + (r1 + r3)/4
chk("Q4 tr(G11 rho(r)) = 1/4 + (r1 + r3)/4",
    sp.simplify((G11 * rho((r1, r2, r3))).trace() - (sp.Rational(1, 4) + (r1 + r3) / 4)) == 0)

# Q5
a, b1, b2, b3 = sp.symbols('a b1 b2 b3', real=True)
E = a * I2 + b1 * sx + b2 * sy + b3 * sz
w = (b2, -b1, 0)  # orthogonal to b; normalisation irrelevant for the equality (affine in w), checked symbolically
pw = sp.expand((E * rho(w)).trace())
pmw = sp.expand((E * rho(tuple(-c for c in w))).trace())
chk("Q5 E gives rho(w) and rho(-w) the same probability for w orthogonal to b", sp.simplify(pw - pmw) == 0)
chk("Q5 (degenerate b1 = b2 = 0 handled by w = e1): equal probabilities",
    sp.simplify((E.subs({b1: 0, b2: 0}) * rho((1, 0, 0))).trace() - (E.subs({b1: 0, b2: 0}) * rho((-1, 0, 0))).trace()) == 0)

# Q6 classical control on the diagonal algebra
p = sp.symbols('p', real=True)
D = sp.diag(p, 1 - p)
br = [P0 * D * P0, P1 * D * P1]
chk("Q6 pinching readout is passive on diagonal states", sp.simplify(br[0] + br[1] - D) == sp.zeros(2, 2))
chk("Q6 pinching outcome law (p, 1-p) separates diagonal states", [sp.simplify(x.trace()) for x in br] == [p, 1 - p])

npass = sum(1 for _, c in checks if c)
print(f"{'ALL-PASS' if npass == len(checks) else 'SOME-FAIL'} {npass}/{len(checks)}")
