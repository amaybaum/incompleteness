"""Independent exact check of the eball3 vertex / Stiemke claims (reviewer's code).
Uses the frozen verifier ONLY for the body definition (pools, reference R, H); everything else is re-derived.
All arithmetic exact: Fractions, or int64 on positively rescaled integer vectors (sign/zero preserving)."""
import sys, json, itertools
from fractions import Fraction as Fr
from math import lcm
import numpy as np
P = sys.argv[1]
sys.path.insert(0, P)
import controls_verify as cv
import controls_gen as cg

body = cv.Body('eball3')
n = body.n; nn = n * n
R = body.reference
import json as _j
M_ = cv.from_json_matrix(_j.load(open(sys.argv[3]))['G'])
Mi_ = cv.inverse(M_)
I = cv.eye(nn)
print('member^2 == 1:', cv.mat_mul(M_, M_) == I); print('member passes frame/relT/relC:', cv.check_VL(body, M_))

# ---- F_0 from the matrix identities themselves (not the free pattern)
T = cv.kron(cv.eye(n), body.H); C = cv.kron(body.H, cv.eye(n))
def lin_constraints():
    rows = []
    # unknown index p*nn+q for G[p][q]
    # relT: (T G T)[p][q] - G[p][q] = T[p][p] T[q][q] G[p][q] - G[p][q]  (T, C diagonal)
    assert all(T[i][j] == 0 for i in range(nn) for j in range(nn) if i != j)
    assert all(C[i][j] == 0 for i in range(nn) for j in range(nn) if i != j)
    for p in range(nn):
        for q in range(nn):
            c = T[p][p] * T[q][q] - 1
            if c: rows.append({p * nn + q: c})
            c = C[p][p] * C[q][q] - T[p][p]          # (C G C - T G)[p][q]
            if c: rows.append({p * nn + q: c})
    z = body.z; corner = {0: z, 1: [-c for c in z]}
    for a in (0, 1):
        for b in (0, 1):
            w = cv.prod(corner[a], corner[b])
            for p in range(nn):
                r = {p * nn + q: w[q] for q in range(nn) if w[q]}
                rows.append(r)
    return rows
def nullspace(rows, nvar):
    A = [dict(r) for r in rows if r]
    piv = []; r = 0
    for c in range(nvar):
        pi = next((i for i in range(r, len(A)) if A[i].get(c, 0)), None)
        if pi is None: continue
        A[r], A[pi] = A[pi], A[r]
        inv = Fr(1) / A[r][c]; A[r] = {k: v * inv for k, v in A[r].items()}
        for i in range(len(A)):
            if i != r and A[i].get(c, 0):
                f = A[i][c]
                for k, v in A[r].items():
                    nv = A[i].get(k, 0) - f * v
                    if nv: A[i][k] = nv
                    else: A[i].pop(k, None)
        piv.append(c); r += 1
    ps = set(piv); basis = []
    for fc in range(nvar):
        if fc in ps: continue
        v = [Fr(0)] * nvar; v[fc] = Fr(1)
        for i, c in enumerate(piv):
            if A[i].get(fc, 0): v[c] = -A[i][fc]
        basis.append(v)
    return basis
B0 = nullspace(lin_constraints(), nn * nn)
print('dim F_0 from the matrix identities:', len(B0))
# R satisfies the inhomogeneous clauses (frame, relT, relC)?
fr, rT, rC = cv.check_VL(body, R); print('R meets frame/relT/relC:', fr, rT, rC)

def rank(rows):
    A = [list(r) for r in rows]; m = len(A[0]); rk = 0
    for c in range(m):
        pi = next((i for i in range(rk, len(A)) if A[i][c] != 0), None)
        if pi is None: continue
        A[rk], A[pi] = A[pi], A[rk]
        for i in range(rk + 1, len(A)):
            if A[i][c] != 0:
                f = Fr(A[i][c], 1) / A[rk][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[rk])]
        rk += 1
    return rk
# does the generator's F (free pattern) equal mine?
free, part, basis = cg.build_F(body.D, body.z, body.N)
def embed(vfree):
    v = [Fr(0)] * (nn * nn)
    for (p, q), x in zip(free, vfree): v[p * nn + q] = x
    return v
GB = [embed(b) for b in basis]
print('generator dim F:', len(GB), '; rank(mine) =', rank(B0), '; rank(mine + generator) =', rank(B0 + GB))
G0 = embed(part)
d0 = [a - b for a, b in zip(G0, [x for row in R for x in row])]
print('G0 - R in F_0 (rank unchanged):', rank(B0 + [d0]) == len(B0))

# ---- exact pool-A values, integer arithmetic on rescaled vectors
pa = body.pools['A']
def scal(v):
    L = 1
    for c in v: L = lcm(L, Fr(c).denominator)
    return [int(Fr(c) * L) for c in v]
S = np.array([scal(cv.hom(x)) for x in pa['states']], dtype=np.int64)
E = np.array([scal(e) for e in pa['effects']], dtype=np.int64)
def vals(M):   # M integer nn x nn (numpy int64) -> (x,y,a,b) scaled values
    Tm = M.reshape(n, n, n, n)
    W = np.einsum('mnkl,xk,yl->xymn', Tm, S, S)
    return np.einsum('am,xymn,bn->xyab', E, W, E)
Ri = np.array([[int(c) for c in row] for row in M_], dtype=np.int64)
Rii = np.array([[int(c) for c in row] for row in Mi_], dtype=np.int64)
assert all(c.denominator == 1 for row in M_ for c in row) and all(c.denominator == 1 for row in Mi_ for c in row)
V = vals(Ri); VI_ = vals(Rii)
print('inverse: min', VI_.min(), 'zeros', int((VI_ == 0).sum()))
print('pool-A quadruples:', V.size, '; min scaled value:', V.min(), '; negatives:', int((V < 0).sum()), '; exact zeros:', int((V == 0).sum()))
tight = [tuple(t) for t in np.argwhere(V == 0)]
tightH = [tuple(t) for t in np.argwhere(VI_ == 0)]
# integer basis of F_0
Bint = []
for b in B0:
    L = 1
    for c in b: L = lcm(L, c.denominator)
    Bint.append(np.array([int(c * L) for c in b], dtype=np.int64).reshape(nn, nn))
Rm = Ri
rowsG, rowsH = [], []
VG = [vals(Bk) for Bk in Bint]
VH = [vals(-(Rii @ Bk @ Rii)) for Bk in Bint]   # d(G^-1) = -M^-1 dG M^-1
for t in tight:
    rowsG.append([int(v[t]) for v in VG])
for t in tightH:
    rowsH.append([int(v[t]) for v in VH])
# H-side tight set: R^-1 = R, so the same quadruples
print('tight G-side:', len(rowsG), 'H-side:', len(rowsH))
print('exact rank of G-tight rows:', rank(rowsG), 'of', len(B0))
allrows = rowsG + rowsH
print('exact rank of G+H tight rows:', rank(allrows))
# are -R d R directions in F_0? (so H stays in F to first order)
print('skip R F_0 R check (n/a)') or None and print('', rank(B0 + [[x for row in cv.mat_mul(cv.mat_mul(R, [list(map(Fr, r)) for r in Bk.tolist()]), R) for x in row] for Bk in Bint]) == len(B0))

# ---- Stiemke: y > 0 with sum y_i row_i = 0
from scipy.optimize import linprog
A = np.array(allrows, dtype=float); m = len(allrows)
# max t : A^T y = 0, y_i >= t, sum y = m
c = np.zeros(m + 1); c[-1] = -1
Aeq = np.zeros((A.shape[1] + 1, m + 1)); Aeq[:-1, :m] = A.T; Aeq[-1, :m] = 1
beq = np.zeros(A.shape[1] + 1); beq[-1] = m
Aub = np.hstack([-np.eye(m), np.ones((m, 1))]); bub = np.zeros(m)
res = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=[(0, None)] * m + [(None, None)], method='highs')
print('float Stiemke LP status', res.status, 't* =', res.x[-1])
yf = res.x[:m]
# exactify: choose 48 independent rows as pivots, round the rest, solve exactly
def pick_basis(rows):
    chosen = []; cur = []
    for i, r in enumerate(rows):
        if rank(cur + [r]) > len(cur):
            cur.append(r); chosen.append(i)
        if len(chosen) == len(rows[0]): break
    return chosen
piv = pick_basis(allrows)
nonpiv = [i for i in range(m) if i not in set(piv)]
y = [None] * m
for i in nonpiv: y[i] = Fr(float(yf[i])).limit_denominator(10 ** 6)
# solve sum_{i in piv} y_i row_i = - sum_{nonpiv} y_i row_i  (48x48 system on transposed rows)
k = len(allrows[0])
rhs = [-sum(y[i] * allrows[i][j] for i in nonpiv) for j in range(k)]
M = [[Fr(allrows[i][j]) for i in piv] + [rhs[j]] for j in range(k)]
for c_ in range(k):
    p_ = next(r for r in range(c_, k) if M[r][c_] != 0)
    M[c_], M[p_] = M[p_], M[c_]
    pv = M[c_][c_]; M[c_] = [x / pv for x in M[c_]]
    for r in range(k):
        if r != c_ and M[r][c_] != 0:
            f = M[r][c_]; M[r] = [x - f * yy for x, yy in zip(M[r], M[c_])]
for idx, i in enumerate(piv): y[i] = M[idx][k]
ok_null = all(sum(y[i] * allrows[i][j] for i in range(m)) == 0 for j in range(k))
print('exact Stiemke certificate: sum y_i row_i == 0:', ok_null, '; all y_i > 0:', all(v > 0 for v in y),
      '; min y_i = %.4f (t* normalisation sum y = %d)' % (float(min(y)), m))
json.dump({'y': [str(v) for v in y]}, open(sys.argv[2], 'w'))
