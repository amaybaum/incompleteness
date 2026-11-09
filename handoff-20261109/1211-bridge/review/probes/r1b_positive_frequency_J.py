"""Reviewer probe R1b (exact sympy): the positive-frequency complex structure of one
non-null mode of the real lift, and the O-commutant at the null mode."""
import sympy as sp
a = sp.Rational(1, 2)
f = sp.Matrix([[0, 1], [-1, a]])
c = a / 2; s = sp.sqrt(1 - c**2)
Jf = (f - c * sp.eye(2)) / s
print('Jf^2 == -I:', sp.simplify(Jf**2 + sp.eye(2)) == sp.zeros(2, 2))
I6 = sp.eye(6); Z6 = sp.zeros(6, 6)
F = sp.Matrix(sp.kronecker_product(f, I6))
J = sp.Matrix(sp.kronecker_product(Jf, I6))
Omega = sp.Matrix(sp.BlockMatrix([[Z6, I6], [-I6, Z6]]))
print('J commutes with F:', sp.simplify(J * F - F * J) == sp.zeros(12, 12))
print('J symplectic (J^T Omega J == Omega):', sp.simplify(J.T * Omega * J - Omega) == sp.zeros(12, 12))
X = sp.Matrix(12, 12, sp.symbols('y0:144'))
eqs = list(X * F - F * X) + list(X.T * Omega + Omega * X)
A, _ = sp.linear_eq_to_matrix(eqs, list(X))
basis = [sp.Matrix(12, 12, list(v)) for v in A.nullspace()]
print('every commutant element commutes with J:', all(sp.simplify(B * J - J * B) == sp.zeros(12, 12) for B in basis))
# null mode a=2: commutant of f in Mat2(R)
fn = sp.Matrix([[0, 1], [-1, 2]])
p, q, r, t = sp.symbols('p q r t')
Y = sp.Matrix([[p, q], [r, t]])
sol = sp.solve(list(Y * fn - fn * Y), [p, q, r, t], dict=True)
print('null-mode commutant of f in Mat2(R):', sol, '; N = f - I, N^2 =', ((fn - sp.eye(2))**2).tolist())
