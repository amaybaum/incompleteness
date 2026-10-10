"""Exact checks for the DIM-1 design module at d = 3 (sympy): CNOT table, frame, Rt, Rc,
involution, the SOS identity for pure data, and the Bell-state extremality algebra."""
import sympy as sp

def cnot(r):
    """Schroedinger action on the 4x4 Pauli-coefficient matrix r (0=1,1=X,2=Y,3=Z)."""
    w = sp.zeros(4, 4)
    w[0,0]=r[0,0]; w[0,1]=r[0,1]; w[0,2]=r[3,2]; w[0,3]=r[3,3]
    w[1,0]=r[1,1]; w[1,1]=r[1,0]; w[1,2]=r[2,3]; w[1,3]=-r[2,2]
    w[2,0]=r[2,1]; w[2,1]=r[2,0]; w[2,2]=-r[1,3]; w[2,3]=r[1,2]
    w[3,0]=r[3,0]; w[3,1]=r[3,1]; w[3,2]=r[0,2]; w[3,3]=r[0,3]
    return w

r = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"r{i}{j}"))
assert cnot(cnot(r)) == r, "involution"
Nh = sp.diag(1, 1, -1, -1)  # homogenized NOT (X conjugation): flips Y, Z
# Rt: actT(G(actT w)) = G w, actT w = w * Nh^T ; Rc: actC(G(actC w)) = actT(G w), actC w = Nh * w
assert sp.simplify(cnot(r * Nh.T) * Nh.T - cnot(r)) == sp.zeros(4,4), "Rt"
assert sp.simplify(Nh * cnot(Nh * r) - cnot(r) * Nh.T) == sp.zeros(4,4), "Rc"
# frame: corners z = (0,0,1), k0 = z, k1 = -z
def hom(v): return sp.Matrix([1, v[0], v[1], v[2]])
z = (0, 0, 1); k = {0: z, 1: (0, 0, -1)}
for a in (0, 1):
    for b in (0, 1):
        assert cnot(hom(k[a]) * hom(k[b]).T) == hom(k[a]) * hom(k[(a + b) % 2]).T, "frame"
# SOS identity
def bloch(p):
    a, b, c, d = p
    return sp.Matrix([a*a+b*b+c*c+d*d, 2*(a*c+b*d), 2*(a*d-b*c), a*a+b*b-c*c-d*d])
eta = sp.symbols('e0:4', real=True); xi = sp.symbols('f0:4', real=True); psi = sp.symbols('p0:4', real=True); phi = sp.symbols('q0:4', real=True)
def val(e, f, w): return (e.T * w * f)[0, 0]
V = sp.expand(val(bloch(eta), bloch(xi), cnot(bloch(psi) * bloch(phi).T)))
I = sp.I
def amp(p): return (p[0] + I*p[1], p[2] + I*p[3])
P, Q = amp(psi), amp(phi); E, F = amp(eta), amp(xi)
c = {(0,0): P[0]*Q[0], (0,1): P[0]*Q[1], (1,0): P[1]*Q[1], (1,1): P[1]*Q[0]}
A = sum(sp.conjugate(E[a]*F[b]) * c[(a, b)] for a in (0,1) for b in (0,1))
A = sp.expand(A)
re, im = sp.re(A), sp.im(A)
re = sp.expand(re); im = sp.expand(im)
diff = sp.expand(V - 4*(re**2 + im**2))
print("SOS residual:", diff)
print("Re amp =", re)
print("Im amp =", im)
# Bell state: input x = (1,0,0) control, y = z target
bell = cnot(hom((1, 0, 0)) * hom(z).T)
print("Bell coefficient matrix:", bell.tolist())
# phi+ check: coefficient 1 at (0,0),(1,1),(3,3), -1 at (2,2)
