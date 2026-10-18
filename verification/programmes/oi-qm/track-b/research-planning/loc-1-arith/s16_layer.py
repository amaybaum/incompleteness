"""The Q(zeta_16) layer of the LOC-1 S16 engine, and its control K-arith-16 on synthetic inputs (research development).

The layer runs the frozen engine c21_engine.py (sha256 ENGINE_SHA256), byte for byte, in a fresh module namespace
in which exactly three names are rebound after the source has executed:

    int       -> Q16.coerce   the engine's entry conversion keeps entries exact in Q(zeta_16)       (E1)
    Fraction  -> Q16.coerce   arith="exact" runs N2 in Q(zeta_16) instead of Q                     (cross-check)
    PR        -> PLACE        'x % PR' is rho: Z[zeta]_P -> F_p, zeta -> w, p = 1 (mod 16), and the
                              union-find's arithmetic is mod p; the engine's own assertion that no
                              nonzero entry has image 0 is then E2's assertion                     (E2)

The static order sorts entries by Q16's total order on normal forms (E3).  Nothing else changes, so the symmetry
breaking, the four rules, the leaf rule, the budget and the undo records are the frozen code's (E4); e4_check()
verifies the source digest, the rebound names and that every other global is the one the source defines.

This file evaluates no target object.  check_entries() is the stage-2 assertion over a target set; here it runs on
synthetic matrices only.

Run:  python3 -I -B s16_layer.py --self-test [--full]   (fast by default, well under two minutes; --full for CI)
"""
import hashlib
import itertools
import os
import sys
import tempfile
import time
import types

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cyclo16 import PLACE, Place, Q16, SM64, zeta  # noqa: E402

ENGINE_SHA256 = "28a6a538245a250f7e4aa80957f9e420d191a38461e3cfc02955f5da7f5dd6fc"
ENGINE_PATH = os.path.join(HERE, "c21_engine.py")
REBOUND = ("Fraction", "PR", "int")


def _exec_source(src, name):
    mod = types.ModuleType(name)
    mod.__file__ = name + ".py"
    exec(compile(src, name + ".py", "exec"), mod.__dict__)
    return mod


def load_engine(path=ENGINE_PATH, layered=True, place=PLACE, expect_sha=ENGINE_SHA256, extra=None):
    """The frozen engine as a module: plain (integer) or with the Q(zeta_16) layer bound."""
    with open(path, "rb") as fh:
        src = fh.read()
    digest = hashlib.sha256(src).hexdigest()
    if expect_sha is not None and digest != expect_sha:
        raise ValueError("engine source sha256 %s is not the frozen %s" % (digest, expect_sha))
    mod = _exec_source(src, "c21_engine_q16" if layered else "c21_engine_int")
    mod.SOURCE_SHA256 = digest
    mod.REBOUND = ()
    if layered:
        mod.int = Q16.coerce
        mod.Fraction = Q16.coerce
        mod.PR = place
        mod.REBOUND = REBOUND
        for k, v in (extra or {}).items():          # negative controls only
            setattr(mod, k, v)
            mod.REBOUND = tuple(sorted(set(mod.REBOUND) | {k}))
    return mod


def e4_check(mod, path=ENGINE_PATH):
    """E4: the layered module is the frozen source with exactly int, Fraction and PR rebound."""
    bad = []
    if mod.SOURCE_SHA256 != ENGINE_SHA256:
        bad.append("source digest differs from the frozen engine")
    plain = load_engine(path, layered=False, expect_sha=None)
    skip = {"SOURCE_SHA256", "REBOUND", "__builtins__"}
    names_l = set(mod.__dict__) - skip
    names_p = set(plain.__dict__) - skip
    if names_l - names_p != {"int"}:
        bad.append("names added by the layer: %s" % sorted(names_l - names_p))
    if names_p - names_l:
        bad.append("names removed by the layer: %s" % sorted(names_p - names_l))
    changed = set()
    for k in names_l & names_p:
        a, b = mod.__dict__[k], plain.__dict__[k]
        if k.startswith("__"):
            continue
        if k in REBOUND:
            if a is b:
                changed.add(k + " (not rebound)")
            continue
        if isinstance(a, type) and isinstance(b, type):
            for attr, va in vars(a).items():
                vb = vars(b).get(attr)
                ca, cb = getattr(va, "__code__", None), getattr(vb, "__code__", None)
                if (ca is None) != (cb is None) or (ca is not None and (ca.co_code != cb.co_code or
                                                                         ca.co_consts != cb.co_consts)):
                    changed.add(k + "." + attr)
        elif hasattr(a, "__code__"):
            if a.__code__.co_code != b.__code__.co_code or a.__code__.co_consts != b.__code__.co_consts:
                changed.add(k)
        elif a is not b and a != b:
            changed.add(k)
    if changed:
        bad.append("globals that differ from the frozen source: %s" % sorted(changed))
    if tuple(sorted(mod.REBOUND)) != REBOUND:
        bad.append("rebound names %s, not %s" % (list(mod.REBOUND), list(REBOUND)))
    return bad


def to_q16(mats):
    return [[[Q16.coerce(x) for x in row] for row in M] for M in mats]


def check_entries(mats, place=PLACE):
    """E2's precondition over a target set: every nonzero entry has a denominator prime to p and image != 0.
    Returns the offending (target, row, column) positions."""
    out = []
    for k, M in enumerate(mats):
        for i, row in enumerate(M):
            for j, x in enumerate(row):
                x = Q16.coerce(x)
                if not x:
                    continue
                try:
                    if place.rho(x) == 0:
                        out.append((k, i, j, "image 0"))
                except ValueError:
                    out.append((k, i, j, "denominator divisible by p"))
    return out


# ------------------------------------------------------------------- an independent exact product test (PC)

def is_product(M, sig, m, n):
    """M^sig = A (x) B, by rank <= 1 of the reshuffle, written here independently of the engine's leaf_ok."""
    inv = [0] * (m * n)
    for i, g in enumerate(sig):
        inv[g] = i
    R = [[M[inv[a * n + b]][inv[a2 * n + b2]] for b in range(n) for b2 in range(n)]
         for a in range(m) for a2 in range(m)]
    piv = next(((r, c) for r in range(len(R)) for c in range(len(R[0])) if R[r][c]), None)
    if piv is None:
        return True
    p, q = piv
    for r in range(len(R)):
        for c in range(len(R[0])):
            if R[r][c] * R[p][q] != R[r][q] * R[p][c]:
                return False
    return True


def brute_classes(mod, mats, m, n, order):
    N = m * n
    out = set()
    for perm in itertools.permutations(range(N)):
        if all(is_product(M, perm, m, n) for M in mats):
            out.add(mod.canonical(perm, m, n, order))
    return out


# ------------------------------------------------------------------- synthetic instances

def rq16(rng, span=2, dens=3, zero_p=0):
    if zero_p and rng.below(100) < zero_p:
        return Q16()
    c = [0] * 8
    for _ in range(dens):
        c[rng.below(8)] = rng.below(2 * span + 1) - span
    x = Q16(c)
    return x if x else Q16((1,))


def rmat(rng, k, f):
    return [[f() for _ in range(k)] for _ in range(k)]


def planted(mod, rng, m, n, zero_p=0):
    A = rmat(rng, m, lambda: rq16(rng, zero_p=zero_p))
    B = rmat(rng, n, lambda: rq16(rng, zero_p=zero_p))
    sig = list(range(m * n))
    for i in range(len(sig) - 1, 0, -1):
        j = rng.below(i + 1)
        sig[i], sig[j] = sig[j], sig[i]
    return mod.relabel(mod.kron(A, B), sig), tuple(sig)


def run(mod, mats, m, n, mode, rules="RWVP", arith="modp", mut=None, budget=10 ** 7):
    eng = mod.Engine(mats, m, n, rules=rules, order="greedy", arith=arith, mut=mut)
    status, found, counts = eng.run(mode, budget)
    return eng, status, set(found), counts


# ------------------------------------------------------------------- K-arith-16

def self_test(full=False):
    t0 = time.perf_counter()
    lines, ok = [], True
    npos = nneg = 0

    def rep(name, passed, detail="", neg=False):
        nonlocal ok, npos, nneg
        ok &= bool(passed)
        if neg:
            nneg += 1
        else:
            npos += 1
        lines.append("%s %s%-58s %s" % ("PASS" if passed else "FAIL", "NEG " if neg else "", name, detail))

    L = load_engine()
    I = load_engine(layered=False)

    # E4
    bad = e4_check(L)
    rep("E4: frozen source, only int/Fraction/PR rebound", not bad, "; ".join(bad) or "sha256 %s" % L.SOURCE_SHA256[:16])
    with open(ENGINE_PATH, "rb") as fh:
        src = bytearray(fh.read())
    src[src.index(b"budget=10 ** 8")] ^= 0x01
    fd, tmp = tempfile.mkstemp(suffix=".py")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(bytes(src))
        try:
            load_engine(tmp)
            refused = False
        except ValueError:
            refused = True
    finally:
        os.remove(tmp)
    rep("E4: a one-byte change to the engine source is refused", refused, neg=True)
    X = load_engine(extra={"canonical": lambda *a: ()})
    rep("E4: an extra rebinding (canonical) is detected", bool(e4_check(X)), neg=True)

    # E2: the place and the engine's assertion
    rep("E2: p prime, p = 1 (mod 16), w^8 = -1", PLACE.valid(), "p = %d" % int(PLACE))
    rng = SM64(0x4B413136)
    Mp, _ = planted(L, rng, 2, 2)
    Mk = [row[:] for row in Mp]
    Mk[0][0] = zeta(1) - Q16((PLACE.w,))
    try:
        L.Engine([Mk], 2, 2)
        fired = False
    except AssertionError:
        fired = True
    rep("E2: the engine refuses a nonzero entry with image 0", fired and bool(check_entries([Mk])),
        "check_entries flags %d position(s)" % len(check_entries([Mk])))
    rep("E2: check_entries passes a planted synthetic product", not check_entries([Mp]))

    # E1/E4 on integers: the layer reproduces the integer engine exactly
    rng = SM64(0x4B413137)
    ints = []
    for t in range(3 if not full else 12):
        m, n = (2, 2) if t % 3 == 0 else (2, 3) if t % 3 == 1 else (3, 2)
        A = [[rng.below(5) - 2 for _ in range(m)] for _ in range(m)]
        B = [[rng.below(5) - 2 for _ in range(n)] for _ in range(n)]
        sig = list(range(m * n))
        for i in range(len(sig) - 1, 0, -1):
            j = rng.below(i + 1)
            sig[i], sig[j] = sig[j], sig[i]
        ints.append(([I.relabel(I.kron(A, B), sig)], m, n))
        ints.append(([[[rng.below(5) - 2 for _ in range(m * n)] for _ in range(m * n)]], m, n))
    for _ in range(1 if not full else 4):
        A = [[rng.below(7) - 3 or 1 for _ in range(4)] for _ in range(4)]
        B = [[rng.below(7) - 3 or 1 for _ in range(4)] for _ in range(4)]
        sig = list(range(16))
        for i in range(15, 0, -1):
            j = rng.below(i + 1)
            sig[i], sig[j] = sig[j], sig[i]
        ints.append(([I.relabel(I.kron(A, B), sig)], 4, 4))
    if full:
        tr = list(range(16))
        tr[3], tr[11] = tr[11], tr[3]
        ints.append(([[[1 if tr[i] == j else 0 for j in range(16)] for i in range(16)]], 4, 4))
    same = 0
    for mats, m, n in ints:
        mode = "exist" if m * n == 16 else "all"
        ei, si, fi, ci = run(I, mats, m, n, mode, budget=10 ** 8)
        el, sl, fl, cl = run(L, to_q16(mats), m, n, mode, budget=10 ** 8)
        same += (si, fi, ei.order) == (sl, fl, el.order)
    rep("E1/E3/E4: on %d integer instances the layer equals the integer engine" % len(ints), same == len(ints),
        "%d/%d equal in status, classes and static order" % (same, len(ints)))

    # Q(zeta_16) instances: exact N2 and N2 on images give the same classes, and brute force agrees (N <= 6 or 9)
    rng = SM64(0x4B413138)
    shapes = [(2, 2), (2, 3), (3, 2)] + ([(2, 4), (3, 3)] if full else [])
    agree = total = planted_hit = 0
    for (m, n) in shapes:
        for kind in ("planted", "planted-zeros", "near-product", "non-product"):
            if kind == "non-product":
                M = rmat(rng, m * n, lambda: rq16(rng))
                sig = None
            else:
                M, sig = planted(L, rng, m, n, zero_p=30 if kind == "planted-zeros" else 0)
                if kind == "near-product":
                    i, j = rng.below(m * n), rng.below(m * n)
                    M[i][j] = M[i][j] + zeta(3) + Q16((1,))
                    sig = None
            el, sp, fp, _ = run(L, [M], m, n, "all")
            _, sx, fx, _ = run(L, [M], m, n, "all", arith="exact")
            bf = brute_classes(L, [M], m, n, el.order)
            total += 1
            agree += (sp == sx == "ALL" and fp == fx == bf)
            if sig is not None:
                planted_hit += L.canonical(sig, m, n, el.order) in fp
    rep("K-arith-16: %d Q(zeta_16) instances, modp = exact = brute force" % total, agree == total,
        "%d/%d agree; planted classes recovered %d" % (agree, total, planted_hit))
    rep("K-arith-16: every planted class is recovered", planted_hit == sum(1 for _ in shapes) * 2)

    # 4 x 4 planted Q(zeta_16) products in existence mode (the C21 shape)
    rng = SM64(0x4B413139)
    hits = 0
    nplant = 1 if not full else 6
    for _ in range(nplant):
        M, sig = planted(L, rng, 4, 4)
        el, st, fd, cnt = run(L, [M], 4, 4, "exist", budget=10 ** 6)
        hits += st == "FOUND" and all(is_product(M, f, 4, 4) for f in fd)
    rep("K-arith-16: 4x4 planted Q(zeta_16) products found and verified", hits == nplant, "%d/%d" % (hits, nplant))

    # collision: an entry changed by zeta - w passes every image test at its planted leaf; the exact leaf rejects it
    rng = SM64(0x434F4C4C)
    m, n = (2, 3) if not full else (4, 4)
    while True:
        M, sig = planted(L, rng, m, n)
        if all(x for row in M for x in row):
            break
    i, j = rng.below(m * n), rng.below(m * n)
    Mc = [row[:] for row in M]
    Mc[i][j] = M[i][j] + zeta(1) - Q16((PLACE.w,))
    imgs_equal = all((Mc[a][b] % PLACE) == (M[a][b] % PLACE) for a in range(m * n) for b in range(m * n))
    cm, cn = m, n
    _, st, fd, cnt = run(L, [Mc], m, n, "all", rules="R")
    rep("K-arith-16 collision (%dx%d, rules=R)" % (m, n), imgs_equal and st == "ALL" and not fd and cnt[2] >= 1,
        "images equal %s, status %s, classes %d, leaves reached %d" % (imgs_equal, st, len(fd), cnt[2]))

    # negative: a non-homomorphic reduction (w of order 8) loses planted classes that exact N2 keeps
    rng = SM64(0x4B41313A)
    badP = Place(int(PLACE), PLACE.w * PLACE.w)
    LB = load_engine(place=badP)
    lost = 0
    trials = 4 if not full else 12
    for t in range(trials):
        m, n = ((2, 2), (2, 3), (3, 2))[t % 3]
        M, sig = planted(L, rng, m, n)
        try:
            el, sp, fp, _ = run(LB, [M], m, n, "all")
            _, sx, fx, _ = run(LB, [M], m, n, "all", arith="exact")
            lost += fp != fx
        except AssertionError:
            lost += 1
    rep("E2 is load-bearing: w of order 8 changes the class set", lost > 0, "%d/%d instances differ" % (lost, trials),
        neg=True)

    # negative: the frozen engine mutations are detected on Q(zeta_16) instances
    rng = SM64(0x4D555451)
    muts = ("MUT-LEAF", "MUT-SECOND") if not full else L.MUTATIONS
    inst = []
    for (m, n) in ((2, 3), (3, 2), (2, 2)):
        M, sig = planted(L, rng, m, n, zero_p=25)
        inst.append(([M], m, n))
        inst.append(([rmat(rng, m * n, lambda: rq16(rng))], m, n))
    for mut in muts:
        detected = False
        _, st, fd, _ = run(L, [Mc], cm, cn, "all", rules="R", mut=mut)
        if st != "ALL" or fd:
            detected = True                         # the collision instance has no class (K-collision)
        for mats, m, n in ([] if detected else inst):
            el, st, fd, _ = run(L, mats, m, n, "all", mut=mut)
            bf = brute_classes(L, mats, m, n, el.order)
            if st != "ALL" or fd != bf:
                detected = True
                break
        rep("engine mutation %s detected" % mut, detected, neg=True)

    dt = time.perf_counter() - t0
    lines.append("s16_layer K-arith-16 self-test (%s): %d positive controls, %d negative controls: %s"
                 % ("full" if full else "fast", npos, nneg, "ALL PASS" if ok else "FAILURE"))
    sys.stderr.write("s16_layer self-test %.1f s\n" % dt)
    return ok, lines


def main(argv):
    if argv[:1] == ["--self-test"]:
        ok, lines = self_test(full="--full" in argv[1:])
        print("\n".join(lines))
        return 0 if ok else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
