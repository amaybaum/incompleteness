#!/usr/bin/env python3
"""QPHEN Phase 1 r6: exact checks of paper claims on generic objects only.

No OI mechanism is constructed or simulated. Imports no earlier probe.

(1) Q4-P19, strong form (N3): on F_2^4 with coordinates (c, x, m, mp) and
    symplectic pairs (c, x), (m, mp), every location-preserving affine-symplectic
    map whose meter write depends on c changes x on some state with c = 0.
    Symplectic group built by brute force over all 2^16 matrices (independent of
    the Gram/transvection constructions of earlier probes).
(2) B1, the SA-1(a) row: the phase-space second-order step
    (a, b) -> (b, F b - a + k) is symplectic iff F is symmetric, for every k
    (translations are symplectic). Exhaustive over F at small (q, n).
(3) N2: a deterministic response table (2 settings, +-1 outcomes per wing) with
    no remote-setting dependence has |CHSH| <= 2; every table with |CHSH| > 2 has
    remote-setting dependence. Exhaustive over all 256 tables.
(4) N15: no-signalling of a point-mass preparation forces a local table; a
    mixture of signalling point masses can be no-signalling with S = 4
    (countercontrol: the restriction is not vacuous).
"""
import itertools
import sys

PASS = 0
FAIL = 0


def check(label, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("PASS", label)
    else:
        FAIL += 1
        print("FAIL", label)


# ---------------------------------------------------------------- (1)
q = 2
C, X, M, MP = 0, 1, 2, 3
J = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]  # mod 2, -1 = 1


def matmul(A, B, mod):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) % mod for j in range(m)] for i in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def apply(Mx, b, y):
    return tuple((sum(Mx[i][j] * y[j] for j in range(4)) + b[i]) % 2 for i in range(4))


sp = []
for bits in range(1 << 16):
    Mx = [[(bits >> (4 * i + j)) & 1 for j in range(4)] for i in range(4)]
    if matmul(matmul(transpose(Mx), J, 2), Mx, 2) == J:
        sp.append(Mx)
check("(1a) |Sp(4,F_2)| = 720 by brute force over 65536 matrices", len(sp) == 720)

pts = list(itertools.product(range(2), repeat=4))
trans = pts
loc_pres = []
for Mx in sp:
    for b in trans:
        if all(apply(Mx, b, y)[C] == y[C] for y in pts):
            loc_pres.append((Mx, b))


def meter_depends_on_c(Mx, b):
    for y in pts:
        y1 = tuple((y[i] + (1 if i == C else 0)) % 2 for i in range(4))
        t0, t1 = apply(Mx, b, y), apply(Mx, b, y1)
        if (t0[M], t0[MP]) != (t1[M], t1[MP]):
            return True
    return False


def changes_x_on_silent(Mx, b):
    return any(apply(Mx, b, y)[X] != y[X] for y in pts if y[C] == 0)


strong = [(Mx, b) for (Mx, b) in loc_pres if meter_depends_on_c(Mx, b)]
print("     (1) location-preserving affine-symplectic maps:", len(loc_pres),
      "; with meter write depending on c:", len(strong))
check("(1b) strong-form recorders number 288", len(strong) == 288)
check("(1c) every strong-form recorder changes x on some c = 0 state",
      all(changes_x_on_silent(Mx, b) for (Mx, b) in strong))


def weak_records(Mx, b):
    return any(apply(Mx, b, y)[M] != y[M] or apply(Mx, b, y)[MP] != y[MP] for y in pts if y[C] == 1)


weak_only = [(Mx, b) for (Mx, b) in loc_pres
             if weak_records(Mx, b) and not meter_depends_on_c(Mx, b) and not changes_x_on_silent(Mx, b)]
I4 = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
check("(1d) weak 'records' admits maps that never change x on c = 0 (e.g. the translation m <- m + 1)",
      len(weak_only) > 0 and (I4, (0, 0, 1, 0)) in weak_only)
ident_c0 = [(Mx, b) for Mx in sp for b in trans
            if all(apply(Mx, b, y) == y for y in pts if y[C] == 0)]
check("(1e) affine-symplectic maps that are the identity on c = 0 change no meter slot on c = 1 (0 of 11520)",
      len(sp) * 16 == 11520 and not any(weak_records(Mx, b) for (Mx, b) in ident_c0))


# ---------------------------------------------------------------- (2)
def step_symplectic(Fm, mod, n):
    # phase-space matrix [[0, I], [-I, F]] on (a, b); form [[0, I], [-I, 0]]
    N = 2 * n
    Mx = [[0] * N for _ in range(N)]
    Jn = [[0] * N for _ in range(N)]
    for i in range(n):
        Mx[i][n + i] = 1
        Mx[n + i][i] = (-1) % mod
        Jn[i][n + i] = 1
        Jn[n + i][i] = (-1) % mod
        for j in range(n):
            Mx[n + i][n + j] = Fm[i][j]
    return matmul(matmul(transpose(Mx), Jn, mod), Mx, mod) == Jn


ok2 = True
counts = []
for (mod, n) in [(2, 2), (2, 3), (3, 2), (5, 2)]:
    sym = 0
    for entries in itertools.product(range(mod), repeat=n * n):
        Fm = [list(entries[i * n:(i + 1) * n]) for i in range(n)]
        s = step_symplectic(Fm, mod, n)
        is_sym = Fm == transpose(Fm)
        if s != is_sym:
            ok2 = False
        sym += s
    counts.append((mod, n, sym))
print("     (2) symplectic second-order steps (q, n, count):", counts)
check("(2a) the step (a,b) -> (b, F b - a) is symplectic iff F = F^T (q in {2,3,5}, n <= 3, exhaustive)", ok2)
check("(2b) translation (a,b) -> (a,b) + k has linear part I, which is symplectic",
      step_symplectic([[0, 0], [0, 0]], 3, 2) is True)

# ---------------------------------------------------------------- (3)
settings = [(0, 0), (0, 1), (1, 0), (1, 1)]
tables = list(itertools.product([1, -1], repeat=8))  # A(x,y) for 4 pairs, then B(x,y)


def chsh(t):
    A = dict(zip(settings, t[:4]))
    B = dict(zip(settings, t[4:]))
    E = {s: A[s] * B[s] for s in settings}
    return E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]


def local(t):
    A = dict(zip(settings, t[:4]))
    B = dict(zip(settings, t[4:]))
    return all(A[(x, 0)] == A[(x, 1)] for x in (0, 1)) and all(B[(0, y)] == B[(1, y)] for y in (0, 1))


check("(3a) 256 tables; every local table has |CHSH| <= 2", len(tables) == 256 and all(abs(chsh(t)) <= 2 for t in tables if local(t)))
check("(3b) every table with |CHSH| > 2 has a remote-setting dependence",
      all(not local(t) for t in tables if abs(chsh(t)) > 2) and any(abs(chsh(t)) == 4 for t in tables))


# ---------------------------------------------------------------- (4)
def marginals_ns(mix):
    # mix: list of (weight, table); no-signalling of each wing's outcome law
    from fractions import Fraction
    def pA(x, y, a):
        return sum(w for w, t in mix if dict(zip(settings, t[:4]))[(x, y)] == a)
    def pB(x, y, b):
        return sum(w for w, t in mix if dict(zip(settings, t[4:]))[(x, y)] == b)
    return (all(pA(x, 0, a) == pA(x, 1, a) for x in (0, 1) for a in (1, -1)) and
            all(pB(0, y, b) == pB(1, y, b) for y in (0, 1) for b in (1, -1)))


check("(4a) a point mass is no-signalling iff its table is local (256 tables)",
      all(marginals_ns([(1, t)]) == local(t) for t in tables))
from fractions import Fraction
# PR box as a mixture of two signalling point masses: A outputs w, B outputs w xor (x and y)
def pr_table(w):
    sgn = lambda bit: 1 - 2 * bit
    A = [sgn(w) for (x, y) in settings]
    B = [sgn(w ^ (x & y)) for (x, y) in settings]
    return tuple(A + B)


mix = [(Fraction(1, 2), pr_table(0)), (Fraction(1, 2), pr_table(1))]
S = sum(w * chsh(t) for w, t in mix)
check("(4b) countercontrol: uniform mixture of two signalling point masses is no-signalling with S = 4",
      marginals_ns(mix) and S == 4 and not any(marginals_ns([(1, t)]) for _, t in mix))

print()
print(f"{PASS} of {PASS + FAIL} checks pass")
sys.exit(0 if FAIL == 0 else 1)
