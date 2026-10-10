"""Exploration only (A32 pre-freeze research). Exact integer data for the nine relabelled
Fourier circles of act 26 at the single carrier, and checks of the single-circle conjugation.

Conventions follow the Lean record:
  M(z) = [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]], U = M/2,
  F(z)_i[j,k] = conj(U_ij) U_ik                         (FibreGram at A = Fin 1)
  relabel (pi,tau): G'_i[j,k] = G_{pi i}[tau j, tau k]
  mixedTriple G ((i1,i2,i3),(j1,j2,j3)) = G_i1[j1,j2] G_i2[j2,j3] G_i3[j3,j1]
On the unit circle every coordinate of a relabelled Fourier tuple is S z^m / 64, S = +-1.
"""
import itertools
from fractions import Fraction

IDX4 = range(4)
COORDS = [((i1, i2, i3), (j1, j2, j3)) for i1 in IDX4 for i2 in IDX4 for i3 in IDX4
          for j1 in IDX4 for j2 in IDX4 for j3 in IDX4]

# M entries as (sign, exponent of z)
MS = [[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]]
ME = [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0], [0, 1, 0, 1]]


def entry(i, j, k):
    """F(z)_i[j,k] * 4 = conj(M_ij) M_ik = s z^e (conj z = z^-1 on the unit circle)."""
    return MS[i][j] * MS[i][k], ME[i][k] - ME[i][j]


def perm_apply(p, x):
    return p[x]


def coord_data(pi, tau):
    """Return dict coord -> (S, m) for the relabelled tuple (pi,tau) F(z); value S z^m / 64."""
    out = {}
    for (i1, i2, i3), (j1, j2, j3) in COORDS:
        a = (pi[i1], tau[j1], tau[j2])
        b = (pi[i2], tau[j2], tau[j3])
        c = (pi[i3], tau[j3], tau[j1])
        s1, e1 = entry(*a)
        s2, e2 = entry(*b)
        s3, e3 = entry(*c)
        out[((i1, i2, i3), (j1, j2, j3))] = (s1 * s2 * s3, e1 + e2 + e3)
    return out


ID = (0, 1, 2, 3)


def swap(a, b):
    p = list(ID)
    p[a], p[b] = p[b], p[a]
    return tuple(p)


REPS1 = [ID, swap(2, 3), swap(1, 2)]
R = [(a, b) for a in REPS1 for b in REPS1]  # a26_1_circle_count's list, same order


def circle_vectors(pi, tau):
    """(c, A, B) with x(z) = c + A z + B conj(z) (real integer vectors, scaled by 64)."""
    d = coord_data(pi, tau)
    c = [0] * len(COORDS)
    A = [0] * len(COORDS)
    B = [0] * len(COORDS)
    for n, p in enumerate(COORDS):
        S, m = d[p]
        assert m in (-1, 0, 1), (p, m)
        if m == 0:
            c[n] = S
        elif m == 1:
            A[n] = S
        else:
            B[n] = S
    return c, A, B


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


if __name__ == "__main__":
    vecs = [circle_vectors(*r) for r in R]
    # real structure: x(z) = c + (A+B) cos t + i (A-B) sin t
    cos_v = [[a + b for a, b in zip(A, B)] for (_, A, B) in vecs]
    sin_v = [[a - b for a, b in zip(A, B)] for (_, A, B) in vecs]
    cen = [c for (c, _, _) in vecs]
    print("exponents all in {-1,0,1}: ok")
    print("sine Gram (x64^2):")
    for u in sin_v:
        print([dot(u, v) for v in sin_v])
    print("cosine Gram:")
    for u in cos_v:
        print([dot(u, v) for v in cos_v])
    print("|cos|^2 == |sin|^2 each circle:", all(dot(cos_v[k], cos_v[k]) == dot(sin_v[k], sin_v[k]) for k in range(9)))
    print("cos . sin (same circle, real parts only so trivially 0 in ambient)")
    print("centre - centre Gram (to c0):")
    diffs = [[a - b for a, b in zip(cen[k], cen[0])] for k in range(9)]
    for u in diffs:
        print([dot(u, v) for v in diffs])
    print("centre_k . cos_j:")
    for k in range(9):
        print([dot(cen[k], cos_v[j]) for j in range(9)])
