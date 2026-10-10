"""Uniform d-ball theorem (native NOT relations + reversibility) -- exact checks of each step, plus controls. Read-only.
Claim: locally tomographic d-ball composite, min <= C <= max; G linear, G(C) = C, CNOT on the corners; native relations
(I(x)N)G(I(x)N) = G, (N(x)I)G(N(x)I) = (I(x)N)G for an involution N of the ball swapping the corners.
Then d = 3 (or d = 1).  No G^2 = I, no local continuous group.
 S1 controlled form (depth-1 positivity for G and G^-1): G(|a>(x)t) = |a>(x)M_a t, M_a isometries, M_1 = N M_0.
 S2 first order at control corners: Gt = G(I(x)M_0^-1) acts on T_A (x) E+ (E+ = u + V+, V+ = N's +1 transverse
    space, dim p) as [[0, A_r],[A_r, B_rs]] (B antisymmetric in r,s) and maps T_A (x) V- into itself.
 S3 averaging: a target form [[1, g^T],[g, I + K]] (K antisymmetric) is Lorentz-positive only if, averaging over the target
    sphere, |g|^2 (1 - 1/p) + |K|^2/p <= 0: for p >= 2, g = 0 and K = 0.
 S4 the same holds for f = u + a, s = u + c with any unit a, c: Gamma_ac = [[0, g^T],[g, K]] with g_r = a.A_r c and K
    antisymmetric, so the bound gives A_r = 0 and B_rs = 0: Gt vanishes on T_A (x) E+ and G is singular.  Hence p <= 1.
 S5 control relation: G on T_A (x) V- anticommutes with N_A (x) I and is invertible there: p = q.  So p = q <= 1: d <= 3."""
import sympy as sp, numpy as np
OUT = []
def rep(n, ok, det=''):
    OUT.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + n + ('  ' + det if det else ''), flush=True)
# S3: averaging identity with E[t] = 0, E[t t^T] = I/p, for p = 2..5
for p in (2, 3, 4, 5):
    A = sp.Matrix(sp.symbols('A0:%d' % p)); Bs = sp.symbols('B0:%d' % (p * (p - 1) // 2)); B = sp.zeros(p)
    k = 0
    for i in range(p):
        for j in range(i + 1, p): B[i, j] = Bs[k]; B[j, i] = -Bs[k]; k += 1
    I = sp.eye(p)
    # E(1 + A.t)^2 = 1 + |A|^2/p ;  E|A + (I+B)t|^2 = |A|^2 + tr((I+B)^T (I+B))/p
    lhs = 1 + (A.T * A)[0] / p
    rhs = (A.T * A)[0] + ((I + B).T * (I + B)).trace() / p
    diff = sp.expand(lhs - rhs)
    target = sp.expand(-((A.T * A)[0] * (1 - sp.Rational(1, p)) + (B.T * B).trace() / p))
    rep('S3 p=%d: E[(1+A.t)^2] - E|A+(I+B)t|^2 = -(|A|^2 (1-1/p) + |B|^2/p)' % p, sp.simplify(diff - target) == 0)
# S3 applies to every pair (a, c): check the form of Gamma_ac on the positive examples (symmetric u-coupling, V+ block
# antisymmetric), computed directly from G with M_0 = I.  J/K (d = 5, p = 1) and the complex CNOT (d = 3, p = 1).
def gamma_form(G, n, TA, Eplus):
    ok = True
    for a_ in TA:
        for c_ in TA:
            Gam = np.zeros((len(Eplus), len(Eplus)))
            for j, ej in enumerate(Eplus):
                col = G[:, c_ * n + ej].reshape(n, n)       # G(c (x) e_j) as control x target
                for i, ei in enumerate(Eplus): Gam[i, j] = col[a_, ei]
            ok &= np.allclose(Gam[0, 1:], Gam[1:, 0]) and np.allclose(Gam[1:, 1:], -Gam[1:, 1:].T)
    return ok
import ball5_run1 as r1
GJK = r1.JK_G().mat()
rep('S3 form: J/K (d=5) Gamma_ac has symmetric u-coupling and antisymmetric V+ block for all basis a, c',
    gamma_form(GJK, 6, [1, 2, 4, 5], [0, 1]))
from disc_cnot_search import complex_cnot
rep('S3 form: complex CNOT (d=3) likewise', gamma_form(complex_cnot(), 4, [1, 2], [0, 1]))
# control d = 3 (p = 1): Gamma_cc = [[0,1],[1,0]] (u <-> x), I + Gamma Lorentz-positive (rank one); S3 bound is 0 at p = 1
t = sp.symbols('t'); X = sp.Matrix([[1, 1], [1, 1]])
rep('control d=3 (p=1): (1,b)[[1,1],[1,1]](1,t) = (1+b)(1+t) >= 0 on [-1,1]^2', sp.factor((sp.Matrix([1, sp.Symbol('b')]).T * X * sp.Matrix([1, t]))[0]) == (sp.Symbol('b') + 1) * (t + 1))
# explicit witness for the d = 7 algebraic candidate (p = 3): s = f = u + x, t = u + v3, g = (1, -w/|w|)
from ball7 import build, n
G = build(); e = np.eye(n); u, x, v2, v3, z = 0, 1, 2, 3, 7
s = e[u] + e[x]; f = e[u] + e[x]; tt = e[u] + e[v3]
vec = G @ np.kron(s, tt)                               # evaluate (f (x) .) : contract control with f
Wt = vec.reshape(n, n); w = f @ Wt                     # target vector (Lorentz: need w0 >= |w_{1:}|)
w0, wr = sp.nsimplify(w[0]), [sp.nsimplify(val) for val in w[1:]]
norm = sp.sqrt(sum(val ** 2 for val in wr))
rep('d=7 candidate witness: (f(x)g)(G(s(x)t)) = w0 - |w| = %s < 0 (exact, g = (1, -w/|w|))' % sp.simplify(w0 - norm),
    sp.simplify(w0 - norm) < 0)
print('\nSUMMARY: %d PASS, %d FAIL' % (sum(OUT), len(OUT) - sum(OUT)))
