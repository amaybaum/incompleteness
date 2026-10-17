#!/usr/bin/env python3
"""Avenue 1: the padded two-token experiment realized by the finite reversible gluing construction
of papers/Main.md (Theorem "finite operational realization and gluing", exact-ring variant).

Standard library only; arithmetic in Q(i).  Self-contained: reads no file.
Run:  python3 -I oi_realization_exact.py

The construction, as stated there: visible sector = step counter t, intervention record and outcome
registers; hidden sector = the unnormalized branch matrix R, a predecessor stack and K preloaded
seeds uniform on {0..G-1}; one FIXED step map phi_a per instrument a.  A unitary instrument
conjugates R; an instrument with outcomes computes q_o = Tr(Pi_o R Pi_o) exactly, compares the t-th
seed r by the exact threshold G*q_<o <= r*sum(q) < G*q_<=o, writes o, and sets R <- Pi_o R Pi_o.
Every step pushes the predecessor register; the stack carries invertibility.  With G a common
denominator of every conditional the grid is exact.

Two register models of the same experiment:
  V16  verbatim: the experiment is one quantum system of dimension d = 16 (qubits A, B, hA, hB),
       initial |00><00| (x) I/4; R is its 16 x 16 branch matrix.
  VS   site-assigned: R is the 4 x 4 branch matrix of (A, B); hA and hB are separate hidden
       classical sites, hA in region A and hB in region B, with the fixed product prior uniform on
       {0,1}^2.  L reads both sites.  No other instrument reads or writes them.
Instruments: HA, VA (local A); HB, VB, XB (local B); CN = CNOT(A->B), L = X_B iff hA xor hB (joint);
MZB (Z on B), RD (Z on A and Z on B, the visible readout of both regions).
Protocols: 7 preparation words (two with selection on MZB) x 43 test words (|w| <= 2) x RD.

Checks:
  GRID  G = lcm of the denominators of every conditional outcome probability (exact).
  LAW   for every protocol and both register models, the realized joint outcome law (all seeds at
        the measured steps, and in VS the prior on hA, hB) equals the Born law computed by an
        independent dense Kronecker-product code path.
  INJ   each phi_a is injective on the states it is applied to, and the explicit inverse
        (pop the stack, strip the record, t - 1) recovers the argument.
  BIJ   each phi_a extends to a bijection of one finite set S containing all reached states.
  SEED  phi_a reads the seed of its own step only (regression, every 7th reached state).
  SITE  VS: no instrument other than L depends on hA or hB, or changes them; L depends on hA and on
        hB (exact witnesses).  V16: every instrument other than L acts identically on the four hh
        blocks of every reached register; L conjugates exactly the odd-parity blocks by X_B.
  TBL   the realized stage table reproduces the non-local-tomography certificate: Qe and Qo agree on
        every local-only test and differ on (L, RD).
A mutation self-test runs first; the verdict prints only if every mutation is detected and every
unmutated check passes.
"""
from fractions import Fraction as Fr
from math import lcm
import sys

MUT = set()
RESULTS = []


def check(ok, cid, text):
    RESULTS.append((bool(ok), cid, text))


# ---------------------------------------------------------------- Gaussian rationals as pairs
def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gconj(x):
    return (x[0], -x[1])


def gsc(x, f):
    return (x[0] * f, x[1] * f)


ZERO = (Fr(0), Fr(0))


def g(re, im=0):
    return (Fr(re), Fr(im))


# ---------------------------------------------------------------- reference: dense Born law
def dzeros(n):
    return [[ZERO] * n for _ in range(n)]


def dkron(a, b):
    na, nb = len(a), len(b)
    return [[gmul(a[i // nb][j // nb], b[i % nb][j % nb]) for j in range(na * nb)] for i in range(na * nb)]


def dmm(a, b):
    n = len(a)
    out = dzeros(n)
    for i in range(n):
        row = a[i]
        for k in range(n):
            if row[k] == ZERO:
                continue
            bk = b[k]
            for j in range(n):
                if bk[j] != ZERO:
                    out[i][j] = gadd(out[i][j], gmul(row[k], bk[j]))
    return out


def ddag(a):
    n = len(a)
    return [[gconj(a[j][i]) for j in range(n)] for i in range(n)]


I2 = [[g(1), ZERO], [ZERO, g(1)]]
H2 = [[g(1), g(1)], [g(1), g(-1)]]            # sqrt(2) H
V2 = [[g(1), g(0, -1)], [g(1), g(0, 1)]]      # sqrt(2) H S^dag
X2 = [[ZERO, g(1)], [g(1), ZERO]]
P0 = [[g(1), ZERO], [ZERO, ZERO]]
P1 = [[ZERO, ZERO], [ZERO, g(1)]]


def k4(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = dkron(out, m)
    return out


def dperm(f):
    out = dzeros(16)
    for i in range(16):
        out[f(i)][i] = g(1)
    return out


def bit16(i, k):
    return (i >> (3 - k)) & 1


DENSE_U = {
    "HA": (k4(H2, I2, I2, I2), Fr(1, 2)),
    "VA": (k4(V2, I2, I2, I2), Fr(1, 2)),
    "HB": (k4(I2, H2, I2, I2), Fr(1, 2)),
    "VB": (k4(I2, V2, I2, I2), Fr(1, 2)),
    "XB": (k4(I2, X2, I2, I2), Fr(1)),
    "CN": (dperm(lambda i: i ^ (4 * bit16(i, 0))), Fr(1)),
    "L": (dperm(lambda i: i ^ (4 * (bit16(i, 2) ^ bit16(i, 3)))), Fr(1)),
}
DENSE_P = {
    "MZB": [k4(I2, P0, I2, I2), k4(I2, P1, I2, I2)],
    "RD": [k4(P0, P0, I2, I2), k4(P0, P1, I2, I2), k4(P1, P0, I2, I2), k4(P1, P1, I2, I2)],
}


def dense_init():
    R = dzeros(16)
    for h in range(4):
        R[h][h] = g(Fr(1, 4))
    return R


def dtr(R):
    s = ZERO
    for i in range(len(R)):
        s = gadd(s, R[i][i])
    return s


def born_law(protocol):
    """Joint law of the outcome sequence: dict outcome-tuple -> probability, by dense products."""
    branches = {(): dense_init()}
    for sym in protocol:
        new = {}
        for outs, R in branches.items():
            if sym in DENSE_U:
                M, s = DENSE_U[sym]
                Rn = dmm(dmm(M, R), ddag(M))
                new[outs] = [[gsc(x, s) for x in row] for row in Rn]
            else:
                for o, P in enumerate(DENSE_P[sym]):
                    Rn = dmm(dmm(P, R), P)
                    if dtr(Rn) != ZERO:
                        new[outs + (o,)] = Rn
        branches = new
    law = {}
    for outs, R in branches.items():
        t = dtr(R)
        assert t[1] == 0
        law[outs] = t[0]
    return law


def conditionals(protocol):
    """Every conditional probability of an outcome at a measured step, given the earlier outcomes."""
    out = []
    branches = {(): dense_init()}
    for sym in protocol:
        new = {}
        for outs, R in branches.items():
            if sym in DENSE_U:
                M, s = DENSE_U[sym]
                Rn = dmm(dmm(M, R), ddag(M))
                new[outs] = [[gsc(x, s) for x in row] for row in Rn]
            else:
                tot = dtr(R)[0]
                for o, P in enumerate(DENSE_P[sym]):
                    Rn = dmm(dmm(P, R), P)
                    q = dtr(Rn)[0]
                    out.append(q / tot)
                    if q != 0:
                        new[outs + (o,)] = Rn
        branches = new
    return out


# ---------------------------------------------------------------- the machine: register models
# a register is a frozen sparse matrix: tuple of sorted ((i, j), (re, im)) with nonzero entries
INTERN = {}
REGS = []


def intern(d):
    key = tuple(sorted((k, v) for k, v in d.items() if v != ZERO))
    if key not in INTERN:
        INTERN[key] = len(REGS)
        REGS.append(key)
    return INTERN[key]


def reg_dict(rid):
    return dict(REGS[rid])


class Model:
    """Register model: dimension n, qubit list, initial register, hidden-site prior."""

    def __init__(self, name):
        self.name = name
        if name == "V16":
            self.nq = 4                       # A, B, hA, hB
            init = {(h, h): g(Fr(1, 4)) for h in range(4)}
            self.prior = [()]
        else:
            self.nq = 2                       # A, B
            init = {(0, 0): g(1)}
            self.prior = [(ha, hb) for ha in range(2) for hb in range(2)]
        self.init = intern(init)
        self.cache = {}

    def bit(self, i, k):
        return (i >> (self.nq - 1 - k)) & 1

    def setbit(self, i, k, v):
        sh = self.nq - 1 - k
        return (i & ~(1 << sh)) | (v << sh)

    def conj1(self, d, k, M, s):
        out = {}
        for (i, j), v in d.items():
            bi, bj = self.bit(i, k), self.bit(j, k)
            for x in range(2):
                mx = M[x][bi]
                if mx == ZERO:
                    continue
                for y in range(2):
                    my = M[y][bj]
                    if my == ZERO:
                        continue
                    key = (self.setbit(i, k, x), self.setbit(j, k, y))
                    out[key] = gadd(out.get(key, ZERO), gsc(gmul(gmul(mx, v), gconj(my)), s))
        return out

    def permute(self, d, f):
        return {(f(i), f(j)): v for (i, j), v in d.items()}

    def unitary(self, sym, rid, hid):
        key = (sym, rid, hid)             # the full input: a cache must not hide a dependency
        if key in self.cache:
            return self.cache[key]
        d = reg_dict(rid)
        if sym in ("HA", "VA", "HB", "VB"):
            k = 0 if sym[1] == "A" else 1
            M = H2 if sym[0] == "H" else V2
            if sym == "HA" and "local_reads_h" in MUT and self.name == "VS" and hid[0] == 1:
                out = d
            else:
                out = self.conj1(d, k, M, Fr(1, 2))
        elif sym == "XB":
            out = self.permute(d, lambda i: self.setbit(i, 1, 1 - self.bit(i, 1)))
        elif sym == "CN":
            out = self.permute(d, lambda i: self.setbit(i, 1, self.bit(i, 1) ^ self.bit(i, 0)))
        elif sym == "L":
            if self.name == "V16":
                out = self.permute(d, lambda i: self.setbit(i, 1, self.bit(i, 1) ^ self.bit(i, 2) ^ self.bit(i, 3)))
            else:
                par = hid[1] if "L_one_site" in MUT else (hid[0] ^ hid[1])
                out = self.permute(d, lambda i: self.setbit(i, 1, 1 - self.bit(i, 1))) if par else d
        else:
            raise ValueError(sym)
        r = intern(out)
        self.cache[key] = r
        return r

    def outcomes(self, sym):
        if sym == "MZB":
            return [lambda i, b=b: self.bit(i, 1) == b for b in range(2)]
        return [lambda i, a=a, b=b: self.bit(i, 0) == a and self.bit(i, 1) == b for a in range(2) for b in range(2)]

    def measure(self, sym, rid):
        key = (sym, rid)
        if key in self.cache:
            return self.cache[key]
        d = reg_dict(rid)
        res = []
        for pred in self.outcomes(sym):
            part = {(i, j): v for (i, j), v in d.items() if pred(i) and pred(j)}
            q = sum((v[0] for (i, j), v in part.items() if i == j), Fr(0))
            res.append((q, intern(part)))
        self.cache[key] = res
        return res


MEAS = {"MZB", "RD"}


def phi(model, a, state, G):
    """The fixed step map of instrument a.  state = (t, rec, rid, stack, seeds, hid)."""
    t, rec, rid, stack, seeds, hid = state
    if a in MEAS:
        branches = model.measure(a, rid)
        tot = sum(q for q, _ in branches)
        r = seeds[0] if "seed_reuse" in MUT else seeds[t]
        lo = Fr(0)
        chosen = None
        for o, (q, nrid) in enumerate(branches):
            hi = lo + q
            if G * lo <= r * tot < G * hi:
                chosen = (o, nrid)
                break
            lo = hi
        assert chosen is not None
        o, nrid = chosen
    else:
        o, nrid = None, model.unitary(a, rid, hid)
    if "no_ledger" in MUT:
        return (t + 1, rec, nrid, stack, seeds, hid)
    return (t + 1, rec + ((a, o),), nrid, stack + (rid,), seeds, hid)


def phi_inv(state):
    t, rec, rid, stack, seeds, hid = state
    return (t - 1, rec[:-1], stack[-1], stack[:-1], seeds, hid)


PREPS = [
    ("P00", (), None), ("P+0", ("HA",), None), ("PPhi", ("HA", "CN"), None),
    ("Qe", ("L", "MZB"), 0), ("Qo", ("L", "MZB", "XB"), 1),
    ("Qe+", ("HA", "L", "MZB"), 0), ("Qo+", ("HA", "L", "MZB", "XB"), 1),
]
TEST_SYMS = ["HA", "VA", "HB", "VB", "CN", "L"]
WORDS = [()] + [(s,) for s in TEST_SYMS] + [(s, t) for s in TEST_SYMS for t in TEST_SYMS]
LOCAL = {"HA", "VA", "HB", "VB", "XB"}
K = 7


def protocols():
    return [(pn, pw, sel, w, pw + w + ("RD",)) for pn, pw, sel in PREPS for w in WORDS]


def realize(model, G, record):
    """Run every protocol from every initial state; return realized joint laws and the domains."""
    laws = {}
    for pn, pw, sel, w, prot in protocols():
        mpos = [i for i, s in enumerate(prot) if s in MEAS]
        counts = {}
        n = 0
        for hid in model.prior:
            for combo in range(G ** len(mpos)):
                seeds = [0] * K
                c = combo
                for p in mpos:
                    seeds[p] = c % G
                    c //= G
                state = (0, (), model.init, (), tuple(seeds), hid)
                for a in prot:
                    nxt = phi(model, a, state, G)
                    record.setdefault(a, {})[state] = nxt
                    state = nxt
                outs = tuple(o for (_, o) in state[1] if o is not None) if "no_ledger" not in MUT else ()
                counts[outs] = counts.get(outs, 0) + 1
                n += 1
        laws[prot] = {k: Fr(v, n) for k, v in counts.items()}
    return laws


def run():
    RESULTS.clear()
    INTERN.clear()
    REGS.clear()
    # ---- grid
    dens = set()
    born = {}
    for pn, pw, sel, w, prot in protocols():
        born[prot] = born_law(prot)
        for c in conditionals(prot):
            dens.add(c.denominator)
    G = 1
    for d in dens:
        G = lcm(G, d)
    if "grid_small" in MUT:
        G = 2
    check(G > 1, "GRID", f"G = lcm of the conditional denominators = {G}; seeds uniform on {{0..{G - 1}}}")

    results = {}
    for mname in ("V16", "VS"):
        model = Model(mname)
        record = {}
        laws = realize(model, G, record)
        results[mname] = (model, record, laws)
        okl = all(laws[p] == born[p] for p in born) if "no_ledger" not in MUT else True
        check(okl, "LAW", f"{mname}: realized joint law = dense Born law on all {len(born)} distinct instrument sequences (the {len(protocols())} preparation-test pairs)")
        # ---- injectivity and inverse
        okinj, okinv, nstates = True, True, 0
        for a, mp in record.items():
            imgs = set(mp.values())
            okinj &= len(imgs) == len(mp)
            nstates += len(mp)
            if "no_ledger" not in MUT:
                okinv &= all(phi_inv(y) == x for x, y in mp.items())
        check(okinj and okinv, "INJ", f"{mname}: each of the {len(record)} step maps is injective on its {nstates} reached arguments in total, and the explicit inverse recovers each argument")
        # ---- bijective completion on one finite set
        S = set()
        for mp in record.values():
            S |= set(mp.keys()) | set(mp.values())
        okbij = True
        if okinj:
            Sl = sorted(S, key=repr)
            for a, mp in record.items():
                dom = set(mp)
                img = set(mp.values())
                free_src = [x for x in Sl if x not in dom]
                free_tgt = [x for x in Sl if x not in img]
                okbij &= len(free_src) == len(free_tgt)
                full = dict(mp)
                full.update(zip(free_src, free_tgt))
                okbij &= set(full.keys()) == S and set(full.values()) == S
        else:
            okbij = False
        check(okbij, "BIJ", f"{mname}: every step map extends to a bijection of one finite set of {len(S)} states (partial permutation completed on the remainder)")
        # ---- seed locality (regression sample)
        oks = True
        for a, mp in record.items():
            for idx, (x, y) in enumerate(mp.items()):
                if idx % 7:
                    continue
                t = x[0]
                for p in range(K):
                    if a in MEAS and p == t:
                        continue
                    seeds = list(x[4])
                    seeds[p] = (seeds[p] + 1) % G
                    x2 = x[:4] + (tuple(seeds),) + x[5:]
                    y2 = phi(model, a, x2, G)
                    oks &= y2 == y[:4] + (tuple(seeds),) + y[5:]
        check(oks, "SEED", f"{mname}: on every 7th reached argument, changing any seed other than that of the step's own measurement changes only that seed in the image")

    # ---- site structure, VS
    model, record, laws = results["VS"]
    ok_loc, ok_L_a, ok_L_b = True, False, False
    for a, mp in record.items():
        for x, y in mp.items():
            for k in range(2):
                h = list(x[5])
                h[k] = 1 - h[k]
                x2 = x[:5] + (tuple(h),)
                y2 = phi(model, a, x2, G)
                same = y2[:5] == y[:5] and y2[5] == tuple(h)
                if a == "L":
                    if not same:
                        if k == 0:
                            ok_L_a = True
                        else:
                            ok_L_b = True
                else:
                    ok_loc &= same
    check(ok_loc and ok_L_a and ok_L_b, "SITE", "VS: every instrument other than L is independent of the hidden sites hA, hB and leaves them unchanged on all reached arguments; L's image depends on hA and on hB (exact witnesses)")
    # ---- site structure, V16
    model16, record16, _ = results["V16"]
    ok16 = True
    for a, mp in record16.items():
        if a in MEAS:
            continue
        for x, y in mp.items():
            din, dout = reg_dict(x[2]), reg_dict(y[2])
            for (i, j) in set(din) | set(dout):
                if (i & 3) != (j & 3) and (din.get((i, j), ZERO) != ZERO or dout.get((i, j), ZERO) != ZERO):
                    ok16 = False
            for h in range(4):
                blk = {(i >> 2, j >> 2): v for (i, j), v in din.items() if (i & 3) == h and (j & 3) == h}
                blo = {(i >> 2, j >> 2): v for (i, j), v in dout.items() if (i & 3) == h and (j & 3) == h}
                vs = Model("VS")
                rb = intern(blk)
                if a == "L":
                    par = ((h >> 1) ^ h) & 1
                    exp = vs.unitary("L", rb, (par, 0))
                else:
                    exp = vs.unitary(a, rb, (0, 0))
                ok16 &= reg_dict(exp) == {k: v for k, v in blo.items() if v != ZERO}
    check(ok16, "SITE", "V16: every reached register is block-diagonal in hh; every instrument other than L acts identically on the four hh blocks, and L conjugates exactly the odd-parity blocks by X_B")

    # ---- realized table certificate (VS)
    def cond_row(prep, w):
        pn, pw, sel = next(p for p in PREPS if p[0] == prep)
        law = laws[pw + w + ("RD",)]
        if sel is None:
            return {k[-1]: v for k, v in law.items()}
        tot = sum(v for k, v in law.items() if k[0] == sel)
        return {k[-1]: v / tot for k, v in law.items() if k[0] == sel}
    if "no_ledger" in MUT:
        okt = False
    else:
        prod_words = [w for w in WORDS if all(s in LOCAL for s in w)]
        same = all(cond_row("Qe", w) == cond_row("Qo", w) for w in prod_words)
        diff = cond_row("Qe", ("L",)) != cond_row("Qo", ("L",))
        okt = same and diff
    check(okt, "TBL", "VS realized table: Qe and Qo agree on every local-only test word and differ on (L, RD)")
    return results


MUTATIONS = {
    "grid_small": "LAW",
    "no_ledger": "INJ",
    "seed_reuse": "LAW",
    "L_one_site": "SITE",
    "local_reads_h": "SITE",
}


def main():
    global MUT
    detected = {}
    for m, target in MUTATIONS.items():
        MUT = {m}
        run()
        failed = {cid for ok, cid, _ in RESULTS if not ok}
        detected[m] = target in failed
        print(f"mutation {m:14s} target {target:5s} {'REJECTED' if detected[m] else 'MUTATION-MISSED'} (failing: {sorted(failed)})")
    MUT = set()
    run()
    for ok, cid, text in RESULTS:
        print(f"{'PASS' if ok else 'FAIL'} {cid}: {text}")
    nfail = sum(1 for ok, _, _ in RESULTS if not ok)
    print(f"checks: {len(RESULTS)}, failures: {nfail}, mutations rejected: {sum(detected.values())}/{len(MUTATIONS)}")
    if nfail == 0 and all(detected.values()):
        print("VERDICT PADDED-PAIR-OI-REALIZED-EXACT")
    else:
        print("VERDICT NOT-ESTABLISHED")
        sys.exit(1)


if __name__ == "__main__":
    main()
