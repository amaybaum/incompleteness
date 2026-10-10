"""A33 research: the exact nine-circle object of the single-carrier normalized space.

Faithful to the landed Lean construction:
  FibreGram 0 U i = B^H B with B[0][j] = U((i,0),(j,0)) = (1/2) M[i][j], so G[i][j][k] = (1/4) conj(M[i][j]) M[i][k];
  mixedTriple G ((i1,i2,i3),(j1,j2,j3)) = G[i1][j1][j2] * G[i2][j2][j3] * G[i3][j3][j1];
  circle r = (r1, r2) of act 26's list R: fun i => (F (r1 i)).submatrix r2 r2, i.e. G'[i][j][k] = G[r1 i][r2 j][r2 k].
On the unit circle conj(w) = w^-1, so every coordinate of every circle is sign * w^e / 64 exactly.
"""
from fractions import Fraction
import itertools

MS = [[(1, 0), (1, 0), (1, 0), (1, 0)],
      [(1, 0), (1, 1), (-1, 0), (-1, 1)],
      [(1, 0), (-1, 0), (1, 0), (-1, 0)],
      [(1, 0), (-1, 1), (-1, 0), (1, 1)]]          # (sign, exponent of w)
ID = (0, 1, 2, 3)
def sw(a, b):
    p = list(ID); p[a], p[b] = p[b], p[a]; return tuple(p)
P1, S23, S12 = ID, sw(2, 3), sw(1, 2)
R = [(P1, P1), (P1, S23), (P1, S12), (S23, P1), (S23, S23), (S23, S12), (S12, P1), (S12, S23), (S12, S12)]
IDX = list(itertools.product(itertools.product(range(4), repeat=3), itertools.product(range(4), repeat=3)))


def entry(i, j, k):
    """F[i][j][k] = (1/4) conj(M[i][j]) M[i][k] as (sign, exponent); the 1/4 is carried separately."""
    s1, e1 = MS[i][j]; s2, e2 = MS[i][k]
    return s1 * s2, -e1 + e2


def coords(r):
    """circle r: list over IDX of (sign, exponent), the coordinate being sign * w^exponent / 64."""
    a, b = R[r]
    out = []
    for (i1, i2, i3), (j1, j2, j3) in IDX:
        s, e = 1, 0
        for (i, j, k) in ((i1, j1, j2), (i2, j2, j3), (i3, j3, j1)):
            si, ei = entry(a[i], b[j], b[k]); s *= si; e += ei
        out.append((s, e))
    return out


C = [coords(r) for r in range(9)]


def gram(r, s):
    """S_rs(w, w') = <f_r(w), f_s(w')> = sum_p conj(f_r(w)_p) f_s(w')_p, as {(a, b): Fraction} with
    S = sum coef * w^a w'^b (conj(w^e) = w^-e on the unit circle)."""
    out = {}
    for (s1, e1), (s2, e2) in zip(C[r], C[s]):
        k = (-e1, e2)
        out[k] = out.get(k, 0) + s1 * s2
    return {k: Fraction(v, 4096) for k, v in out.items() if v}


def re_part(S):
    """Re S as a Laurent polynomial on the torus: (S(w,w') + conj S(w,w')) / 2, coefficients real."""
    out = {}
    for (a, b), c in S.items():
        for k in ((a, b), (-a, -b)):
            out[k] = out.get(k, 0) + c / 2
    return {k: v for k, v in out.items() if v}


RE = {(r, s): re_part(gram(r, s)) for r in range(9) for s in range(9)}
N = 9
