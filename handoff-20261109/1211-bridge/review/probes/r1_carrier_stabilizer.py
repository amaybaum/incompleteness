"""Reviewer probe R1 (independent of the writer's script; exact sympy).

(a) Config-space carrier: cubic rotation group O (24 elements) acting on the six signed
    links; generic O-equivariant symmetric Sigma; stabilizer Lie-algebra dimension in
    so(6) (real carrier) and in u(6) (complexified carrier).
(b) Phase-space real lift, one spatial Fourier mode, six degenerate components:
    F(u,v) = (v, a v - u) on R^6 + R^6.  Commutant of F inside sp(12,R): its dimension,
    and whether it is u(6) (36) or o(6) (15).  Then the stabilizer of a stationary
    O-equivariant covariance C = Sigma (x) K inside that commutant.
(c) Same at the null mode a = 2 (alpha = 1/d, k = 0).
"""
import itertools
import sympy as sp

# ---------- (a) cubic group on signed links ----------
def rot_mats():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = sp.zeros(3, 3)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if M.det() == 1:
                mats.append(M)
    return mats

O = rot_mats()
assert len(O) == 24
links = []
for j in range(3):
    for s in (1, -1):
        e = sp.zeros(3, 1); e[j] = s
        links.append(e)

def link_rep(R):
    P = sp.zeros(6, 6)
    for a, e in enumerate(links):
        img = R * e
        b = next(i for i, f in enumerate(links) if f == img)
        P[b, a] = 1
    return P

reps = [link_rep(R) for R in O]
# Reynolds average of a generic symmetric matrix -> generic O-equivariant Sigma
syms = sp.symbols('s0:21')
S0 = sp.zeros(6, 6); k = 0
for i in range(6):
    for j in range(i, 6):
        S0[i, j] = S0[j, i] = syms[k]; k += 1
avg = sp.zeros(6, 6)
for P in reps:
    avg += P * S0 * P.T
avg = avg / 24
# pick generic numeric values
vals = {s: sp.Rational(p, 7) for s, p in zip(syms, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6])}
Sigma = avg.subs(vals)
ev = Sigma.eigenvals()
print('(a) eigenvalue multiplicities of generic O-equivariant Sigma:', sorted(ev.values()))

def stab_dim_real(Sig, n):
    X = sp.Matrix(n, n, sp.symbols(f'x0:{n*n}'))
    eqs = list(X + X.T) + list(X * Sig - Sig * X)
    A, _ = sp.linear_eq_to_matrix(eqs, list(X))
    return n * n - A.rank()

def stab_dim_unitary(Sig, n):
    # u(n) as real 2n x 2n: H = A + iB, A antisym, B sym; commute with Sigma (real sym)
    Avars = sp.Matrix(n, n, sp.symbols(f'a0:{n*n}'))
    Bvars = sp.Matrix(n, n, sp.symbols(f'b0:{n*n}'))
    eqs = list(Avars + Avars.T) + list(Bvars - Bvars.T)
    eqs += list(Avars * Sig - Sig * Avars) + list(Bvars * Sig - Sig * Bvars)
    unk = list(Avars) + list(Bvars)
    A, _ = sp.linear_eq_to_matrix(eqs, unk)
    return 2 * n * n - A.rank()

print('(a) stabilizer dim in so(6):', stab_dim_real(Sigma, 6))
print('(a) stabilizer dim in u(6):', stab_dim_unitary(Sigma, 6))

# ---------- (b),(c) phase-space real lift, one mode ----------
I6 = sp.eye(6); Z6 = sp.zeros(6, 6)
def F_of(a):
    return sp.Matrix(sp.BlockMatrix([[Z6, I6], [-I6, a * I6]]))
Omega = sp.Matrix(sp.BlockMatrix([[Z6, I6], [-I6, Z6]]))

def commutant_sp(F):
    X = sp.Matrix(12, 12, sp.symbols('y0:144'))
    eqs = list(X * F - F * X) + list(X.T * Omega + Omega * X)
    A, _ = sp.linear_eq_to_matrix(eqs, list(X))
    ns = A.nullspace()
    return [sp.Matrix(12, 12, list(v)) for v in ns]

for a in (sp.Rational(1, 2), sp.Integer(2)):
    F = F_of(a)
    assert sp.simplify(F.T * Omega * F - Omega) == sp.zeros(12, 12)
    basis = commutant_sp(F)
    print(f'(b/c) a={a}: dim(commutant of F in sp(12,R)) =', len(basis))
    # stationary covariance for one mode: K with f K f^T = K, K > 0 (a=1/2 only)
    if a != 2:
        f = sp.Matrix([[0, 1], [-1, a]])
        k11, k12, k22 = sp.symbols('k11 k12 k22')
        K = sp.Matrix([[k11, k12], [k12, k22]])
        sol = sp.solve(list(f * K * f.T - K), [k12, k22], dict=True)[0]
        K = K.subs(sol).subs(k11, 1)
        C = sp.Matrix(sp.kronecker_product(K, Sigma))  # ordering: (u-block, v-block) x components
        assert sp.simplify(F * C * F.T - C) == sp.zeros(12, 12)
        cs = sp.symbols(f'c0:{len(basis)}')
        X = sum((c * B for c, B in zip(cs, basis)), sp.zeros(12, 12))
        eqs = list(X * C + C * X.T)
        A, _ = sp.linear_eq_to_matrix(eqs, list(cs))
        print(f'     stabilizer of stationary O-equivariant C inside that commutant: dim =', len(basis) - A.rank())
        # stabilizer if only the configuration-space O(6) acting as g (+) g is allowed
        Xo = sp.Matrix(6, 6, sp.symbols('o0:36'))
        Xb = sp.Matrix(sp.BlockMatrix([[Xo, Z6], [Z6, Xo]]))
        eqs = list(Xo + Xo.T) + list(Xb * C + C * Xb.T)
        A, _ = sp.linear_eq_to_matrix(eqs, list(Xo))
        print('     same, restricted to configuration-space o(6) acting diagonally: dim =', 36 - A.rank())
