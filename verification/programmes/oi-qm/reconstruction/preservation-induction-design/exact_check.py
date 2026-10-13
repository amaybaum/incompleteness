#!/usr/bin/env python3
"""Research controls: SymPy protocol recursion, exact unnormalized branches.

The decision rule is fixed in result.md. No universal/kernel verdict is emitted.
The independent checker enumerates Kraus paths rather than interpreting this AST.
"""
import hashlib
import itertools
import json
import sympy as s

checks = []
seen = set()


def check(name, condition):
    if condition is not True:
        raise AssertionError(name)
    checks.append(name)


def perm(p):
    n = len(p)
    return s.Matrix(n, n, lambda i, j: int(i == p[j]))


def ptrace(x, m):
    n = x.rows // m
    return s.Matrix(n, n, lambda i, j: sum(x[i*m+a, j*m+a] for a in range(m)))


def eval_protocol(p, x):
    tag, *args = p
    seen.add(tag)
    if tag == 'op':
        k, = args
        check('isometry', k.conjugate().T*k == s.eye(k.rows))
        return {0: k*x*k.conjugate().T}
    if tag == 'readout':
        m, reindex = args
        n = x.rows
        u = perm(reindex)
        projectors = [u*s.diag(*[int(i % m == k) for i in range(n)])*u.T for k in range(m)]
        check('readout-complete', sum(projectors, s.zeros(n)) == s.eye(n))
        return {k: p*x*p for k, p in enumerate(projectors)}
    if tag == 'coarse':
        child, f, count = args
        branches = eval_protocol(child, x)
        return {k: sum((v for a, v in branches.items() if f[a] == k), s.zeros(x.rows))
                for k in range(count)}
    if tag == 'bind':
        child, continuations = args
        return {(a, b): z for a, y in eval_protocol(child, x).items()
                for b, z in eval_protocol(continuations[a], y).items()}
    if tag == 'discard':
        m, child = args
        check('ancilla-positive-size', m > 0)
        attached = s.kronecker_product(x, s.eye(m)/m)
        check('mixed-attachment-trace', s.trace(attached) == s.trace(x))
        return {a: ptrace(y, m) for a, y in eval_protocol(child, attached).items()}
    raise AssertionError(tag)


def diagonal_positive(x):
    return x == s.diag(*x.diagonal()) and all(t >= 0 for t in x.diagonal())


def psd(x):
    if x != x.conjugate().T:
        return False
    # All principal minors, rather than only leading minors (singular samples occur).
    for k in range(1, x.rows+1):
        for subset in itertools.combinations(range(x.rows), k):
            if s.simplify(x.extract(subset, subset).det()) < 0:
                return False
    return True


def canonical(x):
    return [[[str(s.re(z)), str(s.im(z))] for z in row] for row in x.tolist()]


swap = s.Matrix([[0, 1], [1, 0]])
rotation = s.Matrix([[s.Rational(3, 5), -s.Rational(4, 5)],
                     [s.Rational(4, 5), s.Rational(3, 5)]])
cnot = perm([0, 1, 3, 2])
identity = s.eye(4)
read = ('readout', 2, [0, 1, 2, 3, 4, 5, 6, 7])
inner = ('discard', 2, read)
middle = ('bind', inner, {0: ('op', identity), 1: ('op', cnot)})
coarse = ('coarse', middle, {(0, 0): 0, (1, 0): 1}, 3)
outer = ('discard', 2, coarse)

inputs = [('classical-0', s.diag(1, 0)), ('classical-1', s.diag(0, 1)),
          ('classical-mixed', s.diag(s.Rational(2, 3), s.Rational(1, 3))),
          ('quantum-complex', s.Matrix([[s.Rational(1, 2), -s.I/2], [s.I/2, s.Rational(1, 2)]])),
          ('quantum-real', s.Matrix([[s.Rational(9, 25), s.Rational(12, 25)],
                                     [s.Rational(12, 25), s.Rational(16, 25)]]))]
manifest = {}
for name, x in inputs:
    quantum = name.startswith('quantum')
    continuations = {0: ('op', rotation if quantum else swap),
                     1: ('op', swap), 2: ('op', s.eye(2))}
    branches = eval_protocol(('bind', outer, continuations), x)
    check('aggregate-trace:'+name, sum(s.trace(y) for y in branches.values()) == s.trace(x))
    check('empty-coarse-fibre:'+name, branches[(2, 0)] == s.zeros(2))
    for a, y in branches.items():
        check('branch-PSD:'+name+str(a), bool(psd(y)))
        if not quantum:
            check('classical-branch:'+name+str(a), bool(diagonal_positive(y)))
    manifest[name] = [canonical(branches[(a, 0)]) for a in range(3)]

check('all-five-constructors', seen == {'op', 'readout', 'coarse', 'bind', 'discard'})
# Actual carrier relabelling changes which coordinate is measured.
x4 = s.diag(1, 2, 3, 4)
r = eval_protocol(('readout', 2, [2, 0, 3, 1]), x4)
check('relabelled-register-0', r[0] == s.diag(0, 0, 3, 4))
check('relabelled-register-1', r[1] == s.diag(1, 2, 0, 0))

h = s.Matrix([[1, 1], [1, -1]]) / s.sqrt(2)
had = h*s.diag(1, 0)*h.T
check('Hadamard-isometry', h.T*h == s.eye(2))
check('Hadamard-trace', s.trace(had) == 1)
check('operation-premise-missing', not diagonal_positive(had))
# Other scalar-cone premise fields hold universally, as written in result.md.
i2 = s.eye(2)
p0 = s.diag(1, 0)
check('readout-not-isometry', p0.T*p0 != s.eye(2))
check('readout-scalar-cone-failure', p0*i2*p0 != s.trace(p0*i2*p0)/2*i2)
check('readout-total-normalized', p0*i2*p0 + (i2-p0)*i2*(i2-p0) == i2)
check('scalar-mixed-attach', s.kronecker_product(3*i2, s.eye(3)/3) == s.eye(6))
check('scalar-discard', ptrace(2*s.eye(6), 3) == 6*i2)
# Enlarged-carrier premise is substantive: C_2=diagonal PSD and C_n=PSD
# otherwise; monomial class at dimension 2 and fullClass otherwise.
attached = s.kronecker_product(s.diag(1, 0), i2/2)
enlarged_h = s.kronecker_product(h, i2)
enlarged_out = enlarged_h*attached*enlarged_h.T
check('discard-enlarged-isometry', enlarged_h.T*enlarged_h == s.eye(4))
check('discard-enlarged-PSD', bool(psd(enlarged_out)))
check('discard-enlarged-trace', s.trace(enlarged_out) == 1)
check('discard-missing-cone-premise', ptrace(enlarged_out, 2) == had and not diagonal_positive(had))

# Named wrong-step variants: each must differ on a retained, nonvacuous control.
mutations = {
    'aggregate-is-branch': p0 != s.trace(p0)/2*i2 and p0 + (i2-p0) == i2,
    'readout-is-isometry': p0.T*p0 != s.eye(2),
    'pure-instead-of-uniform': s.kronecker_product(i2, p0) != s.kronecker_product(i2, i2/2),
    'empty-fibre-drops-zero': outer[0] == 'discard' and manifest['classical-0'][2] == canonical(s.zeros(2)),
    'discard-omits-sum': ptrace(s.eye(4)/2, 2) != s.eye(2)/2,
    'discard-cone-premise-dropped': not diagonal_positive(ptrace(enlarged_out, 2)),
    'labels-carry-inventory-only': swap*s.diag(1, 0)*swap.T != i2/2,
}
for name, rejected in mutations.items():
    check('mutation-rejected:'+name, bool(rejected))

payload = json.dumps(manifest, sort_keys=True, separators=(',', ':'))
print('SAMPLE-MANIFEST-SHA256', hashlib.sha256(payload.encode()).hexdigest())
print('EXACT-CONTROLS', len(checks))
print('MUTATIONS-REJECTED', len(mutations))
print('CHECKED: finite constructor examples and named countercontrols only')
