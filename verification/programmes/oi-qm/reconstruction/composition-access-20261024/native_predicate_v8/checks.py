#!/usr/bin/env python3
"""Passive native readout as the v6 acceptance predicate.

Exact actual-L tail-free geometry for a radius-4 readout region, and an exact
search, in a scaled dirty-background native control, over every set R of whole
native triples for a record (V, w_R) carrying v6's complete law with some
predicate. Standard library only; no author engine is imported; no repository
file is read.
"""
from collections import Counter
from itertools import product
import hashlib
import json
import sys

# Triple encoding v=4A+2B+D. H(A,B,D)=(B,D,A XOR (B AND D)).
H = tuple(4*((v >> 1) & 1) + 2*(v & 1) + (((v >> 2) & 1) ^ ((v >> 1) & (v & 1) & 1))
          for v in range(8))
N = {(0, 0): 5, (0, 1): 0, (1, 0): 4, (1, 1): 1}       # v6 thresholds
N_BAD = {(0, 0): 5, (0, 1): 4, (1, 0): 0, (1, 1): 1}   # x4: permuted thresholds
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
# delayed_history_v7 result.json, first_tail_arrival_minus_L_at_carrier_sites.
V7_FIRST_TAIL = {'m': 77, 'q10': 79, 'q8': 77, 'q9': 78, 'q9+x': 77, 'q9+y': 77, 'q9-y': 79}

PARTITION_CHOICE_CAP = 10**5
COMMON_CANDIDATE_CAP = 24


class Void(Exception):
    pass


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def control(ok, name):
    if not ok:
        raise Void(name)


def comp(v, i):
    """Component i of a triple: 0=A, 1=B, 2=D."""
    return (v >> (2-i)) & 1


def dist(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def ball(r):
    out = []
    for x in range(-r, r+1):
        for y in range(-(r-abs(x)), r-abs(x)+1):
            rz = r-abs(x)-abs(y)
            for z in range(-rz, rz+1):
                out.append((x, y, z))
    return out


# ---------------------------------------------------------------------------
# Scaled geometry constants.

NS = 6                          # n in place of L
RHO = 4                         # readout region radius
TAU = 16                        # tau_max
TEND = NS+1+TAU                 # last read slice
R0 = RHO+TEND                   # dirty initial radius: every read cone
Q9 = (0, 0, 0)
Q8, Q10, MM = (0, 0, -1), (0, 0, 1), (-1, 0, 0)
OTHERS = ((1, 0, 0), (0, -1, 0), (0, 1, 0))
SRC = ((-(NS+1), 0, -1), (-(NS+1), 0, 1), (-(NS+2), 0, 0))
REGION = sorted(ball(RHO))
SLICES = tuple(range(-1, TEND+1))
SITE_TIMES = [(x, t) for t in SLICES for x in REGION]
LANES = 9
WORLDS = 1 << LANES
FULL = (1 << WORLDS)-1
SUCCESS_PER_SIGN = 8


# ---------------------------------------------------------------------------
# 1. Actual-L geometry (exact integers), ports and bank as in delayed_history_v7.

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
    sources = [(-(L+1), S, 76), (-(L+1), S, 78), (-(L+2), S, 77)]
    named = {'q8': (0, 0, -1), 'q10': (0, 0, 1), 'm': (-1, 0, 0), 'q9': (0, 0, 0),
             'q9+x': (1, 0, 0), 'q9-y': (0, -1, 0), 'q9+y': (0, 1, 0)}

    def frontier(i, t):
        a = list(ports[i])
        a[axes[i]] += signs[i]*t
        return tuple(a)

    def first_tail(x):
        site = add(q9, x)
        best = None
        for i in range(8):
            lo, hi = max(deadlines[i], L)+1, H2
            ax = axes[i]
            u0 = ports[i][ax]-site[ax]
            rest = sum(abs(ports[i][k]-site[k]) for k in range(3) if k != ax)
            cands = {lo, hi}
            root = -u0*signs[i]
            if lo <= root <= hi:
                cands.add(root)
            vals = [dist(frontier(i, t), site) for t in cands]
            need(all(v == abs(u0+signs[i]*t)+rest for v, t in zip(vals, cands)),
                 'distance decomposition')
            m = min(vals)
            best = m if best is None else min(best, m)
        return best-L

    carrier_first = {k: first_tail(x) for k, x in named.items()}
    region_free = {x: first_tail(x) for x in REGION}
    region_g = {x: min(dist(f, add(q9, x)) for f in sources)-L for x in REGION}
    return {'carrier_first_tail_minus_L': dict(sorted(carrier_first.items())),
            'region_first_tail_minus_L': region_free,
            'region_first_G_minus_L': region_g}


# ---------------------------------------------------------------------------
# 2. Scaled native control: bit-sliced over the 512 G values.

PAT = [sum(1 << l for l in range(WORLDS) if (l >> j) & 1) for j in range(LANES)]


def var_planes(base):
    # Triple bits A,B,D of source i are lane bits 3i+2, 3i+1, 3i.
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


INITIAL_CELLS = sorted(ball(R0))


def make_background(seed):
    """Dirty previous/current initial slices on the ball of radius R0."""
    if seed == 0:
        return {}, {}
    rng = Rng(seed)
    prev, cur = {}, {}
    for c in INITIAL_CELLS:
        prev[c] = rng.next() & 7
        cur[c] = rng.next() & 7
    for f in SRC:
        cur.pop(f, None)
    return prev, cur


def bitsliced(bg):
    prev, cur = bg
    fields = {-1: {c: const_planes(prev.get(c, 0)) for c in INITIAL_CELLS},
              0: {}}
    for c in INITIAL_CELLS:
        fields[0][c] = var_planes(3*SRC.index(c)) if c in SRC else const_planes(cur.get(c, 0))
    for t in range(1, TEND+1):
        layer = {}
        p1, p2 = fields[t-1], fields[t-2]
        for x in ball(RHO+TEND-t):
            a = b = d = 0
            for st in STEPS:
                pa, pb, pd = p1[(x[0]+st[0], x[1]+st[1], x[2]+st[2])]
                a ^= pa
                b ^= pb
                d ^= pd
            ha, hb, hd = b, d, a ^ (b & d)
            oa, ob, od = p2[x]
            layer[x] = (oa ^ ha, ob ^ hb, od ^ hd)
        fields[t] = layer
    return fields


def lanes_of(planes):
    strs = [bin(p)[2:].zfill(WORLDS)[::-1] if p else '0'*WORLDS for p in planes]
    return tuple(4*(a == '1')+2*(b == '1')+(c == '1') for a, b, c in zip(*strs))


def scalar_world(bg, lane):
    """Independent per-world evaluator: scalar triples, explicit Boolean H."""
    prev, cur = dict(bg[0]), dict(bg[1])
    for i, f in enumerate(SRC):
        cur[f] = (lane >> (3*i)) & 7

    def h(v):
        a, b, d = (v >> 2) & 1, (v >> 1) & 1, v & 1
        return (b << 2) | (d << 1) | (a ^ (b & d))

    slices = {-1: prev, 0: cur}
    for t in range(1, TEND+1):
        r = RHO+TEND-t
        out = {}
        for x in range(-r, r+1):
            for y in range(-(r-abs(x)), r-abs(x)+1):
                rz = r-abs(x)-abs(y)
                for z in range(-rz, rz+1):
                    s = 0
                    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0),
                                       (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                        s ^= slices[t-1].get((x+dx, y+dy, z+dz), 0)
                    out[x, y, z] = slices[t-2].get((x, y, z), 0) ^ h(s)
        slices[t] = out
    return {(x, t): slices[t].get(x, 0) for x, t in SITE_TIMES}


def old_q9_scalar(bg):
    prev, cur = bg
    slices = {-1: prev, 0: cur}
    for t in range(1, NS+1):
        out = {}
        for x in ball(NS-t):
            s = 0
            for st in STEPS:
                s ^= slices[t-1].get(add(x, st), 0)
            out[x] = slices[t-2].get(x, 0) ^ H[s]
        slices[t] = out
    return slices[NS][Q9]


def choose_families():
    chosen, counts, seed = [], {0: 0, 1: 0}, 1
    while counts[0] < SUCCESS_PER_SIGN or counts[1] < SUCCESS_PER_SIGN:
        p = old_q9_scalar(make_background(seed))
        s = comp(p, 1)
        if comp(p, 0) == 0 and counts[s] < SUCCESS_PER_SIGN:
            chosen.append(seed)
            counts[s] += 1
        seed += 1
        need(seed < 400, 'family search')
    return chosen


# ---------------------------------------------------------------------------
# 3. The cell law and the exact search.

def j_index(y, r, z):
    return 4*y+2*r+z


def targets(s, n=N):
    t1 = tuple(n[y ^ s, r ^ s] for y, r, z in product(range(2), repeat=3))
    return t1, tuple(8-c for c in t1)


def proportional(counts, target):
    tot, tt = sum(counts), sum(target)
    return tot > 0 and all(c*tt == t*tot for c, t in zip(counts, target))


def canonical(labels):
    seen = {}
    return tuple(seen.setdefault(x, len(seen)) for x in labels)


class Family:
    """Native data of one background: pool, V, carrier, per-v partitions."""

    def __init__(self, seed, inject=None):
        self.seed = seed
        bg = make_background(seed)
        self.bg = bg
        fields = bitsliced(bg)
        self.vals = {(x, t): lanes_of(fields[t][x]) for x, t in SITE_TIMES}
        p = set(self.vals[Q9, NS])
        control(len(p) == 1, 'x2_old_q9_constant')
        self.p = p.pop()
        self.s = comp(self.p, 1)
        q8, q10, mm = self.vals[Q8, NS+1], self.vals[Q10, NS+1], self.vals[MM, NS+1]
        self.V = self.vals[Q9, NS+2]
        oth = [self.vals[o, NS+1] for o in OTHERS]
        control(all(len(set(o)) == 1 for o in oth), 'x2_other_neighbours_constant')
        cx = oth[0][0] ^ oth[1][0] ^ oth[2][0]
        lanes = range(WORLDS)
        control(len({(q8[l], q10[l], mm[l]) for l in lanes}) == WORLDS, 'x2_pool_bijection')
        control(all(self.V[l] ^ H[q8[l] ^ q10[l] ^ mm[l] ^ cx] == self.p for l in lanes),
                'x2_seven_site_inverse')
        dbits = (cx & 1)
        control(all(comp(self.V[l], 1) ^ comp(q8[l], 2) ^ comp(q10[l], 2) ^ comp(mm[l], 2)
                    ^ dbits == self.s for l in lanes), 'x2_phase_sign')
        self.Y = tuple(comp(q8[l], 1) for l in lanes)
        self.R = tuple(comp(q10[l], 2) for l in lanes)
        self.Z = tuple(comp(q10[l], 1) for l in lanes)
        self.K = tuple(comp(q8[l], 0)+2*comp(q8[l], 2)+4*comp(q10[l], 0) for l in lanes)
        self.J = tuple(j_index(self.Y[l], self.R[l], self.Z[l]) for l in lanes)

        def pred(n):
            return tuple(int(self.K[l] < n[self.Y[l] ^ self.s, self.R[l] ^ self.s])
                         for l in lanes)
        self.A = pred(N)
        self.A_bad = pred(N_BAD)
        self.t1, self.t0 = targets(self.s)
        self.byv = {v: tuple(l for l in lanes if self.V[l] == v) for v in range(8)}
        control(all(len(self.byv[v]) == 64 for v in range(8)), 'x2_V_uniform')
        if inject is not None:
            self.vals[inject] = tuple(2*a for a in self.A)
        self.parts = {}
        for key, w in self.vals.items():
            if key in SITE_TIMES_SET:
                self.parts[key] = self.partitions(w)

    def partitions(self, w):
        return tuple(canonical([w[l] for l in self.byv[v]]) for v in range(8))

    def law_of(self, v, part):
        """Two-block partition of the V=v worlds: (accept block label) or None."""
        lanes = self.byv[v]
        blocks = {}
        for l, b in zip(lanes, part):
            blocks.setdefault(b, [0]*8)[self.J[l]] += 1
        if len(blocks) != 2:
            return None
        c0, c1 = tuple(blocks[0]), tuple(blocks[1])
        if c0 == self.t1 and c1 == self.t0:
            return 0
        if c1 == self.t1 and c0 == self.t0:
            return 1
        return None

    def planted(self):
        lanes = range(WORLDS)
        return {
            ('P', 'A'): tuple(2*self.A[l] for l in lanes),
            ('P', 'A_xor_VB'): tuple(2*(self.A[l] ^ comp(self.V[l], 1)) for l in lanes),
            ('P', 'A_other_code'): tuple(5+2*self.A[l] for l in lanes),
            ('P', 'A_Y_leak'): tuple(4*self.A[l]+2*self.Y[l] for l in lanes),
            ('P', 'A_permuted_n'): tuple(2*self.A_bad[l] for l in lanes),
            ('P', 'Z_only'): tuple(2*self.Z[l] for l in lanes),
        }


SITE_TIMES_SET = set(SITE_TIMES)


def is_trivial(pv):
    return not any(pv)


def two_block(pv):
    return max(pv) == 1


def passes_reduction(fam, parts_list):
    """Reduction rule for one family: R passes iff for every v all nontrivial
    member partitions are one and the same law-good two-block partition."""
    for v in range(8):
        nontriv = {p[v] for p in parts_list if not is_trivial(p[v])}
        if len(nontriv) != 1:
            return False
        pv = nontriv.pop()
        if not two_block(pv) or fam.law_of(v, pv) is None:
            return False
    return True


def passes_direct(fam, w_list):
    """Direct check: join classes of (V, w_R), each proportional to a target."""
    classes = {}
    for l in range(WORLDS):
        key = (fam.V[l],)+tuple(w[l] for w in w_list)
        classes.setdefault(key, [0]*8)[fam.J[l]] += 1
    return all(proportional(c, fam.t1) or proportional(c, fam.t0) for c in classes.values())


def family_search(fam, parts):
    """Exact existence of an admissible R among the given cells, one family."""
    cand = {k: p for k, p in parts.items()
            if all(is_trivial(pv) or two_block(pv) for pv in p)}
    good = []
    for v in range(8):
        gv = sorted({p[v] for p in cand.values()
                     if not is_trivial(p[v]) and fam.law_of(v, p[v]) is not None})
        good.append(gv)
    sizes = [len(g) for g in good]
    choices = 1
    for n in sizes:
        choices *= n
    if choices > PARTITION_CHOICE_CAP:
        return {'undecided': True, 'good_partitions_per_v': sizes}
    # Cells trivial for every v never cover and never conflict: they may be
    # added to any admissible R, which is reported by its nontrivial cells.
    split = {k: p for k, p in cand.items() if not all(is_trivial(pv) for pv in p)}
    admissible = []
    if choices:
        for pick in product(*good):
            allowed = sorted((k for k, p in split.items()
                              if all(is_trivial(p[v]) or p[v] == pick[v] for v in range(8))), key=repr)
            if all(any(parts[k][v] == pick[v] for k in allowed) for v in range(8)):
                admissible.append(allowed)
    return {'undecided': False, 'two_block_or_trivial_cells': len(cand),
            'good_partitions_per_v': sizes, 'admissible_R': admissible}


def common_search(fams, parts_by_fam, items):
    """Exact search for a conflict-free union of items (streams), common to all
    families, covering every (family, v), with a consistent accept map."""
    def ok_cell(k):
        for f, fam in enumerate(fams):
            p = parts_by_fam[f].get(k)
            if p is None:
                return False
            for v in range(8):
                if not is_trivial(p[v]) and (not two_block(p[v]) or fam.law_of(v, p[v]) is None):
                    return False
        return True

    all_cells = set()
    for its in items.values():
        all_cells.update(its)
    good_cells = {k for k in all_cells if ok_cell(k)}
    nodes = sorted((i for i, its in items.items() if all(k in good_cells for k in its)), key=repr)
    nodes = [i for i in nodes if any(not is_trivial(parts_by_fam[f][k][v])
                                     for k in items[i] for f in range(len(fams))
                                     for v in range(8))]
    if len(nodes) > COMMON_CANDIDATE_CAP:
        return {'undecided': True, 'candidates': len(nodes)}

    def compatible(a, b):
        for f in range(len(fams)):
            for v in range(8):
                ps = {parts_by_fam[f][k][v] for k in items[a]+items[b]
                      if not is_trivial(parts_by_fam[f][k][v])}
                if len(ps) > 1:
                    return False
        return True

    adj = {a: {b for b in nodes if b != a and compatible(a, b)} for a in nodes}
    cliques = []

    def bk(r, p, x):
        if not p and not x:
            cliques.append(sorted(r, key=repr))
            return
        for u in sorted(p, key=repr):
            bk(r | {u}, p & adj[u], x & adj[u])
            p = p - {u}
            x = x | {u}
    bk(set(), set(nodes), set())
    found = []
    for cl in cliques:
        if not cl:
            continue
        cells = sorted({k for i in cl for k in items[i]}, key=repr)
        if not all(passes_reduction(fams[f], [parts_by_fam[f][k] for k in cells])
                   for f in range(len(fams))):
            continue
        amap, consistent = {}, True
        for f, fam in enumerate(fams):
            ws = [fam.vals_all[k] for k in cells]
            for l in range(WORLDS):
                key = (fam.p, fam.V[l])+tuple(w[l] for w in ws)
                a = acc_of(fam, cells, parts_by_fam[f], l)
                if amap.setdefault(key, a) != a:
                    consistent = False
        if consistent:
            found.append(cells)
    return {'undecided': False, 'candidates': len(nodes), 'admissible_common_R': found}


def acc_of(fam, cells, parts, lane):
    v = fam.V[lane]
    idx = fam.byv[v].index(lane)
    for k in cells:
        pv = parts[k][v]
        if not is_trivial(pv):
            return int(pv[idx] == fam.law_of(v, pv))
    raise RuntimeError('uncovered lane')


def streams(keys):
    """Stream-closed items: site x read at every slice from -1 through t."""
    items = {}
    for x, t in keys:
        items[('S', x, t)] = [(x, u) for u in range(-1, t+1)]
    return items


# ---------------------------------------------------------------------------

def histogram(fam):
    h = Counter(max(max(pv)+1 for pv in fam.parts[k]) for k in SITE_TIMES)
    return {str(b): h[b] for b in sorted(h)}


def diagnostics(fam):
    heralded = a_function = 0
    for k in SITE_TIMES:
        w = fam.vals[k]
        classes, amap, afun = {}, {}, True
        for l in range(WORLDS):
            key = (fam.V[l], w[l])
            classes.setdefault(key, [0]*8)[fam.J[l]] += 1
            if amap.setdefault(key, fam.A[l]) != fam.A[l]:
                afun = False
        heralded += int(any(proportional(c, fam.t1) for c in classes.values()))
        a_function += int(afun)
    return heralded, a_function


def run_family(seed, inject=None):
    fam = Family(seed, inject)
    fam.vals_all = dict(fam.vals)
    # x7: samples before G's first scaled arrival are constant.
    early_ok = all(len(set(fam.vals[x, t])) == 1 for x, t in SITE_TIMES
                   if t < min(dist(f, x) for f in SRC))
    control(early_ok, 'x7_pre_arrival_samples_constant')
    # x1: independent scalar evaluator.
    sample = sorted({0, WORLDS-1, (seed*97+13) % WORLDS})
    mism = 0
    for l in sample:
        sc = scalar_world(fam.bg, l)
        mism += sum(int(sc[k] != fam.vals[k][l]) for k in SITE_TIMES
                    if not (inject is not None and k == inject))
    control(mism == 0, 'x1_scalar_evaluator_agrees')
    search = family_search(fam, fam.parts)
    control(not search['undecided'], 'search_decided_family')
    her, afun = diagnostics(fam)
    few = [k for k in SITE_TIMES
           if all(is_trivial(pv) or two_block(pv) for pv in fam.parts[k])
           and not all(is_trivial(pv) for pv in fam.parts[k])]
    digest = hashlib.sha256()
    for k in SITE_TIMES:
        digest.update(bytes(fam.vals[k]))
    return fam, {
        'seed': seed, 'old_q9': fam.p, 'old_sign': fam.s, 'worlds': WORLDS,
        'read_site_times': len(SITE_TIMES),
        'max_blocks_given_V_histogram': histogram(fam),
        'two_block_or_trivial_cells': search['two_block_or_trivial_cells'],
        'nontrivial_two_block_or_trivial_cells': len(few),
        # Post-plan, reported only: where those cells are, how many V values
        # they split, and on how many of those the split has the target law.
        'nontrivial_two_block_cells_reported_only': [
            {'offset': list(k[0]), 'slice': k[1], 'G_arrival_slice': min(dist(f, k[0]) for f in SRC),
             'V_values_split': sum(1 for pv in fam.parts[k] if not is_trivial(pv)),
             'V_values_with_target_law': sum(1 for v, pv in enumerate(fam.parts[k])
                                             if not is_trivial(pv) and fam.law_of(v, pv) is not None)}
            for k in few],
        'law_good_partitions_per_v': search['good_partitions_per_v'],
        'admissible_R_exists': bool(search['admissible_R']),
        'admissible_R_count': len(search['admissible_R']),
        'heralded_single_site_times': her,
        'v6_A_function_of_V_and_single_site_time': afun,
        'x1_scalar_worlds': len(sample),
        'native_table_sha256': digest.hexdigest(),
    }


def planted_controls(fams):
    out = {}
    # x3: planted (0,A,0) in the full search pipeline, every family and common.
    x3 = True
    parts_by_fam = []
    for fam in fams:
        pl = fam.planted()
        parts = dict(fam.parts)
        parts[('P', 'A')] = fam.partitions(pl[('P', 'A')])
        fam.vals_all[('P', 'A')] = pl[('P', 'A')]
        r = family_search(fam, parts)
        x3 = x3 and not r['undecided'] and any(('P', 'A') in R for R in r['admissible_R'])
        x3 = x3 and passes_direct(fam, [pl[('P', 'A')]])
        parts_by_fam.append(parts)
    items = streams(SITE_TIMES)
    items[('P', 'A')] = [('P', 'A')]
    common = common_search(fams, parts_by_fam, items)
    x3 = x3 and not common['undecided'] and any(('P', 'A') in R for R in common['admissible_common_R'])
    out['x3_planted_positive_found'] = x3
    # x4: planted negatives rejected by both statistics.
    x4 = True
    for fam in fams:
        pl = fam.planted()
        for name in ('A_Y_leak', 'A_permuted_n', 'Z_only'):
            w = pl[('P', name)]
            x4 = x4 and not passes_direct(fam, [w]) and not passes_reduction(fam, [fam.partitions(w)])
        for name in ('A', 'A_xor_VB', 'A_other_code'):
            w = pl[('P', name)]
            x4 = x4 and passes_direct(fam, [w]) and passes_reduction(fam, [fam.partitions(w)])
    out['x4_planted_negatives_rejected_and_encodings_accepted'] = x4
    # x5: reduction against brute force, subset by subset, in two families.
    agree, subsets, passing = True, 0, 0
    for fam in fams[:2]:
        pl = fam.planted()
        pool = [pl[k] for k in sorted(pl)]
        nontriv = [k for k in SITE_TIMES if not all(is_trivial(pv) for pv in fam.parts[k])]
        triv = [k for k in SITE_TIMES if all(is_trivial(pv) for pv in fam.parts[k])]
        pool += [fam.vals[k] for k in nontriv[:3]] + [fam.vals[k] for k in triv[:1]]
        pparts = [fam.partitions(w) for w in pool]
        for mask in range(1, 1 << len(pool)):
            idx = [i for i in range(len(pool)) if (mask >> i) & 1]
            d = passes_direct(fam, [pool[i] for i in idx])
            r = passes_reduction(fam, [pparts[i] for i in idx])
            agree = agree and d == r
            subsets += 1
            passing += int(d)
    out['x5_reduction_equals_brute_force'] = agree
    out['x5_subsets_compared'] = subsets
    out['x5_passing_subsets'] = passing
    return out


def main():
    need(H == (0, 2, 4, 7, 1, 3, 5, 6), 'H table')
    controls = {}
    result = {
        'schema': 'oi-passive-native-readout-predicate-v8.0',
        'scope': ('class C(4,16): any set of whole native triples within distance 4 of q9, '
                  'read through L+17, with the single whole-V record; scaled dirty families, '
                  'conditional on C0; no gates, pads or added sources'),
        'scaled_parameters': {'n': NS, 'rho': RHO, 'tau_max': TAU, 'last_read_slice': TEND,
                              'dirty_initial_radius': R0, 'region_sites': len(REGION),
                              'read_site_times': len(SITE_TIMES)},
        'actual_astronomical_time_simulated': False,
        'native_storage_or_compilation_established': False,
        'observer_access_rule_adopted': False,
        'post_plan_rows': ['nontrivial_two_block_cells_reported_only, per family, reported only'],
    }
    try:
        geo = actual_geometry()
        controls['x6_carrier_first_tail_table_equals_v7'] = (
            geo['carrier_first_tail_minus_L'] == V7_FIRST_TAIL)
        control(controls['x6_carrier_first_tail_table_equals_v7'], 'x6')
        g_map = all(geo['region_first_G_minus_L'][x] == min(dist(f, x) for f in SRC)-NS
                    for x in REGION)
        free = min(geo['region_first_tail_minus_L'].values())
        controls['x7_reads_tail_free_at_actual_L'] = free > TEND-NS and g_map
        control(controls['x7_reads_tail_free_at_actual_L'], 'x7_geometry')
        result['actual_geometry'] = {
            'carrier_first_tail_minus_L': geo['carrier_first_tail_minus_L'],
            'region_min_first_tail_minus_L': free,
            'region_max_first_tail_minus_L': max(geo['region_first_tail_minus_L'].values()),
            'last_read_actual_time_minus_L': TEND-NS,
            'region_min_first_G_minus_L': min(geo['region_first_G_minus_L'].values()),
            'scaled_G_arrival_equals_actual_minus_L_plus_n': g_map,
        }
        seeds = choose_families()
        fams, rows = [], []
        for seed in seeds:
            fam, row = run_family(seed)
            fams.append(fam)
            rows.append(row)
        controls['x1_scalar_evaluator_agrees'] = True
        controls['x2_native_A_pool_and_inverse'] = True
        controls['x7_pre_arrival_samples_constant'] = True
        pc = planted_controls(fams)
        for k in ('x3_planted_positive_found',
                  'x4_planted_negatives_rejected_and_encodings_accepted',
                  'x5_reduction_equals_brute_force'):
            controls[k] = pc[k]
            control(pc[k], k)
        # Main decision on native cells only (planted cells removed).
        native_parts = [{k: p for k, p in fam.parts.items()} for fam in fams]
        common = common_search(fams, native_parts, streams(SITE_TIMES))
        control(not common['undecided'], 'search_decided_common')
        zero_fam, zero_row = run_family(0)
    except Void as e:
        controls['failed'] = str(e)
        result['required_controls'] = controls
        result['all_required_controls_pass'] = False
        result['verdict'] = 'VOID'
        print(json.dumps(result, indent=2, sort_keys=True))
        sys.exit(2)
    holds = bool(common['admissible_common_R'])
    result['verdict'] = 'HOLDS_WITHIN_SCOPE' if holds else 'NEGATIVE_FOR_CONSTRUCTION'
    result['families'] = rows
    result['families_with_no_admissible_R'] = sum(1 for r in rows if not r['admissible_R_exists'])
    result['common_stream_closed_candidates'] = common['candidates']
    result['common_stream_closed_admissible_R'] = [
        [repr(k) for k in R] for R in common['admissible_common_R']]
    result['zero_background_diagnostic'] = zero_row
    result['planted_controls'] = pc
    result['required_controls'] = controls
    result['all_required_controls_pass'] = True
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
