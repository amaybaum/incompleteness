#!/usr/bin/env python3
"""Round PRESERVE-INDUCT-1 -- exact finite instances of the conditional preservation induction.

The kernel statement (OIBridge/PreservationInduction.lean) is: if an independently given carrier
cone family C is closed under zero and addition, preserved by every admitted isometric conjugation
and by every branch of an admitted native register readout, sent into C(S x Fin m) by uniform
mixed attachment and back into C(S) by partial trace for m > 0, then every branch of every
InstAvail family preserves C(S). This script interprets the five constructors (op, readout,
coarse, bind, discard) with exact SymPy matrices on fixed inputs, for the two comparison families
of OIBridge/PreservationInductionInstances.lean: positive semidefinite matrices, and positive
semidefinite diagonal matrices with monomial operations.

Exact arithmetic only (SymPy Rationals and Gaussian rationals); no floating point, no randomness,
no time-dependence, no file input. Positive semidefiniteness is checked through every principal
minor. Every check prints nothing on its own; each code prints one PASS or FAIL line with its count.
The script ends with 'preserve_induct1_probe: OK -- N checks' when everything passes; otherwise
with 'preserve_induct1_probe: FAILED -- ...' and exit 1.

Codes:
  CONSTRUCTORS  the main protocol uses all five constructors, nested bind and discard, positive-size
                ancillas and an outcome-dependent continuation
  ISOMETRY      every op step evaluated is an isometry
  READOUT       every readout evaluated is a complete family of register projections
  ATTACH        every uniform attachment preserves trace and lands in the enlarged cone
  AGGREGATE     the branch traces sum to the input trace
  EMPTY         the empty coarse-graining fibre is present and zero
  NONVACUOUS    every input is nonzero and leaves at least two nonzero branches
  BRANCH-PSD    every final branch is positive semidefinite
  BRANCH-DIAG   every final branch of a classical input is nonnegative diagonal
  RELABEL       a nontrivial carrier relabelling changes which coordinate the readout measures
  COUNTER-HADAMARD  an isometric conjugation available in fullClass leaves the diagonal cone
  COUNTER-READOUT   the scalar cone keeps every premise but readout
  COUNTER-DISCARD   an enlarged-carrier operation leaves the diagonal cone after partial trace
  MANIFEST      the sample manifest of every final branch has the frozen digest
  MUTATION-RULE the reading of a mutation run: a named check holds only on an exact True, fails
                only on an exact False or that check's own violation, and is undecided on any
                other exception or any other value; and exactly eight distinct mutation runs exist
Mutations: eight mutation runs. Each evaluates the faithful step and the mutated step separately,
and the mutation is rejected only when the named check holds on the faithful step and fails on
the mutated one. A run that raises anything but the named check's violation, or returns anything
but a bool, is undecided: a crash is not a rejection, and it fails the script.

These are finite exact instances. They are evidence for the recorded examples only; the universal
statement is the kernel's.
"""
import hashlib
import itertools
import json
import sys

import sympy as s

MANIFEST_SHA256 = 'a1f82e289ba07a4c60dd6b56396dcdf7c0c217b2ff49a8d779f1c4e923842ea9'
CODES = ['CONSTRUCTORS', 'ISOMETRY', 'READOUT', 'ATTACH', 'AGGREGATE', 'EMPTY', 'NONVACUOUS',
         'BRANCH-PSD', 'BRANCH-DIAG', 'RELABEL', 'COUNTER-HADAMARD', 'COUNTER-READOUT',
         'COUNTER-DISCARD', 'MANIFEST', 'MUTATION-RULE']
counts = {c: 0 for c in CODES}
failures = []


def check(code, name, condition):
    counts[code] += 1
    if condition is not True:
        failures.append('%s %s' % (code, name))


class Violation(Exception):
    """A step's own check failed during an evaluation that does not record (the check's name)."""

    def __init__(self, name):
        super().__init__(name)
        self.name = name


def perm(p):
    n = len(p)
    return s.Matrix(n, n, lambda i, j: int(i == p[j]))


def ptrace(x, m):
    n = x.rows // m
    return s.Matrix(n, n, lambda i, j: sum(x[i * m + a, j * m + a] for a in range(m)))


def psd(x):
    if x != x.conjugate().T:
        return False
    for k in range(1, x.rows + 1):
        for subset in itertools.combinations(range(x.rows), k):
            if s.simplify(x.extract(list(subset), list(subset)).det()) < 0:
                return False
    return True


def diagonal_positive(x):
    return x == s.diag(*x.diagonal()) and all(bool(t >= 0) for t in x.diagonal())


def scalar(x):
    return x == (s.trace(x) / x.rows) * s.eye(x.rows) and bool(s.trace(x) >= 0)


def canonical(x):
    return [[[str(s.re(z)), str(s.im(z))] for z in row] for row in x.tolist()]


class Evaluator:
    """The five constructors. cone(x) is the comparison family's membership test on the carrier of
    x; record=True counts the step checks under their codes. The keyword switches are the wrong
    steps the mutations apply; with their defaults the evaluator is the faithful one."""

    def __init__(self, cone, record=True, attach='uniform', keep_empty=True, discard_sum=True):
        self.cone, self.record, self.attach = cone, record, attach
        self.keep_empty, self.discard_sum = keep_empty, discard_sum
        self.seen = set()

    def step(self, code, name, ok):
        if self.record:
            check(code, name, ok)
        elif ok is not True:
            raise Violation(name)

    def run(self, p, x):
        tag, *args = p
        self.seen.add(tag)
        if tag == 'op':
            k, = args
            self.step('ISOMETRY', 'op-isometry', k.conjugate().T * k == s.eye(k.rows))
            return {0: k * x * k.conjugate().T}
        if tag == 'readout':
            m, reindex = args
            n = x.rows
            u = perm(reindex)
            projectors = [u * s.diag(*[int(i % m == k) for i in range(n)]) * u.T for k in range(m)]
            self.step('READOUT', 'readout-complete', sum(projectors, s.zeros(n)) == s.eye(n))
            return {k: q * x * q for k, q in enumerate(projectors)}
        if tag == 'coarse':
            child, f, count = args
            branches = self.run(child, x)
            out = {k: sum((v for a, v in branches.items() if f[a] == k), s.zeros(x.rows)) for k in range(count)}
            if not self.keep_empty:
                out = {k: v for k, v in out.items() if any(f[a] == k for a in branches)}
            return out
        if tag == 'bind':
            child, continuations = args
            return {(a, b): z for a, y in self.run(child, x).items()
                    for b, z in self.run(continuations[a], y).items()}
        if tag == 'discard':
            m, child = args
            self.step('ATTACH', 'attach-positive', m > 0)
            anc = s.eye(m) / m if self.attach == 'uniform' else s.diag(*([1] + [0] * (m - 1)))
            attached = s.kronecker_product(x, anc)
            self.step('ATTACH', 'attach-trace', s.trace(attached) == s.trace(x))
            self.step('ATTACH', 'attach-cone', self.cone(attached))
            out = self.run(child, attached)
            if self.discard_sum:
                return {a: ptrace(y, m) for a, y in out.items()}
            n = x.rows
            return {a: s.Matrix(n, n, lambda i, j: y[i * m, j * m]) for a, y in out.items()}
        raise AssertionError(tag)


swap = s.Matrix([[0, 1], [1, 0]])
rotation = s.Matrix([[s.Rational(3, 5), -s.Rational(4, 5)], [s.Rational(4, 5), s.Rational(3, 5)]])
cnot = perm([0, 1, 3, 2])
identity4 = s.eye(4)
read = ('readout', 2, [0, 1, 2, 3, 4, 5, 6, 7])
inner = ('discard', 2, read)
middle = ('bind', inner, {0: ('op', identity4), 1: ('op', cnot)})
coarse = ('coarse', middle, {(0, 0): 0, (1, 0): 1}, 3)
outer = ('discard', 2, coarse)
inputs = [('classical-0', s.diag(1, 0)), ('classical-1', s.diag(0, 1)),
          ('classical-mixed', s.diag(s.Rational(2, 3), s.Rational(1, 3))),
          ('quantum-complex', s.Matrix([[s.Rational(1, 2), -s.I / 2], [s.I / 2, s.Rational(1, 2)]])),
          ('quantum-real', s.Matrix([[s.Rational(9, 25), s.Rational(12, 25)],
                                     [s.Rational(12, 25), s.Rational(16, 25)]]))]


def protocol(quantum):
    continuations = {0: ('op', rotation if quantum else swap), 1: ('op', swap), 2: ('op', s.eye(2))}
    return ('bind', outer, continuations)


def nested(p, depth=0):
    """(tag, depth) of every node of a protocol."""
    tag, *args = p
    out = [(tag, depth)]
    for a in args:
        if isinstance(a, tuple) and a and a[0] in ('op', 'readout', 'coarse', 'bind', 'discard'):
            out += nested(a, depth + 1)
        if isinstance(a, dict):
            for v in a.values():
                if isinstance(v, tuple) and v and v[0] in ('op', 'readout', 'coarse', 'bind', 'discard'):
                    out += nested(v, depth + 1)
    return out


# ---------------------------------------------------------------- the faithful evaluation
manifest = {}
seen = set()
for name, x in inputs:
    quantum = name.startswith('quantum')
    cone = psd if quantum else (lambda y: bool(psd(y)) and bool(diagonal_positive(y)))
    ev = Evaluator(lambda y, c=cone: bool(c(y)))
    branches = ev.run(protocol(quantum), x)
    seen |= ev.seen
    check('AGGREGATE', name, sum(s.trace(y) for y in branches.values()) == s.trace(x))
    check('EMPTY', name, (2, 0) in branches and branches[(2, 0)] == s.zeros(2))
    check('NONVACUOUS', name, x != s.zeros(2) and sum(y != s.zeros(2) for y in branches.values()) >= 2)
    for a, y in sorted(branches.items()):
        check('BRANCH-PSD', name + str(a), bool(psd(y)))
        if not quantum:
            check('BRANCH-DIAG', name + str(a), bool(diagonal_positive(y)))
    manifest[name] = [canonical(branches[(a, 0)]) for a in range(3)]

tags = nested(protocol(False))
check('CONSTRUCTORS', 'all five', seen == {'op', 'readout', 'coarse', 'bind', 'discard'})
check('CONSTRUCTORS', 'nested bind/discard', [t for t, _ in tags[:5]] == ['bind', 'discard', 'coarse', 'bind', 'discard'])
check('CONSTRUCTORS', 'positive-size ancillas', all(p[1] > 0 for p in (outer, inner)))
check('CONSTRUCTORS', 'outcome-dependent continuation', middle[2][0][1] != middle[2][1][1])

x4 = s.diag(1, 2, 3, 4)
r = Evaluator(psd).run(('readout', 2, [2, 0, 3, 1]), x4)
check('RELABEL', 'nontrivial', [2, 0, 3, 1] != list(range(4)))
check('RELABEL', 'register 0', r[0] == s.diag(0, 0, 3, 4))
check('RELABEL', 'register 1', r[1] == s.diag(1, 2, 0, 0))

h = s.Matrix([[1, 1], [1, -1]]) / s.sqrt(2)
p0 = s.diag(1, 0)
i2 = s.eye(2)
had = h * p0 * h.T
check('COUNTER-HADAMARD', 'isometry', h.T * h == i2)
check('COUNTER-HADAMARD', 'trace', s.trace(had) == 1)
check('COUNTER-HADAMARD', 'leaves the diagonal cone', not diagonal_positive(had))
check('COUNTER-READOUT', 'readout is not an isometry', p0.T * p0 != i2)
check('COUNTER-READOUT', 'readout leaves the scalar cone', not scalar(p0 * i2 * p0))
check('COUNTER-READOUT', 'readout total is normalized', p0 * i2 * p0 + (i2 - p0) * i2 * (i2 - p0) == i2)
check('COUNTER-READOUT', 'uniform attachment keeps the scalar cone', scalar(s.kronecker_product(3 * i2, s.eye(3) / 3)))
check('COUNTER-READOUT', 'partial trace keeps the scalar cone', scalar(ptrace(2 * s.eye(6), 3)))
attached = s.kronecker_product(p0, i2 / 2)
enlarged_h = s.kronecker_product(h, i2)
enlarged_out = enlarged_h * attached * enlarged_h.T
check('COUNTER-DISCARD', 'enlarged isometry', enlarged_h.T * enlarged_h == s.eye(4))
check('COUNTER-DISCARD', 'enlarged output PSD', bool(psd(enlarged_out)))
check('COUNTER-DISCARD', 'enlarged output trace', s.trace(enlarged_out) == 1)
check('COUNTER-DISCARD', 'partial trace leaves the diagonal cone',
      ptrace(enlarged_out, 2) == had and not diagonal_positive(had))

payload = json.dumps(manifest, sort_keys=True, separators=(',', ':'))
digest = hashlib.sha256(payload.encode()).hexdigest()
check('MANIFEST', 'digest', digest == MANIFEST_SHA256)


# ---------------------------------------------------------------- mutations
def classical(y):
    return bool(psd(y)) and bool(diagonal_positive(y))


def first_coordinate(y):
    """A cone that is not invariant under relabelling: nonnegative multiples of diag(1, 0)."""
    return y == s.diag(y[0, 0], 0) and bool(y[0, 0] >= 0)


def holds(name, thunk):
    """Whether the named check holds on an evaluation: True on the thunk's exact True, False on its
    exact False or when the evaluation raised that check's own Violation. Another check's Violation,
    any other exception, or any value but a bool is not the named check failing: None (undecided)."""
    try:
        value = thunk()
    except Violation as v:
        return False if v.name == name else None
    except Exception:  # a crash is undecided, never a rejection
        return None
    return value if value is True or value is False else None


def crash():
    raise ZeroDivisionError('a crashing run')


def other_violation():
    raise Violation('another-check')


def named_violation():
    raise Violation('named-check')


check('MUTATION-RULE', 'exact True holds', holds('named-check', lambda: True) is True)
check('MUTATION-RULE', 'exact False fails', holds('named-check', lambda: False) is False)
check('MUTATION-RULE', 'the named violation fails', holds('named-check', named_violation) is False)
check('MUTATION-RULE', 'a crash is undecided', holds('named-check', crash) is None)
check('MUTATION-RULE', 'another check\'s violation is undecided', holds('named-check', other_violation) is None)
check('MUTATION-RULE', 'a non-bool value is undecided',
      holds('named-check', lambda: 1) is None and holds('named-check', lambda: None) is None
      and holds('named-check', lambda: s.true) is None)


def ev(cone, **kw):
    return Evaluator(cone, record=False, **kw)


def branches_in(cone, b):
    return all(cone(y) for y in b.values())


def aggregate(x, b):
    return sum(s.trace(y) for y in b.values()) == s.trace(x)


x0 = s.diag(1, 0)
eye4 = s.eye(4)
# (name, named check, the check on the faithful step, the check on the mutated step). A mutation is
# rejected when the named check holds on the faithful step and fails on the mutated one.
mutations = [
    ('readout-as-isometry', 'op-isometry',
     lambda: ev(classical).run(('op', swap), x0) is not None,
     lambda: ev(classical).run(('op', p0), x0) is not None),
    ('aggregate-for-branch', 'branch-cone',
     lambda: branches_in(scalar, ev(scalar).run(('op', swap), i2)),
     lambda: (lambda b: not scalar(sum(b.values(), s.zeros(2))) or branches_in(scalar, b))(
         ev(scalar).run(('readout', 2, [0, 1]), i2))),
    ('discard-enlarged-premise-dropped', 'branch-cone',
     lambda: branches_in(classical, ev(classical).run(('discard', 2, ('op', eye4)), x0)),
     lambda: branches_in(classical, ev(psd).run(('discard', 2, ('op', enlarged_h)), x0))),
    ('labels-as-cone-transport', 'branch-cone',
     lambda: branches_in(first_coordinate, ev(first_coordinate).run(('op', i2), x0)),
     lambda: branches_in(first_coordinate, ev(first_coordinate).run(('op', swap), x0))),
    ('availability-as-source', 'branch-cone',
     lambda: branches_in(classical, ev(classical).run(('op', swap), x0)),
     lambda: (lambda b: not aggregate(x0, b) or branches_in(classical, b))(ev(psd).run(('op', h), x0))),
    ('pure-for-uniform', 'attach-cone',
     lambda: ev(scalar).run(('discard', 2, ('op', eye4)), 2 * i2) is not None,
     lambda: ev(scalar, attach='pure').run(('discard', 2, ('op', eye4)), 2 * i2) is not None),
    ('empty-fibre-dropped', 'empty-fibre',
     lambda: (2, 0) in ev(classical).run(protocol(False), x0),
     lambda: (2, 0) in ev(classical, keep_empty=False).run(protocol(False), x0)),
    ('discard-omits-sum', 'aggregate-trace',
     lambda: aggregate(x0, ev(classical).run(('discard', 2, ('op', eye4)), x0)),
     lambda: aggregate(x0, ev(classical, discard_sum=False).run(('discard', 2, ('op', eye4)), x0))),
]

MUTATION_RUNS = 8
check('MUTATION-RULE', 'exactly eight distinct mutation runs',
      len(mutations) == MUTATION_RUNS and len({m[0] for m in mutations}) == MUTATION_RUNS)

print('SYMPY %s' % s.__version__)
for c in CODES:
    bad = [f for f in failures if f.split(' ', 1)[0] == c]
    print(('PASS %s (%d)' % (c, counts[c])) if not bad and counts[c] else ('FAIL %s (%d): %s' % (c, counts[c], '; '.join(bad))))
rejected = survived = undecided = 0
for name, named, faithful, mutated in mutations:
    f, m = holds(named, faithful), holds(named, mutated)
    if f is True and m is False:
        print('REJECTED %s: %s' % (name, named))
        rejected += 1
    elif f is None or m is None:
        print('UNDECIDED %s: %s (faithful %s, mutated %s)' % (name, named, f, m))
        undecided += 1
    else:
        print('SURVIVED %s: %s (faithful %s, mutated %s)' % (name, named, f, m))
        survived += 1
print('mutations: %d rejected, %d survived, %d undecided' % (rejected, survived, undecided))
ran = rejected + survived + undecided
print('SAMPLE-MANIFEST-SHA256 %s' % digest)
n = sum(counts.values())
nfail = len(failures) + sum(1 for c in CODES if not counts[c]) + (len(mutations) - rejected) + (ran != MUTATION_RUNS)
print('checks: %d, failures: %d' % (n, nfail))
if nfail:
    print('preserve_induct1_probe: FAILED -- %d failure(s)' % nfail)
    sys.exit(1)
print('preserve_induct1_probe: OK -- %d checks' % n)
