"""Exact sweeps of the embedded classes P^emb(m) (PLAN.md §3): the aggregated transfer computation.

For every observer o and generator phi, C_K[o, v, x] counts the prior seeds with (v_K, x_K) = (v, x)
after K rounds. Under Q_p the visible outputs are fresh fair bits, so v_K is driven by i.i.d. fair
bits and x_K is fair and independent: Q[(v_K, x_K) = (v, x)] = q_K(v)/2, with q_K computed exactly
as integers Q_K = 2^K q_K per (rho_0, rho_1) pair (the policy a never enters Q_p).

Exactness. With den = 2^(K+1) and Z_v = Q_K(v) M, the cell difference times M is
C - Z_v/den = C - beta_v - r_v/den (beta_v = Z_v // den, r_v = Z_v % den). Every advantage is an
integer plus an integer combination of the fractions r/den; maxima are found by integer bounds and
decided by exact Python-int evaluation of the remaining candidates. No float is used.
"""
from fractions import Fraction

import numpy as np

W = 3            # window parameter w of §6 (4 steps K-3..K)
READINGS = ("abs", "signed")   # the two readings of condition (d) (open item D-SIGN)
DELTA_CX_NUM, DELTA_CX_DEN = 1, 8


def subset_sums_last(a):
    """a (..., V) -> (..., 2^V): out[..., S] = sum_{v in S} a[..., v]."""
    out = np.zeros(a.shape[:-1] + (1,), dtype=np.int64)
    for v in range(a.shape[-1]):
        out = np.concatenate([out, out + a[..., v:v + 1]], axis=-1)
    return out


def det_core(A, bet, half, rz):
    """Per test (o, F): |Delta_phi| M = |A_phi - beta - rho| with rho = r/den in [0, 1) common to all
    phi. Returns (first, I, base, cv):
      worst  min_phi |.| = I + tau/den, tau = r if first else (0 if rz else den - r);
      average sum_phi |.| = base + cv * rho.
    half = (2 r > den), rz = (r == 0). A: (..., F); bet, half, rz: (...)."""
    small = A.dtype == np.int16
    big = np.int16(1 << 14) if small else np.int64(1 << 40)
    b3 = bet[..., None].astype(A.dtype)
    le = A <= b3
    maxle = np.where(le, A, -big).max(axis=-1).astype(np.int64)
    mingt = np.where(le, big, A).min(axis=-1).astype(np.int64)
    hasle = maxle > -int(big)
    hasgt = mingt < int(big)
    a = bet - maxle                 # a + rho for the closest A_phi <= beta
    b = mingt - bet - 1             # b + 1 - rho for the closest A_phi > beta
    t = b - a + 1                   # a + rho <= b + 1 - rho  iff  2 rho <= t
    first = hasle & (~hasgt | (t >= 2) | ((t == 1) & ~half))
    I = np.where(first, a, b + (rz & ~first))
    D = A - b3
    Itot = np.where(le, -D, D - 1).sum(axis=-1, dtype=np.int64)
    na = le.sum(axis=-1, dtype=np.int64)
    nb = A.shape[-1] - na
    return first, I, Itot + nb, na - nb


class QChain:
    """Q_K(v) = 2^K q_K(v) for each pair (rho_0, rho_1), as Python ints in an object array."""

    def __init__(self, pairs):
        P, _, V = pairs.shape
        self.P, self.V = P, V
        inv = np.zeros_like(pairs)
        for x in (0, 1):
            inv[np.arange(P)[:, None], x, pairs[:, x, :]] = np.arange(V)[None, :]
        self.inv = inv
        Q = np.empty((P, V), dtype=object)
        Q[:, :] = 0
        Q[:, 0] = 1
        self.Q = Q
        self.K = 0

    def advance(self):
        ar = np.arange(self.P)[:, None]
        self.Q = self.Q[ar, self.inv[:, 0, :]] + self.Q[ar, self.inv[:, 1, :]]
        self.K += 1

    def split(self, M):
        """(beta int64 (P, V), rem object (P, V), den) for the cell offsets M q_K(v)/2 = Z/den."""
        den = 1 << (self.K + 1)
        Z = self.Q * M
        beta = (Z // den).astype(np.int64)
        rem = Z % den
        return beta, rem, den


def check_q_sums(Q, K):
    """EX2 for Q_p: sum_v q_K(v) = 1 exactly."""
    s = Q.sum(axis=1)
    return all(int(x) == (1 << K) for x in s.tolist())


# ------------------------------------------------------------------ exact maxima

def tv_numerators(C, beta, rem_rows, den):
    """For each observer: exact numerator of 2 M den TV(P_(v,x), Q_(v,x)) as Python int is
    I*den + sum_v c_v r_v. Returns (I, c) integer arrays; rem_rows (n, V) object."""
    b = beta[:, :, None]
    gt = C > b
    I = np.where(gt, C - b, b - C).sum(axis=(1, 2))
    c = (~gt).sum(axis=2) - gt.sum(axis=2)
    return I, c


def _obj_argmax(vals):
    """First index of the maximum of a 1-d object array of Python ints."""
    best = None
    arg = None
    for i, v in enumerate(vals.tolist()):
        if best is None or v > best:
            best, arg = v, i
    return best, arg


def exact_max(I, c, rem_rows, den):
    """max over rows of I*den + sum_v c_v r_v (each r_v/den in [0, 1)); returns (num, row) with the
    smallest row index among maximisers. Integer bounds prune; the rest is exact Python ints."""
    lb = I + np.minimum(c, 0).sum(axis=1)
    ub = I + np.maximum(c, 0).sum(axis=1)
    L = int(lb.max())
    cand = np.flatnonzero(ub >= L)
    cr = c[cand]
    rr = rem_rows[cand]
    if not cr.any() or all(int(r) == 0 for r in rr[cr != 0].tolist()):
        j = int(np.argmax(I[cand]))
        return int(I[cand][j]) * den, int(cand[j])
    vals = I[cand].astype(object) * den + (cr.astype(object) * rr).sum(axis=1)
    best, j = _obj_argmax(vals)
    return int(best), int(cand[j])


# ------------------------------------------------------------------ simulation

class Sim:
    """Joint simulation of one observer chunk against several generators."""

    def __init__(self, obs, idx, gens, kcaps):
        self.obs = obs
        self.idx = idx
        self.R = obs.R[idx]                  # (c, 2, V)
        self.A = obs.Aact[idx]               # (c, V)
        self.passive = bool((self.A == 0).all())
        self.V = obs.V
        self.gens = gens
        self.kcaps = kcaps
        self.K = 0
        c = len(idx)
        self.c = c
        self.Rflat = self.R.reshape(-1)
        self.base = (np.arange(c, dtype=np.int64) * (2 * self.V))[:, None]
        self.st = []
        for g, kc in zip(gens, kcaps):
            S = len(g.seed_x)
            v = np.zeros((c, S), dtype=np.int64)
            x = np.broadcast_to(g.seed_x.astype(np.int64)[None, :], (c, S)).copy()
            if self.passive:
                self.st.append({"v": v, "X": g.records(kc).astype(np.int64)})
            else:
                h = np.broadcast_to(g.seed_h[None, :], (c, S)).copy()
                self.st.append({"v": v, "x": x, "h": h})

    def counts(self, gi):
        st = self.st[gi]
        if self.passive:
            x = np.broadcast_to(st["X"][:, self.K][None, :], st["v"].shape)
        else:
            x = st["x"]
        key = (np.arange(self.c, dtype=np.int64)[:, None] * (2 * self.V) + st["v"] * 2 + x).reshape(-1)
        C = np.bincount(key, minlength=self.c * 2 * self.V).reshape(self.c, self.V, 2)
        return C

    def step(self):
        for gi, (g, st) in enumerate(zip(self.gens, self.st)):
            if self.K >= self.kcaps[gi]:
                continue
            if self.passive:
                xt = st["X"][:, self.K][None, :]
                st["v"] = self.Rflat[self.base + xt * self.V + st["v"]]
            else:
                v = self.Rflat[self.base + st["x"] * self.V + st["v"]]
                cc = st["x"] ^ self.A[np.arange(self.c)[:, None], v]
                h = g.sig[cc, st["h"]]
                st["x"] = cc ^ g.f[h]
                st["h"] = h
                st["v"] = v
        self.K += 1


# ------------------------------------------------------------------ the sweep

class Sweep:
    """One pass over an observer set against a list of generators of one degree n.

    gens: list of Gen; kcap1[gi]: K range for the per-generator K1 curves; fam: indices of the K0
    family; primaries: indices whose prediction windows are tracked as candidate witnesses;
    k0cap: K range for K0; k0_kind: 'det' (tests (rho, a, F), all F; m <= 2) or 'pred' (prediction
    tests chi over chi_masks); subclasses: {name: boolean mask over observers}.
    """

    def __init__(self, obs, gens, kcap1, fam, primaries, k0cap, k0_kind, subclasses,
                 chi_k0=None, window_cap=None, lp_cap=-1, chunk=None, im3=None):
        self.obs = obs
        self.gens = gens
        self.kcap1 = kcap1
        self.fam = fam
        self.primaries = primaries
        self.k0cap = k0cap
        self.k0_kind = k0_kind
        self.sub = subclasses
        self.V = obs.V
        self.chi_k0 = chi_k0
        self.window_cap = window_cap if window_cap is not None else {g: kcap1[g] for g in primaries}
        self.lp_cap = lp_cap
        self.chunk = chunk or obs.n
        self.im3 = im3
        M = gens[0].M
        for g in gens:
            assert g.M == M and (g.seed_w == 1).all()
        self.M = M
        V = self.V
        cells = 2 * V
        # F masks (det K0): all subsets of the 2V cells, cell index v*2 + x
        if k0_kind == "det":
            nF = 1 << cells
            Fm = ((np.arange(nF)[None, :] >> np.arange(cells)[:, None]) & 1).astype(np.int64)  # (cells, nF)
            self.Fm = Fm
            kv = Fm.reshape(V, 2, nF).sum(axis=1)  # (V, nF) in {0,1,2}
            self.kid = (kv * (3 ** np.arange(V))[:, None]).sum(axis=0)  # (nF,)
            self.kmat = np.array([[(k // 3 ** v) % 3 for v in range(V)] for k in range(3 ** V)], dtype=np.int64)
        # results
        self.k1d = {(s, gi): {} for s in subclasses for gi in range(len(gens))}
        self.k1p = {(s, gi): {} for s in subclasses for gi in range(len(gens))}
        self.k0w = {s: {} for s in subclasses}
        self.k0a = {s: {} for s in subclasses}
        self.win = {(rd, s, gi): {} for rd in READINGS for s in subclasses for gi in primaries}
        self.lpdata = {}
        self.ex2_q = True
        self.im3_ok = True
        self.im3_fail = []

    # -- K1 merges: keep (num, global obs) with num exact over a K-dependent common denominator
    @staticmethod
    def _merge(store, K, num, arg):
        cur = store.get(K)
        if cur is None or num > cur[0]:
            store[K] = (num, arg)

    def run(self):
        obs = self.obs
        n = obs.n
        for start in range(0, n, self.chunk):
            idx = np.arange(start, min(n, start + self.chunk))
            self._run_chunk(idx)
        return self

    def _run_chunk(self, idx):
        obs = self.obs
        V = self.V
        M = self.M
        gens = self.gens
        kmax = max(max(self.kcap1), self.k0cap if self.k0cap is not None else -1)
        k0c = self.k0cap if self.k0cap is not None else -1
        kcaps = [max(self.kcap1[gi], k0c if gi in self.fam else -1) for gi in range(len(gens))]
        sim = Sim(obs, idx, gens, kcaps)
        pairs_local, pinv = np.unique(obs.pair[idx], return_inverse=True)
        pinv = pinv.reshape(-1)
        ptab = obs.R[idx][np.unique(pinv, return_index=True)[1]]
        q = QChain(ptab)
        submask = {s: m[idx] for s, m in self.sub.items()}
        nchi = 1 << V
        track = (set(self.primaries) | set(self.fam)) if self.primaries else set()
        runs = {(rd, gi): np.zeros((len(idx), nchi), dtype=np.int16) for gi in track for rd in READINGS}
        im3 = self.im3(obs, idx, gens) if self.im3 is not None else None
        for K in range(kmax + 1):
            beta_p, rem_p, den = q.split(M)
            if not check_q_sums(q.Q, K):
                self.ex2_q = False
            beta = beta_p[pinv]
            Cs = {}
            for gi in range(len(gens)):
                if K <= kcaps[gi]:
                    Cs[gi] = sim.counts(gi)
            if im3 is not None:
                ok, why = im3.compare(K, Cs)
                if not ok:
                    self.im3_ok = False
                    self.im3_fail.append((K, why))
            # K1 distinguishing (optimal F) and prediction (best chi)
            for gi, C in Cs.items():
                if K > self.kcap1[gi]:
                    continue
                I, c = tv_numerators(C, beta, None, den)
                pred = C.max(axis=2).sum(axis=1)          # sum_v max_x C
                for s, msk in submask.items():
                    rows = np.flatnonzero(msk)
                    if rows.size == 0:
                        continue
                    num, a = exact_max(I[rows], c[rows], rem_p[pinv[rows]], den)
                    self._merge(self.k1d[(s, gi)], K, num, int(idx[rows[a]]))
                    j = int(np.argmax(pred[rows]))
                    self._merge(self.k1p[(s, gi)], K, int(pred[rows][j]), int(idx[rows[j]]))
            # prediction windows: the same O and chi at every K' in K-3..K, under both readings of (d):
            # 'abs'    |Pr[chi = X_K'] - 1/2| >= 1/8, i.e. 4 |2S - M| >= M   (S = sum_v C[v, chi(v)])
            # 'signed' Pr[chi = X_K'] - 1/2 >= 1/8,   i.e. 4 (2S - M) >= M
            for gi in track:
                if gi not in Cs:
                    continue
                C = Cs[gi]
                base = C[:, :, 0].sum(axis=1).astype(np.int16)[:, None]
                ss = subset_sums_small(C[:, :, 1] - C[:, :, 0]) + base
                d2 = 2 * ss.astype(np.int32) - M
                for rd, ok in (("abs", 4 * np.abs(d2) >= M), ("signed", 4 * d2 >= M)):
                    r = runs[(rd, gi)]
                    r += 1
                    r[~ok] = 0
            for gi in self.primaries:
                if gi not in Cs or K < W or K > self.window_cap[gi]:
                    continue
                same = [f for f in self.fam if gens[f].family == gens[gi].family]
                famg = [f for f in same if f in Cs]
                for rd in READINGS:
                    wg = runs[(rd, gi)] >= W + 1
                    famw = None
                    if famg and len(famg) == len(same):
                        famw = np.ones_like(wg)
                        for f in famg:
                            famw &= runs[(rd, f)] >= W + 1
                    for s, msk in submask.items():
                        w2 = wg & msk[:, None]
                        cnt = int(w2.sum())
                        rec = self.win[(rd, s, gi)].setdefault(K, {"count": 0, "first": None, "count_family": 0,
                                                                   "first_family": None,
                                                                   "family_checked": famw is not None,
                                                                   "count_member": [0] * len(famg)})
                        for j, f in enumerate(famg):
                            rec["count_member"][j] += int(((runs[(rd, f)] >= W + 1) & msk[:, None]).sum())
                        if not cnt:
                            continue
                        rec["count"] += cnt
                        if rec["first"] is None:
                            o, ch = np.unravel_index(int(np.argmax(w2.reshape(-1))), w2.shape)
                            rec["first"] = (int(idx[o]), int(ch))
                        if famw is not None:
                            wf = w2 & famw
                            cf = int(wf.sum())
                            rec["count_family"] += cf
                            if cf and rec["first_family"] is None:
                                o, ch = np.unravel_index(int(np.argmax(wf.reshape(-1))), wf.shape)
                                rec["first_family"] = (int(idx[o]), int(ch))
            # K0
            if self.k0cap is not None and K <= self.k0cap and all(f in Cs for f in self.fam):
                if self.k0_kind == "det":
                    self._k0_det(K, idx, [Cs[f] for f in self.fam], q, pinv, submask, den)
                else:
                    self._k0_pred(K, idx, [Cs[f] for f in self.fam], submask)
            if K <= self.lp_cap:
                self.lpdata.setdefault(K, []).append((idx, [Cs[f].copy() for f in self.fam]))
            if K < kmax:
                sim.step()
                q.advance()
                if im3 is not None:
                    im3.step()

    def _k0_det(self, K, idx, Cf, q, pinv, submask, den):
        """K0 over tests (o, F), all F: worst max min_phi |Delta_phi| and average max mean_phi."""
        M = self.M
        nF = self.Fm.shape[1]
        # group offsets G = sum_v k_v Z_v for (pair, kvec)
        Z = q.Q * M
        G = Z.dot(self.kmat.T)                      # (P, 3^V) object
        bg = (G // den).astype(np.int64)
        rg = G % den
        Fl = len(Cf)
        # A_phi(F) = sum of C over the cells of F, by subset sums (F bit c = cell c = v*2 + x)
        A = np.stack([subset_sums_last(C.reshape(len(idx), -1)) for C in Cf], axis=2)
        A = A.astype(np.int16) if M < (1 << 13) else A          # (c, nF, F)
        bet = bg[pinv][:, self.kid]                                              # (c, nF)
        gp = pinv[:, None]                                                       # rr[o, f] = rg[gp[o], kid[f]]
        flat_r = [int(r) for r in rg.reshape(-1).tolist()]
        half = np.array([2 * r > den for r in flat_r], dtype=bool).reshape(rg.shape)[pinv][:, self.kid]
        rz = np.array([r == 0 for r in flat_r], dtype=bool).reshape(rg.shape)[pinv][:, self.kid]
        first, I, base, cv = det_core(A, bet, half, rz)
        rvals = sorted(set(flat_r) | {den - r for r in flat_r if r} | {0})
        rank = {v: i for i, v in enumerate(rvals)}
        rk_r = np.array([rank[r] for r in flat_r], dtype=np.int64).reshape(rg.shape)[pinv][:, self.kid]
        rk_m = np.array([rank[den - r] if r else rank[0] for r in flat_r], dtype=np.int64).reshape(rg.shape)[pinv][:, self.kid]
        rkey = np.where(first, rk_r, rk_m)
        NR = len(rvals) + 1
        key = I * NR + rkey
        lbA = base + np.minimum(cv, 0)
        ubA = base + np.maximum(cv, 0)
        for s, msk in submask.items():
            rows = np.flatnonzero(msk)
            if rows.size == 0:
                continue
            ks = key[rows]
            o, f = np.unravel_index(int(np.argmax(ks)), ks.shape)
            gi_o = rows[o]
            r_of = int(rg[pinv[gi_o], self.kid[f]])
            tnum = r_of if first[gi_o, f] else (0 if rz[gi_o, f] else den - r_of)
            num = int(I[gi_o, f]) * den + tnum
            cur = self.k0w[s].get(K)
            if cur is None or num > cur[0]:
                self.k0w[s][K] = (num, int(idx[gi_o]), int(f), den)
            L = int(lbA[rows].max())
            co, cf = np.nonzero(ubA[rows] >= L)
            r0 = rows[co]
            vals = base[r0, cf].astype(object) * den + cv[r0, cf].astype(object) * rg[pinv[r0], self.kid[cf]]
            best, j = _obj_argmax(vals)
            barg = (int(idx[r0[j]]), int(cf[j]))
            cur = self.k0a[s].get(K)
            if cur is None or best > cur[0]:
                self.k0a[s][K] = (best, barg[0], barg[1], den)

    def _k0_pred(self, K, idx, Cf, submask):
        """K0 over prediction tests chi in chi_k0: worst max min_phi |2 S - M| and average max sum_phi,
        with S = sum_v C[v, chi(v)] (integers; |2 S - M| <= M < 2^15)."""
        M = self.M
        assert M < (1 << 14)
        mn = None
        sm = None
        for C in Cf:
            base = C[:, :, 0].sum(axis=1).astype(np.int16)[:, None]
            ss = subset_sums_small(C[:, :, 1] - C[:, :, 0]) + base
            if self.chi_k0 is not None:
                ss = ss[:, self.chi_k0]
            v = np.abs(2 * ss - np.int16(M))
            if mn is None:
                mn = v
                sm = v.astype(np.int32)
            else:
                np.minimum(mn, v, out=mn)
                sm += v
        for s, msk in submask.items():
            rows = np.flatnonzero(msk)
            if rows.size == 0:
                continue
            for store, arr in ((self.k0w[s], mn), (self.k0a[s], sm)):
                sub = arr[rows] if rows.size != arr.shape[0] else arr
                o, ch = np.unravel_index(int(np.argmax(sub)), sub.shape)
                num = int(sub[o, ch])
                cur = store.get(K)
                if cur is None or num > cur[0]:
                    og = int(rows[o])
                    per = []
                    for C in Cf:
                        chi = self.chi_k0[ch] if self.chi_k0 is not None else ch
                        S = sum(int(C[og, v, (chi >> v) & 1]) for v in range(self.V))
                        per.append(abs(2 * S - M))
                    store[K] = (num, int(idx[og]), int(ch), per)


def subset_sums_small(a):
    """subset_sums_last in int16 (|entries| small)."""
    out = np.zeros(a.shape[:-1] + (1,), dtype=np.int16)
    a = a.astype(np.int16)
    for v in range(a.shape[-1]):
        out = np.concatenate([out, out + a[..., v:v + 1]], axis=-1)
    return out


# ------------------------------------------------------------------ result extraction

def k1_dist_value(num, M, K):
    return Fraction(num, 2 * M * (1 << (K + 1)))


def k1_pred_value(num, M):
    return Fraction(num, M) - Fraction(1, 2)


def cell_delta(C, Qv, M, K):
    """Exact Delta(v, x) = C/M - q(v)/2 for one observer's table C (V, 2) and Q_K row Qv."""
    out = {}
    for v in range(C.shape[0]):
        for x in (0, 1):
            out[(v, x)] = Fraction(int(C[v, x]), M) - Fraction(int(Qv[v]), 1 << (K + 1))
    return out
