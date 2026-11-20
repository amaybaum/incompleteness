#!/usr/bin/env python3
"""MEAS-Q exact checks: delivery and preparation on the published rounded rule Q (q = 2**16).

All lattice arithmetic is exact integer arithmetic (numpy integer arrays or Python integers).
Floating point is used only to print logarithms of exact probabilities; no check depends on it.

  Q    x_{t+1}(i) = floor((sum_{j~i} x_t(j) + 1)/3) - x_{t-1}(i)  mod 2**16   (representatives 0..q-1)
  RZ   y_{t+1}(i) = floor((sum_{j~i} y_t(j) + 1)/3) - y_{t-1}(i)               (integers, y = x - c)
  U2   x_{t+1}(i) = g(sum_{j~i} x_t(j)) xor x_{t-1}(i),  g(s) = 1 iff s in {2,3,4}  (q = 2 member)

Run from the record directory (meas-q-20261120/):
  python3 -I checks/measq_checks.py            controls, Node 1 checks, S-A, S-C, CC*, Node 3 cost
  python3 -I checks/measq_checks.py --search   also S-B, S-D and S-E (bounded searches, PREREG §4)
Writes results.json (PREREG §8) beside this directory's RESULT.md and exits 0 iff every check holds.
"""
import itertools
import json
import math
import os
import sys
from fractions import Fraction

import numpy as np

q = 2 ** 16
C = 2 ** 15
RESULTS = {"checks": {}, "searches": {}}


def check(name, ok, info="", data=None):
    ok = bool(ok)
    RESULTS["checks"][name] = {"ok": ok, "info": info, "data": data}
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}{('  ' + info) if info else ''}", flush=True)
    return ok


def G(s):
    return np.floor_divide(s + 1, 3)


def g2(s):
    return ((s >= 2) & (s <= 4)).astype(s.dtype)


# =============================================================== lattice helpers (torus, Q)
def nb(x, axes=(0, 1, 2)):
    return sum(np.roll(x, sh, ax) for ax in axes for sh in (1, -1))


def q_step(prev, cur, axes=(0, 1, 2)):
    """One tick of Q on a torus (int64 arrays of representatives 0..q-1)."""
    return cur, (np.floor_divide(nb(cur, axes) + 1, 3) - prev) % q


def q_back(prev, cur, axes=(0, 1, 2)):
    """Inverse tick: from (x_{t-1}, x_t) to (x_{t-2}, x_{t-1})."""
    return (np.floor_divide(nb(prev, axes) + 1, 3) - cur) % q, prev


def rz_step(prev, cur, axes=(0, 1, 2)):
    return cur, G(nb(cur, axes)) - prev


def u2_step(prev, cur, axes=(0, 1, 2)):
    return cur, g2(nb(cur, axes)) ^ prev


# =============================================================== small boxes (S-A, PC1)
class Box:
    """A box of Z^3 (free boundary: zero outside). Sites indexed 0..n-1."""

    def __init__(self, dims):
        self.dims = dims
        self.S = list(itertools.product(*[range(d) for d in dims]))
        ix = {s: i for i, s in enumerate(self.S)}
        self.n = len(self.S)
        A = np.zeros((self.n, self.n), np.int64)
        for s in self.S:
            for ax in range(len(dims)):
                for d in (1, -1):
                    t = list(s)
                    t[ax] += d
                    if tuple(t) in ix:
                        A[ix[s], ix[tuple(t)]] = 1
        self.A = A


def box_traj(rule, B, p0, c0, W):
    """Trajectories of a batch: p0, c0 int arrays (M, n). Returns (traj, tb) where traj has shape
    (W+1, M, 2, n) with traj[t] = (y_{t-1}, y_t), and tb[m] = first t with some |y_t| >= 2
    (RZ only; W+1 if none). For RZ the box run is exact in Z^3 through t = tb + 1 (PREREG S-A)."""
    M = p0.shape[0]
    traj = np.zeros((W + 1, M, 2, B.n), np.int8 if rule == "U2" else np.int32)
    p, c = p0.astype(np.int64), c0.astype(np.int64)
    traj[0, :, 0], traj[0, :, 1] = p, c
    tb = np.full(M, W + 1, np.int64)
    if rule == "RZ":
        big = np.abs(c).max(axis=1) >= 2
        tb[big & (tb > 0)] = 0
    for t in range(1, W + 1):
        s = c @ B.A.T
        if rule == "U2":
            nc = ((s >= 2) & (s <= 4)).astype(np.int64) ^ p
        else:
            nc = np.floor_divide(s + 1, 3) - p
            assert np.abs(nc).max() < 2 ** 15
        p, c = c, nc
        traj[t, :, 0], traj[t, :, 1] = p, c
        if rule == "RZ":
            big = np.abs(c).max(axis=1) >= 2
            tb[big & (tb > t)] = t
    return traj, tb


def periods(traj):
    """First t >= 1 with traj[t] == traj[0] (0 if none within the trajectory)."""
    W1, M = traj.shape[0], traj.shape[1]
    P = np.zeros(M, np.int64)
    for t in range(1, W1):
        eq = (traj[t] == traj[0]).all(axis=(1, 2)) & (P == 0)
        P[eq] = t
    return P


MODES = ("c", "p", "b")


def enumerate_box(rule, dims, cap_period=40, Wcap=120, persist=60, want_hits=False):
    """S-A / PC1: one carrier, N = 1, single-site H, single-site log, eps = 0 (PREREG §2, §4).
    Returns per-configuration DT_s and DT_A outcomes and summary counts."""
    B = Box(dims)
    vals = (0, 1) if rule == "U2" else (-1, 0, 1)
    out = dict(configs=0, dts=0, dta=0, breach=0, min_weight=None, hits=[], dta_hits=[],
               breach_list=[])
    for j in range(B.n):
        for mode in MODES:
            cslots = [(1, j)] if mode == "c" else [(0, j)] if mode == "p" else [(0, j), (1, j)]
            eslots = [(sl, i) for sl in (0, 1) for i in range(B.n) if (sl, i) not in cslots]
            E = np.array(list(itertools.product(vals, repeat=len(eslots))), np.int64)
            M = E.shape[0]
            p0 = np.zeros((M, B.n), np.int64)
            c0 = np.zeros((M, B.n), np.int64)
            for k, (sl, i) in enumerate(eslots):
                (c0 if sl else p0)[:, i] = E[:, k]
            p1, c1 = p0.copy(), c0.copy()
            for sl, i in cslots:
                if rule == "U2":
                    (c1 if sl else p1)[:, i] ^= 1
                else:
                    (c1 if sl else p1)[:, i] += 1
            weight = (E != 0).sum(axis=1)
            T0, tb0 = box_traj(rule, B, p0, c0, max(Wcap, 3 * cap_period) + persist)
            T1, tb1 = box_traj(rule, B, p1, c1, max(Wcap, 3 * cap_period) + persist)
            P0, P1 = periods(T0), periods(T1)
            Pl = np.array([math.lcm(int(a), int(b)) if a and b else 0 for a, b in zip(P0, P1)])
            Wn = np.where((Pl > 0) & (Pl <= cap_period), 3 * Pl, Wcap)
            tb = np.minimum(tb0, tb1)
            breach = tb <= Wn
            Wn = np.minimum(Wn, tb + 1)              # exact window end (inclusive)
            Wex = np.minimum(tb + 1, T0.shape[0] - 1)  # exact horizon for persistence
            out["configs"] += M * (B.n - 1)
            out["breach"] += int(breach.sum()) * (B.n - 1)
            if want_hits:
                for m in np.nonzero(breach)[0]:
                    out["breach_list"].append(dict(dims=list(dims), j=j, mode=mode,
                                                   eslots=[list(e) for e in eslots],
                                                   env=[int(v) for v in E[m]], tb=int(tb[m])))
            Wmax = int(Wn.max())
            tt = np.arange(T0.shape[0])[:, None]
            inwin = tt <= Wn[None, :]                                   # (W+1, M)
            diff = (T0 != T1).any(axis=2)                               # (W+1, M, n)
            for H in range(B.n):
                if H == j:
                    continue
                hv0 = T0[:, :, 0, H].astype(np.int64) * 7 + T0[:, :, 1, H]
                ready = ~diff[:, :, H] & inwin
                use = diff[:, :, H] & inwin
                anyuse = use.any(axis=0)
                smin = np.where(anyuse, use.argmax(axis=0), 10 ** 6)
                logs = [i for i in range(B.n) if i not in (H, j)]
                okR = np.zeros((len(logs), M), bool)
                for a, L in enumerate(logs):
                    dl = diff[:, :, L]
                    before = (dl & (tt < smin[None, :])).any(axis=0)
                    okR[a] = ~before
                # record available at t: some valid log differs at t
                rec = np.zeros(diff.shape[:2], bool)
                for a, L in enumerate(logs):
                    rec |= diff[:, :, L] & okR[a][None, :]
                # delivery at t2: ready, record, and some ready t1 < s < t2 with same w*, use at s
                deliv = np.zeros(diff.shape[:2], bool)
                lastuse = np.full(M, -1)
                for t2 in range(Wmax + 1):
                    cand = ready[t2] & rec[t2] & (lastuse >= 0)
                    if cand.any():
                        ok = np.zeros(M, bool)
                        for t1 in range(t2):
                            ok |= ready[t1] & (hv0[t1] == hv0[t2]) & (t1 < lastuse)
                        deliv[t2] = cand & ok
                    lastuse = np.where(use[t2], t2, lastuse)
                hit = deliv.any(axis=0)
                t2hit = np.where(hit, deliv.argmax(axis=0), -1)
                nh = int(hit.sum())
                out["dts"] += nh
                if nh:
                    w = int(weight[hit].min())
                    out["min_weight"] = w if out["min_weight"] is None else min(out["min_weight"], w)
                # DT_A (A01 item 1): the largest admissible block (all logs meeting (R)) differs
                # at every t in [t2, t2+persist], within the exact horizon
                dta = np.zeros(M, bool)
                for m in np.nonzero(hit)[0]:
                    Lb = [L for a, L in enumerate(logs) if okR[a, m]]
                    if not Lb:
                        continue
                    for t2 in np.nonzero(deliv[:, m])[0]:
                        t2 = int(t2)
                        if t2 + persist <= Wex[m] and \
                                diff[t2:t2 + persist + 1, m][:, Lb].any(axis=1).all():
                            dta[m] = True
                            break
                out["dta"] += int(dta.sum())
                if want_hits:
                    for m in np.nonzero(hit)[0]:
                        out["hits"].append(dict(dims=list(dims), j=j, mode=mode, H=H,
                                                eslots=[list(e) for e in eslots],
                                                env=[int(v) for v in E[m]],
                                                weight=int(weight[m]), t2=int(t2hit[m]),
                                                P=int(Pl[m]), dta=bool(dta[m])))
    return out




# =============================================================== ledger and audit (PREREG §3)
class Ledger:
    """Every input of a run: background c, designed items, carriers, declared controller writes.
    States are Q states (representatives) on a torus of the given shape."""

    def __init__(self, shape, c):
        self.shape, self.c = shape, c
        self.items, self.carriers, self.controller = [], [], []

    def add(self, name, cells):
        """cells: list of (slice, index-tuple, value relative to c)."""
        self.items.append((name, cells))

    def add_carrier(self, name, cells):
        """cells: list of (slice, index-tuple, delta added when the carrier bit is 1)."""
        self.carriers.append((name, cells))

    def build(self, cv):
        prev = np.full(self.shape, self.c, np.int64)
        cur = np.full(self.shape, self.c, np.int64)
        for _, cells in self.items:
            for sl, ix, v in cells:
                (cur if sl else prev)[ix] = (self.c + v) % q
        if cv:
            for _, cells in self.carriers:
                for sl, ix, d in cells:
                    a = cur if sl else prev
                    a[ix] = (a[ix] + d) % q
        return prev, cur

    def bits(self):
        """Pin cost relative to the uniform law on the torus (PREREG §3): 16 bits per pinned
        designed slot, 16 bits per background slot."""
        slots = {(sl, ix) for _, cells in self.items for sl, ix, _ in cells}
        n = int(np.prod(self.shape))
        return dict(pattern_slots=len(slots), pattern_bits=16 * len(slots),
                    background_bits=32 * n - 16 * len(slots))

    def audit(self, traj, cv):
        """traj: list of (prev, cur) Q states. Returns 'ok' or the first unaccounted input."""
        p0, c0 = self.build(cv)
        if not (np.array_equal(traj[0][0], p0) and np.array_equal(traj[0][1], c0)):
            return "unaccounted prepared resource (initial state differs from the ledger)"
        for t in range(len(traj) - 1):
            p, c = q_step(*traj[t])
            for (tc, sl, ix, v) in self.controller:
                if tc == t + 1:
                    (c if sl else p)[ix] = v
            if not (np.array_equal(p, traj[t + 1][0]) and np.array_equal(c, traj[t + 1][1])):
                return f"unaccounted controller (tick {t + 1} is not the rule's iterate)"
        return "ok"


def q_run(prev, cur, T):
    tr = [(prev.copy(), cur.copy())]
    for _ in range(T):
        prev, cur = q_step(prev, cur)
        tr.append((prev.copy(), cur.copy()))
    return tr


def stackY(trj, sites=None):
    """(T+1, 2, k) array of the tracked sites (flat indices) of a list of (prev, cur) states."""
    if sites is None:
        return np.stack([np.stack([p.reshape(-1), c_.reshape(-1)]) for p, c_ in trj])
    return np.stack([np.stack([p.reshape(-1)[sites], c_.reshape(-1)[sites]]) for p, c_ in trj])


# =============================================================== two-branch delivery evaluator
def dt_eval(Y0, Y1, H, logs, A=None, persist=60, tmax=None, t2range=None):
    """Y0, Y1: int arrays (T+1, 2, k) of tracked sites in the two carrier branches. H: index into
    the tracked sites; logs: tracked indices admissible as logs (disjoint from H and from the
    carrier's initial sites); A: tracked indices of the apparatus region (DT_A), or None.
    DT_s with single-site logs; DT_A with the largest admissible block in A (A01 item 1)."""
    T = Y0.shape[0] - 1 if tmax is None else min(tmax, Y0.shape[0] - 1)
    diff = (Y0 != Y1).any(axis=1)                               # (T+1, k)
    hv = Y0[:, 0, H].astype(np.int64) * (2 * q + 7) + Y0[:, 1, H]
    ready = ~diff[:, H]
    use = diff[:, H]
    out = dict(dts=False, dta=False)
    if not use[:T + 1].any():
        return out
    smin = int(use.argmax())
    okR = [L for L in logs if not diff[:smin, L].any()]
    Aset = set(A) if A is not None else None
    Lb = [L for L in okR if Aset is not None and L in Aset and L != H]
    lastuse = -1
    first = {}
    for t in range(T + 1):
        if ready[t] and hv[t] not in first:
            first[hv[t]] = t
        if ready[t] and lastuse >= 0 and first.get(hv[t], 10 ** 9) < lastuse and \
                (t2range is None or t2range[0] <= t <= t2range[1]):
            recs = [L for L in okR if diff[t, L]]
            if recs and not out["dts"]:
                out.update(dts=True, t1=int(first[hv[t]]), t2=t, log=int(recs[0]), smin=smin)
            if Lb and not out["dta"] and t + persist <= Y0.shape[0] - 1 and \
                    diff[t:t + persist + 1][:, Lb].any(axis=1).all():
                out.update(dta=True, t2a=t, block=len(Lb))
        if use[t]:
            lastuse = t
    return out


# =============================================================== Node 1: confinement on Q
def node1_checks():
    # K1: exhaustive one-site test in Q, all neighbour representatives r, five backgrounds.
    allok, table = True, {}
    r = np.arange(q, dtype=np.int64)
    for c in (0, 1, C, q - 2, q - 1):
        nxt = (np.floor_divide(5 * c + r + 1, 3) - c) % q
        stay = set(np.nonzero(nxt == c)[0].tolist())
        pred = {v for v in (c - 1, c, c + 1) if 0 <= v < q}
        table[str(c)] = sorted(stay)
        allok &= stay == pred
    check("K1 one-site test in Q (all 65 536 neighbour representatives r; c in {0, 1, 2^15, q-2, "
          "q-1}): a background site with one non-background neighbour stays at c iff r in "
          "[c-1, c+1] (Lemma MQ1, sharp)", allok, data=table)

    # K2: windowed confinement and class isolation on random configurations in Q.
    rng = np.random.default_rng(20261120)
    n = 20
    inst, nontriv, ok = 0, 0, True
    for trial in range(300):
        c = int(rng.choice([1, 2, C, q - 3, q - 2]))
        kind = trial % 3
        prev = np.full((n, n, n), c, np.int64)
        cur = prev.copy()
        D1 = tuple(slice(3, 3 + int(rng.integers(1, 4))) for _ in range(3))
        D2 = (slice(11, 11 + int(rng.integers(1, 4))),) + tuple(slice(3, 3 + int(rng.integers(1, 4))) for _ in range(2))
        for Dk in (D1, D2):
            shp = prev[Dk].shape
            if kind == 0:      # ternary values
                prev[Dk] = c + rng.integers(-1, 2, shp)
                cur[Dk] = c + rng.integers(-1, 2, shp)
            elif kind == 1:    # arbitrary values (full alphabet)
                prev[Dk] = rng.integers(0, q, shp)
                cur[Dk] = rng.integers(0, q, shp)
            else:              # mostly ternary, a few large values
                prev[Dk] = c + rng.integers(-1, 2, shp)
                cur[Dk] = c + rng.integers(-1, 2, shp)
                cur[Dk] = np.where(rng.random(shp) < 0.1, rng.integers(0, q, shp), cur[Dk])
        Dmask = np.zeros((n, n, n), bool)
        Dmask[D1] = True
        Dmask[D2] = True
        D1mask = np.zeros((n, n, n), bool)
        D1mask[D1] = True
        bd = Dmask & (nb((~Dmask).astype(np.int64)) > 0)       # inner boundary layer of D
        sp, sc = prev.copy(), cur.copy()
        sp[D2], sc[D2] = c, c                                   # D1 alone
        p_, c_ = prev, cur
        for t in range(1, 40):
            if not (np.abs(c_[bd] - c) <= 1).all():
                break                                           # hypothesis fails at tick t-1
            p_, c_ = q_step(p_, c_)
            sp, sc = q_step(sp, sc)
            inst += 1
            nontriv += t >= 3
            if (c_[~Dmask] != c).any() or (p_[~Dmask] != c).any():
                ok = False
            if not (np.array_equal(c_[D1mask], sc[D1mask]) and np.array_equal(p_[D1mask], sp[D1mask])):
                ok = False
    check("K2 windowed confinement and class isolation in Q (300 random two-box configurations, "
          "ternary, full-alphabet and mixed contents; c in {1, 2, 2^15, q-3, q-2}): while the inner "
          "boundary layer of D stays in [c-1, c+1], the support stays in D and D1 evolves as alone "
          "(Theorem MQ2; the instance-ticks tested carry in-range values throughout D, out-of-range "
          "interior and previous-slice values are exercised by K2b)", ok and nontriv > 50,
          f"{inst} instance-ticks, {nontriv} with t >= 3",
          data=dict(instance_ticks=inst, nontrivial=int(nontriv)))
    k2b()

    # CC5: sharpness. (a) value c+2 at a closed singleton; (b) vacuum c = 0 with the residue of -1.
    res = {}
    for c, v in ((C, C + 2), (0, q - 1)):
        prev = np.full((8, 8, 8), c, np.int64)
        cur = prev.copy()
        cur[4, 4, 4] = v
        _, c_ = q_step(prev, cur)
        m = np.ones((8, 8, 8), bool)
        m[4, 4, 4] = False
        res[str(c)] = int((c_[m] != c).sum())
    check("CC5 countercontrol: a closed singleton whose value leaves [c-1, c+1] breaches at once "
          "(c = 2^15 with value c+2; vacuum c = 0 with q-1, the residue of -1): all six neighbours "
          "leave c", res[str(C)] == 6 and res["0"] == 6, data=res)

    # K3: U1 Lemma 2.1 at c in {1, 2^15, q-2}: ternary RZ orbit = Q orbit while in the window.
    rng = np.random.default_rng(7)
    ok, cc = True, False
    for c in (1, C, q - 2, 0):
        for _ in range(5):
            yp = np.zeros((10, 10, 10), np.int64)
            yc = yp.copy()
            yp[3:6, 3:6, 3:6] = rng.integers(-1, 2, (3, 3, 3))
            yc[3:6, 3:6, 3:6] = rng.integers(-1, 2, (3, 3, 3))
            xp, xc = (c + yp) % q, (c + yc) % q
            agree = True
            for t in range(12):
                inwin = ((c + yc) >= 0).all() and ((c + yc) < q).all() and \
                    ((c + yp) >= 0).all() and ((c + yp) < q).all()
                if not (np.array_equal(xc, (c + yc) % q) and np.array_equal(xp, (c + yp) % q)):
                    agree = False
                    break
                if not inwin and c != 0:
                    break
                yp, yc = rz_step(yp, yc)
                xp, xc = q_step(xp, xc)
            if c == 0:
                cc |= not agree
            else:
                ok &= agree
    check("K3 U1 Lemma 2.1 at c in {1, 2^15, q-2}: c + (RZ orbit) is the Q orbit while c + y stays "
          "in [0, q); countercontrol c = 0 (the residue of -1 is q-1) differs", ok and cc)

    # D1 (A01 item 4): every single-site perturbation with slices in [c-1, c+1] stays on its site.
    ok = True
    m = np.ones((5, 5, 5), bool)
    m[2, 2, 2] = False
    for c in (1, C, q - 2):
        for a in (-1, 0, 1):
            for b in (-1, 0, 1):
                prev = np.full((5, 5, 5), c, np.int64)
                cur = prev.copy()
                prev[2, 2, 2], cur[2, 2, 2] = c + a, c + b
                for _ in range(64):
                    prev, cur = q_step(prev, cur)
                    if (cur[m] != c).any() or (prev[m] != c).any():
                        ok = False
    check("D1 in Q every single-site perturbation with both slices in [c-1, c+1] stays on its site "
          "for 64 ticks (c in {1, 2^15, q-2}); the step behind NP1 Lemma N2.3 on Q", ok)


def k2b():
    """K2b (post-review, B3): Theorem MQ2 with the inner boundary layer in [c-1, c+1] and every other
    value of D unrestricted (interior current slice and the whole previous slice over the full
    alphabet), including the wrap backgrounds c in {0, q-1}. Counts the instance-ticks at which an
    out-of-range interior or previous-slice value is present."""
    rng = np.random.default_rng(20261121)
    n = 20
    inst, exer, ok = 0, 0, True
    for c in (0, 1, 2, C, q - 3, q - 2, q - 1):
        lo, hi = max(c - 1, 0), min(c + 1, q - 1)
        for trial in range(100):
            prev = np.full((n, n, n), c, np.int64)
            cur = prev.copy()
            D1 = tuple(slice(3, 3 + int(rng.integers(3, 6))) for _ in range(3))
            D2 = (slice(12, 12 + int(rng.integers(1, 6))),) + \
                tuple(slice(3, 3 + int(rng.integers(1, 6))) for _ in range(2))
            Dmask = np.zeros((n, n, n), bool)
            Dmask[D1] = True
            Dmask[D2] = True
            D1mask = np.zeros((n, n, n), bool)
            D1mask[D1] = True
            bd = Dmask & (nb((~Dmask).astype(np.int64)) > 0)
            inner = Dmask & ~bd
            prev[Dmask] = rng.integers(0, q, int(Dmask.sum()))
            cur[inner] = rng.integers(0, q, int(inner.sum()))
            cur[bd] = rng.integers(lo, hi + 1, int(bd.sum()))
            sp, sc = prev.copy(), cur.copy()
            sp[D2], sc[D2] = c, c
            p_, c_ = prev, cur
            for t in range(1, 40):
                if not ((c_[bd] >= lo) & (c_[bd] <= hi)).all():
                    break
                outr = ((c_[inner] < lo) | (c_[inner] > hi)).any() or \
                    ((p_[Dmask] < lo) | (p_[Dmask] > hi)).any()
                p_, c_ = q_step(p_, c_)
                sp, sc = q_step(sp, sc)
                inst += 1
                exer += bool(outr)
                if (c_[~Dmask] != c).any() or (p_[~Dmask] != c).any():
                    ok = False
                if not (np.array_equal(c_[D1mask], sc[D1mask]) and np.array_equal(p_[D1mask], sp[D1mask])):
                    ok = False
    check("K2b (post-review) Theorem MQ2 with the inner boundary layer in [c-1, c+1] and the interior "
          "current slice and the whole previous slice of D unrestricted (700 random two-box "
          "configurations; c in {0, 1, 2, 2^15, q-3, q-2, q-1}): at every instance-tick the support "
          "stays in D and D1 evolves as alone",
          ok and exer >= 500 and exer * 2 >= inst, f"{inst} instance-ticks, {exer} with out-of-range values",
          data=dict(instance_ticks=inst, exercised=exer))


# =============================================================== S-A, PC1, PC2
def s_a():
    tot = {}
    for d in [(3,), (4,), (5,), (2, 2)]:
        tot[str(d)] = enumerate_box("U2", d)["dts"]
    check("PC1 the S-A enumerator on U2 reproduces NP1 S2 (line 3, line 4, line 5, 2x2; one carrier, "
          "N = 1): 0, 184, 1904, 736", [tot[k] for k in ("(3,)", "(4,)", "(5,)", "(2, 2)")] ==
          [0, 184, 1904, 736], data=tot)
    r5 = enumerate_box("U2", (5,), want_hits=True)
    target = None
    for h in r5["hits"]:
        if h["j"] == 0 and h["mode"] == "c" and h["H"] == 1:
            env = dict(zip(map(tuple, h["eslots"]), h["env"]))
            cur = [env.get((1, i), 0) for i in range(1, 5)]
            prev = [env.get((0, i), 0) for i in range(5)]
            if cur == [0, 1, 0, 1] and prev == [0] * 5:
                target = h
    check("PC2 DL1 2.3(f) is found by the same enumerator on U2 (line 5, carrier at site 0 current "
          "slice, H = 1, environment (.,0,1,0,1)) with tau2 = 5",
          target is not None and target["t2"] == 5, data=target)
    out = {}
    for d in [(3,), (4,), (5,), (2, 2)]:
        r = enumerate_box("RZ", d, want_hits=True)
        out[str(d)] = r
        print(f"  S-A RZ {d}: configs x H {r['configs']}, DT_s {r['dts']}, DT_A {r['dta']}, "
              f"breaching configs {len(r['breach_list'])}, min weight {r['min_weight']}", flush=True)
    RESULTS["searches"]["S-A"] = {k: dict(configs_times_H=v["configs"], dts=v["dts"], dta=v["dta"],
                                          breach_configs=len(v["breach_list"]),
                                          min_weight=v["min_weight"]) for k, v in out.items()}
    return out


def place_box(hit, n=16, c=C):
    """Ledger for an S-A configuration placed in Q on the torus (Z/n)^3 at background c."""
    B = Box(tuple(hit["dims"]))
    ix = [tuple(int(v) + 4 for v in (tuple(s) + (0,) * (3 - len(s)))) for s in B.S]
    L = Ledger((n, n, n), c)
    L.add("environment", [(sl, ix[i], v) for (sl, i), v in zip(hit["eslots"], hit["env"]) if v != 0])
    cs = [(1, hit["j"])] if hit["mode"] == "c" else [(0, hit["j"])] if hit["mode"] == "p" else \
        [(0, hit["j"]), (1, hit["j"])]
    L.add_carrier("carrier", [(sl, ix[i], 1) for sl, i in cs])
    return L, ix


def rerun_in_q(hit, T):
    """Re-run an S-A hit in Q itself; re-evaluate DT_s/DT_A there; ledger-audit both branches."""
    L, ix = place_box(hit)
    tr = [q_run(*L.build(cv), T) for cv in (0, 1)]
    aud = [L.audit(tr[cv], cv) for cv in (0, 1)]
    n = L.shape[0]
    flat = {s: k for k, s in enumerate(itertools.product(range(n), repeat=3))}
    Y0, Y1 = stackY(tr[0]), stackY(tr[1])
    H = flat[ix[hit["H"]]]
    js = flat[ix[hit["j"]]]
    logs = [k for k in range(n ** 3) if k not in (H, js)]
    A = {flat[s] for s in ix} - {js}
    return dt_eval(Y0, Y1, H, logs, A=A, persist=60), aud, L


def s_a_q_reruns(SA):
    """Q re-run, ledger audit and pin cost for the minimum-weight DT_s hit of every box and for
    every DT_A hit (at most 50 per box, in enumeration order)."""
    rep, ok = {}, True
    for k, r in SA.items():
        if not r["hits"]:
            rep[k] = []
            continue
        sel = [min(r["hits"], key=lambda h: (h["weight"], h["t2"]))] + [h for h in r["hits"] if h["dta"]][:50]
        out = []
        for h in sel:
            res, aud, L = rerun_in_q(h, T=h["t2"] + 64)
            good = res["dts"] and aud == ["ok", "ok"] and (res["dta"] if h["dta"] else True)
            ok &= bool(good)
            out.append(dict(hit=h, q=res, audit=aud, bits=L.bits()))
        rep[k] = out
    return rep, ok


# =============================================================== W2 line (S-C, S-D)
PW2 = [-1, -1, 1, 1]          # W2 background along a line (U1 E2; U2R), period 4
LX, LY = 384, 8               # torus (LX, LY, LY), bipartite (all sides even); line along x at y = z = 0
OX, OY = LX // 2, LY // 2     # origin index (OX + 2*OY even: index parity = coordinate parity)
T1, TP = 120, 60


def lidx(p):
    return ((p[0] + OX) % LX, p[1] + OY, p[2] + OY)


def par(p):
    return (p[0] + p[1] + p[2]) % 2


def put(s, p, v):
    """Signal component at t = 0: current slice on even sites, previous slice on odd sites."""
    (s[1] if par(p) == 0 else s[0])[lidx(p)] = v


def getv(s, p):
    return int((s[1] if par(p) == 0 else s[0])[lidx(p)])


def line_bg(phi):
    s = (np.zeros((LX, LY, LY), np.int64), np.zeros((LX, LY, LY), np.int64))
    for x in range(-OX, LX - OX):
        put(s, (x, 0, 0), PW2[(x + 1 + phi) % 4])
    return s


def with_flip(s, xs):
    s = (s[0].copy(), s[1].copy())
    for x in xs:
        put(s, (x, 0, 0), -getv(s, (x, 0, 0)))
    return s


LINE_MASK = np.zeros((LX, LY, LY), bool)
LINE_MASK[:, OY, OY] = True
RL = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1) if (y, z) != (0, 0)]
RLP = [(x, y, z) for x in range(-2, 3) for y in range(-2, 3) for z in range(-2, 3) if (y, z) != (0, 0)]
ASITES = [(x, 0, 0) for x in range(-2, 3)] + RLP           # apparatus region A of S-C and S-D
ALLOWED = LINE_MASK.copy()
for p in RLP:
    ALLOWED[lidx(p)] = True
AFLAT = np.array([np.ravel_multi_index(lidx(p), (LX, LY, LY)) for p in ASITES])
LFLAT = np.array([np.ravel_multi_index(lidx((x, 0, 0)), (LX, LY, LY)) for x in range(-OX, LX - OX)])


def k0_launch():
    """A01 item 2: for each phase and direction, the flip pair whose plain-line defect stays on at
    most 3 sites for 30 ticks and moves toward the origin."""
    choice, ok = {}, True
    for phi in range(4):
        N = line_bg(phi)
        Ntr = [N]
        s = N
        for _ in range(30):
            s = rz_step(*s)
            Ntr.append(s)
        per = all(np.array_equal(Ntr[t + 4][0], Ntr[t][0]) and np.array_equal(Ntr[t + 4][1], Ntr[t][1])
                  for t in range(4))
        ok &= per
        for d in (1, -1):
            pick = None
            for x0 in ((-12, -11) if d == 1 else (10, 11)):
                s = with_flip(N, (x0, x0 + 1))
                good, xs = True, []
                for t in range(31):
                    df = ((s[0] != Ntr[t][0]) | (s[1] != Ntr[t][1]))
                    if (df & ~LINE_MASK).any() or df.sum() > 3 or df.sum() == 0:
                        good = False
                        break
                    xs.append(np.nonzero(df[:, OY, OY])[0].mean() - OX)
                    s = rz_step(*s)
                if good and d * (xs[-1] - xs[0]) >= 8:
                    pick = x0
                    break
            choice[(phi, d)] = pick
        ok &= choice[(phi, 1)] is not None or choice[(phi, -1)] is not None
    return choice, ok


def line_ledger(phi, flip=None, gadget=(), c=C):
    L = Ledger((LX, LY, LY), c)
    cells = []
    for x in range(-OX, LX - OX):
        p = (x, 0, 0)
        cells.append((1 if par(p) == 0 else 0, lidx(p), PW2[(x + 1 + phi) % 4]))
    L.add("W2 line", cells)
    if gadget:
        L.add("gadget", [(1 if par(p) == 0 else 0, lidx(p), v) for p, v in gadget])
    if flip is not None:
        cl = []
        for x in flip:
            p = (x, 0, 0)
            v = PW2[(x + 1 + phi) % 4]
            cl.append((1 if par(p) == 0 else 0, lidx(p), (-2 * v) % q))
        L.add_carrier("W2 signal (flip of a background pair)", cl)
    return L


def s_c(choice):
    """S-C and CC4: the plain W2 line with a passing signal, run in Q itself."""
    phi, d = 0, 1
    x0 = choice[(phi, d)]
    L = line_ledger(phi, flip=(x0, x0 + 1))
    tr = [q_run(*L.build(cv), T1 + TP) for cv in (0, 1)]
    aud = [L.audit(tr[cv], cv) for cv in (0, 1)]
    sites = np.concatenate([LFLAT, AFLAT])
    sites = np.unique(sites)
    pos = {int(s): k for k, s in enumerate(sites)}
    Y0, Y1 = stackY(tr[0], sites), stackY(tr[1], sites)
    carrier = {pos[int(np.ravel_multi_index(lidx((x, 0, 0)), (LX, LY, LY)))] for x in (x0, x0 + 1)}
    A = [pos[int(a)] for a in AFLAT]
    res = {}
    for xh in range(-2, 3):
        H = pos[int(np.ravel_multi_index(lidx((xh, 0, 0)), (LX, LY, LY)))]
        logs = [k for k in range(len(sites)) if k != H and k not in carrier]
        res[xh] = dt_eval(Y0, Y1, H, logs, A=A, persist=TP, tmax=T1)
    offline = all(((p != C) | (c_ != C))[~LINE_MASK].sum() == 0 for p, c_ in tr[1])
    dts = any(r["dts"] for r in res.values())
    dta = any(r["dta"] for r in res.values())
    check("CC4 S-C in Q: the plain W2 line with a passing signal meets DT_s (H a line site within 2 "
          "of the origin; the log is the moved signal) and fails DT_A (no record persists in A); "
          "no off-line value; ledger audit ok", dts and not dta and offline and aud == ["ok", "ok"],
          data={str(k): v for k, v in res.items()})
    RESULTS["searches"]["S-C"] = dict(dts=dts, dta=dta, per_H={str(k): v for k, v in res.items()},
                                      audit=aud, bits=L.bits())
    # CC3: an undeclared prepared resource (an off-line value not in the ledger).
    p0, c0 = L.build(1)
    c0 = c0.copy()
    c0[lidx((5, 2, 0))] = (C + 1) % q
    tr3 = q_run(p0, c0, 3)
    a3 = L.audit(tr3, 1)
    check("CC3 an initial pattern outside the ledger is reported as an unaccounted prepared resource",
          a3.startswith("unaccounted prepared resource"), a3)
    return res, L, tr


def cc2():
    """CC2: an imported controller. A box configuration whose H is used and not re-armed by Q;
    a write H := w* at a tick t2 at which a valid log holds the carrier gives DT arithmetic; the
    ledger audit reports the write as an unaccounted controller."""
    hit = dict(dims=[4], j=0, mode="c", H=1, eslots=None, env=None, t2=0, dta=False)
    B = Box((4,))
    eslots = [(sl, i) for sl in (0, 1) for i in range(4) if (sl, i) != (1, 0)]
    for env in itertools.product((-1, 0, 1), repeat=len(eslots)):
        hit.update(eslots=[list(e) for e in eslots], env=list(env))
        L, ix = place_box(hit)
        tr = [q_run(*L.build(cv), 12) for cv in (0, 1)]
        n = L.shape[0]
        flat = {s: k for k, s in enumerate(itertools.product(range(n), repeat=3))}
        Y0, Y1 = stackY(tr[0]), stackY(tr[1])
        H, js = flat[ix[1]], flat[ix[0]]
        logs = [k for k in range(n ** 3) if k not in (H, js)]
        if dt_eval(Y0, Y1, H, logs)["dts"]:
            continue
        diff = (Y0 != Y1).any(axis=1)
        if not diff[:, H].any():
            continue
        smin = int(diff[:, H].argmax())
        okR = [k for k in logs if not diff[:smin, k].any()]
        for t2 in range(smin + 1, 12):
            if diff[t2, H] and any(diff[t2, k] for k in okR):
                # controller writes H := its t = 0 value in both slices, both branches, at t2
                w = (int(tr[0][0][0][ix[1]]), int(tr[0][0][1][ix[1]]))
                L.controller = [(t2, 0, ix[1], w[0]), (t2, 1, ix[1], w[1])]
                trc = []
                for cv in (0, 1):
                    p, c_ = L.build(cv)
                    seq = [(p.copy(), c_.copy())]
                    for t in range(1, t2 + 1):
                        p, c_ = q_step(p, c_)
                        if t == t2:
                            p[ix[1]], c_[ix[1]] = w
                        seq.append((p.copy(), c_.copy()))
                    trc.append(seq)
                Z0, Z1 = stackY(trc[0]), stackY(trc[1])
                met = dt_eval(Z0, Z1, H, logs)["dts"]
                undeclared = Ledger(L.shape, L.c)
                undeclared.items, undeclared.carriers = L.items, L.carriers
                a_un = undeclared.audit(trc[1], 1)
                a_de = L.audit(trc[1], 1)
                return check("CC2 an imported controller (H rewritten to w* by a write that Q does "
                             "not produce) meets DT_s arithmetic; the audit reports an unaccounted "
                             "controller, and accepts the run only when the write is declared",
                             met and a_un.startswith("unaccounted controller") and a_de == "ok",
                             f"t2 = {t2}; {a_un}", data=dict(env=list(env), t2=t2))
    return check("CC2 imported controller", False, "no configuration found")


def cc1():
    """CC1: U2, carrier class and H class at l1-distance >= 3 (two boxes): H never depends on c."""
    rng = np.random.default_rng(11)
    n, ok = 16, True
    for _ in range(50):
        prev = np.zeros((n, n, n), np.int64)
        cur = prev.copy()
        D1 = (slice(2, 5), slice(2, 5), slice(2, 5))
        D2 = (slice(8, 11), slice(2, 5), slice(2, 5))   # distance 4 from D1
        for Dk in (D1, D2):
            prev[Dk] = rng.integers(0, 2, (3, 3, 3))
            cur[Dk] = rng.integers(0, 2, (3, 3, 3))
        p1, c1 = prev.copy(), cur.copy()
        c1[3, 3, 3] ^= 1                                # carrier in D1
        a, b = (prev, cur), (p1, c1)
        for _ in range(60):
            if not (np.array_equal(a[0][D2], b[0][D2]) and np.array_equal(a[1][D2], b[1][D2])):
                ok = False
            a, b = u2_step(*a), u2_step(*b)
    check("CC1 U2 countercontrol: with the carrier's class and H's class at distance >= 3, H's class "
          "never depends on the carrier (50 random designs, 60 ticks; DL1 2.3(c))", ok)


# =============================================================== S-B (breach and contact, Q)
def s_b(SA):
    pool = []
    for k in ("(3,)", "(4,)", "(2, 2)"):
        pool += SA[k]["breach_list"]
    cnt = len(pool)
    m = max(1, math.ceil(cnt / 4000))
    sel = pool[::m]
    n, T, R = 42, 28, 8
    # exact region: sites at l1 distance 1..R from the box (box placed at offset 4)
    grid = np.indices((n, n, n)).reshape(3, -1).T
    stats = dict(pool=cnt, stride=m, run=len(sel), contact=0, contact_by_d={d: 0 for d in range(1, R + 1)},
                 return_after_use=0, dts=0, examples=[], breach_t=[], support28=[])
    batch = 24
    for b0 in range(0, len(sel), batch):
        chunk = sel[b0:b0 + batch]
        P = np.full((2 * len(chunk), n, n, n), C, np.int64)
        Cc = P.copy()
        boxes = []
        for k, h in enumerate(chunk):
            B = Box(tuple(h["dims"]))
            ix = [tuple(int(v) + 4 for v in (tuple(s) + (0,) * (3 - len(s)))) for s in B.S]
            boxes.append((ix, h))
            for br in (0, 1):
                for (sl, i), v in zip(h["eslots"], h["env"]):
                    (Cc if sl else P)[(2 * k + br,) + ix[i]] = C + v
                if br:
                    cs = [(1, h["j"])] if h["mode"] == "c" else [(0, h["j"])] if h["mode"] == "p" else \
                        [(0, h["j"]), (1, h["j"])]
                    for sl, i in cs:
                        (Cc if sl else P)[(2 * k + 1,) + ix[i]] += 1
        hist = [(P.copy(), Cc.copy())]
        for t in range(T):
            P, Cc = q_step(P, Cc, axes=(1, 2, 3))
            hist.append((P.copy(), Cc.copy()))
        for k, (ix, h) in enumerate(boxes):
            arr = np.array(ix)
            dist = np.abs(grid[:, None, :] - arr[None, :, :]).sum(axis=2).min(axis=1)
            ex = np.nonzero((dist >= 1) & (dist <= R))[0]
            Y0 = np.stack([np.stack([hist[t][0][2 * k].reshape(-1)[ex], hist[t][1][2 * k].reshape(-1)[ex]])
                           for t in range(T + 1)])
            Y1 = np.stack([np.stack([hist[t][0][2 * k + 1].reshape(-1)[ex], hist[t][1][2 * k + 1].reshape(-1)[ex]])
                           for t in range(T + 1)])
            diff = (Y0 != Y1).any(axis=1)
            nonbg = ((Y0 != C) | (Y1 != C)).any(axis=1)
            used = diff.any(axis=0)
            if nonbg.any():
                stats["contact"] += 1
                for d in range(1, R + 1):
                    if nonbg[:, dist[ex] == d].any():
                        stats["contact_by_d"][d] += 1
            stats["breach_t"].append(h["tb"])
            stats["support28"].append(int(((hist[T][0][2 * k] != C) | (hist[T][1][2 * k] != C)).sum()))
            back = np.zeros(len(ex), bool)
            for a in np.nonzero(used)[0]:
                s1 = int(diff[:, a].argmax())
                bgboth = (Y0[:, :, a] == C).all(axis=1) & (Y1[:, :, a] == C).all(axis=1)
                if bgboth[s1 + 1:].any():
                    back[a] = True
            if back.any():
                stats["return_after_use"] += 1
                for a in np.nonzero(back)[0][:5]:
                    logs = [z for z in range(len(ex)) if z != a]
                    r = dt_eval(Y0, Y1, a, logs)
                    if r["dts"]:
                        stats["dts"] += 1
                        if len(stats["examples"]) < 10:
                            stats["examples"].append(dict(hit=h, site=grid[ex[a]].tolist(),
                                                          d=int(dist[ex[a]]), dt=r))
                        break
    bt = np.array(stats["breach_t"])
    s28 = np.array(stats["support28"])
    stats["breach_t"] = dict(min=int(bt.min()), median=float(np.median(bt)), max=int(bt.max()))
    stats["support28"] = dict(min=int(s28.min()), median=float(np.median(s28)), max=int(s28.max()))
    RESULTS["searches"]["S-B"] = stats
    print(f"  S-B: pool {cnt}, run {len(sel)} (stride {m}); contact outside the box "
          f"{stats['contact']}; by distance {stats['contact_by_d']}; a used outside site back at "
          f"(c,c) in both branches: {stats['return_after_use']}; DT_s across classes: {stats['dts']}",
          flush=True)
    check("S-B completeness: every selected breaching configuration was run (stride rule of PREREG §4)",
          len(sel) == math.ceil(cnt / m))
    return stats


# =============================================================== S-D (latch beside a W2 line)
def sd_family():
    fam = [()]
    for p in RL:
        for v in (1, -1, 2, -2):
            fam.append(((p, v),))
    for a, b in itertools.combinations(RL, 2):
        for v in (1, -1, 2, -2):
            for w in (1, -1, 2, -2):
                fam.append(((a, v), (b, w)))
    return fam


def sd_states(phi, gadgets, flip=None):
    base = line_bg(phi)
    M = len(gadgets)
    P = np.repeat(base[0][None], M, axis=0)
    Cc = np.repeat(base[1][None], M, axis=0)
    for k, g in enumerate(gadgets):
        for p, v in g:
            (Cc if par(p) == 0 else P)[(k,) + lidx(p)] = v
    if flip is not None:
        for x in flip:
            p = (x, 0, 0)
            (Cc if par(p) == 0 else P)[(slice(None),) + lidx(p)] *= -1
    return P, Cc


def classify_sd(SA_hist, N4, rad_tick, line_T, line_N):
    """S-D requirements L2-L4 on one candidate (L1 is applied before).
    SA_hist: (T1+TP+1, 2, |A|) signal-orbit values on A; N4: (4, 2, |A|) no-signal values on A
    (4-periodic by L1); rad_tick: first tick with a value outside line u R_L+ (or None);
    line_T: dict t -> (2, LX) signal-orbit line values at T1 and T1+TP; line_N: dict t -> (2, LX)."""
    if rad_tick is not None:
        return "L2", None
    Aline = {k for k, p in enumerate(ASITES) if p[1:] == (0, 0)}
    for t in (T1, T1 + TP):
        d = (line_T[t] != line_N[t]).any(axis=0)
        xs = np.nonzero(d)[0] - OX
        xs = [x for x in xs if abs(x) > 2]
        if xs:
            xs = sorted((x + OX) % LX for x in xs)
            gaps = [(xs[(i + 1) % len(xs)] - xs[i]) % LX for i in range(len(xs))]
            span = LX - max(gaps) + 1 if len(xs) > 1 else 1
            if span > 8:
                return "L3", None
    Nt = np.stack([N4[t % 4] for t in range(SA_hist.shape[0])])
    for H in range(len(ASITES)):
        logs = [k for k in range(len(ASITES)) if k != H]
        r = dt_eval(Nt, SA_hist, H, logs, A=list(range(len(ASITES))), persist=TP,
                    t2range=(T1 - 3, T1))
        if r["dta"]:
            r["H"] = list(ASITES[H])
            return "pass", r
    return "L4", None


def s_d(choice):
    fam = sd_family()
    nfam = len(fam)
    check("S-D family size (1 + 4*24 + 16*C(24,2)) = 4513 per phase", nfam == 1 + 4 * 24 + 16 * 276)
    stage = {}
    hits = []
    sym = {}
    for phi in range(4):
        # L1 prefilter on the no-signal orbit (8 ticks)
        quiet = []
        for b0 in range(0, nfam, 512):
            chunk = fam[b0:b0 + 512]
            P, Cc = sd_states(phi, chunk)
            P0, C0 = P.copy(), Cc.copy()
            good = np.ones(len(chunk), bool)
            for t in range(1, 9):
                P, Cc = rz_step(P, Cc, axes=(1, 2, 3))
                good &= ~(((P != 0) | (Cc != 0)) & ~ALLOWED[None]).any(axis=(1, 2, 3))
                if t == 4:
                    good &= (P == P0).all(axis=(1, 2, 3)) & (Cc == C0).all(axis=(1, 2, 3))
            quiet += [b0 + k for k in np.nonzero(good)[0]]
        for d in (1, -1):
            x0 = choice[(phi, d)]
            if x0 is None:
                stage[f"phi{phi}_d{d:+d}"] = "not launched (K0)"
                continue
            res = dict(L1=len(quiet), L2=0, L3=0, L4=0, passed=0)
            outcomes = {}
            for b0 in range(0, len(quiet), 128):
                ids = quiet[b0:b0 + 128]
                gad = [fam[i] for i in ids]
                PN, CN = sd_states(phi, gad)
                N4 = []
                lineN = {}
                p_, c_ = PN, CN
                for t in range(4):
                    N4.append(np.stack([p_.reshape(len(ids), -1)[:, AFLAT], c_.reshape(len(ids), -1)[:, AFLAT]], 1))
                    p_, c_ = rz_step(p_, c_, axes=(1, 2, 3))
                for t in (T1, T1 + TP):
                    # N is 4-periodic (L1); take N(t mod 4) on the line
                    pp, cc = PN, CN
                    for _ in range(t % 4):
                        pp, cc = rz_step(pp, cc, axes=(1, 2, 3))
                    lineN[t] = np.stack([pp.reshape(len(ids), -1)[:, LFLAT], cc.reshape(len(ids), -1)[:, LFLAT]], 1)
                P, Cc = sd_states(phi, gad, flip=(x0, x0 + 1))
                histA = [np.stack([P.reshape(len(ids), -1)[:, AFLAT], Cc.reshape(len(ids), -1)[:, AFLAT]], 1)]
                rad = np.full(len(ids), -1)
                lineT = {}
                for t in range(1, T1 + TP + 1):
                    P, Cc = rz_step(P, Cc, axes=(1, 2, 3))
                    assert max(int(np.abs(P).max()), int(np.abs(Cc).max())) < 2 ** 15
                    out = (((P != 0) | (Cc != 0)) & ~ALLOWED[None]).any(axis=(1, 2, 3))
                    rad[(rad < 0) & out] = t
                    histA.append(np.stack([P.reshape(len(ids), -1)[:, AFLAT], Cc.reshape(len(ids), -1)[:, AFLAT]], 1))
                    if t in (T1, T1 + TP):
                        lineT[t] = np.stack([P.reshape(len(ids), -1)[:, LFLAT], Cc.reshape(len(ids), -1)[:, LFLAT]], 1)
                    if (rad >= 0).all():
                        break
                histA = np.stack(histA)
                for k, i in enumerate(ids):
                    if rad[k] >= 0:
                        st, r = "L2", None
                    else:
                        st, r = classify_sd(histA[:, k], np.stack(N4)[:, k], None,
                                            {t: lineT[t][k] for t in lineT}, {t: lineN[t][k] for t in lineN})
                    outcomes[i] = st
                    if st == "pass":
                        res["passed"] += 1
                        hits.append(dict(phi=phi, d=d, gadget=[[list(p), v] for p, v in fam[i]], dt=r))
                    else:
                        res[st] += 1
            stage[f"phi{phi}_d{d:+d}"] = res
            sym[(phi, d)] = outcomes
            print(f"  S-D phase {phi} dir {d:+d}: quiescent {res['L1']}, fail L2 {res['L2']}, L3 {res['L3']}, "
                  f"L4 {res['L4']}, pass {res['passed']}", flush=True)
    # K5 (A01 item 3): phase phi+2 with negated gadget values = phase phi
    neg = {g: k for k, g in enumerate(fam)}
    k5 = True
    for phi in (0, 1):
        for d in (1, -1):
            if (phi, d) not in sym or (phi + 2, d) not in sym:
                k5 &= ((phi, d) in sym) == ((phi + 2, d) in sym)
                continue
            a, b = sym[(phi, d)], sym[(phi + 2, d)]
            for i, st in a.items():
                gi = tuple((p, -v) for p, v in fam[i])
                j = neg[gi]
                if b.get(j) != st:
                    k5 = False
            if len(a) != len(b):
                k5 = False
    check("K5 S-D phase symmetry: outcomes at phase phi+2 equal those at phase phi with every gadget "
          "value negated (RZ is odd), for both directions", k5)
    RESULTS["searches"]["S-D"] = dict(stages=stage, hits=hits[:20], n_hits=len(hits))
    return hits


def pc3(choice):
    """PC3 / PC3b: latch calibration oracle through the S-D classifier."""
    phi, d = 0, 1
    x0 = choice[(phi, d)]
    gsite = (0, 1, 0)
    ell = (0, 0, 0)
    out = {}
    for inc in (1, 0):
        def run(flip):
            s = line_bg(phi)
            if flip:
                s = with_flip(s, (x0, x0 + 1))
            line = (s[0][:, OY, OY].copy(), s[1][:, OY, OY].copy())
            Nline = line_bg(phi)
            nl = (Nline[0][:, OY, OY].copy(), Nline[1][:, OY, OY].copy())
            g = [0, 0]
            hist = []
            yl_hist = []

            def full():
                P = np.zeros((LX, LY, LY), np.int64)
                Cc = P.copy()
                P[:, OY, OY], Cc[:, OY, OY] = line
                P[lidx(gsite)], Cc[lidx(gsite)] = g
                return P, Cc
            ref = []
            r_ = nl
            for t in range(4):
                ref.append(r_[1][OX])
                r_ = (r_[1], G(np.roll(r_[1], 1) + np.roll(r_[1], -1)) - r_[0])
            for t in range(T1 + TP + 1):
                P, Cc = full()
                hist.append((P, Cc))
                yl = int(line[1][OX])
                prev4 = yl_hist[t - 4] if t >= 4 else ref[t % 4]
                yl_hist.append(yl)
                delta = inc * int(yl != prev4)
                line = (line[1], G(np.roll(line[1], 1) + np.roll(line[1], -1)) - line[0])
                g = [g[1], g[0] + delta]
            return hist
        S, N = run(True), run(False)
        HA = np.stack([np.stack([p.reshape(-1)[AFLAT], c_.reshape(-1)[AFLAT]]) for p, c_ in S])
        N4 = np.stack([np.stack([p.reshape(-1)[AFLAT], c_.reshape(-1)[AFLAT]]) for p, c_ in N[:4]])
        rad = None
        for t, (p, c_) in enumerate(S):
            if (((p != 0) | (c_ != 0)) & ~ALLOWED).any():
                rad = t
                break
        lT = {t: np.stack([S[t][0].reshape(-1)[LFLAT], S[t][1].reshape(-1)[LFLAT]]) for t in (T1, T1 + TP)}
        lN = {t: np.stack([N[t][0].reshape(-1)[LFLAT], N[t][1].reshape(-1)[LFLAT]]) for t in (T1, T1 + TP)}
        st, r = classify_sd(HA, N4, rad, lT, lN)
        # L5: re-run in Q; the oracle is not Q
        L = line_ledger(phi, flip=(x0, x0 + 1))
        tr = q_run(*L.build(1), T1 + TP)
        q_agree = all(np.array_equal((C + S[t][1]) % q, tr[t][1]) for t in range(len(tr)))
        out[inc] = (st, q_agree)
    check("PC3 latch calibration oracle passes L1-L4 of the S-D classifier and is rejected by L5 "
          "(its run is not the Q run)", out[1][0] == "pass" and not out[1][1], str(out[1]))
    check("PC3b the oracle with the increment set to 0 fails at L4 (no record)", out[0][0] == "L4",
          str(out[0]))


def k4(choice):
    """K4: component independence (U2R A1) in Q on the S-D box."""
    rng = np.random.default_rng(3)
    phi = 0
    x0 = choice[(phi, 1)]
    s = with_flip(line_bg(phi), (x0, x0 + 1))
    P, Cc = (C + s[0]) % q, (C + s[1]) % q
    par_idx = np.indices((LX, LY, LY)).sum(axis=0) % 2      # index parity = coordinate parity
    P2, C2 = P.copy(), Cc.copy()
    other_c = par_idx == 1                                  # other component at t = 0: current slice on odd
    other_p = par_idx == 0
    C2[other_c] = rng.integers(0, q, int(other_c.sum()))
    P2[other_p] = rng.integers(0, q, int(other_p.sum()))
    ok = True
    for t in range(1, 13):
        P, Cc = q_step(P, Cc)
        P2, C2 = q_step(P2, C2)
        sig = (par_idx == t % 2)
        if not np.array_equal(Cc[sig], C2[sig]):
            ok = False
    check("K4 component independence in Q on the S-D box: randomizing the other component leaves "
          "the signal component unchanged for 12 ticks", ok)


# =============================================================== S-E (noise on Q, evidence)
def s_e():
    n, T = 32, 40
    out = {}
    ter = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
    for rho in (1e-3, 1e-2, 5e-2):
        for kap in ("full", "ternary"):
            rows = []
            for seed in range(3):
                rng = np.random.default_rng(1000 + seed)
                P = np.full((n, n, n), C, np.int64)
                Cc = P.copy()
                hitm = rng.random((n, n, n)) < rho
                k = int(hitm.sum())
                if kap == "full":
                    P[hitm] = rng.integers(0, q, k)
                    Cc[hitm] = rng.integers(0, q, k)
                else:
                    ch = rng.integers(0, 8, k)
                    P[hitm] = C + np.array([ter[i][0] for i in ch])
                    Cc[hitm] = C + np.array([ter[i][1] for i in ch])
                ever = np.zeros((n, n, n), bool)
                bgfrac = []
                for t in range(T + 1):
                    bgfrac.append(float(((P == C) & (Cc == C)).mean()))
                    ever |= np.abs(Cc - C) > 1
                    P, Cc = q_step(P, Cc)
                rows.append(dict(seed=seed, bg_t0=bgfrac[0], bg_t10=bgfrac[10], bg_t20=bgfrac[20],
                                 bg_t40=bgfrac[40], ever_out_of_ternary=float(ever.mean())))
            out[f"rho={rho},kappa={kap}"] = rows
            print(f"  S-E rho {rho} kappa {kap}: background fraction t=0/10/20/40 "
                  f"{[round(r['bg_t0'], 4) for r in rows]} / {[round(r['bg_t10'], 4) for r in rows]} / "
                  f"{[round(r['bg_t20'], 4) for r in rows]} / {[round(r['bg_t40'], 4) for r in rows]}; "
                  f"ever outside [c-1,c+1] {[round(r['ever_out_of_ternary'], 4) for r in rows]}", flush=True)
    RESULTS["searches"]["S-E"] = out
    return out


# =============================================================== Node 3 (cost and probability)
def ball_count(sites, T):
    """|B(S, T)| in Z^3 for a finite site set S (l1 ball), by enumeration."""
    pts = set()
    rng_ = range(-T, T + 1)
    for s in sites:
        for dx in rng_:
            r1 = T - abs(dx)
            for dy in range(-r1, r1 + 1):
                r2 = r1 - abs(dy)
                for dz in range(-r2, r2 + 1):
                    pts.add((s[0] + dx, s[1] + dy, s[2] + dz))
    return len(pts)


# =============================================================== verdict
def a02_inputs():
    """Structured outputs of the A02 run and the post hoc diagnostics, if present. They are produced
    after --search; on a re-run they are read from the record directory (post-review, B1)."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = {}
    for key, fn in (("sbl", "results-sb-long.json"), ("x1", "posthoc-sb.json"), ("x2", "posthoc-x2.json")):
        try:
            with open(os.path.join(base, fn)) as f:
                out[key] = json.load(f)
        except OSError:
            out[key] = None
    return out


def verdict(green, gem_i_hits, use_outside, node1_ok, a02):
    v = dict(controls_green=green)
    if not green:
        v["text"] = "VOID: a control failed; no verdict is rendered."
        return v
    gi = len(gem_i_hits) > 0
    gii = bool(use_outside and node1_ok)
    v.update(gem_i_preregistered_searches=gi, gem_ii_checks=gii, n_gem_i_candidates=len(gem_i_hits),
             use_outside_class_SB=use_outside)
    parts = []
    if gi:
        parts.append(f"gem (i) met in the preregistered searches: {len(gem_i_hits)} DT_A deliveries on Q "
                     "re-run in Q and ledger-audited ((i-cond))")
    else:
        parts.append("gem (i) not met in the preregistered searches, which did not evaluate DT_A "
                     "outside the carrier's class (S-B horizon 28)")
    sbl, x1, x2 = a02["sbl"], a02["x1"], a02["x2"]
    if sbl and x1 and x2:
        sm = sbl["summary"]
        nx1 = sum(1 for r in x1 if r["dta_t2_le_27"])
        naud = sum(1 for r in x2["rows"] if r["audit"])
        audok = x2["summary"]["audits_ok"]
        cost = RESULTS["searches"].get("A02-cost", {}).get("selection_cost_bits_best_rho_kappa_ternary")
        v.update(formal_icond_SBlong_DT_A=sm["dta"], SBlong_sample=sm["sample"],
                 SBlong_DT_s=sm["dts"], SBlong_DT_A_h=sm["dtah"], formal_icond_X1=nx1,
                 X1_examples=len(x1), ledger_audited=naud, ledger_audits_ok=audok)
        parts.append(f"PREREG §6 item 1 in its formal (i-cond) form: DT_A on Q (re-run in Q) is met by "
                     f"{sm['dta']} of {sm['sample']} S-B-long configurations (A02; DT_s {sm['dts']}, "
                     f"DT_A^h {sm['dtah']}) and by {nx1} of {len(x1)} X1 examples; the audit clause was "
                     f"checked on {naud} ({'ok' if audok else 'failed'}; it holds by construction for runs "
                     f"built from the ledger) and the cost clause on 1 ({cost} bits)")
    else:
        parts.append("A02 and post hoc outputs not present: the formal (i-cond) count is not evaluated")
    if gii:
        parts.append(f"gem (ii) checks hold (K1, K2, K2b green; use outside the carrier's class after a "
                     f"breach in at least {use_outside} S-B configurations); the obstruction itself rests "
                     "on the written proof of Lemma MQ1 / Theorem MQ2 in RESULT")
    else:
        parts.append("gem (ii) checks do not hold")
    v["text"] = "; ".join(parts) + "."
    return v


def cost_of(box_sites, w, T):
    """Lower bound on nu_{c,rho,kappa}(pattern on the box and every cone site at (c,c)) for kappa
    uniform on the pair alphabet: (rho 2^-32)^w (1-rho)^(|box| - w + cone); w counts the box sites
    whose pair (carrier slots at background) is not (c,c). Selection cost = -log2 of it."""
    cone = ball_count(box_sites, T) - len(box_sites)
    out = dict(box_sites=len(box_sites), pattern_sites=w, cone=cone, horizon=T)
    for rho in (Fraction(1, 100), Fraction(1, 1000)):
        lg = w * (math.log2(rho) - 32) + (len(box_sites) - w + cone) * math.log2(1 - rho)
        out[f"selection_cost_bits_rho_1/{rho.denominator}"] = round(-lg, 2)
        # informative: kappa concentrated on the 8 non-background ternary pairs (each 1/8); a
        # full-support kappa (1-l) kappa_ter + l u, l > 0 small, changes this by O(l)
        lt = w * (math.log2(rho) - 3) + (len(box_sites) - w + cone) * math.log2(1 - rho)
        out[f"selection_cost_bits_rho_1/{rho.denominator}_kappa_ternary"] = round(-lt, 2)
    M = len(box_sites) - w + cone
    rbest = Fraction(w, w + M)
    out["best_rho_kappa_ternary"] = str(rbest)
    out["selection_cost_bits_best_rho_kappa_ternary"] = round(
        -(w * (math.log2(rbest) - 3) + M * math.log2(1 - rbest)), 2)
    return out


def cost_of_fast(box_sites, w, T):
    """Post-review: cost_of with the cone counted on a grid (for large T), kappa on the ternary pairs."""
    pts = np.array(box_sites)
    g = np.indices((2 * T + 8,) * 3).reshape(3, -1).T - (T + 2)
    best = None
    for p in pts:
        d = np.abs(g - p).sum(axis=1)
        best = d if best is None else np.minimum(best, d)
    cone = int(((best >= 1) & (best <= T)).sum())
    M = len(box_sites) - w + cone
    out = dict(box_sites=len(box_sites), pattern_sites=w, cone=cone, horizon=T)
    for rho in (Fraction(1, 1000), Fraction(1, 10000)):
        lt = w * (math.log2(rho) - 3) + M * math.log2(1 - rho)
        out[f"selection_cost_bits_rho_1/{rho.denominator}_kappa_ternary"] = round(-lt, 1)
    rb = Fraction(w, w + M)
    out["best_rho_kappa_ternary"] = str(rb)
    out["selection_cost_bits_best_rho_kappa_ternary"] = round(
        -(w * (math.log2(rb) - 3) + M * math.log2(1 - rb)), 1)
    return out


def sd_l5(hit, choice):
    """L5 for an S-D candidate: re-run in Q itself, re-classify on the Q values, ledger audit."""
    phi, d = hit["phi"], hit["d"]
    x0 = choice[(phi, d)]
    gad = tuple((tuple(p), v) for p, v in hit["gadget"])
    L = line_ledger(phi, flip=(x0, x0 + 1), gadget=gad)
    tr = [q_run(*L.build(cv), T1 + TP) for cv in (0, 1)]
    aud = [L.audit(tr[cv], cv) for cv in (0, 1)]
    S = [((p - C + q // 2) % q - q // 2, (c_ - C + q // 2) % q - q // 2) for p, c_ in tr[1]]
    N = [((p - C + q // 2) % q - q // 2, (c_ - C + q // 2) % q - q // 2) for p, c_ in tr[0][:4]]
    HA = np.stack([np.stack([p.reshape(-1)[AFLAT], c_.reshape(-1)[AFLAT]]) for p, c_ in S])
    N4 = np.stack([np.stack([p.reshape(-1)[AFLAT], c_.reshape(-1)[AFLAT]]) for p, c_ in N])
    rad = None
    for t, (p, c_) in enumerate(S):
        if (((p != 0) | (c_ != 0)) & ~ALLOWED).any():
            rad = t
            break
    NN = [((p - C + q // 2) % q - q // 2, (c_ - C + q // 2) % q - q // 2) for p, c_ in tr[0]]
    lT = {t: np.stack([S[t][0].reshape(-1)[LFLAT], S[t][1].reshape(-1)[LFLAT]]) for t in (T1, T1 + TP)}
    lN = {t: np.stack([NN[t][0].reshape(-1)[LFLAT], NN[t][1].reshape(-1)[LFLAT]]) for t in (T1, T1 + TP)}
    st, r = classify_sd(HA, N4, rad, lT, lN)
    return st == "pass" and aud == ["ok", "ok"], dict(stage=st, dt=r, audit=aud, bits=L.bits())


def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, Fraction):
        return str(o)
    return o


CONTROLS = ["PC1", "PC2", "PC3", "PC3b", "CC1", "CC2", "CC3", "CC4", "CC5", "K0", "K1", "K2", "K3",
            "K4", "D1"]


def main():
    search = "--search" in sys.argv
    node1_checks()
    SA = s_a()
    rep, ok = s_a_q_reruns(SA)
    check("S-A re-run in Q: the minimum-weight DT_s delivery of every box (and every DT_A delivery, "
          "up to 50 per box) holds in Q itself and passes the ledger audit in both branches", ok,
          data={k: [dict(t2=x["hit"]["t2"], weight=x["hit"]["weight"], dta=x["hit"]["dta"],
                         q_dts=x["q"]["dts"], q_dta=x["q"]["dta"], audit=x["audit"]) for x in v]
                for k, v in rep.items()})
    costs = {}
    for k, v in rep.items():
        if v:
            h = v[0]["hit"]
            B = Box(tuple(h["dims"]))
            sites = [tuple(s) + (0,) * (3 - len(s)) for s in B.S]
            env = dict(zip(map(tuple, h["eslots"]), h["env"]))
            w = sum(1 for i in range(B.n) if env.get((0, i), 0) != 0 or env.get((1, i), 0) != 0)
            costs[k] = dict(hit=h, **cost_of(sites, w, h["t2"]))
    RESULTS["searches"]["S-A-cost"] = costs
    choice, k0ok = k0_launch()
    check("K0 W2 line: background 4-periodic at every phase; at every phase some launch pair gives a "
          "defect on at most 3 sites moving toward the origin; cells with no such pair are recorded "
          "as not launched (A01 item 2)", k0ok,
          data={f"{a}{b:+d}": v for (a, b), v in choice.items()})
    s_c(choice)
    cc2()
    cc1()
    pc3(choice)
    k4(choice)
    gem_i = [dict(source="S-A", box=k, **x) for k, v in rep.items() for x in v
             if x["hit"]["dta"] and x["q"]["dta"] and x["audit"] == ["ok", "ok"]]
    use_outside = 0
    if search:
        SB = s_b(SA)
        use_outside = SB["return_after_use"]
        hits = s_d(choice)
        l5 = []
        for h in hits:
            good, info = sd_l5(h, choice)
            l5.append(dict(hit=h, l5=good, **info))
            if good:
                gem_i.append(dict(source="S-D", **h, l5=info))
        RESULTS["searches"]["S-D"]["l5"] = l5[:20]
        s_e()
    ctl = CONTROLS + (["K5"] if search else [])         # K5 runs with --search (S-D)
    green = all(RESULTS["checks"][k]["ok"] for k in RESULTS["checks"] if k.split()[0] in ctl)
    missing = [k for k in ctl if not any(c.split()[0] == k for c in RESULTS["checks"])]
    if missing:
        green = False
        print("missing controls:", missing)
    node1_ok = all(RESULTS["checks"][k]["ok"] for k in RESULTS["checks"]
                   if k.split()[0] in ("K1", "K2", "K2b"))
    RESULTS["controls_green"] = green
    RESULTS["mode"] = "search" if search else "default"
    if search:
        a02 = a02_inputs()
        if a02["sbl"] and a02["x2"]:
            rows = [r for r in a02["sbl"]["rows"] if r["dtah"]]
            h = rows[0]["hit"]
            B = Box(tuple(h["dims"]))
            env = dict(zip(map(tuple, h["eslots"]), h["env"]))
            w = sum(1 for i in range(B.n) if env.get((0, i), 0) or env.get((1, i), 0))
            t2 = a02["x2"]["rows"][0]["t2"]
            sites = [tuple(s_) + (0,) * (3 - len(s_)) for s_ in B.S]
            # the record is read on A (l1-distance <= 8 from the box) up to tau2 + 60, so isolation
            # needs the background on the backward cone of radius tau2 + 60 + 8 around the box
            RESULTS["searches"]["A02-cost"] = dict(hit=h, tau2=t2, **cost_of_fast(sites, w, t2 + 60 + 8))
        RESULTS["verdict"] = verdict(green, gem_i, use_outside, node1_ok, a02)
        print("VERDICT:", RESULTS["verdict"]["text"])
    RESULTS["gem_i_candidates"] = gem_i[:20]
    allok = all(v["ok"] for v in RESULTS["checks"].values())
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fn = os.path.join(here, "results.json" if search else "results-default.json")
    with open(fn, "w") as f:
        json.dump(jsonable(RESULTS), f, indent=1, sort_keys=True)
    npass = sum(v["ok"] for v in RESULTS["checks"].values())
    print(f"{npass}/{len(RESULTS['checks'])} checks hold; controls green: {green}; wrote {fn}")
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
