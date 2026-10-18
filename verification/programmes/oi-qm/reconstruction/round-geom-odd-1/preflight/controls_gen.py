"""GEOM-ODD-1 controls preflight: the generator (floating point; numpy, scipy's HiGHS).

It is told the body's corner z, its NOT N and the generation pool A (states and effects, read as data from the
verifier's `--emit-pool`), and nothing about any gate. It writes a rational candidate G, or none, and is never trusted:
`controls_verify.py` decides.

Method (frozen for the preflight; design item 3's coupling of G and G^-1).
  F    the linear clauses solved exactly: the free pattern of relT and relC for a diagonal N (an entry (mu nu, mu' nu')
       may be nonzero only if h_nu = h_nu' and h_mu = h_mu' h_nu', H = 1 (+) N), the frame on the four corner products,
       by exact elimination: G = G0 + sum_k lam_k B_k. A gate's inverse satisfies the same clauses, so H = G^-1 is
       sought in F too.
  P    posFwd on pool A as linear constraints on lam, by constraint generation: every value on the pool is evaluated
       at the current point and the most negative quadruples are added (at most ADD per round).
  ALT  multi-start alternating L1 coupling: start s takes the vertex of P minimising a seeded random objective c_s for
       G and -c_s for H, then alternates G <- argmin |G H - 1|_1 over P and H <- argmin |G H - 1|_1 over P, each
       solved by HiGHS with the separation repeated until the point is pool-feasible to SEP_TOL. A start ends when
       max |G H - 1| < ACCEPT (a candidate), or after STALL rounds without a decrease of the residual by 1e-6.
  EXACT a converged lam is rounded coordinatewise (Fraction.limit_denominator, bounds 1, 2, 4, ..., 2^20); the first
       bound whose exact G = G0 + sum lam_k B_k is within 1e-6 of the float G is written. The candidate lies in F
       exactly by construction; nothing else about it is assumed.
  DEADLINE every LP and every start checks the wall-clock deadline passed by the driver; at the deadline the generator
       writes `status: deadline` and no candidate.
"""
import json
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog

SEP_TOL = 1e-7
ACCEPT = 1e-9
STALL = 3
ADD = 1500
INIT = 3000
BOX = 8.0


def rref_solve(rows, rhs, nvar):
    A = [dict(r) for r in rows]
    b = list(rhs)
    piv, r = [], 0
    for c in range(nvar):
        p = next((i for i in range(r, len(A)) if A[i].get(c, 0) != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        b[r], b[p] = b[p], b[r]
        inv = 1 / A[r][c]
        A[r] = {k: v * inv for k, v in A[r].items()}
        b[r] *= inv
        for i in range(len(A)):
            if i != r and A[i].get(c, 0) != 0:
                f = A[i][c]
                for k, v in A[r].items():
                    nv = A[i].get(k, 0) - f * v
                    if nv == 0:
                        A[i].pop(k, None)
                    else:
                        A[i][k] = nv
                b[i] -= f * b[r]
        piv.append(c)
        r += 1
    if any(b[i] != 0 for i in range(r, len(A))):
        return None
    part = [Fr(0)] * nvar
    for i, c in enumerate(piv):
        part[c] = b[i]
    basis = []
    ps = set(piv)
    for fc in range(nvar):
        if fc in ps:
            continue
        v = [Fr(0)] * nvar
        v[fc] = Fr(1)
        for i, c in enumerate(piv):
            if A[i].get(fc, 0):
                v[c] = -A[i][fc]
        basis.append(v)
    return part, basis


def build_F(D, z, N):
    n = D + 1
    assert all(N[i][j] == 0 for i in range(D) for j in range(D) if i != j), 'N must be diagonal'
    hh = [Fr(1)] + [N[i][i] for i in range(D)]
    free = [(mu * n + nu, m2 * n + n2) for mu in range(n) for nu in range(n) for m2 in range(n) for n2 in range(n)
            if hh[nu] == hh[n2] and hh[mu] == hh[m2] * hh[n2]]
    pos = {pq: i for i, pq in enumerate(free)}
    hom = lambda x: [Fr(1)] + list(x)
    corner = {0: z, 1: [-c for c in z]}
    rows, rhs = [], []
    for a in (0, 1):
        for b in (0, 1):
            w = [p * q for p in hom(corner[a]) for q in hom(corner[b])]
            u = [p * q for p in hom(corner[a]) for q in hom(corner[(a + b) % 2])]
            for p in range(n * n):
                row = {pos[(p, q)]: w[q] for q in range(n * n) if w[q] != 0 and (p, q) in pos}
                if row:
                    rows.append(row)
                    rhs.append(u[p])
                elif u[p] != 0:
                    return None
    sol = rref_solve(rows, rhs, len(free))
    if sol is None:
        return None
    part, basis = sol
    return free, part, basis


class Problem:
    def __init__(self, pool):
        self.D = pool['D']
        self.n = self.D + 1
        z = [Fr(c) for c in pool['z']]
        N = [[Fr(c) for c in r] for r in pool['N']]
        self.free, part, basis = build_F(self.D, z, N)
        nn = self.n * self.n
        self.nv = len(basis)
        fp = np.array([p for p, q in self.free])
        fq = np.array([q for p, q in self.free])
        self.fp, self.fq = fp, fq
        self.part_exact, self.basis_exact = part, basis
        self.G0 = np.zeros((nn, nn))
        self.G0[fp, fq] = [float(v) for v in part]
        self.Nmat = np.array([[float(v) for v in bv] for bv in basis]).T          # nfree x nv
        self.g0free = np.array([float(v) for v in part])
        self.Bm = np.zeros((self.nv, nn, nn))
        for k in range(self.nv):
            self.Bm[k][fp, fq] = self.Nmat[:, k]
        S = np.array([[1.0] + [float(Fr(c)) for c in s] for s in pool['states']])
        E = np.array([[float(Fr(c)) for c in e] for e in pool['effects']])
        self.S, self.E = S, E
        self.ns, self.ne = len(S), len(E)

    def G(self, lam):
        return self.G0 + np.tensordot(lam, self.Bm, 1)

    def values(self, M):
        """all pool values (x, y, e, f) of M, shape (ns, ns, ne, ne)"""
        n = self.n
        T = M.reshape(n, n, n, n)                              # [mu, nu, kappa, lambda]
        W = np.einsum('mnkl,xk,yl->xymn', T, self.S, self.S)
        return np.einsum('am,xymn,bn->xyab', self.E, W, self.E)

    def rows(self, quads):
        """for quadruples (x, y, a, b): rows r with value = c + r . lam"""
        n = self.n
        out_r = np.zeros((len(quads), self.nv))
        out_c = np.zeros(len(quads))
        for t, (x, y, a, b) in enumerate(quads):
            ef = np.outer(self.E[a], self.E[b]).reshape(-1)
            w = np.outer(self.S[x], self.S[y]).reshape(-1)
            d = ef[self.fp] * w[self.fq]
            out_r[t] = d @ self.Nmat
            out_c[t] = d @ self.g0free
        return out_r, out_c


def solve_lp(c, A_ub, b_ub, A_eq, b_eq, bounds, deadline):
    left = deadline - time.monotonic()
    if left < 5:
        return None
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs',
                  options={'time_limit': max(1.0, left - 2)})
    return res if res.status == 0 else None


class Cuts:
    def __init__(self, prob, rng):
        self.prob = prob
        tot = prob.ns * prob.ns * prob.ne * prob.ne
        idx = rng.choice(tot, size=min(INIT, tot), replace=False)
        self.quads = [tuple(int(v) for v in np.unravel_index(i, (prob.ns, prob.ns, prob.ne, prob.ne))) for i in idx]
        self.R, self.C = prob.rows(self.quads)

    def separate(self, lam):
        vals = self.prob.values(self.prob.G(lam))
        bad = np.argwhere(vals < -SEP_TOL)
        if len(bad) == 0:
            return False
        order = np.argsort(vals[tuple(bad.T)])[:ADD]
        new = [tuple(int(v) for v in bad[o]) for o in order]
        R, C = self.prob.rows(new)
        self.quads += new
        self.R = np.vstack([self.R, R])
        self.C = np.concatenate([self.C, C])
        return True


def vertex(prob, cuts, cobj, deadline):
    nv = prob.nv
    while True:
        res = solve_lp(cobj, -cuts.R, cuts.C, None, None, [(-BOX, BOX)] * nv, deadline)
        if res is None:
            return None
        if not cuts.separate(res.x):
            return res.x


def couple(prob, cuts, Hfix, left, deadline):
    """argmin over P of |G Hfix - 1|_1 (left) or |Hfix G - 1|_1"""
    nv, nn = prob.nv, prob.n * prob.n
    if left:
        J = np.einsum('kij,jl->kil', prob.Bm, Hfix).reshape(nv, -1).T
        R0 = (prob.G0 @ Hfix - np.eye(nn)).reshape(-1)
    else:
        J = np.einsum('ij,kjl->kil', Hfix, prob.Bm).reshape(nv, -1).T
        R0 = (Hfix @ prob.G0 - np.eye(nn)).reshape(-1)
    m = J.shape[0]
    Js = sp.csr_matrix(J)
    I = sp.identity(m, format='csr')
    while True:
        c = np.concatenate([np.zeros(nv), np.ones(m)])
        A = sp.vstack([sp.hstack([Js, -I]), sp.hstack([-Js, -I]),
                       sp.hstack([sp.csr_matrix(-cuts.R), sp.csr_matrix((len(cuts.C), m))])], format='csr')
        b = np.concatenate([-R0, R0, cuts.C])
        res = solve_lp(c, A, b, None, None, [(-BOX, BOX)] * nv + [(0, None)] * m, deadline)
        if res is None:
            return None
        lam = res.x[:nv]
        if not cuts.separate(lam):
            return lam


def exactify(prob, lam):
    Gf = prob.G(lam)
    for k in range(21):
        den = 2 ** k
        lr = [Fr(float(v)).limit_denominator(den) for v in lam]
        g = [prob.part_exact[i] + sum(lr[j] * prob.basis_exact[j][i] for j in range(prob.nv) if lr[j])
             for i in range(len(prob.free))]
        nn = prob.n * prob.n
        G = [[Fr(0)] * nn for _ in range(nn)]
        for (p, q), v in zip(prob.free, g):
            G[p][q] = v
        if np.abs(np.array([[float(v) for v in r] for r in G]) - Gf).max() < 1e-6:
            return G
    return None


def main(argv):
    pool_path, out_path, deadline_s = argv[1], argv[2], float(argv[3])
    t0 = time.monotonic()
    deadline = t0 + deadline_s
    pool = json.load(open(pool_path))
    prob = Problem(pool)
    log = {'control': pool['control'], 'dim_F': prob.nv, 'starts': []}
    cand = None
    s = 0
    while time.monotonic() < deadline - 10 and cand is None:
        rng = np.random.RandomState(1000 + s)
        cuts = Cuts(prob, rng)
        cobj = rng.randn(prob.nv)
        lg = vertex(prob, cuts, cobj, deadline)
        lh = vertex(prob, cuts, -cobj, deadline) if lg is not None else None
        best, stall, it = np.inf, 0, 0
        while lg is not None and lh is not None and time.monotonic() < deadline - 5:
            lg = couple(prob, cuts, prob.G(lh), True, deadline)
            if lg is None:
                break
            lh = couple(prob, cuts, prob.G(lg), False, deadline)
            if lh is None:
                break
            it += 1
            resid = np.abs(prob.G(lg) @ prob.G(lh) - np.eye(prob.n * prob.n)).max()
            if resid < ACCEPT:
                cand = exactify(prob, lg)
                break
            if resid < best - 1e-6:
                best, stall = resid, 0
            else:
                stall += 1
                if stall >= STALL:
                    break
        log['starts'].append({'start': s, 'rounds': it, 'best_residual': None if best == np.inf else float(best),
                              'cuts': len(cuts.quads)})
        print('start %d: rounds %d, best residual %s, cuts %d, %.0f s' % (s, it, best, len(cuts.quads),
                                                                            time.monotonic() - t0), flush=True)
        s += 1
    out = {'control': pool['control'], 'status': 'candidate' if cand is not None else 'deadline',
           'G': None if cand is None else [[str(v) for v in r] for r in cand], 'log': log}
    json.dump(out, open(out_path, 'w'))
    print('generator: %s after %d start(s)' % (out['status'], s), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
