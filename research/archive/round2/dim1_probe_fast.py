#!/usr/bin/env python3
"""DIM-1 design probe, fast version: exact linear algebra (sympy) for the family; numpy for the positivity scan.
Same questions as dim1_probe.py (Q1-Q4). Read-only research artifact."""
from fractions import Fraction as Fr
import itertools, math
import numpy as np
import sympy as sp

n = 4
U, X, Y, Z = 0, 1, 2, 3
Nvec = [1, 1, -1, -1]
TA = [X, Y]

def kron(a, b):
    return [a[i] * b[j] for i in range(n) for j in range(n)]
def idx(i, j):
    return i * n + j
k = {0: [1, 0, 0, 1], 1: [1, 0, 0, -1]}

syms = {}
def sym(name):
    s = sp.Symbol(name); syms[name] = s; return s

G = sp.zeros(n * n, n * n)
for b in range(n):
    plus = sp.Rational(1 + Nvec[b], 2); minus = sp.Rational(1 - Nvec[b], 2)
    G[idx(U, b), idx(U, b)] += plus; G[idx(Z, b), idx(U, b)] += minus
    G[idx(U, b), idx(Z, b)] += minus; G[idx(Z, b), idx(Z, b)] += plus
for c in TA:
    for i in range(n):
        a = sym('a_%d%d' % (i, c)); bb = sym('b_%d%d' % (i, c))
        G[idx(i, X), idx(c, U)] += a
        G[idx(i, U), idx(c, X)] += a
        G[idx(i, Z), idx(c, Y)] += bb
        G[idx(i, Y), idx(c, Z)] += -bb
params = list(syms.values())
eqs = []
for c in TA:
    for b in range(n):
        eqs.append(G[idx(U, U), idx(c, b)])
Nm = sp.diag(*Nvec); I4 = sp.eye(n)
IN = sp.kronecker_product(I4, Nm); NI = sp.kronecker_product(Nm, I4)
eqs += list(IN * G * IN - G) + list(NI * G * NI - IN * G)
eqs = [sp.expand(q) for q in eqs if sp.expand(q) != 0]
sol = list(sp.linsolve(eqs, params))[0]
free = sorted({s for expr in sol for s in expr.free_symbols}, key=str)
Gsol = G.subs(dict(zip(params, sol)))
print('Q1: %d parameters; after normalization + Rt + Rc: %d free: %s' % (len(params), len(free), free))
print('Q1: the family G~(free):')
sp.pprint(Gsol)
for a in (0, 1):
    for b in (0, 1):
        assert list(Gsol * sp.Matrix(kron(k[a], k[b]))) == kron(k[a], k[a ^ b])
print('Q1: frame F holds on the family')
print('Q1: det G~ =', sp.factor(Gsol.det()))

cnot = {(U, U): (U, U, 1), (U, X): (U, X, 1), (U, Y): (Z, Y, 1), (U, Z): (Z, Z, 1),
        (X, U): (X, X, 1), (X, X): (X, U, 1), (X, Y): (Y, Z, 1), (X, Z): (Y, Y, -1),
        (Y, U): (Y, X, 1), (Y, X): (Y, U, 1), (Y, Y): (X, Z, -1), (Y, Z): (X, Y, 1),
        (Z, U): (Z, U, 1), (Z, X): (Z, X, 1), (Z, Y): (U, Y, 1), (Z, Z): (U, Z, 1)}
C = sp.zeros(n * n, n * n)
for (a, b), (i, j, s) in cnot.items():
    C[idx(i, j), idx(a, b)] = s
match = sp.solve([sp.expand(x - y) for x, y in zip(list(Gsol), list(C))], free, dict=True)
print('Q3: complex CNOT in the family at', match)

def L(sx, sy):
    return sp.diag(1, sx, sy, 1)
conj = {}
for (ax, ay, bx, by) in itertools.product((1, -1), repeat=4):
    LL = sp.kronecker_product(L(ax, ay), L(bx, by))
    Cc = LL * C * LL.inv()
    m = sp.solve([sp.expand(x - y) for x, y in zip(list(Gsol), list(Cc))], free, dict=True)
    if m:
        conj[tuple(m[0][f] for f in free)] = (ax, ay, bx, by)
print('Q3: frame-preserving local conjugates L_A⊗L_B of CNOT inside the family: %d points' % len(conj))
for kk, vv in sorted(conj.items()):
    print('     params', dict(zip(map(str, free), kk)), 'from L_A=diag(1,%d,%d,1), L_B=diag(1,%d,%d,1)' % vv)

# numerical positivity scan: product pure states/effects, one- and two-sided
rng = np.random.default_rng(11)
def sample_pts(m):
    v = rng.standard_normal((m, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    return np.concatenate([np.ones((m, 1)), v], axis=1)
S = sample_pts(22); E = sample_pts(22)
prodS = np.array([np.kron(s, t) for s in S for t in S])          # 3600 x 16
prodE = np.array([np.kron(f, g) for f in E for g in E])          # 3600 x 16
Gfun = sp.lambdify(free, Gsol, 'numpy')
def minval(Gn):
    return float((prodE @ (Gn @ prodS.T)).min())
structural = {'a_11', 'a_22', 'b_12', 'b_21'}
grids = [([-1, -0.5, 0.5, 1] if str(f) in structural else [-0.5, 0, 0.5]) for f in free]
print('Q2: scan: structural params (det factors) over {-1,-1/2,1/2,1}, the others over {-1/2,0,1/2}; survivors (two-sided product-positive on the sample):')
good = []
for vals in itertools.product(*grids):
    Gn = np.array(Gfun(*vals), dtype=float)
    if abs(np.linalg.det(Gn)) < 1e-9:
        continue
    m1 = minval(Gn)
    if m1 < -1e-9:
        continue
    m2 = minval(np.linalg.inv(Gn))
    good.append((vals, m1, m2))
for g in good:
    print('     ', dict(zip(map(str, free), g[0])), 'min G: %.2e  min G^-1: %.2e' % (g[1], g[2]))
# finer 1-D/2-D continuation around survivors: is positivity a discrete set or a continuum?
print('Q2: refinement — for each survivor, perturb each free parameter by ±0.05 and report whether positivity survives')
for g in good:
    base = np.array(g[0], dtype=float)
    res = []
    for i in range(len(free)):
        for dlt in (-0.05, 0.05):
            v = base.copy(); v[i] += dlt
            Gn = np.array(Gfun(*v), dtype=float)
            ok = abs(np.linalg.det(Gn)) > 1e-9 and minval(Gn) > -1e-9 and minval(np.linalg.inv(Gn)) > -1e-9
            res.append(ok)
    print('     ', dict(zip(map(str, free), g[0])), 'perturbations surviving:', sum(res), 'of', len(res))

for d in (2, 3, 4, 5, 6, 7):
    splits = [(p, d - 1 - p) for p in range(d)]
    eq = [s for s in splits if s[0] == s[1]]
    print('Q4: d=%d: p=q split: %s' % (d, eq if eq else 'none'))
print('dim1_probe_fast: done')
