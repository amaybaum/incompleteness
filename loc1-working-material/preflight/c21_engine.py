"""LOC-1 preflight, leg T: exact complete backtracking search for product identifications (engine only).

Problem.  Given target matrices M_1..M_K (N x N, integer entries; a rational matrix is scaled by a common
denominator first, which changes no product test) and a grid Fin m x Fin n with N = m n, find the
bijections sigma: Fin N -> Fin m x Fin n, modulo post-composition with S_m x S_n and (when m = n) the
factor swap, such that every M_k^sigma = P_sigma M_k P_sigma^T is a Kronecker product A (x) B.  Here
M^sigma[sigma(i)][sigma(j)] = M[i][j] and grid point (a, b) has declared index a n + b, so the reshuffle is
    R[(a, a')][(b, b')] = M[sigma^{-1}(a, b)][sigma^{-1}(a', b')],
and M^sigma is a product iff R has rank <= 1 (PC).

Search.  Indices are assigned in a static order ord[0], ord[1], ... fixed before the search; index
ord[d] is sent to an unused grid point.  Symmetry rules (S1, S2) both coordinate sequences
s1(d) = sigma_1(ord[d]) and s2(d) = sigma_2(ord[d]) are restricted growth strings; (S3) when m = n,
s1 <_lex s2.  Pruning rules on a partial assignment (all necessary; proofs in the report):
  (N1) R-support: no known zero R[r][c] with a known nonzero in row r and a known nonzero in column c;
  (N2) R-cycles: the known nonzero entries of R admit x, y with x_r y_c = R[r][c]
       (decided by a weighted union-find on rows and columns of R; images mod PR, see below);
  (N4) partner rule: if row r and column c of R each hold a known nonzero, R[r][c] != 0 in every
       completion; so when one grid point of that entry holds an index i with no unassigned partner j
       (M[i][j] != 0 for the left point, M[j][i] != 0 for the right point), the other point is assigned;
  (N3) W-COL family: for every product-form function f of the left index i (each column j of M, each
       row j of M, the diagonal, and the row/column power sums of order 0, 1, 2), the grid matrix
       F(a, b) = f(sigma^{-1}(a, b)) on the assigned points has every 2x2 minor zero (exact) and
       a product support (no assigned zero with a nonzero in its grid row and in its grid column).
Leaf rule: at a complete assignment PC is applied to every target in exact integer arithmetic; only the
leaf rule accepts.  N2 is evaluated on images in F_PR (PR = 2^61 - 1), which is sound: entries are
integers of absolute value < PR, every weight is a ratio of nonzero entries, reduction mod PR is a ring
homomorphism on the rationals prime to PR, so an inequality of images certifies an exact inequality; an
exact equality is never pruned.  arith="exact" runs N2 with Fractions instead (cross-check).
"""
from fractions import Fraction

PR = (1 << 61) - 1
MASK64 = (1 << 64) - 1


class SM64:
    """SplitMix64 (integer only)."""

    def __init__(self, seed):
        self.s = seed & MASK64

    def next(self):
        self.s = (self.s + 0x9E3779B97F4A7C15) & MASK64
        z = self.s
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK64
        return z ^ (z >> 31)

    def below(self, k):
        lim = (1 << 64) - ((1 << 64) % k)
        while True:
            x = self.next()
            if x < lim:
                return x % k

    def shuffle(self, xs):
        xs = list(xs)
        for i in range(len(xs) - 1, 0, -1):
            j = self.below(i + 1)
            xs[i], xs[j] = xs[j], xs[i]
        return xs


class Stop(Exception):
    pass


class BudgetOut(Exception):
    pass


MUTATIONS = ("MUT-INDEX", "MUT-SUPPORT-STRONG", "MUT-LEX-ALWAYS", "MUT-NOLEX", "MUT-SECOND", "MUT-LEAF")


class Engine:
    def __init__(self, mats, m, n, rules="RWVP", order="greedy", arith="modp", mut=None):
        assert mut is None or mut in MUTATIONS
        self.mats = [[[int(x) for x in row] for row in M] for M in mats]
        N = m * n
        for M in self.mats:
            assert len(M) == N and all(len(r) == N for r in M)
        self.m, self.n, self.N, self.K = m, n, N, len(mats)
        self.square = m == n
        self.rules, self.arith, self.mut = rules, arith, mut
        self.modp = arith == "modp"
        self.order = self._order(order)
        # W-COL family profiles: product-form functions of the left index
        prof = [[] for _ in range(N)]
        for M in self.mats:
            for i in range(N):
                part = []
                if "W" in rules:
                    part += [M[i][j] for j in range(N)] + [M[j][i] for j in range(N)]
                if "V" in rules:
                    row = M[i]
                    col = [M[j][i] for j in range(N)]
                    part += [M[i][i], sum(1 for x in row if x), sum(row), sum(x * x for x in row),
                             sum(1 for x in col if x), sum(col), sum(x * x for x in col)]
                prof[i] += part
        self.L = len(prof[0])
        self.FULL = (1 << self.L) - 1
        self.NZP = [sum(1 << c for c, x in enumerate(prof[i]) if x) for i in range(N)]
        self.PV = [[tuple(x * y for x, y in zip(prof[i], prof[j])) for j in range(N)] for i in range(N)]
        self.NZr = [[sum(1 << j for j in range(N) if M[i][j]) for i in range(N)] for M in self.mats]
        self.NZc = [[sum(1 << j for j in range(N) if M[j][i]) for i in range(N)] for M in self.mats]
        self.rowmask = [sum(1 << (a * n + b) for b in range(n)) for a in range(m)]
        self.colmask = [sum(1 << (a * n + b) for a in range(m)) for b in range(n)]
        if self.modp:
            self.img = [[[x % PR for x in row] for row in M] for M in self.mats]
            # soundness precondition of N2 on images: no exactly nonzero entry has image 0
            assert all((x == 0) == (y == 0) for M, I in zip(self.mats, self.img)
                       for r, s in zip(M, I) for x, y in zip(r, s)), "an entry vanishes mod PR"
        else:
            self.img = [[[Fraction(x) for x in row] for row in M] for M in self.mats]
        self.reset()

    # ------------------------------------------------------------ static order
    def _order(self, how):
        N = self.N
        if how == "nat":
            return list(range(N))
        if isinstance(how, (list, tuple)):
            assert sorted(how) == list(range(N))
            return list(how)
        assert how in ("rare", "greedy")
        sig = []
        for i in range(N):
            s = []
            for M in self.mats:
                s.append((tuple(sorted(M[i])), tuple(sorted(M[j][i] for j in range(N))), M[i][i]))
            sig.append(tuple(s))
        freq = {}
        for s in sig:
            freq[s] = freq.get(s, 0) + 1
        if how == "rare":
            return sorted(range(N), key=lambda i: (freq[sig[i]], i))
        # greedy: rarest index first, then repeatedly the index with the most nonzero links
        # (M[i][j] or M[j][i] != 0 in some target) to the indices already ordered; ties by rarity, index
        link = [[any(M[i][j] or M[j][i] for M in self.mats) and i != j for j in range(N)] for i in range(N)]
        order = [min(range(N), key=lambda i: (freq[sig[i]], i))]
        rest = set(range(N)) - set(order)
        while rest:
            nxt = min(rest, key=lambda i: (-sum(1 for j in order if link[i][j]), freq[sig[i]], i))
            order.append(nxt)
            rest.discard(nxt)
        return order

    # ------------------------------------------------------------ state
    def reset(self):
        m, n, N = self.m, self.n, self.N
        self.pos = [-1] * N
        self.occ = [-1] * N
        self.rowpts = [[] for _ in range(m)]
        self.colpts = [[] for _ in range(n)]
        self.GR = [0] * m
        self.GC = [0] * n
        self.assigned = []
        self.UA = (1 << N) - 1          # unassigned indices
        self.AP = 0                     # assigned grid points
        self.rows_used = self.cols_used = 0
        self.eq = True
        nodes = m * m + n * n
        one = 1 if self.modp else Fraction(1)
        self.comp = [list(range(nodes)) for _ in range(self.K)]
        self.w = [[one] * nodes for _ in range(self.K)]
        self.mem = [[[u] for u in range(nodes)] for _ in range(self.K)]
        self.KZr = [[0] * (m * m) for _ in range(self.K)]
        self.KZc = [[0] * (n * n) for _ in range(self.K)]
        self.NZR = [0] * self.K
        self.NZC = [0] * self.K
        self.U = []
        self.tested = self.accepted = self.leaves = 0
        self.found = []

    def undo(self, mark):
        U = self.U
        while len(U) > mark:
            rec = U.pop()
            t = rec[0]
            if t == 0:
                _, g, i, a, b, gr, gc = rec
                self.occ[g] = -1
                self.pos[i] = -1
                self.rowpts[a].pop()
                self.colpts[b].pop()
                self.GR[a], self.GC[b] = gr, gc
                self.UA |= 1 << i
                self.AP &= ~(1 << g)
            elif t == 1:
                _, k, r, c, kzr, kzc = rec
                self.KZr[k][r], self.KZc[k][c] = kzr, kzc
            elif t == 2:
                _, k, nzr, nzc = rec
                self.NZR[k], self.NZC[k] = nzr, nzc
            else:
                _, k, croot, keep, oldlen, moved = rec
                comp, w = self.comp[k], self.w[k]
                for x, wx in moved:
                    comp[x] = croot
                    w[x] = wx
                del self.mem[k][keep][oldlen:]

    # ------------------------------------------------------------ one placement with all pruning rules
    def place(self, i, a, b):
        n, m = self.n, self.m
        g = a * n + b
        occ = self.occ
        rowpts, colpts = self.rowpts[a], self.colpts[b]
        an = a * n
        if self.L:
            PV = self.PV
            PVi = PV[i]
            for g2 in rowpts:
                b2 = g2 - an
                PVi2 = PV[occ[g2]]
                for g3 in colpts:
                    i4 = occ[g3 - b + b2]
                    if i4 >= 0 and PVi[i4] != PVi2[occ[g3]]:
                        return False
            FULL, NZP, GR, GC = self.FULL, self.NZP, self.GR, self.GC
            nzi = NZP[i]
            GRa = GR[a] | nzi
            GCb = GC[b] | nzi
            if (FULL ^ nzi) & GRa & GCb:
                return False
            for g2 in rowpts:
                if (FULL ^ NZP[occ[g2]]) & GRa & GC[g2 - an]:
                    return False
            for g3 in colpts:
                if (FULL ^ NZP[occ[g3]]) & GR[(g3 - b) // n] & GCb:
                    return False
        else:
            GRa = GCb = 0
        U = self.U
        mark = len(U)
        U.append((0, g, i, a, b, self.GR[a], self.GC[b]))
        occ[g] = i
        self.pos[i] = g
        rowpts.append(g)
        colpts.append(g)
        self.GR[a], self.GC[b] = GRa, GCb
        self.UA &= ~(1 << i)
        self.AP |= 1 << g
        if "R" in self.rules:
            for k in range(self.K):
                if not self._r_add(k, i, a, b):
                    self.undo(mark)
                    return False
            if "P" in self.rules:
                for k in range(self.K):
                    if not self._partner(k, i):
                        self.undo(mark)
                        return False
        return True

    def _partner(self, k, i):
        """N4 over every assigned index (the masks change with each placement)."""
        m, n = self.m, self.n
        NZR, NZC = self.NZR[k], self.NZC[k]
        rowmask, colmask = self.rowmask, self.colmask
        free = ~self.AP
        UA = self.UA
        # left point (a, b): partners at (a', b') with (a, a') in NZR, (b, b') in NZC
        LA = [0] * m
        RA = [0] * m
        for a in range(m):
            for a2 in range(m):
                if (NZR >> (a * m + a2)) & 1:
                    LA[a] |= rowmask[a2]
                    RA[a2] |= rowmask[a]
        LB = [0] * n
        RB = [0] * n
        for b in range(n):
            for b2 in range(n):
                if (NZC >> (b * n + b2)) & 1:
                    LB[b] |= colmask[b2]
                    RB[b2] |= colmask[b]
        NZr, NZc, pos = self.NZr[k], self.NZc[k], self.pos
        for j in self.assigned + [i]:
            a, b = divmod(pos[j], n)
            if not (NZr[j] & UA) and LA[a] & LB[b] & free:
                return False
            if not (NZc[j] & UA) and RA[a] & RB[b] & free:
                return False
        return True

    def _r_add(self, k, i, a, b):
        m, n = self.m, self.n
        m2 = m * m
        Mi = self.img[k][i]
        Mz = self.mats[k]
        Mzi = Mz[i]
        imgk = self.img[k]
        ents = [(a * m + a, b * n + b, Mzi[i], Mi[i])]
        mutidx = self.mut == "MUT-INDEX"
        for j in self.assigned:
            pj = self.pos[j]
            a2, b2 = divmod(pj, n)
            if mutidx:
                ents.append((a * m + a2, b2 * n + b, Mzi[j], Mi[j]))
                ents.append((a2 * m + a, b * n + b2, Mz[j][i], imgk[j][i]))
            else:
                ents.append((a * m + a2, b * n + b2, Mzi[j], Mi[j]))
                ents.append((a2 * m + a, b2 * n + b, Mz[j][i], imgk[j][i]))
        U = self.U
        KZr, KZc = self.KZr[k], self.KZc[k]
        strong = self.mut == "MUT-SUPPORT-STRONG"
        for r, c, z, v in ents:
            NZR, NZC = self.NZR[k], self.NZC[k]
            if z == 0:
                if (NZR >> r) & 1 and (NZC >> c) & 1:
                    return False
                if strong and (NZR >> r) & 1:
                    return False
                U.append((1, k, r, c, KZr[r], KZc[c]))
                KZr[r] |= 1 << c
                KZc[c] |= 1 << r
            else:
                U.append((2, k, NZR, NZC))
                NZR |= 1 << r
                NZC |= 1 << c
                self.NZR[k], self.NZC[k] = NZR, NZC
                if KZr[r] & NZC or KZc[c] & NZR:
                    return False
                if strong and KZr[r]:
                    return False
                if not self._union(k, r, m2 + c, v):
                    return False
        return True

    def _union(self, k, u, v, val):
        """Constraint z_u = val * z_v; weights w[x] = z_x / z_root(x)."""
        comp, w, mem = self.comp[k], self.w[k], self.mem[k]
        cu, cv = comp[u], comp[v]
        if self.modp:
            if cu == cv:
                return (w[u] - val * w[v]) % PR == 0
            if len(mem[cu]) <= len(mem[cv]):
                f = val * w[v] % PR * pow(w[u], PR - 2, PR) % PR
                src, dst = cu, cv
            else:
                f = w[u] * pow(val * w[v] % PR, PR - 2, PR) % PR
                src, dst = cv, cu
            moved = [(x, w[x]) for x in mem[src]]
            self.U.append((3, k, src, dst, len(mem[dst]), moved))
            for x, wx in moved:
                comp[x] = dst
                w[x] = wx * f % PR
            mem[dst].extend(mem[src])
            return True
        if cu == cv:
            return w[u] == val * w[v]
        if len(mem[cu]) <= len(mem[cv]):
            f = val * w[v] / w[u]
            src, dst = cu, cv
        else:
            f = w[u] / (val * w[v])
            src, dst = cv, cu
        moved = [(x, w[x]) for x in mem[src]]
        self.U.append((3, k, src, dst, len(mem[dst]), moved))
        for x, wx in moved:
            comp[x] = dst
            w[x] = wx * f
        mem[dst].extend(mem[src])
        return True

    # ------------------------------------------------------------ the exact leaf rule (PC)
    def leaf_ok(self):
        m, n = self.m, self.n
        occ = self.occ
        for M in self.mats:
            R = [[M[occ[a * n + b]][occ[a2 * n + b2]] for b in range(n) for b2 in range(n)]
                 for a in range(m) for a2 in range(m)]
            piv = None
            for r, row in enumerate(R):
                for c, x in enumerate(row):
                    if x:
                        piv = (r, c)
                        break
                if piv:
                    break
            if piv is None:
                continue
            p, q = piv
            Rp, rpq = R[p], R[p][q]
            for row in R:
                rq = row[q]
                for c, x in enumerate(row):
                    if rpq * x != rq * Rp[c]:
                        return False
        return True

    # ------------------------------------------------------------ depth-first search
    def candidates(self, d):
        m, n = self.m, self.n
        ru, cu, eq = self.rows_used, self.cols_used, self.eq
        mut = self.mut
        occ = self.occ
        out = []
        for a in range(min(ru + 1, m)):
            for b in range(min(cu + 1, n)):
                if occ[a * n + b] >= 0:
                    continue
                if self.square:
                    if mut == "MUT-LEX-ALWAYS":
                        if a > b:
                            continue
                    elif mut != "MUT-NOLEX" and eq and a > b:
                        continue
                if mut == "MUT-SECOND" and d == 1 and (a, b) != (0, 1):
                    continue
                out.append((a, b))
        return out

    def _commit_state(self, a, b):
        saved = (self.rows_used, self.cols_used, self.eq)
        if a == self.rows_used:
            self.rows_used += 1
        if b == self.cols_used:
            self.cols_used += 1
        if self.eq and a < b:
            self.eq = False
        return saved

    def _dfs(self, d):
        if d == self.N:
            self.leaves += 1
            if self.mut == "MUT-LEAF" or self.leaf_ok():
                self.found.append(tuple(self.pos))
                if self.mode == "exist":
                    raise Stop
            return
        i = self.order[d]
        for a, b in self.candidates(d):
            self.tested += 1
            if self.tested > self.budget:
                raise BudgetOut
            mark = len(self.U)
            if self.place(i, a, b):
                self.accepted += 1
                saved = self._commit_state(a, b)
                self.assigned.append(i)
                self._dfs(d + 1)
                self.assigned.pop()
                self.rows_used, self.cols_used, self.eq = saved
                self.undo(mark)

    def run(self, mode="exist", budget=10 ** 8):
        """mode 'exist' stops at the first accepted leaf; 'all' returns every class.  Status is
        FOUND / NONE (complete, no class) / ALL (complete enumeration) / EXHAUSTED (budget)."""
        self.reset()
        self.mode, self.budget = mode, budget
        try:
            self._dfs(0)
            status = "ALL" if mode == "all" else "NONE"
        except Stop:
            status = "FOUND"
        except BudgetOut:
            status = "EXHAUSTED"
        if mode == "exist" and status == "NONE" and self.found:
            status = "FOUND"
        return status, list(self.found), (self.tested, self.accepted, self.leaves)

    # ------------------------------------------------------------ Knuth's unbiased tree-size estimator
    def knuth(self, probes, seed):
        """Mean over seeded random root-to-leaf probes of (accepted-node estimate, tested-node estimate),
        as exact Fractions.  Design evidence only."""
        rng = SM64(seed)
        tot_acc, tot_tst = Fraction(0), Fraction(0)
        for _ in range(probes):
            self.reset()
            self.mode, self.budget = "exist", 10 ** 30
            weight, est_acc, est_tst = 1, 1, 0
            for d in range(self.N):
                i = self.order[d]
                cand = self.candidates(d)
                ok = []
                for a, b in cand:
                    mark = len(self.U)
                    if self.place(i, a, b):
                        ok.append((a, b))
                        self.undo(mark)
                est_tst += weight * len(cand)
                if not ok:
                    break
                weight *= len(ok)
                est_acc += weight
                a, b = ok[rng.below(len(ok))]
                self.place(i, a, b)
                self._commit_state(a, b)
                self.assigned.append(i)
            tot_acc += est_acc
            tot_tst += est_tst
        self.reset()
        return tot_acc / probes, tot_tst / probes


# ---------------------------------------------------------------- helpers shared by the suites

def kron(A, B):
    m, n = len(A), len(B)
    return [[A[a][a2] * B[b][b2] for a2 in range(m) for b2 in range(n)] for a in range(m) for b in range(n)]


def relabel(K, sig):
    """M with M^sig = K, i.e. M[i][j] = K[sig[i]][sig[j]] (sig[i] = grid index a n + b)."""
    N = len(K)
    return [[K[sig[i]][sig[j]] for j in range(N)] for i in range(N)]


def canonical(sig, m, n, order):
    """Canonical representative (S1-S3) of the class of sig, w.r.t. the static order."""
    def rgs(seq):
        lab = {}
        out = []
        for x in seq:
            if x not in lab:
                lab[x] = len(lab)
            out.append(lab[x])
        return out
    s1 = rgs([sig[i] // n for i in order])
    s2 = rgs([sig[i] % n for i in order])
    if m == n and s2 < s1:
        s1, s2 = s2, s1
    res = [0] * len(sig)
    for d, i in enumerate(order):
        res[i] = s1[d] * n + s2[d]
    return tuple(res)
