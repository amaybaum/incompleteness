"""Exploratory exact probe of the registered InstAvail-to-pair-cone bridge.

Uses the actual BridgeFiniteProtocol circuit/reset/correction definitions.
Does not certify a physical cone, a native round, or a new Lean theorem.
"""
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[5]
Q, I = s.Rational, s.I

def simple(m):
    return m.applyfunc(s.simplify)

def same(a, b):
    return simple(a - b) == s.zeros(*a.shape)

def unit(n, a, b):
    m = s.zeros(n); m[a, b] = 1
    return m

def pt(m):
    return s.Matrix(4, 4, lambda a, b: m[(a // 2) * 2 + b % 2,
                                        (b // 2) * 2 + a % 2])

checks = []
def control(label, condition):
    checks.append((label, bool(condition)))
    if not condition:
        raise AssertionError('Failed control: ' + label)

source = (ROOT / 'verification/lean-mathlib/OIBridge/BridgeFiniteProtocol.lean').read_text()
for pin in ['3 / 5 + (4 / 5) * Complex.I',
            'if a = 1 ∨ a = 2 then -1 else 1',
            '(Equiv.refl Token).prodCongr (Equiv.swap j 0)',
            '((if r.1 = 0 then Complex.I - 1 else 1 - Complex.I) / 4) * v r.2 * v c.2',
            'if j = 0 ∨ r.1 = 0 then 1 else -1',
            '| k + 1 => ∑ j : Fin 4, (if j = 0 then LinearMap.id else stopped F k).comp (F j)']:
    control('actual kernel definition: ' + pin, pin in source)

D = s.diag(1, Q(3, 5) + Q(4, 5) * I)
signs = [1, -1, -1, 1]
def entry(a, b):
    r, f, t, e = a // 4, a % 4, b // 4, b % 4
    if r != t: return 0
    diagonal = (1 if r == 0 else I) if f == e else 0
    factor = (I - 1 if r == 0 else 1 - I) / 4
    return diagonal + factor * signs[f] * signs[e]

U = s.Matrix(8, 8, entry)
control('balanced circuit isometry', same(U.H * U, s.eye(8)))
control('drive phase isometry', same(D.H * D, s.eye(2)))

projectors, resets, corrections = [], [], []
for j in range(4):
    projectors.append(s.diag(*[int(a % 4 == j) for a in range(8)]))
    reset = s.zeros(8)
    for a in range(8):
        f = a % 4
        moved = 0 if f == j else j if f == 0 else f
        reset[(a // 4) * 4 + moved, a] = 1
    resets.append(reset)
    control('reset swap isometry ' + str(j), same(reset.H * reset, s.eye(8)))
    corrections.append(s.diag(*[1 if j == 0 or a < 4 else -1 for a in range(8)]))

for a in range(2):
    for b in range(2):
        x = unit(2, a, b)
        attached = s.kronecker_product(x, s.eye(4)) / 4
        reset = sum((resets[j] * projectors[j] * attached * projectors[j] * resets[j].H
                     for j in range(4)), s.zeros(8))
        control('reset uniform ancilla matrix unit ' + str((a, b)),
                same(reset, s.kronecker_product(x, unit(4, 0, 0))))

ks = [s.Matrix(2, 2, lambda a, b: (corrections[j] * U)[a * 4 + j, b * 4])
      for j in range(4)]
def apply(k, x):
    return simple(k * x * k.H)

for a in range(2):
    for b in range(2):
        x = unit(2, a, b)
        control('derived success branch ' + str((a, b)), same(apply(ks[0], x), Q(5, 8) * apply(D, x)))
        for j in range(1, 4):
            control('derived failure branch ' + str((j, a, b)), same(apply(ks[j], x), x / 8))
control('branch trace normalization', same(sum((k.H * k for k in ks), s.zeros(2)), s.eye(2)))

# Sum the failure branches before recurring, using linearity of every channel.
spectator_ks = [s.kronecker_product(s.eye(2), k) for k in ks]
Ds = s.kronecker_product(s.eye(2), D)
def stopped(x, depth):
    if depth == 0: return x
    success = apply(spectator_ks[0], x)
    failure = sum((apply(k, x) for k in spectator_ks[1:]), s.zeros(4))
    return simple(success + stopped(failure, depth - 1))

for depth in range(5):
    r = Q(3, 8) ** depth
    for a in range(4):
        for b in range(4):
            x = unit(4, a, b)
            control('stopped spectator matrix unit ' + str((depth, a, b)),
                    same(stopped(x, depth), (1-r) * apply(Ds, x) + r*x))

B = s.zeros(4)
for a in [0, 3]:
    for b in [0, 3]: B[a, b] = Q(1, 2)
control('Bell input is a normalized positive rank-one generator',
        same(B.H, B) and same(B * B, B) and B.trace() == 1)
# P is the projector onto (|01> - i|10>)/sqrt(2), expressed without radicals.
P = s.zeros(4); P[1, 1] = P[2, 2] = Q(1, 2)
P[1, 2] = I / 2; P[2, 1] = -I / 2
W = pt(P)
control('witness is partial transpose of a positive rank-one projector',
        same(P.H, P) and same(P * P, P) and P.trace() == 1)
control('Bell generator has zero witness', s.simplify((W * B).trace()) == 0)
control('zero-depth countercontrol', s.simplify((W * stopped(B, 0)).trace()) == 0)

# Match the native W(3) dictionary independently at the exhibited matrices.
pauli = [s.eye(2), s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-I],[I,0]]), s.diag(1,-1)]
def table(m):
    return s.Matrix(4, 4, lambda a, b: s.simplify((s.kronecker_product(pauli[a], pauli[b]) * m).trace()))
def dictionary(t):
    return simple(sum((t[a,b] * s.kronecker_product(pauli[a], pauli[b]) / 4
                       for a in range(4) for b in range(4)), s.zeros(4)))
control('native Pauli dictionary Bell round-trip', same(dictionary(table(B)), B))
control('native Pauli dictionary witness round-trip', same(dictionary(table(W)), W))
control('native Pauli dictionary stopped round-trip', same(dictionary(table(stopped(B,1))), stopped(B,1)))
control('matrix/table trace normalization',
        s.simplify(sum(table(W)[a,b] * table(stopped(B,1))[a,b]
                       for a in range(4) for b in range(4)) - 4*(W*stopped(B,1)).trace()) == 0)

# Supplement the universal product proof with explicit exact product controls.
points = [(0,0,0), (1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1),
          (Q(3,5),Q(4,5),0)]
for x in points:
    for y in points:
        A = (s.eye(2) + sum((x[j]*pauli[j+1] for j in range(3)), s.zeros(2))) / 2
        C = (s.eye(2) + sum((y[j]*pauli[j+1] for j in range(3)), s.zeros(2))) / 2
        value = s.simplify((W*s.kronecker_product(A,C)).trace())
        control('product witness nonnegativity ' + str((x,y)), value.is_nonnegative)

# Negative controls must reject mistakes in reset/correction and in the separating datum.
off = unit(2, 0, 1)
def no_reset_branch(j, x):
    out = s.zeros(2)
    for e in range(4):
        k = s.Matrix(2, 2, lambda a,b: (corrections[j]*U)[a*4+j,b*4+e])
        out += apply(k,x) / 4
    return simple(out)
control('removing reset breaks the independently derived success branch',
        not same(no_reset_branch(0,off), Q(5,8)*apply(D,off)))
uncorrected = s.Matrix(2,2,lambda a,b: U[a*4+1,b*4])
control('omitting correction breaks the independently derived failure branch',
        not same(apply(uncorrected,off), off/8))
control('identity drive cannot satisfy the negative-witness decision rule',
        not same(apply(ks[0], off), Q(5,8)*off) and s.simplify((W*B).trace()) == 0)
control('opposite witness phase reverses the claimed sign',
        s.simplify((pt(P.conjugate())*stopped(B,1)).trace()).is_positive)

values = []
for depth in range(1,9):
    out = stopped(B,depth)
    control('output is a valid quantum density matrix ' + str(depth),
            same(out.H,out) and out.trace()==1 and all(ev.is_nonnegative for ev in out.eigenvals()))
    value = s.simplify((W*out).trace())
    values.append((depth, value))

assert all(ok for _,ok in checks)
print('CONTROLS:', len(checks), 'exact controls passed; required mutations rejected')
print('Bell native table:', str(table(B)))
for depth,value in values: print('depth',depth,'separating value',value)
if any(value.is_negative for _,value in values):
    print('EXPLORATORY RESULT: literal InstAvail premises do not imply preservation of every eligible pair cone.')
else:
    print('EXPLORATORY RESULT: no separating counterexample at the registered witness.')
print('SCOPE: exact algebra at the stated interface; not a physical model, a native receipt or new kernel certification.')
