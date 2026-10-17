"""LOC-1 preflight, leg T at C21: cost of the complete pruned search, on SYNTHETIC instances and on
controls whose answer is fixed by a written argument.  No frozen target lift (F, T, PF, Wd.P, Wd.PQ,
PQ.Dn), no carrier value of one, and no matrix built from H_i, F_16, W_d or tau is constructed here.
The one P0 object used is the admitted lift P = H_1 (x) H_1 (scaled by 4 to integers), whose declared
(identity) class is a product by construction.

Run:  python3 -I c21_search.py [WITNESS.json]      (stdout deterministic; timing on stderr)
Self-contained: imports only the standard library and c21_engine.py from this directory, reads only
frozen_inputs.json from this directory, and by default writes c21_witness.json here.
"""
import sys
import os
import json
import time
import resource
from math import factorial, gcd
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, HERE)
from c21_engine import Engine, SM64, kron, relabel, canonical, MUTATIONS, PR  # noqa: E402

OUT, FAILS, WIT = [], [], []
BUDGET_EXIST = 2 * 10 ** 7          # preflight cap per run (tested nodes); the frozen budget is a decision
BUDGET_ALL = 2 * 10 ** 7
WCAP16 = 2000                       # 16-point runs: witnesses verified in-suite and stored (total recorded);
                                    # small shapes (N <= 9) keep every witness for the brute-force replay


def say(*a):
    OUT.append(" ".join(str(x) for x in a))


def check(name, ok, detail=""):
    say("CONTROL", name, "PASS" if ok else "FAIL", detail)
    if not ok:
        FAILS.append(name)
    return ok


def tlog(*a):
    print("TIMING", *a, file=sys.stderr, flush=True)


# ---------------------------------------------------------------- independent exact factor check

def verify_kron(M, sig, m, n):
    """Explicit factor reconstruction, exact (Fractions): M^sig == A (x) B ?  (separate from leaf_ok)."""
    N = m * n
    K = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            K[sig[i]][sig[j]] = Fraction(M[i][j])
    piv = next(((p, q) for p in range(N) for q in range(N) if K[p][q] != 0), None)
    if piv is None:
        return True
    (a0, b0), (a1, b1) = divmod(piv[0], n), divmod(piv[1], n)
    A = [[K[a * n + b0][a2 * n + b1] for a2 in range(m)] for a in range(m)]
    B = [[K[a0 * n + b][a1 * n + b2] / K[piv[0]][piv[1]] for b2 in range(n)] for b in range(n)]
    return all(K[a * n + b][a2 * n + b2] == A[a][a2] * B[b][b2]
               for a in range(m) for b in range(n) for a2 in range(m) for b2 in range(n))


# ---------------------------------------------------------------- synthetic instances

def rmat(rng, k, vals):
    return [[vals[rng.below(len(vals))] for _ in range(k)] for _ in range(k)]


def eye(k):
    return [[1 if i == j else 0 for j in range(k)] for i in range(k)]


def ones(k):
    return [[1] * k for _ in range(k)]


def perm_matrix(pi):
    N = len(pi)
    M = [[0] * N for _ in range(N)]
    for j in range(N):
        M[pi[j]][j] = 1
    return M


def perm_of_type(lengths, labels):
    pi = [None] * sum(lengths)
    k = 0
    for L in lengths:
        cyc = labels[k:k + L]
        for t in range(L):
            pi[cyc[t]] = cyc[(t + 1) % L]
        k += L
    return pi


def cycle_type(pi):
    seen, out = set(), []
    for s in range(len(pi)):
        if s in seen:
            continue
        L, x = 0, s
        while x not in seen:
            seen.add(x)
            x = pi[x]
            L += 1
        out.append(L)
    return tuple(sorted(out, reverse=True))


def partitions(k, maxpart=None):
    maxpart = maxpart or k
    if k == 0:
        yield ()
        return
    for p in range(min(k, maxpart), 0, -1):
        for rest in partitions(k - p, p):
            yield (p,) + rest


def product_type_formula(t1, t2):
    out = []
    for k in t1:
        for l in t2:
            g = gcd(k, l)
            out += [k * l // g] * g
    return tuple(sorted(out, reverse=True))


def graph_matrix(adj, N):
    return [[1 if adj(i, j) else 0 for j in range(N)] for i in range(N)]


def popcount(x):
    return bin(x).count("1")


def gid(m, n):
    """Order of the class group: S_m x S_n, times 2 when m = n."""
    return factorial(m) * factorial(n) * (2 if m == n else 1)


# ---------------------------------------------------------------- running one instance

def run_instance(name, mats, m, n, mode, expect=None, planted=None, rules="RWVP", order="greedy",
                 arith="modp", mut=None, budget=None, record=True, knuth=0):
    budget = budget or (BUDGET_EXIST if mode == "exist" else BUDGET_ALL)
    E = Engine(mats, m, n, rules=rules, order=order, arith=arith, mut=mut)
    t0 = time.perf_counter()
    status, found, (tested, acc, leaves) = E.run(mode, budget)
    dt = time.perf_counter() - t0
    canon = [canonical(s, m, n, E.order) for s in found]
    res = {"name": name, "m": m, "n": n, "mode": mode, "status": status, "found": len(found),
           "tested": tested, "accepted": acc, "leaves": leaves, "rules": rules, "order": order,
           "arith": arith, "mut": mut, "canon": canon, "found_sigmas": found, "order_list": E.order}
    WCAP = len(found) if m * n <= 9 else WCAP16
    res["verified"] = all(verify_kron(M, s, m, n) for s in found[:WCAP] for M in mats)
    res["distinct"] = len(set(canon)) == len(canon) and all(c == s for c, s in zip(canon, found))
    if planted is not None:
        res["planted_found"] = canonical(planted, m, n, E.order) in set(canon)
    if knuth and status == "EXHAUSTED":
        tk = time.perf_counter()
        ea, et = E.knuth(knuth, 0x4B4E555448 + len(name))
        res["knuth"] = (int(ea), int(et))
        tlog("knuth %-40s probes %d  %.2fs" % (name, knuth, time.perf_counter() - tk))
    if mut is None:
        tlog("%-44s %-5s %-9s tested %10d  %.3fs  %.2f us/tested" % (name, mode, status, tested, dt,
                                                                    1e6 * dt / max(1, tested)))
    if record:
        line = ("RUN %-44s %-5s %-9s found %6d  tested %10d  accepted %9d  leaves %8d  rules %-3s order %s"
                % (name, mode, status, len(found), tested, acc, leaves, rules, order))
        if "planted_found" in res:
            line += "  planted-class-found %s" % res["planted_found"]
        if "knuth" in res:
            line += "  knuth-estimate accepted %d tested %d" % res["knuth"]
        say(line)
        if expect is not None:
            ok = {"some": status == "FOUND" or (status == "ALL" and len(found) > 0),
                  "none": status == "NONE" or (status == "ALL" and len(found) == 0),
                  "all": status in ("FOUND", "ALL", "EXHAUSTED") and len(found) > 0}[expect]
            res["expect_ok"] = ok
        WIT.append({"name": name, "m": m, "n": n, "mode": mode, "status": status, "mats": mats,
                    "found": [list(s) for s in found[:WCAP]], "found_total": len(found),
                    "planted": list(planted) if planted else None, "expect": expect})
    if len(found) > WCAP:
        res["found_sigmas"] = found[:WCAP]
        res["canon"] = canon[:WCAP]
    return res


def control_line(res, label):
    if res["mode"] == "all" and res["status"] == "EXHAUSTED":
        say("BOUNDED", label, res["name"], "all: enumeration exhausted the cap after %d classes; "
            "not a control (the existence-mode run is)" % res["found"])
        return True
    ok = res["verified"] and res["distinct"]
    if "planted_found" in res:
        ok = ok and res["planted_found"]
    if "expect_ok" in res:
        ok = ok and res["expect_ok"]
    return check(label, ok, res["name"] + " " + res["mode"] + " " + res["status"])


# ---------------------------------------------------------------- the suites

def small_shapes(mut=None, record=True):
    """K-canon / K-search on small shapes: identity (every class), planted, random, permutations."""
    rng = SM64(0x534D414C4C)
    results = []
    for (m, n) in [(2, 2), (2, 3), (3, 2), (2, 4), (4, 2), (3, 3)]:
        N = m * n
        tot = factorial(N) // gid(m, n)
        r = run_instance("small %dx%d identity" % (m, n), [eye(N)], m, n, "all", expect="all", mut=mut,
                         record=record)
        okc = r["status"] == "ALL" and r["found"] == tot and r["distinct"]
        if record:
            check("K-canon %dx%d" % (m, n), okc, "found %d classes, N!/|G| = %d" % (r["found"], tot))
        results.append(("K-canon %dx%d" % (m, n), okc))
        for t in range(3):
            A = rmat(rng, m, [-2, -1, 0, 1, 2, 3])
            B = rmat(rng, n, [-2, -1, 0, 1, 2, 3])
            sig = rng.shuffle(range(N))
            r = run_instance("small %dx%d planted %d" % (m, n, t), [relabel(kron(A, B), sig)], m, n, "all",
                             planted=sig, mut=mut, record=record)
            ok = r["verified"] and r["distinct"] and r["planted_found"]
            results.append(("K-search-planted %dx%d %d" % (m, n, t), ok))
            if record:
                control_line(r, "K-search-planted")
        for t in range(2):
            M = rmat(rng, N, [-3, -2, -1, 0, 1, 2, 3])
            r = run_instance("small %dx%d random %d" % (m, n, t), [M], m, n, "all", mut=mut, record=record)
            results.append(("K-search-random %dx%d %d" % (m, n, t), r["verified"] and r["distinct"]))
        lab = rng.shuffle(range(N))
        pi = perm_of_type([2] + [1] * (N - 2), lab)
        r = run_instance("small %dx%d transposition" % (m, n), [perm_matrix(pi)], m, n, "all", mut=mut,
                         record=record)
        results.append(("K-search-transposition %dx%d" % (m, n), r["verified"] and r["distinct"]))
    return results


def cycle_table():
    types = {}
    for t1 in partitions(4):
        for t2 in partitions(4):
            types.setdefault(product_type_formula(t1, t2), []).append((t1, t2))
    # control: the formula agrees with an explicit product permutation for every pair of types
    bad = 0
    for t1 in partitions(4):
        for t2 in partitions(4):
            p1, p2 = perm_of_type(list(t1), list(range(4))), perm_of_type(list(t2), list(range(4)))
            prod = [p1[g // 4] * 4 + p2[g % 4] for g in range(16)]
            if cycle_type(prod) != product_type_formula(t1, t2):
                bad += 1
    check("K-cycle-formula", bad == 0, "25 type pairs of S_4 x S_4; %d types of pi_1 x pi_2" % len(types))
    say("cycle types of pi_1 x pi_2 on 4 x 4:", sorted(types))
    return set(types)


def big_suite():
    rng = SM64(0x4C4F43312D433231)            # "LOC1-C21"
    res = []
    N, m, n = 16, 4, 4
    I16, J16 = eye(16), ones(16)
    # --- the P0 control: P = H_1 (x) H_1, scaled by 4; its declared class is a product
    with open(os.path.join(HERE, "frozen_inputs.json")) as fh:
        H = json.load(fh)["P0_H1_times_2"]
    check("K-input-H", all(x in (1, -1) for r in H for x in r) and
          all(sum(H[i][k] * H[j][k] for k in range(4)) == (4 if i == j else 0) for i in range(4) for j in range(4)),
          "frozen_inputs.json P0_H1_times_2 is a 4x4 +-1 matrix with H H^T = 4 I")
    P = kron(H, H)
    ident = tuple(range(16))
    for mode in ("exist", "all"):
        r = run_instance("P0 control P = H1(x)H1", [P], m, n, mode, expect="some",
                         planted=ident if mode == "all" else None, knuth=2000)
        control_line(r, "K-rel-pos-P")
        res.append(r)
    # --- planted products relabelled by fixed-seed sigma*
    fams = [("dense", [-3, -2, -1, 1, 2, 3]), ("with-zeros", [-2, -1, 0, 0, 1, 2]),
            ("repeated{1,2}", [1, 2]), ("signs", [-1, 1])]
    for fam, vals in fams:
        for t in range(5):
            A, B = rmat(rng, 4, vals), rmat(rng, 4, vals)
            sig = rng.shuffle(range(16))
            M = relabel(kron(A, B), sig)
            for mode in ("exist", "all"):
                r = run_instance("planted %s %d" % (fam, t), [M], m, n, mode, expect="some",
                                 planted=sig if mode == "all" else None, knuth=2000)
                control_line(r, "K-plant")
                res.append(r)
    # 0/1 symmetric factors with large automorphism groups
    C4 = [[1 if (i - j) % 4 in (1, 3) else 0 for j in range(4)] for i in range(4)]
    K4 = [[0 if i == j else 1 for j in range(4)] for i in range(4)]
    J2J2 = [[1 if i // 2 == j // 2 else 0 for j in range(4)] for i in range(4)]
    for nm, A, B in [("C4 x C4 (tensor)", C4, C4), ("K4 x K4 (tensor; complement of rook)", K4, K4),
                     ("J4 (x) I4", ones(4), eye(4)), ("C4 (x) (J2+J2)", C4, J2J2)]:
        sig = rng.shuffle(range(16))
        M = relabel(kron(A, B), sig)
        for mode in ("exist", "all"):
            r = run_instance("planted 0/1 " + nm, [M], m, n, mode, expect="some",
                             planted=sig if mode == "all" else None, knuth=2000)
            control_line(r, "K-plant")
            res.append(r)
    # joint targets: two products under one sigma*
    for t in range(3):
        sig = rng.shuffle(range(16))
        Ms = [relabel(kron(rmat(rng, 4, [-2, -1, 0, 1, 2]), rmat(rng, 4, [-2, -1, 0, 1, 2])), sig)
              for _ in range(2)]
        for mode in ("exist", "all"):
            r = run_instance("joint planted pair %d" % t, Ms, m, n, mode, expect="some",
                             planted=sig if mode == "all" else None)
            control_line(r, "K-plant-joint")
            res.append(r)
    # --- every class: identity and J (existence only; enumeration is 1.8e10 classes)
    for nm, M in (("identity", I16), ("all-ones J", J16)):
        r = run_instance(nm, [M], m, n, "exist", expect="all")
        control_line(r, "K-all")
        res.append(r)
    r = run_instance("identity", [I16], m, n, "all", knuth=2000, budget=2 * 10 ** 6)
    say("NOTE identity enumeration is expected to exhaust any budget: 18162144000 classes")
    res.append(r)
    # --- permutation matrices, decided by cycle type (W-PERM)
    admitted = cycle_table()
    ptypes = [(2,) + (1,) * 14, (16,), (8, 8), (4, 4, 4, 4), (2,) * 8, (15, 1), (12, 4), (6, 6, 2, 2),
              (4, 4, 4, 2, 2), (3, 3, 3, 3, 1, 1, 1, 1), (2, 2) + (1,) * 12, (3, 1) + (1,) * 12,
              (2, 2, 2, 2) + (1,) * 8, (5, 5, 5, 1), (7, 7, 1, 1), (4, 4, 2, 2, 2, 2),
              (2, 2, 2) + (1,) * 10, (2,) * 5 + (1,) * 6, (2,) * 7 + (1,) * 2, (3, 3, 3) + (1,) * 7,
              (2,) * 6 + (1,) * 4, (6, 3, 3, 2, 1, 1), (3, 3, 3, 3, 3, 1)]
    for ct in ptypes:
        for lab_kind in ("consecutive", "seeded"):
            lab = list(range(16)) if lab_kind == "consecutive" else rng.shuffle(range(16))
            pi = perm_of_type(list(ct), lab)
            exp = "some" if ct in admitted else "none"
            nm = "perm %s %s [%s]" % ("".join("%d." % x for x in ct).rstrip("."), lab_kind,
                                      "admitted" if exp == "some" else "excluded")
            r = run_instance(nm, [perm_matrix(pi)], m, n, "exist", expect=exp, knuth=2000)
            control_line(r, "K-perm")
            res.append(r)
            if exp == "some":
                r = run_instance(nm, [perm_matrix(pi)], m, n, "all", knuth=2000, budget=2 * 10 ** 6)
                res.append(r)
    # --- 0/1 graphs with large automorphism groups and no product class (written arguments)
    graphs = {
        "Q4 hypercube": lambda i, j: popcount(i ^ j) == 1,
        "rook K4 box K4": lambda i, j: i != j and (i // 4 == j // 4 or i % 4 == j % 4),
        "Shrikhande": lambda i, j: ((i // 4 - j // 4) % 4, (i % 4 - j % 4) % 4) in
        {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)},
        "Clebsch": lambda i, j: popcount(i ^ j) in (1, 4),
        "I + J": lambda i, j: True,
        "J - I": lambda i, j: i != j,
    }
    for nm, adj in graphs.items():
        G = graph_matrix(adj, 16)
        if nm == "I + J":
            G = [[G[i][j] + (1 if i == j else 0) for j in range(16)] for i in range(16)]
        for lab_kind in ("declared", "seeded"):
            sig = list(range(16)) if lab_kind == "declared" else rng.shuffle(range(16))
            M = relabel(G, sig)
            r = run_instance("graph %s %s" % (nm, lab_kind), [M], m, n, "exist", expect="none", knuth=2000)
            control_line(r, "K-none-graph")
            res.append(r)
    # --- near-identity I + E_{14,15}: no class (support size 17 is prime and both factors have >= 4)
    NI = [row[:] for row in I16]
    NI[14][15] = 1
    for order, rules in (("greedy", "RWVP"), ("nat", "RWVP"), ("greedy", "RWV"), ("nat", "RWV")):
        r = run_instance("near-identity I+E(14,15) order=%s rules=%s" % (order, rules), [NI], m, n, "exist",
                         expect="none", order=order, rules=rules, knuth=2000, budget=2 * 10 ** 6)
        if (order, rules) == ("greedy", "RWVP"):
            control_line(r, "K-none-near-identity")
        else:
            say("NOTE adversarial-order/ablation demonstration, not a control:", r["name"], r["status"])
        res.append(r)
    # --- random non-product matrices (synthetic outcome; every find verified)
    for fam, vals in [("dense ints", list(range(-9, 10))), ("{1,2}", [1, 2]), ("signs", [-1, 1]),
                      ("sparse 0/1", [0, 0, 0, 1])]:
        for t in range(5):
            M = rmat(rng, 16, vals)
            r = run_instance("random %s %d" % (fam, t), [M], m, n, "exist", knuth=2000)
            check("K-verify", r["verified"] and r["distinct"], r["name"])
            res.append(r)
    # --- near-products: one entry of a planted product changed by +1 (synthetic outcome)
    for t in range(5):
        A, B = rmat(rng, 4, [-2, -1, 1, 2]), rmat(rng, 4, [-2, -1, 1, 2])
        sig = rng.shuffle(range(16))
        M = relabel(kron(A, B), sig)
        M[rng.below(16)][rng.below(16)] += 1
        r = run_instance("near-product %d" % t, [M], m, n, "exist", knuth=2000)
        check("K-verify", r["verified"] and r["distinct"], r["name"])
        res.append(r)
    return res


def ablation_and_arith():
    """Completeness does not depend on pruning; exact and mod-p N2 agree."""
    rng = SM64(0x41424C)
    insts = []
    for t in range(3):
        A, B = rmat(rng, 4, [-1, 0, 1, 2]), rmat(rng, 4, [-1, 0, 1, 2])
        sig = rng.shuffle(range(16))
        insts.append(("ablation planted %d" % t, [relabel(kron(A, B), sig)], sig))
    C4 = [[1 if (i - j) % 4 in (1, 3) else 0 for j in range(4)] for i in range(4)]
    sig = rng.shuffle(range(16))
    insts.append(("ablation planted C4 x C4", [relabel(kron(C4, C4), sig)], sig))
    pi = perm_of_type([2] + [1] * 14, rng.shuffle(range(16)))
    insts.append(("ablation transposition", [perm_matrix(pi)], None))
    for nm, mats, sig in insts:
        ref = None
        # W-COL alone (rules=WV) cannot prune a permutation matrix (every column profile has one nonzero)
        for rules in (("RWVP", "RWV", "RW", "R", "RP") if sig is None else ("RWVP", "RWV", "RW", "R", "RP", "WV")):
            r = run_instance(nm + " rules=" + rules, mats, 4, 4, "all", rules=rules, planted=sig,
                             budget=4 * 10 ** 7)
            s = (r["status"], sorted(r["canon"]))
            if ref is None:
                ref = s
            check("K-ablation", s == ref and r["status"] == "ALL", nm + " rules=" + rules)
        rx = run_instance(nm + " arith=exact", mats, 4, 4, "all", arith="exact", planted=sig,
                          budget=4 * 10 ** 7)
        rp = run_instance(nm + " arith=modp", mats, 4, 4, "all", arith="modp", planted=sig,
                          budget=4 * 10 ** 7, record=False)
        check("K-arith", (rx["status"], sorted(rx["canon"])) == (rp["status"], sorted(rp["canon"]))
              and rp["accepted"] >= rx["accepted"],
              "%s exact accepted %d, modp accepted %d" % (nm, rx["accepted"], rp["accepted"]))


def collision_instance():
    """Dense planted product with one entry raised by PR: images mod PR are a product under sigma*,
    the exact matrix has no product class (written argument W-COLL)."""
    rng = SM64(0x434F4C4C)
    A, B = rmat(rng, 4, [-3, -2, -1, 1, 2, 3]), rmat(rng, 4, [-3, -2, -1, 1, 2, 3])
    sig = rng.shuffle(range(16))
    M = relabel(kron(A, B), sig)
    M[rng.below(16)][rng.below(16)] += PR
    return M, sig


def collision_control(mut=None, record=True):
    M, sig = collision_instance()
    r = run_instance("mod-p collision (rules=R)", [M], 4, 4, "all", rules="R", mut=mut, record=record)
    ok = r["status"] == "ALL" and r["found"] == 0 and r["leaves"] >= 1 and r["verified"]
    if record:
        check("K-collision", ok, "leaves reached %d (the sigma* leaf passes every mod-p test), classes %d"
              % (r["leaves"], r["found"]))
    return ok


def mutation_planted(mut):
    """4x4 planted products (zeros and non-symmetric factors) in enumeration mode, plus the transposition."""
    rng = SM64(0x4D5554)
    oks = []
    for t in range(6):
        A, B = rmat(rng, 4, [-2, -1, 0, 1, 2]), rmat(rng, 4, [-2, -1, 0, 1, 2])
        sig = rng.shuffle(range(16))
        r = run_instance("mut planted %d" % t, [relabel(kron(A, B), sig)], 4, 4, "all", planted=sig, mut=mut,
                         record=False, budget=4 * 10 ** 7)
        oks.append(r["status"] == "ALL" and r["planted_found"] and r["verified"] and r["distinct"])
    pi = perm_of_type([2] + [1] * 14, rng.shuffle(range(16)))
    r = run_instance("mut transposition", [perm_matrix(pi)], 4, 4, "all", mut=mut, record=False)
    oks.append(r["status"] == "ALL" and r["found"] == 0)
    return all(oks)


def mutation_harness():
    lines = []
    allok = True
    for mut in MUTATIONS:
        t0 = time.perf_counter()
        small = small_shapes(mut=mut, record=False)
        small_ok = all(ok for _, ok in small)
        planted_ok = mutation_planted(mut)
        coll_ok = collision_control(mut=mut, record=False)
        failed = [lab for lab, ok in (("K-canon/K-search(small)", small_ok), ("K-plant(4x4)", planted_ok),
                                      ("K-collision", coll_ok)) if not ok]
        detected = bool(failed)
        allok &= detected
        lines.append("MUTATION %-19s %s  (controls failed: %s)"
                     % (mut, "DETECTED" if detected else "NOT DETECTED", ", ".join(failed) or "none"))
        tlog("mutation %s %.2fs" % (mut, time.perf_counter() - t0))
    return lines, allok


def main():
    global BUDGET_EXIST, BUDGET_ALL
    wpath = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "c21_witness.json")
    if len(sys.argv) > 2:                       # calibration only
        BUDGET_EXIST = BUDGET_ALL = int(sys.argv[2])
    T0 = time.perf_counter()
    say("== small shapes: K-canon and K-search inputs")
    small_shapes()
    say("== 16 points as 4 x 4: proxies (preflight cap %d tested nodes per run unless stated)" % BUDGET_EXIST)
    res = big_suite()
    say("== ablation and arithmetic cross-checks")
    ablation_and_arith()
    say("== mod-p collision control")
    collision_control()
    T1 = time.perf_counter()
    mlines, mok = mutation_harness()
    T2 = time.perf_counter()
    # summary of node counts over the proxies that terminated in existence mode
    say("== summary")
    for mode in ("exist", "all"):
        done = [r for r in res if r["mode"] == mode and r["status"] != "EXHAUSTED"]
        exh = [r for r in res if r["mode"] == mode and r["status"] == "EXHAUSTED"]
        if done:
            ts = sorted(r["tested"] for r in done)
            say("mode %s: %d runs complete; tested nodes min %d median %d max %d (%s); %d runs exhausted the cap: %s"
                % (mode, len(done), ts[0], ts[len(ts) // 2], ts[-1],
                   max(done, key=lambda r: r["tested"])["name"], len(exh), [r["name"] for r in exh]))
    for line in OUT:
        print(line)
    for line in mlines:
        print(line)
    green = not FAILS and mok
    print("C21 PREFLIGHT:", "CONTROLS GREEN" if green else "VOID (failed: %s)" % sorted(set(FAILS)))
    with open(wpath, "w") as f:
        json.dump(WIT, f, sort_keys=True, separators=(",", ":"))
    tlog("suite_s %.1f  mutation_harness_s %.1f  peak_rss_kB %d"
         % (T1 - T0, T2 - T1, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))


if __name__ == "__main__":
    main()
