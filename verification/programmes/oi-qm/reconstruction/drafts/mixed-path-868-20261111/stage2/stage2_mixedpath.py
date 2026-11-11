#!/usr/bin/env python3
"""MIXED-PATH-1 Stage 2: the preregistered exact computation of STAGE2-PREREG.md.

Usage:  python3 stage2_mixedpath.py --selftest      (dummy rule only; steps no rule of section 2.2)
        python3 stage2_mixedpath.py                 (the registered run)

Integers and Fractions only.  Printed output is diagnostic; a consumer reads the exit line of
invocations.jsonl and runs/<n>/results.json.
"""
import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"

import ast
import datetime
import hashlib
import inspect
import itertools
import json
import resource
import shutil
import signal
import time
from fractions import Fraction

import numpy as np

import s2_linalg as la
import s2_solver as sol
import s2_stepper as stp
import s2_verify as ver

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "invocations.jsonl")
STAGING = os.path.join(HERE, "staging")
RUNS = os.path.join(HERE, "runs")
PREREG = os.path.join(os.path.dirname(HERE), "STAGE2-PREREG.md")
MODULES = ["s2_linalg.py", "s2_solver.py", "s2_stepper.py", "s2_verify.py", "stage2_mixedpath.py"]

SCHEMA = "mixed-path-1/stage2/v1"
PREREG_SHA256 = "1ee9fd8f7322921bee73e3069ee8cfa9d86e5b380981ea6018f799a2cc43fb74"
CORPUS_PIN = "cac5d26441dd33e9348151487e4df7b547195481"

BLOCK = 1 << 16
PASS_LIMIT_NS = 90 * 60 * 10 ** 9
RSS_LIMIT_BYTES = 2 * (1 << 30)
LP_EACH_NS = 10 * 60 * 10 ** 9
LP_TOTAL_NS = 30 * 60 * 10 ** 9
AGGREGATE_ABOVE = 4096

# ---- frozen lists of STAGE2-PREREG.md ------------------------------------------------------
FROZEN_F = {
    ("R-round", 2): (0, 0, 1, 1, 1, 0, 0),
    ("R-round", 3): (0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1),
    ("R-lin", 2): (0, 1, 0, 1, 0, 1, 0),
    ("R-lin", 3): (0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0),
    ("R-lin", 5): (0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4),
    ("R-norm", 5): (0, 2, 4, 1, 3, 0, 2, 4, 1, 3, 0, 2, 4, 1, 3, 0, 2, 4, 1, 3, 0, 2, 4, 1, 3),
    ("dummy", 2): (1, 0, 0, 1, 0, 1, 1),
}
# extra self-test coverage only (IMPLEMENTATION-NOTES.md): a second table outside the corpus, q = 3
DUMMY3 = (1, 2, 2, 0, 1, 0, 0, 2, 1, 1, 0, 2, 0)
DUMMY_AFFINE = ("dummy-affine", 7, 3)
FROZEN_WINDOWS = {
    6: [(2, 2), (2, 3)],
    8: [(2, 2), (2, 3)],
    10: [(2, 2), (2, 3), (4, 4), (4, 5)],
    12: [(2, 2), (2, 3), (4, 4), (4, 5), (4, 6)],
}
FROZEN_WINGS = {2: ["S"], 4: ["S", "I", "O"]}
FROZEN_PATCH = [((2, 0, 0), [2, 3]), ((1, 1, 0), [2]), ((4, 0, 0), [4, 5, 6]),
                ((3, 1, 0), [4, 5]), ((2, 2, 0), [4]), ((2, 1, 1), [4])]
BRUTE_RULES = [("R-round", 2), ("R-round", 3), ("R-lin", 3)]
LA_RULES = [("R-lin", 2), ("R-lin", 3), ("R-lin", 5), ("R-norm", 5)]


class InvariantFailure(Exception):
    pass


class BoundReached(Exception):
    pass


class Terminated(Exception):
    pass


# ---- rule tables: the one dictionary through which rule labels reach the steppers -----------
F_TABLES = {}


def build_tables():
    F_TABLES.clear()
    for q in (2, 3):
        F_TABLES[("R-round", q)] = tuple(((s + 1) // 3) % q for s in range(6 * (q - 1) + 1))
    for q in (2, 3, 5):
        F_TABLES[("R-lin", q)] = tuple(s % q for s in range(6 * (q - 1) + 1))
    F_TABLES[("R-norm", 5)] = tuple((pow(3, -1, 5) * s) % 5 for s in range(25))
    F_TABLES[("dummy", 2)] = (1, 0, 0, 1, 0, 1, 1)
    F_TABLES[("dummy3", 3)] = DUMMY3


def table_for(rule, q):
    return F_TABLES[(rule, q)]


# ---- small helpers -------------------------------------------------------------------------
def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    with open(path, "rb") as fh:
        return sha256_bytes(fh.read())


def program_sha256():
    h = hashlib.sha256()
    for name in MODULES:
        with open(os.path.join(HERE, name), "rb") as fh:
            data = fh.read()
        h.update(name.encode() + b"\0" + str(len(data)).encode() + b"\0" + data)
    return h.hexdigest()


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def frac_str(fr):
    return "%d/%d" % (fr.numerator, fr.denominator)


def rss_bytes():
    with open("/proc/self/statm") as fh:
        return int(fh.read().split()[1]) * os.sysconf("SC_PAGE_SIZE")


def lcg_stream(s0, n):
    """n successive outputs s1..sn of s <- (1103515245 s + 12345) mod 2^31 (s0 is the seed)."""
    M = 1 << 31
    A = 1103515245
    C = 12345
    out = np.empty(n, dtype=np.uint64)
    out[0] = (A * s0 + C) % M
    have = 1
    Am, Cm = A, C
    while have < n:
        take = min(have, n - have)
        out[have:have + take] = (np.uint64(Am) * out[:take] + np.uint64(Cm)) % np.uint64(M)
        Am, Cm = (Am * Am) % M, (Am * Cm + Cm) % M
        have += take
    return out


def lcg_loop(s0, n):
    s = s0
    out = []
    for _ in range(n):
        s = (1103515245 * s + 12345) % (1 << 31)
        out.append(s)
    return out


def literal_roll_sum(a):
    """The literal six-shift np.roll sum over the last three axes."""
    return (np.roll(a, 1, axis=-3) + np.roll(a, -1, axis=-3) + np.roll(a, 1, axis=-2)
            + np.roll(a, -1, axis=-2) + np.roll(a, 1, axis=-1) + np.roll(a, -1, axis=-1))


class Geo:
    def __init__(self, L):
        self.L = L
        self.subs, self.pos, self.nbr = stp.class_geometry(L)
        par = np.zeros((L, 2, 2), dtype=np.int64)
        for (x, y, z) in stp.thin_sites(L):
            par[x, y, z] = (x + y + z) % 2
        self.par = par


_GEO = {}


def geo(L):
    if L not in _GEO:
        _GEO[L] = Geo(L)
    return _GEO[L]


def thin_dist(s, t, L):
    dx = abs(s[0] - t[0])
    return min(dx, L - dx) + (1 if s[1] != t[1] else 0) + (1 if s[2] != t[2] else 0)


def cname(c):
    return "%s@(%d,%d,%d)" % (c[0], c[1][0], c[1][1], c[1][2])


# ---- execution context ---------------------------------------------------------------------
class Ctx:
    def __init__(self, selftest, plant):
        self.selftest = selftest
        self.plant = plant
        self.controls = {}
        self.invariants = []
        self.start_ns = time.monotonic_ns()
        self.pass_start_ns = self.start_ns
        self.budget = sol.Budget(LP_EACH_NS, LP_TOTAL_NS)
        self.loc_cache = {}
        self.certs = {}
        self.counters = {"every_run_checks": 0, "prior_digest_checks": 0, "certificates_verified": 0,
                         "exclusivity_checks": 0, "window_asserts": 0, "record_tick_asserts": 0,
                         "partition_compares": 0}
        self.bound = None

    def control(self, cid, green, nonvacuous, counts, detail):
        self.controls[cid] = {"id": cid, "green": bool(green and nonvacuous), "nonvacuous": bool(nonvacuous),
                              "counts": counts, "detail": detail}

    def invariant(self, name, ok, measured):
        self.invariants.append({"name": name, "ok": bool(ok), "measured": measured})
        if not ok:
            raise InvariantFailure(name)

    def check_bounds(self):
        if time.monotonic_ns() - self.pass_start_ns > PASS_LIMIT_NS:
            raise BoundReached("timeout")
        if rss_bytes() > RSS_LIMIT_BYTES:
            raise BoundReached("memory")


# ---- invariant checkpoints of section 5 ----------------------------------------------------
def inv_static(ctx):
    trees = {}
    for name in MODULES:
        with open(os.path.join(HERE, name)) as fh:
            trees[name] = ast.parse(fh.read())
    banned_attr = {"float64", "float32", "float16", "longdouble", "mean", "true_divide", "sqrt", "linprog",
                   "average", "std", "var"}
    hits = []
    for name, tree in trees.items():
        for node in ast.walk(tree):
            if isinstance(node, ast.Div):
                hits.append([name, "true division"])
            elif isinstance(node, ast.Constant) and type(node.value).__name__ in ("float", "complex"):
                hits.append([name, "float constant"])
            elif isinstance(node, ast.Name) and node.id in ("float", "math", "complex"):
                hits.append([name, "name " + node.id])
            elif isinstance(node, ast.Attribute) and node.attr in banned_attr:
                hits.append([name, "attribute " + node.attr])
            elif (isinstance(node, ast.Attribute) and node.attr == "time"
                  and isinstance(node.value, ast.Name) and node.value.id == "time"):
                hits.append([name, "time.time"])
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                mods = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module]
                if "math" in mods:
                    hits.append([name, "import math"])
    ctx.invariant("exact-arithmetic-static", not hits, {"modules": len(trees), "hits": hits})
    # (iv) the linear-algebra module does not import the stepper
    imported = []
    for node in ast.walk(trees["s2_linalg.py"]):
        if isinstance(node, ast.Import):
            imported += [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module)
    ctx.invariant("linalg-does-not-import-stepper", "s2_stepper" not in imported, {"imports": sorted(imported)})

    # (iii) table look-ups (the write of a stepped state) occur only inside the two steppers
    def take_sites(tree):
        res = []
        for fn in ast.walk(tree):
            if isinstance(fn, ast.FunctionDef):
                for node in ast.walk(fn):
                    if isinstance(node, ast.Attribute) and node.attr == "take":
                        res.append(fn.name)
        tot = sum(1 for node in ast.walk(tree) if isinstance(node, ast.Attribute) and node.attr == "take")
        return res, tot
    in_stepper, tot_stepper = take_sites(trees["s2_stepper.py"])
    elsewhere = sum(take_sites(trees[n])[1] for n in MODULES if n != "s2_stepper.py")
    ok = sorted(in_stepper) == ["class_step", "full_step"] and tot_stepper == 2 and elsewhere == 0
    # the table dictionary is referenced only where it is built, read out and compared
    users = set()
    for fn in trees["stage2_mixedpath.py"].body:
        if isinstance(fn, ast.FunctionDef):
            for node in ast.walk(fn):
                if isinstance(node, ast.Name) and node.id == "F_TABLES":
                    users.add(fn.name)
    ok2 = users <= {"build_tables", "table_for", "inv_rules"}
    ctx.invariant("stepper-static", ok and ok2, {"lookup_functions": sorted(in_stepper),
                                                 "lookups_outside_stepper": elsewhere,
                                                 "table_dictionary_users": sorted(users)})


def inv_rules(ctx):
    build_tables()
    measured = {}
    # generator: vectorised stream equals the literal loop
    ok_gen = [int(v) for v in lcg_stream(871, 1000)] == lcg_loop(871, 1000)
    ctx.invariant("generator", ok_gen, {"outputs_compared": 1000})
    # (i) neighbour sums
    lattices = (6, 8, 10, 12)
    total = sum(16 * 4 * L for L in lattices)
    stream = ((lcg_stream(871, total) >> np.uint64(16)) % np.uint64(5)).astype(np.int64)
    arrays = {}
    off = 0
    n_i = 0
    ok_i = True
    for L in lattices:
        G = geo(L)
        arr = stream[off:off + 16 * 4 * L].reshape(16, L, 2, 2)
        off += 16 * 4 * L
        arrays[L] = arr
        for a in arr:
            lit = literal_roll_sum(a)
            ok_i &= bool(np.array_equal(stp.full_sigma(a), lit))
            for tgt in (0, 1):
                cur = a[G.par == 1 - tgt].astype(np.uint8)
                got = stp.class_sigma(cur, G.nbr[tgt])
                ok_i &= bool(np.array_equal(got.astype(np.int64), lit[G.par == tgt]))
            n_i += 1
    ctx.invariant("rule-(i)-neighbour-sums", ok_i, {"arrays": n_i})
    # (ii) tables
    wanted = [("dummy", 2)] if ctx.selftest else list(BRUTE_RULES) + [("dummy", 2)]
    all_keys = sorted(FROZEN_F)
    hashes = {}
    ok_ii = sorted(F_TABLES) == sorted(all_keys + [("dummy3", 3)]) and F_TABLES[("dummy3", 3)] == DUMMY3
    for key in all_keys:
        tab = F_TABLES[key]
        ok_ii &= tuple(tab) == FROZEN_F[key] and len(tab) == 6 * (key[1] - 1) + 1
        hashes["%s/q%d" % key] = sha256_bytes(",".join(str(v) for v in tab).encode())
        ok_ii &= hashes["%s/q%d" % key] == sha256_bytes(",".join(str(v) for v in FROZEN_F[key]).encode())
    for key in LA_RULES:
        ok_ii &= la.alpha_table(key[0], key[1]) == FROZEN_F[key]
    ctx.invariant("rule-(ii)-tables", ok_ii, {"tables": len(all_keys), "linear_algebra_tables": len(LA_RULES),
                                               "table_sha256": hashes})
    # (iii) source hashes of the steppers
    src = {"full_step": sha256_bytes(inspect.getsource(stp.full_step).encode()),
           "class_step": sha256_bytes(inspect.getsource(stp.class_step).encode()),
           "full_sigma": sha256_bytes(inspect.getsource(stp.full_sigma).encode()),
           "class_sigma": sha256_bytes(inspect.getsource(stp.class_sigma).encode())}
    ctx.invariant("rule-(iii)-stepper-source", True, {"source_sha256": src})
    # (iv) operator columns against the literal six-shift sum
    ok_iv = True
    cols = 0
    for dims in ((6, 2, 2), (24, 24, 24), (28, 28, 28)):
        A, sites, index = la.build_operator(dims)
        Ac = A.tocsc()
        n = len(sites)
        e = np.zeros(dims, dtype=np.int64)
        for j in range(n):
            s = sites[j]
            e[s] = 1
            lit = literal_roll_sum(e).reshape(-1)
            e[s] = 0
            lo, hi = Ac.indptr[j], Ac.indptr[j + 1]
            nzl = np.flatnonzero(lit)
            order = np.argsort(Ac.indices[lo:hi])
            if not (np.array_equal(Ac.indices[lo:hi][order], nzl)
                    and np.array_equal(Ac.data[lo:hi][order], lit[nzl])):
                ok_iv = False
            cols += 1
    ctx.invariant("rule-(iv)-operator-columns", ok_iv, {"columns": cols})
    # (v) one application of each stepper against the literal expression
    ok_v = True
    n_v = 0
    for key in wanted:
        q = key[1]
        T = table_for(key[0], q)
        Tarr = np.array(T, dtype=np.int64)
        for L in (6, 12):
            G = geo(L)
            arr = arrays[L] % q
            for i in range(8):
                cur = arr[2 * i]
                prv = arr[2 * i + 1]
                lit_new = (Tarr[literal_roll_sum(cur)] - prv) % q
                new, ret = stp.full_step(cur, prv, T, q)
                ok_v &= bool(np.array_equal(new, lit_new)) and bool(np.array_equal(ret, cur))
                for p in (0, 1):
                    ccur = cur[G.par == p].astype(np.uint8)
                    cprv = prv[G.par == 1 - p].astype(np.uint8)
                    cnew, cret = stp.class_step(ccur, cprv, T, q, G.nbr[1 - p])
                    ok_v &= bool(np.array_equal(cnew.astype(np.int64), lit_new[G.par == 1 - p]))
                    ok_v &= bool(np.array_equal(cret.astype(np.int64), cur[G.par == p]))
                n_v += 1
    ctx.invariant("rule-(v)-stepper-literal", ok_v, {"pairs": n_v, "tables": ["%s/q%d" % k for k in wanted]})
    ctx.invariant("prereg-sha256", sha256_file(PREREG) == PREREG_SHA256, {"sha256": sha256_file(PREREG)})


# ---- tables: signalling counts, locality with certificate, CHSH ------------------------------
def submenus(q):
    return [((a, a2), (b, b2)) for a in range(q) for a2 in range(a + 1, q)
            for b in range(q) for b2 in range(b + 1, q)]


def sig_counts(N4, q):
    """N4[a][b][x][y] integer counts.  Number of (own setting, remote pair) with unequal marginals."""
    sig_a = 0
    sig_b = 0
    for a in range(q):
        for b in range(q):
            for b2 in range(b + 1, q):
                if not np.array_equal(N4[a, b].sum(axis=1), N4[a, b2].sum(axis=1)):
                    sig_a += 1
    for b in range(q):
        for a in range(q):
            for a2 in range(a + 1, q):
                if not np.array_equal(N4[a, b].sum(axis=0), N4[a2, b].sum(axis=0)):
                    sig_b += 1
    return sig_a, sig_b


def locality(ctx, N4, H, sub):
    Nsub = [[[[int(v) for v in row] for row in N4[a, b].tolist()] for b in sub[1]] for a in sub[0]]
    key = sha256_bytes(canon([H, Nsub]))
    if key in ctx.loc_cache:
        return ctx.loc_cache[key]
    cert = sol.decide_locality(Nsub, H, ctx.budget)
    if cert is None:
        res = {"loc": None, "certificate_verified": False, "chsh_max": None, "certificate": None}
    else:
        if not ver.verify_certificate(Nsub, H, cert):
            ctx.invariant("certificate-verification", False, {"table": key})
        ctx.counters["certificates_verified"] += 1
        ch = sol.chsh_max(Nsub, H)
        res = {"loc": cert["type"], "certificate_verified": True,
               "chsh_max": None if ch is None else frac_str(ch), "certificate": key}
        ctx.certs[key] = {"table_sha256": key, "H": H, "table": Nsub, "certificate": cert}
    ctx.loc_cache[key] = res
    return res


def analyse_table(ctx, N4, H, q):
    sa, sb = sig_counts(N4, q)
    out = {"sig_A": sa, "sig_B": sb, "submenus": None}
    if sa == 0 and sb == 0:
        subs = []
        for sub in submenus(q):
            r = locality(ctx, N4, H, sub)
            subs.append({"a": list(sub[0]), "b": list(sub[1]), "loc": r["loc"],
                         "certificate_verified": r["certificate_verified"], "chsh_max": r["chsh_max"],
                         "certificate": r["certificate"]})
        out["submenus"] = subs
    return out


def decide(groups):
    """Rules 2-6 of section 6 over the contents of one (instance, family, window)."""
    if all(g["dep_A"] == 0 and g["dep_B"] == 0 for g in groups):
        return "NO-DEPENDENCE", {"signalling_contents": 0, "nonlocal_among_nonsignalling": 0,
                                 "undecided_among_nonsignalling": 0}
    n_sig = sum(g["mult"] for g in groups if g["sig_A"] > 0 or g["sig_B"] > 0)
    ns = [g for g in groups if g["sig_A"] == 0 and g["sig_B"] == 0]
    nonloc = sum(g["mult"] for g in ns if any(s["loc"] == "NONLOCAL" for s in g["submenus"]))
    undec = sum(g["mult"] * sum(1 for s in g["submenus"] if s["loc"] is None) for g in ns)
    flags = {"signalling_contents": n_sig, "nonlocal_among_nonsignalling": nonloc,
             "undecided_among_nonsignalling": undec}
    if n_sig > 0:
        return "SIGNALLING", flags
    if nonloc > 0:
        chs = [s["chsh_max"] for g in ns for s in g["submenus"]]
        if all(c is not None for c in chs) and all(Fraction(c) <= 2 for c in chs):
            return "BELL-VIOLATION-NO-SIGNALLING-NON-CHSH", flags
        return "BELL-VIOLATION-NO-SIGNALLING", flags
    if undec == 0:
        return "DEPENDENCE-MASKED-LOCAL", flags
    return "LOCALITY-UNDECIDED", flags


# ---- planted tables (C7, C8, C9, C11, C14) ---------------------------------------------------
def planted_controls(ctx):
    # C7: PR table
    N = np.zeros((2, 2, 2, 2), dtype=np.int64)
    for a in (0, 1):
        for b in (0, 1):
            for r in (0, 1):
                N[a, b, r, r ^ (a & b)] += 1
    t7 = analyse_table(ctx, N, 2, 2)
    s7 = t7["submenus"][0] if t7["submenus"] else None
    ok7 = (t7["sig_A"] == 0 and t7["sig_B"] == 0 and s7 is not None and s7["loc"] == "NONLOCAL"
           and s7["certificate_verified"] and s7["chsh_max"] == "4/1")
    ctx.control("C7", ok7, True, {"tables": 1}, "planted PR table")
    # C8: planted local tables
    strategies = list(itertools.product((0, 1), repeat=4))
    seq = lcg_loop(869, 16 * 2000)
    pos = 0
    tables = []
    for i in range(1, 200):
        while True:
            w = [(seq[pos + j] >> 16) % 8 for j in range(16)]
            pos += 16
            if any(w):
                break
        tables.append(w)

    def chsh_s(st):
        A = [1 - 2 * st[0], 1 - 2 * st[1]]
        B = [1 - 2 * st[2], 1 - 2 * st[3]]
        return A[0] * B[0] + A[0] * B[1] + A[1] * B[0] - A[1] * B[1]
    w200 = [1 if chsh_s(st) == 2 else 0 for st in strategies]
    tables.append(w200)
    ok8 = sum(w200) == 8
    distinct = set()
    five = 0
    exact2 = 0
    cert_local = None
    for i, w in enumerate(tables):
        H = sum(w)
        N = np.zeros((2, 2, 2, 2), dtype=np.int64)
        for st, wj in zip(strategies, w):
            for a in (0, 1):
                for b in (0, 1):
                    N[a, b, st[a], st[2 + b]] += wj
        distinct.add(tuple(Fraction(int(v), H) for v in N.reshape(-1)))
        five += 1 if sum(1 for v in w if v) >= 5 else 0
        t = analyse_table(ctx, N, H, 2)
        s = t["submenus"][0] if t["submenus"] else None
        good = (s is not None and s["loc"] == "LOCAL" and s["certificate_verified"]
                and s["chsh_max"] is not None and Fraction(s["chsh_max"]) <= 2)
        ok8 &= bool(good)
        if good and Fraction(s["chsh_max"]) == 2:
            exact2 += 1
        if i == 199:
            ok8 &= bool(good and s["chsh_max"] == "2/1")
            cert_local = (ctx.certs[s["certificate"]] if good else None)
    nonvac8 = exact2 >= 1 and len(distinct) >= 150 and five >= 100
    ctx.control("C8", ok8, nonvac8, {"tables": len(tables), "distinct_tables": len(distinct),
                                    "five_or_more_weights": five, "chsh_exactly_2": exact2},
                "planted local tables")
    # C9: non-coset Z4 table of Stage 1 (probe X1)
    sigma = {0: 1, 1: 0, 2: 2, 3: 3}
    N9 = np.zeros((2, 2, 4, 4), dtype=np.int64)
    for a in (0, 1):
        for b in (0, 1):
            for p in range(4):
                N9[a, b, (p + b) % 4, (sigma[p] + a) % 4] += 1
    t9 = analyse_table(ctx, N9, 4, 2)
    s9 = t9["submenus"][0] if t9["submenus"] else None
    ok9 = (t9["sig_A"] == 0 and t9["sig_B"] == 0 and s9 is not None and s9["loc"] == "NONLOCAL"
           and s9["certificate_verified"] and s9["chsh_max"] == "3/1")
    ctx.control("C9", ok9, True, {"tables": 1}, "planted non-coset Z4 table")
    # C11: the verifier rejects perturbed certificates
    rej_local = False
    rej_nonlocal = False
    if cert_local is not None and cert_local["certificate"]["weights"]:
        c = json.loads(json.dumps(cert_local["certificate"]))
        c["weights"][0][4] = frac_str(Fraction(c["weights"][0][4]) + Fraction(1, 7))
        rej_local = (ver.verify_certificate(cert_local["table"], cert_local["H"], cert_local["certificate"])
                     and not ver.verify_certificate(cert_local["table"], cert_local["H"], c))
    if s7 is not None and s7["certificate"] is not None:
        rec = ctx.certs[s7["certificate"]]
        c = json.loads(json.dumps(rec["certificate"]))
        mabs = max(abs(Fraction(v)) for a in (0, 1) for b in (0, 1) for row in c["beta"][a][b] for v in row)
        done = False
        for a in (0, 1):
            for b in (0, 1):
                for x in range(2):
                    for y in range(2):
                        if not done and rec["table"][a][b][x][y] == 0:
                            c["beta"][a][b][x][y] = frac_str(Fraction(c["beta"][a][b][x][y]) + 100 * (mabs + 1))
                            done = True
        rej_nonlocal = (done and ver.verify_certificate(rec["table"], rec["H"], rec["certificate"])
                        and not ver.verify_certificate(rec["table"], rec["H"], c))
    ctx.control("C11", rej_local and rej_nonlocal, True,
                {"local_rejected": int(rej_local), "nonlocal_rejected": int(rej_nonlocal)},
                "perturbed certificates")
    # C14: planted signalling table h_B = a, h_A = r
    N14 = np.zeros((2, 2, 2, 2), dtype=np.int64)
    for a in (0, 1):
        for b in (0, 1):
            for r in (0, 1):
                N14[a, b, r, a] += 1
    t14 = analyse_table(ctx, N14, 2, 2)
    ctx.control("C14", t14["sig_B"] > 0, True, {"sig_B": t14["sig_B"]}, "planted signalling table")


def control_c12(ctx):
    regen = {}
    for L in (6, 8, 10, 12):
        regen[L] = [(D, k) for D in range(2, L + 1, 2) for k in range(D, 4 * L)
                    if k * k < 3 * D * D and L >= D + k + 1]
    ok = regen == FROZEN_WINDOWS
    wings = {D: (["S"] + (["I", "O"] if D >= 4 else [])) for D in (2, 4)}
    ok &= wings == FROZEN_WINGS
    patch = []
    for n in itertools.product(range(5), repeat=3):
        l1 = sum(n)
        if n[0] >= n[1] >= n[2] and l1 % 2 == 0 and 0 < l1 <= 4:
            ks = [k for k in range(l1, 40) if k * k < 3 * sum(c * c for c in n)]
            if ks:
                patch.append((n, ks))
    ok &= sorted(patch) == sorted(FROZEN_PATCH)
    diag = all(not [k for k in range(3 * D, 60) if k * k < 3 * 3 * D * D] for D in range(1, 7))
    ctx.control("C12", ok and diag, True, {"torus_rows": sum(len(v) for v in regen.values()),
                                            "patch_rows": len(patch), "diagonals_checked": 6},
                "window arithmetic")


# ---- controls on T(6): C2, C2b, C3 -----------------------------------------------------------
def controls_t6(ctx, rules):
    c2, c2_nonvac, c2b, c3, c3_ok, c3_nonvac = t6_checks(ctx, rules)
    ctx.control("C2", c2["violations"] == 0, c2_nonvac and c2["comparisons"] > 0, c2, "parity decoupling")
    ctx.control("C2b", c2b["violations"] == 0, c2b["comparisons"] > 0, c2b,
                "class-restricted stepper equals full-field stepper")
    ctx.control("C3", c3_ok, c3_nonvac, c3, "bijection and measure")


def t6_checks(ctx, rules):
    L = 6
    G = geo(L)
    c2 = {"comparisons": 0, "violations": 0, "per_rule": {}}
    c2b = {"comparisons": 0, "violations": 0, "per_rule": {}}
    c3 = {"round_trips": 0, "violations": 0, "per_rule": {}}
    c2_nonvac = True
    c3_ok = True
    c3_nonvac = True
    for rule, q in rules:
        T = table_for(rule, q)
        tag = "%s/q%d" % (rule, q)
        # base states B
        const = [(i, j) for i in range(q) for j in range(q)]
        seeded = ((lcg_stream(868, 256 * 48) >> np.uint64(16)) % np.uint64(q)).astype(np.int64)
        seeded = seeded.reshape(256, 2, L, 2, 2)
        U = np.concatenate([np.array([np.full((L, 2, 2), i) for i, _ in const], dtype=np.int64), seeded[:, 0]])
        V = np.concatenate([np.array([np.full((L, 2, 2), j) for _, j in const], dtype=np.int64), seeded[:, 1]])
        nb = len(U)
        # C2: single-coordinate changes of one class leave the other class unchanged through tick 6
        per_class = []
        viol_rule = 0
        for cls in (0, 1):
            cu = np.argwhere(G.par == cls)
            cv = np.argwhere(G.par == 1 - cls)
            coords = [("u", tuple(int(v) for v in c)) for c in cu] + [("v", tuple(int(v) for v in c)) for c in cv]
            PU = []
            PV = []
            for (sl, s) in coords:
                for delta in range(1, q):
                    u2 = U.copy()
                    v2 = V.copy()
                    if sl == "u":
                        u2[:, s[0], s[1], s[2]] = (u2[:, s[0], s[1], s[2]] + delta) % q
                    else:
                        v2[:, s[0], s[1], s[2]] = (v2[:, s[0], s[1], s[2]] + delta) % q
                    PU.append(u2)
                    PV.append(v2)
            PU = np.concatenate(PU)
            PV = np.concatenate(PV)
            reps = len(coords) * (q - 1)
            BU = np.concatenate([U] * reps)
            BV = np.concatenate([V] * reps)
            bad = np.zeros(len(PU), dtype=bool)
            for t in range(1, 7):
                PU, PV = stp.full_step(PU, PV, T, q)
                BU, BV = stp.full_step(BU, BV, T, q)
                mask = G.par == (t + 1 - cls) % 2
                bad |= np.any(PU[:, mask] != BU[:, mask], axis=1)
            per_class.append(len(bad))
            viol_rule += int(bad.sum())
            c2_nonvac &= len(bad) >= 260 * 24 * (q - 1)
        c2["comparisons"] += sum(per_class)
        c2["violations"] += viol_rule
        c2["per_rule"][tag] = {"comparisons_per_class": per_class, "violations": viol_rule, "base_states": nb}
        # C2b on B: class-restricted stepper against the full-field stepper, six ticks, both classes
        n2b = 0
        v2b = 0
        for p in (0, 1):
            cur = np.ascontiguousarray(U[:, G.par == p].T).astype(np.uint8)
            prv = np.ascontiguousarray(V[:, G.par == 1 - p].T).astype(np.uint8)
            FU, FV = U, V
            for t in range(1, 7):
                tgt = (t + p) % 2
                cur, prv = stp.class_step(cur, prv, T, q, G.nbr[tgt])
                FU, FV = stp.full_step(FU, FV, T, q)
                n2b += nb
                v2b += int(np.any(cur.astype(np.int64) != FU[:, G.par == tgt].T, axis=0).sum())
        # C3 (and C2b on the states of C3), both step types
        rule3 = {}
        for tau in (0, 1):
            nbt = G.nbr[1 - tau]
            if q == 2:
                total = 1 << 24
                seen = np.zeros(total, dtype=bool)
                sample = None
            else:
                total = 1 << 20
                sample = lcg_stream(870, 24 * total)
                sample >>= np.uint64(16)
                sample %= np.uint64(3)
                sample = sample.astype(np.uint8).reshape(total, 24)
                enc_states = []
                enc_images = []
            rt = 0
            rv = 0
            blk = 1 << 17
            pw = [q ** i for i in range(24)]
            for n0 in range(0, total, blk):
                ctx.check_bounds()
                B = min(blk, total - n0)
                if q == 2:
                    idx = np.arange(n0, n0 + B, dtype=np.int64)
                    cur = np.stack([((idx >> i) & 1).astype(np.uint8) for i in range(12)])
                    prv = np.stack([((idx >> (12 + i)) & 1).astype(np.uint8) for i in range(12)])
                else:
                    cur = np.ascontiguousarray(sample[n0:n0 + B, :12].T)
                    prv = np.ascontiguousarray(sample[n0:n0 + B, 12:].T)
                new, keep = stp.class_step(cur, prv, T, q, nbt)
                back, keep2 = stp.class_step(keep, new, T, q, nbt)
                rt += B
                rv += int((np.any(back != prv, axis=0) | np.any(keep2 != cur, axis=0)).sum())
                code = np.zeros(B, dtype=np.int64)
                for i in range(12):
                    code += new[i].astype(np.int64) * pw[i] + keep[i].astype(np.int64) * pw[12 + i]
                if q == 2:
                    seen[code] = True
                else:
                    scode = np.zeros(B, dtype=np.int64)
                    for i in range(12):
                        scode += cur[i].astype(np.int64) * pw[i] + prv[i].astype(np.int64) * pw[12 + i]
                    enc_states.append(scode)
                    enc_images.append(code)
                # C2b: the same step on the full two-slice field, other class zero
                FU = np.zeros((B, L, 2, 2), dtype=np.int64)
                FV = np.zeros((B, L, 2, 2), dtype=np.int64)
                FU[:, G.par == tau] = cur.T
                FV[:, G.par == 1 - tau] = prv.T
                NU, NV = stp.full_step(FU, FV, T, q)
                n2b += B
                v2b += int(np.any(NU[:, G.par == 1 - tau] != new.T, axis=1).sum())
            if q == 2:
                distinct_states = total
                distinct_images = int(np.count_nonzero(seen))
                del seen
                nonvac = rt == total
            else:
                distinct_states = int(len(np.unique(np.concatenate(enc_states))))
                distinct_images = int(len(np.unique(np.concatenate(enc_images))))
                nonvac = distinct_states >= (1 << 19)
                del sample
            ok = rv == 0 and distinct_images == distinct_states
            c3_ok &= ok
            c3_nonvac &= nonvac
            c3["round_trips"] += rt
            c3["violations"] += rv + (0 if distinct_images == distinct_states else 1)
            rule3["step_type_%d" % tau] = {"round_trips": rt, "round_trip_violations": rv,
                                           "distinct_states": distinct_states,
                                           "distinct_images": distinct_images,
                                           "exhaustive": q == 2}
        c3["per_rule"][tag] = rule3
        c2b["comparisons"] += n2b
        c2b["violations"] += v2b
        c2b["per_rule"][tag] = {"comparisons": n2b, "violations": v2b}
    return c2, c2_nonvac, c2b, c3, c3_ok, c3_nonvac


# ---- instances -------------------------------------------------------------------------------
def make_inst(rule, q, L, part, wing, D, sl, family):
    ks = [k for (d, k) in FROZEN_WINDOWS[L] if d == D]
    return {"id": "%s/q%d/T%d/%s/%s/D%d/%s/%s" % (rule, q, L, part, wing, D, sl, family),
            "rule": rule, "q": q, "L": L, "partition": part, "wing": wing, "D": D, "slice": sl,
            "family": family, "ks": ks, "primary": rule == "R-round"}


def instance_list(selftest):
    out = []
    if selftest:
        for part in ("cb3", "cb4"):
            for sl in ("u", "v"):
                out.append(make_inst("dummy", 2, 6, part, "S", 2, sl, "F_const"))
        return out
    for L in (6, 8, 10, 12):
        Ds = sorted(set(d for d, _ in FROZEN_WINDOWS[L]))
        parts = ["cb3", "cb4", "hor"] + (["reg"] if L == 6 else [])
        fams = ["F_const"] + (["F_all"] if L == 6 else [])
        for part in parts:
            for D in Ds:
                for wing in FROZEN_WINGS[D]:
                    for sl in ("u", "v"):
                        for fam in fams:
                            out.append(make_inst("R-round", 2, L, part, wing, D, sl, fam))
        if L == 6:
            for sl in ("u", "v"):
                out.append(make_inst("R-round", 3, 6, "cb3", "S", 2, sl, "F_const"))
            for part in ("cb3", "cb4"):
                for sl in ("u", "v"):
                    out.append(make_inst("R-lin", 3, 6, part, "S", 2, sl, "F_const"))
    return out


def setup(inst, shift=0):
    L, D = inst["L"], inst["D"]
    G = geo(L)
    p = 0 if inst["slice"] == "u" else 1
    base = {"S": (0, 0, D, D), "I": (0, 2, D, D + 2), "O": (2, 0, D + 2, D)}[inst["wing"]]
    gA, rA, rB, gB = [((x + shift) % L, 0, 0) for x in base]

    def sh(s):
        return ((s[0] + shift) % L, s[1], s[2])
    coords = [("u", sh(s)) for s in G.subs[p]] + [("v", sh(s)) for s in G.subs[1 - p]]

    def where(c):
        return (0, G.pos[p][c[1]]) if c[0] == "u" else (1, G.pos[1 - p][c[1]])
    genA = (inst["slice"], gA)
    genB = (inst["slice"], gB)
    wing_sites = {gA, gB, rA, rB}
    hidden = []
    visible = []
    for c in coords:
        if c == genA or c == genB:
            continue
        s = c[1]
        if inst["partition"] == "cb3":
            h = (s[0] + s[1] + s[2]) % 2 == 1
        elif inst["partition"] == "reg":
            h = s not in wing_sites
        elif inst["partition"] in ("cb4", "hor"):
            h = False
        else:
            raise ValueError(inst["partition"])
        (hidden if h else visible).append(c)
    kmax = max(inst["ks"])
    sigs = {k: tuple(t for t in range(1, k + 1) if (t + p) % 2 == 0) for k in inst["ks"]}
    masks = {}
    for t in range(1, kmax + 1):
        tgt = (t + p) % 2
        masks[t] = (np.array([r for r, s in enumerate(G.subs[tgt]) if thin_dist(gA, s, L) > t], dtype=np.intp),
                    np.array([r for r, s in enumerate(G.subs[tgt]) if thin_dist(gB, s, L) > t], dtype=np.intp))
    return {"G": G, "p": p, "gA": gA, "rA": rA, "rB": rB, "gB": gB, "coords": coords, "where": where,
            "genA": where(genA), "genB": where(genB), "hidden": hidden, "visible": visible,
            "kmax": kmax, "sigs": sigs, "masks": masks, "recA": G.pos[0][rA], "recB": G.pos[0][rB],
            "L": L, "shift": shift}


def hidden_coords_second(inst):
    """Second, independent generator of the hidden coordinates of the setting's class."""
    L, D = inst["L"], inst["D"]
    xs = {"S": [0, D], "I": [0, 2, D, D + 2], "O": [0, 2, D, D + 2]}[inst["wing"]]
    out = set()
    for sl in "uv":
        for x in range(L):
            for y in (0, 1):
                for z in (0, 1):
                    eps = (x + y + z) & 1
                    in_class = (eps == 0) == ((sl == "u") == (inst["slice"] == "u"))
                    if not in_class:
                        continue
                    if inst["partition"] == "cb3":
                        hid = eps == 1
                    elif inst["partition"] == "reg":
                        hid = not (y == 0 and z == 0 and x in xs)
                    else:
                        hid = False
                    if hid:
                        out.add("%s@(%d,%d,%d)" % (sl, x, y, z))
    return out


class PriorEnumeration:
    """The one enumeration object of hidden configurations of an instance and pass."""

    def __init__(self, coords, q):
        self.names = [cname(c) for c in coords]
        self.q = q
        self.count = q ** len(coords)

    def digest(self):
        return sha256_bytes(canon([self.q, self.count, self.names]))


def simulate(ctx, st, q, table, enum_coords, fixed, n_total, on_block, c1, prior, prior_digest):
    G = st["G"]
    p = st["p"]
    nset = q * q
    nsub = len(G.subs[0])
    enum_pos = [st["where"](c) for c in enum_coords]
    fixed_pos = [(st["where"](c), v) for c, v in fixed.items()]
    wA, rowA = st["genA"]
    wB, rowB = st["genB"]
    pairs_a = [(a * q + b, a2 * q + b) for b in range(q) for a in range(q) for a2 in range(a + 1, q)]
    pairs_b = [(a * q + b, a * q + b2) for a in range(q) for b in range(q) for b2 in range(b + 1, q)]
    a1 = [x for x, _ in pairs_a]
    a2 = [y for _, y in pairs_a]
    b1 = [x for x, _ in pairs_b]
    b2 = [y for _, y in pairs_b]
    for s in range(nset):
        ctx.counters["prior_digest_checks"] += 1
        if prior.digest() != prior_digest:
            ctx.invariant("same-hidden-prior", False, {"setting": s})
    for n0 in range(0, n_total, BLOCK):
        ctx.check_bounds()
        B = min(BLOCK, n_total - n0)
        idx = np.arange(n0, n0 + B, dtype=np.int64)
        arrs = [np.zeros((nsub, nset, B), dtype=np.uint8), np.zeros((nsub, nset, B), dtype=np.uint8)]
        for (w, row), val in fixed_pos:
            arrs[w][row] = val
        for i, (w, row) in enumerate(enum_pos):
            arrs[w][row] = ((idx // (q ** i)) % q).astype(np.uint8)[None, :]
        for s in range(nset):
            a, b = divmod(s, q)
            arrs[wA][rowA, s, :] = a
            arrs[wB][rowB, s, :] = b
        cur, prv = arrs
        recs = {}
        for t in range(1, st["kmax"] + 1):
            tgt = (t + p) % 2
            cur, prv = stp.class_step(cur, prv, table, q, G.nbr[tgt])
            if c1 is not None:
                mA, mB = st["masks"][t]
                if len(mA):
                    sel = cur[mA]
                    c1["violations"] += int(np.count_nonzero(sel[:, a1, :] != sel[:, a2, :]))
                    c1["comparisons"] += len(mA) * len(a1) * B
                if len(mB):
                    sel = cur[mB]
                    c1["violations"] += int(np.count_nonzero(sel[:, b1, :] != sel[:, b2, :]))
                    c1["comparisons"] += len(mB) * len(b1) * B
            if tgt == 0:
                recs[t] = (cur[st["recA"]], cur[st["recB"]])
        on_block(n0, B, recs)


def run_instance(ctx, inst, shift=0, do_c1=True):
    q = inst["q"]
    st = setup(inst, shift)
    table = table_for(inst["rule"], q)
    nset = q * q
    prior = PriorEnumeration(st["hidden"], q)
    prior_digest = prior.digest()
    sig_set = []
    for k in inst["ks"]:
        if st["sigs"][k] not in sig_set:
            sig_set.append(st["sigs"][k])
    for k in inst["ks"]:
        D = inst["D"]
        ctx.counters["window_asserts"] += 1
        if not (D <= k and k * k < 3 * D * D and inst["L"] - D > k):
            ctx.invariant("window", False, {"instance": inst["id"], "k": k})
        for t in st["sigs"][k]:
            ctx.counters["record_tick_asserts"] += 1
            if not 1 <= t <= k:
                ctx.invariant("record-tick-in-window", False, {"instance": inst["id"], "k": k})
    c1 = None
    if do_c1:
        c1 = {"comparisons": 0, "violations": 0,
              "pairs_A": int(sum(len(st["masks"][t][0]) for t in st["masks"])),
              "pairs_B": int(sum(len(st["masks"][t][1]) for t in st["masks"]))}
    pairs_a = [(a * q + b, a2 * q + b) for b in range(q) for a in range(q) for a2 in range(a + 1, q)]
    pairs_b = [(a * q + b, a * q + b2) for a in range(q) for b in range(q) for b2 in range(b + 1, q)]
    res = {"st": st, "sig_set": sig_set, "c1": c1, "hidden_names": prior.names,
           "hidden_count": prior.count, "prior_digest": prior_digest}
    point = inst["family"] == "F_all" and not st["hidden"]
    if point:
        nc = q ** len(st["visible"])
        codes = {sg: np.zeros((nc, nset), dtype=np.uint16) for sg in sig_set}

        def on_block(n0, B, recs):
            for sg in sig_set:
                n = q ** len(sg)
                hA = np.zeros((nset, B), dtype=np.uint16)
                hB = np.zeros((nset, B), dtype=np.uint16)
                for i, t in enumerate(sg):
                    hA += recs[t][0].astype(np.uint16) * np.uint16(q ** i)
                    hB += recs[t][1].astype(np.uint16) * np.uint16(q ** i)
                codes[sg][n0:n0 + B] = (hA * np.uint16(n) + hB).T
        simulate(ctx, st, q, table, st["visible"], {}, nc, on_block, c1, prior, prior_digest)
        ctx.counters["every_run_checks"] += nc * nset
        res.update({"mode": "point", "codes": codes, "nc": nc})
        return res
    nvis = len(st["visible"])
    if inst["family"] == "F_const":
        if nvis == 0:
            contents = [("*", {})]
        else:
            contents = [(str(c), {v: c for v in st["visible"]}) for c in range(q)]
    else:
        contents = []
        for ci in range(q ** nvis):
            digs = [(ci // (q ** i)) % q for i in range(nvis)]
            contents.append(("".join(str(d) for d in digs), {v: d for v, d in zip(st["visible"], digs)}))
    out = []
    for label, fixed in contents:
        acc = {"label": label, "fixed": fixed,
               "N": {sg: np.zeros((nset, (q ** len(sg)) ** 2), dtype=np.int64) for sg in sig_set},
               "depA": {sg: 0 for sg in sig_set}, "depB": {sg: 0 for sg in sig_set},
               "tdA": {}, "tdB": {}}

        def on_block(n0, B, recs, acc=acc):
            for t in recs:
                rA, rB = recs[t]
                acc["tdB"][t] = acc["tdB"].get(t, False) or any(
                    bool(np.any(rB[x] != rB[y])) for x, y in pairs_a)
                acc["tdA"][t] = acc["tdA"].get(t, False) or any(
                    bool(np.any(rA[x] != rA[y])) for x, y in pairs_b)
            for sg in sig_set:
                n = q ** len(sg)
                hA = np.zeros((nset, B), dtype=np.uint8)
                hB = np.zeros((nset, B), dtype=np.uint8)
                for i, t in enumerate(sg):
                    hA += recs[t][0] * np.uint8(q ** i)
                    hB += recs[t][1] * np.uint8(q ** i)
                joint = hA * np.uint8(n) + hB
                for s in range(nset):
                    acc["N"][sg][s] += np.bincount(joint[s], minlength=n * n)
                acc["depB"][sg] += sum(int(np.count_nonzero(hB[x] != hB[y])) for x, y in pairs_a)
                acc["depA"][sg] += sum(int(np.count_nonzero(hA[x] != hA[y])) for x, y in pairs_b)
        simulate(ctx, st, q, table, st["hidden"], fixed, prior.count, on_block, c1, prior, prior_digest)
        for sg in sig_set:
            for s in range(nset):
                ctx.counters["every_run_checks"] += 1
                tot = int(acc["N"][sg][s].sum())
                if ctx.plant == "invariant":
                    tot += 1
                if tot != prior.count:
                    ctx.invariant("every-run", False, {"instance": inst["id"], "c": label})
        out.append(acc)
    res.update({"mode": "hidden", "contents": out})
    return res


def table_digests(inst, res):
    """Canonical serialisation and SHA-256 of every count table of an instance (section 5, replay)."""
    q = inst["q"]
    out = []
    done = set()
    for k in inst["ks"]:
        sg = res["st"]["sigs"][k]
        if sg in done:
            continue
        done.add(sg)
        n = q ** len(sg)
        if res["mode"] == "point":
            head = canon({"id": inst["id"], "k": k, "q": q, "n": n, "contents": res["nc"], "form": "codes-u2"})
            out.append(("%s/k%d/*" % (inst["id"], k),
                        sha256_bytes(head + res["codes"][sg].astype("<u2").tobytes())))
        else:
            for acc in res["contents"]:
                head = canon({"id": inst["id"], "k": k, "c": acc["label"], "q": q, "n": n, "form": "counts-i8"})
                out.append(("%s/k%d/%s" % (inst["id"], k, acc["label"]),
                            sha256_bytes(head + acc["N"][sg].astype("<i8").tobytes())))
    return out


def first_tick(flags, sg):
    for t in sg:
        if flags.get(t, False):
            return t
    return None


def sparse_table(N4, q):
    out = {}
    for a in range(q):
        for b in range(q):
            nz = np.argwhere(N4[a, b] > 0)
            out["%d,%d" % (a, b)] = [[int(x), int(y), int(N4[a, b, x, y])] for x, y in nz]
    return out


def summarise(ctx, inst, res):
    """Window entries (per content measurements, locality with certificates, token)."""
    q = inst["q"]
    st = res["st"]
    H = res["hidden_count"]
    digs = dict(table_digests(inst, res))
    windows = []
    tables_out = []
    first_k = {}
    for k in inst["ks"]:
        sg = st["sigs"][k]
        n = q ** len(sg)
        if sg in first_k:
            w = json.loads(json.dumps(windows[[x["k"] for x in windows].index(first_k[sg])]))
            w["k"] = k
            w["same_histories_as"] = first_k[sg]
            windows.append(w)
            continue
        first_k[sg] = k
        groups = []
        entry = {"k": k, "record_ticks": list(sg), "in_window": True, "same_histories_as": None}
        if res["mode"] == "hidden":
            per = []
            tab_contents = []
            for acc in res["contents"]:
                N4 = acc["N"][sg].reshape(q, q, n, n)
                t = analyse_table(ctx, N4, H, q)
                dA, dB = int(acc["depA"][sg]), int(acc["depB"][sg])
                ctx.counters["exclusivity_checks"] += 1
                if dA == 0 and dB == 0 and (t["sig_A"] or t["sig_B"]):
                    ctx.invariant("token-exclusivity", False, {"instance": inst["id"], "k": k})
                key = "%s/k%d/%s" % (inst["id"], k, acc["label"])
                pc = {"c": acc["label"], "dep_A": dA, "dep_B": dB,
                      "first_dep_tick": {"A": first_tick(acc["tdA"], sg), "B": first_tick(acc["tdB"], sg)},
                      "sig_A": t["sig_A"], "sig_B": t["sig_B"], "submenus": t["submenus"],
                      "table_digest": digs[key]}
                per.append(pc)
                groups.append({"mult": 1, "dep_A": dA, "dep_B": dB, "sig_A": t["sig_A"], "sig_B": t["sig_B"],
                               "submenus": t["submenus"]})
                tab_contents.append({"c": acc["label"], "N": sparse_table(N4, q), "table_digest": digs[key]})
            entry["per_content"] = per
            tables_out.append({"k": k, "record_ticks": list(sg), "contents": tab_contents})
        else:
            codes = res["codes"][sg]
            nset = q * q
            key64 = np.zeros(res["nc"], dtype=np.uint64)
            for s in range(nset):
                key64 |= codes[:, s].astype(np.uint64) << np.uint64(16 * s)
            uniq, first_idx, counts = np.unique(key64, return_index=True, return_counts=True)
            agg = []
            for u in range(len(uniq)):
                row = [int(v) for v in codes[int(first_idx[u])]]
                N4 = np.zeros((q, q, n, n), dtype=np.int64)
                hA = {}
                hB = {}
                for s in range(nset):
                    a, b = divmod(s, q)
                    x, y = divmod(row[s], n)
                    N4[a, b, x, y] = 1
                    hA[(a, b)] = x
                    hB[(a, b)] = y
                dB = sum(1 for b in range(q) for a in range(q) for a2 in range(a + 1, q)
                         if hB[(a, b)] != hB[(a2, b)])
                dA = sum(1 for a in range(q) for b in range(q) for b2 in range(b + 1, q)
                         if hA[(a, b)] != hA[(a, b2)])

                def ftick(h, pairs):
                    best = None
                    for (s1, s2) in pairs:
                        for i, tk in enumerate(sg):
                            if (h[s1] // (q ** i)) % q != (h[s2] // (q ** i)) % q:
                                best = tk if best is None else min(best, tk)
                                break
                    return best
                fB = ftick(hB, [((a, b), (a2, b)) for b in range(q) for a in range(q) for a2 in range(a + 1, q)])
                fA = ftick(hA, [((a, b), (a, b2)) for a in range(q) for b in range(q) for b2 in range(b + 1, q)])
                t = analyse_table(ctx, N4, 1, q)
                ctx.counters["exclusivity_checks"] += 1
                if dA == 0 and dB == 0 and (t["sig_A"] or t["sig_B"]):
                    ctx.invariant("token-exclusivity", False, {"instance": inst["id"], "k": k})
                ci = int(first_idx[u])
                label = "".join(str((ci // (q ** i)) % q) for i in range(len(st["visible"])))
                mult = int(counts[u])
                agg.append({"contents": mult, "example_c": label, "dep_A": dA, "dep_B": dB,
                            "first_dep_tick": {"A": fA, "B": fB}, "sig_A": t["sig_A"], "sig_B": t["sig_B"],
                            "submenus": t["submenus"], "N": sparse_table(N4, q)})
                groups.append({"mult": mult, "dep_A": dA, "dep_B": dB, "sig_A": t["sig_A"],
                               "sig_B": t["sig_B"], "submenus": t["submenus"]})
            key = "%s/k%d/*" % (inst["id"], k)
            entry["per_content"] = None
            entry["contents"] = res["nc"]
            entry["per_content_aggregate"] = [{kk: v for kk, v in g.items() if kk != "N"} for g in agg]
            entry["table_digest"] = digs[key]
            tables_out.append({"k": k, "record_ticks": list(sg), "contents": res["nc"],
                               "table_digest": digs[key],
                               "distinct_tables": [{"contents": g["contents"], "example_c": g["example_c"],
                                                    "N": g["N"]} for g in agg]})
        token, flags = decide(groups)
        entry.update(flags)
        entry["token"] = token
        entry["_groups"] = groups
        windows.append(entry)
    record = {"id": inst["id"], "rule": inst["rule"], "q": q, "lattice": "T%d" % inst["L"],
              "partition": inst["partition"], "wing": inst["wing"], "D": inst["D"], "slice": inst["slice"],
              "sites": {"gA": list(st["gA"]), "rA": list(st["rA"]), "gB": list(st["gB"]), "rB": list(st["rB"])},
              "hidden_coordinates": res["hidden_names"], "hidden_count": H, "family": inst["family"],
              "method": "enumeration", "primary": inst["primary"], "windows": windows}
    return record, {"id": inst["id"], "family": inst["family"], "windows": tables_out}, list(digs.items())


def control_c10_instance(ctx, inst, res, acc10):
    """Reflection (exchange of the wings) and translation by 2 along x, count tables compared exactly."""
    q = inst["q"]
    st = res["st"]
    L = inst["L"]
    nset = q * q
    res2 = run_instance(ctx, inst, shift=2, do_c1=False)

    def refl(c):
        return (c[0], ((st["gA"][0] + st["gB"][0] - c[1][0]) % L, c[1][1], c[1][2]))
    for sg in res["sig_set"]:
        n = q ** len(sg)
        if res["mode"] == "point":
            acc10["comparisons"] += 2 * res["nc"] * nset
            acc10["violations"] += int(np.count_nonzero(res["codes"][sg] != res2["codes"][sg]))
            vis = st["visible"]
            rho = [vis.index(refl(c)) for c in vis]
            idx = np.arange(res["nc"], dtype=np.int64)
            ridx = np.zeros(res["nc"], dtype=np.int64)
            for i in range(len(vis)):
                ridx += ((idx // (q ** rho[i])) % q) * (q ** i)
            codes = res["codes"][sg].astype(np.int64)
            for a in range(q):
                for b in range(q):
                    c1 = codes[:, a * q + b]
                    c2 = codes[ridx, b * q + a]
                    acc10["violations"] += int(np.count_nonzero((c1 // n != c2 % n) | (c1 % n != c2 // n)))
        else:
            index = {frozenset(acc["fixed"].items()): i for i, acc in enumerate(res["contents"])}
            for i, acc in enumerate(res["contents"]):
                acc10["comparisons"] += 2 * nset
                if not np.array_equal(acc["N"][sg], res2["contents"][i]["N"][sg]):
                    acc10["violations"] += 1
                j = index[frozenset((refl(c), v) for c, v in acc["fixed"].items())]
                other = res["contents"][j]["N"][sg]
                for a in range(q):
                    for b in range(q):
                        m1 = acc["N"][sg][a * q + b].reshape(n, n)
                        m2 = other[b * q + a].reshape(n, n).T
                        if not np.array_equal(m1, m2):
                            acc10["violations"] += 1
    acc10["instances"] += 1


# ---- affine rules by linear algebra ---------------------------------------------------------
def la_patch(ctx, lam, rules):
    dims = (lam, lam, lam)
    op = la.build_operator(dims)
    out = {}
    for (n, ks) in FROZEN_PATCH:
        for (rule, q, alpha) in rules:
            for part in ("cb3", "reg"):
                for sl in ("u", "v"):
                    ctx.check_bounds()
                    iid = "%s/q%d/P/%s/S/n%d%d%d/%s/F_const" % (rule, q, part, n[0], n[1], n[2], sl)
                    for k in ks:
                        l1 = sum(n)
                        if not (l1 <= k and k * k < 3 * sum(c * c for c in n) and 2 * (k + l1) < lam):
                            ctx.invariant("window", False, {"instance": iid, "k": k})
                        ctx.counters["window_asserts"] += 1
                    r = la.analyse(op, dims, q, alpha, (0, 0, 0), n, part, sl, ks)
                    r.update({"rule": rule, "q": q, "n": n, "partition": part, "slice": sl, "ks": ks})
                    out[iid] = r
    return out


def la_token(w):
    if not w["dep_A"] and not w["dep_B"]:
        return "NO-DEPENDENCE-BY-THEOREM-L"
    if w["sig_A"] or w["sig_B"]:
        return "SIGNALLING-BY-THEOREM-L"
    if w["thmL_A"] and w["thmL_B"]:
        return "DEPENDENCE-MASKED-LOCAL-BY-THEOREM-L"
    return "LOCALITY-UNDECIDED-BY-THEOREM-L"


def la_records(la24):
    recs = []
    for iid, r in la24.items():
        q = r["q"]
        windows = []
        first = {}
        for w in r["windows"]:
            tk = tuple(w["ticks"])
            ns = not (w["sig_A"] or w["sig_B"])
            loc = None
            if ns:
                loc = "LOCAL" if (w["thmL_A"] and w["thmL_B"]) else None
            per = [{"c": str(c), "dep_A": int(w["dep_A"]), "dep_B": int(w["dep_B"]),
                    "sig_A": int(w["sig_A"]), "sig_B": int(w["sig_B"]),
                    "submenus": ([{"all_submenus": True, "count": len(submenus(q)), "loc": loc,
                                   "certificate_verified": bool(loc), "chsh_max": None}] if ns else None)}
                   for c in range(q)]
            windows.append({"k": w["k"], "record_ticks": w["ticks"], "in_window": True,
                            "same_histories_as": first.get(tk), "per_content": per,
                            "indicator_counts": True,
                            "theorem_L_vectors_verified": {"A": w["thmL_A"], "B": w["thmL_B"]},
                            "nonlocal_among_nonsignalling": 0,
                            "undecided_among_nonsignalling": (len(submenus(q)) * q if ns and loc is None else 0),
                            "token": la_token(w)})
            first.setdefault(tk, w["k"])
        recs.append({"id": iid, "rule": r["rule"], "q": q, "lattice": "P24", "partition": r["partition"],
                     "wing": "S", "D": None, "n": list(r["n"]), "slice": r["slice"],
                     "sites": {"gA": [0, 0, 0], "rA": [0, 0, 0], "gB": list(r["n"]), "rB": list(r["n"])},
                     "hidden_coordinates": None, "hidden_count": None,
                     "hidden_dimension": r["hidden_dimension"], "family": "F_const",
                     "method": "linear-algebra", "primary": False, "windows": windows})
    return recs


def la_core(w):
    return [w["k"], w["ticks"], w["dep_A"], w["dep_B"], w["sig_A"], w["sig_B"], w["thmL_A"], w["thmL_B"],
            w["col_A"], w["col_B"], w["hidden_columns_A"], w["hidden_columns_B"]]


# ---- the two passes -------------------------------------------------------------------------
def process(ctx, insts, staging, tag):
    """First pass over a list of instances, by increasing L; results staged after each lattice."""
    out = {"insts": insts, "records": {}, "tables": {}, "digests1": [], "c1_all": {},
           "acc10": {"instances": 0, "comparisons": 0, "violations": 0}, "completed": [],
           "stopped": None, "part_ok": True}
    seen = set()
    for inst in insts:
        if inst["id"] in seen:
            ctx.invariant("instance-list", False, {"duplicate": inst["id"]})
        seen.add(inst["id"])
    records = out["records"]
    try:
        for L in sorted(set(i["L"] for i in insts)):
            for inst in [i for i in insts if i["L"] == L]:
                if inst["partition"] == "hor":
                    continue
                res = run_instance(ctx, inst)
                names = set(res["hidden_names"])
                ctx.counters["partition_compares"] += 1
                if names != hidden_coords_second(inst) or len(names) != len(res["hidden_names"]):
                    out["part_ok"] = False
                    ctx.invariant("partition-second-generator", False, {"instance": inst["id"]})
                rec, tab, digs = summarise(ctx, inst, res)
                if L in (6, 8):
                    control_c10_instance(ctx, inst, res, out["acc10"])
                records[inst["id"]] = rec
                out["tables"][inst["id"]] = tab
                out["digests1"] += digs
                out["c1_all"][inst["id"]] = res["c1"]
                out["completed"].append(inst)
                del res
                if ctx.plant == "error":
                    raise RuntimeError("planted uncaught error")
                print("[stage2] %s pass 1: instance %d of %d done (%d s)"
                      % (tag, len(out["completed"]), len(insts),
                         (time.monotonic_ns() - ctx.start_ns) // 10 ** 9), flush=True)
            # hor: the same computation as cb4, reported under both labels
            for inst in [i for i in insts if i["L"] == L and i["partition"] == "hor"]:
                src = inst["id"].replace("/hor/", "/cb4/")
                rec = json.loads(json.dumps(records[src]))
                rec["id"] = inst["id"]
                rec["partition"] = "hor"
                rec["computed_as"] = src
                records[inst["id"]] = rec
                out["completed"].append(inst)
            tmp = os.path.join(staging, "partial_%s_T%d.json.tmp" % (tag, L))
            with open(tmp, "w") as fh:
                json.dump([strip(records[i["id"]]) for i in insts if i["L"] == L and i["id"] in records], fh)
            os.replace(tmp, os.path.join(staging, "partial_%s_T%d.json" % (tag, L)))
    except BoundReached as exc:
        out["stopped"] = str(exc)
        ctx.bound = out["stopped"]
    out["done_ids"] = set(i["id"] for i in out["completed"])
    return out


def c1_scan(pr, la_items):
    counts = {"comparisons": 0, "violations": 0, "instances": 0, "per_instance": {}}
    nonvac = True
    for iid, c in pr["c1_all"].items():
        counts["comparisons"] += c["comparisons"]
        counts["violations"] += c["violations"]
        counts["instances"] += 1
        counts["per_instance"][iid] = c
        nonvac &= c["pairs_A"] > 0 and c["pairs_B"] > 0 and c["comparisons"] > 0
    for iid, r in la_items:
        pa, pb = r["c1"]["A"], r["c1"]["B"]
        counts["comparisons"] += pa["pairs"] + pb["pairs"]
        counts["violations"] += pa["violations"] + pb["violations"]
        counts["instances"] += 1
        counts["per_instance"][iid] = {"pairs_A": pa["pairs"], "pairs_B": pb["pairs"],
                                       "comparisons": pa["pairs"] + pb["pairs"],
                                       "violations": pa["violations"] + pb["violations"]}
        nonvac &= pa["pairs"] > 0 and pb["pairs"] > 0
    return counts, nonvac and counts["instances"] > 0


def c5_scan(pr, la24):
    c5 = {"windows": 0, "violations": 0, "missing_certificates": 0}
    dk = set()
    for iid in sorted(pr["done_ids"]):
        rec = pr["records"][iid]
        if rec["slice"] != "u" or rec["partition"] not in ("cb3", "reg"):
            continue
        for w in rec["windows"]:
            if w["k"] > rec["D"] + 1:
                continue
            c5["windows"] += 1
            dk.add((rec["D"], w["k"]))
            for g in w["_groups"]:
                if g["sig_A"] or g["sig_B"]:
                    c5["violations"] += g["mult"]
                else:
                    for sm in g["submenus"]:
                        if sm["loc"] is None:
                            c5["missing_certificates"] += g["mult"]
                        elif sm["loc"] != "LOCAL" or not sm["certificate_verified"]:
                            c5["violations"] += g["mult"]
    for iid, r in la24.items():
        if r["slice"] != "u" or r["partition"] not in ("cb3", "reg"):
            continue
        for w in r["windows"]:
            if w["k"] > sum(r["n"]) + 1:
                continue
            c5["windows"] += 1
            if w["sig_A"] or w["sig_B"] or not (w["thmL_A"] and w["thmL_B"]):
                c5["violations"] += 1
    return c5, dk


def c4_scan(pr, la6, rule_tag):
    c4 = {"comparisons": 0, "disagreements": 0, "missing_certificates": 0, "with_dep": 0, "with_sig0": 0}
    evaluated = True
    for (part, sl), r in la6.items():
        iid = "%s/T6/%s/S/D2/%s/F_const" % (rule_tag, part, sl)
        if iid not in pr["done_ids"]:
            evaluated = False
            continue
        for lw in r["windows"]:
            bw = [x for x in pr["records"][iid]["windows"] if x["k"] == lw["k"]][0]
            for pc in bw["per_content"]:
                c4["comparisons"] += 1
                bad = ((pc["dep_A"] > 0) != lw["dep_A"] or (pc["dep_B"] > 0) != lw["dep_B"]
                       or (pc["sig_A"] > 0) != lw["sig_A"] or (pc["sig_B"] > 0) != lw["sig_B"])
                if pc["dep_A"] > 0 or pc["dep_B"] > 0:
                    c4["with_dep"] += 1
                if pc["sig_A"] == 0 and pc["sig_B"] == 0 and not lw["sig_A"] and not lw["sig_B"]:
                    c4["with_sig0"] += 1
                    if not (lw["thmL_A"] and lw["thmL_B"]):
                        bad = True
                    for sm in pc["submenus"]:
                        if sm["loc"] is None:
                            c4["missing_certificates"] += 1
                        elif sm["loc"] != "LOCAL" or not sm["certificate_verified"]:
                            bad = True
                if bad:
                    c4["disagreements"] += 1
    return c4, evaluated


def second_pass(ctx, pr, tag):
    """Rebuilds the enumeration objects and recomputes every count table of the completed instances."""
    ctx.pass_start_ns = time.monotonic_ns()
    digests2 = []
    completed2 = set()
    try:
        for inst in pr["completed"]:
            if inst["partition"] == "hor":
                continue
            res = run_instance(ctx, inst, do_c1=False)
            digests2 += table_digests(inst, res)
            completed2.add(inst["id"])
            del res
            print("[stage2] %s pass 2: instance %d done (%d s)"
                  % (tag, len(completed2), (time.monotonic_ns() - ctx.start_ns) // 10 ** 9), flush=True)
    except BoundReached as exc:
        pr["stopped"] = pr["stopped"] or str(exc)
        ctx.bound = pr["stopped"]
    for inst in pr["completed"]:
        if inst["partition"] == "hor" and inst["id"].replace("/hor/", "/cb4/") in completed2:
            completed2.add(inst["id"])
    d1 = [(k, v) for k, v in pr["digests1"] if k.rsplit("/k", 1)[0] in completed2]
    if ctx.plant == "replay":
        digests2 = digests2 + [("planted", "0")]
    h1 = sha256_bytes("".join("%s:%s\n" % kv for kv in d1).encode())
    h2 = sha256_bytes("".join("%s:%s\n" % kv for kv in digests2).encode())
    return h1, h2, completed2, len(d1)


def write_outputs(staging, state, certs):
    os.makedirs(os.path.join(staging, "tables"))
    os.makedirs(os.path.join(staging, "certificates"))
    for iid, tab in state["tables"].items():
        if iid in state["done_ids"]:
            with open(os.path.join(staging, "tables", iid.replace("/", "__") + ".json"), "w") as fh:
                json.dump(tab, fh, sort_keys=True)
    with open(os.path.join(staging, "certificates", "certificates.json"), "w") as fh:
        json.dump(certs, fh, sort_keys=True)


def coverage(ctx, staging):
    """Extra self-test coverage (IMPLEMENTATION-NOTES.md): the code paths of the registered run that
    the dummy pipeline of section 5.1 does not reach, on rules outside the corpus only.  Nothing
    about these rules is reported beyond the counts of this invariant record."""
    insts = []
    for part in ("cb3", "cb4", "hor", "reg"):
        for sl in ("u", "v"):
            for fam in ("F_const", "F_all"):
                insts.append(make_inst("dummy", 2, 6, part, "S", 2, sl, fam))
    for part in ("cb3", "cb4"):
        for sl in ("u", "v"):
            insts.append(make_inst("dummy3", 3, 6, part, "S", 2, sl, "F_const"))
    insts.append(make_inst("dummy", 2, 8, "cb4", "S", 2, "v", "F_const"))
    insts.append(make_inst("dummy", 2, 8, "hor", "S", 2, "v", "F_const"))
    for wing in ("S", "I", "O"):
        for sl in ("u", "v"):
            insts.append(make_inst("dummy", 2, 10, "cb3", wing, 4, sl, "F_const"))
    for i in insts:
        i["primary"] = i["rule"] == "dummy"
    t6 = t6_checks(ctx, [("dummy3", 3)])
    t6_ok = (t6[0]["violations"] == 0 and t6[1] and t6[2]["violations"] == 0 and t6[4] and t6[5])
    pr = process(ctx, insts, staging, "coverage")
    rules = [DUMMY_AFFINE]
    la24 = la_patch(ctx, 24, rules)
    la28 = la_patch(ctx, 28, rules)
    same = (set(la24) == set(la28)
            and all(json.dumps([la_core(w) for w in la24[i]["windows"]], sort_keys=True)
                    == json.dumps([la_core(w) for w in la28[i]["windows"]], sort_keys=True) for i in la24))
    op6 = la.build_operator((6, 2, 2))
    la6 = {}
    for part in ("cb3", "cb4"):
        for sl in ("u", "v"):
            la6[(part, sl)] = la.analyse(op6, (6, 2, 2), 7, 3, (0, 0, 0), (2, 0, 0), part, sl, [2, 3])
    c1, c1_nonvac = c1_scan(pr, list(la24.items()) + [("LA6/%s/%s" % k, v) for k, v in la6.items()])
    c5, dk = c5_scan(pr, la24)
    c4_scan(pr, la6, "dummy3/q3")      # executed for coverage of the comparison code; outcome not used
    h1, h2, completed2, ntab = second_pass(ctx, pr, "coverage")
    state = {"insts": insts, "records": pr["records"], "tables": pr["tables"], "done_ids": completed2,
             "la24": la24, "stopped": pr["stopped"]}
    recs, verd = verdicts(ctx, state)
    sub = os.path.join(staging, "coverage_outputs")
    os.makedirs(sub)
    write_outputs(sub, state, ctx.certs)
    with open(os.path.join(sub, "results.json"), "w") as fh:
        json.dump({"instances": recs, "verdicts": verd}, fh, sort_keys=True)
    frac_bad = reject_fractional({"instances": recs, "verdicts": verd})
    shutil.rmtree(sub)
    tokens_ok = all(t.split("-BY-THEOREM-L")[0] in (
        "NO-DEPENDENCE", "SIGNALLING", "BELL-VIOLATION-NO-SIGNALLING", "BELL-VIOLATION-NO-SIGNALLING-NON-CHSH",
        "DEPENDENCE-MASKED-LOCAL", "LOCALITY-UNDECIDED") for t in verd["tokens"].values())
    ok = (t6_ok and pr["stopped"] is None and pr["part_ok"] and len(pr["done_ids"]) == len(insts)
          and c1["violations"] == 0 and c1_nonvac and pr["acc10"]["violations"] == 0
          and c5["violations"] == 0 and c5["missing_certificates"] == 0 and same
          and h1 == h2 and not frac_bad and tokens_ok and not ctx.budget.exhausted)
    ctx.invariant("selftest-extra-coverage", ok,
                  {"t6_checks_q3": int(t6_ok), "instances": len(insts), "linear_algebra_instances": len(la24) + len(la6),
                   "c1_comparisons": c1["comparisons"], "c1_violations": c1["violations"],
                   "c10_comparisons": pr["acc10"]["comparisons"], "c10_violations": pr["acc10"]["violations"],
                   "c5_windows": c5["windows"], "c5_violations": c5["violations"],
                   "patch_24_equals_28": int(same), "replay_equal": int(h1 == h2), "tables": ntab,
                   "tokens_well_formed": int(tokens_ok)})


def core(ctx, staging):
    selftest = ctx.selftest
    inv_static(ctx)
    inv_rules(ctx)
    print("[stage2] invariants (static, rule) evaluated", flush=True)
    planted_controls(ctx)
    control_c12(ctx)
    rules6 = [("dummy", 2)] if selftest else list(BRUTE_RULES)
    controls_t6(ctx, rules6)
    print("[stage2] controls on T(6) evaluated (%d s)" % ((time.monotonic_ns() - ctx.start_ns) // 10 ** 9),
          flush=True)
    la24 = {}
    la6 = {}
    if not selftest:
        rules = [(r, q, la.ALPHA[(r, q)]) for (r, q) in LA_RULES]
        la24 = la_patch(ctx, 24, rules)
        la28 = la_patch(ctx, 28, rules)
        same = all(json.dumps([la_core(w) for w in la24[i]["windows"]], sort_keys=True)
                   == json.dumps([la_core(w) for w in la28[i]["windows"]], sort_keys=True) for i in la24)
        ctx.control("C13", same and set(la24) == set(la28), len(la24) > 0, {"instances": len(la24)},
                    "no-wrap on the patch")
        del la28
        op6 = la.build_operator((6, 2, 2))
        for part in ("cb3", "cb4"):
            for sl in ("u", "v"):
                la6[(part, sl)] = la.analyse(op6, (6, 2, 2), 3, 1, (0, 0, 0), (2, 0, 0), part, sl, [2, 3])
        print("[stage2] linear-algebra path evaluated", flush=True)
    insts = instance_list(selftest)
    pr = process(ctx, insts, staging, "main")
    records = pr["records"]
    done_ids = pr["done_ids"]
    completed = pr["completed"]
    stopped = pr["stopped"]
    # ---- controls evaluated over instances ----
    c1_counts, c1_nonvac = c1_scan(pr, list(la24.items())
                                   + [("R-lin/q3/T6-LA/%s/%s" % k, v) for k, v in la6.items()])
    if ctx.plant == "red_control":
        c1_counts["violations"] += 1
    ctx.control("C1", c1_counts["violations"] == 0, c1_nonvac, c1_counts,
                "cone lemma on the full class field")
    c5, c5_dk = c5_scan(pr, la24)
    need = {(2, 2), (2, 3)} if selftest else {(2, 2), (2, 3), (4, 4), (4, 5)}
    ctx.control("C5", c5["violations"] == 0 and c5["missing_certificates"] == 0, need <= c5_dk, c5,
                "slice shift")
    acc10 = pr["acc10"]
    ctx.control("C10", acc10["violations"] == 0,
                acc10["instances"] == sum(1 for i in completed if i["L"] in (6, 8) and i["partition"] != "hor")
                and acc10["instances"] > 0, acc10, "symmetry")
    if not selftest:
        # C1'
        iid = "R-lin/q3/T6/cb3/S/D2/u/F_const"
        if iid in done_ids:
            w = [x for x in records[iid]["windows"] if x["k"] == 2][0]
            cnt = sum(pc["dep_B"] for pc in w["per_content"])
            want = (3 ** 12) * 3 * 3 * 3
            every = all(pc["dep_B"] == (3 ** 12) * 3 * 3 for pc in w["per_content"])
            ctx.control("C1'", cnt == want and every and w["record_ticks"] == [2], True,
                        {"count": cnt, "required": want}, "detector sensitivity")
        # C6
        iid = "R-lin/q3/T6/cb4/S/D2/u/F_const"
        if iid in done_ids:
            w = [x for x in records[iid]["windows"] if x["k"] == 2][0]
            ctx.control("C6", all(pc["sig_B"] > 0 for pc in w["per_content"]), True,
                        {"contents": len(w["per_content"]),
                         "contents_with_sig_B": sum(1 for pc in w["per_content"] if pc["sig_B"] > 0)},
                        "native signalling is detected")
        # C4
        c4, c4_eval = c4_scan(pr, la6, "R-lin/q3")
        if c4_eval:
            ctx.control("C4", c4["disagreements"] == 0 and c4["missing_certificates"] == 0,
                        c4["with_dep"] > 0 and c4["with_sig0"] > 0 and c4["comparisons"] > 0, c4,
                        "two code paths on the affine rule")
    expected = (["C1", "C2", "C2b", "C3", "C5", "C7", "C8", "C9", "C10", "C11", "C12", "C14"]
                + ([] if selftest else ["C1'", "C4", "C6", "C13"]))
    for cid in expected:
        if cid not in ctx.controls:
            ctx.control(cid, False, False, {}, "not evaluated")
    all_green = all(c["green"] for c in ctx.controls.values())
    # ---- remaining invariant records ----
    ctx.invariant("every-run", True, {"checks": ctx.counters["every_run_checks"]})
    ctx.invariant("same-hidden-prior", True, {"digest_checks": ctx.counters["prior_digest_checks"]})
    ctx.invariant("partition-second-generator", pr["part_ok"], {"instances": ctx.counters["partition_compares"]})
    ctx.invariant("window", True, {"window_asserts": ctx.counters["window_asserts"],
                                   "record_tick_asserts": ctx.counters["record_tick_asserts"]})
    ctx.invariant("certificate-verification", True, {"verified": ctx.counters["certificates_verified"]})
    ctx.invariant("token-exclusivity", True, {"checks": ctx.counters["exclusivity_checks"]})
    want_ids = [i["id"] for i in insts]
    ctx.invariant("instance-list", stopped is not None or sorted(records) == sorted(want_ids),
                  {"instances": len(want_ids), "reported": len(records)})
    # ---- second pass ----
    replay = {"performed": False, "tables_digest_equal": None}
    tables_digest = None
    if all_green:
        h1, h2, completed2, ntab = second_pass(ctx, pr, "main")
        stopped = pr["stopped"]
        replay = {"performed": True, "tables_digest_equal": h1 == h2}
        ctx.invariant("deterministic-replay", h1 == h2, {"tables": ntab})
        tables_digest = h1
        done_ids = completed2
        if selftest and ctx.plant is None:
            coverage(ctx, staging)
    return {"insts": insts, "records": records, "tables": pr["tables"], "done_ids": done_ids, "la24": la24,
            "all_green": all_green, "replay": replay, "tables_digest": tables_digest, "stopped": stopped}


def strip(rec):
    out = dict(rec)
    out["windows"] = [{k: v for k, v in w.items() if k != "_groups"} for w in rec["windows"]]
    return out


def verdicts(ctx, state):
    insts = state["insts"]
    tokens = {}
    counts = {}
    by_part = {}
    primary_tokens = []
    recs = []
    for inst in insts:
        iid = inst["id"]
        rec = state["records"].get(iid)
        if rec is None or iid not in state["done_ids"]:
            rec = {"id": iid, "rule": inst["rule"], "q": inst["q"], "lattice": "T%d" % inst["L"],
                   "partition": inst["partition"], "wing": inst["wing"], "D": inst["D"],
                   "slice": inst["slice"], "family": inst["family"], "primary": inst["primary"],
                   "windows": [{"k": k, "token": "VOID", "reason": state["stopped"],
                                "same_histories_as": None} for k in inst["ks"]]}
        rec = strip(rec)
        recs.append(rec)
        for w in rec["windows"]:
            tokens["%s/k%d" % (iid, w["k"])] = w["token"]
            if inst["primary"] and w["same_histories_as"] is None:
                counts[w["token"]] = counts.get(w["token"], 0) + 1
                bp = by_part.setdefault(inst["partition"], {})
                bp[w["token"]] = bp.get(w["token"], 0) + 1
                primary_tokens.append((inst["partition"], w["token"]))
    la_recs = la_records(state["la24"])
    for rec in la_recs:
        for w in rec["windows"]:
            tokens["%s/k%d" % (rec["id"], w["k"])] = w["token"]
    recs += la_recs
    hidden_prior = [t for p, t in primary_tokens if p in ("cb3", "reg")]
    if ctx.bound is not None or ctx.budget.exhausted or any(
            t in ("VOID", "LOCALITY-UNDECIDED") for _, t in primary_tokens):
        headline = "INCOMPLETE"
    elif any(t.startswith("BELL-VIOLATION-NO-SIGNALLING") for t in hidden_prior):
        headline = "BELL-VIOLATION-NO-SIGNALLING-FOUND"
    elif any(t == "SIGNALLING" for t in hidden_prior):
        headline = "SIGNALLING-FOUND"
    elif any(t == "DEPENDENCE-MASKED-LOCAL" for _, t in primary_tokens):
        headline = "DEPENDENCE-MASKED-LOCAL-ONLY"
    else:
        headline = "NO-DEPENDENCE"
    return recs, {"headline": headline, "counts": counts, "counts_by_partition": by_part, "tokens": tokens}


def reject_fractional(obj, path="$"):
    """The result schema rejects JSON numbers with a fractional part (there are none, timing included)."""
    if isinstance(obj, bool) or obj is None or isinstance(obj, (int, str)):
        return []
    if isinstance(obj, dict):
        bad = []
        for k, v in obj.items():
            bad += reject_fractional(v, path + "." + str(k))
        return bad
    if isinstance(obj, (list, tuple)):
        bad = []
        for i, v in enumerate(obj):
            bad += reject_fractional(v, path + "[%d]" % i)
        return bad
    return [path]


# ---- invocation log, staging, publication ---------------------------------------------------
def log_append(obj):
    with open(LOG, "a") as fh:
        fh.write(json.dumps(obj, sort_keys=True) + "\n")
        fh.flush()
        os.fsync(fh.fileno())


def log_lines():
    if not os.path.exists(LOG):
        return []
    with open(LOG) as fh:
        return [json.loads(x) for x in fh.read().splitlines() if x.strip()]


def invocation_table(own_line, own_status):
    lines = log_lines()
    exits = {x["start_line"]: x for x in lines if x.get("event") == "exit"}
    out = []
    for x in lines:
        if x.get("event") != "start":
            continue
        e = exits.get(x["line"])
        ent = {"utc": x["utc"], "argv": x["argv"], "program_sha256": x["program_sha256"], "line": x["line"],
               "exit": e["exit"] if e else None, "published": e["published"] if e else None}
        if x["line"] == own_line:
            ent["exit"] = own_status
            ent["published"] = True
        out.append(ent)
    return out


def delete_leftover_staging(start_line, planted=False):
    if os.path.lexists(STAGING):
        shutil.rmtree(STAGING)
        log_append({"event": "staging_deleted_unread", "utc": utc_now(), "start_line": start_line,
                    "planted": planted})
        return True
    return False


def execute(selftest, plant, out_dir, own_line, extra_invariants=None):
    """One execution: both passes, then publication by one rename.  Returns (status, published)."""
    ctx = Ctx(selftest, plant)
    status = None
    state = None
    if os.path.lexists(out_dir):
        return 1, False
    os.makedirs(STAGING)
    inv_failed = False
    try:
        try:
            for rec in (extra_invariants or []):
                ctx.invariant(rec["name"], rec["ok"], rec["measured"])
            state = core(ctx, STAGING)
        except InvariantFailure:
            inv_failed = True
        except BoundReached as exc:
            ctx.bound = str(exc)
        all_green = state["all_green"] if state is not None else False
        if inv_failed:
            status = 4
        elif not all_green:
            status = 2
        elif ctx.bound is not None or ctx.budget.exhausted:
            status = 3
        else:
            status = 0
        wall = (time.monotonic_ns() - ctx.start_ns) // (10 ** 9)
        with open("/proc/self/status") as fh:
            threads = [int(x.split()[1]) for x in fh.read().splitlines() if x.startswith("Threads:")][0]
        result = {
            "schema": SCHEMA, "prereg_sha256": sha256_file(PREREG), "program_sha256": program_sha256(),
            "corpus_pin": CORPUS_PIN, "selftest": selftest,
            "controls": list(ctx.controls.values()),
            "controls_all_green": bool(all_green) and bool(ctx.controls),
            "invariants": ctx.invariants,
            "instances": None, "verdicts": None,
            "invocations": invocation_table(own_line, status),
            "tables_digest": None,
            "replay": state["replay"] if state is not None else {"performed": False, "tables_digest_equal": None},
            "timing": {"wall_seconds": int(wall),
                       "peak_rss_mb": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024),
                       "processes": 1, "threads": threads,
                       "lp_solved": ctx.budget.solved, "lp_milliseconds": int(ctx.budget.used // (10 ** 6))},
            "exit_status": status,
        }
        for name in os.listdir(STAGING):
            path = os.path.join(STAGING, name)
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
        if status in (0, 3) and not selftest:
            recs, verd = verdicts(ctx, state)
            result["instances"] = recs
            result["verdicts"] = verd
            result["tables_digest"] = state["tables_digest"]
            result["resource_bound"] = {"pass_bound": ctx.bound, "lp_bound": bool(ctx.budget.exhausted)}
            write_outputs(STAGING, state, ctx.certs)
        bad = reject_fractional(result)
        if bad:
            raise RuntimeError("fractional JSON number at " + bad[0])
        with open(os.path.join(STAGING, "results.json"), "w") as fh:
            json.dump(result, fh, sort_keys=True, indent=1)
        if status in (2, 4) or selftest:
            with open(os.path.join(STAGING, "results.json")) as fh:
                back = json.load(fh)
            assert back["instances"] is None and back["verdicts"] is None and back["tables_digest"] is None
            assert sorted(os.listdir(STAGING)) == ["results.json"]
        os.makedirs(os.path.dirname(out_dir), exist_ok=True)
        assert not os.path.lexists(out_dir)
        os.rename(STAGING, out_dir)
        published = True
    except BaseException as exc:
        print("[stage2] error: %s: %s" % (type(exc).__name__, exc), flush=True)
        status = 1
        published = False
        if os.path.lexists(STAGING):
            shutil.rmtree(STAGING)
        if os.path.lexists(out_dir) and not os.path.exists(os.path.join(out_dir, "results.json")):
            status = 1
    if os.path.lexists(STAGING):
        shutil.rmtree(STAGING)
        status = 4
        published = False
    return status, published


def selftest_plants(own_line):
    """Planted failures on the dummy rule, each with an output path of its own."""
    records = []
    plan = [("red_control", 2), ("invariant", 4), ("replay", 4), ("error", 1)]
    for i, (plant, want) in enumerate(plan, start=1):
        out_dir = os.path.join(RUNS, "%d-planted-%d" % (own_line, i))
        status, published = execute(True, plant, out_dir, own_line)
        ok = status == want and not os.path.lexists(STAGING)
        if want == 1:
            ok = ok and not published and not os.path.lexists(out_dir)
        else:
            ok = ok and published and sorted(os.listdir(out_dir)) == ["results.json"]
            if ok:
                with open(os.path.join(out_dir, "results.json")) as fh:
                    back = json.load(fh)
                ok = (back["instances"] is None and back["verdicts"] is None
                      and back["tables_digest"] is None and back["exit_status"] == want)
        records.append({"name": "planted-%d-%s" % (i, plant), "ok": bool(ok),
                        "measured": {"exit_status": status, "required": want, "published": int(published)}})
        print("[stage2] planted case %d (%s): exit %s" % (i, plant, status), flush=True)
    os.makedirs(STAGING)
    with open(os.path.join(STAGING, "leftover"), "w") as fh:
        fh.write("planted leftover staging area\n")
    before = len(log_lines())
    deleted = delete_leftover_staging(own_line, planted=True)
    lines = log_lines()
    ok = (deleted and not os.path.lexists(STAGING) and len(lines) == before + 1
          and lines[-1].get("event") == "staging_deleted_unread")
    records.append({"name": "planted-leftover-staging", "ok": bool(ok), "measured": {"deleted": int(deleted)}})
    return records


def on_signal(signum, frame):
    raise Terminated("signal %d" % signum)


def main(argv):
    selftest = "--selftest" in argv[1:]
    unknown = [a for a in argv[1:] if a != "--selftest"]
    log_append({"event": "start", "utc": utc_now(), "argv": argv, "program_sha256": program_sha256(),
                "line": len(log_lines()) + 1})
    own_line = len(log_lines())
    status = 1
    published = False
    try:
        signal.signal(signal.SIGTERM, on_signal)
        signal.signal(signal.SIGINT, on_signal)
        delete_leftover_staging(own_line)
        out_dir = os.path.join(RUNS, str(own_line))
        if unknown:
            raise RuntimeError("unknown arguments")
        if os.path.lexists(out_dir):
            status, published = 1, False
        elif selftest:
            extra = selftest_plants(own_line)
            status, published = execute(True, None, out_dir, own_line, extra)
        else:
            status, published = execute(False, None, out_dir, own_line)
    except BaseException as exc:
        print("[stage2] error: %s: %s" % (type(exc).__name__, exc), flush=True)
        status, published = 1, False
        if os.path.lexists(STAGING):
            shutil.rmtree(STAGING)
    if os.path.lexists(STAGING):
        status, published = 4, False
    log_append({"event": "exit", "utc": utc_now(), "exit": status, "published": bool(published),
                "start_line": own_line})
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv))
