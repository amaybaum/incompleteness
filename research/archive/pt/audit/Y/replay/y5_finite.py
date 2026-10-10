# y5_finite.py -- thread Y (stage 4, Q-EX): the finite extensions, S1 and S2, decided by the reachability
# dichotomy with one exact witness.
#
# DECISION RULE (fixed before the first run; rules, not expected numbers):
#  * Groups are enumerated exactly as projective maps psi -> U conj^k(psi), U a primitive Gaussian-integer matrix
#    normalized by a unit (first nonzero entry with re > 0, im >= 0), k in {0,1} (k = 1: the global transpose T).
#    Generators (unnormalized, Gaussian-integer): Ht = [[1,1],[1,-1]], Sg = diag(1, i), CNOT, Z, X, SWAP, T.
#  * G16 must come out of order 16 (control: the stage-3 order); every named group's generators must lie in
#    BIG = <Ht(x)I, I(x)Ht, Sg(x)I, I(x)Sg, CNOT, T>; orders are reported.
#  * Witness: the first phi0 of the fixed list such that every g in BIG has det Psi(g phi0) != 0 (exact integers).
#    Then d_min = min_g |det Psi(g phi0)|^2/|g phi0|^4 > 0 is exact; x = 4 d_min; c = min(2, 1 + x/8), and
#    PASS iff (2/c - 1)^2 >= 1 - x (exact rational): then c times the largest product overlap of g phi0 is <= 1
#    for all g, and e = (I - c P_phi0)/8 seeds EBF for BIG and every subgroup of BIG, and for S2 (whose reachable
#    set is G16.SEP, written argument in RESULT Y5).
#  * Countercontrols: for phi = |00> and for the Bell vector (1,0,0,1), some g in BIG gives det Psi(g phi) = 0
#    (the certificate must fail on reachable states).
#  * "VERDICT Y5-FINITE-EXACT" iff every line passes; otherwise "VERDICT Y5-FINITE-FAILED" and the failing ids.
from fractions import Fraction as Fr

fails = []


def report(cid, ok, text):
    print(("PASS " if ok else "FAIL ") + cid + " " + text)
    if not ok:
        fails.append(cid)


# Gaussian integers as (re, im) tuples of Python ints.
def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gconj(a):
    return (a[0], -a[1])


def gnorm(a):
    return a[0] * a[0] + a[1] * a[1]


def ground_div(a, b):
    n = gnorm(b)
    p = gmul(a, gconj(b))
    rd = lambda t: (2 * t + n) // (2 * n)          # nearest integer, exact
    return (rd(p[0]), rd(p[1]))


def ggcd(a, b):
    while b != (0, 0):
        q = ground_div(a, b)
        r = (a[0] - gmul(q, b)[0], a[1] - gmul(q, b)[1])
        a, b = b, r
    return a


def gexdiv(a, g):
    n = gnorm(g)
    p = gmul(a, gconj(g))
    assert p[0] % n == 0 and p[1] % n == 0
    return (p[0] // n, p[1] // n)


UNITS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def canon(M):
    g = (0, 0)
    for x in M:
        if x != (0, 0):
            g = ggcd(g, x) if g != (0, 0) else x
    M = [gexdiv(x, g) for x in M]
    first = next(x for x in M if x != (0, 0))
    for u in UNITS:
        y = gmul(first, u)
        if y[0] > 0 and y[1] >= 0:
            return tuple(gmul(x, u) for x in M)
    raise ValueError


def mmul(A, B):
    return tuple(
        (lambda r, c: (sum(gmul(A[4 * r + k], B[4 * k + c])[0] for k in range(4)),
                       sum(gmul(A[4 * r + k], B[4 * k + c])[1] for k in range(4))))(r, c)
        for r in range(4) for c in range(4))


def mconj(A):
    return tuple(gconj(x) for x in A)


def compose(g1, g2):
    (U1, k1), (U2, k2) = g1, g2
    return (canon(mmul(U1, mconj(U2) if k1 else U2)), k1 ^ k2)


def kron2(A, B):  # A, B: 2x2 as 4-tuples row-major of Gaussian ints
    return tuple(gmul(A[2 * (r // 2) + (c // 2)], B[2 * (r % 2) + (c % 2)]) for r in range(4) for c in range(4))


g = lambda *xs: tuple((x, 0) if isinstance(x, int) else x for x in xs)
I2, Ht, Sg = g(1, 0, 0, 1), g(1, 1, 1, -1), g(1, 0, 0, (0, 1))
Zp, Xp = g(1, 0, 0, -1), g(0, 1, 1, 0)
CNOT = g(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0)
SWAP = g(1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1)
I4 = kron2(I2, I2)
T = (canon(I4), 1)
el = lambda U: (canon(U), 0)


def enum(gens):
    start = (canon(I4), 0)
    seen = {start}
    frontier = [start]
    while frontier:
        new = []
        for x in frontier:
            for h in gens:
                y = compose(h, x)
                if y not in seen:
                    seen.add(y); new.append(y)
        frontier = new
    return seen


G16g = [el(CNOT), el(kron2(Zp, I2)), el(kron2(I2, Zp)), T]
NAMED = {
    'S0 = G16': G16g,
    'S1 = G16 + SWAP': G16g + [el(SWAP)],
    'LPT = G16 + local Paulis (X Gbig)': G16g + [el(kron2(Xp, I2)), el(kron2(I2, Xp))],
    'LPT + SWAP': G16g + [el(kron2(Xp, I2)), el(kron2(I2, Xp)), el(SWAP)],
    'G16 + control Clifford': G16g + [el(kron2(Ht, I2)), el(kron2(Sg, I2))],
    'G16 + target Clifford': G16g + [el(kron2(I2, Ht)), el(kron2(I2, Sg))],
}
BIGg = [el(kron2(Ht, I2)), el(kron2(I2, Ht)), el(kron2(Sg, I2)), el(kron2(I2, Sg)), el(CNOT), T]
BIG = enum(BIGg)
report("O1", True, "BIG = <Ht(x)I, I(x)Ht, Sg(x)I, I(x)Sg, CNOT, T> (two-qubit Clifford group with the transpose): order %d" % len(BIG))
for name, gens in NAMED.items():
    G = enum(gens)
    inbig = all(h in BIG for h in gens)
    ok = inbig and (len(G) == 16 if name.startswith('S0') else True)
    report("O-" + name.split()[0], ok, "%s: order %d; generators in BIG: %s" % (name, len(G), inbig))


def apply(gel, v):
    U, k = gel
    w = tuple(gconj(x) for x in v) if k else v
    return tuple((sum(gmul(U[4 * r + c], w[c])[0] for c in range(4)), sum(gmul(U[4 * r + c], w[c])[1] for c in range(4)))
                 for r in range(4))


def dval(v):
    det = (gmul(v[0], v[3])[0] - gmul(v[1], v[2])[0], gmul(v[0], v[3])[1] - gmul(v[1], v[2])[1])
    n2 = sum(gnorm(x) for x in v)
    return Fr(gnorm(det), n2 * n2)


CANDS = [g(1, 2, (0, 3), (-1, 1)), g(2, (1, 1), (0, -1), 3), g(1, 3, (0, 2), (-2, 1)), g(3, -1, (1, 2), (0, 2)),
         g(5, (2, 3), (-1, 4), (3, -2))]
phi0, dmin = None, None
for cand in CANDS:
    ds = [dval(apply(h, cand)) for h in BIG]
    if min(ds) > 0:
        phi0, dmin = cand, min(ds); break
report("W1", phi0 is not None, "witness phi0 = %s: every image under BIG is entangled; d_min = %s" % (phi0, dmin))
x = 4 * dmin
c = min(Fr(2), 1 + x / 8)
okc = c > 1 and (Fr(2) / c - 1) ** 2 >= 1 - x
report("C1", okc, "cap parameter c = %s: (2/c - 1)^2 >= 1 - 4 d_min exactly, so c * (max product overlap) <= 1 on the whole orbit" % c)
G16 = enum(G16g)
d16 = min(dval(apply(h, phi0)) for h in G16)
report("C2", d16 >= dmin, "S2: min over G16 of the normalized |det|^2 is %s >= d_min (S2's reachable set is G16.SEP)" % d16)
for nm, v in (("|00>", g(1, 0, 0, 0)), ("Bell", g(1, 0, 0, 1))):
    m = min(dval(apply(h, v)) for h in BIG)
    report("cc-" + nm, m == 0, "countercontrol %s: min over BIG of the normalized |det|^2 = %s (the certificate fails)" % (nm, m))
if fails:
    print("VERDICT Y5-FINITE-FAILED " + " ".join(fails))
else:
    print("VERDICT Y5-FINITE-EXACT")
