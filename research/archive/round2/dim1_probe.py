#!/usr/bin/env python3
"""DIM-1 design probe (exact where it matters; read-only research, not a governed artifact).

Questions it answers, at d = 3 (basis u, x, y, z; N = diag(1, 1, -1, -1); corners k_a = u ± z):

  Q1  Parametrize G~ by S1 (G~(k_a ⊗ t) = k_a ⊗ N^a t) and the S2 tangent form on every control-output
      component (two parameters per (output i, input c) pair: alpha at (x,u),(u,x) and beta on so(V-)).
      Impose normalization, Rt and Rc as exact linear equations. Report the dimension of the surviving
      linear family and a basis.
  Q2  On that family, test two-sided product positivity (G and G^-1 send product pure states into the
      maximal cone) on a fixed deterministic grid of pure product states and product effects, and report
      the surviving parameter set (exact for the candidates we can name; numerical scan otherwise).
  Q3  Check that the complex CNOT (Pauli coordinates) is in the family, and which other members survive
      positivity; compare against local symmetries L_A ⊗ L_B that fix the frame and commute with N.
  Q4  Parity controls: for d = 2, 4, 6 no (p, q) with p = q exists; for every d ≥ 2 an involution of every
      split exists (so copy covariance alone excludes nothing).
"""
from fractions import Fraction as Fr
import itertools, math, sys
import sympy as sp

n = 4
U, X, Y, Z = 0, 1, 2, 3
Nvec = [1, 1, -1, -1]
TA = [X, Y]          # tangent directions at the corners (control side)
Vp = [X]             # +1 eigenspace of N in T
Vm = [Y, Z]          # -1 eigenspace of N in T ⊕ Rz

def e(i):
    v = [0] * n; v[i] = 1; return v

def kron(a, b):
    return [a[i] * b[j] for i in range(n) for j in range(n)]

def idx(i, j):
    return i * n + j

k = {0: [1, 0, 0, 1], 1: [1, 0, 0, -1]}

# ---- Q1: the parametrized G~ ---------------------------------------------------------------------
# columns are indexed by (control input a, target input b); rows by (control output i, target output j)
syms = {}
def sym(name):
    s = sp.Symbol(name); syms[name] = s; return s

G = sp.zeros(n * n, n * n)
# S1 part: G~(k_a ⊗ t) = k_a ⊗ N^a t  ⇒  G~(u⊗t) = u⊗(t+Nt)/2 + z⊗(t−Nt)/2 ; G~(z⊗t) = u⊗(t−Nt)/2 + z⊗(t+Nt)/2
for b in range(n):
    plus = Fr(1 + Nvec[b], 2); minus = Fr(1 - Nvec[b], 2)
    G[idx(U, b), idx(U, b)] += plus; G[idx(Z, b), idx(U, b)] += minus
    G[idx(U, b), idx(Z, b)] += minus; G[idx(Z, b), idx(Z, b)] += plus
# S2 part: for control input c ∈ T_A and every control output i, the target-side matrix Phi_{i,c} has the form
#   Phi[0][0] = 0; Phi[0][x] = Phi[x][0] = alpha; Phi[y][z] = beta, Phi[z][y] = -beta; all else 0.
for c in TA:
    for i in range(n):
        a = sym('a_%d%d' % (i, c)); bb = sym('b_%d%d' % (i, c))
        G[idx(i, X), idx(c, U)] += a
        G[idx(i, U), idx(c, X)] += a
        G[idx(i, Z), idx(c, Y)] += bb
        G[idx(i, Y), idx(c, Z)] += -bb

params = list(syms.values())
eqs = []
# normalization: (u^T ⊗ u^T) G~ (c ⊗ t) = 0 for all t  (control marginal of every product state is normalized)
for c in TA:
    for b in range(n):
        eqs.append(G[idx(U, U), idx(c, b)])
Nm = sp.diag(*Nvec); I4 = sp.eye(n)
IN = sp.kronecker_product(I4, Nm); NI = sp.kronecker_product(Nm, I4)
Rt = IN * G * IN - G
Rc = NI * G * NI - IN * G
eqs += list(Rt) + list(Rc)
eqs = [sp.expand(q) for q in eqs if sp.expand(q) != 0]
sol = sp.linsolve(eqs, params)
assert len(sol) == 1, sol
sol = list(sol)[0]
free = sorted({s for expr in sol for s in expr.free_symbols}, key=str)
print('Q1: parameters before relations: %d; after normalization + Rt + Rc: %d free (%s)'
      % (len(params), len(free), ', '.join(map(str, free))))
Gsol = G.subs(dict(zip(params, sol)))
# frame F: G~(k_a ⊗ k_b) = k_a ⊗ k_{a xor b} holds by S1 construction; check it
for a in (0, 1):
    for b in (0, 1):
        v = Gsol * sp.Matrix(kron(k[a], k[b]))
        assert list(v) == kron(k[a], k[a ^ b]), (a, b)
print('Q1: frame F holds on the family (by S1); Rt, Rc, normalization imposed exactly')

# ---- Q3: the complex CNOT in Pauli coordinates -----------------------------------------------------
# CNOT transfer on the Pauli basis (I,X,Y,Z)⊗(I,X,Y,Z) (control first):
cnot = {(U, U): (U, U, 1), (U, X): (U, X, 1), (U, Y): (Z, Y, 1), (U, Z): (Z, Z, 1),
        (X, U): (X, X, 1), (X, X): (X, U, 1), (X, Y): (Y, Z, 1), (X, Z): (Y, Y, -1),
        (Y, U): (Y, X, 1), (Y, X): (Y, U, 1), (Y, Y): (X, Z, -1), (Y, Z): (X, Y, 1),
        (Z, U): (Z, U, 1), (Z, X): (Z, X, 1), (Z, Y): (U, Y, 1), (Z, Z): (U, Z, 1)}
C = sp.zeros(n * n, n * n)
for (a, b), (i, j, s) in cnot.items():
    C[idx(i, j), idx(a, b)] = s
# solve for the free parameters matching C
match = sp.solve([sp.expand(x - y) for x, y in zip(list(Gsol), list(C))], free, dict=True)
print('Q3: complex CNOT lies in the family at parameters', match)

# ---- Q2: positivity on a deterministic grid -------------------------------------------------------
# pure states (1, t), |t| = 1, and effects (1, b)/2, |b| = 1; rational points on S^2 plus axis points
def rational_sphere():
    pts = []
    for (p, q, r) in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (3, 4, 0), (0, 3, 4), (4, 0, 3), (2, 3, 6), (1, 2, 2), (6, 2, 3)]:
        s = p * p + q * q + r * r
        root = int(round(math.sqrt(s)))
        assert root * root == s
        for sx in (1, -1):
            for sy in (1, -1):
                for sz in (1, -1):
                    pts.append((Fr(sx * p, root), Fr(sy * q, root), Fr(sz * r, root)))
    return sorted(set(pts))

S2 = rational_sphere()
def vec(t):  # state or effect vector (1, t)
    return sp.Matrix([1, t[0], t[1], t[2]])

def min_value(M, grid):
    """exact minimum of (f⊗g)^T M (s⊗t) over the grid of pure product states/effects"""
    worst = None
    for s in grid:
        for t in grid:
            v = M * sp.Matrix(kron(list(vec(s)), list(vec(t))))
            for f in grid:
                for g in grid:
                    val = (sp.Matrix(kron(list(vec(f)), list(vec(g)))).T * v)[0]
                    if worst is None or val < worst[0]:
                        worst = (val, s, t, f, g)
    return worst

# scan the free parameters over a small exact set and keep those with G and G^{-1} product-positive on the grid
grid_small = [p for p in S2 if sum(1 for c in p if c != 0) <= 2][:40]
cands = [Fr(v) for v in (-1, Fr(-1, 2), 0, Fr(1, 2), 1)]
survivors = []
for vals in itertools.product(cands, repeat=len(free)):
    Gi = Gsol.subs(dict(zip(free, vals)))
    if Gi.det() == 0:
        continue
    w = min_value(Gi, grid_small)
    if w[0] < 0:
        continue
    wi = min_value(Gi.inv(), grid_small)
    if wi[0] < 0:
        continue
    survivors.append(vals)
print('Q2: free parameters scanned over %s^%d; two-sided product-positive survivors on the grid: %d'
      % ('{-1,-1/2,0,1/2,1}', len(free), len(survivors)))
for s in survivors:
    print('    ', dict(zip(map(str, free), s)))

# the local frame symmetries: L = diag(1, ±1, ±1, 1) on each factor (fix u, z, commute with N)
def L(sx, sy):
    return sp.diag(1, sx, sy, 1)
conj_class = set()
for (ax, ay, bx, by) in itertools.product((1, -1), repeat=4):
    LA = L(ax, ay); LB = L(bx, by)
    Cc = sp.kronecker_product(LA, LB) * C * sp.kronecker_product(LA, LB).inv()
    m = sp.solve([sp.expand(x - y) for x, y in zip(list(Gsol), list(Cc))], free, dict=True)
    if m:
        conj_class.add(tuple(sorted((str(kk), vv) for kk, vv in m[0].items())))
print('Q3: local frame conjugates L_A⊗L_B of the CNOT inside the family: %d distinct parameter points' % len(conj_class))
for c in sorted(conj_class):
    print('    ', dict(c))
surv_set = {tuple(sorted((str(kk), vv) for kk, vv in zip(free, s))) for s in survivors}
print('Q3: survivors not in the CNOT conjugacy class:', [dict(c) for c in sorted(surv_set - conj_class)])
print('Q3: CNOT conjugates not among survivors (grid too coarse if nonempty):', [dict(c) for c in sorted(conj_class - surv_set)])

# a finer, numerical scan of the continuous free directions for positivity of G alone (one-sided)
import random
random.seed(7)
def num_min(Gi, trials=4000):
    import numpy as np
    Gn = np.array(Gi.evalf(), dtype=float)
    worst = 1e9
    for _ in range(trials):
        pts = []
        for _ in range(4):
            v = np.random.randn(3); v /= np.linalg.norm(v); pts.append(np.concatenate(([1.0], v)))
        s, t, f, g = pts
        val = np.kron(f, g) @ Gn @ np.kron(s, t)
        worst = min(worst, val)
    return worst
import numpy as np
np.random.seed(7)
print('Q2: numerical one-sided positivity minimum along the free directions (value ≥ -1e-12 means positive on sample):')
for vals in itertools.product([Fr(-1), Fr(-3, 4), Fr(-1, 2), Fr(-1, 4), Fr(0), Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(1)], repeat=len(free)):
    Gi = Gsol.subs(dict(zip(free, vals)))
    if Gi.det() == 0:
        continue
    m = num_min(Gi, 1500)
    if m > -1e-9:
        print('    ', dict(zip(map(str, free), vals)), 'min %.3e' % m)

# ---- Q4: parity controls -----------------------------------------------------------------------------
for d in (2, 3, 4, 5, 6, 7):
    splits = [(p, d - 1 - p) for p in range(d)]
    eq = [s for s in splits if s[0] == s[1]]
    print('Q4: d=%d splits (p,q): %s; p=q: %s' % (d, splits, eq if eq else 'none'))
print('dim1_probe: done')
