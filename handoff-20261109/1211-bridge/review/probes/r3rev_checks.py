"""REVIEWER'S EXACT GENERIC CHECKS FOR BRIDGE-UNIT1 r3 (generic mathematical objects only).

Run under the owner's permission in #1211 c.6739843458 ("Allow generic checks (as #1210)").
Controls on algebra stated in the r3 text or in this review; not evidence for any physical
result. No OI mechanism is run: no cubic lattice, no ring rule of the corpus, no encoding of the
corpus, no kernel object. Imports no earlier script. Exact arithmetic only.

R1  NQ1 / §5.2 scope guard ("over Z_q a J with J^2 = -1 exists only where -1 is a square").
    Over F_p, p in {3,5,7,11,13}: (a) J0 = [[0,-1],[1,0]] satisfies J0^2 = -I for every p,
    including p with -1 a non-square; (b) for the 2x2 mode map f_a = [[0,1],[-1,a]], enumerate
    every J in M_2(F_p) with J^2 = -I and Jf = fJ, and every such J with det J = 1 (symplectic
    on F_p^2); compare existence with "-1 is a square mod p". Countercontrol: at the null modes
    a = +-2 no symplectic commuting J exists (enumerated).
R2  §10 claim (a), isolating the read pattern from nonlinearity. Graph K_{2,3} (colour 0: A0,A1;
    colour 1: B0,B1,B2), second-order rule over F_2, u_i(t+1) = g_i(reads) + v_i(t),
    v_i(t+1) = u_i(t). Exhaustive over 2^10 initial configurations, t = 1..4.
    (i) nonlinear, opposite-colour reads only: split holds;
    (ii) LINEAR rule with one same-colour read: split fails;
    (iii) nonlinear rule with the same same-colour read: split fails;
    (iv) linear, opposite-colour reads only: split holds (control).
R3  G2 step 3 needs affinity, not linearity: over F_2^3, for an affine map F,
    F(y + c e) - F(y) is independent of y; for a non-affine F (AND) it is not (countercontrol).
R4  H-Bell exact vs finite accuracy (review, generic). (a) Maximally entangled two-qubit state,
    measurement directions in the x-z plane at angles 0, 2al (Alice) and al, -al (Bob), with
    cos al = 4/5, sin al = 3/5: all 16 joint probabilities are rational, no-signalling holds,
    CHSH = 344/125 > 2 (exact). (b) At the Tsirelson angles, P(a = b) = (2 + sqrt 2)/4 is
    irrational, so no law whose probabilities are ratios of counts (counting measure on a finite
    set) equals it.
R5  §5.2 arrow 3 (review B2): on three states, a driven transition at angle pi/4 is non-monomial
    and moves the all-ones ray; the exchange's gate flow at time 1/2 is non-monomial and fixes it.
"""
import itertools
from fractions import Fraction
import sympy as sp

ok = True


def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


# ---------------- R1 ----------------
def mat_mul(A, B, p):
    return ((A[0] * B[0] + A[1] * B[2]) % p, (A[0] * B[1] + A[1] * B[3]) % p,
            (A[2] * B[0] + A[3] * B[2]) % p, (A[2] * B[1] + A[3] * B[3]) % p)


def minus_one_square(p):
    return any((x * x) % p == p - 1 for x in range(p))


for p in (3, 5, 7, 11, 13):
    negI = (p - 1, 0, 0, p - 1)
    J0 = (0, p - 1, 1, 0)
    check(f"R1(a) p={p}: J0^2 = -I (-1 square mod p: {minus_one_square(p)})",
          mat_mul(J0, J0, p) == negI)

mismatch = []
null_ok = True
rows = []
for p in (3, 5, 7, 11, 13):
    negI = (p - 1, 0, 0, p - 1)
    for a in range(p):
        f = (0, 1, p - 1, a)
        com, sym = 0, 0
        for J in itertools.product(range(p), repeat=4):
            if mat_mul(J, J, p) == negI and mat_mul(J, f, p) == mat_mul(f, J, p):
                com += 1
                if (J[0] * J[3] - J[1] * J[2]) % p == 1:
                    sym += 1
        rows.append((p, a, com, sym))
        if (sym > 0) != minus_one_square(p):
            mismatch.append((p, a, sym))
        if a in (2 % p, (p - 2) % p) and sym != 0:
            null_ok = False
check("R1(b) symplectic J commuting with f_a exists where -1 is a non-square (e.g. p=3, a=0)",
      any(p == 3 and a == 0 and s > 0 for (p, a, c, s) in rows))
check("R1(b) existence of a symplectic commuting J is not equivalent to '-1 is a square mod p'",
      len(mismatch) > 0)
# record the actual criterion: symplectic commuting J exists iff 4 - a^2 is a nonzero square mod p
crit = all((s > 0) == (((4 - a * a) % p != 0) and any((x * x) % p == (4 - a * a) % p
                                                         for x in range(1, p)))
           for (p, a, c, s) in rows)
check("R1(b) observed criterion: symplectic commuting J exists iff 4 - a^2 is a nonzero square mod p",
      crit)
check("R1 countercontrol: no symplectic commuting J at the null modes a = +-2", null_ok)
print("     R1 mismatches (p, a, #symplectic J):", mismatch[:8], "... total", len(mismatch))

# ---------------- R2 ----------------
V = ['A0', 'A1', 'B0', 'B1', 'B2']
chi = {'A0': 0, 'A1': 0, 'B0': 1, 'B1': 1, 'B2': 1}
opp = {x: [y for y in V if chi[y] != chi[x]] for x in V}  # K_{2,3}: all opposite pairs


def g_nl(x, u):
    n = [u[y] for y in opp[x]]
    if chi[x] == 0:            # three opposite reads
        return (n[0] & n[1]) | n[2]
    return n[0] & n[1]         # two opposite reads


def g_lin(x, u):
    s = 0
    for y in opp[x]:
        s ^= u[y]
    return s


def g_lin_same(x, u):          # linear, plus one same-colour read at A0
    return g_lin(x, u) ^ (u['A1'] if x == 'A0' else 0)


def g_nl_same(x, u):           # nonlinear, plus the same same-colour read at A0
    return g_nl(x, u) ^ (u['A1'] if x == 'A0' else 0)


VARS = [('u', x) for x in V] + [('v', x) for x in V]
vtype = {('u', x): chi[x] for x in V}
vtype.update({('v', x): (chi[x] + 1) % 2 for x in V})


def run(g, init, T):
    u = {x: init[('u', x)] for x in V}
    v = {x: init[('v', x)] for x in V}
    hist = []
    for _ in range(T):
        un = {x: g(x, u) ^ v[x] for x in V}
        v, u = u, un
        hist.append(dict(u))
    return hist


def deps(g, T):
    D = {(t, x): set() for t in range(1, T + 1) for x in V}
    confs = list(itertools.product((0, 1), repeat=len(VARS)))
    tab = {c: run(g, dict(zip(VARS, c)), T) for c in confs}
    for c in confs:
        for k in range(len(VARS)):
            c2 = list(c)
            c2[k] ^= 1
            h1, h2 = tab[c], tab[tuple(c2)]
            for t in range(T):
                for x in V:
                    if h1[t][x] != h2[t][x]:
                        D[(t + 1, x)].add(VARS[k])
    return D


def split(D):
    return all(vtype[w] == (t + chi[x]) % 2 for (t, x), S in D.items() for w in S)


T = 4
Dnl = deps(g_nl, T)
check("R2(i) nonlinear, opposite-colour reads only: split holds", split(Dnl))
check("R2(i) non-vacuous: some u_i(t) depends on >= 3 variables", any(len(S) >= 3 for S in Dnl.values()))
def h(w):
    return (w[0] & w[1]) | w[2]


def xor3(w, w2):
    return tuple(a ^ b for a, b in zip(w, w2))


check("R2(i) non-vacuous: g_A0 = (x&y)|z is not affine over F_2",
      any(h(xor3(w, w2)) ^ h(w) ^ h(w2) ^ h((0, 0, 0))
          for w in itertools.product((0, 1), repeat=3) for w2 in itertools.product((0, 1), repeat=3)))
check("R2(ii) LINEAR rule with a same-colour read: split fails", not split(deps(g_lin_same, T)))
check("R2(iii) nonlinear rule with the same same-colour read: split fails", not split(deps(g_nl_same, T)))
check("R2(iv) control: linear, opposite-colour reads only: split holds", split(deps(g_lin, T)))

# ---------------- R3 ----------------
def affine_F(y):
    return (y[0] ^ y[2] ^ 1)


def and_F(y):
    return y[0] & y[1]


e = (0, 1, 0)
e2 = (1, 0, 0)
ys = list(itertools.product((0, 1), repeat=3))


def diff_const_e(F, e):
    for c in (0, 1):
        vals = {F(tuple(yi ^ (c * ei) for yi, ei in zip(y, e))) ^ F(y) for y in ys}
        if len(vals) != 1:
            return False
    return True


check("R3 affine F: F(y + c e) - F(y) independent of y", diff_const_e(affine_F, e2) and diff_const_e(affine_F, e))
check("R3 countercontrol: AND: F(y + c e) - F(y) depends on y", not diff_const_e(and_F, e2))

# ---------------- R4 ----------------
c, s = sp.Rational(4, 5), sp.Rational(3, 5)
c2, s2 = c * c - s * s, 2 * s * c          # cos 2al, sin 2al
I2 = sp.eye(2)
Z = sp.Matrix([[1, 0], [0, -1]])
X = sp.Matrix([[0, 1], [1, 0]])


def proj(cth, sth, o):  # projector onto outcome o in {+1,-1} along (sin, 0, cos)
    return (I2 + o * (cth * Z + sth * X)) / 2


phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
rho = phi * phi.T
A = {0: (sp.Integer(1), sp.Integer(0)), 1: (c2, s2)}
B = {0: (c, s), 1: (c, -s)}
probs = {}
for x in (0, 1):
    for y in (0, 1):
        for oa in (1, -1):
            for ob in (1, -1):
                M = sp.kronecker_product(proj(*A[x], oa), proj(*B[y], ob))
                probs[(x, y, oa, ob)] = sp.nsimplify(sp.simplify((rho * M).trace()))
check("R4(a) all 16 joint probabilities are rational", all(v.is_Rational for v in probs.values()))
check("R4(a) normalized per setting pair",
      all(sum(probs[(x, y, oa, ob)] for oa in (1, -1) for ob in (1, -1)) == 1 for x in (0, 1) for y in (0, 1)))
nosig = all(sum(probs[(x, 0, oa, ob)] for ob in (1, -1)) == sum(probs[(x, 1, oa, ob)] for ob in (1, -1))
            for x in (0, 1) for oa in (1, -1)) and \
    all(sum(probs[(0, y, oa, ob)] for oa in (1, -1)) == sum(probs[(1, y, oa, ob)] for oa in (1, -1))
        for y in (0, 1) for ob in (1, -1))
check("R4(a) no-signalling", nosig)
E = {(x, y): sum(oa * ob * probs[(x, y, oa, ob)] for oa in (1, -1) for ob in (1, -1)) for x in (0, 1) for y in (0, 1)}
chsh = E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]
check("R4(a) CHSH = 344/125 > 2, exact rational", chsh == sp.Rational(344, 125) and chsh > 2)
pt = (2 + sp.sqrt(2)) / 4
check("R4(b) Tsirelson-point P(a=b) = (2+sqrt2)/4 is irrational", pt.is_rational is False)
# control: a ratio of counts is rational for any finite counting measure (exhaustive small check)
check("R4(b) control: every k/N with 0<=k<=N<=50 is rational and none equals (2+sqrt2)/4",
      all(sp.Rational(k, N) != pt for N in range(1, 51) for k in range(N + 1)))

# ---------------- R5 ----------------
# One operator can meet both necessary conditions; a ones-fixing flow meets only one.
# (a) drive on the pair (0,1) of three states at angle pi/4: D = exp(-i pi/4 X_01) (+1 on state 2):
#     unitary, non-monomial, moves the all-ones ray. (b) the gate flow of the exchange (0 1) at
#     time 1/2, G = (1+i)/2 I + (1-i)/2 P on the pair (+1 on state 2): non-monomial, fixes all-ones.
r = sp.sqrt(2) / 2
Dd = sp.Matrix([[r, -sp.I * r, 0], [-sp.I * r, r, 0], [0, 0, 1]])
P01 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
Gh = (1 + sp.I) / 2 * sp.eye(3) + (1 - sp.I) / 2 * P01
Gh[2, 2] = 1
one = sp.ones(3, 1)


def monomial(M):
    return all(sum(1 for j in range(3) if sp.simplify(M[i, j]) != 0) == 1 for i in range(3))


def on_ray(w):
    return all(sp.simplify(w[i] * 1 - w[0] * 1) == 0 for i in range(3))


check("R5(a) drive: unitary, non-monomial, moves the all-ones ray",
      sp.simplify(Dd.H * Dd) == sp.eye(3) and not monomial(Dd) and not on_ray(Dd * one))
check("R5(b) ones-fixing gate flow at t=1/2: unitary, non-monomial, fixes the all-ones ray",
      sp.simplify(Gh.H * Gh) == sp.eye(3) and not monomial(Gh) and on_ray(Gh * one))

print("ALL PASS" if ok else "SOME CHECK FAILED")
