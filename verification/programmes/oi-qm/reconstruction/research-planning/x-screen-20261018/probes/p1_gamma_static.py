#!/usr/bin/env python3
"""p1_gamma_static.py -- exact screen (SymPy, no floats).  Research only; decides no round.

Question: can a principle that is invariant under GPT isomorphism tell Q3 from Gamma(Q3)?
Gamma = partial transpose on token 2 of C^2 (x) C^2, basis index 2a+b.

Checks (each a certificate for a written argument; finite checks on matrix units certify linear
identities on all matrices, nothing else):
  G1  Gamma is linear, involutive, trace preserving, a Hilbert-Schmidt isometry and self-adjoint
      (256 unit pairs)  -> transports SP frames, self-duality, LT dimension, homogeneity [W].
  G2  Gamma fixes every diagonal (configuration-level) matrix unit -> no configuration-level /
      ensemble-pushforward principle can separate Q3 from Gamma(Q3) [W].
  G3  local covariance  Gamma(Ad_{A(x)B} Gamma(Y)) = Ad_{A(x)conj(B)} Y  with symbolic A, B.
  G4  SP frame: Gamma(Bell frame) is a trace-orthonormal frame summing to I.
  G5  purification (OP) inside Gamma(Q3): Gamma(Phi+), Gamma((I(x)S)Phi+) have equal token-1
      marginals and are related by the NATIVE local unitary Ad_{I(x)conj(S)}.
  G6  continuous interacting reversible group on Gamma(Q3): Gamma Ad_U Gamma, U = 3/5 I - 4i/5 Z(x)Z,
      maps the Gamma-product of |++> to a non-product (entangled-class) element.
  G7  separation by the native CNOT (Fact B replay): Bell in Q3, not in Gamma(Q3);
      Gamma(CNOT Gamma(B) CNOT) has eigenvalue -1/2.
Controls:  positive  -- Q3 (Gamma -> identity) passes every principle and contains Bell;
           mutation  -- full transpose T in place of Gamma must FAIL the Bell-exclusion test;
           mutation  -- the OP map with S instead of conj(S) must FAIL;
           mutation  -- a local U (Z(x)I) in G6 must FAIL the entangling test.
"""
import sympy as sp
from itertools import product

I = sp.I
def E(i, j, n=4):
    M = sp.zeros(n, n); M[i, j] = 1; return M
def pt2(M):
    R = sp.zeros(4, 4)
    for a, b, c, d in product(range(2), repeat=4):
        R[2*a+d, 2*c+b] = M[2*a+b, 2*c+d]
    return R
def ptfull(M): return M.T
def ident(M): return M
def kron(A, B): return sp.kronecker_product(A, B)
def ad(U, X): return sp.simplify(U * X * U.H)
def herm_psd(M):
    """exact PSD test for a Hermitian matrix: all principal minors >= 0."""
    n = M.shape[0]
    from itertools import combinations
    for k in range(1, n+1):
        for S in combinations(range(n), k):
            m = sp.nsimplify(sp.simplify(M.extract(list(S), list(S)).det()))
            m = sp.simplify(m)
            if not (m.is_real and m >= 0):
                return False
    return True
def marg1(M):  # trace out token 2
    R = sp.zeros(2, 2)
    for a, c in product(range(2), repeat=2):
        R[a, c] = sum(M[2*a+b, 2*c+b] for b in range(2))
    return sp.simplify(R)
def is_product_matrix(M):
    """M (4x4) is a tensor product A(x)B iff its realignment has rank <= 1."""
    R = sp.zeros(4, 4)
    for a, b, c, d in product(range(2), repeat=4):
        R[2*a+c, 2*b+d] = M[2*a+b, 2*c+d]
    return sp.simplify(R).rank() <= 1

results = []
def check(name, cond):
    results.append((name, bool(cond))); print(('PASS ' if cond else 'FAIL ') + name)

units = [E(i, j) for i in range(4) for j in range(4)]
G = pt2
# G1
check('G1 involution on 16 units', all(G(G(U)) == U for U in units))
check('G1 trace preserving on 16 units', all(G(U).trace() == U.trace() for U in units))
check('G1 HS isometry on 256 pairs', all((G(X).H * G(Y)).trace() == (X.H * Y).trace() for X in units for Y in units))
check('G1 self-adjoint on 256 pairs', all((G(X) * Y).trace() == (X * G(Y)).trace() for X in units for Y in units))
# G2
check('G2 Gamma fixes the 4 diagonal units', all(G(E(i, i)) == E(i, i) for i in range(4)))
# G3
a = sp.symbols('a0:4'); b = sp.symbols('b0:4'); c = sp.symbols('c0:4'); d = sp.symbols('d0:4')
A = sp.Matrix(2, 2, [a[k] + I*b[k] for k in range(4)])
B = sp.Matrix(2, 2, [c[k] + I*d[k] for k in range(4)])
def conjm(M): return M.applyfunc(sp.conjugate)
ok3 = True
for U in units:
    lhs = G(kron(A, B) * G(U) * kron(A, B).H)
    rhs = kron(A, conjm(B)) * U * kron(A, conjm(B)).H
    ok3 &= sp.expand(lhs - rhs) == sp.zeros(4, 4)
check('G3 local covariance identity, symbolic A,B, 16 units', ok3)
# G4
s2 = sp.sqrt(2)
bells = [sp.Matrix([1, 0, 0, 1])/s2, sp.Matrix([1, 0, 0, -1])/s2, sp.Matrix([0, 1, 1, 0])/s2, sp.Matrix([0, 1, -1, 0])/s2]
P = [v * v.H for v in bells]
GP = [G(p) for p in P]
check('G4 Gamma(Bell frame) trace-orthonormal', all(sp.simplify((GP[i]*GP[j]).trace()) == (1 if i == j else 0) for i in range(4) for j in range(4)))
check('G4 Gamma(Bell frame) sums to I', sp.simplify(sum(GP, sp.zeros(4, 4))) == sp.eye(4))
# G5
S = sp.diag(1, I)
phi = bells[0]; psi = kron(sp.eye(2), S) * phi
X1, X2 = G(phi*phi.H), G(psi*psi.H)
check('G5 equal token-1 marginals I/2', marg1(X1) == sp.eye(2)/2 and marg1(X2) == sp.eye(2)/2)
check('G5 native local Ad_{I(x)conj S} maps Gamma(Phi+) to Gamma((I(x)S)Phi+)', ad(kron(sp.eye(2), conjm(S)), X1) == sp.simplify(X2))
mut5 = ad(kron(sp.eye(2), S), X1) == sp.simplify(X2)
check('G5 mutation (S instead of conj S) fails as required', not mut5)
# G6
Z = sp.diag(1, -1)
U = sp.Rational(3, 5)*sp.eye(4) - sp.Rational(4, 5)*I*kron(Z, Z)
check('G6 U unitary', sp.simplify(U*U.H) == sp.eye(4))
plus = sp.Matrix([1, 1])/s2; pp = kron(plus, plus); Pp = pp*pp.H
img = G(ad(U, G(G(Pp))))   # Gamma Ad_U Gamma applied to Gamma(product) = Gamma(U P U^dag)
check('G6 input Gamma(|++><++|) is a product', is_product_matrix(G(Pp)))
check('G6 Gamma Ad_U Gamma output is not a product (interacting)', not is_product_matrix(img))
check('G6 output lies in Gamma(Q3) (preimage PSD)', herm_psd(sp.simplify(G(img))))
Uloc = sp.Rational(3, 5)*sp.eye(4) - sp.Rational(4, 5)*I*kron(Z, sp.eye(2))
imgl = G(ad(Uloc, G(G(Pp))))
check('G6 mutation (local Z(x)I) stays product, i.e. the entangling test can fail', is_product_matrix(imgl))
# G7
Bm = P[0]
CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
check('G7 Bell in Q3', herm_psd(Bm))
check('G7 Bell not in Gamma(Q3) (Gamma(B) not PSD)', not herm_psd(G(Bm)))
ev = sp.Matrix(G(CN*G(Bm)*CN.T)).eigenvals()
check('G7 Gamma(CNOT Gamma(B) CNOT) eigenvalues {1/2:3,-1/2:1}', {sp.nsimplify(k): v for k, v in ev.items()} == {sp.Rational(1, 2): 3, sp.Rational(-1, 2): 1})
# positive control: identity in place of Gamma (Q3 itself)
check('POS Q3: Bell contained (identity frame)', herm_psd(ident(Bm)))
check('POS Q3: CNOT preserves the Bell state', herm_psd(CN*Bm*CN.T))
# mutation: full transpose
check('MUT full transpose keeps Bell (exclusion test reports no separation)', herm_psd(ptfull(Bm)))

n_fail = sum(1 for _, okk in results if not okk)
print('SUMMARY checks=%d failed=%d' % (len(results), n_fail))
print('VERDICT', 'GAMMA-INVISIBLE-STATIC: SP, self-duality, HS isometry (LT/homogeneity), local covariance, '
      'purification and a continuous interacting group all transport to Gamma(Q3); the native CNOT separates '
      '(which other native permutations separate: p2)'
      if n_fail == 0 else 'VOID (a control failed)')
