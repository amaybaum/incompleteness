"""A3: first-order rigidity of the reference gate R inside the generator's own feasible set (read-only analysis).

The generator's feasible set is  K = {(G, H) in F x F : G, H pool-positive (pool A)}  with the target G H = 1.
Near (R, R^-1) a gate path G(t) = R + t delta + O(t^2) has H(t) = R^-1 - t R^-1 delta R^-1 + O(t^2), so delta must lie in
the cone  C = {delta in T F : <q, delta> >= 0 for every pool quadruple q tight at R,
                              <q, -R^-1 delta R^-1> >= 0 for every quadruple tight at R^-1}.
Reported:
  rank of the tight rows (exact: Fraction elimination for eball3; modular rank, an upper bound on the nullity, for omegah),
  dim L, L = the lineality space (all tight rows vanish),
  and the LP maximum of the summed tight values over C intersected with the box |delta| <= 1 (0 means C = L: R is
  first-order rigid modulo L in the generator's own relaxation).
"""
import json
import os
import sys
from fractions import Fraction as Fr

import numpy as np
from scipy.optimize import linprog

PRE, WORK, control = sys.argv[1:4]
POOLS = sys.argv[4] if len(sys.argv) > 4 else 'A'
sys.path.insert(0, PRE)
import controls_gen as cg       # noqa: E402
import controls_verify as cv    # noqa: E402

body = cv.Body(control)
pool = json.load(open(os.path.join(WORK, 'pool-%s.json' % control)))
prob = cg.Problem(pool)
if POOLS == 'AB':       # widen to pool A + pool B (the verifier's view)
    prob.S = np.array([[1.0] + [float(c) for c in s] for p in 'AB' for s in body.pools[p]['states']])
    prob.E = np.array([[float(c) for c in e] for p in 'AB' for e in body.pools[p]['effects']])
    prob.ns, prob.ne = len(prob.S), len(prob.E)
    statesX = [s for p in 'AB' for s in body.pools[p]['states']]
    effX = [e for p in 'AB' for e in body.pools[p]['effects']]
else:
    statesX = body.pools['A']['states']
    effX = body.pools['A']['effects']
R = body.reference
if os.environ.get('A3_REF'):    # correction pass: the point tested may be any accepted member, not only R
    R = cv.from_json_matrix(json.load(open(os.environ['A3_REF']))['G'])
Ri = cv.inverse(R)
Rf = np.array([[float(v) for v in r] for r in R])
Rif = np.array([[float(v) for v in r] for r in Ri])
valsG = prob.values(Rf)
valsH = prob.values(Rif)
tG = np.argwhere(np.abs(valsG) < 1e-12)
tH = np.argwhere(np.abs(valsH) < 1e-12)
print('== %s pools %s: dim F %d; quadruples %d; tight for R %d, for R^-1 %d' % (control, POOLS, prob.nv, valsG.size,
                                                                             len(tG), len(tH)))
# float rows
rowsG, _ = prob.rows([tuple(q) for q in tG])
n, nn = prob.n, prob.n * prob.n
rowsH = np.zeros((len(tH), prob.nv))
for t, (x, y, a, b) in enumerate(tH):
    ef = np.outer(prob.E[a], prob.E[b]).reshape(-1)
    w = np.outer(prob.S[x], prob.S[y]).reshape(-1)
    av = ef @ Rif
    bv = Rif @ w
    d = av[prob.fp] * bv[prob.fq]
    rowsH[t] = -(d @ prob.Nmat)
A = np.vstack([rowsG, rowsH])
# dedupe rows (scale-normalised) to keep the rank computation small
key = {}
for r in A:
    m = np.abs(r).max()
    if m < 1e-12:
        continue
    k = tuple(np.round(r / m, 9))
    key.setdefault(k, r)
U = np.array(list(key.values()))
print('distinct nonzero tight rows: %d' % len(U))
svals = np.linalg.svd(U, compute_uv=False)
rk_float = int((svals > 1e-9 * svals.max()).sum())
print('float rank of tight rows: %d -> float dim L = %d' % (rk_float, prob.nv - rk_float))


def rank_mod(rows, p):
    M = [[v % p for v in r] for r in rows]
    rk, ncol = 0, len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][c], p - 2, p)
        M[rk] = [v * inv % p for v in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk


# exact rows (Fraction) for the tight quadruples, confirmed exactly tight; rank modulo primes on integer rescalings
from math import gcd
homx = [[Fr(1)] + list(x) for x in statesX]
basis = prob.basis_exact
fpl, fql = list(prob.fp), list(prob.fq)


def exrow(x, y, a, b, M):
    ef = [p * q for p in effX[a] for q in effX[b]]
    w = [p * q for p in homx[x] for q in homx[y]]
    if M is None:
        av, bv, sg = ef, w, 1
    else:
        av = [sum((ef[i] * M[i][j] for i in range(nn) if ef[i] and M[i][j]), Fr(0)) for j in range(nn)]
        bv = [sum((M[i][j] * w[j] for j in range(nn) if w[j] and M[i][j]), Fr(0)) for i in range(nn)]
        sg = -1
    d = [av[p] * bv[q] for p, q in zip(fpl, fql)]
    return [sg * sum((di * bk[i] for i, di in enumerate(d) if di and bk[i]), Fr(0)) for bk in basis]


def exval(x, y, a, b, M):
    ef = [p * q for p in effX[a] for q in effX[b]]
    w = [p * q for p in homx[x] for q in homx[y]]
    Mw = [sum((M[i][j] * w[j] for j in range(nn) if w[j] and M[i][j]), Fr(0)) for i in range(nn)]
    return sum((e * v for e, v in zip(ef, Mw) if e), Fr(0))


LIM = int(os.environ.get('A3_EXACT_LIMIT', '6000'))
if len(tG) + len(tH) <= LIM:
    assert all(exval(*map(int, q), R) == 0 for q in tG) and all(exval(*map(int, q), Ri) == 0 for q in tH)
    ER = [exrow(*map(int, q), None) for q in tG] + [exrow(*map(int, q), Ri) for q in tH]
    IR = []
    for r in ER:
        L = 1
        for f in r:
            L = L * f.denominator // gcd(L, f.denominator)
        IR.append([int(f * L) for f in r])
    print('exact tightness confirmed for all %d + %d quadruples' % (len(tG), len(tH)))
    for p in (2147483647, 1000000007):
        rp = rank_mod(IR, p)
        print('rank mod %d of the exact tight rows: %d -> dim L over Q <= %d' % (p, rp, prob.nv - rp))
else:
    print('exact rows skipped (%d tight quadruples > limit %d)' % (len(tG) + len(tH), LIM))


# Stiemke certificate (exact): y > 0 with sum_i y_i ER_i = 0 proves that no delta has all tight values >= 0 with one > 0;
# with rank(ER) = dim F (above, modular) this proves C = {0}: R is first-order isolated in the coupled relaxation.
if os.environ.get('A3_STIEMKE') and len(tG) + len(tH) <= LIM:
    m = len(ER)
    Af = np.array([[float(v) for v in r] for r in ER])
    # LP: max s  s.t.  Af^T y = 0, y >= s, y <= 1
    c = np.zeros(m + 1); c[-1] = -1
    Aeq = np.hstack([Af.T, np.zeros((prob.nv, 1))])
    Aub = np.hstack([-np.eye(m), np.ones((m, 1))])
    r = linprog(c, A_ub=Aub, b_ub=np.zeros(m), A_eq=Aeq, b_eq=np.zeros(prob.nv), bounds=[(0, 1)] * m + [(None, 1)], method='highs')
    print('Stiemke LP: status %d, min y = %.3e' % (r.status, -r.fun))
    if r.status == 0 and -r.fun > 0:
        y = r.x[:m]
        # exact nullspace of ER^T (prob.nv equations in m unknowns) by Fraction elimination
        rows = [[ER[i][k] for i in range(m)] for k in range(prob.nv)]
        piv = []; M = [list(rw) for rw in rows]; rk = 0
        for col in range(m):
            p = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
            if p is None: continue
            M[rk], M[p] = M[p], M[rk]; pv = M[rk][col]; M[rk] = [v / pv for v in M[rk]]
            for i in range(len(M)):
                if i != rk and M[i][col] != 0:
                    f = M[i][col]; M[i] = [a - f * b for a, b in zip(M[i], M[rk])]
            piv.append(col); rk += 1
        free = [j for j in range(m) if j not in set(piv)]
        # y is determined by its free coordinates: take them rational (rounded), solve pivots exactly
        yq = [Fr(0)] * m
        for j in free:
            yq[j] = Fr(float(y[j])).limit_denominator(10 ** 6)
        for i, col in enumerate(piv):
            yq[col] = -sum((M[i][j] * yq[j] for j in free if M[i][j] != 0), Fr(0))
        ok_null = all(sum((ER[i][k] * yq[i] for i in range(m) if yq[i] and ER[i][k]), Fr(0)) == 0 for k in range(prob.nv))
        print('exact Stiemke certificate: nullspace %s, all y_i > 0: %s, min y_i = %.3e'
              % (ok_null, all(v > 0 for v in yq), float(min(yq))))

# LP: max sum of tight values over C cap box
c = -A.sum(axis=0)
res = linprog(c, A_ub=-A, b_ub=np.zeros(len(A)), bounds=[(-1, 1)] * prob.nv, method='highs')
print('LP status %d; max summed tight value over C cap box = %.3e' % (res.status, -res.fun))
# per-direction: is any one-sided direction outside L?  max of each row individually
mx = 0.0
for i in range(0, len(U)):
    r = linprog(-U[i], A_ub=-A, b_ub=np.zeros(len(A)), bounds=[(-1, 1)] * prob.nv, method='highs')
    mx = max(mx, -r.fun)
print('max over distinct tight rows of the single-row LP: %.3e' % mx)
