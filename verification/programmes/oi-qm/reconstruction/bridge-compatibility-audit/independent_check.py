#!/usr/bin/env python3
"""Separate exact implementation of the depth-one witness.

Standard-library rational pairs and sparse matrices; no probe imports, SymPy,
Kraus-block extraction, or use of the stopped closed form to compute the output.
Builds the balanced circuit by composing H, Toffoli, S, Toffoli, H.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
IMAG = (F(0), F(1))


def q(r=0, i=0):
    return (F(r), F(i))


def plus(x, y):
    return (x[0] + y[0], x[1] + y[1])


def times(x, y):
    return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])


def conjugate(x):
    return (x[0], -x[1])


def put(a, row, col, z):
    z = plus(a.get((row, col), ZERO), z)
    if z == ZERO:
        a.pop((row, col), None)
    else:
        a[row, col] = z


def scale(a, z):
    return {ij: times(x, z) for ij, x in a.items() if times(x, z) != ZERO}


def add(*arrays):
    result = {}
    for a in arrays:
        for (r, c), z in a.items():
            put(result, r, c, z)
    return result


def multiply(a, b):
    result = {}
    for (r, k), x in a.items():
        for (l, c), y in b.items():
            if k == l:
                put(result, r, c, times(x, y))
    return result


def adjoint(a):
    return {(c, r): conjugate(z) for (r, c), z in a.items()}


def identity(n):
    return {(r, r): ONE for r in range(n)}


def tensor(a, b, bsize):
    return {(r*bsize+t, c*bsize+u): times(x, y)
            for (r, c), x in a.items() for (t, u), y in b.items()}


def act(u, a):
    return multiply(multiply(u, a), adjoint(u))


def trace(a):
    z = ZERO
    for (r, c), x in a.items():
        if r == c:
            z = plus(z, x)
    return z


def pairing(a, b):
    return trace(multiply(a, b))


checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


root = Path(__file__).resolve().parents[5]
source = root / 'verification/lean-mathlib/OIBridge/BridgeFiniteProtocol.lean'
check('adopted source digest', sha256(source.read_bytes()).hexdigest() ==
      '9ae957839f49f57222bb968741d04b17496d2d355a47ab7918b0b6149d8aaba8')

# The two unnormalized Hadamards together are divided by 2.
h = {(r, c): q(F((-1)**((r & c).bit_count()), 2))
     for r in range(4) for c in range(4)}
hh = tensor(identity(2), h, 4)
toffoli = {(r ^ 4 if r % 4 == 3 else r, r): ONE for r in range(8)}
phase = {(r, r): ONE if r < 4 else IMAG for r in range(8)}
u = multiply(multiply(multiply(multiply(hh, toffoli), phase), toffoli), hh)
check('composed circuit unitary', multiply(adjoint(u), u) == identity(8))
# Cross-check composed gates against the adopted rank-one entry definition.
signs = (1, -1, -1, 1)
literal = {}
for r in range(8):
    for c in range(8):
        if r // 4 == c // 4:
            base = (ONE if r < 4 else IMAG) if r % 4 == c % 4 else ZERO
            coeff = q(F(-1, 4), F(1, 4)) if r < 4 else q(F(1, 4), F(-1, 4))
            put(literal, r, c, plus(base, times(coeff, q(signs[r % 4]*signs[c % 4]))))
check('gate circuit equals adopted entries', u == literal)
us = tensor(identity(2), u, 8)


def readout(a, j):
    return {(r, c): z for (r, c), z in a.items() if r % 4 == c % 4 == j}


def discard(a):
    result = {}
    for (r, c), z in a.items():
        if r % 4 == c % 4:
            put(result, r // 4, c // 4, z)
    return result


def direct_branches(x, reset=True, correction=True):
    attached = scale(tensor(x, identity(4), 4), q(F(1, 4)))
    if reset:
        parts = []
        for j in range(4):
            swap = {(r // 4 * 4 + (0 if r % 4 == j else j if r % 4 == 0 else r % 4), r): ONE
                    for r in range(16)}
            parts.append(act(swap, readout(attached, j)))
        attached = add(*parts)
    evolved = act(us, attached)
    result = []
    for j in range(4):
        measured = readout(evolved, j)
        if correction:
            diagonal = {(r, r): q(1 if j == 0 or (r // 4) % 2 == 0 else -1)
                        for r in range(16)}
            measured = act(diagonal, measured)
        result.append(discard(measured))
    return result


b = {(r, c): q(F(1, 2)) for r in (0, 3) for c in (0, 3)}
p = {(1, 1): q(F(1, 2)), (2, 2): q(F(1, 2)),
     (1, 2): q(0, F(1, 2)), (2, 1): q(0, F(-1, 2))}
w = {(2*(r//2)+c%2, 2*(c//2)+r%2): z for (r, c), z in p.items()}
check('Bell positive projector', adjoint(b) == b and multiply(b, b) == b and trace(b) == ONE)
check('P positive projector', adjoint(p) == p and multiply(p, p) == p and trace(p) == ONE)
check('witness zero on Bell generator', pairing(w, b) == ZERO)
ds = {(r, r): ONE if r % 2 == 0 else q(F(3, 5), F(4, 5)) for r in range(4)}
for r in range(4):
    for c in range(4):
        x = {(r, c): ONE}
        branches = direct_branches(x)
        check('full-register success ' + str((r, c)), branches[0] == scale(act(ds, x), q(F(5, 8))))
        check('full-register failures ' + str((r, c)),
              all(a == scale(x, q(F(1, 8))) for a in branches[1:]))

out = add(*direct_branches(b))
expected = {(0, 0): q(F(1, 2)), (3, 3): q(F(1, 2)),
            (0, 3): q(F(3, 8), F(-1, 4)), (3, 0): q(F(3, 8), F(1, 4))}
check('depth-one matrix', out == expected)
check('depth-one separator', pairing(w, out) == q(F(-1, 4)))
check('density Hermitian/trace', adjoint(out) == out and trace(out) == ONE)
minor = plus(times(out[0, 0], out[3, 3]), times(q(-1), times(out[0, 3], out[3, 0])))
check('density PSD principal minor', minor == q(F(3, 64)))
check('zero-depth control', pairing(w, b) == ZERO)
check('missing reset rejected', direct_branches(b, reset=False)[0] != direct_branches(b)[0])
check('missing correction rejected', direct_branches(b, correction=False)[1] != direct_branches(b)[1])
check('opposite witness rejected', pairing(adjoint({ij: conjugate(z) for ij, z in w.items()}), out) == q(F(1, 4)))
check('identity target rejected', direct_branches(b)[0] != scale(b, q(F(5, 8))))

# This explicitly demonstrates why CNOT preservation is not a retained premise.
local = {(0, 0): q(F(1, 2)), (1, 1): q(F(1, 2)),
         (0, 1): q(0, F(-1, 2)), (1, 0): q(0, F(1, 2))}
product = tensor(local, {(0, 0): ONE}, 2)
cnot = {(r ^ 1 if r // 2 else r, r): ONE for r in range(4)}
check('CNOT fails this K', pairing(w, act(cnot, product)) == q(F(-1, 2)))

# Historical K(Z_F): explicit dual witness, checked by this direct simulation.
x = {(0, 1): ONE, (1, 0): ONE}
y = {(0, 1): q(0, -1), (1, 0): IMAG}
z = {(0, 0): ONE, (1, 1): q(-1)}
defects = [scale(add(identity(4), scale(tensor(x, z, 2), q(s)),
                     scale(tensor(y, y, 2), q(t)), scale(tensor(z, x, 2), q(-s*t))), q(F(1, 16)))
           for s in (-1, 1) for t in (-1, 1)]
vector = (q(F(1, 2)), q(0, F(-1, 2)), q(F(1, 2)), q(0, F(1, 2)))
test = {(r, c): times(vector[r], conjugate(vector[c])) for r in range(4) for c in range(4)}
check('ZF test PSD projector', adjoint(test) == test and multiply(test, test) == test and trace(test) == ONE)
check('ZF test nonnegative on all defects', [pairing(test, e) for e in defects] ==
      [ZERO, ZERO, q(F(1, 8)), q(F(1, 8))])
check('ZF input generator zero pairing', pairing(test, defects[1]) == ZERO)
check('ZF drive witness', pairing(test, act(ds, defects[1])) == q(F(-1, 10)))
check('ZF actual depth-one witness', pairing(test, add(*direct_branches(defects[1]))) == q(F(-1, 16)))

print('INDEPENDENT CHECK: PASS;', len(checks), 'exact controls')
print('depth-one output:', sorted(out.items()))
print('separating matrix trace: -1/4; PSD minor: 3/64')
print('CNOT product countercontrol: -1/2')
print('ZF generator index 1: drive trace -1/10; actual depth-one trace -1/16')
print('SCOPE: finite-protocol availability does not imply preservation of this given pair cone.')
