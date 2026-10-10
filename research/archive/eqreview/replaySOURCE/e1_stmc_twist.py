"""EQ4-SOURCE e1 — exact exploration (a lead, not a certificate): does the simplest twist that respects single-token
marginal coherence (STMC) give a model of KT4-without-tok for the odd pattern (Q3, Q3, Q3, twin)?

Setting.  In a KT4 model with local tomography of both groupings, the B-coordinates of the common body are Psi applied
to the A-coordinates (tables in token order 0, 1, 2, 3), Psi linear.  Cross-positivity for family (i) reads
  v(Psi) = sum_{abcd} E_ac F_bd [Psi(prodA X Y)]_abcd >= 0   for X, Y in Q3, E in dualW Q3, F in dualW twin.
Psi = id is the token-coherent table model (it fails for the odd pattern: Lemma P, -1/8); Psi = rho3 is M_tw (valid,
STMC fails at token 3).  The STMC-respecting candidate examined here is
  Psi_mf(Z)_abcd = s_d Z_abcd if (a, b, c) != (0, 0, 0), and Z_000d otherwise   (s = (1, 1, -1, 1)),
i.e. rho3 on every correlation entry and the identity on token 3's own marginal.

Witnesses (all exact): X = prodState(z, 0) on tokens 0, 1; Y = prodState(-z, y) on tokens 2, 3; E = phiW / 4 (the Bell
effect table of pair 02, in dualW Q3 through cnot as in s1 R5); F = actT reflY (tens(u0, sharpVec y)) (a product effect
table of pair 13 read in the twin chart, so F in dualW twin).

DECISION RULE (fixed before the first run; rules, not expected numbers):
  controls: (c1) v(rho3) at these witnesses equals fourVal(X, Y, E, actT reflY F) and is >= 0 (M_tw's identity);
            (c2) v(id) at Lemma P's witnesses (s1 R4) is negative (the token-coherent structure fails for the odd
                 pattern);
            (c3) Psi_mf preserves every single-token marginal entry (STMC holds for Psi_mf).
  lead:     LEAD STMC-TWIST-EXCLUDED is printed iff all controls pass and v(Psi_mf) < 0 at the witnesses;
            LEAD STMC-TWIST-NOT-EXCLUDED-HERE iff all controls pass and v(Psi_mf) >= 0; otherwise LEAD NOT RENDERED.
  A lead certifies nothing about other STMC-respecting maps.
"""
import itertools
from fractions import Fraction as Fr

R4 = range(4)
I4 = list(itertools.product(R4, R4, R4, R4))
S = [1, 1, -1, 1]


def hom3(x):
    return [Fr(1)] + [Fr(v) for v in x]


def prodState(x, y):
    hx, hy = hom3(x), hom3(y)
    return [[hx[m] * hy[n] for n in R4] for m in R4]


def tens(a, b):
    return [[Fr(a[m]) * Fr(b[n]) for n in R4] for m in R4]


def actT_reflY(T):
    return [[S[n] * T[m][n] for n in R4] for m in R4]


def sharpVec(b):
    return [Fr(1, 2)] + [Fr(v, 2) for v in b]


def prodA(X, Y):
    return {(a, b, c, d): X[a][b] * Y[c][d] for a, b, c, d in I4}


def val(E, F, Z):
    return sum(E[a][c] * F[b][d] * Z[(a, b, c, d)] for a, b, c, d in I4)


def fourVal(X, Y, E, F):
    return sum(X[a][b] * Y[c][d] * E[a][c] * F[b][d] for a, b, c, d in I4)


def psi_rho3(Z):
    return {I: S[I[3]] * Z[I] for I in I4}


def psi_mf(Z):
    return {I: (S[I[3]] * Z[I] if I[:3] != (0, 0, 0) else Z[I]) for I in I4}


PHIW = [[Fr([1, 1, -1, 1][i]) if i == j else Fr(0) for j in R4] for i in R4]
z, y = [0, 0, 1], [0, 1, 0]
X = prodState(z, [0, 0, 0])
Y = prodState([0, 0, -1], y)
E = [[v / 4 for v in row] for row in PHIW]
Fp = tens([1, 0, 0, 0], sharpVec(y))
F = actT_reflY(Fp)
Z = prodA(X, Y)

c1v = val(E, F, psi_rho3(Z))
c1 = c1v == fourVal(X, Y, E, actT_reflY(F)) and c1v >= 0
print("CONTROL c1 v(rho3) = fourVal(X, Y, E, actT reflY F) = %s, nonnegative: %s" % (c1v, c1))
# Lemma P witnesses (s1 R4): X = Y = phiW, E = phiW/4, F = dg(1,-1,1,-1)/4
Fw = [[Fr([1, -1, 1, -1][i], 4) if i == j else Fr(0) for j in R4] for i in R4]
c2v = val(E, Fw, prodA(PHIW, PHIW))
c2 = c2v < 0
print("CONTROL c2 v(id) at Lemma P's witnesses = %s, negative: %s" % (c2v, c2))
Zg = {I: Fr(sum((k + 1) * (3 ** k) for k in I) + 1, 7) for I in I4}      # an arbitrary exact test table
single = [I for I in I4 if sum(1 for k in I if k != 0) <= 1]
c3 = all(psi_mf(Zg)[I] == Zg[I] for I in single)
print("CONTROL c3 Psi_mf fixes every entry with at most one nonzero index (STMC): %s" % c3)
v = val(E, F, psi_mf(Z))
print("VALUE v(Psi_mf) at the witnesses = %s" % v)
if c1 and c2 and c3:
    print("LEAD STMC-TWIST-EXCLUDED" if v < 0 else "LEAD STMC-TWIST-NOT-EXCLUDED-HERE")
else:
    print("LEAD NOT RENDERED")
