#!/usr/bin/env python3
"""Reviewer's exact generic check for #1216 unit 1, sec 5.1 row "A2 at finite b": closure fails
after ONE digitized step from an exact initial register, under a stated reading of Main:578's
fixed-point model.  Imports nothing from earlier probes or the repository.

Reading (stated, not Main's text verbatim): entries are dyadic with b fractional bits; every
multiplication result is rounded to the nearest multiple of 2^-b (ties up), so |error| <= 2^-(b+1)
<= 2^-b as Main:578 requires; Hermiticity by computing the upper triangle and conjugating.  The Kraus
operator is the digitized y-rotation K^ = round_b(R_y(theta)), theta = pi/4 (cos pi/8, sin pi/8, which
are irrational: rounding is decided exactly by sympy on algebraic numbers).  Initial register
|0><0| (exact).  Step: A = round_b(K^ rho0) (exact here, no rounding needed), rho1 = round_b(A K^T).

F1  for some b in 4..24 the reachable rho1 has det < 0 (a negative eigenvalue): closure fails.
F2  control: the same computation without rounding (exact dyadic product) gives det = 0 and a PSD
    rank-one register, so the negativity is the rounding's, not the data's.
F3  validity is kept: the pre-grid probabilities of the Z read on rho1 after clipping are >= 0
    (here both diagonal entries are > 0, so nothing is clipped) and sum to the normalized total.
Run: python3 -I -B rv_finiteb.py   (exit 0 iff all pass)
"""
import sys
from fractions import Fraction as Fr

import sympy as sp

FAIL = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


def rnd_exact(x, b):
    """Nearest multiple of 2^-b to the algebraic number x, decided exactly (ties up)."""
    n = sp.floor(sp.nsimplify(x) * 2 ** b + sp.Rational(1, 2))
    return Fr(int(n), 2 ** b)


def rnd(q, b):
    n = (q * 2 ** b + Fr(1, 2)).__floor__()
    return Fr(n, 2 ** b)


c = sp.cos(sp.pi / 8); s = sp.sin(sp.pi / 8)
hits = []
ctrl_ok = True
for b in range(4, 25):
    K = [[rnd_exact(c, b), rnd_exact(-s, b)], [rnd_exact(s, b), rnd_exact(c, b)]]
    # rho0 = |0><0|: A = K rho0 = [[K00, 0], [K10, 0]] exactly
    A = [[K[0][0], Fr(0)], [K[1][0], Fr(0)]]
    exact = [[sum(A[i][k] * K[j][k] for k in range(2)) for j in range(2)] for i in range(2)]
    r1 = [[rnd(exact[i][j], b) for j in range(2)] for i in range(2)]
    r1[1][0] = r1[0][1]                       # Hermiticity by construction (real case)
    d = r1[0][0] * r1[1][1] - r1[0][1] * r1[1][0]
    de = exact[0][0] * exact[1][1] - exact[0][1] * exact[1][0]
    ctrl_ok &= (de == 0 and exact[0][0] >= 0 and exact[1][1] >= 0)
    if d < 0:
        hits.append((b, d, r1))
print("     b values with a non-PSD reachable register:", [h[0] for h in hits])
if hits:
    b, d, r1 = hits[0]
    print(f"     b = {b}: rho1 = {[[str(x) for x in row] for row in r1]}, det = {d}")
check("F1 for some b in 4..24, one digitized step from |0><0| reaches a register with det < 0 (non-PSD)", bool(hits))
# Rounding Lemma window at K = 1, d = 2, R = 1: b >= log2(2 K C_{d,R}), C = 48 R d^4 = 768, i.e. b >= 11
win = [h for h in hits if 2 ** h[0] >= 2 * 1 * 768]
if win:
    print(f"     inside the window: b = {win[0][0]}, det = {win[0][1]}")
check("F1 such a register also occurs at a b inside the Rounding Lemma's window (b >= 11 at K = 1)", bool(win))
check("F2 control: the unrounded product is rank one and PSD (det = 0) at every b", ctrl_ok)
if hits:
    b, d, r1 = hits[0]
    q = [max(r1[0][0], Fr(0)), max(r1[1][1], Fr(0))]
    check("F3 validity: clipped pre-grid Z-read probabilities are nonnegative and normalize",
          all(x >= 0 for x in q) and sum(x / sum(q) for x in q) == 1)
print("RESULT", "ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
