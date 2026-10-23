#!/usr/bin/env python3
"""Round PRESERVE-INDUCT-1 -- an independent exact check of the finite instances.

A second implementation of the finite examples of preserve_induct1_probe.py, written separately:
it imports neither SymPy nor that script, uses its own rational complex arithmetic from the
Python standard library, and does not interpret a protocol tree. It enumerates the uniform
ancilla preparations, the retained register label and the discarded labels as Kraus paths of
the same protocol, and checks, on the same five inputs:

  I-TRACE     the branch traces sum to the input trace
  I-EMPTY     the empty coarse-graining fibre is zero
  I-PSD       every final 2x2 branch is positive semidefinite (Hermitian, both diagonal entries
              and the determinant nonnegative)
  I-DIAG      every final branch of a classical input is nonnegative diagonal
  I-HADAMARD  an isometric conjugation leaves the diagonal cone (HH^T/2, rational entries only)
  I-READOUT   a register projection is not an isometry and leaves the scalar cone, while the
              readout total is normalized
  I-DISCARD   an enlarged-carrier conjugation leaves the diagonal cone after partial trace
  I-SEPARATE  SymPy and the primary script were not imported
  I-MANIFEST  the sample manifest of every final branch has the frozen digest, the same one the
              primary script must reach

It ends with 'preserve_induct1_indep_check: OK -- N checks' when everything passes; otherwise with
'preserve_induct1_indep_check: FAILED -- ...' and exit 1. Finite exact examples only.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
import sys

MANIFEST_SHA256 = 'a1f82e289ba07a4c60dd6b56396dcdf7c0c217b2ff49a8d779f1c4e923842ea9'
CODES = ['I-TRACE', 'I-EMPTY', 'I-PSD', 'I-DIAG', 'I-HADAMARD', 'I-READOUT', 'I-DISCARD',
         'I-SEPARATE', 'I-MANIFEST']
counts = {c: 0 for c in CODES}
failures = []


def check(code, name, condition):
    counts[code] += 1
    if condition is not True:
        failures.append('%s %s' % (code, name))


@dataclass(frozen=True)
class Q:
    r: F = F(0)
    i: F = F(0)

    def __add__(a, b):
        return Q(a.r + b.r, a.i + b.i)

    def __neg__(a):
        return Q(-a.r, -a.i)

    def __sub__(a, b):
        return a + -b

    def __mul__(a, b):
        return Q(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r)

    def star(a):
        return Q(a.r, -a.i)


zero = Q()
one = Q(F(1))


def mat(rows):
    return [[z if isinstance(z, Q) else Q(F(z)) for z in row] for row in rows]


def zeros(n):
    return [[zero for _ in range(n)] for _ in range(n)]


def add(a, b):
    return [[x + y for x, y in zip(r, t)] for r, t in zip(a, b)]


def sumq(items):
    out = zero
    for x in items:
        out = out + x
    return out


def mul(a, b):
    return [[sumq(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def star(a):
    return [[a[j][i].star() for j in range(len(a))] for i in range(len(a[0]))]


def scale(c, a):
    return [[Q(F(c)) * z for z in row] for row in a]


def conj(k, x):
    return mul(mul(k, x), star(k))


def trace(x):
    return sumq(x[i][i] for i in range(len(x)))


def psd2(x):
    if x != star(x):
        return False
    determinant = x[0][0] * x[1][1] - x[0][1] * x[1][0]
    return all(z.i == 0 and z.r >= 0 for z in (x[0][0], x[1][1], determinant))


def diagonal_positive(x):
    return psd2(x) and x[0][1] == zero


def canon(x):
    return [[[str(z.r), str(z.i)] for z in row] for row in x]


def inner_branch(x, outcome):
    # The uniform ancilla preparations a, b and both discarded labels r, t. The native readout of
    # the last register keeps b = outcome; the outcome-1 continuation CNOT sends (j, a) to
    # (j, a XOR j).
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
          ('quantum-complex', mat([[F(1, 2), Q(F(0), -F(1, 2))], [Q(F(0), F(1, 2)), F(1, 2)]])),
          ('quantum-real', mat([[F(9, 25), F(12, 25)], [F(12, 25), F(16, 25)]]))]
manifest = {}
for name, x in inputs:
    quantum = name.startswith('quantum')
    branches = [conj(rotation if quantum else swap, inner_branch(x, 0)), conj(swap, inner_branch(x, 1)), zeros(2)]
    check('I-TRACE', name, sumq(trace(y) for y in branches) == trace(x))
    check('I-EMPTY', name, branches[2] == zeros(2))
    for a, y in enumerate(branches):
        check('I-PSD', name + str(a), psd2(y))
        if not quantum:
            check('I-DIAG', name + str(a), diagonal_positive(y))
    manifest[name] = [canon(y) for y in branches]

h_numerator = mat([[1, 1], [1, -1]])
p0 = mat([[1, 0], [0, 0]])
had = scale(F(1, 2), conj(h_numerator, p0))
check('I-HADAMARD', 'normalization', scale(F(1, 2), mul(star(h_numerator), h_numerator)) == identity)
check('I-HADAMARD', 'off-diagonal', had[0][1] == Q(F(1, 2)))
check('I-HADAMARD', 'trace', trace(had) == one)
check('I-HADAMARD', 'leaves the diagonal cone', not diagonal_positive(had))
check('I-READOUT', 'not an isometry', mul(star(p0), p0) != identity)
check('I-READOUT', 'leaves the scalar cone', p0 != scale(F(1, 2), identity))
check('I-READOUT', 'total normalized', add(p0, mat([[0, 0], [0, 1]])) == identity)
check('I-READOUT', 'a relabelled projection is not scalar', conj(swap, p0) != scale(F(1, 2), identity))
# Each of the two uniform ancilla blocks contributes HH^T/4; their partial-trace sum is HH^T/2.
one_block = scale(F(1, 4), conj(h_numerator, p0))
discard_out = add(one_block, one_block)
check('I-DISCARD', 'leaves the diagonal cone', discard_out == had and not diagonal_positive(discard_out))
check('I-DISCARD', 'normalized', trace(discard_out) == one)
check('I-SEPARATE', 'no SymPy', 'sympy' not in sys.modules)
check('I-SEPARATE', 'no primary script', 'preserve_induct1_probe' not in sys.modules)

payload = json.dumps(manifest, sort_keys=True, separators=(',', ':'))
digest = hashlib.sha256(payload.encode()).hexdigest()
check('I-MANIFEST', 'digest', digest == MANIFEST_SHA256)

for c in CODES:
    bad = [f for f in failures if f.split(' ', 1)[0] == c]
    print(('PASS %s (%d)' % (c, counts[c])) if not bad and counts[c] else ('FAIL %s (%d): %s' % (c, counts[c], '; '.join(bad))))
print('SAMPLE-MANIFEST-SHA256 %s' % digest)
n = sum(counts.values())
nfail = len(failures) + sum(1 for c in CODES if not counts[c])
print('checks: %d, failures: %d' % (n, nfail))
if nfail:
    print('preserve_induct1_indep_check: FAILED -- %d failure(s)' % nfail)
    sys.exit(1)
print('preserve_induct1_indep_check: OK -- %d checks' % n)
