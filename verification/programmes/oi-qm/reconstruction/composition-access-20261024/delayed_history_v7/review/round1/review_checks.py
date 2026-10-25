#!/usr/bin/env python3
"""Independent review checker for #912 delayed_history_v7 (separate engine).

Written from PLAN.md/REPORT.md, the Native A (native_x_v12) and history_v11
reports, and the composition_flag_v6 report; nothing is imported or copied from
the author's checks.py.  The only element reproduced from the author's code is
the background-generation recipe (xorshift seed schedule and box), which is
needed to land on the same three C0 families so that their c1/c2/c3 values can
be compared exactly.  A fourth family uses an unrelated background generator.

Standard library only; exact integers and Fractions.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from itertools import product
import json
import random
import sys


def need(ok, msg):
    if not ok:
        raise SystemExit('CHECK FAILED: ' + msg)


def l1(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


DIRS = []
for ax in range(3):
    for sg in (1, -1):
        e = [0, 0, 0]
        e[ax] = sg
        DIRS.append(tuple(e))
DIRS = tuple(DIRS)


def Hmap(v):
    a, b, d = (v >> 2) & 1, (v >> 1) & 1, v & 1
    return (b << 2) | (d << 1) | (a ^ (b & d))


HT = tuple(Hmap(v) for v in range(8))
need(sorted(HT) == list(range(8)), 'H is a permutation')
NTAB = {(0, 0): 5, (0, 1): 0, (1, 0): 4, (1, 1): 1}   # n(a,b)


# =====================================================================
# Part A: actual-L geometry
# =====================================================================

def actual():
    T = 185
    P = 12 * 840 ** 185
    S = P + T
    R = S + 68
    L = R + 9
    out = {}
    # history_v11 port table: port, deadline, axis, sign of frontier ray
    table = [((0, T, 0), T, 1, -1), ((0, 0, -8 * T), T, 2, -1),
             ((T, P, 0), S, 1, 1), ((-T, P, 0), S, 1, 1),
             ((4 * T, P, 0), S, 1, 1), ((0, S, 0), S, 1, 1),
             ((12 * R, 0, 0), R, 0, -1), ((48 * L, 0, 0), L, 0, 1)]
    q9 = (0, S, 77)
    # v6 read set: V=q9@L+2, the six previous neighbours @L+1, old q9 @L.
    carrier = [(q9, L + 2, 'q9@L+2'), (q9, L, 'q9@L')]
    names = {(0, 0, -1): 'q8', (0, 0, 1): 'q10', (-1, 0, 0): 'm',
             (1, 0, 0): 'q9+x', (0, -1, 0): 'q9-y', (0, 1, 0): 'q9+y'}
    for e in DIRS:
        carrier.append((plus(q9, e), L + 1, names[e] + '@L+1'))
    need(len(carrier) == 8, 'carrier count')
    # not read by v6; reported as a robustness margin only
    extra = [(q9, L + 1, 'q9@L+1 (unread)')]

    def ray(i, t):
        p, a, ax, sg = table[i]
        x = list(p)
        x[ax] += sg * t
        return tuple(x)

    def mind(i, x, lo, hi):
        p, a, ax, sg = table[i]
        tstar = sg * (x[ax] - p[ax])          # zero of the axial term
        tc = min(max(tstar, lo), hi)
        best = l1(ray(i, tc), x)
        # convexity cross-check on neighbours of the clamp and both endpoints
        for t in (lo, hi, tc - 1, tc + 1):
            if lo <= t <= hi:
                need(l1(ray(i, t), x) >= best, 'convex minimum')
        return best, tc

    H2 = 2 * L
    slacks, first = [], {}
    extra_slack = None
    for i in range(8):
        lo = max(table[i][1], L) + 1
        for x, tm, nm in carrier + extra:
            d, _ = mind(i, x, lo, H2)
            if nm.endswith('(unread)'):
                extra_slack = d - tm if extra_slack is None else min(extra_slack, d - tm)
                continue
            slacks.append(d - tm)
            site = nm.split('@')[0]
            first[site] = min(first.get(site, d), d)
    out['g1_pairs'] = len(slacks)
    out['g1_min_slack'] = min(slacks)
    out['g1_holds'] = min(slacks) > 0
    out['first_tail_arrival_minus_L'] = {k: v - L for k, v in sorted(first.items())}
    out['unread_q9_at_L+1_min_slack'] = extra_slack

    # tail chronology: a tail triple f_i(t) reaches no port before t > L, so
    # N_L (records at times <= L) is free of the tail bank.
    chron = []
    for i in range(8):
        lo = max(table[i][1], L) + 1
        for j in range(8):
            pj = table[j][0]
            p, a, ax, sg = table[i]
            # dist(ray(i,t),pj)-t is piecewise affine; check endpoints+breakpoint
            tstar = sg * (pj[ax] - p[ax])
            ts = {lo, H2} | ({tstar} if lo <= tstar <= H2 else set())
            chron.append(min(l1(ray(i, t), pj) - t for t in ts))
    out['tail_min_port_arrival_minus_own_time'] = min(chron)
    need(min(chron) >= 0, 'tail triple reaches a port before its own time')

    # G sources (Native A)
    G = {'F8': (-(L + 1), S, 76), 'F10': (-(L + 1), S, 78), 'F9': (-(L + 2), S, 77)}
    tri = {g: [l1(f, plus(q9, e)) - L for e in ((0, 0, -1), (0, 0, 1), (-1, 0, 0))]
           for g, f in G.items()}
    need(tri == {'F8': [1, 3, 1], 'F10': [3, 1, 1], 'F9': [3, 3, 1]}, 'Native A triangle')
    need(all(l1(f, q9) == L + 2 for f in G.values()), 'G to q9')
    need(all(l1(f, plus(q9, e)) == L + 3 for f in G.values()
             for e in ((1, 0, 0), (0, 1, 0), (0, -1, 0))), 'G to complement neighbours')
    offs = {g: sorted(l1(f, table[j][0]) - L for j in range(8)) for g, f in G.items()}
    out['g2_min_offsets'] = {g: o[0] for g, o in offs.items()}
    out['g2_three_smallest'] = {g: o[:3] for g, o in offs.items()}
    out['g2_holds'] = all(o[0] > 2 for o in offs.values())
    # G sources are not bank sites (any ray index a_i<t<=2L)
    for f in G.values():
        for i in range(8):
            p, a, ax, sg = table[i]
            if all(f[k] == p[k] for k in range(3) if k != ax):
                t = sg * (f[ax] - p[ax])
                need(not (a < t <= H2), 'G source coincides with a bank triple')
    out['G_sources_off_bank_rays'] = True

    out['g3_core_end_within_2L'] = L + 91 <= H2
    out['g3_dilation_end_within_2L'] = L + 361 <= H2
    out['g3_tail_bits'] = {'L+91': 8 * 3 * 91, 'L+361': 8 * 3 * 361}

    # pre-tail exposure, enumerated directly over the feasible t-interval
    hits = []
    for i in range(8):
        p, a, ax, sg = table[i]
        for x, tm, nm in carrier:
            rest = sum(abs(p[k] - x[k]) for k in range(3) if k != ax)
            room = tm - rest
            if room < 0:
                continue
            c = sg * (x[ax] - p[ax])       # |t - c| <= room
            lo, hi = max(c - room, a + 1), min(c + room, L)
            need(hi - lo < 10 ** 4, 'pre-tail window size')
            for t in range(lo, hi + 1):
                d = l1(ray(i, t), x)
                if d <= tm and (tm - d) % 2 == 0:
                    hits.append((i, t - a, nm, d == tm))
    out['pre_tail_hits'] = len(hits)
    out['pre_tail_ports'] = sorted({h[0] for h in hits})
    out['pre_tail_all_at_deadline_plus_2_first_arrival'] = all(h[1] == 2 and h[3] for h in hits)
    return out


# =====================================================================
# Part B: scaled exhaustive native control (own bit-sliced engine)
# =====================================================================

n, k = 3, 2
q9s = (0, 0, 0)
Q8s, Q10s, Ms = (0, 0, -1), (0, 0, 1), (-1, 0, 0)
NB = [plus(q9s, e) for e in DIRS]                  # six neighbours
REST = [x for x in NB if x not in (Q8s, Q10s, Ms)]
PORTs = (0, 0, -(k + 1))
DEAD = n - k - 1


def bank(t):
    return (PORTs[0], PORTs[1] + t, PORTs[2])


TAILT = (n + 3, n + 4, n + 5)
HOR = n + 5
SRCs = ((-(n + 1), 0, -1), (-(n + 1), 0, 1), (-(n + 2), 0, 0))   # F8, F10, F9
W = 1 << 18
FULL = (1 << W) - 1


def lanemask(bit):
    half = 1 << bit
    unit = ((1 << half) - 1) << half
    return unit * (FULL // ((1 << (2 * half)) - 1))


# my layout: tail triple i -> lane bits 3i..3i+2, G triple g -> 9+3g..
MASK = [lanemask(b) for b in range(18)]


def var_triple(base):
    # value = 4A+2B+D with D at bit base, B at base+1, A at base+2
    return (MASK[base + 2], MASK[base + 1], MASK[base])


def const_triple(v):
    return tuple(FULL if (v >> (2 - c)) & 1 else 0 for c in range(3))


def scaled_geometry_checks():
    for f in SRCs:
        need(l1(f, q9s) == n + 2, 'scaled G to q9')
    need([[l1(f, x) - n for x in (Q8s, Q10s, Ms)] for f in SRCs]
         == [[1, 3, 1], [3, 1, 1], [3, 3, 1]], 'scaled triangle')
    need([l1(f, PORTs) - n for f in SRCs] == [k + 1, k + 3, k + 3], 'scaled port offsets')
    car = [(q9s, n + 2), (q9s, n)] + [(x, n + 1) for x in NB]
    need(all(l1(bank(t), x) > tm for t in range(n + 1, HOR + 1) for x, tm in car),
         'scaled tail-window bank vs carrier')
    need(all(l1(bank(t), PORTs) == t for t in range(1, HOR + 1)), 'own front')
    return min(l1(bank(t), x) - tm for t in TAILT for x, tm in car)


OUTS = ([(PORTs, t) for t in range(0, HOR + 1)] + [(q9s, n), (q9s, n + 2)]
        + [(x, n + 1) for x in NB] + [(Q8s, HOR - 2), (Q8s, HOR)])


def closure(outs):
    req = defaultdict(set)
    stack = list(outs)
    seen = set()
    while stack:
        x, t = stack.pop()
        if (x, t) in seen:
            continue
        seen.add((x, t))
        req[t].add(x)
        if t >= 1:
            for e in DIRS:
                stack.append((plus(x, e), t - 1))
            stack.append((x, t - 2))
    return req


REQ = closure(OUTS)


def engine(prev, cur, overrides):
    """overrides: site -> planes for the enumerated current-slice triples."""
    fld = {}

    def val(x, t):
        if t == -1:
            return const_triple(prev.get(x, 0))
        if t == 0:
            if x in overrides:
                return overrides[x]
            return const_triple(cur.get(x, 0))
        return fld[x, t]

    for t in range(1, HOR + 1):
        for x in REQ.get(t, ()):
            sa = sb = sd = 0
            for e in DIRS:
                a, b, d = val(plus(x, e), t - 1)
                sa ^= a
                sb ^= b
                sd ^= d
            oa, ob, od = val(x, t - 2)
            fld[x, t] = (oa ^ sb, ob ^ sd, od ^ sa ^ (sb & sd))
    return {key: val(*key) for key in OUTS}


def decode(planes):
    strs = [format(p, '0%db' % W)[::-1] for p in planes]
    return [(a == '1') * 4 + (b == '1') * 2 + (c == '1') for a, b, c in zip(*strs)]


def scalar(prev, cur, assign):
    """Plain per-world sparse evaluation on the whole infinite lattice."""
    s = {-1: {x: v for x, v in prev.items() if v}, 0: {}}
    c0 = dict(cur)
    c0.update(assign)
    s[0] = {x: v for x, v in c0.items() if v}
    for t in range(1, HOR + 1):
        a, b = s[t - 2], s[t - 1]
        pts = set(a) | {plus(x, e) for x in b for e in DIRS}
        nxt = {}
        for x in pts:
            acc = 0
            for e in DIRS:
                acc ^= b.get(plus(x, e), 0)
            v = a.get(x, 0) ^ HT[acc]
            if v:
                nxt[x] = v
        s[t] = nxt
    return {(x, t): s[t].get(x, 0) for x, t in OUTS}


def lane_assign(lane):
    asg = {}
    for i, t in enumerate(TAILT):
        asg[bank(t)] = (lane >> (3 * i)) & 7
    for g, f in enumerate(SRCs):
        asg[f] = (lane >> (9 + 3 * g)) & 7
    return asg


def author_background(seed):
    # recipe needed to hit the author's C0 families (seeds 1, 2, 4)
    m = (1 << 64) - 1
    x = (seed * 0x9E3779B97F4A7C15 + 0x1234567) & m or 1

    def nxt():
        nonlocal x
        x ^= (x << 13) & m
        x ^= x >> 7
        x ^= (x << 17) & m
        return x
    prev, cur = {}, {}
    for a in range(-n - 4, 3):
        for b in range(-2, HOR + 4):
            for c in range(-k - 3, 4):
                prev[a, b, c] = nxt() & 7
                cur[a, b, c] = nxt() & 7
    return prev, cur


def my_background(seed):
    rnd = random.Random(seed)
    prev, cur = {}, {}
    for a in range(-n - 6, 5):
        for b in range(-5, HOR + 6):
            for c in range(-k - 6, 6):
                prev[a, b, c] = rnd.randrange(8)
                cur[a, b, c] = rnd.randrange(8)
    return prev, cur


def bit(v, c):          # c: 0=A, 1=B, 2=D
    return (v >> (2 - c)) & 1


def phase_map(V, q8, q10, m, others):
    """v6 phase map. Returns (s, J, A) with J=(X,Y,R,Z)."""
    s = bit(V, 1) ^ bit(q8, 2) ^ bit(q10, 2) ^ bit(m, 2)
    for o in others:
        s ^= bit(o, 2)
    Y, R, Z = bit(q8, 1), bit(q10, 2), bit(q10, 1)
    K = bit(q8, 0) + 2 * bit(q8, 2) + 4 * bit(q10, 0)
    A = int(K < NTAB[Y ^ s, R ^ s])
    return s, (s, Y, R, Z), A


def reference(s, others):
    """v6 reference law of (V, A, J) per fixed C0, built by enumeration:
    V uniform and independent of a uniform (Q8,Q10); count over 8*64=512."""
    ref = Counter()
    for q8, q10 in product(range(8), repeat=2):
        # A and J do not depend on M; choose M to give the requested s
        for V in range(8):
            Y, R, Z = bit(q8, 1), bit(q10, 2), bit(q10, 1)
            K = bit(q8, 0) + 2 * bit(q8, 2) + 4 * bit(q10, 0)
            A = int(K < NTAB[Y ^ s, R ^ s])
            ref[V, A, (s, Y, R, Z)] += 1
    # cross-check against the closed-form count_f(s,j)
    for (V, A, J), c in ref.items():
        nn = NTAB[J[1] ^ s, J[2] ^ s]
        need(c == (nn if A else 8 - nn) and J[0] == s, 'reference closed form')
    need(sum(ref.values()) == 512, 'reference mass')
    return ref


def tv_vs_ref(keys, ref):
    """TV of empirical law of keys=(w,V,A,J) from Pr(w) x ref/512."""
    nn = len(keys)
    act = Counter(keys)
    wm = Counter(kk[0] for kk in keys)
    tot = 0
    seen = set()
    for (w, V, A, J), c in act.items():
        r = wm[w] * ref.get((V, A, J), 0)
        tot += abs(512 * c - r)
        seen.add((w, V, A, J))
    for w, cw in wm.items():
        for (V, A, J), r in ref.items():
            if (w, V, A, J) not in seen:
                tot += cw * r
    return Fr(tot, 2 * 512 * nn)


def tv_product(xs, ys):
    nn = len(xs)
    j = Counter(zip(xs, ys))
    mx, my = Counter(xs), Counter(ys)
    tot = 0
    for a in mx:
        for b in my:
            tot += abs(nn * j.get((a, b), 0) - mx[a] * my[b])
    return Fr(tot, 2 * nn * nn)


def bloch(law):
    mass = sum(law.values())
    mx = Fr(sum(c * (1 - 2 * J[0]) for J, c in law.items()), mass)
    my = Fr(sum(c * (1 - 2 * J[1]) for J, c in law.items()), mass)
    mz = Fr(sum(c * (1 - 2 * J[3]) for J, c in law.items()), mass)
    return mass, mx, my, mz


def run_family(label, prev, cur, mode='normal'):
    prev = dict(prev)
    cur = dict(cur)
    for f in SRCs:
        cur.pop(f, None)
    for t in TAILT:
        cur.pop(bank(t), None)
    ov = {f: var_triple(9 + 3 * g) for g, f in enumerate(SRCs)}
    for i, t in enumerate(TAILT):
        ov[bank(t)] = var_triple(3 * i)
    if mode == 'dup':          # tail triple 1 := tail triple 0 over all lanes
        ov[bank(TAILT[1])] = var_triple(0)
    if mode == 'known_tail':   # tail bank pinned (C0 value 0)
        for t in TAILT:
            ov[bank(t)] = const_triple(0)
    o = engine(prev, cur, ov)
    vals = {key: decode(p) for key, p in o.items()}
    res = {'family': label, 'mode': mode}
    # scalar cross-check on sampled lanes
    rnd = random.Random(912)
    sample = [0, W - 1] + [rnd.randrange(W) for _ in range(14)]
    for lane in sample:
        asg = lane_assign(lane)
        if mode == 'dup':
            asg[bank(TAILT[1])] = asg[bank(TAILT[0])]
        if mode == 'known_tail':
            for t in TAILT:
                asg[bank(t)] = 0
        sc = scalar(prev, cur, asg)
        for key in OUTS:
            need(sc[key] == vals[key][lane], 'engine/scalar mismatch at %r' % (key,))
    res['scalar_lanes_agree'] = len(sample)
    pre_const = all(len(set(vals[PORTs, t])) == 1 for t in range(0, TAILT[0]))
    pset = set(vals[q9s, n])
    oth_const = all(len(set(vals[x, n + 1])) == 1 for x in REST)
    res['s1_pre_tail_ports_constant'] = pre_const
    res['old_q9_constant'] = len(pset) == 1
    res['rest_neighbours_constant'] = oth_const
    if mode == 'normal':
        need(pre_const and len(pset) == 1 and oth_const, 's1')
    p = vals[q9s, n][0]
    s_old = bit(p, 1)
    res['old_q9'] = p
    res['old_success'] = bit(p, 0) == 0
    others = [vals[x, n + 1][0] for x in REST]
    q8, q10, mm, V = vals[Q8s, n + 1], vals[Q10s, n + 1], vals[Ms, n + 1], vals[q9s, n + 2]
    w = [(a << 6) | (b << 3) | c for a, b, c in
         zip(vals[PORTs, TAILT[0]], vals[PORTs, TAILT[1]], vals[PORTs, TAILT[2]])]
    pool = [(a << 6) | (b << 3) | c for a, b, c in zip(q8, q10, mm)]
    res['s2_support'] = len(set(zip(pool, w)))
    ref = reference(s_old, others)
    keys = []
    sbad = 0
    for l in range(W):
        s, J, A = phase_map(V[l], q8[l], q10[l], mm[l], others)
        sbad += s != s_old
        keys.append((w[l], V[l], A, J))
    res['decoded_sign_mismatches'] = sbad
    act = Counter(keys)
    cells = 0
    mism = 0
    for wv in range(512):
        for (Vv, A, J) in product(range(8), range(2), product(range(2), repeat=4)):
            cells += 1
            if act.get((wv, Vv, A, J), 0) != ref.get((Vv, A, J), 0):
                mism += 1
    res['s3_cells'] = cells
    res['s3_mismatched_cells'] = mism
    res['s3_tv_fresh_tail'] = str(tv_vs_ref(keys, ref))
    if res['old_success'] and mode == 'normal':
        post = defaultdict(Counter)
        for (wv, Vv, A, J), c in act.items():
            if A:
                post[wv, Vv][J] += c
        ok = 0
        for law in post.values():
            mass, mx, my, mz = bloch(law)
            if mass == 20 and abs(mx) == 1 and my == 0 and mz == 0:
                ok += 1
        res['accepted_wv_records_pure_X'] = ok
        res['accepted_wv_records'] = len(post)
    if mode != 'normal':
        return res
    # c1: known tail, G varied
    by_tail = defaultdict(list)
    for l in range(W):
        by_tail[l & 0x1FF].append(l)
    c1 = []
    c1_distinct = set()
    negs = recs = 0
    mindet = None
    for tv_ in range(512):
        sub = by_tail[tv_]
        kk = [keys[l] for l in sub]
        c1.append(tv_vs_ref(kk, ref))
        c1_distinct.add(len({w[l] for l in sub}))
        if res['old_success']:
            post = defaultdict(Counter)
            for (wv, Vv, A, J) in kk:
                if A:
                    post[wv, Vv][J] += 1
            for law in post.values():
                mass, mx, my, mz = bloch(law)
                det = (1 - mx * mx - my * my - mz * mz) / 4
                mindet = det if mindet is None else min(mindet, det)
                negs += det < 0
                recs += 1
    res['c1_tv_min'] = str(min(c1))
    res['c1_tv_max'] = str(max(c1))
    res['c1_distinct_tail_records'] = sorted(c1_distinct)
    if res['old_success']:
        res['c1_min_det'] = str(mindet)
        res['c1_negative'] = negs
        res['c1_records'] = recs
    # c2: duplicated triple (t=n+4 equals t=n+3) inside the enumeration
    dup = [l for l in range(W) if (l >> 3) & 7 == l & 7]
    res['c2_tv'] = str(tv_vs_ref([keys[l] for l in dup], ref))
    res['c2_subset_size'] = len(dup)
    res['c2_subset_support'] = len({(pool[l], w[l]) for l in dup})
    # c3: native q8
    res['c3_tv_q8_at_horizon'] = str(tv_product(w, vals[Q8s, HOR]))
    res['c3_tv_q8_two_before'] = str(tv_product(w, vals[Q8s, HOR - 2]))
    return res


def main():
    out = {'actual': actual()}
    out['scaled_min_tail_carrier_slack'] = scaled_geometry_checks()
    fams = []
    for seed in (1, 2, 4):
        pv, cu = author_background(seed)
        fams.append(run_family('author-seed-%d' % seed, pv, cu))
    # unrelated background: first seed giving an old-success sector
    sd = 0
    while True:
        pv, cu = my_background(sd)
        # old-q9 probe via the scalar evaluator
        cc = {x: v for x, v in cu.items() if x not in SRCs and x not in map(bank, TAILT)}
        p = scalar(pv, cc, {})[(q9s, n)]
        if bit(p, 0) == 0:
            break
        sd += 1
    fams.append(run_family('own-random-%d' % sd, pv, cu))
    # detector controls on my own engine (must fire)
    pv, cu = author_background(1)
    fams.append(run_family('author-seed-1', pv, cu, mode='dup'))
    fams.append(run_family('author-seed-1', pv, cu, mode='known_tail'))
    out['families'] = fams
    normal = [f for f in fams if f['mode'] == 'normal']
    ctrl = [f for f in fams if f['mode'] != 'normal']
    out['detectors_fire'] = all(f['s2_support'] < W and Fr(f['s3_tv_fresh_tail']) > 0
                                for f in ctrl)
    out['scaled_ok'] = all(f['s2_support'] == W and f['s3_mismatched_cells'] == 0
                           and f['s3_tv_fresh_tail'] == '0'
                           and f['decoded_sign_mismatches'] == 0 for f in normal)
    a = out['actual']
    out['verdict'] = ('HOLDS_WITHIN_SCOPE' if a['g1_holds'] and a['g2_holds']
                      and a['g3_core_end_within_2L'] and a['g3_dilation_end_within_2L']
                      and out['scaled_ok'] and out['detectors_fire'] else 'NOT_REPRODUCED')
    print(json.dumps(out, indent=1, sort_keys=True))


if __name__ == '__main__':
    main()
