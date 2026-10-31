"""Exact (Fraction) toolkit for SC-16: rooted visible maps of finite bijections, readback gaps,
P-divisibility by exact simplex with verified certificates, TV-monotonicity, exact C3 check.
Run only with python3 -I -B.  No floating point is used in any decision."""
from fractions import Fraction as F
from itertools import combinations
import math

# ---------------------------------------------------------------- exact LP feasibility
def lp_feasible(A, b):
    """Decide {lam >= 0 : A lam = b}.  Returns ('feas', lam) or ('infeas', z) with z^T A <= 0, z^T b > 0.
    Phase-1 simplex, Bland's rule, Fractions.  Certificates are verified here and again by callers."""
    m, N = len(A), len(A[0])
    sg = [(-1 if b[i] < 0 else 1) for i in range(m)]
    T = [[F(sg[i]) * A[i][j] for j in range(N)] + [F(1) if k == i else F(0) for k in range(m)] + [F(sg[i]) * b[i]]
         for i in range(m)]
    W = N + m
    basis = [N + i for i in range(m)]
    cost = [F(0)] * N + [F(1)] * m
    # reduced cost row
    def redrow():
        r = cost[:] + [F(0)]
        for i in range(m):
            cb = cost[basis[i]]
            if cb:
                for j in range(W + 1):
                    r[j] -= cb * T[i][j]
        return r
    R = redrow()
    while True:
        enter = next((j for j in range(W) if R[j] < 0), None)
        if enter is None:
            break
        best, leave = None, None
        for i in range(m):
            if T[i][enter] > 0:
                ratio = T[i][W] / T[i][enter]
                if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                    best, leave = ratio, i
        assert leave is not None  # phase 1 is bounded below by 0
        p = T[leave][enter]
        T[leave] = [v / p for v in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter] != 0:
                f = T[i][enter]
                T[i] = [T[i][j] - f * T[leave][j] for j in range(W + 1)]
        f = R[enter]
        R = [R[j] - f * T[leave][j] for j in range(W + 1)]
        basis[leave] = enter
    opt = -R[W]
    if opt == 0:
        lam = [F(0)] * N
        for i in range(m):
            if basis[i] < N:
                lam[basis[i]] = T[i][W]
        assert all(v >= 0 for v in lam)
        assert all(sum(A[i][j] * lam[j] for j in range(N)) == b[i] for i in range(m)), "primal check"
        return 'feas', lam
    y = [F(1) - R[N + i] for i in range(m)]          # dual of the sign-flipped system
    z = [F(sg[i]) * y[i] for i in range(m)]
    assert all(sum(z[i] * A[i][j] for i in range(m)) <= 0 for j in range(N)), "Farkas zA<=0"
    assert sum(z[i] * b[i] for i in range(m)) > 0, "Farkas zb>0"
    return 'infeas', z

def divisor(Gs, Gt):
    """Exists stochastic Lam with Gt = Gs Lam ?  Returns (bool, certificate)."""
    n = len(Gs)
    idx = lambda k, j: k * n + j
    A, b = [], []
    for i in range(n):
        for j in range(n):
            row = [F(0)] * (n * n)
            for k in range(n):
                row[idx(k, j)] = Gs[i][k]
            A.append(row); b.append(Gt[i][j])
    for k in range(n):
        row = [F(0)] * (n * n)
        for j in range(n):
            row[idx(k, j)] = F(1)
        A.append(row); b.append(F(1))
    st, cert = lp_feasible(A, b)
    if st == 'feas':
        Lam = [[cert[idx(k, j)] for j in range(n)] for k in range(n)]
        assert all(v >= 0 for r in Lam for v in r) and all(sum(r) == 1 for r in Lam)
        assert matmul(Gs, Lam) == Gt
        return True, Lam
    return False, cert

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def is_perm(G):
    return all(sum(1 for v in r if v != 0) == 1 and max(r) == 1 for r in G) and \
        len({r.index(max(r)) for r in G}) == len(G)

def identity(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def div2_closed_form(Gs, Gt):
    """Independent nV=2 test: Lam=[[a,1-a],[c,1-c]], a,c in [0,1]; Gt[i][0] = Gs[i][0] a + Gs[i][1] c."""
    (p, q), (r, s) = Gs
    u, w = Gt[0][0], Gt[1][0]
    det = p * s - q * r
    if det != 0:
        a = (u * s - q * w) / det
        c = (p * w - u * r) / det
        return 0 <= a <= 1 and 0 <= c <= 1
    # rows of Gs equal (both stochastic, det 0 => equal rows)
    if u != w:
        return False
    # need a,c in [0,1] with p a + q c = u: feasible since u in [0,1] (take a=c=u)
    return True

# ---------------------------------------------------------------- TV monotonicity
def nullvec(rows, d):
    """Exact null vector of a (d-1) x d system (rank d-1 assumed) or None."""
    M = [r[:] for r in rows]
    piv, rk = [], 0
    for c in range(d):
        pr = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if pr is None:
            continue
        M[rk], M[pr] = M[pr], M[rk]
        pv = M[rk][c]; M[rk] = [v / pv for v in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c]; M[i] = [M[i][j] - f * M[rk][j] for j in range(d)]
        piv.append(c); rk += 1
    if rk != d - 1:
        return None
    free = [c for c in range(d) if c not in piv][0]
    x = [F(0)] * d; x[free] = F(1)
    for i, c in enumerate(piv):
        x[c] = -M[i][free]
    return x

def tv_monotone_all(Gseq):
    """For every zero-sum v: ||v G_{t+1}||_1 <= ||v G_t||_1, consecutive t.  Exact, via extreme rays."""
    n = len(Gseq[0])
    # basis of zero-sum space: e_i - e_{n-1}
    B = [[F(int(j == i)) - F(int(j == n - 1)) for j in range(n)] for i in range(n - 1)]
    d = n - 1
    def img(c, G):  # coefficients c in basis -> v G
        v = [sum(c[i] * B[i][j] for i in range(d)) for j in range(n)]
        return [sum(v[k] * G[k][j] for k in range(n)) for j in range(n)]
    for t in range(len(Gseq) - 1):
        G0, G1 = Gseq[t], Gseq[t + 1]
        if all(G1[i] == G1[0] for i in range(n)):
            continue          # v G1 = 0 for every zero-sum v: the inequality holds trivially
        if d > 3:
            return None, 'not decided (nV > 4, no shortcut)'
        # hyperplanes in c-space: (v G)_j = 0 for G in (G0,G1), j
        H = []
        for G in (G0, G1):
            for j in range(n):
                h = [sum(B[i][k] * G[k][j] for k in range(n)) for i in range(d)]
                if any(h):
                    H.append(h)
        # coordinate hyperplanes refine the arrangement so every cell is a pointed cone
        H += [[F(int(i == j)) for j in range(d)] for i in range(d)]
        rays = []
        if d == 1:
            rays = [[F(1)], [F(-1)]]
        else:
            for comb in combinations(H, d - 1):
                x = nullvec([list(h) for h in comb], d)
                if x is not None:
                    rays += [x, [-v for v in x]]
            if not rays:  # all maps vanish on zero-sum space or no arrangement: test basis
                rays = [B_i for B_i in [[F(int(i == j)) for j in range(d)] for i in range(d)]]
        for c in rays:
            if sum(abs(v) for v in img(c, G1)) > sum(abs(v) for v in img(c, G0)):
                return False, (t, c)
    return True, None

def tv_monotone_roots(Gseq):
    n = len(Gseq[0])
    for a in range(n):
        for b in range(a + 1, n):
            ds = [sum(abs(G[a][j] - G[b][j]) for j in range(n)) for G in Gseq]
            for t in range(len(ds) - 1):
                if ds[t + 1] > ds[t]:
                    return False, (a, b, t)
    return True, None

# ---------------------------------------------------------------- models
class Model:
    def __init__(self, nV, nH, phi, muH, muV=None, name=''):
        self.nV, self.nH, self.phi, self.muH = nV, nH, list(phi), list(muH)
        self.muV = muV if muV is not None else [F(1, nV)] * nV
        self.name = name
        S = nV * nH
        assert sorted(self.phi) == list(range(S))
        assert sum(self.muH) == 1 and sum(self.muV) == 1
        # order L
        L, seen = 1, [False] * S
        for s in range(S):
            if not seen[s]:
                c, x = 0, s
                while not seen[x]:
                    seen[x] = True; x = self.phi[x]; c += 1
                L = L * c // math.gcd(L, c)
        self.L = L
        self.T = 2 * L + 2
        self.traj = {}
        for x in range(nV):
            for h in range(nH):
                s, tr = x * nH + h, []
                for _ in range(self.T + 1):
                    tr.append(s); s = self.phi[s]
                self.traj[(x, h)] = tr
        self.w = {(x, h): self.muV[x] * self.muH[h] for x in range(nV) for h in range(nH)}
        self._G = {}
        self.r = next(t for t in range(1, L + 1) if self.Gamma(t) == identity(nV))

    def vis(self, s):
        return s // self.nH

    def Gamma(self, t):
        if t not in self._G:
            G = [[F(0)] * self.nV for _ in range(self.nV)]
            for a in range(self.nV):
                for h in range(self.nH):
                    if self.muH[h]:
                        G[a][self.vis(self.traj[(a, h)][t])] += self.muH[h]
            self._G[t] = G
        return self._G[t]

    def hist_groups(self, k):
        """prefix (x_0..x_k) -> list of (initial state key, weight) with positive weight."""
        g = {}
        for key, wt in self.w.items():
            if wt:
                tr = self.traj[key]
                g.setdefault(tuple(self.vis(s) for s in tr[:k + 1]), []).append((key, wt))
        return g

    def next_law(self, members, k):
        tot = sum(w for _, w in members)
        law = [F(0)] * self.nV
        for key, w in members:
            law[self.vis(self.traj[key][k + 1])] += w / tot
        return law

    def gap(self, k):
        """Max TV gap at order k between histories with a common present; also C2s at k."""
        g = self.hist_groups(k)
        bypres = {}
        for pre, mem in g.items():
            bypres.setdefault(pre[-1], []).append((pre, mem))
        best, wit, c2s = F(0), None, False
        for c, lst in bypres.items():
            for (p1, m1), (p2, m2) in combinations(lst, 2):
                l1, l2 = self.next_law(m1, k), self.next_law(m2, k)
                d = sum(abs(u - v) for u, v in zip(l1, l2)) / 2
                if d > best:
                    best, wit = d, (p1, p2, l1, l2)
                # hidden-state law at time k
                def hl(m):
                    tot = sum(w for _, w in m); h = {}
                    for key, w in m:
                        hh = self.traj[key][k] % self.nH; h[hh] = h.get(hh, F(0)) + w / tot
                    return h
                if hl(m1) != hl(m2):
                    c2s = True
        return best, wit, c2s

    def c1(self, n):
        """literal C1: some t<=n-1, c, two positive-prob full states (c,h),(c,h') at time t with different visible successors."""
        for t in range(n):
            succ = {}
            for key, wt in self.w.items():
                if wt:
                    s = self.traj[key][t]
                    succ.setdefault(self.vis(s), set()).add(self.vis(self.traj[key][t + 1]))
            if any(len(v) > 1 for v in succ.values()):
                return True
        return False

    def c1_hist(self, n):
        for t in range(n):
            for pre, mem in self.hist_groups(t).items():
                if sum(1 for v in self.next_law(mem, t) if v) > 1:
                    return True
        return False

    def static_bath(self):
        return all(self.phi[s] % self.nH == s % self.nH for s in range(self.nV * self.nH))

    def cmi_pow(self, t, fut_end):
        """Return (num, den, D) with 2^{D*I} = num/den exactly, I = I(X_{<t}; X_{t+1..fut_end} | X_t)."""
        J = {}
        for key, wt in self.w.items():
            if wt:
                tr = [self.vis(s) for s in self.traj[key]]
                k = (tuple(tr[:t]), tr[t], tuple(tr[t + 1:fut_end + 1]))
                J[k] = J.get(k, F(0)) + wt
        pc, pac, pcb = {}, {}, {}
        for (a, c, b), p in J.items():
            pc[c] = pc.get(c, F(0)) + p; pac[(a, c)] = pac.get((a, c), F(0)) + p; pcb[(c, b)] = pcb.get((c, b), F(0)) + p
        D = 1
        for p in J.values():
            D = D * p.denominator // math.gcd(D, p.denominator)
        num, den = 1, 1
        for (a, c, b), p in J.items():
            ratio = p * pc[c] / (pac[(a, c)] * pcb[(c, b)])
            e = int(p * D)
            num *= ratio.numerator ** e; den *= ratio.denominator ** e
        return num, den, D

    def c3(self, n=None):
        """Exact check log2 nH >= I*.  n=None: full process sup_t (t=1..2L, future t+1..t+L); else window."""
        ok, worst = True, F(0)
        ts = range(1, 2 * self.L + 1) if n is None else range(1, n)
        for t in ts:
            fe = t + self.L if n is None else n
            num, den, D = self.cmi_pow(t, fe)
            if num * 1 > den * self.nH ** D:   # 2^{D I} > nH^D  <=>  I > log2 nH
                ok = False
            # saturation flag: equality
            if num == den * self.nH ** D:
                worst = F(1)
        return ok, worst == 1

    def kernel_divisor(self, s, t):
        """R2: Lambda = P(X_t | X_s) of the realized process."""
        n = self.nV
        P = [[F(0)] * n for _ in range(n)]; ps = [F(0)] * n
        for key, wt in self.w.items():
            if wt:
                tr = self.traj[key]
                P[self.vis(tr[s])][self.vis(tr[t])] += wt; ps[self.vis(tr[s])] += wt
        for k in range(n):
            if ps[k]:
                P[k] = [v / ps[k] for v in P[k]]
            else:
                P[k] = [F(int(j == k)) for j in range(n)]
        return matmul(self.Gamma(s), P) == self.Gamma(t)


_divcache = {}
def div_cached(Gs, Gt):
    key = (tuple(map(tuple, Gs)), tuple(map(tuple, Gt)))
    if key not in _divcache:
        _divcache[key] = divisor(Gs, Gt)[0]
    return _divcache[key]

def analyze(M, nmax=None, readings=('R1', 'R2', 'R3', 'R4'), want_c3=True):
    """Per accessible window n (2 <= n < r): flags.  Returns list of dicts."""
    out = []
    r = M.r
    top = r - 1 if nmax is None else min(nmax, r - 1)
    gaps = {k: M.gap(k) for k in range(0, top)}
    c3full = M.c3() if want_c3 else (True, False)
    pairdiv = {}
    for n in range(2, top + 1):
        ks = [k for k in range(1, n) if gaps[k][0] > 0]
        rec = dict(n=n, r=r, L=M.L, c4_orders=ks)
        rec['C4'] = bool(ks)
        rec['C1'] = M.c1(n); rec['C1hist'] = M.c1_hist(n)
        rec['C2s'] = any(gaps[k][2] for k in ks)
        rec['C3'] = c3full[0]; rec['C3sat'] = c3full[1]
        if 'R1' in readings:
            ok = True
            for t in range(1, n + 1):
                for s in range(1, t):
                    if (s, t) not in pairdiv:
                        pairdiv[(s, t)] = div_cached(M.Gamma(s), M.Gamma(t))
                    if not pairdiv[(s, t)]:
                        ok = False; break
                if not ok:
                    break
            rec['R1'] = ok  # s = 0 trivially divisible (Gamma_0 = I)
        if 'R2' in readings:
            rec['R2'] = all(M.kernel_divisor(s, t) for t in range(1, n + 1) for s in range(0, t))
        seq = [M.Gamma(t) for t in range(0, n + 1)]
        if 'R3' in readings:
            rec['R3'] = tv_monotone_all(seq)[0]
        if 'R4' in readings:
            rec['R4'] = tv_monotone_roots(seq)[0]
        out.append(rec)
    return out, gaps
