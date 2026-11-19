"""Probe P5-QX3 (QPHEN Phase 1 r3, writer's checks). Exact F_2 arithmetic; no import from p1-p4.

On F_2^3 with coordinates (s, c1, c2) and ready support {(s, 1, 0): s in F_2}:
(1) L(s, c1, c2) = (s, s + c1, s + c2) agrees with the Fredkin gate (swap c1, c2 iff s = 1) on the
    sector c1 + c2 = 1, maps the ready support to (0,1,0), (1,0,1), and gives alpha = 0 with own-cell reads.
(2) Affine bijections of F_2^3 preserving Hamming weight everywhere: count and whether all are coordinate
    permutations.  Affine bijections routing on the ready support as L does: count.
(3) Fredkin preserves Hamming weight everywhere and is not affine.  Among all bijections of F_2^3 that
    preserve weight everywhere and route on the ready support, count those that are affine (expect 0).
"""
import itertools
from fractions import Fraction

V = list(itertools.product((0, 1), repeat=3))
w = lambda v: sum(v)
L = lambda v: (v[0], (v[0] + v[1]) % 2, (v[0] + v[2]) % 2)
F = lambda v: (v[0], v[2], v[1]) if v[0] else v

def is_affine_map(T):
    return all(tuple((a + b + c) % 2 for a, b, c in zip(T(x), T(y), T(z))) ==
               T(tuple((p + q + r) % 2 for p, q, r in zip(x, y, z))) for x, y, z in itertools.product(V, repeat=3))

def routes(T):
    imgs = [T((s, 1, 0)) for s in (0, 1)]
    # one excitation in exactly one field cell, which cell set by s, own-cell reads
    return all(i[1] + i[2] == 1 for i in imgs) and imgs[0][1:] != imgs[1][1:]

def alpha(T):
    imgs = [T((s, 1, 0)) for s in (0, 1)]
    PA = Fraction(sum(i[1] for i in imgs), 2); PB = Fraction(sum(i[2] for i in imgs), 2)
    PAB = Fraction(sum(i[1] * i[2] for i in imgs), 2)
    return PAB / (PA * PB)

def all_affine_bijections():
    for M in itertools.product((0, 1), repeat=9):
        A = [M[0:3], M[3:6], M[6:9]]
        for b in V:
            T = lambda v, A=A, b=b: tuple((sum(A[i][j] * v[j] for j in range(3)) + b[i]) % 2 for i in range(3))
            if len({T(v) for v in V}) == 8:
                yield A, b, T

if __name__ == '__main__':
    sector = [v for v in V if v[1] + v[2] == 1]
    print('(1) L = Fredkin on c1 + c2 = 1:', all(L(v) == F(v) for v in sector),
          '| L(ready support):', [L((s, 1, 0)) for s in (0, 1)], '| alpha =', alpha(L),
          '| weight conserved on ready support:', all(w(L((s, 1, 0))) == w((s, 1, 0)) for s in (0, 1)))
    wp, perm, rout = 0, 0, 0
    for A, b, T in all_affine_bijections():
        if all(w(T(v)) == w(v) for v in V):
            wp += 1
            perm += (b == (0, 0, 0) and all(sum(r) == 1 for r in A) and all(sum(A[i][j] for i in range(3)) == 1 for j in range(3)))
        rout += routes(T) and all(w(T((s, 1, 0))) == w((s, 1, 0)) for s in (0, 1))
    print('(2) globally weight-preserving affine bijections:', wp, '; coordinate permutations among them:', perm,
          '| affine bijections routing on the ready support with weight conserved there:', rout)
    print('(3) Fredkin weight-preserving everywhere:', all(w(F(v)) == w(v) for v in V), '| affine:', is_affine_map(F),
          '| routes:', routes(F))
    cnt = aff = 0
    for img in itertools.permutations(V):
        T = dict(zip(V, img)).__getitem__
        if all(w(T(v)) == w(v) for v in V) and routes(T):
            cnt += 1; aff += is_affine_map(T)
    print('    weight-preserving routing bijections of F_2^3:', cnt, '; affine among them:', aff)
