#!/usr/bin/env python3
"""Finite independent exact controls for the MaxCone design proof, in Q(i)."""
import argparse
import importlib.util
import itertools
import sys
from collections import Counter
from fractions import Fraction as R
from functools import lru_cache
from pathlib import Path

spec = importlib.util.spec_from_file_location('maxcone_gaussian', Path(__file__).with_name('gaussian_exact.py'))
g = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = g
spec.loader.exec_module(g)
G, I = g.G, g.I
matrix, eye, diag, add, scale, mul, adj = g.matrix, g.eye, g.diag, g.add, g.scale, g.mul, g.adj
tensor, trace, det, rank, extract = g.tensor, g.trace, g.det, g.rank, g.extract
E = eye(2)
pauli = [E, matrix([[0, 1], [1, 0]]), matrix([[0, -I], [I, 0]]), diag(1, -1)]
P0, P1 = diag(1, 0), diag(0, 1)
CNOT = matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
count = Counter()


def require(code, condition):
    if not bool(condition):
        raise AssertionError(code)
    count[code] += 1


def inner(A, B):
    return trace(mul(A, B))


def vec(v):
    return matrix([[a] for a in v])


def outer(v):
    return mul(v, adj(v))


def conj(B, A):
    return mul(mul(B, A), adj(B))


def block(U, V):
    return add(tensor(P0, U), tensor(P1, V))


def bloch(v):
    A = E
    for j in range(3):
        A = add(A, scale(v[j], pauli[j + 1]))
    return scale(R(1, 2), A)


@lru_cache(maxsize=None)
def table(A):
    return tuple(tuple(inner(tensor(pauli[j], pauli[k]), A) for k in range(4)) for j in range(4))


def ip(A, B):
    a, b = table(A), table(B)
    return sum(a[j][k] * b[j][k] for j in range(4) for k in range(4))


def psd(A):
    return A == adj(A) and all(det(extract(A, ix)).nonnegative()
        for n in range(1, 5) for ix in itertools.combinations(range(4), n))


def partial_transpose(A):
    return matrix([[A[2 * (j // 2) + k % 2][2 * (k // 2) + j % 2]
                    for k in range(4)] for j in range(4)])


def su_to(v, norm):
    if norm == 0:
        return E
    return scale(R(1, norm), matrix([[v[0][0].conj(), v[1][0].conj()], [-v[1][0], v[0][0]]]))


def run(mutation=None):
    count.clear()
    basis = [scale(R(1, 4), tensor(a, b)) for a in pauli for b in pauli]
    factor = 8 if mutation == 'trace-factor' else 4
    for A, B in itertools.product(basis, repeat=2):
        require('TRACE', ip(A, B) == factor * inner(A, B))
    directions = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0),
                  (0, 0, 1), (0, 0, -1), (R(3, 5), R(4, 5), 0), (R(1, 3), R(2, 3), R(2, 3))]
    for x, y in itertools.product(directions, repeat=2):
        A = tensor(bloch(x), bloch(y))
        require('PRODUCT-PSD', psd(A))
        require('PRODUCT-RANK', rank(A) in (1, 2, 4))
        homx, homy = (1,) + x, (1,) + y
        for T in basis:
            raw = sum(homx[j] * table(T)[j][k] * homy[k] for j in range(4) for k in range(4))
            require('PRODUCT-PAIR', raw == ip(T, A) == 4 * inner(T, A))

    vectors = [(1, 0), (0, 1), (I, 0), (R(3, 5), R(4, 5)),
               (3 * I / 5, R(4, 5)), (R(1, 3), R(2, 3) + 2 * I / 3)]
    entries = [(vec((0, 0)), 0)]
    entries += [(scale(t, vec(v)), t) for v in vectors for t in (1, 2)]
    for (a, na), (b, nb) in itertools.product(entries, repeat=2):
        Ua, Ub = su_to(a, na), su_to(b, nb)
        require('SU', mul(Ua, adj(Ua)) == E and det(Ua) == 1)
        require('SU', mul(Ub, adj(Ub)) == E and det(Ub) == 1)
        psi, prod = a + b, vec((na, 0, nb, 0))
        B = block(adj(Ua), adj(Ub))
        require('PURE-ORBIT', mul(B, prod) == psi)
        require('PURE-PROJECTOR', conj(B, outer(prod)) == outer(psi))
        c = na ** 2 + nb ** 2
        x = (R(2 * na * nb, c), 0, R(na ** 2 - nb ** 2, c)) if c else (0, 0, 0)
        require('PURE-PRODUCT', outer(prod) == scale(c, tensor(bloch(x), bloch((0, 0, 1)))))
        A, X = diag(1, 2, 3, 4), add(outer(psi), basis[6])
        badj = B if mutation == 'omit-adjoint' else adj(B)
        require('ADJOINT', ip(A, conj(B, X)) == ip(mul(mul(badj, A), B), X))

    cyclic = scale(R(1, 2), add(add(add(E, scale(-I, pauli[1])), scale(-I, pauli[2])), scale(-I, pauli[3])))
    local = tensor(E, cyclic)
    require('CYCLIC-SU', mul(cyclic, adj(cyclic)) == E and det(cyclic) == 1)
    phi = vec((1, 0, 0, 1))
    fixtures = [outer(phi), diag(1, 2, 3, 4), eye(4)]
    for U, A in itertools.product([CNOT, local], fixtures):
        transformed = conj(U, A)
        require('QUANTUM-CONTROL', psd(transformed) and rank(transformed) == rank(A))

    kappa = R(3, 2)
    expanded = matrix([[R(1, 2), 0, kappa / 2, 0], [0, R(1, 2), 0, kappa / 2],
                       [kappa / 2, 0, R(1, 2), 0], [0, kappa / 2, 0, R(1, 2)]])
    p = vec((1, 0, -1, 0))
    require('KAPPA-PRODUCT', mul(mul(adj(p), expanded), p)[0][0] == -R(1, 2))
    effect = tensor(bloch((-1, 0, 0)), bloch((0, 0, 1)))
    value = R(1, 4) if mutation == 'product-sign' else -R(1, 4)
    require('KAPPA-EFFECT', inner(expanded, effect) == value)
    for U in [CNOT, local]:
        transformed = conj(U, expanded)
        off = matrix([row[2:] for row in transformed[:2]])
        require('KAPPA-INSTANCES', extract(transformed, (0, 1)) == scale(R(1, 2), E)
                and extract(transformed, (2, 3)) == scale(R(1, 2), E)
                and mul(off, adj(off)) == scale(kappa ** 2 / 4, E))

    normalized = scale(R(1, 2), outer(phi))
    require('SCALE-CONTROL', trace(normalized) == 1 and trace(scale(2, normalized)) != 1)
    A, B = diag(1, 1, 0, 0), diag(0, 0, 1, 0)
    require('ADD-CONTROL', psd(A) and psd(B) and psd(add(A, B))
            and rank(A) == 2 and rank(B) == 1 and rank(add(A, B)) == 3)
    require('ZERO-H1-CONTROL', tensor(bloch((0, 0, 0)), bloch((0, 0, 0))) != scale(0, eye(4)))
    entangled = scale(R(1, 2), conj(CNOT, outer(vec((1, 0, 1, 0)))))
    pt = partial_transpose(entangled)
    require('SEPARABLE-GATE-CONTROL', psd(entangled) and det(extract(pt, (1, 2))) == -R(1, 4))
    return dict(sorted(count.items()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--self-test', action='store_true')
    args = ap.parse_args()
    counts = run()
    if args.self_test:
        for mutation, code in [('trace-factor', 'TRACE'), ('omit-adjoint', 'ADJOINT'),
                               ('product-sign', 'KAPPA-EFFECT')]:
            try:
                run(mutation)
            except AssertionError as error:
                if str(error) != code:
                    raise
                print('MUTATION', mutation, 'REJECTED', code)
            else:
                raise AssertionError('mutation escaped: ' + mutation)
        print('SELF-TEST PASS; positive fixture and 3 mutations')
    else:
        for key, value in counts.items():
            print(key + ': PASS (' + str(value) + ')')
        print('MAXCONE-EXACT: PASS; ' + str(sum(counts.values())) + ' finite exact checks')


if __name__ == '__main__':
    main()
