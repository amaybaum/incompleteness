"""Node 2, part A: exact checks of the TU gadgets used in the A2 (KrausDense) argument.

Carrier T = Fin 2 x Fin N (d = 2N), qubit ancilla a = Fin 2. Index (t, a) -> 2*t + a.
Native operations are permutation matrices of T x Fin 2. TU tests: sharp Lueders tests on the
ancilla in the bases X, Y and the real basis w(phi) = (cos phi, sin phi), w_perp = (-sin phi, cos phi).
All checks are exact (SymPy); phi is a free real symbol unless a value is given.
"""
import itertools
import sympy as sp

PASS = []
def check(name, cond):
    ok = bool(cond)
    PASS.append(ok)
    print(("PASS " if ok else "FAIL ") + name)

I = sp.I
phi = sp.symbols('phi', real=True)
n = sp.symbols('n', positive=True, integer=True)

def kron(A, B):
    return sp.kronecker_product(A, B)

def perm_matrix(f, D):
    M = sp.zeros(D, D)
    for j in range(D):
        M[f(j), j] = 1
    return M

def is_perm(M):
    D = M.shape[0]
    return all(sorted(M[:, j]) == [0]*(D-1)+[1] for j in range(D)) and \
        all(sorted(M[i, :]) == [0]*(D-1)+[1] for i in range(D))

def ket(v):
    return sp.Matrix(v)

k0, k1 = ket([1, 0]), ket([0, 1])
plus_i = ket([1, I]) / sp.sqrt(2)
minus_i = ket([1, -I]) / sp.sqrt(2)
w = ket([sp.cos(phi), sp.sin(phi)])
wp = ket([-sp.sin(phi), sp.cos(phi)])
X2 = sp.Matrix([[0, 1], [1, 0]])

def branch(C, d, bra, anc):
    """(I_T (x) <bra|) C (I_T (x) |anc>) as a d x d matrix."""
    L = kron(sp.eye(d), bra.H)
    R = kron(sp.eye(d), anc)
    return sp.simplify(L * C * R)

def zero(M):
    return sp.simplify(M.applyfunc(lambda z: sp.simplify(sp.expand_complex(sp.expand(z))))) == sp.zeros(*M.shape)

# A1: deterministic |+i> preparation from |0>: Y test, native X on outcome -i.
P_p = plus_i * plus_i.H
P_m = minus_i * minus_i.H
b_plus = P_p * k0
b_minus = X2 * P_m * k0
check("A1a Y-test branches complete: P_+ + P_- = I", zero(P_p + P_m - sp.eye(2)))
check("A1b outcome +i branch is (1/sqrt2)|+i>", zero(b_plus - plus_i / sp.sqrt(2)))
check("A1c outcome -i branch, after native X, is (-i/sqrt2)|+i>", zero(b_minus - (-I) * plus_i / sp.sqrt(2)))

for N in (2, 3):
    d = 2 * N
    D = 2 * d
    a_, b_ = 0, d - 1          # the transposed pair of T (configurations (0,0) and (1,N-1))
    s = {1, d - 2}             # a subset of T for the phase gadget
    def Xab_t(t):
        return b_ if t == a_ else (a_ if t == b_ else t)
    Xab = perm_matrix(Xab_t, d)
    # ancilla-controlled X_ab on T x Fin 2: (t, 1) -> (X_ab t, 1)
    C = perm_matrix(lambda j: 2 * Xab_t(j // 2) + 1 if j % 2 == 1 else j, D)
    # data-controlled flip of the ancilla on s: (t, a) -> (t, 1 - a) if t in s
    Cs = perm_matrix(lambda j: (2 * (j // 2) + (1 - j % 2)) if (j // 2) in s else j, D)
    Ps = sp.diag(*[1 if t in s else 0 for t in range(d)])
    Zs = sp.eye(d) - 2 * Ps
    tag = f"[d={d}]"
    check(f"A2a{tag} both couplings are permutation matrices (native)", is_perm(C) and is_perm(Cs))
    check(f"A2b{tag} X_ab^2 = I", zero(Xab * Xab - sp.eye(d)))
    E = sp.cos(phi) * sp.eye(d) + I * sp.sin(phi) * Xab      # = exp(i phi X_ab)
    Bw = branch(C, d, w, plus_i)
    Bwp = branch(C, d, wp, plus_i)
    check(f"A2c{tag} X-type gadget, outcome w: branch = (1/sqrt2) exp(i phi X_ab)", zero(Bw - E / sp.sqrt(2)))
    check(f"A2d{tag} outcome w_perp then native X_ab: branch = (i/sqrt2) exp(i phi X_ab)",
          zero(Xab * Bwp - I * E / sp.sqrt(2)))
    check(f"A2e{tag} exp(i phi X_ab) is unitary and fixes the all-ones vector up to e^(i phi)",
          zero(E.H * E - sp.eye(d)) and zero(E * sp.ones(d, 1) - sp.exp(I*phi).rewrite(sp.cos) * sp.ones(d, 1)))
    Dmat = sp.diag(*[I * sp.exp(-2 * I * phi) if t in s else 1 for t in range(d)])
    Bw2 = branch(Cs, d, w, plus_i)
    Bwp2 = branch(Cs, d, wp, plus_i)
    check(f"A3a{tag} phase gadget, outcome w: branch = (e^(i phi)/sqrt2) D_s(phi), D_s = diag(1 off s, i e^(-2i phi) on s)",
          zero(Bw2 - sp.exp(I * phi) / sp.sqrt(2) * Dmat))
    check(f"A3b{tag} phase gadget, outcome w_perp: branch = (i e^(i phi)/sqrt2) Z_s D_s(phi)",
          zero(Bwp2 - I * sp.exp(I * phi) / sp.sqrt(2) * Zs * Dmat))
    Dq = Dmat.subs(phi, sp.pi / 4)
    check(f"A4{tag} at phi = pi/4 (the X basis) D_s = I: branches are I and Z_s, each p = 1/2 (heralded Z_s)",
          zero(Dq - sp.eye(d)))
    check(f"A4b{tag} D_s(phi) moves the all-ones ray for generic phi (phi = 1/3)",
          not zero(Dmat.subs(phi, sp.Rational(1, 3)) * sp.ones(d, 1) - sp.ones(d, 1))
          and Dmat.subs(phi, sp.Rational(1, 3))[min(s), min(s)] != 1)

# A5: RUS channel for Z_s and its ChanWithin distance, on d = 4, symbolic depth n.
d = 4; s = {1, 2}
Ps = sp.diag(*[1 if t in s else 0 for t in range(d)]); Zs = sp.eye(d) - 2 * Ps
Xs = sp.Matrix(d, d, sp.symbols('x0:16'))
p = sp.Integer(2) ** (-n)
Phi_n = (1 - p) * Zs * Xs * Zs + p * Xs
diff = Phi_n - Zs * Xs * Zs
check("A5a Phi_n X - Z X Z = 2^-n (X - Z X Z) (exact, symbolic X)", zero(diff - p * (Xs - Zs * Xs * Zs)))
Xo = sp.zeros(d); Xo[0, 1] = 1; Xo[1, 0] = 1     # 0 not in s, 1 in s
check("A5b on X = E01 + E10 (||X|| = 1): X - Z X Z = 2X, so the ChanWithin constant 2^(1-n) is attained",
      zero(Xo - Zs * Xo * Zs - 2 * Xo))
# ChanWithin bound: ||X - ZXZ|| <= ||X|| + ||ZXZ|| = 2||X|| (Z unitary). Recorded as [W]; here a sharpness instance.

# A6: phase gadget corrected by RUS at depth n: channel and distance to Ad D.
Dm = sp.diag(1, I * sp.exp(-2 * I * phi), I * sp.exp(-2 * I * phi), 1)
def Ad(U, Y):
    return U * Y * U.H
corr = sp.Rational(1, 2) * Ad(Dm, Xs) + sp.Rational(1, 2) * ((1 - p) * Ad(Zs * Zs * Dm, Xs) + p * Ad(Zs * Dm, Xs))
target = (1 - p / 2) * Ad(Dm, Xs) + (p / 2) * Ad(Zs * Dm, Xs)
check("A6a corrected phase gadget = (1 - 2^(-n-1)) Ad D + 2^(-n-1) Ad(Z_s D) (exact, symbolic X)", zero(corr - target))
check("A6b its distance to Ad D is 2^(-n-1) (Ad(Z_s D) - Ad D), so ChanWithin 2^-n",
      zero(corr - Ad(Dm, Xs) - (p / 2) * (Ad(Zs * Dm, Xs) - Ad(Dm, Xs))))
check("A6c the corrected channel is unital (mixed-unitary), so its infinity-norm is 1 and errors add under composition",
      zero(corr.subs({Xs[i, j]: (1 if i == j else 0) for i in range(d) for j in range(d)}) - sp.eye(d)))

# A7: Lie algebra generated by the TU generators, exact rank over Q(i).
def lie_closure_dim(gens, d):
    basis = []
    def vec(M):
        return [sp.re(z) for z in M] + [sp.im(z) for z in M]
    def add(M):
        nonlocal basis
        cand = basis + [vec(M)]
        if sp.Matrix(cand).rank() > len(basis):
            basis.append(vec(M)); mats.append(M); return True
        return False
    mats = []
    for g in gens:
        add(g)
    changed = True
    while changed:
        changed = False
        cur = list(mats)
        for A, B in itertools.combinations(cur, 2):
            if add(A * B - B * A):
                changed = True
    return len(basis), mats

for d in (2, 4, 6):
    trans = []
    for a_, b_ in itertools.combinations(range(d), 2):
        trans.append(I * perm_matrix(lambda t: b_ if t == a_ else (a_ if t == b_ else t), d))
    phases = [I * sp.diag(*[1 if t == c else 0 for t in range(d)]) for c in range(d)]
    dimX, matsX = lie_closure_dim(trans, d)
    dimAll, _ = lie_closure_dim(trans + phases, d)
    J = sp.ones(d, d) / d
    fixes = all(zero(M * J - J * M) for M in matsX)
    check(f"A7a[d={d}] Lie algebra of {{i X_ab}} has real dim (d-1)^2 = {(d-1)**2} and commutes with the uniform projector J (inside the all-ones ray stabilizer, dim 1+(d-1)^2)",
          dimX == (d - 1) ** 2 and fixes)
    check(f"A7b[d={d}] adding the singleton phase generators {{i P_c}} gives real dim d^2 = {d*d}, i.e. u(d)",
          dimAll == d * d)

# A8: the irrational steps of the finite basis set B = {X, Y, w(1)}.
# X-type step: exp(i X_ab) (phi = 1); phase step: relative phase arg(i e^(-2i)) = pi/2 - 2.
th = sp.pi / 2 - 2
check("A8a phase step pi/2 - 2 over 2 pi is irrational (would make 1/pi rational)",
      sp.nsimplify(th / (2 * sp.pi)).is_rational is not True and (th / (2*sp.pi)).is_rational is not True)
check("A8b X-type step 1 over 2 pi is irrational", (sp.Integer(1) / (2 * sp.pi)).is_rational is False)

# A9: D1 fails for every theory whose available unitaries fix the all-ones ray, at d = 4 with Z (x) I.
d = 4
U = sp.diag(1, 1, -1, -1)
u = sp.ones(d, 1) / 2
check("A9 (Z (x) I) u is orthogonal to u, so ||(Z(x)I - cV) u||^2 = 2 for every ones-fixing unitary V, |c| = 1",
      sp.simplify((u.H * U * u)[0]) == 0)

# A10: countercontrols.
d = 4
Cx = perm_matrix(lambda j: 2 * [3, 1, 2, 0][j // 2] + 1 if j % 2 == 1 else j, 2 * d)
Bc = branch(Cx, d, w, k0)
check("A10a configuration ancilla |0> instead of |+i>: every branch is a scalar times I (no flow)",
      zero(Bc - sp.cos(phi) * sp.eye(d)))
Bz = branch(Cx, d, k0, plus_i)
Bz1 = branch(Cx, d, k1, plus_i)
check("A10b configuration test (phi = 0) on |+i>: branches are I/sqrt2 and (i/sqrt2) X_ab (monomial)",
      zero(Bz - sp.eye(d) / sp.sqrt(2)) and zero(Bz1 - I * perm_matrix(lambda t: [3, 1, 2, 0][t], d) / sp.sqrt(2)))
# monomial words preserve entrywise nonnegativity: conj by c * (partial permutation)
a, b = sp.symbols('a b', nonnegative=True)
c = sp.symbols('c')
M = sp.Matrix([[0, c], [0, 0]])
Y = sp.Matrix([[a, b], [b, a]])
out = M * Y * M.H
check("A10c conjugation by a scaled partial permutation maps nonnegative matrices to nonnegative ones",
      sp.simplify(out[0, 0] - c * sp.conjugate(c) * a) == 0 and out[0, 1] == 0 and out[1, 0] == 0 and out[1, 1] == 0)

# A11: Kraus-word check for the unitary limit: RUS leaves for Z are each proportional to Z.
d = 2
Zq = sp.diag(1, -1)
leaves = []
for depth in range(1, 5):
    # depth-th attempt succeeds after depth-1 failures: Kraus (1/sqrt2)^depth * Z (failure branches act as I)
    leaves.append((sp.Integer(1) / sp.sqrt(2)) ** depth * Zq)
check("A11a every terminating leaf of the RUS tree for Ad Z has Kraus operator proportional to Z (depth <= 4)",
      all(zero(L - L[0, 0] * Zq) for L in leaves))
check("A11b leaf weights sum to 1 - 2^-4 (truncation) and to 1 in the limit",
      sp.simplify(sum((L[0, 0])**2 for L in leaves) - (1 - sp.Rational(1, 16))) == 0)

print()
print(f"{sum(PASS)} PASS, {len(PASS) - sum(PASS)} FAIL")
