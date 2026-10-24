"""Depth extension of the per-slot fresh-block finite controller.

Exact integer/rational arithmetic, Python standard library only. Imports no
earlier checker and reads no input file. Retained a2_efficiency_v6 values are
pinned as constants below; PROVENANCE.json pins the file they come from.
"""
from fractions import Fraction as Q
from itertools import product
from bisect import bisect_right
from math import comb, isqrt, lcm
import hashlib
import json
import sys


def check(x, label):
    if not x:
        raise RuntimeError(label)


# Retained a2_efficiency_v6/result.json values (selected M=16 certificate).
A2_KAPPA = Q(6419131, 419430400)
A2_CQ_BOUND = Q(17239332625914280559, 230584300921369395200)
A2_DIGEST = '0637f0089fc5ce666d17ddaf828cc98bf317d46e3ea3cd22851bc21eb893a6a1'

QUANTUM = Q(4, 5)          # agreement probability for poles at a.X = 3/5
TENTH, HALF = Q(1, 10), Q(1, 2)

AXES = {'X': (Q(1), Q(0), Q(0)), 'Y': (Q(0), Q(1), Q(0)),
        'Z': (Q(0), Q(0), Q(1)), 'a': (Q(3, 5), Q(4, 5), Q(0))}
BASE = dict(AXES, p=(Q(2, 3), Q(-2, 3), Q(1, 3)), q=(Q(2, 3), Q(-2, 3), Q(-1, 3)))
PREP = {name + sg: tuple(s * x for x in n)
        for name, n in BASE.items() for s, sg in [(1, '+'), (-1, '-')]}


def neg(v):
    return tuple(-x for x in v)


def as_integer(n):
    den = lcm(*(x.denominator for x in n))
    return tuple(int(x * den) for x in n), den


class Grid:
    """Six-face grid, integer weights and fair CDF counts (finite-a2-v5 order)."""

    def __init__(self, M, W, B):
        self.M, self.W, self.B, self.K = M, W, B, 1 << B
        self.z, self.q = [], []
        for face in range(3):
            free = [j for j in range(3) if j != face]
            for s in (-1, 1):
                for u, v in product(range(-M + 1, M, 2), repeat=2):
                    z = [0, 0, 0]
                    z[face] = s * M
                    z[free[0]], z[free[1]] = u, v
                    self.z.append(tuple(z))
                    self.q.append(sum(x * x for x in z))
        self.N = len(self.z)
        check(self.N == 6 * M * M and len(set(self.z)) == self.N, 'grid alphabet')
        where = {z: i for i, z in enumerate(self.z)}
        self.anti = [where[neg(z)] for z in self.z]
        self.cache = {}

    def counts(self, n):
        n = tuple(n)
        if n in self.cache:
            return self.cache[n]
        check(sum(x * x for x in n) == 1, 'unit direction')
        if next(x for x in n if x) < 0:
            base = self.counts(neg(n))
            out = tuple(base[self.anti[i]] for i in range(self.N))
        else:
            v, d = as_integer(n)
            f = (1 << self.W) * self.M ** 3
            w = []
            for z, q in zip(self.z, self.q):
                s = sum(a * b for a, b in zip(v, z))
                w.append(f * s // (d * q * q) if s > 0 else 0)
            tot = sum(w)
            check(tot > 0, 'positive weights')
            out, cum, last = [], 0, 0
            for x in w:
                cum += x
                cut = self.K * cum // tot
                out.append(cut - last)
                last = cut
            check(last == self.K, 'complete CDF')
            out = tuple(out)
        check(min(out) >= 0 and sum(out) == self.K, 'fair seed counts')
        self.cache[n] = out
        return out

    def sign_mass(self, n, axis, s):
        """Seed count with response s; zero responses counted separately."""
        v, _ = as_integer(axis)
        hit = zero = 0
        for c, z in zip(self.counts(n), self.z):
            x = sum(a * b for a, b in zip(v, z))
            if x == 0:
                zero += c
            if (1 if x >= 0 else -1) == s:
                hit += c
        return hit, zero

    def table(self, n):
        cum, x = [], 0
        for c in self.counts(n):
            x += c
            cum.append(x)
        return cum

    def label(self, cum, seed):
        return bisect_right(cum, seed)


def agreement(grid):
    """Agreement masses for both signs of each pole, computed directly."""
    X, a = AXES['X'], AXES['a']
    rows = {}
    for s in (1, -1):
        pole = tuple(s * x for x in a)
        hit, zero = grid.sign_mass(pole, X, s)
        rows['A' + ('+' if s == 1 else '-')] = (hit, zero)
        pole = tuple(s * x for x in X)
        hit, zero = grid.sign_mass(pole, a, s)
        rows['B' + ('+' if s == 1 else '-')] = (hit, zero)
    return rows


# ---------- exact complete-record TV of independent agreement slots ----------

def slots(h):
    return h // 2, (h + 1) // 2     # (A-type reads, B-type reads); read 1 is B-type


def tv_direct(pa, pb, h):
    """(1/2) sum |p-q| over agreement counts; small h only."""
    na, nb = slots(h)
    tot = Q(0)
    for i in range(na + 1):
        for j in range(nb + 1):
            src = pa ** i * (1 - pa) ** (na - i) * pb ** j * (1 - pb) ** (nb - j)
            qq = QUANTUM ** (i + j) * (1 - QUANTUM) ** (h - i - j)
            tot += comb(na, i) * comb(nb, j) * abs(src - qq)
    return tot / 2


def tv_fast(pa, pb, h):
    """Sum of positive parts using monotone likelihood ratio and prefix sums."""
    na, nb = slots(h)
    D = lcm(pa.denominator, pb.denominator, QUANTUM.denominator)
    ai, bi, qi = pa.numerator * (D // pa.denominator), pb.numerator * (D // pb.denominator), QUANTUM.numerator * (D // QUANTUM.denominator)
    # source mass numerators over D^h; quantum mass numerators over D^h
    al = [ai ** i * (D - ai) ** (na - i) for i in range(na + 1)]
    be = [bi ** j * (D - bi) ** (nb - j) for j in range(nb + 1)]
    qa = [qi ** i * (D - qi) ** (na - i) for i in range(na + 1)]
    qb = [qi ** j * (D - qi) ** (nb - j) for j in range(nb + 1)]
    cb = [comb(nb, j) for j in range(nb + 1)]
    pre_s, pre_q = [0], [0]
    for j in range(nb + 1):
        pre_s.append(pre_s[-1] + cb[j] * be[j])
        pre_q.append(pre_q[-1] + cb[j] * qb[j])
    inc = bi * (D - qi) > qi * (D - bi)      # be/qb increasing in j
    total = 0
    for i in range(na + 1):
        def pos(j):
            return al[i] * be[j] > qa[i] * qb[j]
        lo, hi = 0, nb + 1                  # find first index where predicate flips
        if inc:
            while lo < hi:
                m = (lo + hi) // 2
                if pos(m):
                    hi = m
                else:
                    lo = m + 1
            js, je = lo, nb + 1
        else:
            while lo < hi:
                m = (lo + hi) // 2
                if pos(m):
                    lo = m + 1
                else:
                    hi = m
            js, je = 0, lo
        part = al[i] * (pre_s[je] - pre_s[js]) - qa[i] * (pre_q[je] - pre_q[js])
        check(part >= 0, 'positive-part block')
        total += comb(na, i) * part
    return Q(total, D ** h)


def tv_records(prob_fn, h):
    """Brute-force TV over all 2^h records; prob_fn(t, agree) per slot."""
    tot = Q(0)
    for rec in product((1, 0), repeat=h):
        src = Q(1)
        qq = Q(1)
        for t, g in enumerate(rec, 1):
            p = prob_fn(t)
            src *= p if g else 1 - p
            qq *= QUANTUM if g else 1 - QUANTUM
        tot += abs(src - qq)
    return tot / 2


def display(x, digits=12):
    scaled = x.numerator * 10 ** digits // x.denominator
    return '0.' + str(scaled).zfill(digits) if scaled < 10 ** digits else str(Q(scaled, 10 ** digits))


def digest(x):
    return hashlib.sha256(f'{x.numerator:x}/{x.denominator:x}'.encode()).hexdigest()   # hexadecimal num/den


def bracket(da, db, h):
    na, nb = slots(h)
    S = (na * da * da + nb * db * db) / 4
    hell = 1 - (1 - da * da / 4) ** na * (1 - db * db / 4) ** nb
    return S / (1 + S), hell, na * da + nb * db


# ---------- controller under test ----------

def controller():
    g = Grid(16, 16, 24)
    blob = json.dumps({k: g.counts(n) for k, n in PREP.items()}, sort_keys=True,
                      separators=(',', ':')).encode()
    check(hashlib.sha256(blob).hexdigest() == A2_DIGEST, 'rebuilt counts equal executed a2 controller')
    rows = agreement(g)
    for k, (hit, zero) in rows.items():
        check(zero == 0, 'no zero responses on X and a reads')
    check(rows['A+'][0] == rows['A-'][0] and rows['B+'][0] == rows['B-'][0], 'sign-independent agreement')
    pa, pb = Q(rows['A+'][0], g.K), Q(rows['B+'][0], g.K)
    da, db = abs(pa - QUANTUM), abs(pb - QUANTUM)
    check(da <= A2_KAPPA and db <= A2_KAPPA, 'per-read discrepancy within retained kappa')
    return g, pa, pb, da, db


def depth_scan(pa, pb, da, db):
    exact = {}
    for h in range(1, 65):
        exact[h] = tv_fast(pa, pb, h)
        if h <= 24:
            check(exact[h] == tv_direct(pa, pb, h), 'fast and direct TV agree')
    for h in (128, 256, 512, 1024, 2048):
        exact[h] = tv_fast(pa, pb, h)
    hs = sorted(exact)
    for u, v in zip(hs, hs[1:]):
        check(exact[u] <= exact[v], 'TV nondecreasing in depth')
    for h, t in exact.items():
        low, hell, up = bracket(da, db, h)
        check(low <= hell <= t <= up, 'certified bracket contains exact TV')
    crossing = None
    above = [h for h in hs if exact[h] > TENTH]
    if above:
        hi = above[0]
        lo = max(h for h in hs if h < hi)
        while hi - lo > 1:
            m = (lo + hi) // 2
            exact[m] = tv_fast(pa, pb, m)
            if exact[m] > TENTH:
                hi = m
            else:
                lo = m
        check(exact[lo] <= TENTH < exact[hi], 'first exact crossing')
        crossing = hi
    above_half = [h for h in sorted(exact) if exact[h] > HALF]
    return exact, crossing, (above_half[0] if above_half else None)


def certified_depth(da, db, level):
    """Least h with S(h)/(1+S(h)) > level, S from the rational Hellinger bound."""
    need = level / (1 - level)
    lo, hi = 0, 1
    while (slots(hi)[0] * da * da + slots(hi)[1] * db * db) / 4 <= need:
        hi *= 2
    while hi - lo > 1:
        m = (lo + hi) // 2
        if (slots(m)[0] * da * da + slots(m)[1] * db * db) / 4 > need:
            hi = m
        else:
            lo = m
    return hi


# ---------- class statement ----------

def nearest_dyadic(B):
    K = 1 << B
    k = (4 * K) // 5
    best = min((k, k + 1), key=lambda x: abs(QUANTUM - Q(x, K)))
    return best, abs(QUANTUM - Q(best, K))


def class_statement():
    rows = []
    for B in range(1, 65):
        k, d = nearest_dyadic(B)
        closed = Q(2 if B % 2 else 1, 5 * (1 << B))
        check(d == closed and d > 0, 'closed-form dyadic distance')
        rows.append(B)
    d24 = Q(1, 5 * (1 << 24))
    c = d24 * d24 / 4
    half_depth = 1 / c + 1                  # h*c > 1 implies T > 1/2
    check(half_depth.denominator == 1, 'integer certified depth')
    tenth_upper = (TENTH / d24).numerator // (TENTH / d24).denominator   # h*d24 <= 1/10
    return {'B_range_verified': [rows[0], rows[-1]],
            'distance_formula': 'dist(4/5,2^-B Z)=2^-B*(2/5 if B odd else 1/5)',
            'B24_distance': str(d24),
            'B24_depth_certified_T_above_half': int(half_depth),
            'B24_max_depth_coupling_T_at_most_tenth_best_sampler': tenth_upper}


def growing_bits_control():
    B0 = 6

    def bits(t):
        return B0 + 2 * (t - 1).bit_length()      # 2*ceil(log2 t)

    def prob(t):
        k, _ = nearest_dyadic(bits(t))
        return Q(k, 1 << bits(t))
    bound_all = Q(4, 5 * (1 << B0))               # (2/5)2^-B0 * sum 1/t^2 <= (2/5)2^-B0 * 2
    out = {}
    for h in (1, 2, 4, 8, 12):
        t = tv_records(prob, h)
        partial = sum((abs(prob(s) - QUANTUM) for s in range(1, h + 1)), Q(0))
        check(t <= partial <= bound_all, 'growing per-slot bits keep TV bounded')
        out[str(h)] = display(t, 20)
    bits_12 = sum(bits(t) for t in range(1, 13))
    # Fixed B0 over the same depth: strictly positive per-read distance.
    k, d = nearest_dyadic(B0)
    check(d > 0, 'fixed-B0 discrepancy positive')
    pf = Q(k, 1 << B0)
    fixed = {str(h): display(tv_fast(pf, pf, h)) for h in (12, 256, 2048)}
    check(tv_fast(pf, pf, 2048) > tv_records(prob, 12), 'fixed B0 exceeds growing-bit control')
    fixed_half = certified_depth(d, d, HALF)
    return {'B0': B0, 'rule': 'B_t=B0+2*ceil(log2 t), nearest-dyadic Bernoulli per slot',
            'tv_by_h_display': out, 'uniform_bound_all_h': str(bound_all),
            'fresh_bits_through_h12': bits_12,
            'fixed_B0_contrast': {'tv_by_h_display': fixed, 'certified_depth_T_above_half': fixed_half}}


# ---------- controls ----------

def positive_control():
    for h in list(range(1, 13)) + [64, 256]:
        check(tv_fast(QUANTUM, QUANTUM, h) == 0, 'exact source gives zero TV')
        if h <= 12:
            check(tv_direct(QUANTUM, QUANTUM, h) == 0, 'direct zero TV')
            check(tv_records(lambda t: QUANTUM, h) == 0, 'record enumeration zero TV')
        low, hell, up = bracket(Q(0), Q(0), h)
        check(low == hell == up == 0, 'zero bracket')
    return {'five_atom_exact_source_zero_tv_through': 256}


def record_enumeration_control(pa, pb):
    n = 0
    for h in range(1, 13):
        t = tv_records(lambda s: pb if s % 2 else pa, h)
        check(t == tv_direct(pa, pb, h) == tv_fast(pa, pb, h), 'record enumeration agrees')
        n += 1 << h
    return n


def seeded_control():
    g = Grid(8, 10, 10)
    X, a = AXES['X'], AXES['a']
    tabs = {(ax, s): g.table(tuple(s * x for x in AXES[ax])) for ax in ('X', 'a') for s in (1, -1)}
    vx, _ = as_integer(X)
    va, _ = as_integer(a)
    lab = {k: [g.label(t, seed) for seed in range(g.K)] for k, t in tabs.items()}
    resp = {'X': [1 if sum(p * q for p, q in zip(vx, z)) >= 0 else -1 for z in g.z],
            'a': [1 if sum(p * q for p, q in zip(va, z)) >= 0 else -1 for z in g.z]}
    counts = {}
    for s0 in range(g.K):                  # preparation block, read a
        s1 = resp['a'][lab['X', 1][s0]]
        row = lab['a', s1]
        for s1seed in range(g.K):          # reset block after read 1, read X
            s2 = resp['X'][row[s1seed]]
            counts[s1, s2] = counts.get((s1, s2), 0) + 1
    rows = agreement(g)
    pa, pb = Q(rows['A+'][0], g.K), Q(rows['B+'][0], g.K)
    check(rows['A+'][0] == rows['A-'][0] and rows['B+'][0] == rows['B-'][0], 'small sign independence')
    for (s1, s2), c in counts.items():
        p1 = pb if s1 == 1 else 1 - pb
        p2 = pa if s2 == s1 else 1 - pa
        check(Q(c, g.K * g.K) == p1 * p2, 'seed exhaustion equals per-slot product law')
        check((Q(c, g.K * g.K) / p1 * g.K).denominator == 1, 'conditional law in 2^-B Z')
    return {'grid': [8, 10, 10], 'seed_pairs': g.K * g.K, 'records': len(counts)}


def pooled_countercontrol():
    out = {}
    nondyadic = False
    for h in range(1, 13):
        N = 24 * h
        K = 1 << N
        leaves = []

        def walk(lo, hi, depth, rec):
            if depth == h:
                leaves.append((rec, lo, hi))
                return
            mid = lo + QUANTUM * (hi - lo)
            walk(lo, mid, depth + 1, rec + (1,))
            walk(mid, hi, depth + 1, rec + (0,))
        walk(Q(0), Q(1), 0, ())

        def ceil_scale(x):
            return -((-x.numerator * K) // x.denominator)
        mass = {}
        tv = Q(0)
        for rec, lo, hi in leaves:
            m = Q(ceil_scale(hi) - ceil_scale(lo), K)
            mass[rec] = m
            tv += abs(m - (hi - lo))
        tv /= 2
        check(sum(mass.values()) == 1, 'pooled sampler normalized')
        check(tv <= Q(1 << (h - 1), K), 'pooled TV within 2^(h-1-N)')
        if h >= 2:
            first = sum((m for r, m in mass.items() if r[0] == 1), Q(0))
            both = sum((m for r, m in mass.items() if r[0] == 1 and r[1] == 1), Q(0))
            cond = both / first
            if (cond * (1 << 24)).denominator != 1:
                nondyadic = True
        out[str(h)] = display(tv, 30)
    check(nondyadic, 'pooled conditional law leaves 2^-24 Z')
    return {'bank_bits_rule': 'N=24h', 'tv_by_h_display': out,
            'conditional_law_outside_2^-24Z': nondyadic}


def main():
    g, pa, pb, da, db = controller()
    exact, cross, cross_half = depth_scan(pa, pb, da, db)
    t3 = exact[3]
    check(t3 <= A2_CQ_BOUND, 'h=3 TV within retained certificate')
    pos = positive_control()
    enum = record_enumeration_control(pa, pb)
    seeded = seeded_control()
    pooled = pooled_countercontrol()
    cls = class_statement()
    grow = growing_bits_control()
    obstruction = (pa != QUANTUM) or (pb != QUANTUM)
    cert = {str(l): certified_depth(da, db, l) for l in (TENTH, HALF, Q(9, 10))} if obstruction else None
    small = {str(h): str(exact[h]) for h in range(1, 5)}
    table = {str(h): {'display': display(exact[h]), 'sha256': digest(exact[h]),
                      'above_tenth': exact[h] > TENTH, 'above_half': exact[h] > HALF}
             for h in sorted(exact)}
    if obstruction:
        verdict = ('NO_DEPTH_UNIFORM_COMPLETE_RECORD_BOUND_FOR_THIS_EXTENSION:'
                   f' exact TV exceeds 1/10 first at h={cross}' if cross else
                   'NO_DEPTH_UNIFORM_COMPLETE_RECORD_BOUND_FOR_THIS_EXTENSION: 1/10 not reached by h=2048')
        verdict += f'; certified TV>1/2 for h>={cert[str(HALF)]}'
    else:
        verdict = 'NO_OBSTRUCTION_FROM_THIS_PROTOCOL'
    out = {
        'schema': 'oi.a2-depth-extension-v7.v1',
        'controller': {'M': g.M, 'W': g.W, 'B': g.B, 'labels': g.N,
                       'counts_digest_matches_a2': True,
                       'A_reset_a_read_X': str(pa), 'B_reset_X_read_a': str(pb),
                       'dA': str(da), 'dB': str(db), 'retained_kappa': str(A2_KAPPA)},
        'protocol': 'prepare X+, then reads a,X,a,X,...; quantum agreement 4/5 per read',
        'exact_tv_h1_to_4': small,
        'exact_tv_table': table,
        'first_exact_depth_tv_above_tenth': cross,
        'first_tabulated_depth_tv_above_half': cross_half,
        'certified_depth_lower_bound_exceeds': cert,
        'h3_tv_vs_retained_certificate': {'tv': str(t3), 'certificate': str(A2_CQ_BOUND)},
        'class_statement': cls,
        'growing_bits_sampler_control': grow,
        'controls': {'positive': pos, 'record_enumeration_records': enum,
                     'seeded_exhaustion': seeded, 'pooled_bank_countercontrol': pooled,
                     'sign_control': 'agreement masses for both pole signs computed directly and equal; zero responses 0'},
        'scope': ('Natural slot extension of the executed M=16 controller and the per-slot fresh '
                  'fair-block class, on one in-menu protocol. Not a bound on total or pooled '
                  'randomness, per-read error, continuous resources or OI; the h=3 certificate is unchanged.'),
        'verdict': verdict,
    }
    text = json.dumps(out, sort_keys=True, separators=(',', ':'))
    if '--output' in sys.argv:
        with open(sys.argv[sys.argv.index('--output') + 1], 'w') as f:
            f.write(text + '\n')
    else:
        print(text)


if __name__ == '__main__':
    main()
