"""Shards of the PE-01 computation. Each shard returns a deterministic measurement payload.

Shard ids:
  controls            EX1 (generators), EX4, EX5, EX6, IM1, IM2, IM4, IM5, AR and internal checks
  tape                the G_tape(K) mutant: NC-1/NC-2 for U and B1-B4 (K <= 20), P^emb(m <= 2,
                      active included; K <= 12) and IM6; SY on G_tape
  n<n>-<fam>          one degree n and family fam in {lin, filt, clk}: U, B1-B4, P^emb(m <= 2),
                      linear filters, randomized K0 (n <= 6), PC/NC/SY/EX/IM3 where they apply,
                      candidate witnesses
  n<n>-<fam>-m3       the passive m = 3 sweep for that (n, fam) (A1: its own shards)
"""
import math
import time
from fractions import Fraction

import numpy as np

from . import ar, bclasses as B, composite as Cm, embedded as E, generators as G, gf2, laws as LW, lc, lp
from . import observers as O, params as P, pending
from .exact import horizons, parse, q, rle, unrle

PROGRESS = None          # set by run.py: called after each completed block with (label, payload)


def progress(label, out):
    out.setdefault("completed_cells", []).append(label)
    if PROGRESS is not None:
        PROGRESS(label, out)

D8, D4 = Fraction(1, 8), Fraction(1, 4)
DELTAS = [D8, D4]
FAMS = ("lin", "filt", "clk")


def shard_ids():
    out = ["controls", "tape"]
    for n in P.NS:
        for f in FAMS:
            out.append("n%d-%s" % (n, f))
    for n in P.NS:
        for f in FAMS:
            out.append("n%d-%s-m3" % (n, f))
    return out


class Controls:
    def __init__(self):
        self.rec = {}

    def add(self, name, ok, detail=None):
        r = self.rec.setdefault(name, {"pass": True, "checks": 0, "failures": []})
        r["checks"] += 1
        if not ok:
            r["pass"] = False
            if len(r["failures"]) < 20:
                r["failures"].append(detail if detail is not None else "failed")
        return ok


def values_of(rec, key="values"):
    """Decode a run-length-encoded list of exact values."""
    return [parse(x) for x in unrle(rec[key])]


def curve_rec(curve, exact=None, arg=None):
    """An exact curve, losslessly run-length encoded, with its horizons and determined flags."""
    Ks = sorted(curve)
    rec = {"values": rle([q(curve[K]) for K in Ks]), "K_cap": Ks[-1]}
    rec["all_exact"] = exact is None or all(exact[K] for K in Ks)
    if exact is not None:
        rec["exact"] = rle([bool(exact[K]) for K in Ks])
    h = horizons(curve, DELTAS, exact)
    rec["K_zero"] = h["K_zero"]
    rec["K_zero_determined"] = h["K_zero_determined"]
    rec["K_delta"] = {"1/8": h["K_delta[1/8]"], "1/4": h["K_delta[1/4]"]}
    rec["K_delta_determined"] = {"1/8": h["K_delta_determined[1/8]"], "1/4": h["K_delta_determined[1/4]"]}
    if arg is not None:
        rec["argmax"] = rle([arg[K] for K in Ks])
    return rec


def k0_rec(d):
    """d: {K: {'value', 'exact', 'test', 'per_phi'}} -> serialized curve with tests."""
    Ks = sorted(d)
    cur = {K: d[K]["value"] for K in Ks}
    ex = {K: d[K]["exact"] for K in Ks}
    r = curve_rec(cur, ex)
    r["tests"] = rle([d[K]["test"] for K in Ks])
    r["per_phi"] = rle([None if d[K]["per_phi"] is None else [q(x) for x in d[K]["per_phi"]] for K in Ks])
    return r


def interval_rec(d, test=None):
    Ks = sorted(d)
    lo = {K: d[K][0] for K in Ks}
    hi = {K: d[K][1] for K in Ks}
    r = {"lower": curve_rec(lo), "upper": curve_rec(hi), "exact": rle([d[K][0] == d[K][1] for K in Ks])}
    if test is not None:
        r["lower"]["tests"] = rle([test if isinstance(test, str) else test(K) for K in Ks])
        r["lower"]["per_phi"] = rle([[q(x) for x in d[K][2]] for K in Ks])
    return r


def count_multiset(law, K):
    c = law.counts(K)
    vals, mult = np.unique(c, return_counts=True)
    return [[int(a), int(b)] for a, b in zip(vals, mult)]


def entropy_rec(law):
    out = {"count_multisets": [], "max_P": [], "display_H": [], "display_Hinf": []}
    for K in range(law.kcap + 1):
        ms = count_multiset(law, K)
        out["count_multisets"].append(ms)
        mx = max(a for a, _ in ms)
        out["max_P"].append(q(Fraction(mx, law.M)))
        out["display_Hinf"].append(round(math.log2(law.M / mx), 6))
        out["display_H"].append(round(-sum(b * (a / law.M) * math.log2(a / law.M) for a, b in ms), 6))
    return {k: rle(v) for k, v in out.items()}


# ================================================================== controls shard

def ex4_ex5(ctl, n, p):
    ok4 = gf2.order_of_z(p) == (1 << n) - 1
    ctl.add("EX4", ok4, "n=%d %s" % (n, gf2.poly_str(p)))
    L = G.companion_table(p, n)
    rows = []
    for i in range(n):
        # functional ell o L^i as a bitmask over h coordinates
        fn = 0
        for j in range(n):
            h = 1 << j
            for _ in range(i):
                h = int(L[h])
            if h & 1:
                fn |= 1 << j
        rows.append(fn)
    ctl.add("EX5", gf2.rank_int_rows(rows) == n, "n=%d %s" % (n, gf2.poly_str(p)))


def ex6(gen):
    """The exact one-step visible matrix under mu; T-level (C1) holds iff it is not a permutation."""
    T = np.zeros((2, 2), dtype=np.int64)
    tb = gen.phi_table()
    s = np.arange(gen.S)
    np.add.at(T, (s & 1, tb & 1), 1)
    rows = [[Fraction(int(T[x, y]), int(T[x].sum())) for y in (0, 1)] for x in (0, 1)]
    perm = all(sorted(r) == [0, 1] for r in rows)
    return rows, not perm


def im4(ctl, law, Kmax=10):
    b = B.B1(law, ktop=min(B.WHT_K, law.kcap))
    for K in range(min(Kmax, law.kcap) + 1):
        keys = B.record_keys(law.X, K)
        # production path: |W(T)| from the K = 23 transform, T subset of [0, K]
        prod = b.absW[: 1 << (K + 1)]
        T = np.arange(1 << (K + 1), dtype=np.int64)
        # direct: sum over seeds of (-1)^{T.r}
        par = B.parity_of(keys[None, :] & T[:, None])
        direct = np.abs((law.w[None, :] * (1 - 2 * par)).sum(axis=1))
        ctl.add("IM4", bool(np.array_equal(prod, direct)), "%s K=%d" % (law.gen.gid, K))


def im5(ctl, law):
    """Annihilator search vs brute-force polynomial search (K <= 5, d <= 2; K <= 3, d = 3)."""
    for d, Kb in ((1, 5), (2, 5), (3, 3)):
        for K in range(min(Kb, law.kcap) + 1):
            N = K + 1
            R = B.support_records(law, K)
            mons = B.monomials(N, d)
            pts = R.astype(np.int64)
            # evaluation of each monomial on the support (bitmask over support points) and on the cube
            cube = ((np.arange(1 << N)[:, None] >> np.arange(N)[None, :]) & 1).astype(np.int64)

            def masks(Pt):
                out = []
                for mo in mons:
                    v = np.ones(Pt.shape[0], dtype=np.int64)
                    for x in mo:
                        v &= Pt[:, x]
                    out.append(int((v << np.arange(Pt.shape[0], dtype=np.int64)).sum()) if Pt.shape[0] <= 62 else
                               sum(int(b) << i for i, b in enumerate(v.tolist())))
                return out
            ms, mc = masks(pts), masks(cube)
            ev = np.zeros(1, dtype=object if R.shape[0] > 62 else np.int64)
            evc = np.zeros(1, dtype=object if (1 << N) > 62 else np.int64)
            for a, c in zip(ms, mc):
                ev = np.concatenate([ev, ev ^ a])
                evc = np.concatenate([evc, evc ^ c])
            ann = np.flatnonzero(ev == 0)[1:]
            bdim = int(round(math.log2(len(ann) + 1))) if len(ann) else 0
            assert (1 << bdim) == len(ann) + 1
            bmax = max((bin(int(evc[i])).count("1") for i in ann), default=None)
            dim, bm = B.annihilator_space(R, N, d, need_basis=True)
            if dim is None:
                ok = False
            elif dim == 0:
                ok = bdim == 0
            else:
                basis, mons2 = bm
                mw = B.max_weight(basis, mons2, N, d, "dickson" if d <= 2 else "histogram")
                ok = bdim == dim and len(basis) == dim and bmax == mw
                if d <= 2 and N <= B.B4_D3_EXACT_N:
                    ok &= B.max_weight(basis, mons2, N, d, "histogram") == mw
            ctl.add("IM5", ok, "%s d=%d K=%d" % (law.gen.gid, d, K))


def dickson_selftest(ctl):
    import random
    rnd = random.Random(20261025)
    for N in range(1, 11):
        mons = B.monomials(N, 2)
        cube = [(x >> np.arange(N)) & 1 for x in range(1 << N)]
        for _ in range(60):
            c = rnd.getrandbits(len(mons))
            w = B.weight_quadratic(c, mons, N)
            cnt = 0
            for x in range(1 << N):
                v = 0
                for j, mo in enumerate(mons):
                    if (c >> j) & 1 and all((x >> i) & 1 for i in mo):
                        v ^= 1
                cnt += v
            ctl.add("IM5", cnt == w, "Dickson N=%d" % N)


def det_core_selftest(ctl):
    rs = np.random.RandomState(20261025)
    bad = 0
    for _ in range(200):
        F = rs.randint(1, 7)
        n = 40
        den = 16
        A = rs.randint(0, 9, size=(n, F)).astype(np.int64)
        bet = rs.randint(0, 9, size=n).astype(np.int64)
        r = rs.randint(0, den, size=n)
        r[rs.rand(n) < 0.2] = 0
        r[rs.rand(n) < 0.2] = den // 2
        first, I, base, cv = E.det_core(A, bet, 2 * r > den, r == 0)
        for i in range(n):
            vals = [abs(Fraction(int(A[i, j])) - int(bet[i]) - Fraction(int(r[i]), den)) for j in range(F)]
            tau = r[i] if first[i] else (0 if r[i] == 0 else den - r[i])
            if int(I[i]) + Fraction(int(tau), den) != min(vals) or int(base[i]) + int(cv[i]) * Fraction(int(r[i]), den) != sum(vals):
                bad += 1
    ctl.add("IM3", bad == 0, "det_core arithmetic: %d mismatches" % bad)


def _brute_tables(obs, gens, K):
    """Independent path: per (observer, phi) the counts C[v, x] after K rounds by scalar simulation,
    and q_K(v) by a Fraction recursion. Shares no code with embedded.Sweep."""
    V = obs.V
    out = {}
    for o in range(obs.n):
        R, A = obs.R[o], obs.Aact[o]
        qv = [Fraction(0)] * V
        qv[0] = Fraction(1)
        for _ in range(K):
            nq = [Fraction(0)] * V
            for v in range(V):
                for x in (0, 1):
                    nq[R[x, v]] += qv[v] / 2
            qv = nq
        for gi, g in enumerate(gens):
            C = [[0, 0] for _ in range(V)]
            for s0 in range(g.S):
                x, h, v = s0 & 1, s0 >> 1, 0
                for _ in range(K):
                    v = int(R[x, v])
                    c = x ^ int(A[v])
                    h = int(g.sig[c, h])
                    x = c ^ int(g.f[h])
                C[v][x] += 1
            out[(o, gi)] = (C, qv)
    return out


def _brute_windows(obs, gens, Kc, rows, M):
    """Window counts under both readings, for gens[0] and family-wide over all gens, by brute force:
    pr[(o, chi, gi)][K] = Pr[chi(v_K) = x_K] - 1/2."""
    V = obs.V
    pmh = {}
    for K in range(Kc + 1):
        tb = _brute_tables(obs, gens, K)
        for o in rows:
            for ch in range(1 << V):
                for gi in range(len(gens)):
                    C = tb[(o, gi)][0]
                    S_ = sum(C[v][(ch >> v) & 1] for v in range(V))
                    pmh.setdefault((o, ch, gi), []).append(Fraction(S_, M) - Fraction(1, 2))
    res = {}
    for K in range(3, Kc + 1):
        for rd in ("abs", "signed"):
            def ok(o, ch, gi):
                vals = pmh[(o, ch, gi)][K - 3:K + 1]
                return all((abs(x) if rd == "abs" else x) >= D8 for x in vals)
            cnt = sum(1 for o in rows for ch in range(1 << V) if ok(o, ch, 0))
            cf = sum(1 for o in rows for ch in range(1 << V) if all(ok(o, ch, gi) for gi in range(len(gens))))
            res[(rd, K)] = (cnt, cf)
    return res, pmh


def embedded_bruteforce(ctl, n, fam, m, Kc, nobs=None):
    """Exact-extraction cross-check against direct Fraction evaluation over every (observer, F):
    the sweep's K1 (distinguishing, prediction) and K0 (worst, average) maxima, and the window
    counts that decide condition (d) under both readings, for the primary and family-wide."""
    gens = G.family(fam, n)
    obs = O.all_observers(m)
    if nobs is not None:
        rs = np.random.RandomState(7)
        sel = np.zeros(obs.n, bool)
        sel[rs.choice(obs.n, nobs, replace=False)] = True
        sel[np.flatnonzero(obs.passive)[:nobs // 3]] = True
        obs = obs.subset(sel, "sample")
    subs = {"all": np.ones(obs.n, bool), "passive": obs.passive.copy()}
    sw = E.Sweep(obs, gens, [Kc] * len(gens), list(range(len(gens))), [0], Kc, "det", subs,
                 window_cap={0: Kc}, chunk=max(1, obs.n // 3)).run()
    M = gens[0].M
    V = obs.V
    bad = []
    for K in range(Kc + 1):
        tb = _brute_tables(obs, gens, K)
        dl = {k: [Fraction(C[v][x], M) - qv[v] / 2 for v in range(V) for x in (0, 1)] for k, (C, qv) in tb.items()}
        for sub, msk in subs.items():
            os_ = np.flatnonzero(msk)
            tv = max(sum(abs(d) for d in dl[(o, 0)]) / 2 for o in os_)
            pr = max(Fraction(sum(max(tb[(o, 0)][0][v]) for v in range(V)), M) - Fraction(1, 2) for o in os_)
            bw = Fraction(-1)
            ba = Fraction(-1)
            for o in os_:
                for Fm in range(1 << (2 * V)):
                    vals = [abs(sum(dl[(o, gi)][i] for i in range(2 * V) if (Fm >> i) & 1)) for gi in range(len(gens))]
                    bw = max(bw, min(vals))
                    ba = max(ba, sum(vals) / len(vals))
            num, _ = sw.k1d[(sub, 0)][K]
            pnum, _ = sw.k1p[(sub, 0)][K]
            w, a = sw.k0w[sub][K], sw.k0a[sub][K]
            if not (E.k1_dist_value(num, M, K) == tv and E.k1_pred_value(pnum, M) == pr
                    and Fraction(w[0], M * w[3]) == bw and Fraction(a[0], M * a[3] * len(gens)) == ba):
                bad.append(("K1/K0", sub, K))
    for sub, msk in subs.items():
        res, _ = _brute_windows(obs, gens, Kc, list(np.flatnonzero(msk)), M)
        for (rd, K), (cnt, cf) in res.items():
            rec = sw.win[(rd, sub, 0)].get(K, {"count": 0, "count_family": 0})
            if rec["count"] != cnt or rec["count_family"] != cf:
                bad.append(("window", rd, sub, K, cnt, rec["count"]))
    ctl.add("IM3", not bad, "exact extraction and windows vs brute force n=%d %s m=%d K<=%d: %s" % (n, fam, m, Kc, bad[:3]))


def pred_bruteforce(ctl, n, fam, obs, Kc, chi_k0, label):
    """The prediction path ('pred' K0, every-chi windows) against brute force: K1 prediction, the
    K0 worst and average maxima over chi_k0, and the window counts under both readings."""
    gens = G.family(fam, n)
    M = gens[0].M
    V = obs.V
    sw = E.Sweep(obs, gens, [Kc] * len(gens), list(range(len(gens))), [0], Kc, "pred",
                 {"s": np.ones(obs.n, bool)}, chi_k0=chi_k0, window_cap={0: Kc}, chunk=max(1, obs.n // 3)).run()
    chis = chi_k0 if chi_k0 is not None else list(range(1 << V))
    bad = []
    res, pmh = _brute_windows(obs, gens, Kc, list(range(obs.n)), M)
    for K in range(Kc + 1):
        best_p = max(max(pmh[(o, ch, 0)][K] for ch in range(1 << V)) for o in range(obs.n))
        bw = max(min(abs(pmh[(o, ch, gi)][K]) for gi in range(len(gens))) for o in range(obs.n) for ch in chis)
        ba = max(sum(abs(pmh[(o, ch, gi)][K]) for gi in range(len(gens))) / len(gens) for o in range(obs.n) for ch in chis)
        if E.k1_pred_value(sw.k1p[("s", 0)][K][0], M) != best_p:
            bad.append(("K1pred", K))
        if Fraction(sw.k0w["s"][K][0], 2 * M) != bw or Fraction(sw.k0a["s"][K][0], 2 * M * len(gens)) != ba:
            bad.append(("K0pred", K))
    for (rd, K), (cnt, cf) in res.items():
        rec = sw.win[(rd, "s", 0)].get(K, {"count": 0, "count_family": 0})
        if rec["count"] != cnt or rec["count_family"] != cf:
            bad.append(("window", rd, K, cnt, rec["count"]))
    ctl.add("IM3", not bad, "prediction path vs brute force %s n=%d %s K<=%d: %s" % (label, n, fam, Kc, bad[:3]))


def lp_selftest(ctl, n, fam, Ks):
    """The cutting-plane LP against the full game over every test (o, F), m = 1."""
    gens = G.family(fam, n)
    obs = O.all_observers(1)
    sw = E.Sweep(obs, gens, [max(Ks)] * len(gens), list(range(len(gens))), [0], max(Ks), "det",
                 {"all": np.ones(obs.n, bool)}, lp_cap=max(Ks)).run()
    M = gens[0].M
    for K in Ks:
        Cf, Z, den = lp_tables(sw, obs, K, M)
        for s in lp.sign_patterns(len(gens)):
            r = lp.randomized_k0(Cf, Z, den, M, s)
            Gm = []
            for o in range(obs.n):
                for Fm in range(1 << (2 * obs.V)):
                    Gm.append([s[f] * sum(Fraction(int(Cf[o, c, f]) * den - int(Z[o, c]), M * den)
                                          for c in range(2 * obs.V) if (Fm >> c) & 1) for f in range(len(gens))])
            v, _, _ = lp.solve_game(Gm)
            ctl.add("K0", v == r["value"], "LP vs full game n=%d %s K=%d s=%s" % (n, fam, K, s))


def lp_tables(sw, obs, K, M):
    chunks = sw.lpdata[K]
    Cf = np.concatenate([np.stack([c.reshape(len(idx), -1) for c in Cs], axis=2) for idx, Cs in chunks], axis=0)
    qc = E.QChain(obs.pair_tables())
    for _ in range(K):
        qc.advance()
    Qo = qc.Q[obs.pair]
    Z = np.repeat(Qo * M, 2, axis=1)
    return Cf, Z, 1 << (K + 1)


def shard_controls(mode, ctl):
    out = {}
    smoke = mode == "smoke"
    ns = (3, 4, 5) if smoke else P.NS
    fam_sizes = {}
    for n in P.NS:
        fam = gf2.primitive_polys(n)
        fam_sizes[n] = len(fam)
        ctl.add("EX4", len(fam) == gf2.euler_phi((1 << n) - 1) // n, "family count n=%d" % n)
        ctl.add("EX4", G.p_n(n) in fam and G.pr_n(n) in fam and gf2.reciprocal(G.p_n(n)) == G.pr_n(n), "p_n, p'_n n=%d" % n)
        for p in fam:
            ex4_ex5(ctl, n, p)
        gens = list(G.named(n).values()) + [G.make(f, n, p) for f in FAMS for p in fam]
        for g in gens:
            ctl.add("EX1", G.is_bijection(g.phi_table(), g.S), g.gid)
            ctl.add("EX2", int(g.seed_w.sum()) == g.S, "mu total %s" % g.gid)
        for nm, g in G.named(n).items():
            rows, c1 = ex6(g)
            want = nm != "G_dec"
            ctl.add("EX6", c1 == want, "%s n=%d" % (nm, n))
            out.setdefault("EX6", {})["%s/n%d" % (nm, n)] = {"matrix": [[q(x) for x in r] for r in rows], "C1": c1}
    out["family_sizes"] = fam_sizes
    # IM1, IM2
    r1 = lc.im1(12)
    ctl.add("IM1", r1["pass"], r1)
    nused = max(P.k_max(n) for n in ns) + 1
    r2 = lc.im2(nused, 20)
    ctl.add("IM2", r2["pass"], {k: v for k, v in r2.items() if k != "pass"})
    out["IM2"] = {"N_enumerated": 20, "N_dp": nused, "markov_premise": r2["markov_premise"]}
    # IM4, IM5 on the named generators
    for n in ns:
        for nm, g in G.named(n).items():
            law = LW.Law(g, min(P.k_max(n), 23))
            im4(ctl, law)
            im5(ctl, law)
    dickson_selftest(ctl)
    # AR
    plan = open(P.repo_root() + "/" + P.PLAN_PATH, encoding="utf-8").read()
    arr = ar.ar_check(plan)
    for n in P.NS:
        for nm in ("G_lin", "G_filt", "G_clk"):
            g = G.named(n)[nm]
            L = Cm.Layout(1, 0, g.H)
            e7 = Cm.ex7_prior(L, g, Cm.prior_dist(L, g))
            if not (e7["product"] and e7["h_uniform"] and e7["registers_fixed"]):
                arr["reasons"].append("prior assumption fails for %s n=%d" % (nm, n))
    arr["pass"] = not arr["reasons"]
    ctl.add("AR", arr["pass"], arr["reasons"])
    out["AR"] = arr
    progress("AR", out)
    # internal checks of the embedded machinery: the canonical m = 3 forms are complete (Hall's
    # counts per k), pairwise distinct, and each is a fixed point of an independent BFS relabelling
    hall = O.hall_subgroup_counts(8)
    forms = O.canonical_passive(8)
    from collections import Counter
    cnt = Counter(k for k, _ in forms)
    ctl.add("IM3", all(cnt[k] == hall[k] for k in range(1, 9)), "canonical m=3 forms vs Hall counts")
    keys = set()
    canon_ok = True
    for k, (r0, r1) in forms:
        keys.add((k, tuple(r0), tuple(r1)))
        lab, order = {0: 0}, [0]
        i = 0
        while i < len(order):
            st = order[i]
            for t in (r0[st], r1[st]):
                if t not in lab:
                    lab[t] = len(order)
                    order.append(t)
            i += 1
        if len(order) != k or any(lab[x] != x for x in range(k)):
            canon_ok = False
    ctl.add("IM3", len(keys) == len(forms), "canonical m=3 forms pairwise distinct")
    ctl.add("IM3", canon_ok, "canonical m=3 forms reachable and fixed by BFS relabelling")
    out["m3_canonical_forms"] = {str(k): cnt[k] for k in range(1, 9)}
    # FP on explicit clocked composites (never vacuous), against an independently written clock width
    g = G.named(4)["G_filt"]
    for m in (1, 2, 3, 4):
        V = 1 << m
        R = np.array([np.roll(np.arange(V), 1), np.arange(V)])
        for K in (0, 1, 3, 4, 7, 8, 15, 31):
            wt = Cm.Witness(g, m, R, [0] * V, [v & 1 for v in range(V)], K)
            ctl.add("FP", wt.L.footprint() == m + Cm.clock_bits_independent(K) + 1 and wt.L.S == len(wt.phi),
                    "composite m=%d K=%d" % (m, K))
            c = wt.checks()
            ctl.add("EX1", c["EX1"], "clocked composite m=%d K=%d" % (m, K))
            ctl.add("EX8", c["EX8"], "clocked composite m=%d K=%d" % (m, K))
            ctl.add("EX7", c["EX7"], "clocked composite m=%d K=%d" % (m, K))
            hits, out1, _ = wt.simulate()
            ctl.add("IM3", out1 == hits[K], "readout consistency m=%d K=%d" % (m, K))
    det_core_selftest(ctl)
    embedded_bruteforce(ctl, 3, "clk", 1, 8)
    embedded_bruteforce(ctl, 4, "filt", 1, 10)
    embedded_bruteforce(ctl, 4, "clk", 1, 14)
    embedded_bruteforce(ctl, 3, "lin", 2, 6, nobs=60)
    embedded_bruteforce(ctl, 4, "clk", 2, 9, nobs=60)
    pred_bruteforce(ctl, 3, "clk", O.linear_obsset(3), 10, O.linear_prediction_masks(3), "passive linear filters m=3")
    pred_bruteforce(ctl, 4, "filt", O.linear_obsset(2), 12, O.linear_prediction_masks(2), "passive linear filters m=2")
    o3 = O.passive_m3()
    rs = np.random.RandomState(3)
    sel = np.zeros(o3.n, bool)
    sel[rs.choice(o3.n, 40, replace=False)] = True
    pred_bruteforce(ctl, 3, "filt", o3.subset(sel, "sample"), 9, None, "passive m=3 sample")
    progress("embedded brute force", out)
    if not smoke:
        embedded_bruteforce(ctl, 5, "clk", 1, 12)
        lp_selftest(ctl, 3, "clk", [2, 3])
        lp_selftest(ctl, 5, "filt", [6, 10])
    else:
        lp_selftest(ctl, 3, "clk", [2, 3])
    return out


# ================================================================== the mutant

def bounded_all(law, K, ctl, tag):
    """All of U and B1-B4 on one law at exactly horizon K; each must be 0 (NC-1, NC-2 mutant)."""
    vals = {}
    c = law.counts(K)
    vals["U"] = LW.tv_uniform_from_counts(c, law.M, K + 1)
    tv, bay = LW.u_k1_curve(law)
    vals["U_bayes"] = bay[K]
    if K <= B.WHT_K:
        b = B.B1(law, ktop=K)
        absW = b.absW.copy()
        absW[0] = 0
        vals["B1"] = Fraction(int(absW.max()), 2 * law.M)
    LCP = lc.bm_profile_np(law.X[:, :K + 1])
    M = law.M
    N = K + 1
    cnt = np.zeros(N + 1, dtype=np.int64)
    np.add.at(cnt, LCP[:, K], law.w)
    cP = np.cumsum(cnt).tolist()
    cQ = 0
    b2 = Fraction(0)
    for lam in range(N + 1):
        cQ += lc.count_closed(N, lam)
        b2 = max(b2, Fraction(abs(cP[lam] * (1 << N) - cQ * M), M << N))
    vals["B2"] = b2
    o1, _, _ = B.b3_kwise([law], kcap=K)
    vals["B3k"] = o1[0][K]
    cw, _ = B.b3_window_k1(law)
    vals["B3w"] = cw[K]
    R = B.support_records(law, K)
    for d in (1, 2, 3):
        dim, _ = B.annihilator_space(R, N, d, need_basis=False)
        vals["B4d%d" % d] = Fraction(0) if dim == 0 else Fraction(1, 1 << d)
    for k, v in vals.items():
        ctl.add("NC", v == 0, "%s %s K=%d: %s" % (tag, k, K, v))
    return vals


def shard_tape(mode, ctl):
    smoke = mode == "smoke"
    ktape = 14 if smoke else P.K_TAPE
    kemb = 8 if smoke else P.K_TAPE_EMB
    out = {"K_tape": ktape, "K_tape_emb": kemb, "values": {}}
    for N in range(0, ktape + 1):
        g = G.tape(N)
        ctl.add("EX1", G.is_bijection(g.phi_table(), g.S), "tape(%d)" % N)
        law = LW.Law(g, N)
        ctl.add("EX2", int(law.counts(N).sum()) == law.M, "tape(%d) law total" % N)
        sy = LW.complement_invariant(g, N)
        ctl.add("SY", sy["pass"], "tape(%d)" % N)
        v = bounded_all(law, N, ctl, "tape(%d)" % N)
        out["values"][str(N)] = {k: q(x) for k, x in v.items()}
    # P^emb(m <= 2), active included, K <= 12: P_p = Q_p exactly for every observer (NC-1, IM6)
    obs_sets = [O.all_observers(1), O.all_observers(2)]
    for K in range(0, kemb + 1):
        g = G.tape(K)
        for obs in obs_sets:
            sw = E.Sim(obs, np.arange(obs.n), [g], [K]) if obs.n <= 16 else None
            ok = True
            for st in range(0, obs.n, 1024 if K >= 10 else 4096):
                idx = np.arange(st, min(obs.n, st + (1024 if K >= 10 else 4096)))
                sim = E.Sim(obs, idx, [g], [K])
                for _ in range(K):
                    sim.step()
                C = sim.counts(0)
                qc = E.QChain(obs.R[idx])
                for _ in range(K):
                    qc.advance()
                # P(v, x) = C / M equals Q(v, x) = Q_K(v) / 2^(K+1) for every cell
                lhs = C.astype(object) * (1 << (K + 1))
                rhs = (qc.Q * g.M)[:, :, None]
                ok &= bool((lhs == rhs).all())
            ctl.add("IM6", ok, "tape(%d) m=%d" % (K, obs.m))
            ctl.add("NC", ok, "tape(%d) P^emb m=%d" % (K, obs.m))
    return out


# ================================================================== (n, family) shard

def named_for(n, fam):
    nd = G.named(n)
    famlist = G.family(fam, n)
    p = G.p_n(n)
    prim = next(i for i, g in enumerate(famlist) if g.p == p)
    famlist[prim].name = {"lin": "G_lin", "filt": "G_filt", "clk": "G_clk"}[fam]
    extra = []
    sib = None
    if fam == "lin":
        sib = next(i for i, g in enumerate(famlist) if g.p == G.pr_n(n))
        famlist[sib].name = "G_lin_sib"
        extra = [nd["G_dec"]]
    return famlist, prim, sib, extra


def shard_family(n, fam, mode, ctl, timing):
    smoke = mode == "smoke"
    kmax = P.k_max(n)
    famlist, prim, sib, extra = named_for(n, fam)
    allg = famlist + extra
    named_idx = [prim] + ([sib] if sib is not None else []) + list(range(len(famlist), len(allg)))
    out = {"n": n, "family": fam, "K_max": kmax, "generators": [g.desc() for g in allg], "family_size": len(famlist),
           "primary": prim, "named": {allg[i].name: allg[i].gid for i in named_idx}, "classes": {}, "k0": {},
           "witnesses": []}
    t0 = time.time()
    laws = [LW.Law(g, kmax) for g in allg]
    for g, law in zip(allg, laws):
        ctl.add("EX1", G.is_bijection(g.phi_table(), g.S), g.gid)
        for K in range(kmax + 1):
            if int(law.counts(K).sum()) != law.M:
                ctl.add("EX2", False, "%s K=%d" % (g.gid, K))
        ctl.add("EX2", True)
        if fam in ("lin", "filt") or g.family == "dec":
            sy = LW.complement_invariant(g, kmax)
            ctl.add("SY", sy["pass"], "%s %s" % (g.gid, sy["failing_K"]))
    timing["laws"] = time.time() - t0
    cls = out["classes"]

    def put(cname, gi, rec):
        cls.setdefault(cname, {})[allg[gi].name if gi in named_idx else allg[gi].gid] = rec

    # ---------------- U
    t0 = time.time()
    tvs = []
    for gi, law in enumerate(laws):
        tv, bay = LW.u_k1_curve(law)
        tvs.append(tv)
        if gi in named_idx:
            put("U", gi, curve_rec(tv))
            put("U_bayes", gi, curve_rec(bay))
            out.setdefault("entropy", {})[allg[gi].name] = entropy_rec(law)
    worst, avg = LW.u_k0([laws[i] for i in range(len(famlist))], tvs[:len(famlist)])
    out["k0"]["U"] = {"worst": interval_rec(worst, "D_union"), "average": interval_rec(avg),
                      "test_worst": "D_union", "family_size": len(famlist)}
    timing["U"] = time.time() - t0

    # ---------------- B1
    t0 = time.time()
    named_b1 = {gi: None for gi in named_idx if gi < len(famlist)}
    w, a = B.b1_k0(laws[:len(famlist)], named_b1)
    for gi in named_idx:
        c, ex, arg, _ = named_b1[gi] if gi in named_b1 else B.b1_curve(laws[gi])
        put("B1", gi, curve_rec(c, ex, {K: arg[K] for K in arg}))
    out["k0"]["B1"] = {"worst": k0_rec(w), "average": k0_rec(a)}
    timing["B1"] = time.time() - t0

    # ---------------- B2
    t0 = time.time()
    tabs = []
    for gi, law in enumerate(laws):
        tab, _ = B.b2_tables(law)
        tabs.append(tab)
        if gi in named_idx:
            k1, arg = B.b2_k1(tab, law.M)
            rec = curve_rec(k1, None, arg)
            lam = n + 1
            rec["lambda_n_plus_1"] = rle([q(Fraction(tab[K][lam], B.b2_den(law.M, K))) if lam <= K + 1 else "0"
                                          for K in range(kmax + 1)])
            rec["lambda_1"] = rle([q(Fraction(tab[K][1], B.b2_den(law.M, K))) for K in range(kmax + 1)])
            put("B2", gi, rec)
    w, a = B.b2_k0(tabs[:len(famlist)], laws[0].M)
    out["k0"]["B2"] = {"worst": k0_rec(w), "average": k0_rec(a)}
    timing["B2"] = time.time() - t0

    progress("U, B1, B2", out)
    # ---------------- B3
    t0 = time.time()
    o1, w, a = B.b3_kwise(laws[:len(famlist)])
    for gi in named_idx:
        if gi < len(famlist):
            put("B3k", gi, curve_rec(o1[gi]))
    for gi in range(len(famlist), len(allg)):
        o1e, _, _ = B.b3_kwise([laws[gi]])
        put("B3k", gi, curve_rec(o1e[0]))
    out["k0"]["B3k"] = {"worst": k0_rec(w), "average": k0_rec(a)}
    for gi in named_idx:
        cw, aw = B.b3_window_k1(laws[gi])
        put("B3w", gi, curve_rec(cw, None, {K: list(aw[K]) if aw[K] else None for K in aw}))
    # B3 window K0 (open item B3W-K0): exact average by stationarity; worst exact for w <= 4, else interval
    bw = B.b3_window_k0(laws[:len(famlist)])
    ctl.add("K0", bw["stationary"], "B3 window marginals stationary (every window of each length)")
    for w_, r in bw["per_w"].items():
        if "avg_brute" in r:
            ctl.add("K0", r["avg"] == r["avg_brute"], "B3 window average: sign patterns = all tests, w=%d" % w_)
    wst = {}
    for K, (lo, hi, per, test) in bw["worst"].items():
        if per is None:
            per = [lo] * len(famlist)   # D_union on a window: P_phi(U) = 1 for every phi
        wst[K] = (lo, hi, per, test)
    out["k0"]["B3w"] = {"average": k0_rec(bw["average"]), "worst": interval_rec(wst, lambda K: wst[K][3]),
                        "stationary": bw["stationary"], "open_item": "B3W-K0"}
    timing["B3"] = time.time() - t0
    progress("B3", out)

    # ---------------- B4 (the class grows with d: a bound at d is improved by the values at d' < d)
    t0 = time.time()
    b4v = {}
    for d in (1, 2, 3):
        for gi in named_idx:
            law = laws[gi]
            cur, kf = B.b4_curve(lambda K, law=law: B.support_records(law, K), law.kcap, d)
            vals = {K: cur[K]["value"] for K in cur}
            ex = {K: cur[K]["exact"] for K in cur}
            if d > 1:
                prev = b4v[(gi, d - 1)]
                for K in vals:
                    if not ex[K] and K in prev and prev[K] > vals[K]:
                        vals[K] = prev[K]
            b4v[(gi, d)] = vals
            rec = curve_rec(vals, ex)
            rec["K_first"] = kf
            rec["dim"] = rle([cur[K]["dim"] for K in sorted(cur)])
            rec["counting_horizon"] = B.b4_counting_horizon(n, d)
            put("B4d%d" % d, gi, rec)
            if d > 1:
                pe = cls["B4d%d" % (d - 1)][allg[gi].name]
                pex = unrle(pe["exact"])
                pv = values_of(pe)
                ctl.add("MO", all(pv[K] <= vals[K] for K in range(min(len(pv), len(vals))) if pex[K] and ex[K]),
                        "B4 d=%d <= d=%d on %s" % (d - 1, d, allg[gi].name))
        flaws = laws[:len(famlist)]
        cur, kf = B.b4_curve(lambda K: B.union_records(flaws, K), kmax, d)
        vals = {K: cur[K]["value"] for K in cur}
        ex = {K: cur[K]["exact"] for K in cur}
        rec = curve_rec(vals, ex)
        rec["K_first"] = kf
        rec["counting_horizon"] = B.b4_counting_horizon(n, d)
        rec["test"] = "q annihilating the union of supports (the same adv on every phi)"
        out["k0"]["B4d%d" % d] = {"worst": rec, "average": rec}
    timing["B4"] = time.time() - t0
    progress("B4", out)

    # ---------------- P^emb(m <= 2)
    k0c = min(P.K0_CAP_M2, kmax)
    kcap1 = [kmax if gi in named_idx else 0 for gi in range(len(allg))]
    fam_idx = list(range(len(famlist)))
    kcx = ar.kcx_of(allg[prim])[0]
    lpcap = P.k_lp(n) if (n in P.LP_NS and not smoke) else -1
    out["K_cx"] = kcx
    im3 = Cm.FullState if n <= 4 else None
    for m in (1, 2):
        t0 = time.time()
        obs = O.all_observers(m)
        if smoke:
            obs = obs.subset(obs.passive, "emb_m%d_passive" % m)
            subs = {"passive": np.ones(obs.n, bool)}
        else:
            subs = {"all": np.ones(obs.n, bool), "passive": obs.passive.copy()}
        if n <= 4:
            for g in allg:
                Lp = Cm.Layout(m, 0, g.H)
                ctl.add("EX7", Cm.ex7_prior(Lp, g, Cm.prior_dist(Lp, g))["pass"], "prior m=%d %s" % (m, g.gid))
                e1, e8 = Cm.exhaustive_maps(obs, g)
                ctl.add("EX1", e1, "composites m=%d %s" % (m, g.gid))
                ctl.add("EX8", e8, "composites m=%d %s" % (m, g.gid))
            r1, r8 = Cm.exhaustive_readout(m, allg[prim], range(1 << (2 * obs.V)), K=3)
            ctl.add("EX1", r1, "readout m=%d" % m)
            ctl.add("EX8", r8, "readout m=%d" % m)
        sw = E.Sweep(obs, allg, kcap1, fam_idx, [prim], k0c, "det", subs,
                     window_cap={prim: kmax}, lp_cap=lpcap, chunk=2048, im3=im3).run()
        ctl.add("EX2", sw.ex2_q, "Q_p sums m=%d" % m)
        if im3 is not None:
            ctl.add("IM3", sw.im3_ok, "m=%d n=%d %s %s" % (m, n, fam, sw.im3_fail[:3]))
        M = allg[0].M
        for s_ in subs:
            cname = "emb_m%d_%s" % (m, s_)
            for gi in named_idx:
                d = {K: E.k1_dist_value(v[0], M, K) for K, v in sw.k1d[(s_, gi)].items()}
                pr = {K: E.k1_pred_value(v[0], M) for K, v in sw.k1p[(s_, gi)].items()}
                put(cname, gi, curve_rec(d, None, {K: v[1] for K, v in sw.k1d[(s_, gi)].items()}))
                put(cname + "_pred", gi, curve_rec(pr, None, {K: v[1] for K, v in sw.k1p[(s_, gi)].items()}))
            kw, ka = {}, {}
            for K, (num, o, f, den) in sw.k0w[s_].items():
                kw[K] = {"value": Fraction(num, M * den), "exact": True, "test": "o=%d,F=%d" % (o, f),
                         "per_phi": test_per_phi(obs, o, f, allg[:len(famlist)], K)}
            for K, (num, o, f, den) in sw.k0a[s_].items():
                ka[K] = {"value": Fraction(num, M * den * len(famlist)), "exact": True, "test": "o=%d,F=%d" % (o, f),
                         "per_phi": test_per_phi(obs, o, f, allg[:len(famlist)], K)}
            out["k0"][cname] = {"worst": k0_rec(kw), "average": k0_rec(ka), "worst_is_lower_bound_of_randomized": True}
            out.setdefault("windows", {})[cname] = window_summary(sw, s_, prim)
            out["witnesses"].extend(witnesses_from(sw, s_, obs, cname, m, allg, prim, famlist, kcx, ctl))
        if lpcap >= 0:
            out["k0"]["emb_m%d_all" % m]["randomized"] = randomized(sw, obs, lpcap, M, len(famlist))
        timing["emb_m%d" % m] = time.time() - t0
        progress("emb m=%d" % m, out)

    # ---------------- passive linear filters (open item LF-A: a = 0)
    if not smoke:
        for m in (1, 2, 3, 4):
            t0 = time.time()
            obs = O.linear_obsset(m)
            masks = O.linear_prediction_masks(m)
            sw = E.Sweep(obs, allg, [kmax if gi in named_idx else 0 for gi in range(len(allg))],
                         fam_idx, [prim], kmax, "pred", {"passive_linear": np.ones(obs.n, bool)}, chi_k0=masks,
                         window_cap={prim: kmax}, chunk=obs.n, im3=im3).run()
            ctl.add("EX2", sw.ex2_q, "Q_p sums passive linear m=%d" % m)
            if im3 is not None:
                ctl.add("IM3", sw.im3_ok, "passive linear m=%d n=%d %s %s" % (m, n, fam, sw.im3_fail[:3]))
            M = allg[0].M
            cname = "plin_m%d" % m
            for gi in named_idx:
                d = {K: E.k1_dist_value(v[0], M, K) for K, v in sw.k1d[("passive_linear", gi)].items()}
                pr = {K: E.k1_pred_value(v[0], M) for K, v in sw.k1p[("passive_linear", gi)].items()}
                put(cname, gi, curve_rec(d, None, {K: obs.labels[v[1]] for K, v in sw.k1d[("passive_linear", gi)].items()}))
                put(cname + "_pred", gi, curve_rec(pr, None, {K: obs.labels[v[1]] for K, v in sw.k1p[("passive_linear", gi)].items()}))
            out["k0"][cname] = {"worst": k0_pred_rec(sw.k0w["passive_linear"], M, len(famlist), False, obs, masks),
                                "average": k0_pred_rec(sw.k0a["passive_linear"], M, len(famlist), True, obs, masks),
                                "test_class": "linear prediction tests chi(v) = c.v + e",
                                "scope": "passive linear filters (a = 0; open item LF-A)"}
            out.setdefault("windows", {})[cname] = window_summary(sw, "passive_linear", prim)
            out["witnesses"].extend(witnesses_from(sw, "passive_linear", obs, cname, m, allg, prim, famlist, kcx, ctl))
            if n <= 4:
                full = O.linear_obsset(m, full=True)
                for g in allg:
                    e1, e8 = Cm.exhaustive_maps(full, g)
                    ctl.add("EX1", e1, "passive linear composites m=%d %s" % (m, g.gid))
                    ctl.add("EX8", e8, "passive linear composites m=%d %s" % (m, g.gid))
                linear_reduction_check(ctl, full, obs, allg, kmax, masks, n, m)
                if m >= 3:
                    V = 1 << m
                    Fs = range(1 << (2 * V)) if m == 3 else \
                        [sum(1 << (2 * v + ((ch >> v) & 1)) for v in range(V)) for ch in range(1 << V)]
                    r1, r8 = Cm.exhaustive_readout(m, allg[prim], Fs, K=3)
                    ctl.add("EX1", r1, "readout passive linear m=%d" % m)
                    ctl.add("EX8", r8, "readout passive linear m=%d" % m)
            timing[cname] = time.time() - t0
            progress("passive linear m=%d" % m, out)
    else:
        out["smoke_scope"] = "passive observers m <= 2 only; no active observers, passive linear filters or LP"
    shard_curve_controls(ctl, out, n, fam, laws, allg, prim, sib)
    out["tags_input"] = tags_input(out, n, fam, allg, prim, sib)
    return out


def test_per_phi(obs, o, f, gens, K):
    """Exact |Delta_phi| of test (o, F) for every phi of the family (the K0 checkpoint), by a
    separate single-observer simulation and a Fraction Q recursion."""
    V = obs.V
    R, A = obs.R[o], obs.Aact[o]
    qv = [Fraction(0)] * V
    qv[0] = Fraction(1)
    for _ in range(K):
        nq = [Fraction(0)] * V
        for v in range(V):
            for x in (0, 1):
                nq[R[x, v]] += qv[v] / 2
        qv = nq
    out = []
    for g in gens:
        sim = E.Sim(obs, np.array([o]), [g], [K])
        for _ in range(K):
            sim.step()
        C = sim.counts(0)[0]
        tot = Fraction(0)
        for c in range(2 * V):
            if (f >> c) & 1:
                v, x = divmod(c, 2)
                tot += Fraction(int(C[v, x]), g.M) - qv[v] / 2
        out.append(abs(tot))
    return out


def k0_pred_rec(d, M, F, average, obs, masks):
    out = {}
    for K, (num, o, ch, per) in d.items():
        val = Fraction(num, 2 * M * (F if average else 1))
        out[K] = {"value": val, "exact": True,
                  "test": "o=%s,chi=%d" % (obs.labels[o] if obs.labels else o, masks[ch] if masks else ch),
                  "per_phi": [Fraction(x, 2 * M) for x in per]}
    return k0_rec(out)


def window_summary(sw, sub, prim):
    """Per reading of (d): for every K with a window, [K, count, count_family, family_checked,
    first, first_family, count per family member]."""
    out = {}
    for rd in E.READINGS:
        rows = []
        for K, r in sorted(sw.win[(rd, sub, prim)].items()):
            if r["count"] or any(r["count_member"]):
                rows.append([K, r["count"], r["count_family"], r["family_checked"], r["first"], r["first_family"],
                             r["count_member"]])
        out[rd] = rows
    return out


def randomized(sw, obs, lpcap, M, F):
    res = {"K_LP": lpcap, "values": [], "all_positive": [], "patterns": [], "tests": []}
    for K in range(lpcap + 1):
        Cf, Z, den = lp_tables(sw, obs, K, M)
        best = None
        allpos = None
        for s in lp.sign_patterns(F):
            r = lp.randomized_k0(Cf, Z, den, M, s)
            if allpos is None:
                allpos = r["value"]
            if best is None or r["value"] > best[0]:
                best = (r["value"], s, r)
        res["values"].append(q(best[0]))
        res["all_positive"].append(q(allpos))
        res["patterns"].append(best[1])
        res["tests"].append({"pi": [q(x) for x in best[2]["pi"]],
                             "mixed": [[o, Fm, q(wt)] for o, Fm, wt in best[2]["mixed"]]})
    return {k: (rle(v) if k != "K_LP" else v) for k, v in res.items()}


def witnesses_from(sw, sub, obs, cname, m, allg, prim, famlist, kcx, ctl):
    """Candidate witnesses, per reading of (d): the least window K, the largest window K <= K_cx,
    and the least window K > K_cx. (c) and (f) both hold for small K only (the footprint is
    non-decreasing in K), so these decide the COUNTEREXAMPLE test and the attribution rule for the
    combination. Where a family-wide window exists, its first (O, chi) is a candidate as well."""
    picks = []
    for rd in E.READINGS:
        win = {K: r for K, r in sw.win[(rd, sub, prim)].items() if r["count"]}
        Ks = sorted(win)
        if not Ks:
            continue
        sel = {Ks[0]}
        le = [K for K in Ks if K <= kcx]
        gt = [K for K in Ks if K > kcx]
        if le:
            sel.add(le[-1])
        if gt:
            sel.add(gt[0])
        for K in sorted(sel):
            picks.append((rd, K, win[K]["first"], win[K]))
        fam = [K for K in Ks if win[K]["count_family"]]
        if fam:
            picks.append((rd, fam[0], win[fam[0]]["first_family"], win[fam[0]]))
    out = []
    seen = set()
    for rd, K, (o, ch), r in picks:
        if (o, ch, K) in seen:
            for w in out:
                if (w["observer"]["index"], w["observer"]["chi_index"], w["K"]) == (o, ch, K):
                    w["found_under"] = sorted(set(w["found_under"]) | {rd})
            continue
        seen.add((o, ch, K))
        w = build_witness(obs, o, ch, K, cname, m, allg, prim, famlist, kcx, ctl)
        w["found_under"] = [rd]
        w["window_count_in_subclass"] = {rd2: sw.win[(rd2, sub, prim)].get(K, {"count": 0})["count"] for rd2 in E.READINGS}
        w["family_window_count"] = {rd2: sw.win[(rd2, sub, prim)].get(K, {"count_family": 0})["count_family"] for rd2 in E.READINGS}
        out.append(w)
    return out


def chi_table(ch, V):
    return [(ch >> v) & 1 for v in range(V)]


def build_witness(obs, o, ch, K, cname, m, allg, prim, famlist, kcx, ctl):
    g = allg[prim]
    V = obs.V
    tabs = obs.tables(o)
    R = np.array([tabs[0], tabs[1]])
    a = tabs[2]
    chi = chi_table(ch, V)
    wt = Cm.Witness(g, m, R, a, chi, K)
    chk = wt.checks()
    hits, out1, M = wt.simulate()
    # aggregated path (IM3 for the witness): the same O and chi through embedded.Sim
    agg = []
    sim = E.Sim(obs, np.array([o]), [g], [K])
    for t in range(K + 1):
        C = sim.counts(0)[0]
        agg.append(int(sum(C[v, chi[v]] for v in range(V))))
        if t < K:
            sim.step()
    window = list(range(K - 3, K + 1))
    pmh = [Fraction(hits[t], M) - Fraction(1, 2) for t in window]
    adv_agg = [abs(Fraction(agg[t], M) - Fraction(1, 2)) for t in window]
    readout_ok = out1 == hits[K]
    im3 = [abs(x) for x in pmh] == adv_agg and readout_ok and hits == agg
    # K0 status under both readings: the same O and chi on every phi of the family
    k0 = {"abs": True, "signed": True}
    for f in famlist:
        sim = E.Sim(obs, np.array([o]), [f], [K])
        vals = []
        for t in range(K + 1):
            C = sim.counts(0)[0]
            vals.append(Fraction(int(sum(C[v, chi[v]] for v in range(V))), f.M) - Fraction(1, 2))
            if t < K:
                sim.step()
        k0["abs"] &= all(abs(vals[t]) >= D8 for t in window)
        k0["signed"] &= all(vals[t] >= D8 for t in window)
    rows, c1 = ex6(g)
    fp = wt.L.footprint()
    rec = {
        "generator": g.name, "generator_id": g.gid, "family": g.family, "n": g.n, "subclass": cname, "m": m,
        "observer": {"rho0": tabs[0], "rho1": tabs[1], "a": a, "chi": chi, "chi_index": int(ch), "F": "graph of chi",
                     "index": int(o), "label": obs.labels[o] if obs.labels else None},
        "K": K, "window": window, "adv_pred": [q(abs(x)) for x in pmh], "pred_minus_half": [q(x) for x in pmh],
        "adv_pred_aggregated": [q(x) for x in adv_agg],
        "window_note": "values at K' < K read from the K-clocked composite's (v, x) registers; the readout "
                       "changes only the output register",
        "K_cx": kcx, "footprint": fp, "footprint_formula": m + Cm.clock_bits_independent(K) + 1,
        "clock_bits": wt.c, "table_size_bits": wt.table_size_bits(), "EX6": c1,
        "EX1": chk["EX1"], "EX7": chk["EX7"], "EX8": chk["EX8"], "IM3": im3, "readout_consistent": readout_ok,
        "K0_status": k0,
        "realization": "T-level (C1) %s; C2-C4 not checked" % ("holds" if c1 else "fails"),
    }
    ctl.add("FP", fp == m + Cm.clock_bits_independent(K) + 1, "witness %s %s K=%d" % (g.gid, cname, K))
    ctl.add("EX1", chk["EX1"], "witness %s K=%d" % (cname, K))
    ctl.add("EX8", chk["EX8"], "witness %s K=%d" % (cname, K))
    ctl.add("EX7", chk["EX7"], "witness %s K=%d" % (cname, K))
    ctl.add("IM3", im3, "witness %s K=%d" % (cname, K))
    return rec


def linear_reduction_check(ctl, full, reps, allg, kmax, masks, n, m):
    """The class reduction of passive linear filters, per observer (n <= 4): at every K, every (A, b)
    has the same multiset of cells (C[v,0], C[v,1], Q_K(v)) as its class representative, and the
    same multiset of linear-prediction hit counts."""
    rep_of = {lab: i for i, lab in enumerate(reps.labels)}
    rmap = np.array([rep_of[lab] for lab in full.labels])
    bad = 0
    for g in allg:
        simr = E.Sim(reps, np.arange(reps.n), [g], [kmax])
        qr = E.QChain(reps.R)
        reps_keys = []
        for K in range(kmax + 1):
            reps_keys.append(_lin_keys(simr.counts(0), qr.Q, masks))
            if K < kmax:
                simr.step()
                qr.advance()
        for st in range(0, full.n, 16384):
            idx = np.arange(st, min(full.n, st + 16384))
            sim = E.Sim(full, idx, [g], [kmax])
            qc = E.QChain(full.R[idx])
            for K in range(kmax + 1):
                cell_k, pred_k = _lin_keys(sim.counts(0), qc.Q, masks)
                rc, rp = reps_keys[K]
                if not (np.array_equal(cell_k, rc[rmap[idx]]) and np.array_equal(pred_k, rp[rmap[idx]])):
                    bad += 1
                if K < kmax:
                    sim.step()
                    qc.advance()
    ctl.add("IM3", bad == 0, "passive linear filters: per-observer class reduction m=%d n=%d (%d mismatches)" % (m, n, bad))


def _lin_keys(C, Q, masks):
    """Sorted cell triples and sorted linear-prediction hit counts per observer (K <= 60: int64)."""
    Qi = np.array(Q.tolist(), dtype=np.int64)
    cells = np.stack([C[:, :, 0], C[:, :, 1], Qi], axis=2)          # (o, V, 3)
    key = (cells[:, :, 0] * 4096 + cells[:, :, 1]) * (1 << 40) + cells[:, :, 2]
    cell_k = np.sort(key, axis=1)
    V = C.shape[1]
    base = C[:, :, 0].sum(axis=1)[:, None]
    bits = np.array([[(mk >> v) & 1 for mk in masks] for v in range(V)], dtype=np.int64)   # (V, nmasks)
    ss = (C[:, :, 1] - C[:, :, 0]) @ bits + base
    pred_k = np.sort(ss, axis=1)
    return cell_k, pred_k


K1_OF_K0 = {"U": "U", "B1": "B1", "B2": "B2", "B3k": "B3k", "B3w": "B3w", "B4d1": "B4d1", "B4d2": "B4d2",
            "B4d3": "B4d3", "emb_m1_all": "emb_m1_all", "emb_m1_passive": "emb_m1_passive",
            "emb_m2_all": "emb_m2_all", "emb_m2_passive": "emb_m2_passive", "emb_m3_passive": "emb_m3_passive_pred",
            "plin_m1": "plin_m1_pred", "plin_m2": "plin_m2_pred", "plin_m3": "plin_m3_pred", "plin_m4": "plin_m4_pred"}


def k0_vs_k1(ctl, out, famlist, named_fam):
    """MO, K0 <= K1 pointwise: each K0 test's value on phi is at most phi's K1 value, and the K0 value
    is at most min over the named phi of K1 (where K1 is exact). named_fam: {name: index in family}."""
    cls = out["classes"]
    for c, rec in out["k0"].items():
        k1c = K1_OF_K0.get(c)
        if k1c is None or k1c not in cls:
            continue
        k1 = {nm: values_of(cls[k1c][nm]) for nm in named_fam if nm in cls[k1c]}
        k1x = {nm: (unrle(cls[k1c][nm]["exact"]) if "exact" in cls[k1c][nm] else None) for nm in k1}
        for form in ("worst", "average"):
            r = rec.get(form)
            if not r:
                continue
            curves = [r["lower"]] if "lower" in r else [r]
            for cr in curves:
                vals = values_of(cr)
                pp = unrle(cr["per_phi"]) if "per_phi" in cr else None
                ok = True
                for K, v in enumerate(vals):
                    for nm, j in named_fam.items():
                        if nm not in k1 or K >= len(k1[nm]):
                            continue
                        if k1x[nm] is not None and not k1x[nm][K]:
                            continue
                        if pp is not None and pp[K] is not None and parse(pp[K][j]) > k1[nm][K]:
                            ok = False
                        if form == "worst" and v > k1[nm][K]:
                            ok = False
                ctl.add("MO", ok, "K0 %s %s <= K1 pointwise" % (c, form))


def shard_curve_controls(ctl, out, n, fam, laws, allg, prim, sib):
    """PC, NC-1, NC-2, MO and K0 checks that this shard's data determine."""
    cls = out["classes"]
    law_of = {g.name: l for g, l in zip(allg, laws)}

    def vals(cname, gname):
        return values_of(cls[cname][gname])

    k1_classes = [c for c in cls if c in ("U", "U_bayes", "B1", "B2", "B3k", "B3w", "B4d1", "B4d2", "B4d3")
                  or c.startswith("emb_") or c.startswith("plin_")]
    if fam == "lin":
        # PC zero: every class on G_lin(p_n) at every K <= n
        for c in k1_classes:
            v = vals(c, "G_lin")
            ctl.add("PC", all(x == 0 for x in v[:n + 1]), "zero %s" % c)
        for c, rec in out["k0"].items():
            for form in ("worst", "average"):
                r = rec.get(form) if isinstance(rec, dict) else None
                if r and "values" in r:
                    ctl.add("PC", all(x == 0 for x in values_of(r)[:n + 1]), "zero K0 %s %s" % (c, form))
                elif r and "upper" in r:
                    ctl.add("PC", all(x == 0 for x in values_of(r["upper"])[:n + 1]), "zero K0 %s %s" % (c, form))
        # PC firing on G_dec at K = 1
        fire = {"U": Fraction(1, 2), "B1": Fraction(1, 2), "B3k": Fraction(1, 2), "B3w": Fraction(1, 2), "B4d1": Fraction(1, 2)}
        for c, want in fire.items():
            ctl.add("PC", vals(c, "G_dec")[1] == want, "firing %s: %s" % (c, vals(c, "G_dec")[1]))
        b2l1 = values_of(cls["B2"]["G_dec"], "lambda_1")[1]
        ctl.add("PC", b2l1 == Fraction(1, 4), "firing B2 lambda=1: %s" % b2l1)
        dec = next(g for g in allg if g.family == "dec")
        w = pc_emb_firing(dec)
        ctl.add("PC", w == Fraction(1, 2), "firing P^emb(1) explicit observer: %s" % w)
        for c in ("emb_m1_all", "emb_m1_passive"):
            if c in cls:
                ctl.add("PC", vals(c, "G_dec")[1] == Fraction(1, 2), "firing %s sweep on G_dec at K=1" % c)
        out["PC_firing_emb1"] = q(w)
        # NC-1 on both siblings, NC-2 on both siblings
        for nm in ("G_lin", "G_lin_sib"):
            v = vals("U", nm)
            ctl.add("NC", all(v[K] == max(Fraction(0), 1 - Fraction(1 << n, 1 << K)) for K in range(len(v))), "NC-1 %s" % nm)
            lam = values_of(cls["B2"][nm], "lambda_n_plus_1")
            okk = True
            for K in range(len(lam)):
                Nn = K + 1
                pq = Fraction(sum(lc.count_closed(Nn, L) for L in range(min(n + 1, Nn) + 1)), 1 << Nn)
                okk &= lam[K] == 1 - pq
            ctl.add("NC", okk, "NC-2 %s" % nm)
    # MO: passive classes at most U; prediction at most distinguishing; m <= m+1; passive <= active
    for gname in cls["U"]:
        u = vals("U", gname)
        for c in k1_classes:
            if c in ("U", "U_bayes") or gname not in cls[c]:
                continue
            if c.startswith("emb_") and "_all" in c:
                continue  # active observers are not tests on X_{0:K}
            v = vals(c, gname)
            ctl.add("MO", all(v[K] <= u[K] for K in range(min(len(v), len(u)))), "%s <= U on %s" % (c, gname))
        for base in [c for c in cls if (c.startswith("emb_") or c.startswith("plin_")) and not c.endswith("_pred")]:
            if gname in cls[base] and gname in cls.get(base + "_pred", {}):
                a, b = vals(base + "_pred", gname), vals(base, gname)
                ctl.add("MO", all(x <= y for x, y in zip(a, b)), "prediction <= distinguishing %s %s" % (base, gname))
        for s_ in ("passive", "all"):
            for suf in ("", "_pred"):
                c1, c2 = "emb_m1_%s%s" % (s_, suf), "emb_m2_%s%s" % (s_, suf)
                if c1 in cls and c2 in cls and gname in cls[c1]:
                    ctl.add("MO", all(x <= y for x, y in zip(vals(c1, gname), vals(c2, gname))), "m1 <= m2 %s%s %s" % (s_, suf, gname))
        for m in (1, 2):
            for suf in ("", "_pred"):
                c1, c2 = "emb_m%d_passive%s" % (m, suf), "emb_m%d_all%s" % (m, suf)
                if c1 in cls and c2 in cls and gname in cls[c1]:
                    ctl.add("MO", all(x <= y for x, y in zip(vals(c1, gname), vals(c2, gname))), "passive <= active m=%d%s %s" % (m, suf, gname))
            for suf in ("", "_pred"):
                c1, c2 = "plin_m%d%s" % (m, suf), "emb_m%d_passive%s" % (m, suf)
                if c1 in cls and c2 in cls and gname in cls[c1]:
                    ctl.add("MO", all(x <= y for x, y in zip(vals(c1, gname), vals(c2, gname))), "passive linear m=%d <= passive m=%d%s %s" % (m, m, suf, gname))
        for m in (1, 2, 3):
            for suf in ("", "_pred"):
                c1, c2 = "plin_m%d%s" % (m, suf), "plin_m%d%s" % (m + 1, suf)
                if c1 in cls and c2 in cls and gname in cls[c1]:
                    ctl.add("MO", all(x <= y for x, y in zip(vals(c1, gname), vals(c2, gname))), "passive linear m=%d <= m+1%s %s" % (m, suf, gname))
        # B4 at d = 1 exists iff B1 has a bias-+-1 test
        if "B4d1" in cls and gname in cls["B4d1"] and gname in law_of:
            b4 = cls["B4d1"][gname]
            rk = B.affine_rank_profile(law_of[gname])
            kf = b4["K_first"]
            for K in range(b4["K_cap"] + 1):
                exists_b4 = kf is not None and K >= kf
                exists_b1 = rk["rank"][K] < K + 1
                ctl.add("MO", exists_b4 == exists_b1, "B4 d=1 iff B1 +-1 at K=%d %s" % (K, gname))
    k0_record_checks(ctl, out, out_family_size(out))
    named_fam = {g.name: j for j, g in enumerate(allg) if g.name in out["named"] and g.family == fam}
    k0_vs_k1(ctl, out, None, named_fam)
    # interval orderings; deterministic <= randomized <= average
    for c, rec in out["k0"].items():
        for form in ("worst", "average"):
            r = rec.get(form)
            if r and "lower" in r:
                lo, hi = values_of(r["lower"]), values_of(r["upper"])
                ctl.add("MO", all(a_ <= b_ for a_, b_ in zip(lo, hi)), "%s K0 %s interval ordered" % (c, form))
        if "average" in rec and "worst" in rec:
            av = values_of(rec["average"]) if "values" in rec["average"] else None
            wl = values_of(rec["worst"]["lower"] if "lower" in rec["worst"] else rec["worst"])
            if av is not None:
                ctl.add("MO", all(a_ <= b_ for a_, b_ in zip(wl, av)), "%s K0 worst <= average" % c)
        rz = rec.get("randomized")
        if rz:
            dw = values_of(rec["worst"])
            av = values_of(rec["average"])
            for K, v in enumerate(unrle(rz["values"])):
                ctl.add("MO", dw[K] <= parse(v) <= av[K], "deterministic <= randomized <= average K0 %s K=%d" % (c, K))


def out_family_size(out):
    return out["k0"]["U"]["family_size"] if "U" in out["k0"] else out["family_size"]


def k0_record_checks(ctl, out, F):
    """K0 checkpoint: each record names one test, evaluated across all of the family, and its value is
    the min (worst) or mean (average) of that test's per-phi values (<= where only a bound)."""
    for c, rec in out["k0"].items():
        for form in ("worst", "average"):
            r = rec.get(form) if isinstance(rec, dict) else None
            if r and "lower" in r and "per_phi" in r["lower"]:
                r = r["lower"]
            if not r or "per_phi" not in r:
                continue
            vals = values_of(r)
            pps = unrle(r["per_phi"])
            tests = unrle(r["tests"])
            exs = unrle(r["exact"]) if "exact" in r else [True] * len(vals)
            ok = True
            for K, (val, pp, ex) in enumerate(zip(vals, pps, exs)):
                if pp is None:
                    continue
                pv = [parse(x) for x in pp]
                good = len(pv) == F and tests[K] is not None
                want = min(pv) if form == "worst" else sum(pv) / len(pv)
                good &= val == want if ex else val <= want
                ok &= good
            ctl.add("K0", ok, "%s %s: one test per K evaluated across the family" % (c, form))


def tags_input(out, n, fam, allg, prim, sib):
    """Mechanical comparisons for the productivity tags (open item TAG-L), from closed forms
    computed here from their formulas: L1 (B1 fires on G_lin at n+1 with value 1/2), L2 (B2 at
    lambda = n+1 equals 1 - Pr_Q[LC <= n+1], and the B2 K_delta equals the closed form's), L3 (B4 at or
    beyond the counting horizon; COVERED-corpus), L4 (a curve equal to max(0, 1 - 2^(n-K)))."""
    cls = out["classes"]
    res = {}

    def nc1(K):
        return max(Fraction(0), 1 - Fraction(1 << n, 1 << K))

    def l4(rec):
        v = values_of(rec)
        return all(v[K] == nc1(K) for K in range(len(v))) and rec.get("all_exact", True)

    def closed_b2(K):
        Nn = K + 1
        return 1 - Fraction(sum(lc.count_closed(Nn, L) for L in range(min(n + 1, Nn) + 1)), 1 << Nn)

    for c, gs in cls.items():
        for gname, rec in gs.items():
            t = {"L4": l4(rec)}
            if c == "B1" and gname in ("G_lin", "G_lin_sib"):
                v = values_of(rec)
                t["L1"] = rec["K_zero"] == n and v[n + 1] == Fraction(1, 2)
            if c == "B2" and gname in ("G_lin", "G_lin_sib"):
                lam = values_of(rec, "lambda_n_plus_1")
                eq = all(lam[K] == closed_b2(K) for K in range(len(lam)))
                kd = {}
                for d, nm in ((D8, "1/8"), (D4, "1/4")):
                    kd[nm] = next((K for K in range(len(lam)) if closed_b2(K) >= d), None)
                t["L2"] = eq and all(rec["K_delta"][nm] == kd[nm] for nm in kd)
            if c.startswith("B4"):
                t["L3_corpus"] = rec["K_first"] is not None and rec["K_first"] >= rec["counting_horizon"]
            res.setdefault("K1", {}).setdefault(c, {})[gname] = t
    for c, rec in out["k0"].items():
        for form in ("worst", "average"):
            r = rec.get(form)
            if not r:
                continue
            t = {"L4": l4(r["lower"]) and l4(r["upper"]) if "lower" in r else l4(r)}
            if c == "B1" and fam == "lin" and "values" in r:
                v = values_of(r)
                t["L1"] = r["K_zero"] == n and v[n + 1] == Fraction(1, 2)
            if c.startswith("B4"):
                t["L3_corpus"] = r["K_first"] is not None and r["K_first"] >= r["counting_horizon"]
            res.setdefault("K0", {}).setdefault(c, {})[form] = t
    return res


def pc_emb_firing(dec):
    """The P^emb(1) firing test of §4 on G_dec at K = 1: rho_0 = id, rho_1 = flip, a = 0, F = {v = x}."""
    R = np.array([[[0, 1], [1, 0]]])
    obs = O.ObsSet("pc", 1, R, np.zeros((1, 2), dtype=np.int64), np.zeros(1, dtype=np.int64))
    sim = E.Sim(obs, np.array([0]), [dec], [1])
    sim.step()
    C = sim.counts(0)[0]
    pP = Fraction(int(C[0, 0] + C[1, 1]), dec.M)
    qc = E.QChain(obs.R)
    qc.advance()
    pQ = sum(Fraction(int(qc.Q[0, v]), 2) * Fraction(1, 2) for v in (0, 1))   # q_1(v)/2 for x = v
    return abs(pP - pQ)


# ================================================================== the m = 3 passive shard

def shard_m3(n, fam, mode, ctl, timing):
    kmax = P.k_max(n)
    cap = P.m3_cap(n, kmax)
    famlist, prim, sib, extra = named_for(n, fam)
    allg = famlist + extra
    named_idx = [prim] + ([sib] if sib is not None else []) + list(range(len(famlist), len(allg)))
    out = {"n": n, "family": fam, "K_cap": cap, "classes": {}, "k0": {}, "witnesses": [], "windows": {},
           "family_size": len(famlist), "named": {allg[i].name: allg[i].gid for i in named_idx},
           "scope": "A1 option (ii)" + (": K <= %d" % cap if n in (7, 8) else ": uncapped (K <= K_max)")}
    t0 = time.time()
    obs = O.passive_m3()
    kcx = ar.kcx_of(allg[prim])[0]
    out["K_cx"] = kcx
    if n <= 4:
        for g in allg:
            e1, e8 = Cm.exhaustive_maps(obs, g, chunk=16384)
            ctl.add("EX1", e1, "composites m=3 %s" % g.gid)
            ctl.add("EX8", e8, "composites m=3 %s" % g.gid)
        r1, r8 = Cm.exhaustive_readout(3, allg[prim], range(1 << 16), K=3)
        ctl.add("EX1", r1, "readout m=3")
        ctl.add("EX8", r8, "readout m=3")
    sw = E.Sweep(obs, allg, [cap if gi in named_idx else 0 for gi in range(len(allg))], list(range(len(famlist))),
                 [prim], cap, "pred", {"passive": np.ones(obs.n, bool)}, window_cap={prim: cap}, chunk=4096,
                 im3=Cm.FullState if n <= 4 else None).run()
    ctl.add("EX2", sw.ex2_q, "Q_p sums m=3")
    if n <= 4:
        ctl.add("IM3", sw.im3_ok, "m=3 n=%d %s %s" % (n, fam, sw.im3_fail[:3]))
    M = allg[0].M
    for gi in named_idx:
        d = {K: E.k1_dist_value(v[0], M, K) for K, v in sw.k1d[("passive", gi)].items()}
        pr = {K: E.k1_pred_value(v[0], M) for K, v in sw.k1p[("passive", gi)].items()}
        out["classes"].setdefault("emb_m3_passive", {})[allg[gi].name] = curve_rec(d)
        out["classes"].setdefault("emb_m3_passive_pred", {})[allg[gi].name] = curve_rec(pr)
    out["k0"]["emb_m3_passive"] = {"worst": k0_pred_rec(sw.k0w["passive"], M, len(famlist), False, obs, None),
                                   "average": k0_pred_rec(sw.k0a["passive"], M, len(famlist), True, obs, None),
                                   "test_class": "prediction tests, every chi"}
    out["windows"]["emb_m3_passive"] = window_summary(sw, "passive", prim)
    out["witnesses"] = witnesses_from(sw, "passive", obs, "emb_m3_passive", 3, allg, prim, famlist, kcx, ctl)
    # U on the named generators, for MO (m = 3 passive <= U)
    for gi in named_idx:
        tv, _ = LW.u_k1_curve(LW.Law(allg[gi], cap))
        out["classes"].setdefault("U", {})[allg[gi].name] = curve_rec(tv)
    cls = out["classes"]
    if fam == "lin":
        for c in ("emb_m3_passive", "emb_m3_passive_pred"):
            ctl.add("PC", all(x == 0 for x in values_of(cls[c]["G_lin"])[:n + 1]), "zero %s" % c)
        ctl.add("PC", all(x == 0 for f in ("worst", "average") for x in values_of(out["k0"]["emb_m3_passive"][f])[:n + 1]),
                "zero K0 emb_m3_passive")
    for gname in cls["emb_m3_passive"]:
        a_, b_, u_ = values_of(cls["emb_m3_passive_pred"][gname]), values_of(cls["emb_m3_passive"][gname]), values_of(cls["U"][gname])
        ctl.add("MO", all(x <= y for x, y in zip(a_, b_)), "m3 prediction <= distinguishing %s" % gname)
        ctl.add("MO", all(x <= y for x, y in zip(b_, u_)), "m3 passive <= U %s" % gname)
    k0_record_checks(ctl, out, len(famlist))
    k0_vs_k1(ctl, out, None, {g.name: j for j, g in enumerate(allg) if g.name in out["named"] and g.family == fam})
    timing["m3"] = time.time() - t0
    return out
