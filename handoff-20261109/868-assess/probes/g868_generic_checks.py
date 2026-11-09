"""Exact generic checks for ASSESS-868 (paper-only re-assessment of Issue #868).

Scope: standard two-qubit / two-rebit matrix algebra over exact numbers (sympy).
These are generic mathematical objects. No OI mechanism, update rule, encoding
or record law is simulated or enumerated here. Each check is a control on a
statement made in ASSESS-868.md; none is evidence for a physical result.

Table convention (matches OIBridge/CompositeDimension.lean, W 3 and pairVal):
  table w[mu][nu] = tr(M sigma_mu (x) sigma_nu), mu, nu in {0,1,2,3}
  pairVal(a, b, w) = sum_mu,nu ahat[mu] w[mu][nu] bhat[nu], ahat = (1, a1, a2, a3)
So pairVal(a, b, table(rho)) = 4 tr(rho P_a (x) P_b) for Bloch effects P_a=(I+a.s)/2,
so the value of a product of sharp effects is pairVal / 4.
"""
import sympy as sp

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
PAULI = [I2, X, Y, Z]
kron = sp.kronecker_product

results = []


def check(name, cond, detail=""):
    ok = bool(cond)
    results.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""))


def table(M):
    return sp.Matrix(4, 4, lambda m, n: sp.simplify((M * kron(PAULI[m], PAULI[n])).trace()))


def pairval(a, b, w):
    ah = sp.Matrix([1] + list(a))
    bh = sp.Matrix([1] + list(b))
    return sp.simplify((ah.T * w * bh)[0, 0])


def eigs(M):
    return sorted([sp.nsimplify(sp.simplify(e)) for e, k in M.eigenvals().items() for _ in range(k)],
                  key=lambda v: float(v))


CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
plus = sp.Matrix([1, 1]) / sp.sqrt(2)
zero = sp.Matrix([1, 0])
rho_plus = plus * plus.T
rho_zero = zero * zero.T


def ptranspose2(M):
    """Partial transpose on the second qubit."""
    out = sp.zeros(4, 4)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    out[2 * i + l, 2 * j + k] = M[2 * i + k, 2 * j + l]
    return out


# ---------------------------------------------------------------------------
# G1. Product-test validity (block positivity, "maxCone") does not select PSD.
#     The swap operator F is positive on every product of Bloch effects but has
#     eigenvalue -1.  (Control for the claim that A2-A4 are satisfied by QM and
#     by non-quantum cones alike; column (iii) does not discriminate.)
F = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
wF = table(F)
a = sp.symbols('a1:4', real=True)
b = sp.symbols('b1:4', real=True)
pvF = sp.expand(pairval(a, b, wF))
check("G1a swap table pairVal = 2(1 + a.b)", sp.simplify(pvF - 2 * (1 + a[0] * b[0] + a[1] * b[1] + a[2] * b[2])) == 0,
      str(pvF))
check("G1b swap has eigenvalue -1 (not PSD)", min(eigs(F)) == -1, str(eigs(F)))

# G2. CNOT invariance excludes the separable cone: CNOT(|+><+| (x) |0><0|) is
#     entangled (its partial transpose has eigenvalue -1/2).
rho1 = kron(rho_plus, rho_zero)
rho2 = CNOT * rho1 * CNOT.T
check("G2 CNOT image of the product (+,0) has PT eigenvalue -1/2",
      min(eigs(ptranspose2(rho2))) == sp.Rational(-1, 2), str(eigs(ptranspose2(rho2))))

# ---------------------------------------------------------------------------
# G3. The K2-GUARD-1 chain on standard matrices (stabilizer data only):
#     product (x+, z+) -> CNOT -> one-copy reflection Y -> -Y (= transpose on
#     qubit 2) -> CNOT; then the product of sharp effects along -e1 and -e3.
#     K2-GUARD-1 (kernel, on main) states the value -1/2.
# First confirm transpose acts on the Bloch vector as diag(1, -1, 1).
check("G3a transpose on one qubit acts as reflY = diag(1,-1,1)",
      X.T == X and Y.T == -Y and Z.T == Z)
rho3 = ptranspose2(rho2)
rho4 = CNOT * rho3 * CNOT.T
v = pairval((-1, 0, 0), (0, 0, -1), table(rho4))
Pmx = (I2 - X) / 2
Pmz = (I2 - Z) / 2
sharp_val = sp.simplify((rho4 * kron(Pmx, Pmz)).trace())
# The kernel's "product of the sharp effects" is the affine effect (1 - x1)/2 times (1 - x3)/2,
# i.e. pairVal / 4.  (Run 1 compared pairVal itself with -1/2; that normalization was wrong.)
check("G3b chain: product of sharp effects along -e1, -e3 = -1/2 (= pairVal/4; pairVal = -2)",
      sharp_val == sp.Rational(-1, 2) and v == -2, "sharp value %s, pairVal %s" % (sharp_val, v))
# Control: a determinant +1 one-copy flip (conjugation by Z on qubit 2: x,y -> -x,-y)
# is completely positive, so the chain stays a state and every product value >= 0.
rho3c = kron(I2, Z) * rho2 * kron(I2, Z)
rho4c = CNOT * rho3c * CNOT.T
vals_c = [pairval(s1, s2, table(rho4c)) for s1 in [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]
          for s2 in [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]]
check("G3c control: det(+1) flip keeps the chain PSD and all Pauli product values >= 0",
      min(eigs(rho4c)) >= 0 and min(vals_c) >= 0, "min eig %s, min pairVal %s" % (min(eigs(rho4c)), min(vals_c)))

# ---------------------------------------------------------------------------
# G4. The correlator table reported in QP DESIGN node 10 for the encoded
#     wing-local-parity composite (<XX> = <ZZ> = 1, <YY> = 0, uniform
#     marginals; the remaining cross terms are read as 0, see ASSESS-868 sec. 4.3).
#     Generic check of where that table sits: in maxCone, outside Q3.
T = (kron(I2, I2) + kron(X, X) + kron(Z, Z)) / 4
wT = table(T)
pvT = sp.expand(pairval(a, b, wT))
check("G4a node-10 table pairVal = 1 + a1 b1 + a3 b3 (>= 0 on the unit balls by Cauchy-Schwarz)",
      sp.simplify(pvT - (1 + a[0] * b[0] + a[2] * b[2])) == 0, str(pvT))
check("G4b node-10 table has eigenvalue -1/4 (not PSD, so outside Q3)",
      min(eigs(T)) == sp.Rational(-1, 4), str(eigs(T)))
phi = CNOT * rho1 * CNOT.T
check("G4c the quantum (table) CNOT image of (x+, z+) has <YY> = -1, not 0",
      sp.simplify((phi * kron(Y, Y)).trace()) == -1)
TreflY = ptranspose2(T)
check("G4d node-10 table is invariant under the one-copy reflection Y -> -Y", sp.simplify(TreflY - T) == sp.zeros(4, 4))
# Pauli product effects (the natively readable tests) are all valid on it:
vals_T = [pairval(s1, s2, wT) for s1 in [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]
          for s2 in [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]]
check("G4e all 36 signed Pauli product values on the node-10 table are >= 0", min(vals_T) >= 0, str(sorted(set(vals_T))))

# ---------------------------------------------------------------------------
# G5. Local tomography is a separate restriction that complex QM satisfies and
#     real (rebit) QM does not: product span dimensions 16 = 16 versus 9 < 10.
herm2 = [I2, X, Y, Z]
prod_c = [kron(p, q) for p in herm2 for q in herm2]
vecs_c = sp.Matrix([[sp.re(e) for e in M] + [sp.im(e) for e in M] for M in prod_c])
check("G5a complex: real span of products of Hermitian 2x2 has dimension 16 = dim Herm(4)", vecs_c.rank() == 16)
sym2 = [I2, X, Z]  # real symmetric 2x2 basis
prod_r = [kron(p, q) for p in sym2 for q in sym2]
vecs_r = sp.Matrix([[e for e in M] for M in prod_r])
check("G5b real: span of products of real symmetric 2x2 has dimension 9 < 10 = dim Sym_4(R)", vecs_r.rank() == 9)
YY = kron(Y, Y)
check("G5c Y(x)Y is real symmetric and HS-orthogonal to every real product, so (I +- e YY)/4 are "
      "distinct rebit states with identical real product statistics",
      YY.is_symmetric() and all(sp.im(e) == 0 for e in YY) and all((YY * M).trace() == 0 for M in prod_r))

# ---------------------------------------------------------------------------
# G6. The operator identity behind T2 sec. 6's quantum bound, on one instance:
#     C^2 = 4I - [A0,A1](x)[B0,B1] and ||C|| = 2 sqrt 2.
A0, A1 = Z, X
B0, B1 = (Z + X) / sp.sqrt(2), (Z - X) / sp.sqrt(2)
C = kron(A0, B0 + B1) + kron(A1, B0 - B1)
lhs = sp.simplify(C * C)
rhs = sp.simplify(4 * sp.eye(4) - kron(A0 * A1 - A1 * A0, B0 * B1 - B1 * B0))
check("G6a C^2 = 4I - [A0,A1](x)[B0,B1]", sp.simplify(lhs - rhs) == sp.zeros(4, 4))
check("G6b max eigenvalue of C is 2 sqrt 2", max(eigs(C), key=lambda t: float(t)) == 2 * sp.sqrt(2), str(eigs(C)))

# ---------------------------------------------------------------------------
# G7. Monomial Kraus operators (permutation times diagonal, symbolic entries)
#     map every diagonal matrix to a diagonal matrix, on a 4-state carrier and
#     for every one of the 24 permutations.  Control: a non-monomial operator
#     (Hadamard on the first factor) maps a diagonal state to one with a
#     nonzero off-diagonal entry.
import itertools
d = sp.symbols('d0:4', real=True)
ph = sp.symbols('c0:4')
D = sp.diag(*d)
all_diag = True
for perm in itertools.permutations(range(4)):
    P = sp.zeros(4, 4)
    for i, j in enumerate(perm):
        P[i, j] = 1
    Mmon = P * sp.diag(*ph)
    out = sp.expand(Mmon * D * Mmon.H)
    if any(out[i, j] != 0 for i in range(4) for j in range(4) if i != j):
        all_diag = False
check("G7a every monomial Kraus operator (24 permutations, symbolic diagonal factor) keeps diagonal matrices diagonal",
      all_diag)
Hd = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
outH = sp.simplify(kron(Hd, I2) * kron(rho_zero, rho_zero) * kron(Hd, I2).T)
check("G7b control: a non-monomial operator produces an off-diagonal entry from a diagonal state",
      any(outH[i, j] != 0 for i in range(4) for j in range(4) if i != j))

print()
n_fail = sum(1 for _, ok in results if not ok)
print("checks: %d, failures: %d" % (len(results), n_fail))
