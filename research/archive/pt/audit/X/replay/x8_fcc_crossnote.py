#!/usr/bin/env python3
"""Thread X (EXOT) -- cross-thread note (S3): does four-copy coherence hold for the uniform exotic cones K1, K4?

Run (cwd pt/X/): python3 -I -B x8_fcc_crossnote.py > x8_fcc_crossnote.out 2> x8_fcc_crossnote.err

For a uniform self-dual cone K (all four pairs K, cnot gates), FCC asks fourVal(X, Y, E, F) >= 0 for states X, Y in K
and effects E, F in K^* = K. The identity fourVal X Y E F = ipW(E, X F Y^T) (table products) is S3's, confirmed
symbolically by the coordinator (AUDIT-S3, item S1); it is used here as recorded, not re-derived from the design
modules. All entries are integers after scaling by positive constants, so numpy int64 arithmetic is exact here.
  P   positive control: fourVal(phiW, phiW, E0, G) = -1 (S3's uniform-K_gen witness) with this implementation;
  QC  countercontrol: on 77 elements of Q3 (36 axis products, their 36 cnot images, the 4 stabilizer states T_s and
      phiW) the minimum of fourVal over all quadruples must be >= 0 (FCC holds for uniform Q3; landed F0-F3);
  K1  minimum over quadruples from {E0} u axis products u cnot images u {T_s : <T_s, E0> >= 0} (all in K1);
  K4  minimum over quadruples from {e_s} u axis products u cnot images (all in K4).
A negative minimum is an exact FCC-violating instance for the uniform cone; a nonnegative one is no claim.

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. P must equal -1 and QC must be >= 0, else 'X8-FCC: CONTROL FAILED' and exit 1.
  R2. For K1 and K4 print the minimum and one minimizing quadruple; print 'FCC-VIOLATION' iff the minimum < 0.
  R3. Integer arithmetic only (numpy int64, entries scaled to integers); no floats or randomness.
"""
import sys
from itertools import product

import numpy as np

SGN_NEG = {(1, 3), (2, 2)}
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot(w):
    return np.array([[(-1 if (m, n) in SGN_NEG else 1) * w[PC[m][n], PT[m][n]] for n in range(4)] for m in range(4)],
                    dtype=np.int64)


def tab(entries):
    w = np.zeros((4, 4), dtype=np.int64)
    for m, n, c in entries:
        w[m, n] += c
    return w


AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
AXP = [(f"p{a}{b}", np.outer([1, *a], [1, *b]).astype(np.int64)) for a, b in product(AX, AX)]
CAXP = [(f"cnot p{a}{b}", cnot(m)) for (_, m), (a, b) in zip(AXP, product(AX, AX))]
S4 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
TS = {s: tab([(0, 0, 1), (1, 3, s[0]), (2, 2, s[1]), (3, 1, s[0] * s[1])]) for s in S4}
E0 = tab([(0, 0, 1), (1, 3, 1), (2, 2, -1)])
G = TS[(-1, 1)]                                         # the pure table of g = (1,-1,-1,-1)/2
phiW = tab([(0, 0, 1), (1, 1, 1), (2, 2, -1), (3, 3, 1)])
E4 = {s: 2 * tab([(0, 0, 1)]) - TS[s] for s in S4}      # 4 e_s = 2 E00 - T_s (positive multiple of e_s)


def ipw(a, b):
    return int(np.sum(a * b))


def four(X, Y, E, F):
    return ipw(E, X @ F @ Y.T)


def min_quad(elems):
    names = [n for n, _ in elems]
    M = np.stack([m for _, m in elems])                  # (N, 4, 4)
    best, arg = None, None
    for ix in range(len(M)):
        XF = np.einsum('ij,fjk->fik', M[ix], M)          # X F for every F
        XFYt = np.einsum('fik,ylk->fyil', XF, M)         # X F Y^T for every F, Y
        vals = np.einsum('fyil,eil->fye', XFYt, M)       # ipW(E, X F Y^T)
        k = int(np.argmin(vals))
        v = int(vals.flat[k])
        if best is None or v < best:
            f, y, e = np.unravel_index(k, vals.shape)
            best, arg = v, (names[ix], names[y], names[e], names[f])
    return best, arg


p = four(phiW, phiW, E0, G)
print(f"P   fourVal(phiW, phiW, E0, G) = {p}")
Q3E = AXP + CAXP + [(f"T{s}", TS[s]) for s in S4] + [("phiW", phiW)]
qmin, qarg = min_quad(Q3E)
print(f"QC  uniform Q3, {len(Q3E)} elements: min fourVal = {qmin} at (X, Y, E, F) = {qarg}")
if p != -1 or qmin < 0:
    print('X8-FCC: CONTROL FAILED')
    sys.exit(1)
K1E = [("E0", E0)] + AXP + CAXP + [(f"T{s}", TS[s]) for s in S4 if ipw(TS[s], E0) >= 0]
kmin, karg = min_quad(K1E)
print(f"K1  uniform K1, {len(K1E)} elements: min fourVal = {kmin} at (X, Y, E, F) = {karg}"
      f"{'  FCC-VIOLATION' if kmin < 0 else ''}")
K4E = [(f"4e{s}", E4[s]) for s in S4] + AXP + CAXP
kmin4, karg4 = min_quad(K4E)
print(f"K4  uniform K4, {len(K4E)} elements (e_s scaled by 4): min fourVal = {kmin4} at (X, Y, E, F) = {karg4}"
      f"{'  FCC-VIOLATION' if kmin4 < 0 else ''}")
print('SUMMARY controls P and QC green; values are exact integers (scaled); see RESULT section 4 cross-notes')
