#!/usr/bin/env python3
"""Separate rational matrix verification; imports neither SymPy nor the probe.

Checks concrete certificates, not the universal separation/effect arguments.
"""
from fractions import Fraction as F
import json

count = 0


def g(a=0, b=0):
    return F(a), F(b)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def conj(a):
    return a[0], -a[1]


def matrix(n):
    return [[g() for _ in range(n)] for _ in range(n)]


def eye(n):
    return [[g(int(i == j)) for j in range(n)] for i in range(n)]


def sum_matrix(*xs):
    result = matrix(len(xs[0]))
    for x in xs:
        for i in range(len(x)):
            for j in range(len(x)):
                result[i][j] = add(result[i][j], x[i][j])
    return result


def scale(a, k):
    return [[mul(z, g(k)) for z in row] for row in a]


def adj(a):
    return [[conj(a[j][i]) for j in range(len(a))] for i in range(len(a))]


def mm(a, b):
    result = matrix(len(a))
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                result[i][j] = add(result[i][j], mul(a[i][k], b[k][j]))
    return result


def tr(a):
    result = g()
    for i in range(len(a)):
        result = add(result, a[i][i])
    assert result[1] == 0
    return result[0]


def ip(a, b):
    return tr(mm(a, b))


def outer(a, b=None):
    b = a if b is None else b
    return [[mul(x, conj(y)) for y in b] for x in a]


def kron(a, b):
    m, n = len(a), len(b)
    return [[mul(a[i//n][j//n], b[i % n][j % n]) for j in range(m*n)] for i in range(m*n)]


def check(name, condition):
    global count
    if not condition:
        raise AssertionError(name)
    count += 1


def projector(name, a, rank):
    check(name+' Hermitian', a == adj(a))
    check(name+' projector', mm(a, a) == a)
    check(name+' trace', tr(a) == rank)


I = eye(4)
p = list(map(g, [1, 0, 0, 0]))
u = list(map(g, [F(12, 13), F(5, 13)]))
q = [mul(a, b) for a in u for b in u]
pp, pq = outer(p), outer(q)
projector('first product', pp, 1)
projector('second product', pq, 1)
local = sum_matrix(outer(u), scale([[g(1), g()], [g(), g()]], -1))
check('local Helstrom gap by square', mm(local, local) == scale(eye(2), F(25, 169)))
check('strict telescoping bound', 2*F(5, 13) < 1)
overlap = q[0][0]
support = scale(sum_matrix(pp, pq, scale(sum_matrix(outer(p, q), outer(q, p)), -overlap)), 1/(1-overlap**2))
fkb = sum_matrix(I, scale(support, -1))
projector('KB support complement', fkb, 2)
bell = scale(outer(list(map(g, [1, 0, 0, 1]))), F(1, 2))
check('Bell outside support', ip(fkb, bell) > 0)
check('KB mixture in face', ip(fkb, scale(sum_matrix(pp, pq), F(1, 2))) == 0)
check('product determinant coefficient', q[3][0] == F(25, 169) and q[0][0]*q[3][0] == q[1][0]*q[2][0])

X, Y, Z = [[g(), g(1)], [g(1), g()]], [[g(), g(0, -1)], [g(0, 1), g()]], [[g(1), g()], [g(), g(-1)]]
defects = [scale(sum_matrix(I, scale(kron(X, Z), a), scale(kron(Y, Y), b), scale(kron(Z, X), -a*b)), F(1, 4))
           for a in (-1, 1) for b in (-1, 1)]
pis = [sum_matrix(scale(I, F(1, 2)), scale(z, -1)) for z in defects]
for j, pi in enumerate(pis):
    projector('actual Bell '+str(j), pi, 1)
check('Bell completeness', sum_matrix(*pis) == I)
U = [[mul(g(2), pis[j][i][0]) for j in range(4)] for i in range(4)]
check('independent Bell basis', mm(adj(U), U) == I)
pv = [[g(F(3, 4) if i == j == 0 else F(1, 4) if i == 0 or j == 0 else F(1, 12)) for j in range(4)] for i in range(4)]
wv = [g(), g(1), g(F(-3, 5), F(4, 5)), g(F(-2, 5), F(-4, 5))]
pw = scale(outer(wv), F(5, 14))
pv, pw = mm(mm(U, pv), adj(U)), mm(mm(U, pw), adj(U))
projector('rational first subspace vector', pv, 1)
projector('rational second subspace vector', pw, 1)
check('orthogonal support rays', mm(pv, pw) == matrix(4))
support = sum_matrix(pv, pw)
fzf = sum_matrix(I, scale(support, -1))
projector('ZF complement', fzf, 2)
rs = [ip(support, pi) for pi in pis]
check('one-cap bounds', F(1, 2) < rs[0] < 1 and all(0 < r < F(1, 2) for r in rs[1:]))
for j, (pi, z) in enumerate(zip(pis, defects)):
    check('defect excluded from face '+str(j), ip(fzf, z) == rs[j] > 0)
    c = mm(mm(support, pi), support)
    check('compressed rank one '+str(j), mm(c, c) == scale(c, rs[j]))
check('distinguished compressed defect', mm(mm(support, defects[0]), support) == sum_matrix(scale(pv, F(-1, 4)), scale(pw, F(1, 2))))
xzf = sum_matrix(scale(pv, F(2, 3)), scale(pw, F(1, 3)))
pairings = [ip(xzf, z) for z in defects]
check('candidate witness in cut PSD base', pairings[0] == 0 and all(a > 0 for a in pairings[1:]))
check('two exposed faces', ip(sum_matrix(fzf, defects[0]), xzf) == 0)
check('overlap constant strictly positive', F(2, 3)-F(1, 3) == F(1, 3))
check('overlap linear coefficient nonnegative', F(2, 3)*F(1, 4)+F(1, 3)*F(1, 2) == F(1, 3))
check('quantum witness normalization', tr(xzf) == 1)
check('quantum distinguishing test', ip(pv, pw) == 0 and ip(pv, pv) == ip(pw, pw) == 1)
check('quantum complete test', sum_matrix(pv, pw, fzf) == I)
classical = [[g(F(1, 2) if i == j == 0 else F(1, 3) if i == j == 1 else F(1, 6) if i == j == 2 else 0) for j in range(4)] for i in range(4)]
check('classical normalization', tr(classical) == 1)
gamma_bell = [[bell[2*(i//2)+j % 2][2*(j//2)+i % 2] for j in range(4)] for i in range(4)]
anti = scale(outer(list(map(g, [0, 1, -1, 0]))), F(1, 2))
check('co-quantum missing Bell certificate', ip(gamma_bell, anti) == F(-1, 2))

print(json.dumps({'controls': count, 'kb_distance_bound': '10/13', 'kb_Bell_support_gap': str(ip(fkb, bell)),
                  'zf_projection_weights': list(map(str, rs)), 'zf_cut_pairings': list(map(str, pairings)),
                  'zf_weighted_overlap_lower': '(1+t)/3',
                  'scope': 'separate rational certificate verification; universal proof and source obligations remain written'}, sort_keys=True, indent=2))
