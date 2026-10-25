#!/usr/bin/env python3
"""BH-01 access audit v1: exact finite checks of accessible information recovery.

Implements the preregistered plan in PLAN.md (same directory). Standard library only;
every verdict quantity is an integer or fractions.Fraction. Deterministic: the output
file result.json is byte-identical under `python3 -I -B` and `python3 -I -B -O`.

Usage (from any directory):
    python3 -I -B checks.py [--out DIR] [--sync-report]

--out DIR       write result.json into DIR (default: this file's directory)
--sync-report   also rewrite the generated block of REPORT.md (this file's directory)
                from the run's verdict text

Exit status: 0 when every required control passes (the claim verdicts are in
result.json); 2 and `VOID` printed when a required control fails, in which case no
result file is written.
"""
import io
import itertools
import json
import os
import sys
import tokenize
from fractions import Fraction

BASE_COMMIT = "809fac52cdf207d24eccc63c734996bcb9d073a0"
HOLDS = "HOLDS_WITHIN_SCOPE"
NEG = "NEGATIVE_FOR_CONSTRUCTION"


def fr(x):
    """Serialize a Fraction (or int) as an exact string."""
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else "%d/%d" % (x.numerator, x.denominator)


# ---------------------------------------------------------------------------
# Configuration spaces, maps, priors, records
# ---------------------------------------------------------------------------

class Space:
    """Finite product of registers; register 0 is the least significant digit."""

    def __init__(self, sizes):
        self.sizes = tuple(sizes)
        self.n = 1
        for q in self.sizes:
            self.n *= q
        self.digits = []
        for idx in range(self.n):
            d, v = [], idx
            for q in self.sizes:
                d.append(v % q)
                v //= q
            self.digits.append(tuple(d))
        self.index = {d: i for i, d in enumerate(self.digits)}


def build_map(space, fn):
    """Tabulate a map given on digit tuples."""
    return tuple(space.index[tuple(fn(d))] for d in space.digits)


def is_bijection(table):
    """Independent bijectivity check: the image is the whole domain."""
    return sorted(table) == list(range(len(table)))


def all_permutations(n):
    return list(itertools.permutations(range(n)))


def support(space, msg_regs, prior):
    """Initial supports X_m. prior[r] is 'hidden' (uniform) or 'blank' (value 0)."""
    hidden = [r for r in range(len(space.sizes)) if r not in msg_regs and prior.get(r) == "hidden"]
    messages = list(itertools.product(*[range(space.sizes[r]) for r in msg_regs]))
    out = {}
    for m in messages:
        lst = []
        for h in itertools.product(*[range(space.sizes[r]) for r in hidden]):
            d = [0] * len(space.sizes)
            for r, v in zip(msg_regs, m):
                d[r] = v
            for r, v in zip(hidden, h):
                d[r] = v
            lst.append(space.index[tuple(d)])
        out[m] = lst
    return messages, out


def make_record(dtraj, schedule, t, mode):
    if mode == "cumulative":
        return tuple(tuple(dtraj[s][r] for r in schedule[s]) for s in range(t + 1))
    return tuple(dtraj[t][r] for r in schedule[t])


def evaluate(space, msg_regs, prior, maps, schedule, mode):
    """Record counts: result[t][m][record] = number of initial configurations."""
    T = len(maps)
    messages, supp = support(space, msg_regs, prior)
    res = [{m: {} for m in messages} for _ in range(T + 1)]
    for m in messages:
        for x0 in supp[m]:
            traj = [x0]
            for F in maps:
                traj.append(F[traj[-1]])
            dtraj = [space.digits[i] for i in traj]
            for t in range(T + 1):
                rec = make_record(dtraj, schedule, t, mode)
                c = res[t][m]
                c[rec] = c.get(rec, 0) + 1
    N = len(supp[messages[0]])
    return messages, N, res


def total_variation(c0, c1, N):
    keys = set(c0) | set(c1)
    return Fraction(sum(abs(c0.get(y, 0) - c1.get(y, 0)) for y in keys), 2 * N)


def bayes_success(cm, messages, N):
    keys = set()
    for m in messages:
        keys |= set(cm[m])
    return Fraction(sum(max(cm[m].get(y, 0) for m in messages) for y in keys), len(messages) * N)


def records_disjoint(cm, messages):
    sets = [set(cm[m]) for m in messages]
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if sets[i] & sets[j]:
                return False
    return True


class Ledger:
    """Enumeration-level control counters (K1, K3)."""

    def __init__(self):
        self.k1_checked = 0
        self.k1_fail = []
        self.k3_checked = 0
        self.k3_fail = []


LEDGER = Ledger()


def figures(messages, N, res, case=""):
    """Per-time figures of merit, with the K3 cross-check applied at every time."""
    out = []
    for t, cm in enumerate(res):
        ps = bayes_success(cm, messages, N)
        disj = records_disjoint(cm, messages)
        tv = total_variation(cm[messages[0]], cm[messages[1]], N) if len(messages) == 2 else None
        ok = (ps == 1) == disj
        if tv is not None:
            ok = ok and ps == (1 + tv) / 2
        LEDGER.k3_checked += 1
        if not ok and len(LEDGER.k3_fail) < 5:
            LEDGER.k3_fail.append("%s t=%d" % (case, t))
        out.append({"psucc": ps, "tv": tv, "recoverable": ps == 1})
    return out


def check_bij(table, case):
    LEDGER.k1_checked += 1
    if not is_bijection(table):
        if len(LEDGER.k1_fail) < 5:
            LEDGER.k1_fail.append(case)
        return False
    return True


def nondecreasing(seq):
    return all(seq[i + 1] >= seq[i] for i in range(len(seq) - 1))


# ---------------------------------------------------------------------------
# GF(2) linear algebra (independent route for K5)
# ---------------------------------------------------------------------------

def gf2_rank(rows):
    rows = [r for r in rows]
    rank = 0
    bit = 0
    width = max([r.bit_length() for r in rows] + [0])
    for bit in range(width):
        piv = None
        for i in range(rank, len(rows)):
            if (rows[i] >> bit) & 1:
                piv = i
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(len(rows)):
            if i != rank and (rows[i] >> bit) & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def parity(v):
    return bin(v).count("1") & 1


def linear_table(rows, n):
    return tuple(sum(parity(rows[i] & x) << i for i in range(n)) for x in range(1 << n))


def linear_rt(rows, t, k):
    """Recovered message dimensions after t emissions, from ranks (Lemma L)."""
    hidden_mask = ((1 << len(rows)) - 1) ^ ((1 << k) - 1)
    return gf2_rank(rows[:t]) - gf2_rank([r & hidden_mask for r in rows[:t]])


# ---------------------------------------------------------------------------
# Named instances
# ---------------------------------------------------------------------------

def named_k2_instances():
    """K2: instances whose figures are derived by hand (registers: 0=B msg, 1=K key, 2=R)."""
    sp = Space([2, 2, 2])
    ident = build_map(sp, lambda d: d)
    otp = build_map(sp, lambda d: (d[0], d[1], d[2] ^ d[0] ^ d[1]))
    andl = build_map(sp, lambda d: (d[0], d[1], d[2] ^ (d[0] & d[1])))
    prior = {1: "hidden", 2: "blank"}
    cases = [
        ("identity_message_unread", ident, (2,), Fraction(0)),
        ("identity_direct_read", ident, (0,), Fraction(1)),
        ("one_time_pad_R_alone", otp, (2,), Fraction(0)),
        ("one_time_pad_K_alone", otp, (1,), Fraction(0)),
        ("one_time_pad_R_and_K", otp, (1, 2), Fraction(1)),
        ("and_leak_R", andl, (2,), Fraction(1, 2)),
    ]
    out = {}
    for name, F, read, expect in cases:
        check_bij(F, "K2:" + name)
        msgs, N, res = evaluate(sp, (0,), prior, [F], [(), read], "cumulative")
        fig = figures(msgs, N, res, "K2:" + name)
        out[name] = {"tv": fig[1]["tv"], "expected": expect, "pass": fig[1]["tv"] == expect}
    return out


def run_controls():
    """Fast controls K1 (rejection), K2, K4 (counts), K5 (identity case)."""
    c = {}
    const = (0, 0, 0, 0)
    swap2 = (1, 0, 3, 2)
    c["K1"] = {"known_nonbijection_rejected": not is_bijection(const),
               "known_bijection_accepted": is_bijection(swap2)}
    c["K2"] = {k: v["pass"] for k, v in named_k2_instances().items()}
    perms = all_permutations(8)
    c["K4"] = {"S8_count": len(perms) == 40320 and len(set(perms)) == 40320}
    # K5 fast case: identity matrix on 4 modes, k = 1 and 2.
    rows = [1, 2, 4, 8]
    ok = True
    for k in (1, 2):
        sp = Space([2] * 4)
        tab = linear_table(rows, 4)
        prior = {r: "hidden" for r in range(k, 4)}
        sched = [tuple(range(t)) for t in range(5)]
        msgs, N, res = evaluate(sp, tuple(range(k)), prior, [tab] + [tuple(range(16))] * 3, sched, "cumulative")
        for t in range(1, 5):
            ps = bayes_success(res[t], msgs, N)
            r = linear_rt(rows, t, k)
            if r < 0 or ps != Fraction(2 ** r, 2 ** k):
                ok = False
    c["K5"] = {"identity_cases": ok}
    return c


def controls_pass(c):
    return all(all(v.values()) for v in c.values())


# ---------------------------------------------------------------------------
# Exhaustive classes
# ---------------------------------------------------------------------------

def hist_add(h, key):
    h[key] = h.get(key, 0) + 1


def s8_classes():
    """All 40320 bijections of {0,1}^3 in several layouts."""
    sp = Space([2, 2, 2])
    perms = all_permutations(8)
    sched_mp = [(), (2,), (1, 2), (0, 1, 2)]
    out = {
        "count": len(perms),
        "MP1": {"C1_violations_t3": 0, "tv_t2_hist": {}, "tv_profile_hist": {},
                "C2_violations": 0, "D1_violations": 0, "zero_adv_t2_example": None},
        "MP1_static": {"C1_violations_t3": 0, "C2_violations": 0, "D1_violations": 0,
                       "tv_profile_hist": {}},
        "MP2": {"C1_violations_t3": 0, "C2_violations": 0, "psucc_t2_hist": {},
                "min_psucc_t2": None, "attains_bound_t2": 0, "blind_t2": 0, "D1_violations": 0},
        "snapshot": {"D2_decreasing": 0, "example": None},
        "nested": {"tv_t3_hist": {}, "E_violations": 0, "E_zero_adv_instances": 0},
        "nested_W_endpoint": {"recover": 0, "not_recover": 0, "product_maps": 0,
                              "product_maps_not_recover": 0, "C3_violations": 0,
                              "nonproduct_not_recover_example": None},
    }
    ident = tuple(range(8))
    w_sp = Space([2, 2])
    for p in perms:
        check_bij(p, "S8")
        # MP1: message mode 0, modes 1,2 hidden; emission 2,1,0; homogeneous.
        msgs, N, res = evaluate(sp, (0,), {1: "hidden", 2: "hidden"}, [p] * 3, sched_mp, "cumulative")
        fig = figures(msgs, N, res, "MP1")
        o = out["MP1"]
        if not fig[3]["recoverable"]:
            o["C1_violations_t3"] += 1
        hist_add(o["tv_t2_hist"], fr(fig[2]["tv"]))
        hist_add(o["tv_profile_hist"], ",".join(fr(f["tv"]) for f in fig))
        for t, K in ((1, 4), (2, 2)):
            if fig[t]["psucc"] < Fraction(1, K):
                o["C2_violations"] += 1
        if not nondecreasing([f["tv"] for f in fig]) or not nondecreasing([f["psucc"] for f in fig]):
            o["D1_violations"] += 1
        if fig[2]["tv"] == 0 and o["zero_adv_t2_example"] is None and p != ident:
            o["zero_adv_t2_example"] = list(p)
        # MP1_static: one scramble, then static emission.
        msgs, N, res = evaluate(sp, (0,), {1: "hidden", 2: "hidden"}, [p, ident, ident], sched_mp, "cumulative")
        fig = figures(msgs, N, res, "MP1_static")
        o = out["MP1_static"]
        if not fig[3]["recoverable"]:
            o["C1_violations_t3"] += 1
        for t, K in ((1, 4), (2, 2)):
            if fig[t]["psucc"] < Fraction(1, K):
                o["C2_violations"] += 1
        if not nondecreasing([f["tv"] for f in fig]):
            o["D1_violations"] += 1
        hist_add(o["tv_profile_hist"], ",".join(fr(f["tv"]) for f in fig))
        # MP2: message modes 0,1; mode 2 hidden.
        msgs, N, res = evaluate(sp, (0, 1), {2: "hidden"}, [p] * 3, sched_mp, "cumulative")
        fig = figures(msgs, N, res, "MP2")
        o = out["MP2"]
        if not fig[3]["recoverable"]:
            o["C1_violations_t3"] += 1
        for t, K in ((1, 4), (2, 2)):
            if fig[t]["psucc"] < Fraction(1, K):
                o["C2_violations"] += 1
        ps2 = fig[2]["psucc"]
        hist_add(o["psucc_t2_hist"], fr(ps2))
        if o["min_psucc_t2"] is None or ps2 < o["min_psucc_t2"]:
            o["min_psucc_t2"] = ps2
        if ps2 == Fraction(1, 2):
            o["attains_bound_t2"] += 1
        if ps2 == Fraction(1, 4):
            o["blind_t2"] += 1
        if not nondecreasing([f["psucc"] for f in fig]):
            o["D1_violations"] += 1
        # Snapshot access of mode 2 at t = 1..3.
        msgs, N, res = evaluate(sp, (0,), {1: "hidden", 2: "hidden"}, [p] * 3,
                                [(), (2,), (2,), (2,)], "snapshot")
        fig = figures(msgs, N, res, "snapshot")
        tvs = [f["tv"] for f in fig]
        if not nondecreasing(tvs):
            out["snapshot"]["D2_decreasing"] += 1
            if out["snapshot"]["example"] is None:
                out["snapshot"]["example"] = {"perm": list(p), "tv": [fr(v) for v in tvs]}
        # Nested layout: 0 = V (blank, read t>=1), 1 = B (message), 2 = D (hidden, never read).
        prior_n = {0: "blank", 2: "hidden"}
        msgs, N, res = evaluate(sp, (1,), prior_n, [p] * 3, [(), (0,), (0,), (0,)], "cumulative")
        fig = figures(msgs, N, res, "nested")
        hist_add(out["nested"]["tv_t3_hist"], fr(fig[3]["tv"]))
        if not nested_assoc(sp, p):
            out["nested"]["E_violations"] += 1
        elif fig[3]["tv"] == 0:
            out["nested"]["E_zero_adv_instances"] += 1
        # Nested, W read at endpoint (V and B), D never read.
        o = out["nested_W_endpoint"]
        msgs, N, res = evaluate(sp, (1,), prior_n, [p] * 3, [(), (0,), (0,), (0, 1)], "cumulative")
        fig = figures(msgs, N, res, "nested_W")
        rec = fig[3]["recoverable"]
        o["recover" if rec else "not_recover"] += 1
        G = product_factor(sp, p)
        if G is not None:
            o["product_maps"] += 1
            if not rec:
                o["product_maps_not_recover"] += 1
            # C3: record distribution equals the W-only model with G.
            msgs_w, N_w, res_w = evaluate(w_sp, (1,), {0: "blank"}, [G] * 3,
                                          [(), (0,), (0,), (0, 1)], "cumulative")
            check_bij(G, "C3:G")
            for t in range(4):
                for m in msgs:
                    a = {y: Fraction(c, N) for y, c in res[t][m].items()}
                    b = {y: Fraction(c, N_w) for y, c in res_w[t][m].items()}
                    if a != b:
                        o["C3_violations"] += 1
        elif not rec and o["nonproduct_not_recover_example"] is None:
            o["nonproduct_not_recover_example"] = list(p)
    for key in ("MP1", "MP1_static", "MP2", "nested", "nested_W_endpoint"):
        for hk in list(out[key]):
            if hk.endswith("_hist"):
                out[key][hk] = dict(sorted(out[key][hk].items()))
    return out


def product_factor(sp, p):
    """If p = G x H on (V,B) x D, return G as a table on the 2-bit W space, else None."""
    G = {}
    H = {}
    for idx, d in enumerate(sp.digits):
        e = sp.digits[p[idx]]
        w, dd = (d[0], d[1]), d[2]
        w2, dd2 = (e[0], e[1]), e[2]
        if G.setdefault(w, w2) != w2 or H.setdefault(dd, dd2) != dd2:
            return None
    return tuple(G[(i & 1, i >> 1)][0] + 2 * G[(i & 1, i >> 1)][1] for i in range(4))


def nested_assoc(sp, p):
    """GR Theorem A.1 check: direct vs sequential marginal transition matrix on V, t = 1..3."""
    pt = tuple(range(8))
    for t in range(1, 4):
        pt = tuple(p[i] for i in pt)
        direct = {}
        for v in range(2):
            for b in range(2):
                for d in range(2):
                    y = sp.digits[pt[sp.index[(v, b, d)]]][0]
                    direct[(v, y)] = direct.get((v, y), Fraction(0)) + Fraction(1, 4)
        # Sequential: stage-1 kernel on W = V x B (marginalize D), then marginalize B.
        k1 = {}
        for v in range(2):
            for b in range(2):
                for d in range(2):
                    e = sp.digits[pt[sp.index[(v, b, d)]]]
                    key = ((v, b), (e[0], e[1]))
                    k1[key] = k1.get(key, Fraction(0)) + Fraction(1, 2)
        seq = {}
        for ((v, b), (v2, b2)), w in k1.items():
            seq[(v, v2)] = seq.get((v, v2), Fraction(0)) + w * Fraction(1, 2)
        if {k: x for k, x in direct.items() if x} != {k: x for k, x in seq.items() if x}:
            return False
    return True


def all_maps_classes():
    """All 256 maps on {0,1}^2 (register 0 = B, register 1 = R)."""
    sp = Space([2, 2])
    maps = list(itertools.product(range(4), repeat=4))
    out = {"count": len(maps),
           "AM1_complete_access": {"bij_rec": 0, "bij_norec": 0, "nonbij_rec": 0, "nonbij_norec": 0,
                                   "nonbij_rec_example": None},
           "AM2_remnant_bound": {"bij_ok": 0, "bij_violate": 0, "nonbij_ok": 0, "nonbij_violate": 0,
                                 "nonbij_violate_example": None},
           "AM3_refinement": {"D1_violations": 0, "snapshot_decreasing": 0}}
    for F in maps:
        bij = is_bijection(F)
        # AM1: message in B, R hidden-uniform, full read at t = 1.
        msgs, N, res = evaluate(sp, (0,), {1: "hidden"}, [F], [(), (0, 1)], "cumulative")
        fig = figures(msgs, N, res, "AM1")
        rec = fig[1]["recoverable"]
        o = out["AM1_complete_access"]
        o[("bij_" if bij else "nonbij_") + ("rec" if rec else "norec")] += 1
        if (not bij) and rec and o["nonbij_rec_example"] is None:
            o["nonbij_rec_example"] = list(F)
        # AM2: message = both registers (|M| = 4), read register 1 at t = 1, K = {0}.
        msgs, N, res = evaluate(sp, (0, 1), {}, [F], [(), (1,)], "cumulative")
        fig = figures(msgs, N, res, "AM2")
        ok = fig[1]["psucc"] >= Fraction(1, 2)
        o = out["AM2_remnant_bound"]
        o[("bij_" if bij else "nonbij_") + ("ok" if ok else "violate")] += 1
        if (not bij) and (not ok) and o["nonbij_violate_example"] is None:
            o["nonbij_violate_example"] = list(F)
        # AM3: cumulative refinement for every map; snapshot for comparison.
        msgs, N, res = evaluate(sp, (0,), {1: "hidden"}, [F, F], [(), (1,), (0, 1)], "cumulative")
        fig = figures(msgs, N, res, "AM3")
        if not nondecreasing([f["tv"] for f in fig]) or not nondecreasing([f["psucc"] for f in fig]):
            out["AM3_refinement"]["D1_violations"] += 1
        msgs, N, res = evaluate(sp, (0,), {1: "hidden"}, [F, F], [(), (1,), (1,)], "snapshot")
        fig = figures(msgs, N, res, "AM3s")
        if not nondecreasing([f["tv"] for f in fig]):
            out["AM3_refinement"]["snapshot_decreasing"] += 1
    return out


def gl42_class():
    """All GL(4,2) bijections: one scramble, then one mode emitted per step (static)."""
    n = 4
    sp = Space([2] * n)
    mats = []
    for rows in itertools.product(range(16), repeat=4):
        if gf2_rank(list(rows)) == 4:
            mats.append(rows)
    ident = tuple(range(16))
    sched = [tuple(range(t)) for t in range(n + 1)]
    out = {"count": len(mats), "distinct_tables": None, "by_k": {}, "K5_fail": 0}
    tables = set()
    for k in (1, 2):
        prof = {}
        c2v = c4v = d1v = 0
        late = early = 0
        for rows in mats:
            tab = linear_table(list(rows), n)
            if k == 1:
                tables.add(tab)
                check_bij(tab, "GL42")
            msgs, N, res = evaluate(sp, tuple(range(k)), {r: "hidden" for r in range(k, n)},
                                    [tab, ident, ident, ident], sched, "cumulative")
            fig = figures(msgs, N, res, "GL42")
            rts = []
            for t in range(n + 1):
                ps = fig[t]["psucc"]
                scaled = ps * (2 ** k)
                if scaled.denominator != 1 or scaled.numerator & (scaled.numerator - 1):
                    c4v += 1
                    rts.append(None)
                    continue
                r_enum = scaled.numerator.bit_length() - 1
                rts.append(r_enum)
                if r_enum != linear_rt(list(rows), t, k):
                    out["K5_fail"] += 1
                if not (max(0, t - (n - k)) <= r_enum <= min(k, t)):
                    c4v += 1
                if ps < Fraction(1, 2 ** (n - t)):
                    c2v += 1
            if not nondecreasing([f["psucc"] for f in fig]):
                d1v += 1
            key = ",".join(str(r) for r in rts)
            hist_add(prof, key)
            if rts == [max(0, t - (n - k)) for t in range(n + 1)]:
                late += 1
            if rts == [min(k, t) for t in range(n + 1)]:
                early += 1
        out["by_k"][str(k)] = {"r_profile_hist": dict(sorted(prof.items())), "C2_violations": c2v,
                               "C4_violations": c4v, "D1_violations": d1v,
                               "late_emergence_count": late, "early_emergence_count": early}
    out["distinct_tables"] = len(tables)
    return out


# ---------------------------------------------------------------------------
# Structured families (claim B and named examples)
# ---------------------------------------------------------------------------

def swap_cascade(nB, k, order, q=2):
    """Interior registers 0..nB-1 (first k carry the message, rest hidden), radiation
    registers nB..2nB-1 (blank). Step j swaps interior register order[j-1] into R_j;
    R_1..R_j are read from step j on (cumulative)."""
    sp = Space([q] * (2 * nB))
    maps = []
    for j in range(1, nB + 1):
        a, b = order[j - 1], nB + j - 1

        def fn(d, a=a, b=b):
            d = list(d)
            d[a], d[b] = d[b], d[a]
            return d
        maps.append(build_map(sp, fn))
    for F in maps:
        check_bij(F, "B1")
    prior = {r: "hidden" for r in range(k, nB)}
    prior.update({r: "blank" for r in range(nB, 2 * nB)})
    sched = [tuple(range(nB, nB + t)) for t in range(nB + 1)]
    msgs, N, res = evaluate(sp, tuple(range(k)), prior, maps, sched, "cumulative")
    return figures(msgs, N, res, "B1")


def cnot_cascade(n, order):
    """Mode 0 carries the message, modes 1..n-1 hidden keys. One step sets
    mode0 ^= mode1 ^ ... ^ mode(n-1); then modes are emitted in `order`, static."""
    sp = Space([2] * n)

    def fn(d):
        d = list(d)
        for r in range(1, n):
            d[0] ^= d[r]
        return d
    F = build_map(sp, fn)
    check_bij(F, "B2")
    ident = tuple(range(sp.n))
    sched = [tuple(sorted(order[:t])) for t in range(n + 1)]
    msgs, N, res = evaluate(sp, (0,), {r: "hidden" for r in range(1, n)}, [F] + [ident] * (n - 1), sched,
                            "cumulative")
    return figures(msgs, N, res, "B2")


def named_examples():
    out = {}
    # A: swap message into a remnant register that is never emitted (registers 0=B msg, 1=R blank, 2=K remnant blank).
    sp = Space([2, 2, 2])
    F = build_map(sp, lambda d: (d[2], d[1], d[0]))
    check_bij(F, "named:swap_into_remnant")
    msgs, N, res = evaluate(sp, (0,), {1: "blank", 2: "blank"}, [F], [(), (0, 1)], "cumulative")
    out["swap_into_remnant"] = {"bijective": is_bijection(F), "tv_t1": figures(msgs, N, res, "n1")[1]["tv"]}
    # A (necessity): erase-and-copy, non-injective: (b, r) -> (0, b), full read.
    sp2 = Space([2, 2])
    E = build_map(sp2, lambda d: (0, d[0]))
    msgs, N, res = evaluate(sp2, (0,), {1: "hidden"}, [E], [(), (0, 1)], "cumulative")
    out["erase_and_copy"] = {"bijective": is_bijection(E), "tv_t1": figures(msgs, N, res, "n2")[1]["tv"]}
    # C3 countercontrol: B-D leak. Registers 0=V blank, 1=B msg, 2=D hidden.
    # t=1 swap B<->D (B-D coupling), t=2 swap V<->B (emission); W = {V,B} read at t=2.
    L1 = build_map(sp, lambda d: (d[0], d[2], d[1]))
    L2 = build_map(sp, lambda d: (d[1], d[0], d[2]))
    check_bij(L1, "named:leak1")
    check_bij(L2, "named:leak2")
    msgs, N, res = evaluate(sp, (1,), {0: "blank", 2: "hidden"}, [L1, L2], [(), (0,), (0, 1)], "cumulative")
    out["B_D_leak"] = {"bijective": is_bijection(L1) and is_bijection(L2),
                       "tv_t2_W_read": figures(msgs, N, res, "n3")[2]["tv"]}
    # Same emission without the leak (product map: identity on D).
    msgs, N, res = evaluate(sp, (1,), {0: "blank", 2: "hidden"}, [tuple(range(8)), L2], [(), (0,), (0, 1)],
                            "cumulative")
    out["no_leak_reference"] = {"tv_t2_W_read": figures(msgs, N, res, "n4")[2]["tv"]}
    # D2: swap message into the read register and back (registers 0=B msg, 1=R hidden).
    S = build_map(sp2, lambda d: (d[1], d[0]))
    check_bij(S, "named:swap_back")
    snap = []
    cum = []
    for mode, store in (("snapshot", snap), ("cumulative", cum)):
        msgs, N, res = evaluate(sp2, (0,), {1: "hidden"}, [S, S], [(), (1,), (1,)], mode)
        store.extend(f["tv"] for f in figures(msgs, N, res, "n5"))
    out["swap_in_swap_out"] = {"snapshot_tv": snap, "cumulative_tv": cum}
    return out


def structured_families():
    out = {"B1_swap": {}, "B1_swap_wide": {}, "B2_cnot": {}}
    for nB in range(1, 7):
        for k in range(1, min(3, nB) + 1):
            for oname in ("message_first", "message_last"):
                order = list(range(nB)) if oname == "message_first" else list(range(nB - 1, -1, -1))
                fig = swap_cascade(nB, k, order)
                out["B1_swap"]["nB=%d,k=%d,%s" % (nB, k, oname)] = [f["psucc"] for f in fig]
    for q in (2, 4, 8, 16):
        for oname, order in (("message_first", [0, 1]), ("message_last", [1, 0])):
            fig = swap_cascade(2, 1, order, q=q)
            out["B1_swap_wide"]["q=%d,%s" % (q, oname)] = [f["psucc"] for f in fig]
    for n in range(2, 7):
        for oname, order in (("message_last", list(range(1, n)) + [0]), ("message_first", list(range(n)))):
            fig = cnot_cascade(n, order)
            out["B2_cnot"]["n=%d,%s" % (n, oname)] = [f["tv"] for f in fig]
    return out


# ---------------------------------------------------------------------------
# Item F: endpoint-decoupling arithmetic (rational interval bounds)
# ---------------------------------------------------------------------------

def sci(x, digits=2):
    """Format a positive Fraction as d.dd x 10^e using integers only (truncated)."""
    x = Fraction(x)
    e = 0
    while x >= 10:
        x /= 10
        e += 1
    while x < 1:
        x *= 10
        e -= 1
    m = int(x * 10 ** digits)
    s = str(m)
    return "%s.%se%d" % (s[0], s[1:], e)


def icbrt_floor(n):
    lo, hi = 0, 1
    while hi ** 3 <= n:
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** 3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def item_f():
    c = Fraction(299792458)
    hbar = Fraction(1054571817, 10 ** 43)
    G_lo, G_hi = Fraction(667415, 10 ** 16), Fraction(667445, 10 ** 16)
    GMsun = Fraction(13271244) * 10 ** 13
    pi_lo, pi_hi = Fraction(3), Fraction(22, 7)
    gam_lo, gam_hi = Fraction(1, 100), Fraction(1000)
    tau_lo, tau_hi = Fraction(10 ** 16), Fraction(10 ** 19)
    GM = 30 * GMsun
    t_lo = 5120 * pi_lo * GM ** 3 / (G_hi * hbar * c ** 4 * gam_hi)
    t_hi = 5120 * pi_hi * GM ** 3 / (G_lo * hbar * c ** 4 * gam_lo)
    r_lo, r_hi = t_lo / tau_hi, t_hi / tau_lo
    status = "contradicted" if r_lo > 1 else ("supported" if r_hi < 1 else "undecided")
    m3_lo = tau_lo * hbar * c ** 4 * gam_lo / (5120 * pi_hi * G_hi ** 2)
    m3_hi = tau_hi * hbar * c ** 4 * gam_hi / (5120 * pi_lo * G_lo ** 2)
    ms_lo = icbrt_floor(m3_lo.numerator // m3_lo.denominator)
    ms_hi = icbrt_floor(m3_hi.numerator // m3_hi.denominator) + 1
    floor_log10 = len(str(r_lo.numerator // r_lo.denominator)) - 1 if r_lo >= 1 else None
    return {
        "inputs": {"c_m_per_s": fr(c), "hbar_J_s": "1.054571817e-34", "G_interval": ["6.67415e-11", "6.67445e-11"],
                   "GM_sun_m3_per_s2": "1.3271244e20", "mass": "30 M_sun", "pi_interval": ["3", "22/7"],
                   "Gamma_interval": ["1/100", "1000"], "tau_B_D_interval_s": ["1e16", "1e19"]},
        "t_evap_s_interval": [sci(t_lo), sci(t_hi)],
        "ratio_t_evap_over_tau_interval": [sci(r_lo), sci(r_hi)],
        "ratio_lower_bound_floor_log10": floor_log10,
        "A7_decoupling_statement_at_30_Msun": status,
        "crossover_mass_kg_interval": [sci(ms_lo), sci(ms_hi)],
    }


# ---------------------------------------------------------------------------
# Self-checks on this source (no assert, no float/math)
# ---------------------------------------------------------------------------

def source_scan():
    with open(os.path.abspath(__file__), "rb") as fh:
        src = fh.read()
    names = {}
    for tok in tokenize.tokenize(io.BytesIO(src).readline):
        if tok.type == tokenize.NAME and tok.string in ("assert", "float", "math", "random"):
            names[tok.string] = names.get(tok.string, 0) + 1
    return names


# ---------------------------------------------------------------------------
# Verdicts
# ---------------------------------------------------------------------------

def decide(s8, am, gl, st, nm):
    claims = {}
    # A
    zero_bij = s8["MP1"]["tv_t2_hist"].get("0", 0) + s8["nested"]["tv_t3_hist"].get("0", 0)
    nonbij_rec = am["AM1_complete_access"]["nonbij_rec"]
    a_ok = zero_bij > 0 and nonbij_rec > 0 and nm["swap_into_remnant"]["tv_t1"] == 0
    claims["A"] = {"verdict": HOLDS if a_ok else NEG,
                   "bijections_zero_advantage_MP1_t2": s8["MP1"]["tv_t2_hist"].get("0", 0),
                   "bijections_zero_advantage_nested_t3": s8["nested"]["tv_t3_hist"].get("0", 0),
                   "nonbijective_maps_exact_recovery_complete_access": nonbij_rec,
                   "swap_into_remnant_tv": nm["swap_into_remnant"]["tv_t1"],
                   "erase_and_copy_tv": nm["erase_and_copy"]["tv_t1"]}
    # B
    b = {}
    for key, prof in st["B1_swap"].items():
        b["B1:" + key] = prof[0] == Fraction(1, 2 ** int(key.split("k=")[1].split(",")[0])) and prof[-1] == 1
    for key, prof in st["B1_swap_wide"].items():
        q = int(key.split("q=")[1].split(",")[0])
        b["B1w:" + key] = prof[0] == Fraction(1, q) and prof[-1] == 1
    for key, prof in st["B2_cnot"].items():
        b["B2:" + key] = prof[0] == 0 and prof[-1] == 1
    b["B3:GL42_all_recover_at_end"] = all(
        all(k.split(",")[-1] == kk for k in gl["by_k"][kk]["r_profile_hist"]) for kk in ("1", "2"))
    claims["B"] = {"verdict": HOLDS if all(b.values()) else NEG, "models_failing": sorted(k for k, v in b.items() if not v),
                   "models_tested": len(b)}
    # C1
    c1_viol = (s8["MP1"]["C1_violations_t3"] + s8["MP1_static"]["C1_violations_t3"]
               + s8["MP2"]["C1_violations_t3"] + am["AM1_complete_access"]["bij_norec"])
    cc_nobij = am["AM1_complete_access"]["nonbij_norec"]
    cc_noaccess = s8["MP1"]["tv_t2_hist"].get("0", 0) + s8["nested_W_endpoint"]["not_recover"]
    claims["C1"] = {"verdict": HOLDS if c1_viol == 0 else NEG, "violations": c1_viol,
                    "countercontrol_without_bijectivity_violations": cc_nobij,
                    "countercontrol_without_complete_access_violations": cc_noaccess}
    # C2
    c2_viol = (s8["MP1"]["C2_violations"] + s8["MP1_static"]["C2_violations"] + s8["MP2"]["C2_violations"]
               + am["AM2_remnant_bound"]["bij_violate"] + gl["by_k"]["1"]["C2_violations"]
               + gl["by_k"]["2"]["C2_violations"])
    claims["C2"] = {"verdict": HOLDS if c2_viol == 0 else NEG, "violations": c2_viol,
                    "MP2_min_psucc_t2": s8["MP2"]["min_psucc_t2"], "MP2_bound_t2": Fraction(1, 2),
                    "MP2_blind_guess": Fraction(1, 4), "MP2_tight": s8["MP2"]["min_psucc_t2"] == Fraction(1, 2),
                    "MP2_instances_attaining_bound": s8["MP2"]["attains_bound_t2"],
                    "MP2_instances_at_blind_guess": s8["MP2"]["blind_t2"],
                    "countercontrol_without_bijectivity_violations": am["AM2_remnant_bound"]["nonbij_violate"]}
    # C3
    nw = s8["nested_W_endpoint"]
    c3_viol = nw["C3_violations"] + nw["product_maps_not_recover"]
    claims["C3"] = {"verdict": HOLDS if c3_viol == 0 and nw["product_maps"] > 0 else NEG,
                    "product_maps": nw["product_maps"], "violations": c3_viol,
                    "countercontrol_B_D_leak_tv": nm["B_D_leak"]["tv_t2_W_read"],
                    "no_leak_reference_tv": nm["no_leak_reference"]["tv_t2_W_read"],
                    "countercontrol_nonproduct_not_recover": nw["not_recover"]}
    # C4
    c4_viol = gl["by_k"]["1"]["C4_violations"] + gl["by_k"]["2"]["C4_violations"]
    claims["C4"] = {"verdict": HOLDS if c4_viol == 0 else NEG, "violations": c4_viol,
                    "late_emergence": {k: gl["by_k"][k]["late_emergence_count"] for k in ("1", "2")},
                    "early_emergence": {k: gl["by_k"][k]["early_emergence_count"] for k in ("1", "2")}}
    # D1, D2, D3
    d1_viol = (s8["MP1"]["D1_violations"] + s8["MP1_static"]["D1_violations"] + s8["MP2"]["D1_violations"]
               + am["AM3_refinement"]["D1_violations"] + gl["by_k"]["1"]["D1_violations"]
               + gl["by_k"]["2"]["D1_violations"])
    swap_cum = nm["swap_in_swap_out"]["cumulative_tv"]
    if not nondecreasing(swap_cum):
        d1_viol += 1
    claims["D1"] = {"verdict": HOLDS if d1_viol == 0 else NEG, "violations": d1_viol}
    d2 = s8["snapshot"]["D2_decreasing"]
    claims["D2"] = {"verdict": HOLDS if d2 > 0 else NEG, "bijections_with_decreasing_snapshot_tv": d2,
                    "swap_in_swap_out_snapshot_tv": nm["swap_in_swap_out"]["snapshot_tv"],
                    "swap_in_swap_out_cumulative_tv": swap_cum}
    d3 = all(claims[x]["verdict"] == HOLDS for x in ("C1", "C2", "D1"))
    claims["D3"] = {"verdict": HOLDS if d3 else NEG, "conjunction_of": ["C1", "C2", "D1"]}
    # E
    e_ok = s8["nested"]["E_violations"] == 0 and s8["nested"]["E_zero_adv_instances"] > 0
    claims["E"] = {"verdict": HOLDS if e_ok else NEG, "violations": s8["nested"]["E_violations"],
                   "zero_advantage_bijections_satisfying_A1": s8["nested"]["E_zero_adv_instances"]}
    return claims


def verdict_lines(claims, f, overall):
    L = []
    L.append("Overall: %s (each claim is the plan's hypothesis; see PLAN.md section 3)." % overall)
    a = claims["A"]
    if a["verdict"] == HOLDS:
        reading = "bijectivity alone does not imply recovery from the accessible records in the tested class"
    else:
        reading = "no bijective instance without accessible recovery was found in the tested class"
    if claims["C1"]["verdict"] == HOLDS and claims["C2"]["verdict"] == HOLDS:
        reading += ("; with bijectivity, complete endpoint access gives exact recovery and an inaccessible "
                    "endpoint set K bounds the loss by P_succ >= 1/|K|")
    L.append("Reading: " + reading + ".")
    L.append("A (%s): %d of 40320 bijections of {0,1}^3 give zero accessible advantage with one mode "
             "unread after two emissions; %d give zero advantage in the nested V/B/D layout with V read; "
             "%d non-injective maps of {0,1}^2 recover the message exactly under complete access."
             % (a["verdict"], a["bijections_zero_advantage_MP1_t2"], a["bijections_zero_advantage_nested_t3"],
                a["nonbijective_maps_exact_recovery_complete_access"]))
    b = claims["B"]
    L.append("B (%s): %d transport models tested; failing: %s." % (
        b["verdict"], b["models_tested"], ", ".join(b["models_failing"]) or "none"))
    c1 = claims["C1"]
    L.append("C1 (%s): %d violations of exact recovery under bijectivity plus complete endpoint access; "
             "dropping bijectivity gives %d failures, dropping complete access gives %d failures."
             % (c1["verdict"], c1["violations"], c1["countercontrol_without_bijectivity_violations"],
                c1["countercontrol_without_complete_access_violations"]))
    c2 = claims["C2"]
    L.append("C2 (%s): %d violations of P_succ >= 1/|K|; two-bit message with a one-bit inaccessible "
             "remnant: minimum P_succ over S_8 = %s (bound %s, blind guess %s, %d instances attain the "
             "bound, %d at blind guess); without bijectivity %d maps violate the bound."
             % (c2["verdict"], c2["violations"], fr(c2["MP2_min_psucc_t2"]), fr(c2["MP2_bound_t2"]),
                fr(c2["MP2_blind_guess"]), c2["MP2_instances_attaining_bound"], c2["MP2_instances_at_blind_guess"],
                c2["countercontrol_without_bijectivity_violations"]))
    c3 = claims["C3"]
    L.append("C3 (%s): %d product maps W x D, %d violations; with B-D coupling the leak model has "
             "advantage %s with all of W read (reference without leak: %s)."
             % (c3["verdict"], c3["product_maps"], c3["violations"], fr(c3["countercontrol_B_D_leak_tv"]),
                fr(c3["no_leak_reference_tv"])))
    c4 = claims["C4"]
    L.append("C4 (%s): %d violations of max(0, t-(n-k)) <= r_t <= min(k, t) over GL(4,2); late-emergence "
             "profiles k=1: %d, k=2: %d; early-emergence profiles k=1: %d, k=2: %d."
             % (c4["verdict"], c4["violations"], c4["late_emergence"]["1"], c4["late_emergence"]["2"],
                c4["early_emergence"]["1"], c4["early_emergence"]["2"]))
    L.append("D1 (%s): %d violations of monotone accessible advantage under cumulative records."
             % (claims["D1"]["verdict"], claims["D1"]["violations"]))
    L.append("D2 (%s): %d bijections with decreasing snapshot advantage; swap-in/swap-out snapshot "
             "advantage %s, cumulative %s." % (
                 claims["D2"]["verdict"], claims["D2"]["bijections_with_decreasing_snapshot_tv"],
                 ",".join(fr(v) for v in claims["D2"]["swap_in_swap_out_snapshot_tv"]),
                 ",".join(fr(v) for v in claims["D2"]["swap_in_swap_out_cumulative_tv"])))
    L.append("D3 (%s): conjunction of C1, C2, D1." % claims["D3"]["verdict"])
    L.append("E (%s): %d violations of GR Theorem A.1 equality; %d zero-advantage bijections satisfy it."
             % (claims["E"]["verdict"], claims["E"]["violations"], claims["E"]["zero_advantage_bijections_satisfying_A1"]))
    L.append("F (audit): GR A.7 decoupling statement at 30 M_sun is %s; t_evap/tau_B^D lies in [%s, %s]; "
             "t_evap = tau_B^D at a mass in [%s, %s] kg." % (
                 f["A7_decoupling_statement_at_30_Msun"], f["ratio_t_evap_over_tau_interval"][0],
                 f["ratio_t_evap_over_tau_interval"][1], f["crossover_mass_kg_interval"][0],
                 f["crossover_mass_kg_interval"][1]))
    return L


def to_json(x):
    if isinstance(x, Fraction):
        return fr(x)
    if isinstance(x, dict):
        return {str(k): to_json(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [to_json(v) for v in x]
    return x


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = here
    if "--out" in argv:
        out_dir = argv[argv.index("--out") + 1]
    controls = run_controls()
    scan = source_scan()
    controls["source"] = {"no_assert": scan.get("assert", 0) == 0,
                          "no_float_math_random": all(scan.get(k, 0) == 0 for k in ("float", "math", "random"))}
    if not controls_pass(controls):
        print("VOID: fast control failure: %s" % json.dumps(to_json(controls), sort_keys=True))
        return 2
    s8 = s8_classes()
    am = all_maps_classes()
    gl = gl42_class()
    st = structured_families()
    nm = named_examples()
    controls["K1"]["labelled_bijections_verified"] = not LEDGER.k1_fail
    controls["K3"] = {"all_instances_agree": not LEDGER.k3_fail}
    controls["K4"]["GL42_count"] = gl["count"] == 20160 and gl["distinct_tables"] == 20160
    controls["K4"]["maps4_count"] = am["count"] == 256
    controls["K5"]["GL42_all"] = gl["K5_fail"] == 0
    if not controls_pass(controls):
        print("VOID: control failure: %s; K1 fails %s; K3 fails %s" % (
            json.dumps(to_json(controls), sort_keys=True), LEDGER.k1_fail, LEDGER.k3_fail))
        return 2
    claims = decide(s8, am, gl, st, nm)
    f = item_f()
    refuted = sorted(k for k, v in claims.items() if v["verdict"] != HOLDS)
    overall = HOLDS if not refuted else NEG + " (" + ", ".join(refuted) + ")"
    lines = verdict_lines(claims, f, overall)
    result = {
        "schema": "bh01-access-v1/result",
        "base_commit": BASE_COMMIT,
        "controls": controls,
        "control_counts": {"K1_maps_checked": LEDGER.k1_checked, "K3_figures_checked": LEDGER.k3_checked},
        "classes": {"S8": s8, "all_maps_2bit": am, "GL42": gl, "structured": st, "named": nm},
        "claims": claims,
        "item_F": f,
        "overall": overall,
        "verdict_text": lines,
    }
    data = json.dumps(to_json(result), sort_keys=True, indent=1, ensure_ascii=True) + "\n"
    with open(os.path.join(out_dir, "result.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(data)
    if "--sync-report" in argv:
        rp = os.path.join(here, "REPORT.md")
        with open(rp, encoding="utf-8") as fh:
            rep = fh.read()
        b, e = "<!-- generated:begin -->", "<!-- generated:end -->"
        i, j = rep.find(b), rep.find(e)
        if i < 0 or j < i:
            print("REPORT.md has no generated block")
            return 1
        block = b + "\n" + "\n".join("- " + ln for ln in lines) + "\n" + e
        with open(rp, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(rep[:i] + block + rep[j + len(e):])
    for ln in lines:
        print(ln)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
