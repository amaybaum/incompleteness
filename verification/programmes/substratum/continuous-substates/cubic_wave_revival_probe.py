#!/usr/bin/env python3
"""Exact controls for cubic-wave-revival.md; added torus/readout candidate only."""
import itertools
import json
from fractions import Fraction as Q
from functools import reduce
from math import gcd


def require(condition, reason):
    if not condition:
        raise AssertionError(reason)


def row(v, M):
    return [sum(v[i]*M[i][j] for i in range(len(v))) for j in range(len(M[0]))]


def multiply(A, B):
    return [row(v, B) for v in A]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def main():
    sites = list(itertools.product(range(3), repeat=3))
    idx = {p: i for i, p in enumerate(sites)}
    n = len(sites)
    A = [[0]*n for _ in range(n)]
    for p, i in idx.items():
        for axis in range(3):
            for direction in (-1, 1):
                q = list(p)
                q[axis] = (q[axis]+direction) % 3
                A[i][idx[tuple(q)]] += 1
    I = identity(n)
    F = [A[i]+[-x for x in I[i]] for i in range(n)] + [I[i]+[0]*n for i in range(n)]
    inverse = [[0]*n+I[i] for i in range(n)] + [[-x for x in I[i]]+A[i] for i in range(n)]
    require(multiply(F, inverse) == multiply(inverse, F) == identity(2*n), 'two-sided integer inverse')
    require(row([1]*n, A) == [6]*n, 'uniform mode eigenvalue six')
    h = [2, -1, -1]
    v = [h[x]*h[y] for x, y, z in sites]
    require(any(v) and reduce(gcd, map(abs, v)) == 1, 'nonzero primitive readout')
    require(1 in v, 'unit coefficient for explicit Haar coordinate change')
    require(row(v, A) == [0]*n, 'zero eigenmode')
    w = v+[0]*n
    ws = [w]
    for _ in range(4):
        ws.append(row(ws[-1], F))
    require(ws[1] == [0]*n+[-a for a in v], 'step one reads previous slice')
    require(ws[2] == [-a for a in w], 'step two negates readout')
    require(ws[4] == w, 'step four returns readout')
    require(any(ws[1][n:]) and not any(w[n:]), 'rank two at step one')
    # A single current-site readout has rank-two (root,time2) forms, so
    # its Haar rooted map is J2 at both steps one and two.
    local = [int(i == 0) for i in range(2*n)]
    local1 = row(local, F)
    local2 = row(local1, F)
    require(any(local1[n:]) and any(local2[n:]), 'single-site previous-slice dependence')
    require(local2 != local and local2 != [-a for a in local], 'single-site fails two-step return/flip')
    # Independent finite-subgroup enumeration on two quotient coordinates.
    # These finite counts are controls, not the Haar/all-state proof.
    grids = []
    for N in (4, 8, 16):
        counts = [[[0, 0], [0, 0]] for _ in range(3)]
        bit = lambda x: int(x % N >= N//2)
        for a, b in itertools.product(range(N), repeat=2):
            for t, y in enumerate((a, -b, -a)):
                counts[t][bit(a)][bit(y)] += 1
        gamma = [[[Q(c, sum(r)) for c in r] for r in M] for M in counts]
        require(gamma[1] == [[Q(1, 2)]*2]*2, ('grid step one', N))
        swap = [[Q(0), Q(1)], [Q(1), Q(0)]]
        errors = [sum(abs(gamma[2][i][j]-swap[i][j]) for j in (0, 1))/2 for i in (0, 1)]
        require(errors == [Q(2, N)]*2, ('finite-grid endpoint correction', N))
        distance = sum(abs(gamma[2][0][j]-gamma[2][1][j]) for j in (0, 1))/2
        require(distance == 1-Q(4, N), ('finite-grid revival distance', N))
        grids.append({'N': N, 'time2_row_distance': str(distance), 'swap_error_per_row': str(errors[0])})
    print(json.dumps({'status': 'PASS', 'sites': n, 'integer_inverse': True,
                      'primitive_readout': True, 'vA': 0, 'vF2': '-v', 'vF4': 'v',
                      'Haar_Gamma1': 'J2', 'Haar_Gamma2': 'swap a.e.',
                      'single_site_Haar_Gamma1_Gamma2': 'J2; no revival on this pair',
                      'finite_grid_controls': grids,
                      'scope': 'mathematical torus extension and distributed observable; native physical availability open'}, sort_keys=True))


if __name__ == '__main__':
    main()
