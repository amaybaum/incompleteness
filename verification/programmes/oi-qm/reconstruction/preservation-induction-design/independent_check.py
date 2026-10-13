#!/usr/bin/env python3
"""Independent exact checker: rational complex arithmetic and Kraus paths.

Imports neither SymPy nor exact_check.py; does not interpret a protocol AST.
Uses all principal minors of the final 2x2 matrices for the positive checks.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json


@dataclass(frozen=True)
class Q:
    r: F = F(0)
    i: F = F(0)

    def __add__(a, b):
        return Q(a.r+b.r, a.i+b.i)

    def __neg__(a):
        return Q(-a.r, -a.i)

    def __sub__(a, b):
        return a+-b

    def __mul__(a, b):
        return Q(a.r*b.r-a.i*b.i, a.r*b.i+a.i*b.r)

    def star(a):
        return Q(a.r, -a.i)


zero = Q()
one = Q(F(1))


def mat(rows):
    return [[z if isinstance(z, Q) else Q(F(z)) for z in row] for row in rows]


def zeros(n):
    return [[zero for _ in range(n)] for _ in range(n)]


def add(a, b):
    return [[x+y for x, y in zip(r, t)] for r, t in zip(a, b)]


def mul(a, b):
    return [[sumq(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def sumq(items):
    out = zero
    for x in items:
        out = out+x
    return out


def star(a):
    return [[a[j][i].star() for j in range(len(a))] for i in range(len(a[0]))]


def scale(c, a):
    return [[Q(F(c))*z for z in row] for row in a]


def conj(k, x):
    return mul(mul(k, x), star(k))


checks = []


def check(name, condition):
    if condition is not True:
        raise AssertionError(name)
    checks.append(name)


def trace(x):
    return sumq(x[i][i] for i in range(len(x)))


def psd2(x):
    if x != star(x):
        return False
    determinant = x[0][0]*x[1][1]-x[0][1]*x[1][0]
    return all(z.i == 0 and z.r >= 0 for z in (x[0][0], x[1][1], determinant))


def diagonal_positive(x):
    return psd2(x) and x[0][1] == zero


def canon(x):
    return [[[str(z.r), str(z.i)] for z in row] for row in x]


def inner_branch(x, outcome):
    # Enumerate the uniform ancilla preparations and both discarded labels.
    # Native last-register readout retains b=outcome. The conditional CNOT
    # at outcome 1 maps (system j, first ancilla a) -> (j, a XOR j).
    y = zeros(2)
    for a in range(2):
        for b in range(2):
            for r in range(2):
                for t in range(2):
                    k = zeros(2)
                    for j in range(2):
                        target_a = a ^ j if outcome else a
                        if b == outcome and r == target_a and t == b:
                            k[j][j] = one
                    y = add(y, scale(F(1, 4), conj(k, x)))
    return y


swap = mat([[0, 1], [1, 0]])
rotation = mat([[F(3, 5), -F(4, 5)], [F(4, 5), F(3, 5)]])
identity = mat([[1, 0], [0, 1]])
inputs = [('classical-0', mat([[1, 0], [0, 0]])),
          ('classical-1', mat([[0, 0], [0, 1]])),
          ('classical-mixed', mat([[F(2, 3), 0], [0, F(1, 3)]])),
          ('quantum-complex', mat([[F(1, 2), Q(F(0), -F(1, 2))],
                                   [Q(F(0), F(1, 2)), F(1, 2)]])),
          ('quantum-real', mat([[F(9, 25), F(12, 25)], [F(12, 25), F(16, 25)]]))]
manifest = {}
for name, x in inputs:
    quantum = name.startswith('quantum')
    branches = [conj(rotation if quantum else swap, inner_branch(x, 0)),
                conj(swap, inner_branch(x, 1)), zeros(2)]
    check('trace:'+name, sumq(trace(y) for y in branches) == trace(x))
    check('empty-coarse:'+name, branches[2] == zeros(2))
    for a, y in enumerate(branches):
        check('PSD:'+name+str(a), psd2(y))
        if not quantum:
            check('diagonal:'+name+str(a), diagonal_positive(y))
    manifest[name] = [canon(y) for y in branches]

# Countercontrols via different formulas. H conjugation is HH^T/2, so no
# irrational numbers enter the independent arithmetic implementation.
h_numerator = mat([[1, 1], [1, -1]])
p0 = mat([[1, 0], [0, 0]])
had = scale(F(1, 2), conj(h_numerator, p0))
check('Hadamard-normalization', scale(F(1, 2), mul(star(h_numerator), h_numerator)) == identity)
check('Hadamard-off-diagonal', had[0][1] == Q(F(1, 2)))
check('Hadamard-trace', trace(had) == one)
check('readout-non-isometry', mul(star(p0), p0) != identity)
check('scalar-readout-failure', p0 != scale(F(1, 2), identity))
check('scalar-readout-aggregate', add(p0, mat([[0, 0], [0, 1]])) == identity)
check('label-cone-not-scalar', conj(swap, p0) != scale(F(1, 2), identity))
# Independent compression formula: each of the two uniform ancilla blocks
# contributes HH^T/4; their partial-trace sum is HH^T/2.
one_block = scale(F(1, 4), conj(h_numerator, p0))
discard_out = add(one_block, one_block)
check('discard-enlarged-failure', discard_out == had and not diagonal_positive(discard_out))
check('discard-enlarged-normalized', trace(discard_out) == one)

payload = json.dumps(manifest, sort_keys=True, separators=(',', ':'))
print('SAMPLE-MANIFEST-SHA256', hashlib.sha256(payload.encode()).hexdigest())
print('INDEPENDENT-CONTROLS', len(checks))
print('CHECKED: rational Kraus-path calculation, finite examples only')
