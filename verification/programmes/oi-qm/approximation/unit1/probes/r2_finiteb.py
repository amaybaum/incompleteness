#!/usr/bin/env python3
"""r2 labelled exact instance check for #1216 unit 1 (finding N5): one digitized step of Main's
fixed-point model can produce a non-PSD register from an exact initial register.  Imports nothing
from earlier probes.  Generic 2x2 matrices; no OI mechanism.

Reading of Main:578's model (stated, not taken from Main verbatim): every register and Kraus entry
is rounded to b fractional bits after each operation, with |error| <= 2^-b; Hermiticity by storing
the upper triangle.  Two admissible rounding rules are tested: round-to-nearest (ties up) and
floor.  The step: K = R_y(theta), applied as rho1 = rd(rd(K_hat rho0) K_hat^dag), K_hat = rd(K),
from rho0 = |0><0|, for theta = pi/4 (cos, sin evaluated exactly by sympy) and for the rational
3-4-5 rotation (cos = 4/5, sin = 3/5).  Window of the Rounding Lemma at K = 1, d = 2, R = 1:
b >= log2(2 K C_{d,R}) with C_{d,R} = 48 R d^4 = 768, i.e. b >= 11 (Main:568, :576, :578).

N5a  for each rule and rotation, the b in 4..24 at which rho1 has det < 0 (non-PSD) are listed;
     the check passes iff such a b exists inside the window (b >= 11) for theta = pi/4 under
     round-to-nearest.
N5b  control: the unrounded product K rho0 K^dag is rank one and PSD (det = 0, trace 1).
N5c  validity under clipping: the clipped and normalized Z-read pre-grid probabilities of the
     non-PSD register are nonnegative and sum to 1.
Run: python3 -I -B r2_finiteb.py   (exit 0 iff every check passes)
"""
import sys
from fractions import Fraction

import sympy as sp

FAILS = []


def check(label, cond):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAILS.append(label)


def rd_nearest(x, b):
    return Fraction(int(sp.floor(sp.nsimplify(x) * 2 ** b + sp.Rational(1, 2))), 2 ** b)


def rd_floor(x, b):
    return Fraction(int(sp.floor(sp.nsimplify(x) * 2 ** b)), 2 ** b)


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def herm_round(M, rd, b):
    a, c, off = rd(M[0][0], b), rd(M[1][1], b), rd(M[0][1], b)
    return [[a, off], [off, c]]          # real symmetric here; lower triangle by conjugation


def step(cs, sn, rd, b):
    K = [[rd(cs, b), rd(-sn, b)], [rd(sn, b), rd(cs, b)]]
    Kd = [[K[0][0], K[1][0]], [K[0][1], K[1][1]]]
    rho0 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
    T = [[rd(x, b) for x in row] for row in matmul(K, rho0)]
    return herm_round(matmul(T, Kd), rd, b)


def det(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


ROTS = {'pi/4': (sp.cos(sp.pi / 8), sp.sin(sp.pi / 8)),       # R_y(theta) has entries cos(theta/2), sin(theta/2)
        '3-4-5': (sp.Rational(4, 5), sp.Rational(3, 5))}
RULES = {'nearest': rd_nearest, 'floor': rd_floor}
WINDOW = 11
hits = {}
for rn, (cs, sn) in ROTS.items():
    for un, rd in RULES.items():
        bad = [b for b in range(4, 25) if det(step(cs, sn, rd, b)) < 0]
        hits[(rn, un)] = bad
        print(f"     theta {rn}, rounding {un}: b in 4..24 with det(rho1) < 0: {bad}")
inside = [b for b in hits[('pi/4', 'nearest')] if b >= WINDOW]
check("N5a theta = pi/4, round-to-nearest: a non-PSD register (det < 0) occurs at some b >= 11 (inside the window)",
      len(inside) > 0)
if inside:
    b0 = inside[0]
    R = step(*ROTS['pi/4'], rd_nearest, b0)
    print(f"     b = {b0}: rho1 = {[[str(x) for x in r] for r in R]}, det = {det(R)}")

# N5b control: exact product
cs, sn = ROTS['pi/4']
Kx = sp.Matrix([[cs, -sn], [sn, cs]])
ex = sp.simplify(Kx * sp.diag(1, 0) * Kx.T)
check("N5b control: the unrounded product is rank one and PSD (det 0, trace 1)",
      sp.simplify(ex.det()) == 0 and sp.simplify(ex.trace()) == 1)

# N5c validity of clipped and normalized Z-read pre-grid probabilities on the non-PSD register
if inside:
    R = step(*ROTS['pi/4'], rd_nearest, inside[0])
    t = [R[0][0], R[1][1]]                     # Z-read branch traces <k|rho1|k>
    c = [x if x > 0 else Fraction(0) for x in t]
    Q = sum(c)
    probs = [x / Q for x in c]
    check("N5c clipped and normalized Z-read probabilities are >= 0 and sum to 1 on that register",
          all(x >= 0 for x in probs) and sum(probs) == 1)
else:
    check("N5c skipped: no in-window instance", False)

print("RESULT " + ("ALL PASS" if not FAILS else f"{len(FAILS)} FAIL"))
sys.exit(1 if FAILS else 0)
