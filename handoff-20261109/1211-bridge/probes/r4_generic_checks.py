"""EXACT GENERIC CHECKS FOR BRIDGE-UNIT1 r4 (generic mathematical objects only).

Run under the owner's permission in #1211 c.6739843458 ("Allow generic checks (as #1210)").
Labelled controls on algebra stated in the r4 text or its dispositions; not evidence for any
physical result. No OI mechanism is run: no cubic lattice, no ring rule of the corpus, no
encoding of the corpus, no kernel object. Imports no earlier script. Exact arithmetic only
(Python integers mod p, F_2, sympy exact numbers).

J   B4 (NQ1 scope guard). Over F_p, p in {3,5,7,11,13}:
    (a) J0 = [[0,-1],[1,0]] has J0^2 = -I for every p, so "a J with J^2 = -1 exists over Z_q
        only where -1 is a square" is false as stated;
    (b) for the mode map f_a = [[0,1],[-1,a]], every J in M_2(F_p) with J^2 = -I, J f_a = f_a J
        and det J = 1 is enumerated; existence is compared with "4 - a^2 is a nonzero square
        mod p" (the reviewer's criterion; proved by hand in the r4 dispositions) and with
        "-1 is a square mod p" (the r3 guard);
    countercontrol: none exists at the null modes a = +-2.
D   B2 (phase versus mixing form). Exact 3x3 and 2x2 complex matrices; the drive is written
    in closed form, exp(-i t X) = I + (cos t - 1) X^2 - i sin t X, using X^3 = X (asserted).
    (a) the driven transition exp(-i t X_ab) at t = pi/4 on three states is unitary,
        non-monomial, and moves the all-ones ray;
    (b) control: on two states the same drive keeps the all-ones vector on its ray;
    (c) the gate flow P_+ + e^{i pi t} P_- of an involution with a moved point (swap of two of
        three states) at t = 1/2 is unitary, non-monomial, and keeps the all-ones vector on
        its ray, as it does at every t in a sample of rational times.
L   n4 (read pattern versus linearity). A fixed bipartite graph K_{2,4} (colour 0: a0,a1;
    colour 1: b0..b3), second-order rule over F_2, u_i(t+1) = g_i(reads) + v_i(t),
    v_i(t+1) = u_i(t); types: u_i(0) has type chi_i, v_i(0) type chi_i + 1. Split: u_i(t)
    depends only on initial variables of type t + chi_i (mod 2). Exhaustive over 2^12 initial
    configurations, t = 1..4.
    (i) control: LINEAR rule, opposite-colour reads only: split holds;
    (ii) LINEAR rule with one same-colour read (a0 also reads a1): split fails.
B   H-Bell exactness bound (REVIEWER-SUPPLIED; re-checked here, computation-supported).
    (a) maximally entangled two-qubit state, measurement directions in the x-z plane at
        angles 0, 2al (one wing) and al, -al (other wing), cos al = 4/5, sin al = 3/5: all 16
        joint probabilities rational, normalized, no-signalling, CHSH = 344/125 > 2;
    (b) the Tsirelson-point value P(a = b) = (2 + sqrt 2)/4 is irrational.
"""
import itertools
import sympy as sp

ok = True


def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


# ---------------- J ----------------
def mat_mul(A, B, p):
    return [[(A[i][0] * B[0][j] + A[i][1] * B[1][j]) % p for j in range(2)] for i in range(2)]


def is_square_nonzero(x, p):
    x %= p
    return x != 0 and any((y * y) % p == x for y in range(1, p))


PRIMES = [3, 5, 7, 11, 13]
for p in PRIMES:
    J0 = [[0, p - 1], [1, 0]]
    check(f"J(a) p={p}: J0^2 = -I (-1 a square mod p: {is_square_nonzero(-1, p)})",
          mat_mul(J0, J0, p) == [[p - 1, 0], [0, p - 1]])

crit_ok, guard_mismatch, null_ok, total = True, [], True, 0
for p in PRIMES:
    minusI = [[p - 1, 0], [0, p - 1]]
    for a in range(p):
        f = [[0, 1], [p - 1, a]]
        count = 0
        for e in itertools.product(range(p), repeat=4):
            J = [[e[0], e[1]], [e[2], e[3]]]
            if (e[0] * e[3] - e[1] * e[2]) % p != 1:
                continue
            if mat_mul(J, J, p) != minusI:
                continue
            if mat_mul(J, f, p) != mat_mul(f, J, p):
                continue
            count += 1
        total += 1
        exists = count > 0
        if exists != is_square_nonzero(4 - a * a, p):
            crit_ok = False
        if exists != is_square_nonzero(-1, p):
            guard_mismatch.append((p, a, count))
        if a in (2 % p, (-2) % p) and exists:
            null_ok = False
check("J(b) symplectic commuting J exists iff 4 - a^2 is a nonzero square mod p (all pairs)", crit_ok)
check("J(b) the r3 guard ('-1 a square') disagrees with existence on some pairs", len(guard_mismatch) > 0)
check("J countercontrol: no symplectic commuting J at the null modes a = +-2", null_ok)
print(f"     J(b) pairs (p, a): {total}; pairs contradicting the r3 guard: {len(guard_mismatch)};"
      f" first: {guard_mismatch[:6]}")


# ---------------- D ----------------
def monomial(M):
    return all(sum(1 for x in M.row(i) if sp.simplify(x) != 0) == 1 for i in range(M.rows)) and \
        all(sum(1 for x in M.col(j) if sp.simplify(x) != 0) == 1 for j in range(M.cols))


def keeps_ones_ray(M):
    v = M * sp.ones(M.rows, 1)
    return all(sp.simplify(v[i] - v[0]) == 0 for i in range(M.rows))


def unitary(M):
    return sp.expand_complex(sp.simplify(M.H * M - sp.eye(M.rows))) == sp.zeros(M.rows)


def drive(n, a, b, t):
    # exp(-i t X) = I + (cos t - 1) X^2 - i sin t X, valid because X^3 = X (X the transition
    # matrix on the pair {a, b}, X^2 the projector on that pair); X^3 = X is checked below.
    X = sp.zeros(n)
    X[a, b] = 1
    X[b, a] = 1
    assert X ** 3 == X
    return sp.expand_complex(sp.eye(n) + (sp.cos(t) - 1) * X ** 2 - sp.I * sp.sin(t) * X)


U3 = drive(3, 0, 1, sp.pi / 4)
check("D(a) drive on 3 states at t=pi/4: unitary", unitary(U3))
check("D(a) drive on 3 states at t=pi/4: non-monomial", not monomial(U3))
check("D(a) drive on 3 states at t=pi/4: moves the all-ones ray", not keeps_ones_ray(U3))
U2 = drive(2, 0, 1, sp.pi / 4)
check("D(b) control: drive on 2 states at t=pi/4 is non-monomial and keeps the all-ones ray",
      unitary(U2) and (not monomial(U2)) and keeps_ones_ray(U2))

P = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
Pp, Pm = (sp.eye(3) + P) / 2, (sp.eye(3) - P) / 2


def gate_flow(t):
    return sp.simplify(Pp + sp.exp(sp.I * sp.pi * t) * Pm)


G = gate_flow(sp.Rational(1, 2))
check("D(c) gate flow at t=1: equals the involution", sp.simplify(gate_flow(1) - P) == sp.zeros(3))
check("D(c) gate flow at t=1/2: unitary, non-monomial, keeps the all-ones ray",
      unitary(G) and (not monomial(G)) and keeps_ones_ray(G))
check("D(c) gate flow keeps the all-ones ray at t in {1/7, 1/3, 2/5, 3/4, 5/6}",
      all(keeps_ones_ray(gate_flow(sp.Rational(k))) for k in ('1/7', '1/3', '2/5', '3/4', '5/6')))


# ---------------- L ----------------
VL = ['a0', 'a1', 'b0', 'b1', 'b2', 'b3']
chiL = {'a0': 0, 'a1': 0, 'b0': 1, 'b1': 1, 'b2': 1, 'b3': 1}
nbrL = {'a0': ['b0', 'b1', 'b2', 'b3'], 'a1': ['b0', 'b1', 'b2', 'b3'],
        'b0': ['a0', 'a1'], 'b1': ['a0', 'a1'], 'b2': ['a0', 'a1'], 'b3': ['a0', 'a1']}


def g_lin(x, u):
    s = 0
    for y in nbrL[x]:
        s ^= u[y]
    return s


def g_lin_same(x, u):
    return g_lin(x, u) ^ (u['a1'] if x == 'a0' else 0)


VARSL = [('u', x) for x in VL] + [('v', x) for x in VL]
vtypeL = {('u', x): chiL[x] for x in VL}
vtypeL.update({('v', x): (chiL[x] + 1) % 2 for x in VL})


def runL(g, init, T):
    u = {x: init[('u', x)] for x in VL}
    v = {x: init[('v', x)] for x in VL}
    hist = []
    for _ in range(T):
        un = {x: g(x, u) ^ v[x] for x in VL}
        v, u = u, un
        hist.append(dict(u))
    return hist


def split_holds(g, T=4):
    configs = list(itertools.product((0, 1), repeat=len(VARSL)))
    table = {c: runL(g, dict(zip(VARSL, c)), T) for c in configs}
    for c in configs:
        for k in range(len(VARSL)):
            c2 = list(c)
            c2[k] ^= 1
            h1, h2 = table[c], table[tuple(c2)]
            for t in range(T):
                for x in VL:
                    if h1[t][x] != h2[t][x] and vtypeL[VARSL[k]] != (t + 1 + chiL[x]) % 2:
                        return False
    return True


check("L(i) control: linear rule, opposite-colour reads only: split holds", split_holds(g_lin))
check("L(ii) linear rule with one same-colour read: split fails", not split_holds(g_lin_same))


# ---------------- B ----------------
c, s = sp.Rational(4, 5), sp.Rational(3, 5)


def proj(cos_t, sin_t, out):
    Z = sp.Matrix([[1, 0], [0, -1]])
    X = sp.Matrix([[0, 1], [1, 0]])
    return (sp.eye(2) + out * (cos_t * Z + sin_t * X)) / 2


cos2, sin2 = c * c - s * s, 2 * s * c
alice = [(sp.Integer(1), sp.Integer(0)), (cos2, sin2)]
bob = [(c, s), (c, -s)]
phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
rho = phi * phi.T
probs = {}
for x, y in itertools.product(range(2), repeat=2):
    for a, b in itertools.product((1, -1), repeat=2):
        M = sp.kronecker_product(proj(*alice[x], a), proj(*bob[y], b))
        probs[(x, y, a, b)] = sp.nsimplify(sp.simplify((rho * M).trace()))
check("B(a) all 16 joint probabilities rational", all(v.is_Rational for v in probs.values()))
check("B(a) normalized per setting pair",
      all(sum(probs[(x, y, a, b)] for a in (1, -1) for b in (1, -1)) == 1
          for x in range(2) for y in range(2)))
nosig = all(sum(probs[(x, y, a, b)] for b in (1, -1)) == sum(probs[(x, 1 - y, a, b)] for b in (1, -1))
            for x in range(2) for y in range(2) for a in (1, -1)) and \
    all(sum(probs[(x, y, a, b)] for a in (1, -1)) == sum(probs[(1 - x, y, a, b)] for a in (1, -1))
        for x in range(2) for y in range(2) for b in (1, -1))
check("B(a) no-signalling", nosig)
E = {(x, y): sum(a * b * probs[(x, y, a, b)] for a in (1, -1) for b in (1, -1))
     for x in range(2) for y in range(2)}
chsh = E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]
check("B(a) CHSH = 344/125 > 2 (exact)", chsh == sp.Rational(344, 125) and chsh > 2)
check("B(b) (2 + sqrt 2)/4 is irrational", ((2 + sp.sqrt(2)) / 4).is_rational is False)

print("ALL PASS" if ok else "SOME FAIL")
