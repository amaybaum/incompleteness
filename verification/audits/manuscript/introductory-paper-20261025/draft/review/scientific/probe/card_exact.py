"""Independent exact check of the card-table claims (Introduction draft §4.3) and §4.1 numbers.
Written for the scientific review; does not import or reuse draft/probe/swap_memory.py.
All arithmetic is exact (fractions / sympy rationals and symbols)."""
from fractions import Fraction as F
from itertools import product
import sympy as sp

# ---------------------------------------------------------------- 1. classical card protocols
def odds(prior, peek=None, shuffles=2):
    """prior: dict (h,b)->prob. Returns P(hole at showdown == hole as dealt).
    peek in {None,'A' overwrite burn with fresh uniform,'B' replace hole with fresh uniform keep burn,
    'C' reveal only}."""
    tot = F(0)
    for (h0, b0), p in prior.items():
        if p == 0:
            continue
        branches = [((h0, b0), p)]
        for step in range(shuffles):
            nb = []
            for (h, b), q in branches:
                h, b = b, h                      # shuffle = swap
                if step == 0 and shuffles == 2 and peek in ('A', 'B'):
                    for c in (0, 1):
                        nb.append((((h, c) if peek == 'A' else (c, b)), q * F(1, 2)))
                else:
                    nb.append(((h, b), q))
            branches = nb
        tot += sum(q for (h, b), q in branches if h == h0)
    return tot

uni = {(h, b): F(1, 4) for h, b in product((0, 1), repeat=2)}
anti = {(h, 1 - h): F(1, 2) for h in (0, 1)}
print("1. card odds, burn uniform & independent:")
print("   one shuffle", odds(uni, shuffles=1), "| two", odds(uni), "| peek A (overwrite burn)", odds(uni, 'A'),
      "| peek B (replace hole only)", odds(uni, 'B'), "| peek C (reveal only)", odds(uni, 'C'))
print("   anticorrelated: one", odds(anti, shuffles=1), "two", odds(anti))

# rooted matrices
def gamma(prior, t):
    G = sp.zeros(2, 2)
    for x0 in (0, 1):
        px = sum(p for (h, b), p in prior.items() if h == x0)
        for (h, b), p in prior.items():
            if h != x0:
                continue
            s = (h, b)
            for _ in range(t):
                s = (s[1], s[0])
            G[x0, s[0]] += sp.Rational(p.numerator, p.denominator) / sp.Rational(px.numerator, px.denominator)
    return G
G1, G2 = gamma(uni, 1), gamma(uni, 2)
print("   Gamma1 =", G1.tolist(), "Gamma2 =", G2.tolist(), "Gamma1^2 =", (G1 * G1).tolist())
print("   anticorrelated Gamma1 =", gamma(anti, 1).tolist())

# ---------------------------------------------------------------- 2. draft line 213 claim
L = sp.Matrix([[1, 0], [1, 0]])  # row-stochastic, not doubly stochastic
print("2. Gamma1*Lambda for Lambda=[[1,0],[1,0]]:", (G1 * L).tolist(), "(draft says = J/2 for every stochastic Lambda)")
l1, l2 = sp.symbols('l1 l2')
Lg = sp.Matrix([[l1, 1 - l1], [l2, 1 - l2]])
P = G1 * Lg
print("   general stochastic Lambda: rows of Gamma1*Lambda equal?", sp.simplify(P[0, :] - P[1, :]) == sp.zeros(1, 2),
      "; can equal I? ", sp.solve(list(P - sp.eye(2)), [l1, l2], dict=True))

# ---------------------------------------------------------------- 3. quantum channels of the swap
def ket(i, n=2):
    v = sp.zeros(n, 1); v[i] = 1; return v
# basis |x,h> index 2*x+h ; U|x,h> = |h,x>
U = sp.zeros(4, 4)
for x, h in product((0, 1), repeat=2):
    U[2 * h + x, 2 * x + h] = 1
assert U * U.T == sp.eye(4)
a, b, c, d = sp.symbols('a b c d')   # arbitrary (not even Hermitian) 2x2 input: linear maps checked on all of M_2
rho = sp.Matrix([[a, b], [c, d]])

def kron(A, B):
    return sp.kronecker_product(A, B)

def ptrace_H(R):
    out = sp.zeros(2, 2)
    for i, j in product((0, 1), repeat=2):
        out[i, j] = sum(R[2 * i + k, 2 * j + k] for k in (0, 1))
    return out

def chan(tau, t):
    Ut = U ** t
    return lambda X: sp.simplify(ptrace_H(Ut * kron(X, tau) * Ut.T))

tau_u = sp.eye(2) / 2
tau_0 = sp.diag(1, 0)
for name, tau in (("uniform burn", tau_u), ("initialized |0>", tau_0)):
    print(f"3. {name}: Phi1(rho) =", chan(tau, 1)(rho).tolist(), " Phi2(rho) =", chan(tau, 2)(rho).tolist())

# ---------------------------------------------------------------- 4. classical-memory decomposition, uniform burn
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.diag(1, -1)
Paulis = [I2, X, Y, Z]
Phi1u, Phi2u = chan(tau_u, 1), chan(tau_u, 2)
inst = [lambda R, s=s: sp.Rational(1, 4) * s * R * s.H for s in Paulis]          # I_o, Kraus op s/2
post = [lambda R, s=s: s * R * s.H for s in Paulis]                              # Psi_o, unitary channel
sum_inst = sp.simplify(sum((f(rho) for f in inst), sp.zeros(2, 2)))
tp = sp.simplify(sum(((s / 2).H * (s / 2) for s in Paulis), sp.zeros(2, 2)))
two = sp.simplify(sum((post[o](inst[o](rho)) for o in range(4)), sp.zeros(2, 2)))
print("4. sum_o I_o(rho) - Phi1(rho) =", sp.simplify(sum_inst - Phi1u(rho)).tolist(),
      "| sum K^dag K =", tp.tolist(),
      "| sum_o Psi_o(I_o(rho)) - Phi2(rho) =", sp.simplify(two - Phi2u(rho)).tolist())

# Choi-matrix form (out (x) in), J(E) = sum_ij E(|i><j|) (x) |i><j|
def choi(E):
    J = sp.zeros(4, 4)
    for i, j in product((0, 1), repeat=2):
        Eij = ket(i) * ket(j).T
        J += kron(E(Eij), Eij)
    return sp.simplify(J)
Jdec = choi(lambda R: sum((post[o](inst[o](R)) for o in range(4)), sp.zeros(2, 2)))
print("   Choi(decomposition) == Choi(id):", Jdec == choi(lambda R: R),
      "| Choi(I_o) PSD each:", all(all(ev >= 0 for ev in choi(f).eigenvals()) for f in inst))

# ---------------------------------------------------------------- 5. initialized slot: no decomposition
Phi10 = chan(tau_0, 1)
J10 = choi(Phi10)
print("5. initialized: Choi(Phi1) =", J10.tolist(), "rank", J10.rank())
# range of Choi(Phi1) = span{|0>_out (x) |v>_in}; any CP I_o <= Phi1 has Choi supported there => I_o(R)=|0><0| tr(E_o R).
# then sum_o Psi_o(I_o(R)) = sum_o tr(E_o R) Psi_o(|0><0|): measure-and-prepare => Choi separable => PPT.
Jid = choi(lambda R: R)
def ptranspose_in(J):
    out = sp.zeros(4, 4)
    for o1, i1, o2, i2 in product((0, 1), repeat=4):
        out[2 * o1 + i1, 2 * o2 + i2] = J[2 * o1 + i2, 2 * o2 + i1]
    return out
print("   Choi(id) partial-transpose eigenvalues:", ptranspose_in(Jid).eigenvals(),
      "-> not PPT, so id is not entanglement-breaking; no classical-memory decomposition (Main:702) - confirmed")
# uniform case: Choi(Phi1) = I/2 (x) I, full rank, so no such restriction
print("   uniform: rank Choi(Phi1) =", choi(Phi1u).rank())

# ---------------------------------------------------------------- 6. CP-indivisibility (uniform): no linear Lambda
# Phi1u(R) = tr(R) I/2 is constant on trace-one inputs; Lambda o Phi1u(R) = tr(R) Lambda(I/2) is rank one as a map.
print("6. Phi1u(rho) == tr(rho) I/2:", sp.simplify(Phi1u(rho) - (a + d) * sp.eye(2) / 2) == sp.zeros(2, 2),
      "=> Lambda o Phi1 has rank <= 1 as a linear map, id has rank 4: no linear (a fortiori no CPTP) divisor")

# ---------------------------------------------------------------- 7. §4.1 minimal model
H = range(1, 7)
pairs = [((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (0, 4)), ((0, 5), (0, 6)), ((1, 3), (1, 4)), ((1, 5), (1, 6))]
phi = {}
for p, q in pairs:
    phi[p] = q; phi[q] = p
assert len(phi) == 12
def G(t):
    M = sp.zeros(2, 2)
    for x in (0, 1):
        for h in H:
            s = (x, h)
            for _ in range(t):
                s = phi[s]
            M[x, s[0]] += sp.Rational(1, 6)
    return M
g1, g2 = G(1), G(2)
print("7. Gamma1", g1.tolist(), "Gamma2", g2.tolist(), "Gamma1^-1 Gamma2", (g1.inv() * g2).tolist(), "Gamma1^2", (g1 ** 2).tolist())
A = sp.symbols('A', positive=True)
num = den = 0
numc = denc = 0
for x0 in (0, 1):
    for h in H:
        w = (A if x0 == 0 else 1 - A) / 6
        s1 = phi[(x0, h)]; s2 = phi[s1]
        if s1[0] == 1:
            den += w
            if s2[0] == 0:
                num += w
            if x0 == 0:
                denc += w
                if s2[0] == 0:
                    numc += w
print("   P(x2=0|x1=1,x0=0) =", sp.simplify(numc / denc), "; P(x2=0|x1=1) =", sp.simplify(num / den),
      "; at a=1/2:", sp.simplify((num / den).subs(A, sp.Rational(1, 2))))

# ---------------------------------------------------------------- 8. XOR family
from math import log2
pj = {(x0, x1, x0 ^ x1): F(1, 4) for x0, x1 in product((0, 1), repeat=2)}
def cmi():
    # I(X0;X2|X1) exact in bits via counts (all probabilities dyadic)
    tot = 0.0
    for (x0, x1, x2), p in pj.items():
        p1 = sum(q for k, q in pj.items() if k[1] == x1)
        p01 = sum(q for k, q in pj.items() if k[0] == x0 and k[1] == x1)
        p12 = sum(q for k, q in pj.items() if k[1] == x1 and k[2] == x2)
        tot += float(p) * log2(float(p * p1 / (p01 * p12)))
    return tot
print("8. XOR: I(X0;X2|X1) =", cmi(), "bit")
