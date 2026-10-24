"""Node 2, part C: exact checks for the Kraus-word lemma, the u(d) generation identity, and the
finite-realization value count. SymPy, exact."""
import itertools
import sympy as sp

PASS = []
def check(name, cond):
    PASS.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)

def vec(K):            # column stacking
    return sp.Matrix([K[i, j] for j in range(K.cols) for i in range(K.rows)])
def choi(kraus):
    return sum((vec(K) * vec(K).H for K in kraus), sp.zeros(kraus[0].rows ** 2))

Z = sp.diag(1, -1); I2 = sp.eye(2)
p = sp.symbols('p', positive=True)
check("W1 Choi(Ad Z) has rank 1", choi([Z]).rank() == 1)
Cn = choi([sp.sqrt(1 - p) * Z, sp.sqrt(p) * I2])
check("W2 Choi(Phi_n) = Choi((1-p) Ad Z + p id) has rank 2 for 0 < p < 1 (p = 1/2, 1/16, 1/1024)",
      all(Cn.subs(p, v).rank() == 2 for v in (sp.Rational(1, 2), sp.Rational(1, 16), sp.Rational(1, 1024))))
# W3: a decomposition of Ad U into several Kraus operators has every operator proportional to U:
# Choi(Ad U) - |K><K| must be PSD; for K not proportional to U it is not.
U = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
K = sp.Matrix([[1, 0], [0, 0]]) / 2
M = choi([U]) - vec(K) * vec(K).H
u_ = vec(U); k_ = vec(K)
v_ = k_ - (u_.H * k_)[0] / (u_.H * u_)[0] * u_          # component of vec K orthogonal to vec U
q_ = sp.simplify((v_.H * M * v_)[0])
check("W3 for K not proportional to U, <<v|Choi(Ad U) - |K>><<K||v>> < 0 exactly for v = vec K minus its vec U part (so K cannot be a summand)",
      sp.simplify(q_ - (-(v_.H * k_)[0] * (k_.H * v_)[0])) == 0 and sp.nsimplify(q_) < 0)
K2 = U / 3
M2 = choi([U]) - vec(K2) * vec(K2).H
check("W3b for K = U/3 the remainder is PSD (8/9 Choi(Ad U))", all(sp.re(ev) >= 0 for ev in M2.eigenvals()))
# W4: generation of u(d) by i X_ab and i P_c: [P_a, X_ab] = E_ab - E_ba and X_ab - sum_{c != a,b} P_c = E_ab + E_ba.
def perm_t(d, a, b):
    M = sp.eye(d); M[a, a] = 0; M[b, b] = 0; M[a, b] = 1; M[b, a] = 1; return M
ok = True
for d in (2, 3, 5, 7):
    for a, b in itertools.combinations(range(d), 2):
        Xab = perm_t(d, a, b)
        Pa = sp.zeros(d); Pa[a, a] = 1
        E = sp.zeros(d); E[a, b] = 1
        rest = sp.diag(*[0 if c in (a, b) else 1 for c in range(d)])
        ok = ok and (Pa * Xab - Xab * Pa == E - E.T) and (Xab - rest == E + E.T)
check("W4 [P_a, X_ab] = E_ab - E_ba and X_ab - sum_{c not in {a,b}} P_c = E_ab + E_ba (d = 2, 3, 5, 7, all pairs)", ok)
# W5: a fixed finite realization has finitely many event probabilities; 2^-n takes infinitely many values.
Nst = 2 ** 10
vals = {sp.Rational(k, Nst) for k in range(Nst + 1)}
check("W5 with 2^10 equiprobable microstates, 2^-11 is not an achievable nonzero event probability",
      sp.Rational(1, 2 ** 11) not in vals and sp.Rational(1, 2 ** 10) in vals)
print()
print(f"{sum(PASS)} PASS, {len(PASS) - sum(PASS)} FAIL")
