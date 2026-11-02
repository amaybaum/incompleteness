#!/usr/bin/env python3
"""Independent re-enumeration of BH-01 counts (reviewer's own code; imports nothing from checks.py).

Encoding: a configuration of {0,1}^3 is an int x in 0..7, register r = bit r of x.
Distributions are exact (Fraction); records are tuples of read bits.
"""
import itertools
from collections import Counter, defaultdict
from fractions import Fraction as Fr

bit = lambda x, r: (x >> r) & 1


def record_dist(perm_seq, init_points, reads):
    """reads[t] = registers read at time t (cumulative record up to the last t).
    perm_seq[t-1] maps x_{t-1} -> x_t. Returns Counter over full cumulative records."""
    c = Counter()
    for x0 in init_points:
        x = x0
        rec = [tuple(bit(x, r) for r in reads[0])]
        for t in range(1, len(reads)):
            x = perm_seq[t - 1][x]
            rec.append(tuple(bit(x, r) for r in reads[t]))
        c[tuple(rec)] += 1
    return c


def psucc(dists):
    """dists: list of Counters, one per message, each over N equally weighted points."""
    N = sum(dists[0].values())
    keys = set().union(*dists)
    return Fr(sum(max(d[k] for d in dists) for k in keys), N * len(dists))


def tv(d0, d1):
    N = sum(d0.values())
    keys = set(d0) | set(d1)
    return Fr(sum(abs(d0[k] - d1[k]) for k in keys), 2 * N)


perms = list(itertools.permutations(range(8)))
assert_count = len(perms)
print("S8 size", assert_count, len(set(perms)))

# --- MP1: message bit 0; bits 1,2 hidden uniform; reads (),(2),(1,2) cumulative, homogeneous p.
sup = {m: [x for x in range(8) if bit(x, 0) == m] for m in (0, 1)}
hist = Counter()
exact_t2 = 0
for p in perms:
    d = [record_dist([p, p], sup[m], [(), (2,), (1, 2)]) for m in (0, 1)]
    hist[tv(*d)] += 1
print("MP1 t=2 TV histogram", {str(k): v for k, v in sorted(hist.items())})

# --- Snapshot-only variant at t=2 (reads only the endpoint (1,2)) for comparison
hist_s = Counter()
for p in perms:
    p2 = [p[p[x]] for x in range(8)]
    d = [Counter((bit(p2[x], 1), bit(p2[x], 2)) for x in sup[m]) for m in (0, 1)]
    hist_s[tv(*d)] += 1
print("MP1 t=2 endpoint-snapshot-only TV histogram", {str(k): v for k, v in sorted(hist_s.items())})

# --- MP2: message bits 0,1 (|M|=4), bit 2 hidden; P_succ at t=2 (cumulative reads (),(2),(1,2)).
sup2 = {m: [x for x in range(8) if (x & 3) == m] for m in range(4)}
h2 = Counter()
for p in perms:
    d = [record_dist([p, p], sup2[m], [(), (2,), (1, 2)]) for m in range(4)]
    h2[psucc(d)] += 1
print("MP2 t=2 P_succ histogram", {str(k): v for k, v in sorted(h2.items())})

# --- Nested: V=bit0 blank(0), B=bit1 message, D=bit2 hidden. V read at t=1..3.
supn = {m: [(m << 1) | (dd << 2) for dd in (0, 1)] for m in (0, 1)}
hn = Counter()
rec_W = Counter()
waut = 0
prod = 0
waut_fail = 0
for p in perms:
    d = [record_dist([p, p, p], supn[m], [(), (0,), (0,), (0,)]) for m in (0, 1)]
    hn[tv(*d)] += 1
    dW = [record_dist([p, p, p], supn[m], [(), (0,), (0,), (0, 1)]) for m in (0, 1)]
    ok = psucc(dW) == 1
    rec_W[ok] += 1
    # W-autonomy: W-part (bits 0,1) of p(x) depends only on W-part of x
    wa = all((p[x] & 3) == (p[x ^ 4] & 3) for x in range(4))
    if wa:
        waut += 1
        if not ok:
            waut_fail += 1
        # product: also D-part of p(x) depends only on D-part of x
        if all(((p[x] >> 2) == (p[y] >> 2)) for x in range(8) for y in range(8) if (x >> 2) == (y >> 2)):
            prod += 1
print("nested t=3 TV histogram", {str(k): v for k, v in sorted(hn.items())})
print("nested W-endpoint exact recovery True/False", rec_W[True], rec_W[False])
print("W-autonomous", waut, "products", prod, "W-autonomous failing", waut_fail)

# --- Snapshot D2: reads (),(2),(2),(2) snapshot, count with some decrease in TV.
dec = 0
for p in perms:
    tvs = []
    for t in range(4):
        pt = list(range(8))
        for _ in range(t):
            pt = [p[y] for y in pt]
        if t == 0:
            tvs.append(Fr(0))
            continue
        dd = [Counter(bit(pt[x], 2) for x in sup[m]) for m in (0, 1)]
        tvs.append(tv(*dd))
    if any(tvs[i + 1] < tvs[i] for i in range(3)):
        dec += 1
print("snapshot decreasing", dec)

# --- All 256 maps on {0,1}^2 (bit0 = B message, bit1 = R).
maps = list(itertools.product(range(4), repeat=4))
am1 = Counter()
am2_viol_bij = 0
am2_viol = []
for F in maps:
    bij = len(set(F)) == 4
    # AM1: message bit0, R hidden uniform, full read at t=1
    im0 = {F[x] for x in (0, 2)}
    im1 = {F[x] for x in (1, 3)}
    am1[(bij, not (im0 & im1))] += 1
    # AM2: message = whole config (|M| = 4, N = 1), read bit1 at t=1
    ps = Fr(len({bit(F[x], 1) for x in range(4)}), 4)
    if ps < Fr(1, 2):
        if bij:
            am2_viol_bij += 1
        am2_viol.append(F)
print("AM1 (bij,recover) counts", dict(am1))
const_read = [F for F in maps if len({bit(F[x], 1) for x in range(4)}) == 1]
print("AM2 violations", len(am2_viol), "bijective among them", am2_viol_bij,
      "== maps with read register constant:", set(am2_viol) == set(const_read), len(const_read))

# --- GL(4,2) via rank formula only (independent of enumeration): r_t = t - rank(C_t)


def rank2(vs):
    piv = {}  # highest bit -> basis vector
    for v in vs:
        while v:
            h = v.bit_length() - 1
            if h in piv:
                v ^= piv[h]
            else:
                piv[h] = v
                break
    return len(piv)


mats = [rows for rows in itertools.product(range(1, 16), repeat=4) if rank2(rows) == 4]
print("GL(4,2)", len(mats))
for k in (1, 2):
    prof = Counter()
    hm = 15 ^ ((1 << k) - 1)
    for rows in mats:
        prof[tuple(t - rank2([r & hm for r in rows[:t]]) for t in range(5))] += 1
    print("k=%d profiles" % k, dict(sorted(prof.items())))
