"""Reviewer's exact generic checks for BRIDGE-UNIT1 r4 (REVIEW-UNIT1-r4.md).

Run under #1211 c.6739843458 ("Allow generic checks (as #1210)"). Generic mathematical objects
only: integers mod p, exact complex matrices with symbolic angles, F_2 rules on a six-cycle,
rational two-qubit matrices. No OI mechanism, no kernel object, no corpus rule or encoding.
Imports no earlier script. Exact arithmetic only. Controls on algebra stated in the review;
no verdict rests on them alone.

R1  B4 hand proof, every odd prime p <= 31 (wider than the writer's p <= 13):
    (a) existence of J in M_2(F_p), det J = 1, J^2 = -I, J f_a = f_a J iff 4 - a^2 is a
        nonzero square mod p;
    (b) proof steps: centralizer of f_a is F_p[f_a] (p^2 elements); a scalar root of -1 has
        det -1; every non-scalar root of -1 in F_p[f_a] has det 1 (the step the writer's
        hand proof leaves implicit);
    countercontrol: dropping det J = 1 changes the answer (scalar 2I at p = 5, a = 1).
R2  B2 refinement (the drive of phase-free richness versus the layer flow), symbolic theta:
    (a) exp(-i th X_ab) on n = 3, 4 states sends 1 to e^{-i th}(e_a + e_b) + sum_{c} e_c;
    (b) isolation form: exp(-i th X_ab) = e^{-i th} * G(2 th / pi) * diag(1, 1, e^{i th}) on
        three states, G the gate flow P_+ + e^{i pi t} P_- of the transposition (a b);
    (c) quarter turn: exp(-i pi/2 X_ab) * swap(a b) = -i * diag(1, 1, i), so its conjugation
        channel is that of the quarter phase on the third state; with the exchanges, the
        quarter phase on every state of a three-state level;
    (d) at th = pi/2 the drive is monomial and still moves the all-ones ray;
    (e) countercontrol: the real rotation exp(th (E_ab - E_ba)) moves the all-ones ray, is
        non-monomial and does not preserve diagonal states, yet the Lie algebra it generates
        with permutation transport is so(3) (dim 3), against su(3) (dim 8) for the X drive;
        and conjugation by any real matrix maps E_ac + E_ca to a real matrix while the quarter
        phase on c does not, so no word in real rotations and permutations gives that phase.
R3  n4 read pattern versus linearity on a six-cycle (a graph neither writer nor r3 reviewer
    used), over F_2, exhaustive: linear opposite-colour rule keeps the sector split; linear
    rule with one same-colour read breaks it.
R4  H-Bell bound (reviewer-supplied in r3): independent closed form CHSH = 6c - 4c^3 for the
    maximally entangled state at angles (0, 2al; al, -al), c = 4/5 gives 344/125, checked
    for every alpha (symbolic), and below the irrational Tsirelson value 2 sqrt 2.
"""
import itertools
import sympy as sp

ok = True


def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


# ------------------------------------------------------------------ R1
def mm(A, B, p):
    return ((A[0] * B[0] + A[1] * B[2]) % p, (A[0] * B[1] + A[1] * B[3]) % p,
            (A[2] * B[0] + A[3] * B[2]) % p, (A[2] * B[1] + A[3] * B[3]) % p)


def det(A, p):
    return (A[0] * A[3] - A[1] * A[2]) % p


def nzsq(x, p):
    x %= p
    return x != 0 and pow(x, (p - 1) // 2, p) == 1


PR = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
crit, cent_ok, scal_ok, nonscal_det_ok, n_pairs = True, True, True, True, 0
for p in PR:
    mI = (p - 1, 0, 0, p - 1)
    lam = [l for l in range(p) if (l * l + 1) % p == 0]
    for l in lam:  # scalar roots of -1 have det l^2 = -1 != 1
        scal_ok = scal_ok and det((l, 0, 0, l), p) == p - 1
    for a in range(p):
        f = (0, 1, p - 1, a)
        cen = [J for J in itertools.product(range(p), repeat=4) if mm(J, f, p) == mm(f, J, p)]
        alg = {((x + 0 * y) % p, y % p, (-y) % p, (x + a * y) % p) for x in range(p) for y in range(p)}
        cent_ok = cent_ok and set(cen) == alg and len(alg) == p * p
        roots = [J for J in cen if mm(J, J, p) == mI]
        nonscal = [J for J in roots if not (J[1] == 0 and J[2] == 0 and J[0] == J[3])]
        nonscal_det_ok = nonscal_det_ok and all(det(J, p) == 1 for J in nonscal)
        exists = any(det(J, p) == 1 for J in roots)
        crit = crit and (exists == nzsq(4 - a * a, p))
        n_pairs += 1
check(f"R1(a) criterion holds on all {n_pairs} pairs (p, a), odd p <= 31", crit)
check("R1(b) centralizer of f_a is F_p[f_a], p^2 elements, every pair", cent_ok)
check("R1(b) scalar roots of -1 have det -1 (excluded by det 1)", scal_ok)
check("R1(b) every non-scalar root of -1 commuting with f_a has det 1", nonscal_det_ok)
p, a = 5, 1
f = (0, 1, p - 1, a)
roots_any = [J for J in itertools.product(range(p), repeat=4)
             if mm(J, f, p) == mm(f, J, p) and mm(J, J, p) == (p - 1, 0, 0, p - 1)]
check("R1 countercontrol: without det 1, p=5 a=1 has a root (2I or 3I) though the criterion fails",
      len(roots_any) > 0 and all(det(J, p) != 1 for J in roots_any) and not nzsq(4 - a * a, p))

# ------------------------------------------------------------------ R2
th = sp.symbols('theta', real=True)


def Xab(n, a, b):
    X = sp.zeros(n)
    X[a, b] = X[b, a] = 1
    return X


def drive(n, a, b, t):
    X = Xab(n, a, b)
    assert X ** 3 == X
    return sp.eye(n) + (sp.exp(-sp.I * t) + sp.exp(sp.I * t) - 2) / 2 * X ** 2 \
        - sp.I * (sp.exp(sp.I * t) - sp.exp(-sp.I * t)) / (2 * sp.I) * X


def z(M):
    return all(sp.simplify(sp.expand(sp.sympify(x).rewrite(sp.exp))) == 0 for x in M)


for n in (3, 4):
    U = drive(n, 0, 1, th)
    target = sp.Matrix([sp.exp(-sp.I * th)] * 2 + [1] * (n - 2))
    check(f"R2(a) n={n}: drive sends 1 to e^(-i th)(e_a+e_b) + rest", z(U * sp.ones(n, 1) - target))
    check(f"R2(a) n={n}: drive is unitary for all theta", z(U.H * U - sp.eye(n)))

P = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
Pp, Pm = (sp.eye(3) + P) / 2, (sp.eye(3) - P) / 2


def G(t):
    return Pp + sp.exp(sp.I * sp.pi * t) * Pm


iso = sp.exp(-sp.I * th) * G(2 * th / sp.pi) * sp.diag(1, 1, sp.exp(sp.I * th))
check("R2(b) drive = e^(-i th) * gateflow(2th/pi) * diag(1,1,e^(i th)) (all theta)",
      z(drive(3, 0, 1, th) - iso))
check("R2(b) control: gate flow fixes the all-ones vector exactly (all theta)",
      z(G(2 * th / sp.pi) * sp.ones(3, 1) - sp.ones(3, 1)))

Q = drive(3, 0, 1, sp.pi / 2)
S = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
check("R2(c) drive(pi/2) * swap(a b) = -i * diag(1, 1, i)",
      sp.simplify(Q * S - (-sp.I) * sp.diag(1, 1, sp.I)) == sp.zeros(3))


def conj_channel_equal(V, W, n):
    for i, j in itertools.product(range(n), repeat=2):
        E = sp.zeros(n)
        E[i, j] = 1
        if sp.simplify(V * E * V.H - W * E * W.H) != sp.zeros(n):
            return False
    return True


check("R2(c) its conjugation channel equals the quarter phase's on the third state",
      conj_channel_equal(Q * S, sp.diag(1, 1, sp.I), 3))
perms = [sp.Matrix(3, 3, lambda i, j: 1 if s[j] == i else 0) for s in itertools.permutations(range(3))]
ph_ok = True
for c in range(3):
    target = sp.diag(*[sp.I if k == c else 1 for k in range(3)])
    ph_ok = ph_ok and any(conj_channel_equal(Pi * Q * S * Pi.T, target, 3) for Pi in perms)
check("R2(c) with permutation transport: quarter phase on every state of the level", ph_ok)


def is_monomial(M):
    M = sp.simplify(M)
    return all(sum(1 for x in M.row(i) if x != 0) == 1 for i in range(M.rows)) and \
        all(sum(1 for x in M.col(j) if x != 0) == 1 for j in range(M.cols))


v = sp.simplify(Q * sp.ones(3, 1))
check("R2(d) at theta=pi/2 the drive is monomial and moves the all-ones ray",
      is_monomial(Q) and sp.simplify(v[0] - v[2]) != 0)


def rot(n, a, b, t):
    A = sp.zeros(n)
    A[a, b], A[b, a] = -1, 1
    return sp.eye(n) + sp.sin(t) * A + (1 - sp.cos(t)) * A ** 2


R = rot(3, 0, 1, sp.pi / 4)
check("R2(e) real rotation is orthogonal at pi/4", sp.simplify(R.T * R - sp.eye(3)) == sp.zeros(3))
w = sp.simplify(R * sp.ones(3, 1))
D0 = sp.diag(1, 0, 0)
check("R2(e) real rotation at pi/4: non-monomial, moves the all-ones ray, mixes a diagonal state",
      (not is_monomial(R)) and sp.simplify(w[0] - w[2]) != 0
      and any(sp.simplify((R * D0 * R.T)[i, j]) != 0 for i in range(3) for j in range(3) if i != j))


def lie_dim(gens):
    def vec(M):
        return [sp.re(x) for x in M] + [sp.im(x) for x in M]
    basis = []

    def rank(ms):
        return sp.Matrix([vec(m) for m in ms]).rank() if ms else 0
    for g in gens:
        if rank(basis + [g]) > rank(basis):
            basis.append(g)
    changed = True
    while changed:
        changed = False
        for A_, B_ in itertools.combinations(list(basis), 2):
            Cm = sp.expand(A_ * B_ - B_ * A_)
            if rank(basis + [Cm]) > rank(basis):
                basis.append(Cm)
                changed = True
    return len(basis)


def transported(M):
    return [sp.expand(Pi * M * Pi.T) for Pi in perms]


Xg = transported(sp.I * Xab(3, 0, 1))
Ag = transported(sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]))
dX, dA = lie_dim(Xg), lie_dim(Ag)
check(f"R2(e) Lie algebra with permutation transport: X drive dim {dX} (su(3)=8), "
      f"real rotation dim {dA} (so(3)=3)", dX == 8 and dA == 3)
Ers = sp.zeros(3)
Ers[0, 2] = Ers[2, 0] = 1
Dq = sp.diag(1, 1, sp.I)
img = sp.simplify(Dq * Ers * Dq.H)
check("R2(e) the quarter phase on c sends E_ac + E_ca to a non-real matrix "
      "(real conjugations keep it real)", any(sp.im(x) != 0 for x in img))

# ------------------------------------------------------------------ R3
VC = list(range(6))  # six-cycle, colours i % 2
nbr = {i: [(i - 1) % 6, (i + 1) % 6] for i in VC}
chi = {i: i % 2 for i in VC}


def g_opp(i, u):
    return u[nbr[i][0]] ^ u[nbr[i][1]]


def g_same(i, u):
    return g_opp(i, u) ^ (u[(i + 2) % 6] if i == 0 else 0)


VARS = [('u', i) for i in VC] + [('v', i) for i in VC]
typ = {('u', i): chi[i] for i in VC}
typ.update({('v', i): (chi[i] + 1) % 2 for i in VC})


def run(g, init, T):
    u = {i: init[('u', i)] for i in VC}
    vv = {i: init[('v', i)] for i in VC}
    out = []
    for _ in range(T):
        un = {i: g(i, u) ^ vv[i] for i in VC}
        vv, u = u, un
        out.append(dict(u))
    return out


def split(g, T=4):
    cfgs = list(itertools.product((0, 1), repeat=12))
    tab = {c: run(g, dict(zip(VARS, c)), T) for c in cfgs}
    for c in cfgs:
        for k in range(12):
            c2 = list(c)
            c2[k] ^= 1
            h1, h2 = tab[c], tab[tuple(c2)]
            for t in range(T):
                for i in VC:
                    if h1[t][i] != h2[t][i] and typ[VARS[k]] != (t + 1 + chi[i]) % 2:
                        return False
    return True


check("R3 control: linear opposite-colour rule on C6 keeps the split", split(g_opp))
check("R3 linear rule with one same-colour read on C6 breaks the split", not split(g_same))

# ------------------------------------------------------------------ R4
al = sp.symbols('alpha', real=True)


def corr(t1, t2):
    Z = sp.Matrix([[1, 0], [0, -1]])
    X = sp.Matrix([[0, 1], [1, 0]])
    A = sp.cos(t1) * Z + sp.sin(t1) * X
    B = sp.cos(t2) * Z + sp.sin(t2) * X
    phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    return sp.simplify((phi.T * sp.kronecker_product(A, B) * phi)[0])


chsh = sp.simplify(corr(0, al) + corr(0, -al) + corr(2 * al, al) - corr(2 * al, -al))
cc = sp.symbols('c')
check("R4 CHSH(alpha) = 6 cos(alpha) - 4 cos(alpha)^3 (exact, all alpha)",
      sp.simplify(sp.expand_trig(chsh) - (6 * sp.cos(al) - 4 * sp.cos(al) ** 3)) == 0)
val = (6 * cc - 4 * cc ** 3).subs(cc, sp.Rational(4, 5))
check("R4 at cos(alpha) = 4/5: CHSH = 344/125 > 2", val == sp.Rational(344, 125) and val > 2)
check("R4 the Tsirelson value 2*sqrt(2) is irrational and exceeds 344/125",
      (2 * sp.sqrt(2)).is_rational is False and 2 * sp.sqrt(2) > sp.Rational(344, 125))

print("ALL PASS" if ok else "SOME FAIL")
