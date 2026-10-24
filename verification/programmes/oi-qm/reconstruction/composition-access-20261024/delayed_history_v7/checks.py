#!/usr/bin/env python3
"""Delayed eight-port public history jointly with the frozen v6 carrier.

Exact actual-L integer geometry plus a scaled exhaustive native control.
Standard library only; no author engine is imported.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
import hashlib
import json

# Triple encoding v=4A+2B+D. H(A,B,D)=(B,D,A XOR (B AND D)).
H = tuple(4*((v >> 1) & 1) + 2*(v & 1) + (((v >> 2) & 1) ^ ((v >> 1) & (v & 1) & 1))
          for v in range(8))
N = {(0, 0): 5, (0, 1): 0, (1, 0): 4, (1, 1): 1}
V6_PHASE_INPUT_BITS = 21           # composition_flag_v6 result.json, phase_input_bits
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def comp(v, i):
    """Component i of a triple: 0=A, 1=B, 2=D."""
    return (v >> (2-i)) & 1


def dist(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def target_count(s, accept, j):
    if j[0] != s:
        return 0
    n = N[j[1] ^ s, j[2] ^ s]
    return n if accept else 8-n


def determinant(law):
    mass = sum(law.values())
    need(mass > 0, 'empty posterior')
    means = [sum(F(n, mass)*(1-2*j[i]) for j, n in law.items()) for i in (0, 1, 3)]
    return (1-sum(m*m for m in means))/4


def tv(a, b):
    return sum((abs(a.get(k, F())-b.get(k, F())) for k in a.keys() | b.keys()), F())/2


# ---------------------------------------------------------------------------
# 1. Actual-L geometry (exact integers).

def actual_geometry():
    T = 185
    P = 12*840**185
    S = P+T
    R = S+68
    L = R+9
    need(L == P+262, 'L constant')
    H2 = 2*L
    q9 = (0, S, 77)
    ports = [(0, T, 0), (0, 0, -8*T), (T, P, 0), (-T, P, 0),
             (4*T, P, 0), (0, S, 0), (12*R, 0, 0), (48*L, 0, 0)]
    deadlines = [T, T, S, S, S, S, R, L]
    axes = [1, 2, 1, 1, 1, 1, 0, 0]
    signs = [-1, -1, 1, 1, 1, 1, -1, 1]
    neighbors = {'q8': (0, S, 76), 'q10': (0, S, 78), 'm': (-1, S, 77),
                 'q9+x': (1, S, 77), 'q9-y': (0, S-1, 77), 'q9+y': (0, S+1, 77)}
    carrier = [('q9', q9, L+2), ('q9', q9, L)]
    carrier += [(name, site, L+1) for name, site in neighbors.items()]
    # Post-plan control: the list must equal v6's read set, derived from q9
    # and the lattice steps: whole V at L+2, the six neighbours at L+1 and the
    # old q9 record at L (v6 phase wires: 7 triples = 21 bits).
    v6_read_set = {(q9, L+2), (q9, L)} | {(add(q9, st), L+1) for st in STEPS}
    carrier_read_set_ok = ({(site, time) for name, site, time in carrier} == v6_read_set
                           and len(carrier) == 8 and 3*(len(carrier)-1) == V6_PHASE_INPUT_BITS)
    sources = {'F8': (-(L+1), S, 76), 'F10': (-(L+1), S, 78), 'F9': (-(L+2), S, 77)}

    def frontier(i, t):
        a = list(ports[i])
        a[axes[i]] += signs[i]*t
        return tuple(a)

    def split(i, x):
        ax = axes[i]
        u0 = ports[i][ax]-x[ax]
        rest = sum(abs(ports[i][k]-x[k]) for k in range(3) if k != ax)
        return u0, rest

    def min_dist(i, x, lo, hi):
        # dist(frontier(i,t),x)=|u0+sign*t|+rest, convex piecewise affine in t.
        u0, rest = split(i, x)
        cands = {lo, hi}
        root = -u0*signs[i]
        if lo <= root <= hi:
            cands.add(root)
        values = [dist(frontier(i, t), x) for t in cands]
        need(all(v == abs(u0+signs[i]*t)+rest for v, t in zip(values, cands)),
             'distance decomposition')
        return min(values)

    # (g1) tail triples t in (max(a_i,L),2L] reach no carrier site-time.
    tail_slacks = []
    tail_rows = 0
    first_tail_arrival = {}
    for i in range(8):
        lo, hi = max(deadlines[i], L)+1, H2
        for name, site, time in carrier:
            md = min_dist(i, site, lo, hi)
            tail_slacks.append(md-time)
            tail_rows += 1
            first_tail_arrival[name] = min(first_tail_arrival.get(name, md), md)
    g1 = min(tail_slacks) > 0
    # (g2) G sources reach no port through L+2; recompute minimum offsets.
    g_offsets = {g: min(dist(f, p) for p in ports)-L for g, f in sources.items()}
    g_port_table = {g: sorted(dist(f, p)-L for p in ports)[:3] for g, f in sources.items()}
    g2 = all(off > 2 for off in g_offsets.values())
    need(g_offsets == {'F8': 77, 'F10': 79, 'F9': 79}, 'inherited public arrival offsets')
    # (g3) horizons covered by the history_v11 theorem.
    horizons = {'serial_core_end_offset': 91, 'serial_recorded_dilation_end_offset': 361}
    g3 = all(L+d <= H2 for d in horizons.values())
    # Pre-tail bank triples (a_i<t<=L) that do reach carrier site-times.
    pre_hits = []
    for i in range(8):
        lo, hi = deadlines[i]+1, L
        for name, site, time in carrier:
            u0, rest = split(i, site)
            room = time-rest
            if room < 0:
                continue
            # |u0+sign*t|<=room  <=>  sign*t in [-u0-room,-u0+room]
            a, b = -u0-room, -u0+room
            if signs[i] < 0:
                a, b = -b, -a
            a, b = max(a, lo), min(b, hi)
            for t in range(a, b+1) if b-a < 1000 else ():
                d = dist(frontier(i, t), site)
                if d <= time and (d-time) % 2 == 0:
                    pre_hits.append({'port': i, 't_minus_deadline': t-deadlines[i],
                                     'site': name, 'site_time_minus_L': time-L,
                                     'first_arrival': d == time})
            need(b-a < 1000, 'pre-tail interval unexpectedly large')
    pre_hits.sort(key=lambda r: (r['port'], r['t_minus_deadline'], r['site']))
    need(all(h['t_minus_deadline'] >= 1 for h in pre_hits), 'pre-tail index')
    return {
        'tail_bank': 'f_i(t), max(a_i,L)<t<=H, eight ports, 24 bits per tick',
        'carrier_site_times': len(carrier),
        'carrier_list_equals_v6_read_set': carrier_read_set_ok,
        'tail_carrier_family_pairs': tail_rows,
        'g1_min_tail_slack_over_carrier_site_times': min(tail_slacks),
        'g1_tail_reaches_no_carrier_site_time': g1,
        'g2_min_G_port_offsets_over_L': g_offsets,
        'g2_three_smallest_G_port_offsets_over_L': g_port_table,
        'g2_G_reaches_no_port_through_L_plus_2': g2,
        'g3_horizons_within_2L': g3,
        'tail_bits_for_horizon_offsets': {k: 24*d for k, d in horizons.items()},
        'first_tail_arrival_minus_L_at_carrier_sites': dict(sorted(
            (k, v-L) for k, v in first_tail_arrival.items())),
        'pre_tail_bank_reaching_carrier': pre_hits,
    }


# ---------------------------------------------------------------------------
# 2. Scaled exhaustive native control (bit-sliced over 2^18 worlds).

NS, KS = 3, 2                      # n in place of L, k in place of 76
DEAD = NS-KS-1                     # bank deadline, in place of S=L-77
HS = NS+KS+3                       # horizon: last first arrival of F10/F9
Q9 = (0, 0, 0)
Q8, Q10, MM = (0, 0, -1), (0, 0, 1), (-1, 0, 0)
OTHERS = ((1, 0, 0), (0, -1, 0), (0, 1, 0))
PHASE_NBRS = (Q8, Q10, MM) + OTHERS
PORT = (0, 0, -(KS+1))
SRC = ((-(NS+1), 0, -1), (-(NS+1), 0, 1), (-(NS+2), 0, 0))
TAIL = (NS+3, NS+4, NS+5)          # covers first G arrivals n+3 and n+5
LANES = 18
WORLDS = 1 << LANES
NBYTES = WORLDS // 8
FULL = (1 << WORLDS)-1


def bank_site(t):
    return (PORT[0], PORT[1]+t, PORT[2])


def scaled_geometry():
    need(DEAD >= 0, 'scaled deadline')
    off = [[dist(f, t)-NS for t in (Q8, Q10, MM)] for f in SRC]
    need(off == [[1, 3, 1], [3, 1, 1], [3, 3, 1]], 'scaled triangular geometry')
    need(all(dist(f, Q9) == NS+2 for f in SRC), 'scaled old-local exclusion')
    need(all(dist(f, o) == NS+3 for f in SRC for o in OTHERS), 'scaled complement exclusion')
    garr = [dist(f, PORT)-NS for f in SRC]
    need(garr == [KS+1, KS+3, KS+3], 'scaled public arrival offsets')
    need(min(dist(f, PORT) for f in SRC) == TAIL[0] and max(dist(f, PORT) for f in SRC) == TAIL[-1],
         'tail window covers first G arrivals')
    for t in range(DEAD+1, HS+4):
        need(dist(bank_site(t), PORT) == t, 'own axial first front')
    carrier = [(Q9, NS+2), (Q9, NS)] + [(x, NS+1) for x in PHASE_NBRS]
    need({x for x, tm in carrier if tm == NS+1} == {add(Q9, st) for st in STEPS},
         'scaled carrier read set')
    for t in TAIL + tuple(range(HS+1, HS+4)):
        need(all(dist(bank_site(t), x) > tm for x, tm in carrier), 'scaled tail reaches carrier')
    hits = [(t, x) for t in range(DEAD+1, TAIL[0]) for x, tm in carrier
            if dist(bank_site(t), x) <= tm and (dist(bank_site(t), x)-tm) % 2 == 0]
    need(hits, 'scaled pre-tail bank exposure absent')
    return {'n': NS, 'k': KS, 'bank_deadline': DEAD, 'horizon': HS,
            'port': list(PORT), 'G_port_offsets_over_n': garr,
            'tail_bank_times': list(TAIL),
            'pre_tail_bank_reaching_carrier': len(hits)}


def pattern(j):
    if j < 3:
        byte = (0xAA, 0xCC, 0xF0)[j]
        return int.from_bytes(bytes([byte])*NBYTES, 'little')
    sh = j-3
    return int.from_bytes(bytes(0xFF if (b >> sh) & 1 else 0 for b in range(NBYTES)), 'little')


PAT = [pattern(j) for j in range(LANES)]


def var_planes(base):
    return (PAT[base+2], PAT[base+1], PAT[base])


def const_planes(v):
    return tuple(FULL if comp(v, i) else 0 for i in range(3))


class Rng:
    def __init__(self, seed):
        self.x = (seed*0x9E3779B97F4A7C15+0x1234567) & ((1 << 64)-1) or 1

    def next(self):
        x = self.x
        x ^= (x << 13) & ((1 << 64)-1)
        x ^= x >> 7
        x ^= (x << 17) & ((1 << 64)-1)
        self.x = x
        return x


BOX = ((-NS-4, 2), (-2, HS+3), (-KS-3, 3))


def make_background(seed):
    """Dense dirty previous/current slices in a box; zero outside.

    Source cells carry G, tail bank cells carry enumerated triples; pre-tail
    and later bank cells carry fixed background values (part of C0).
    """
    rng = Rng(seed)
    prev, cur = {}, {}
    for x in range(BOX[0][0], BOX[0][1]+1):
        for y in range(BOX[1][0], BOX[1][1]+1):
            for z in range(BOX[2][0], BOX[2][1]+1):
                prev[x, y, z] = rng.next() & 7
                cur[x, y, z] = rng.next() & 7
    for f in SRC:
        cur.pop(f, None)
    for t in TAIL:
        cur.pop(bank_site(t), None)
    return prev, cur


TAIL_SITES = tuple(bank_site(t) for t in TAIL)


def initial_value(bg, slice_, x):
    """Bit planes of an initial field; G and the tail bank are enumerated."""
    prev, cur = bg
    if slice_ < 0:
        return const_planes(prev.get(x, 0))
    if x in SRC:
        return var_planes(3*SRC.index(x))
    if x in TAIL_SITES:
        return var_planes(9+3*TAIL_SITES.index(x))
    return const_planes(cur.get(x, 0))


OUTPUTS = ([(PORT, t) for t in range(0, HS+1)] + [(Q9, NS), (Q9, NS+2)]
           + [(x, NS+1) for x in PHASE_NBRS] + [(Q8, HS-2), (Q8, HS)])


def needed_sets():
    sets = {}
    for tau in range(1, HS+1):
        s = set()
        for y, ty in OUTPUTS:
            r = ty-tau
            if r < 0:
                continue
            for dx in range(-r, r+1):
                for dy in range(-(r-abs(dx)), r-abs(dx)+1):
                    rz = r-abs(dx)-abs(dy)
                    for dz in range(-rz, rz+1):
                        s.add((y[0]+dx, y[1]+dy, y[2]+dz))
        sets[tau] = s
    return sets


NEEDED = needed_sets()


def bitsliced(bg):
    fields = {}

    def get(tau, x):
        if tau <= 0:
            return initial_value(bg, tau, x)
        return fields[tau][x]

    for tau in range(1, HS+1):
        layer = {}
        for x in NEEDED[tau]:
            a = b = d = 0
            for st in STEPS:
                pa, pb, pd = get(tau-1, add(x, st))
                a ^= pa
                b ^= pb
                d ^= pd
            ha, hb, hd = b, d, a ^ (b & d)
            oa, ob, od = get(tau-2, x)
            layer[x] = (oa ^ ha, ob ^ hb, od ^ hd)
        fields[tau] = layer
    return lambda tau, x: get(tau, x)


def lanes_of(planes):
    """Per-world integer values of a triple from its three bit planes."""
    strs = [bin(p)[2:].zfill(WORLDS)[::-1] if p else '0'*WORLDS for p in planes]
    return [int(a+b+c, 2) for a, b, c in zip(*strs)]


def native_step(previous, current):
    pts = set(previous)
    for p in current:
        for st in STEPS:
            pts.add(add(p, st))
    out = {}
    for p in pts:
        x = 0
        for st in STEPS:
            x ^= current.get(add(p, st), 0)
        v = previous.get(p, 0) ^ H[x]
        if v:
            out[p] = v
    return out


def scalar_world(bg, lane):
    """Independent sparse evaluator on the full infinite lattice."""
    prev, cur = dict(bg[0]), dict(bg[1])
    for i, f in enumerate(SRC):
        cur[f] = (lane >> (3*i)) & 7
    for i, t in enumerate(TAIL):
        cur[bank_site(t)] = (lane >> (9+3*i)) & 7
    prev = {p: v for p, v in prev.items() if v}
    cur = {p: v for p, v in cur.items() if v}
    slices = {-1: prev, 0: cur}
    for tau in range(1, HS+1):
        slices[tau] = native_step(slices[tau-2], slices[tau-1])
    return {(y, ty): slices[ty].get(y, 0) for y, ty in OUTPUTS}


def old_q9(bg):
    prev = {p: v for p, v in bg[0].items() if v}
    cur = {p: v for p, v in bg[1].items() if v}
    # q9 at n does not depend on G or tail (distance >= n+2); use zeros there.
    slices = {-1: prev, 0: cur}
    for tau in range(1, NS+1):
        slices[tau] = native_step(slices[tau-2], slices[tau-1])
    return slices[NS].get(Q9, 0)


def choose_families():
    wanted = [('success', 0), ('success', 1), ('failure', None)]
    chosen = []
    seed = 1
    while wanted:
        bg = make_background(seed)
        p = old_q9(bg)
        for w in list(wanted):
            kind, s = w
            if kind == 'success' and comp(p, 0) == 0 and comp(p, 1) == s:
                chosen.append((seed, kind, p))
                wanted.remove(w)
                break
            if kind == 'failure' and comp(p, 0) == 1:
                chosen.append((seed, kind, p))
                wanted.remove(w)
                break
        seed += 1
        need(seed < 200, 'family search')
    return sorted(chosen)


def family(seed, kind, p_expected):
    bg = make_background(seed)
    get = bitsliced(bg)
    vals = {key: lanes_of(get(key[1], key[0])) for key in OUTPUTS}
    lanes = range(WORLDS)
    # (s1) pre-tail port records constant; p and complement constant.
    s1 = (all(len(set(vals[PORT, t])) == 1 for t in range(0, TAIL[0]))
          and set(vals[Q9, NS]) == {p_expected}
          and all(len(set(vals[o, NS+1])) == 1 for o in OTHERS))
    p = p_expected
    s_old = comp(p, 1)
    q8, q10, mm = vals[Q8, NS+1], vals[Q10, NS+1], vals[MM, NS+1]
    v_cur = vals[Q9, NS+2]
    others = [vals[o, NS+1][0] for o in OTHERS]
    w = [(a << 6) | (b << 3) | c for a, b, c in
         zip(vals[PORT, TAIL[0]], vals[PORT, TAIL[1]], vals[PORT, TAIL[2]])]
    pool = [(a << 6) | (b << 3) | c for a, b, c in zip(q8, q10, mm)]
    # (x2) seven-site inverse recovers old q9 in every world.
    cx = others[0] ^ others[1] ^ others[2]
    inv_ok = all(v_cur[l] ^ H[q8[l] ^ q10[l] ^ mm[l] ^ cx] == p for l in lanes)
    sign_mismatch = 0
    # Triangular Native A pool at fixed tail.
    fixed_tail = [l for l in lanes if l >> 9 == 0]
    need(len({pool[l] for l in fixed_tail}) == 512, 'triangular pool bijection')
    # (s2) joint pool/tail-record support.
    s2 = len(set(zip(pool, w))) == WORLDS
    # Phase map and predicate.
    sel, acc = [], []
    dbits = (others[0] & 1) ^ (others[1] & 1) ^ (others[2] & 1)
    for l in lanes:
        a8, a10, am = q8[l], q10[l], mm[l]
        s = comp(v_cur[l], 1) ^ comp(a8, 2) ^ comp(a10, 2) ^ comp(am, 2) ^ dbits
        sign_mismatch += int(s != s_old)
        j = (s, comp(a8, 1), comp(a10, 2), comp(a10, 1))
        k = comp(a8, 0)+2*comp(a8, 2)+4*comp(a10, 0)
        sel.append(j)
        acc.append(int(k < N[j[1] ^ s, j[2] ^ s]))
    counts = Counter(zip(w, v_cur, acc, sel))
    # (s3) complete public record: constants, tail record, V, pointer(A, pads).
    # The pads are fresh and enter only through the pointer prefix, so they
    # factor out by product; the cells compared below exclude them.
    s3_cells = 0
    s3 = True
    for rec, v, a in product(range(512), range(8), range(2)):
        for j in product(range(2), repeat=4):
            if counts.get((rec, v, a, j), 0) != target_count(s_old, a, j):
                s3 = False
            s3_cells += 1
    positive = 0
    if kind == 'success':
        for rec, v in product(range(512), range(8)):
            law = {j: counts[rec, v, 1, j] for j in product(range(2), repeat=4)
                   if counts.get((rec, v, 1, j), 0)}
            if sum(law.values()) == 20 and determinant(law) == 0 and all(j[0] == s_old for j in law):
                positive += 1
            else:
                s3 = False
    offered = 0 if kind == 'failure' else sum(acc)
    # (x1) independent scalar evaluator on sampled worlds.
    sample = [0, WORLDS-1] + [(l*0x9E37+seed*0x1F3) % WORLDS for l in range(1, 23)]
    scalar_mismatch = 0
    for l in sample:
        sc = scalar_world(bg, l)
        scalar_mismatch += sum(int(sc[key] != vals[key][l]) for key in OUTPUTS)
    # (x3)/(c2) duplicated tail triple: second tail triple equals the first.
    dup = [l for l in lanes if (l >> 12) & 7 == (l >> 9) & 7]
    dup_support = len({(pool[l], w[l]) for l in dup})
    def joint_tv(subset):
        # TV of the actual (record, V, A, J) law from Pr(record) x v6 reference,
        # in exact integers: sum over actual keys of |a-p|-p, plus total mass.
        n = len(subset)
        jt = Counter((w[l], v_cur[l], acc[l], sel[l]) for l in subset)
        wm = Counter(w[l] for l in subset)
        total = n*512
        acc_sum = total
        for (r, v, a, j), c in jt.items():
            pnum = wm[r]*target_count(s_old, a, j)
            acc_sum += abs(c*512-pnum)-pnum
        return F(acc_sum, 2*total), jt

    full_tv, _ = joint_tv(list(lanes))
    s3 = s3 and full_tv == 0
    dup_tv, _ = joint_tv(dup)
    # (x3) post-plan form: the s3 statistic must fire on the duplicated bank.
    x3_ok = dup_tv > 0
    # (c1) known tail: for each fixed tail value, vary only G.
    by_tail = defaultdict(list)
    for l in lanes:
        by_tail[l >> 9].append(l)
    c1_tvs, c1_distinct, c1_min_det, c1_neg, c1_records = [], [], F(), 0, 0
    for tval in range(512):
        sub = by_tail[tval]
        d, jt = joint_tv(sub)
        c1_tvs.append(d)
        c1_distinct.append(len({w[l] for l in sub}))
        if kind == 'success':
            post = defaultdict(Counter)
            for (r, v, a, j), c in jt.items():
                if a:
                    post[r, v][j] += c
            for law in post.values():
                det = determinant(law)
                c1_min_det = min(c1_min_det, det)
                c1_neg += int(det < 0)
                c1_records += 1
    # (c3) native continuation of the q8 field. At n+3 (same parity class as the
    # source fronts) it is a nonconstant (C0,G) function;
    # the first tail triple reaches it at n+5. The n+3 row was added after the
    # plan was published and is reported only.
    def dependence(field):
        jq = Counter(zip(w, field))
        mw, mq = Counter(w), Counter(field)
        return tv({k: F(c, WORLDS) for k, c in jq.items()},
                  {(a, b): F(mw[a]*mq[b], WORLDS*WORLDS) for a in mw for b in mq})

    q8late = vals[Q8, HS]
    c3_tv = dependence(q8late)
    c3_before_tv = dependence(vals[Q8, HS-2])
    need(len(set(vals[Q8, HS-2])) > 1, 'pre-arrival native q8 constant')
    digest = hashlib.sha256()
    for l in lanes:
        digest.update(bytes((pool[l] >> 1, pool[l] & 1, w[l] >> 1, w[l] & 1, v_cur[l], q8late[l])))
    return {
        'seed': seed, 'family': kind, 'old_q9': p, 'old_sign': s_old,
        'worlds': WORLDS,
        's1_pre_tail_records_constant': s1,
        's2_pool_tail_record_support': len(set(zip(pool, w))),
        's2_joint_bijective': s2,
        's3_cells_compared_including_zeros_pads_by_product': s3_cells,
        's3_complete_record_law_matches_v6': s3,
        's3_fresh_tail_record_carrier_tv': str(full_tv),
        'positive_accepted_records_pads_by_product': positive,
        'accepted_worlds_offered': offered,
        'x1_scalar_sampled_worlds': len(sample),
        'x1_scalar_mismatched_outputs': scalar_mismatch,
        'x1_pass': scalar_mismatch == 0,
        'x2_seven_site_inverse_worlds': WORLDS,
        'x2_pass': inv_ok and sign_mismatch == 0,
        'x3_duplicated_tail_support': dup_support,
        'x3_duplicated_tail_tv_positive': x3_ok,
        'c2_duplicated_tail_record_carrier_tv': str(dup_tv),
        'c1_known_tail_values': 512,
        'c1_max_distinct_tail_records_over_G': max(c1_distinct),
        'c1_min_distinct_tail_records_over_G': min(c1_distinct),
        'c1_max_record_carrier_tv': str(max(c1_tvs)),
        'c1_min_record_carrier_tv': str(min(c1_tvs)),
        'c1_tail_values_with_positive_tv': sum(1 for d in c1_tvs if d > 0),
        'c1_min_accepted_determinant': str(c1_min_det) if kind == 'success' else None,
        'c1_negative_accepted_records': c1_neg if kind == 'success' else None,
        'c1_accepted_records': c1_records if kind == 'success' else None,
        'c3_native_q8_at_horizon_tail_record_tv': str(c3_tv),
        'c3_native_q8_two_ticks_before_tail_arrival_tv': str(c3_before_tv),
        'world_table_sha256': digest.hexdigest(),
    }


def main():
    need(H == (0, 2, 4, 7, 1, 3, 5, 6), 'H table')
    geo = actual_geometry()
    sgeo = scaled_geometry()
    fams = [family(*f) for f in choose_families()]
    g_ok = (geo['g1_tail_reaches_no_carrier_site_time'] and
            geo['g2_G_reaches_no_port_through_L_plus_2'] and geo['g3_horizons_within_2L'])
    s_ok = all(f['s1_pre_tail_records_constant'] and f['s2_joint_bijective'] and
               f['s3_complete_record_law_matches_v6'] for f in fams)
    controls = {
        'x1_scalar_evaluator_agrees': all(f['x1_pass'] for f in fams),
        'x2_seven_site_inverse': all(f['x2_pass'] for f in fams),
        'x3_duplicated_tail_detected': all(f['x3_duplicated_tail_tv_positive'] for f in fams),
        'carrier_list_equals_v6_read_set': geo['carrier_list_equals_v6_read_set'],
    }
    controls_ok = all(controls.values())
    if not controls_ok:
        verdict = 'VOID'
    else:
        verdict = 'HOLDS_WITHIN_SCOPE' if g_ok and s_ok else 'NEGATIVE_FOR_CONSTRUCTION'
    bank_load_bearing = any(F(f['c1_max_record_carrier_tv']) > 0 for f in fams)
    storage_load_bearing = any(F(f['c3_native_q8_at_horizon_tail_record_tv']) > 0 for f in fams)
    result = {
        'schema': 'oi-delayed-port-history-frozen-carrier-v7.2',
        'scope': ('frozen logical v6 carrier; eight old ports with the supplied '
                  'history_v11 bank through H<=2L; Native A source contract'),
        'verdict': verdict,
        'actual_geometry': geo,
        'scaled_geometry': sgeo,
        'scaled_families': fams,
        'known_tail_countercontrol_shows_bank_load_bearing': bank_load_bearing,
        'native_continuation_shows_frozen_storage_load_bearing': storage_load_bearing,
        'actual_astronomical_time_simulated': False,
        'native_storage_or_compilation_established': False,
        'observer_access_rule_adopted': False,
        'required_controls': controls,
        'all_required_controls_pass': controls_ok,
        'post_plan_rows': [
            'x3 criterion: duplicated-tail record/carrier TV > 0 (support count kept, reported only)',
            'carrier_list_equals_v6_read_set control',
            'all_required_controls_pass computed from required_controls; VOID otherwise',
            's3 and positive-record counts exclude the pad factor',
            's1 recorded as a criterion rather than an exception',
            'c1_accepted_records denominator, reported only',
            'c3 native q8 row at n+3, reported only',
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not controls_ok:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
