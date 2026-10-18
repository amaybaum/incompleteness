# Exact check of f2-decision-memo.md Fact B with SymPy: Gamma = partial transpose on the second token of C^2 (x) C^2.
import sympy as sp
def pt(M):  # partial transpose on token 2; basis index = 2*a + b
    R = sp.zeros(4,4)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    R[2*a+d, 2*c+b] = M[2*a+b, 2*c+d]
    return R
def psd(M): return all(sp.nsimplify(e) >= 0 for e in M.eigenvals())
CNOT = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
phi = sp.Matrix([1,0,0,1])/sp.sqrt(2); B = phi*phi.T
# (1) Bell projector not in Gamma(Q3): B = Gamma(X) needs X = Gamma(B) PSD
print("Gamma(B) eigenvalues:", Gamma_B := pt(B).eigenvals(), "-> B in Gamma(Q3):", psd(pt(B)))
# (2) Gamma(Q3) not CNOT-invariant: find X in Gamma(Q3) (X = Gamma(rho), rho PSD) with CNOT X CNOT not in Gamma(Q3)
X = pt(B)                       # in Gamma(Q3) since B is PSD
Y = CNOT*X*CNOT.T
print("Gamma(CNOT X CNOT) eigenvalues:", pt(Y).eigenvals(), "-> invariant on this element:", psd(pt(Y)))
# (3) product states are fixed by Gamma up to a product state (transpose of a qubit state is a state)
a = sp.Matrix([[sp.Rational(1,2), sp.I/3],[-sp.I/3, sp.Rational(1,2)]]); b = sp.Matrix([[sp.Rational(2,3), sp.Rational(1,4)-sp.I/5],[sp.Rational(1,4)+sp.I/5, sp.Rational(1,3)]])
P = sp.kronecker_product(a,b); print("Gamma(product) is a PSD product:", psd(pt(P)) and pt(P)==sp.kronecker_product(a,b.T))
