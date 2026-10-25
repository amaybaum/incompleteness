"""Bounded persistent memory and the depth obstruction (a2_memory_v8).

Exact integer/rational arithmetic, Python standard library only. Imports no
earlier checker. Reads one retained file, a2_depth_v7/result.json, after
checking its SHA-256 against the pinned value; its values are the targets of
the reproduction controls. A failed required control prints VOID and exits 2.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, isqrt, lcm
import hashlib
import json
import os
import re
import subprocess
import sys


class Void(Exception):
    pass


def check(x, label):
    if not x:
        raise Void(label)


HERE = os.path.dirname(os.path.abspath(__file__))
V7_RESULT = os.path.join(HERE, '..', 'a2_depth_v7', 'result.json')
V7_RESULT_SHA256 = '2e8988de7285cf1ae6781fbed37eb4e869ecf16511b374a923b5dcdbfed589a7'
PLAN = os.path.join(HERE, 'PLAN.md')
PLAN_SHA256 = 'b7f7eaae58de13b9eb348bb4e31e92a7bce6741be64553c9ba496af9a2c6a275'
PLAN_COMMIT = '1dfec979721336cc9f0ce703b544f9d6be8e906c'
PROVENANCE = os.path.join(HERE, 'PROVENANCE.json')
GIT_DIR = HERE
A2_DIGEST = '0637f0089fc5ce666d17ddaf828cc98bf317d46e3ea3cd22851bc21eb893a6a1'

QUANTUM = Q(4, 5)          # agreement probability for poles at a.X = 3/5
TENTH, HALF = Q(1, 10), Q(1, 2)
ROOT_BITS = 192

AXES = {'X': (Q(1), Q(0), Q(0)), 'Y': (Q(0), Q(1), Q(0)),
        'Z': (Q(0), Q(0), Q(1)), 'a': (Q(3, 5), Q(4, 5), Q(0))}
BASE = dict(AXES, p=(Q(2, 3), Q(-2, 3), Q(1, 3)), q=(Q(2, 3), Q(-2, 3), Q(-1, 3)))
PREP = {name + sg: tuple(s * x for x in n)
        for name, n in BASE.items() for s, sg in [(1, '+'), (-1, '-')]}


def load_v7():
    with open(V7_RESULT, 'rb') as f:
        raw = f.read()
    check(hashlib.sha256(raw).hexdigest() == V7_RESULT_SHA256, 'K1/K2 pinned a2_depth_v7 result.json hash')
    return json.loads(raw)


def display(x, digits=12):
    scaled = x.numerator * 10 ** digits // x.denominator
    return '0.' + str(scaled).zfill(digits) if scaled < 10 ** digits else str(Q(scaled, 10 ** digits))


def digest(x):
    return hashlib.sha256(f'{x.numerator:x}/{x.denominator:x}'.encode()).hexdigest()


def root_hi(x, bits=ROOT_BITS):
    """Rational upper endpoint of sqrt(x), verified by squaring."""
    check(x >= 0, 'K7 nonnegative root')
    d = 1 << bits
    k = isqrt(x.numerator * d * d // x.denominator)
    hi = Q(k, d) if Q(k, d) ** 2 >= x else Q(k + 1, d)
    check(hi * hi >= x and (hi == 0 or (hi - Q(1, d)) ** 2 < x), 'K7 square-root upper enclosure')
    return hi


def root_lo(x, bits=ROOT_BITS):
    """Rational lower endpoint of sqrt(x), verified by squaring."""
    check(x >= 0, 'K7 nonnegative root')
    d = 1 << bits
    k = isqrt(x.numerator * d * d // x.denominator)
    lo = Q(k, d)
    check(lo * lo <= x and (lo + Q(1, d)) ** 2 > x, 'K7 square-root lower enclosure')
    return lo


# ---------- K1: the executed memoryless controller ----------

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
        check(self.N == 6 * M * M and len(set(self.z)) == self.N, 'K1 grid alphabet')
        where = {z: i for i, z in enumerate(self.z)}
        self.anti = [where[neg(z)] for z in self.z]
        self.cache = {}

    def counts(self, n):
        n = tuple(n)
        if n in self.cache:
            return self.cache[n]
        check(sum(x * x for x in n) == 1, 'K1 unit direction')
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
            out, cum, last = [], 0, 0
            for x in w:
                cum += x
                cut = self.K * cum // tot
                out.append(cut - last)
                last = cut
            check(last == self.K, 'K1 complete CDF')
            out = tuple(out)
        check(min(out) >= 0 and sum(out) == self.K, 'K1 fair seed counts')
        self.cache[n] = out
        return out

    def sign_mass(self, n, axis, s):
        v, _ = as_integer(axis)
        hit = zero = 0
        for c, z in zip(self.counts(n), self.z):
            x = sum(a * b for a, b in zip(v, z))
            if x == 0:
                zero += c
            if (1 if x >= 0 else -1) == s:
                hit += c
        return hit, zero


def tv_iid(p, h):
    """Exact TV of Bernoulli(p)^h against Bernoulli(4/5)^h."""
    D = lcm(p.denominator, QUANTUM.denominator)
    pi, qi = p.numerator * (D // p.denominator), QUANTUM.numerator * (D // QUANTUM.denominator)

    def powers(x):
        out = [1]
        for _ in range(h):
            out.append(out[-1] * x)
        return out
    ps, pf, qs, qf = powers(pi), powers(D - pi), powers(qi), powers(D - qi)
    tot, c = 0, 1
    for i in range(h + 1):
        tot += c * abs(ps[i] * pf[h - i] - qs[i] * qf[h - i])
        c = c * (h - i) // (i + 1)
    return Q(tot, 2 * D ** h)


def tv_product(pa, pb, h):
    """Exact TV of alternating independent agreement slots (read 1 B-type) against Bernoulli(4/5)^h."""
    na, nb = h // 2, (h + 1) // 2
    D = lcm(pa.denominator, pb.denominator, QUANTUM.denominator)
    ai, bi, qi = (x.numerator * (D // x.denominator) for x in (pa, pb, QUANTUM))
    tot = 0
    for i in range(na + 1):
        for j in range(nb + 1):
            src = ai ** i * (D - ai) ** (na - i) * bi ** j * (D - bi) ** (nb - j)
            qq = qi ** (i + j) * (D - qi) ** (h - i - j)
            tot += comb(na, i) * comb(nb, j) * abs(src - qq)
    return Q(tot, 2 * D ** h)


def memoryless_controller(v7):
    g = Grid(16, 16, 24)
    blob = json.dumps({k: g.counts(n) for k, n in PREP.items()}, sort_keys=True,
                      separators=(',', ':')).encode()
    check(hashlib.sha256(blob).hexdigest() == A2_DIGEST, 'K1 rebuilt counts equal executed a2 controller')
    nxt = {'X': 'a', 'a': 'X'}
    mass = {}
    for ax in ('X', 'a'):
        for s in (1, -1):
            pole = tuple(s * x for x in AXES[ax])
            for o in (1, -1):
                hit, zero = g.sign_mass(pole, AXES[nxt[ax]], o)
                check(zero == 0, 'K1 no zero responses')
                mass[ax, s, o] = Q(hit, g.K)
    pa, pb = mass['a', 1, 1], mass['X', 1, 1]
    check(mass['a', -1, -1] == pa and mass['X', -1, -1] == pb, 'K1 sign control')
    c = v7['controller']
    check(str(pa) == c['A_reset_a_read_X'] and str(pb) == c['B_reset_X_read_a'], 'K1 A and B equal a2_depth_v7')
    for h in range(1, 5):
        check(str(tv_product(pa, pb, h)) == v7['exact_tv_h1_to_4'][str(h)], 'K1 exact T(1..4) equal a2_depth_v7')
    for h in range(1, 65):
        check(digest(tv_product(pa, pb, h)) == v7['exact_tv_table'][str(h)]['sha256'],
              'K1 T(h) digests h<=64 equal a2_depth_v7')
    # The same controller as a finite chain on signed poles, for the generic engine and step (4).
    states = [(ax, s) for ax in ('X', 'a') for s in (1, -1)]
    idx = {st: i for i, st in enumerate(states)}
    D = {0: {}, 1: {}}
    for (ax, s) in states:
        for o in (1, -1):
            D[1 if o == s else 0][idx[ax, s], idx[nxt[ax], o]] = mass[ax, s, o]
    chain = {'n': 4, 'init': {idx['X', 1]: Q(1)}, 'D': D}
    return chain, pa, pb, g.K


# ---------- generic hidden-chain record engine ----------

def chain_tv(chain, h):
    """Exact complete-record TV of a finite chain's agreement record against Bernoulli(4/5)^h."""
    D = chain['D']
    rows = {g: {} for g in (0, 1)}
    for g in (0, 1):
        for (i, j), p in D[g].items():
            rows[g].setdefault(i, []).append((j, p))
    total = [Q(0)]

    def dfs(alpha, qm, depth):
        if depth == h:
            total[0] += abs(sum(alpha.values(), Q(0)) - qm)
            return
        for g in (1, 0):
            nxt = {}
            for i, w in alpha.items():
                for j, p in rows[g].get(i, ()):
                    nxt[j] = nxt.get(j, Q(0)) + w * p
            dfs(nxt, qm * (QUANTUM if g else 1 - QUANTUM), depth + 1)
    dfs(dict(chain['init']), Q(1), 0)
    return total[0] / 2


def chain_law(chain, h):
    D = chain['D']
    rows = {g: {} for g in (0, 1)}
    for g in (0, 1):
        for (i, j), p in D[g].items():
            rows[g].setdefault(i, []).append((j, p))
    law = {}

    def dfs(alpha, rec):
        if len(rec) == h:
            law[rec] = sum(alpha.values(), Q(0))
            return
        for g in (1, 0):
            nxt = {}
            for i, w in alpha.items():
                for j, p in rows[g].get(i, ()):
                    nxt[j] = nxt.get(j, Q(0)) + w * p
            dfs(nxt, rec + (g,))
    dfs(dict(chain['init']), ())
    return law


# ---------- step (4): closed classes, stationary laws, run mismatches ----------

def closed_classes(n, P):
    reach = [{i} for i in range(n)]
    for i in range(n):
        stack = [i]
        while stack:
            u = stack.pop()
            for v in range(n):
                if P[u][v] and v not in reach[i]:
                    reach[i].add(v)
                    stack.append(v)
    out = []
    for i in range(n):
        if all(i in reach[j] for j in reach[i]):
            cls = tuple(sorted(reach[i]))
            if cls not in out:
                out.append(cls)
    return out


def solve(Amat, b):
    """Exact Gaussian elimination for a nonsingular square system."""
    n = len(Amat)
    M = [row[:] + [b[i]] for i, row in enumerate(Amat)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        check(p is not None, 'step4 nonsingular stationary system')
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


def det(Mat):
    n = len(Mat)
    M = [row[:] for row in Mat]
    d = Q(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Q(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            if M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return d


RUN_RANGE = None   # None: n = 1..|C| as the proof requires


def class_analysis(n, D0, D1, N):
    """For each closed class: stationary law, least run mismatch, char-poly value at 4N/5."""
    P = [[D0[i][j] + D1[i][j] for j in range(n)] for i in range(n)]
    out = []
    for C in closed_classes(n, P):
        m = len(C)
        PC = [[P[i][j] for j in C] for i in C]
        # pi (P - I) = 0, sum pi = 1: replace the last equation with normalization.
        A = [[PC[j][i] - (1 if i == j else 0) for j in range(m)] for i in range(m)]
        A[-1] = [Q(1)] * m
        b = [Q(0)] * (m - 1) + [Q(1)]
        pi = solve(A, b)
        check(all(x >= 0 for x in pi) and sum(pi) == 1, 'step4 stationary law')
        for i in range(m):
            check(sum(pi[j] * PC[j][i] for j in range(m)) == pi[i], 'step4 stationary equation')
        D1C = [[D1[i][j] for j in C] for i in C]
        vec = pi[:]
        first = None
        top = m if RUN_RANGE is None else RUN_RANGE
        runs = []
        for t in range(1, top + 1):
            vec = [sum(vec[i] * D1C[i][j] for i in range(m)) for j in range(m)]
            a = sum(vec, Q(0))
            runs.append(a)
            if first is None and a != QUANTUM ** t:
                first = t
        lam = QUANTUM * N
        chi = det([[(lam if i == j else 0) - N * D1C[i][j] for j in range(m)] for i in range(m)])
        out.append({'size': m, 'freq': runs[0], 'first_mismatch': first, 'chi': chi})
    return out


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for rest in compositions(total - x, parts - 1):
            yield (x,) + rest


def enumerate_chains(n, N):
    """Every n-state agreement chain whose per-state outcome counts over (next state, bit) sum to N."""
    per_state = list(compositions(N, 2 * n))
    for choice in product(per_state, repeat=n):
        D0 = [[Q(0)] * n for _ in range(n)]
        D1 = [[Q(0)] * n for _ in range(n)]
        for i, comp in enumerate(choice):
            for k, c in enumerate(comp):
                j, g = divmod(k, 2)
                (D1 if g else D0)[i][j] = Q(c, N)
        yield D0, D1


def step4_census():
    sizes = [(1, B) for B in range(1, 9)] + [(2, 1), (2, 2), (2, 3), (3, 1)]
    rows = {}
    exact_freq = []
    for n, B in sizes:
        N = 1 << B
        chains = classes = freq45 = 0
        worst = 0
        for D0, D1 in enumerate_chains(n, N):
            chains += 1
            for cl in class_analysis(n, D0, D1, N):
                classes += 1
                if cl['first_mismatch'] is None:
                    raise Void(f'step4 dyadic chain without run mismatch (n={n}, B={B}): proof route contradicted')
                check(cl['chi'] != 0, 'step4 characteristic polynomial nonzero at 2^(B+2)/5')
                worst = max(worst, cl['first_mismatch'])
                if cl['freq'] == QUANTUM:
                    freq45 += 1
                    check(cl['first_mismatch'] >= 2, 'K5 exact-frequency class mismatches at n>=2')
                    if len(exact_freq) < 3:
                        exact_freq.append({'n': n, 'B': B, 'D0': [[str(x) for x in r] for r in D0],
                                           'D1': [[str(x) for x in r] for r in D1],
                                           'first_mismatch': cl['first_mismatch']})
        check(chains == comb(N + 2 * n - 1, 2 * n - 1) ** n, 'census chain count equals C(2^B+2n-1,2n-1)^n')
        rows[f'n{n}_B{B}'] = {'chains': chains, 'closed_classes': classes,
                              'classes_with_exact_frequency_4/5': freq45,
                              'largest_least_mismatch_index': worst}
    check(sum(r['classes_with_exact_frequency_4/5'] for r in rows.values()) > 0,
          'K5 a dyadic chain with exact stationary frequency 4/5 exists')
    return rows, exact_freq


def base5_countercontrol():
    """K4: one fair five-valued symbol per slot. Exact matches must be found."""
    out = {}
    for n in (1, 2):
        matches = chains = 0
        for D0, D1 in enumerate_chains(n, 5):
            chains += 1
            for cl in class_analysis(n, D0, D1, 5):
                if cl['first_mismatch'] is None:
                    matches += 1
                    check(cl['chi'] == 0, 'K4 exact match has eigenvalue 4')
        out[f'n{n}'] = {'chains': chains, 'classes_matching_(4/5)^n_for_all_n<=|C|': matches}
    check(out['n1']['classes_matching_(4/5)^n_for_all_n<=|C|'] >= 1, 'K4 base-5 countercontrol finds an exact match')
    for n in (1, 2):
        check(out[f'n{n}']['chains'] == comb(5 + 2 * n - 1, 2 * n - 1) ** n, 'K4 chain count equals C(2n+4,2n-1)^n')
    exact = {'n': 1, 'init': {0: Q(1)}, 'D': {1: {(0, 0): QUANTUM}, 0: {(0, 0): 1 - QUANTUM}}}
    for h in range(1, 13):
        check(chain_tv(exact, h) == 0, 'K3 exact base-5 source gives zero TV')
    out['K3_zero_tv_through'] = 12
    return out


def dense(chain):
    n = chain['n']
    D0 = [[Q(0)] * n for _ in range(n)]
    D1 = [[Q(0)] * n for _ in range(n)]
    for g, M in ((0, D0), (1, D1)):
        for (i, j), p in chain['D'][g].items():
            M[i][j] += p
    return D0, D1


# ---------- K2: the retained-seed reset in rescaled-cell coordinates ----------

def retained_seed_runs(B, h):
    """Record -> (seed count, run left end L, run end R) in coordinates rescaled to the record's exact
    quantum interval. A run is the contiguous set of consistent tB-bit seed cells."""
    out = {}
    F = 1 << B
    cutq = QUANTUM

    def walk(t, L, count, w, rec):
        if t == h:
            out[rec] = (count, L, L + count * w)
            return
        sub = w / F
        tot = count * F
        # subcells with left end below the cut agree
        if cutq <= L:
            j = 0
        else:
            x = (cutq - L) / sub
            j = -((-x.numerator) // x.denominator)        # ceil
            j = min(j, tot)
        walk(t + 1, L / cutq, j, sub / cutq, rec + (1,))
        walk(t + 1, (L + j * sub - cutq) / (1 - cutq), tot - j, sub / (1 - cutq), rec + (0,))
    walk(0, Q(0), 1, Q(1), ())
    return out


def qmass(rec):
    k = sum(rec)
    return QUANTUM ** k * (1 - QUANTUM) ** (len(rec) - k)


def retained_seed_tv_gap(B, h):
    runs = retained_seed_runs(B, h)
    scale = 1 << (B * h)
    tv = overlap = Q(0)
    for rec, (count, L, R) in runs.items():
        q = qmass(rec)
        tv += abs(Q(count, scale) - q)
        overlap += q * max(Q(0), min(Q(1), R) - max(Q(0), L))
    check(sum(c for c, _, _ in runs.values()) == scale, 'K2 retained-seed law normalized')
    return tv / 2, 1 - overlap


def retained_seed_reproduction(v7):
    ref = v7['class_statement']['limiting_counterexample_retained_seed_reset']
    n = 0
    for B, hmax in ((2, 8), (3, 6), (4, 5)):
        e = ref['B' + str(B)]
        for h in range(1, hmax + 1):
            tv, gap = retained_seed_tv_gap(B, h)
            shown = str(tv) if B == 4 else display(tv)
            check(shown == e['tv_by_h'][str(h)], 'K2 retained-seed TV equals a2_depth_v7')
            check(str(gap) == e['coupling_gap_exact_by_h'][str(h)], 'K2 retained-seed coupling gap equals a2_depth_v7')
            n += 2
    for h in (8, 12, 16):
        tv, _ = retained_seed_tv_gap(4, h)
        check(display(tv) == ref['B4_tv_display_h8_12_16'][str(h)], 'K2 retained-seed B=4 display equals a2_depth_v7')
        n += 1
    k6 = 0
    p4 = Q(-((-4 * 16) // 5), 16)     # read 1 of the reset with B=4: ceil(4*16/5)/16
    check(str(p4) == ref['memoryless_B4_nearest_dyadic'], 'K6 RS(4,1) is the memoryless 4-bit reset')
    check(tv_iid(p4, 64) == tv_product(p4, p4, 64), 'K6 iid and alternating engines agree')
    check(display(tv_iid(p4, 4096)) == ref['memoryless_B4_tv_h4096_display'],
          'K6 RS(4,1) T(4096) equals a2_depth_v7 memoryless value')
    k6 += 3
    return n, k6


# ---------- the restarted family RS(B,k) ----------

def block_law(B, k):
    runs = retained_seed_runs(B, k)
    scale = 1 << (B * k)
    return {rec: Q(c, scale) for rec, (c, _, _) in runs.items()}


def bc_enclosure(law):
    lo = hi = Q(0)
    for rec, p in law.items():
        x = p * qmass(rec)
        lo += root_lo(x)
        hi += root_hi(x)
    check(lo <= hi <= 1, 'K7 Bhattacharyya enclosure')
    return lo, hi


def tv_of(law):
    return sum((abs(p - qmass(rec)) for rec, p in law.items()), Q(0)) / 2


def product_law(law, n):
    out = {(): Q(1)}
    for _ in range(n):
        out = {r + s: p * q for r, p in out.items() for s, q in law.items()}
    return out


def floor_q(x):
    return x.numerator // x.denominator


def least_power_below(x, level):
    """Least n >= 1 with x^n < level, for 0 <= x < 1, by exact doubling and bisection."""
    check(0 <= x < 1, 'K7 power-rule base in [0,1)')
    hi = 1
    while x ** hi >= level:
        hi *= 2
    lo = hi // 2                      # x^lo >= level, or lo = 0
    while hi - lo > 1:
        m = (lo + hi) // 2
        if x ** m < level:
            hi = m
        else:
            lo = m
    check(x ** hi < level and (hi == 1 or x ** (hi - 1) >= level), 'K7 power-rule depth minimal')
    return hi


def ceiling_rounded(B):
    """Agreement of RS(B,1), the ceiling-rounded B-bit reset: ceil(4*2^B/5)/2^B."""
    return Q(-((-4 * (1 << B)) // 5), 1 << B)


def nearest_dyadic(B):
    """The multiple of 2^-B nearest to 4/5 (never a tie, since 4*2^B/5 is not a half-integer)."""
    K = 1 << B
    lo = Q((4 * K) // 5, K)
    hi = lo + Q(1, K)
    check(abs(lo - QUANTUM) != abs(hi - QUANTUM), 'nearest dyadic unique')
    return lo if abs(lo - QUANTUM) < abs(hi - QUANTUM) else hi


def memoryless_crossing(p):
    """Exact first depth with T > 1/2 for the memoryless reset with agreement p at every read."""
    hi = 1
    while tv_iid(p, hi) <= HALF:
        hi *= 2
    lo = hi // 2
    while hi - lo > 1:
        m = (lo + hi) // 2
        if tv_iid(p, m) > HALF:
            hi = m
        else:
            lo = m
    check(tv_iid(p, hi) > HALF and (hi == 1 or tv_iid(p, hi - 1) <= HALF), 'memoryless exact crossing located')
    return p, hi


def power_rule_lower(bc, n):
    """Post-plan power-rule lower bound: T(nk) >= 1 - BC_k^n for n independent blocks. The depth search, the k=1
    exact check and the n*k<=16 product check all use this one function."""
    return 1 - bc ** n


def least_n_above(f, level):
    """Least n >= 1 with f(n) > level, for f nondecreasing in n, by exact doubling and bisection."""
    hi = 1
    while f(hi) <= level:
        hi *= 2
    lo = hi // 2
    while hi - lo > 1:
        m = (lo + hi) // 2
        if f(m) > level:
            hi = m
        else:
            lo = m
    return hi


def power_rule_exact_k1(p, bl, bh, Tk, n_hp, n_half):
    """K7 for the post-plan power rule at k=1: exact T(h) from the binomial engine against the shared power-rule
    lower bound, sqrt(1-BC_lower^(2h)) and h*T_1. The depths checked do not depend on the power-rule depth: every
    h <= 600, every multiple of 1024 up to twice the preregistered depth n_half, and n_hp-1..n_hp+1."""
    top = 2 * n_half
    hs = sorted(set(range(1, 601)) | set(range(1024, top + 1, 1024)) | {max(1, n_hp - 1), n_hp, n_hp + 1})
    for h in hs:
        T = tv_iid(p, h)
        check(T >= power_rule_lower(bh, h), 'K7 exact T(h) >= power-rule lower bound at k=1')
        check(T * T <= 1 - (bl * bl) ** h and T <= h * Tk, 'K7 exact T(h) inside power-rule upper bounds at k=1')
    return {'depths_checked': len(hs), 'all_h_up_to': 600, 'max_h': hs[-1]}


def family(Bs=(2, 3, 4), kmax=16):
    rows = {}
    encl = {}
    for B in Bs:
        base_half = None
        p_mem, cross_mem = memoryless_crossing(ceiling_rounded(B))
        p_near, cross_near = memoryless_crossing(nearest_dyadic(B))
        lo_n = Q((4 << B) // 5, 1 << B)
        p_other = lo_n + Q(1, 1 << B) if p_near == lo_n else lo_n
        p_other, cross_other = memoryless_crossing(p_other)
        # TV of Bernoulli(p)^h against Bernoulli(4/5)^h is nondecreasing as p moves away from 4/5 on either side
        # (monotone likelihood ratio), so among i.i.d. B-bit laws the first crossing is maximal at a neighbour.
        check(cross_near >= cross_other, 'nearest-dyadic i.i.d. reset crosses no earlier than the other neighbour')
        check(all(abs(Q(x, 1 << B) - QUANTUM) >= abs(p_near - QUANTUM) for x in range((1 << B) + 1)),
              'nearest dyadic minimal over 2^-B Z')            # the best i.i.d. B-bit memoryless law
        for k in range(1, kmax + 1):
            law = block_law(B, k)
            check(len(law) == 1 << k and all(len(rec) == k for rec in law),
                  'scope: block-law record length equals member k')
            check(sum(law.values()) == 1, 'family block law normalized')
            Tk = tv_of(law)
            check(Tk > 0, 'family dyadic block law differs from quantum')
            if B >= 2:
                check(Tk < Q(1, (1 << B) - 2), 'K6 block TV below the all-depth retained-seed bound')
            bl, bh = bc_enclosure(law)
            encl[B, k] = (bl, bh)
            check(1 - bh <= Tk and bl * bl <= 1 - Tk * Tk, 'K7 Le Cam inequalities between TV and BC')
            c_low, c_up = 1 - bh, 1 - bl          # c_low <= 1-BC <= c_up
            null_q = sum((qmass(r) for r, p in law.items() if p == 0), Q(0))
            n_states = sum(1 << (j * (B + 1)) for j in range(k))   # (phase j, j*B seed bits, j record bits)
            entry = {'memory_bits_upper': (k - 1) * B + (k - 1) + (k - 1).bit_length(),
                     'block_tv': display(Tk), 'block_tv_exact_sha256': digest(Tk),
                     'one_minus_bc_lower': display(c_low, 20), 'one_minus_bc_upper': display(c_up, 20),
                     'persistent_states': n_states}
            check((1 << entry['memory_bits_upper']) >= n_states, 'memory column bounds the persistent-state count')
            if c_low > 0:
                n_half = floor_q(1 / c_low) + 1                   # n*c > 1  =>  T(nk) >= nc/(1+nc) > 1/2
                check(n_half * c_low > 1 and (n_half - 1) * c_low <= 1, 'K7 half-depth minimal for its rule')
                n_t1 = floor_q(TENTH / Tk) if Tk > 0 else None  # n*T_k <= 1/10
                n_t2 = floor_q(1 / (200 * c_up))                  # sqrt(2 n c_up) <= 1/10
                check(n_t1 * Tk <= TENTH < (n_t1 + 1) * Tk, 'K7 tenth-depth maximal (coupling rule)')
                check(200 * n_t2 * c_up <= 1 < 200 * (n_t2 + 1) * c_up, 'K7 tenth-depth maximal (Hellinger rule)')
                n_tenth = max(n_t1, n_t2)
                entry['certified_T_above_half_for_h_at_least'] = k * n_half
                entry['certified_T_at_most_tenth_for_h_at_most'] = k * n_tenth
                if k == 1:
                    base_half = k * n_half
                entry['half_depth_ratio_to_k1'] = display(Q(k * n_half, base_half), 6)
                entry['half_depth_per_memory_bit'] = (display(Q(k * n_half, entry['memory_bits_upper']), 3)
                                                      if entry['memory_bits_upper'] else None)
                # Power rule (post-plan): T(nk) >= 1 - BC^n and T(nk) <= sqrt(1 - BC^(2n)) or n*T_k.
                n_hp = least_n_above(lambda n: power_rule_lower(bh, n), HALF)
                check(power_rule_lower(bh, n_hp) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp - 1) <= HALF),
                      'K7 power-rule depth is the least n with lower bound above 1/2')
                n_lp = max(least_power_below(bl * bl, Q(3, 4)) - 1, floor_q(HALF / Tk))
                check(n_lp * Tk <= HALF or (bl * bl) ** n_lp >= Q(3, 4), 'K7 half-upper depth valid')
                # Independent constraints on the power-rule depth (post-recheck), from code paths it does not share:
                # the separately coded preregistered rule (1 - BC^n >= nc/(1+nc), so the power depth is no later),
                # and the upper certificates computed from BC_lower and T_k (T <= 1/2 certified only earlier).
                check(n_hp <= n_half, 'K7 power-rule depth no later than the preregistered depth')
                check(n_lp < n_hp, 'K7 upper and lower half-level certificates consistent')
                post = {'power_rule_T_above_half_for_h_at_least': k * n_hp,
                        'power_rule_T_at_most_half_for_h_at_most': k * n_lp}
                if k == 1:
                    check(law[(1,)] == p_mem, 'K6 RS(B,1) is the ceiling-rounded B-bit reset')
                    check(k * n_lp < cross_mem <= k * n_hp, 'K7 power rule brackets the exact ceiling-rounded crossing')
                    post['power_rule_exact_checks_at_k1'] = power_rule_exact_k1(p_mem, bl, bh, Tk, n_hp, n_half)
                else:
                    post['certified_fails_before_nearest_dyadic_reset'] = k * n_hp < cross_near
                    post['certified_outlasts_nearest_dyadic_reset'] = k * n_lp >= cross_near
                    post['certified_fails_before_ceiling_rounded_reset'] = k * n_hp < cross_mem
                    post['certified_outlasts_ceiling_rounded_reset'] = k * n_lp >= cross_mem
                entry['post_plan'] = post
            else:
                entry['certified_T_above_half_for_h_at_least'] = None
            entry.setdefault('post_plan', {})['quantum_mass_of_source_null_records'] = display(null_q)
            runs = {}
            for r in (5, 8):
                if k >= r:
                    ps = sum((p for rec, p in law.items() if rec[-r:] == (0,) * r), Q(0))
                    check(sum((qmass(rec) for rec in law if rec[-r:] == (0,) * r), Q(0)) == (1 - QUANTUM) ** r,
                          'diagnostic trailing-run quantum mass')
                    runs[str(r)] = {'source': display(ps), 'quantum': display((1 - QUANTUM) ** r)}
            entry.setdefault('post_plan', {})['mass_of_records_ending_in_r_disagreements'] = runs
            # K7: exact product TV inside the bracket where enumerable.
            n = 1
            while n * k <= 16:
                T = tv_of(product_law(law, n)) if n > 1 else Tk
                lower = n * c_low / (1 + n * c_low)
                check(lower <= T <= n * Tk, 'K7 exact product TV inside certified bracket')
                check(T * T <= 2 * n * c_up, 'K7 exact product TV inside Hellinger upper bound')
                check(T >= power_rule_lower(bh, n) and T * T <= 1 - (bl * bl) ** n,
                      'K7 exact product TV inside power-rule bracket')
                n += 1
            rows[f'B{B}_k{k}'] = entry
        rows[f'B{B}_memoryless_comparators_post_plan'] = {
            'ceiling_rounded_reset_RS_B_1': {'agreement': str(p_mem), 'exact_first_depth_T_above_half': cross_mem},
            'nearest_dyadic_reset': {'agreement': str(p_near), 'exact_first_depth_T_above_half': cross_near},
            'other_neighbour_reset_post_recheck': {'agreement': str(p_other), 'exact_first_depth_T_above_half': cross_other}}
    return rows, encl


# ---------- K8: explicit state machine for RS(B,k) ----------

class RestartController:
    """Persistent state: phase j in 0..k-1, retained seed integer of j*B bits, within-block record."""

    def __init__(self, B, k, clear=True):
        self.B, self.k, self.clear = B, k, clear
        self.j, self.seed, self.rec = 0, 0, ()

    def step(self, u):
        lo, hi = Q(0), Q(1)
        for g in self.rec:                     # exact quantum interval of the within-block record
            m = lo + QUANTUM * (hi - lo)
            lo, hi = (lo, m) if g else (m, hi)
        cut = lo + QUANTUM * (hi - lo)
        seed = (self.seed << self.B) | u
        bits = (len(self.rec) + 1) * self.B
        g = 1 if Q(seed, 1 << bits) < cut else 0     # left end of the known cell below the cut
        self.seed, self.rec, self.j = seed, self.rec + (g,), self.j + 1
        if self.clear and self.j == self.k:
            self.j, self.seed, self.rec = 0, 0, ()
        return g


def machine_law(B, k, h, clear=True):
    law = {}
    for word in range(1 << (B * h)):
        c = RestartController(B, k, clear)
        rec = tuple(c.step((word >> (B * (h - 1 - t))) & ((1 << B) - 1)) for t in range(h))
        law[rec] = law.get(rec, 0) + 1
    return {r: Q(v, 1 << (B * h)) for r, v in law.items()}


def machine_chain(B, k):
    """RS(B,k) as a finite time-homogeneous chain over its persistent states."""
    states = []
    for j in range(k):
        for rec in product((1, 0), repeat=j):
            for seed in range(1 << (j * B)):
                states.append((j, seed, rec))
    idx = {s: i for i, s in enumerate(states)}
    D = {0: {}, 1: {}}
    for (j, seed, rec) in states:
        for u in range(1 << B):
            c = RestartController(B, k)
            c.j, c.seed, c.rec = j, seed, rec
            g = c.step(u)
            key = (idx[j, seed, rec], idx[c.j, c.seed, c.rec])
            D[g][key] = D[g].get(key, Q(0)) + Q(1, 1 << B)
    return {'n': len(states), 'init': {idx[0, 0, ()]: Q(1)}, 'D': D}


def restart_mechanics():
    out = {}
    for B, k, h in ((2, 2, 8), (2, 3, 7), (3, 2, 5), (4, 3, 4)):
        law = machine_law(B, k, h)
        blk = block_law(B, k)
        full, rem = divmod(h, k)
        pred = product_law(blk, full)
        if rem:
            tail = block_law(B, rem)
            pred = {r + s: p * q for r, p in pred.items() for s, q in tail.items()}
        check(all(law.get(r, 0) == pred.get(r, 0) for r in product((1, 0), repeat=h)),
              'K8 state machine equals product of block laws')
        out[f'B{B}_k{k}_h{h}'] = 'equal'
    # without clearing, the state machine is the a2_depth_v7 reset and equals the h-read law
    for B, h in ((2, 6), (3, 4)):
        ml, bl = machine_law(B, 1, h, clear=False), block_law(B, h)
        check(all(ml.get(r, 0) == bl[r] for r in product((1, 0), repeat=h)), 'K6 unrestarted machine is the retained-seed reset')
    out['unrestarted_equals_retained_seed'] = [[2, 6], [3, 4]]
    chains = {}
    for B, k in ((2, 2), (2, 3), (3, 2)):
        ch = machine_chain(B, k)
        for h in range(1, 8):
            law = chain_law(ch, h)
            full, rem = divmod(h, k)
            pred = product_law(block_law(B, k), full)
            if rem:
                tail = block_law(B, rem)
                pred = {r + s: p * q for r, p in pred.items() for s, q in tail.items()}
            check(all(law.get(r, 0) == pred.get(r, 0) for r in product((1, 0), repeat=h)),
                  'K8 chain form equals product of block laws')
        check(ch['n'] == sum(1 << (j * (B + 1)) for j in range(k)), 'memory column state count equals explicit chain')
        D0, D1 = dense(ch)
        cls = class_analysis(ch['n'], D0, D1, 1 << B)
        for cl in cls:
            check(cl['first_mismatch'] is not None and cl['chi'] != 0, 'step4 RS chain mismatch')
        chains[f'B{B}_k{k}'] = {'states': ch['n'], 'closed_classes': len(cls),
                                'class_sizes': [cl['size'] for cl in cls],
                                'least_mismatch': [cl['first_mismatch'] for cl in cls],
                                'stationary_agreement_frequency': [str(cl['freq']) for cl in cls]}
    out['step4_on_RS_chains'] = chains
    return out


# ---------- second concrete class member: floor-truncated rescaling decoder (post-review) ----------

def floor_decoder_chain(B, m):
    """State r in [0, 2^m): append B fresh bits, v = r*2^B + u; agree iff v < ceil(4*2^(m+B)/5); rescale the
    left end by 5/4 (agree) or 5 (disagree) and truncate to m bits. A finite-state, time-independent member of the
    bounded-state class; it reads the quantum cut."""
    K = 1 << (m + B)
    c = -((-4 * K) // 5)
    D = {0: {}, 1: {}}
    for r in range(1 << m):
        for u in range(1 << B):
            v = (r << B) + u
            if v < c:
                g, r2 = 1, (5 * v) // (4 << B)
            else:
                g, r2 = 0, (5 * v - 4 * K) >> B
            check(0 <= r2 < (1 << m), 'floor decoder state in range')
            D[g][r, r2] = D[g].get((r, r2), Q(0)) + Q(1, 1 << B)
    return {'n': 1 << m, 'init': {r: Q(1, 1 << m) for r in range(1 << m)}, 'D': D}


def floor_decoder_member():
    out = {}
    for B in (2, 3, 4):
        for m in range(1, 6):
            ch = floor_decoder_chain(B, m)
            D0, D1 = dense(ch)
            cls = class_analysis(ch['n'], D0, D1, 1 << B)
            for cl in cls:
                check(cl['first_mismatch'] is not None and cl['chi'] != 0, 'step4 floor-decoder chain mismatch')
            out[f'B{B}_m{m}'] = {'states': ch['n'], 'class_sizes': [cl['size'] for cl in cls],
                                 'least_mismatch': [cl['first_mismatch'] for cl in cls],
                                 'stationary_agreement_frequency': [str(cl['freq']) for cl in cls]}
    return out


# ---------- independent certificate audit (post-recheck-2) ----------
# Separately written: integer-only block laws in absolute coordinates, integer square-root summation for BC,
# integer exact TV, and every reported depth recomputed from its stated definition. Shares no helper with
# retained_seed_runs, block_law, bc_enclosure, root_lo/root_hi, power_rule_lower, least_n_above,
# least_power_below or tv_of. Reads only the reported family entries.

AUDIT_R = 1 << 200


def audit_block_counts(B, k):
    """Record -> seed count over 2^(B*k), from integer intervals: the quantum interval of a record of length t is
    [L, H) / 5^t, and agree at read t+1 iff prefix * 5^(t+1) < (L + 4H) * 2^((t+1)B)."""
    out = {}

    def go(t, a, b, L, H, rec):
        if t == k:
            out[rec] = b - a
            return
        a2, b2 = a << B, b << B
        C = L + 4 * H
        num, den = C << ((t + 1) * B), 5 ** (t + 1)
        m = min(max(-((-num) // den), a2), b2)
        go(t + 1, a2, m, 5 * L, C, rec + (1,))
        go(t + 1, m, b2, C, 5 * H, rec + (0,))
    go(0, 0, 1, 0, 1, ())
    if sum(out.values()) != 1 << (B * k) or len(out) != 1 << k:
        raise Void('audit block law complete')
    return out


def audit_bc_and_tv(B, k, counts):
    """Integer enclosure [Lnum, Unum]/Dn of the Bhattacharyya coefficient and exact TV as Tnum/Tden."""
    S, F = 1 << (B * k), 5 ** k
    Dn = AUDIT_R * S * F
    Lnum = Unum = 0
    tnum = 0
    for rec, c in counts.items():
        a = sum(rec)
        s = isqrt(c * F * S * AUDIT_R * AUDIT_R)
        Lnum += (1 << a) * s
        Unum += (1 << a) * (s + (0 if s * s == c * F * S * AUDIT_R * AUDIT_R else 1))
        tnum += abs(c * F - (4 ** a) * S)
    return Lnum, Unum, Dn, tnum, 2 * S * F


def audit_least(pred, guess):
    """Least n >= 1 with pred(n), for pred monotone false-then-true, starting from an estimate; exact steps."""
    n = max(1, guess)
    while n > 1 and pred(n - 1):
        n -= 1
    while not pred(n):
        n += 1
    return n


def audit_estimate(x, target):
    """Float estimate of log(target)/log(x) used only to seed the exact search."""
    from math import log, ceil
    if x <= 0 or x >= 1:
        return 1
    return max(1, int(ceil(log(target) / log(x))))


def audit_product_tv(B, k, counts, n):
    S, F = 1 << (B * k), 5 ** k
    items = list(counts.items())
    tot = 0
    for combo in product(items, repeat=n):
        c, a = 1, 0
        for rec, ci in combo:
            c *= ci
            a += sum(rec)
        tot += abs(c * F ** n - (4 ** a) * S ** n)
    return Q(tot, 2 * (S * F) ** n)


def plan_pin_crosschecks():
    """The PLAN.md pin must equal PROVENANCE.json's plan_sha256 and the PLAN.md blob of the plan commit. A source
    that is absent in the running environment (a copy outside the repository) is recorded as unavailable; a
    mismatch is a control failure."""
    status = {}
    try:
        with open(PROVENANCE, 'rb') as f:
            prov = json.loads(f.read())
    except OSError:
        status['provenance_plan_sha256'] = 'unavailable'
    else:
        check(prov.get('plan_sha256') == PLAN_SHA256 and prov.get('plan_commit') == PLAN_COMMIT,
              'scope: plan pin equals PROVENANCE plan_sha256')
        status['provenance_plan_sha256'] = 'matches'
    try:
        p = subprocess.run(['git', '-C', GIT_DIR, 'show', PLAN_COMMIT + ':./PLAN.md'], capture_output=True)
    except OSError:
        p = None
    if p is None or p.returncode != 0:
        status['plan_commit_blob'] = 'unavailable'
    else:
        check(hashlib.sha256(p.stdout).hexdigest() == PLAN_SHA256, 'scope: plan pin equals the PLAN.md blob of 1dfec979')
        status['plan_commit_blob'] = 'matches'
    return status


def preregistered_scope():
    """The RS scope and thresholds as preregistered, parsed from PLAN.md after checking its pinned SHA-256; not
    taken from any code default."""
    with open(PLAN, 'rb') as f:
        raw = f.read()
    check(hashlib.sha256(raw).hexdigest() == PLAN_SHA256, 'scope: pinned PLAN.md hash')
    pin_status = plan_pin_crosschecks()
    text = raw.decode()
    m = re.search(r'\*\*The family RS\(B,k\), B in \{([0-9,]+)\}, k = 1\.\.([0-9]+)\*\*', text)
    check(m is not None, 'scope: preregistered family line present in PLAN.md')
    Bs = tuple(int(x) for x in m.group(1).split(','))
    kmax = int(m.group(2))
    check('T(h) > 1/2 for every h >= k*n_half' in text and 'T(h) <= 1/10 for every h <= k*n_tenth' in text,
          'scope: preregistered thresholds present in PLAN.md')
    check(HALF == Q(1, 2) and TENTH == Q(1, 10), 'scope: threshold constants equal the preregistered 1/2 and 1/10')
    keys = {f'B{B}_k{k}' for B in Bs for k in range(1, kmax + 1)}
    check(len(keys) == 48, 'scope: preregistered set has 48 members')
    return Bs, kmax, keys, pin_status


def independent_audit(fam, encl, Bs=(2, 3, 4), kmax=16):
    n_members = n_cert = 0
    audited = set()
    half_reached = set()
    for B in Bs:
        for k in range(1, kmax + 1):
            check(f'B{B}_k{k}' in fam and (B, k) in encl, 'scope: audited member present in reported family')
            e = fam[f'B{B}_k{k}']
            audited.add(f'B{B}_k{k}')
            pp = e['post_plan']
            counts = audit_block_counts(B, k)
            Lnum, Unum, Dn, tnum, tden = audit_bc_and_tv(B, k, counts)
            check(digest(Q(tnum, tden)) == e['block_tv_exact_sha256'], 'audit block TV equals reported')
            bl_rep, bh_rep = encl[B, k]                       # the enclosure every reported depth was built from
            check(Q(Lnum, Dn) <= bh_rep and bl_rep <= Q(Unum, Dn),
                  'audit independent BC enclosure overlaps the reported enclosure')
            # depths recomputed from their stated definitions
            cl = Dn - Unum                                    # Dn * (1 - BC_upper)
            n_half = Dn // cl + 1
            n_hp = audit_least(lambda n: 2 * Unum ** n < Dn ** n, audit_estimate(Unum / Dn, 0.5))
            n1 = audit_least(lambda n: 4 * Lnum ** (2 * n) < 3 * Dn ** (2 * n), audit_estimate((Lnum / Dn) ** 2, 0.75)) - 1
            n_lp = max(n1, tden // (2 * tnum))
            n_tenth = max(tden // (10 * tnum), Dn // (200 * (Dn - Lnum)))
            for field, val in (('certified_T_above_half_for_h_at_least', k * n_half),
                               ('certified_T_at_most_tenth_for_h_at_most', k * n_tenth)):
                check(e[field] == val, 'audit recomputed depth equals reported (' + field + ')')
            for field, val in (('power_rule_T_above_half_for_h_at_least', k * n_hp),
                               ('power_rule_T_at_most_half_for_h_at_most', k * n_lp)):
                check(pp[field] == val, 'audit recomputed depth equals reported (' + field + ')')
            # certificate-level exact checks wherever exact TV is enumerable, at the depths as reported
            n_hp, n_half = pp['power_rule_T_above_half_for_h_at_least'] // k, e['certified_T_above_half_for_h_at_least'] // k
            n_lp, n_tenth = pp['power_rule_T_at_most_half_for_h_at_most'] // k, e['certified_T_at_most_tenth_for_h_at_most'] // k
            n = 1
            while n * k <= 16:
                T = Q(tnum, tden) if n == 1 else audit_product_tv(B, k, counts, n)
                if n >= n_hp or n >= n_half:
                    check(T > HALF, 'audit certificate T>1/2 contradicted by exact TV')
                    n_cert += 1
                    half_reached.add(f'B{B}_k{k}')
                if n <= n_lp:
                    check(T <= HALF, 'audit certificate T<=1/2 contradicted by exact TV')
                    n_cert += 1
                if n <= n_tenth:
                    check(T <= TENTH, 'audit certificate T<=1/10 contradicted by exact TV')
                    n_cert += 1
                n += 1
            if k == 1:
                p = Q(counts[(1,)], 1 << B)
                half_reached.add(f'B{B}_k{k}')
                for nn, up in ((n_hp, False), (n_half, False), (n_lp, True)):
                    if nn >= 1:
                        T = tv_iid(p, nn)
                        check((T <= HALF if up else T > HALF), 'audit k=1 certificate contradicted by exact TV')
                        n_cert += 1
                if n_tenth >= 1:
                    check(tv_iid(p, n_tenth) <= TENTH, 'audit k=1 certificate T<=1/10 contradicted by exact TV')
                    n_cert += 1
            n_members += 1
    return {'members': n_members, 'certificates_checked_against_exact_tv': n_cert,
            'members_with_T_above_half_certificate_checked_against_exact_tv': sorted(half_reached)}, audited


# ---------- main ----------

def run():
    v7 = load_v7()
    chain, pa, pb, K = memoryless_controller(v7)
    for h in range(1, 13):
        check(chain_tv(chain, h) == tv_product(pa, pb, h), 'K1 generic engine equals product engine (h<=12)')
    D0, D1 = dense(chain)
    exec_cls = class_analysis(4, D0, D1, K)
    for cl in exec_cls:
        check(cl['first_mismatch'] is not None and cl['chi'] != 0, 'step4 executed controller mismatch')
    k2, k6 = retained_seed_reproduction(v7)
    census, exact_freq = step4_census()
    cc = base5_countercontrol()
    floor_member = floor_decoder_member()
    mech = restart_mechanics()
    fam, encl = family()
    sB, skmax, scope_keys, pin_status = preregistered_scope()
    reported_keys = {key for key in fam if '_k' in key}
    check(reported_keys == scope_keys and set(f'B{B}_k{k}' for (B, k) in encl) == scope_keys,
          'scope: reported members equal the preregistered B x k set')
    audit = independent_audit(fam, encl)
    audit, audited_keys = audit
    check(audited_keys == scope_keys and audit['members'] == len(scope_keys),
          'scope: audited members equal the preregistered B x k set')
    audit['scope'] = {'source': 'PLAN.md, SHA-256 pinned', 'B': list(sB), 'k': [1, skmax],
                      'members': len(scope_keys), 'thresholds': ['1/2', '1/10'], 'plan_pin_crosschecks': pin_status}
    members = {k: v for k, v in fam.items() if 'memoryless' not in k}
    n_floor_classes = sum(len(v['class_sizes']) for v in floor_member.values())
    certified = {k: v['certified_T_above_half_for_h_at_least'] for k, v in members.items()}
    all_cert = all(v is not None for v in certified.values())
    n_chains = sum(r['chains'] for r in census.values())
    n_classes = sum(r['closed_classes'] for r in census.values())
    n_freq = sum(r['classes_with_exact_frequency_4/5'] for r in census.values())
    worst = max(r['largest_least_mismatch_index'] for r in census.values())
    class_verdict = ('BOUNDED_STATE_CLASS_NO_ESCAPE: every bounded-state controller with B fair fresh bits per slot '
                     'and a time-independent update has T(h)->1 on this protocol (proof in REPORT.md); finite step '
                     f'checked on {n_chains} enumerated dyadic chains ({n_classes} closed classes, {n_freq} with '
                     f'exact stationary frequency 4/5, least run mismatch at most n={worst}), on the executed '
                     f'controller chain and on three RS chains (post-review: also on {len(floor_member)} '
                     f'floor-truncated decoder chains, {n_floor_classes} closed classes); base-5 countercontrol '
                     'matches exactly')
    by_B = {}
    for key, v in members.items():
        B = int(key[1:key.index('_')])
        by_B.setdefault(B, []).append((int(key[key.index('k') + 1:]), v))
    pre, post = [], []
    for B in sorted(by_B):
        rows = sorted(by_B[B])
        comp = fam[f'B{B}_memoryless_comparators_post_plan']
        near = comp['nearest_dyadic_reset']
        ceil_ = comp['ceiling_rounded_reset_RS_B_1']
        pk, pv = max(((k, v['certified_T_above_half_for_h_at_least']) for k, v in rows), key=lambda x: (x[1], -x[0]))
        pre.append(f'B={B}: each k=1..{rows[-1][0]} certified T>1/2 beyond a finite depth (nc/(1+nc) rule), '
                   f'largest h={pv} (k={pk})')
        best_k, best = min(((k, v['post_plan']['power_rule_T_above_half_for_h_at_least']) for k, v in rows),
                           key=lambda x: (x[1], x[0]))
        worst_k, worst = max(((k, v['post_plan']['power_rule_T_above_half_for_h_at_least']) for k, v in rows),
                             key=lambda x: (x[1], -x[0]))
        before = [k for k, v in rows if k > 1 and v['post_plan']['certified_fails_before_nearest_dyadic_reset']]
        outlast = [k for k, v in rows if k > 1 and v['post_plan']['certified_outlasts_nearest_dyadic_reset']]
        cn = near['exact_first_depth_T_above_half']
        check(before == [k for k, v in rows if k > 1 and v['post_plan']['power_rule_T_above_half_for_h_at_least'] < cn]
              and outlast == [k for k, v in rows if k > 1 and v['post_plan']['power_rule_T_at_most_half_for_h_at_most'] >= cn],
              'comparison flags recomputed from stored depths and the nearest-dyadic crossing')
        undet = [k for k, v in rows if k > 1 and k not in before and k not in outlast]
        post.append(f'B={B}: power-rule depths from h={best} (k={best_k}, {dict(rows)[best_k]["memory_bits_upper"]} '
                    f'memory bits) to h={worst} (k={worst_k}); nearest-dyadic i.i.d. reset (agreement '
                    f'{near["agreement"]}; best i.i.d. B-bit law at this B by first crossing, other neighbour '
                    f'{comp["other_neighbour_reset_post_recheck"]["agreement"]} crossing at '
                    f'h={comp["other_neighbour_reset_post_recheck"]["exact_first_depth_T_above_half"]}; not compared '
                    f'with record-dependent or time-varying controllers) first exceeds T=1/2 at h={cn} (exact); '
                    f'certified to fail before it for k in {before}; certified to outlast it for k in {outlast}; '
                    f'ordering undetermined for k in {undet}; ceiling-rounded reset RS(B,1) (agreement '
                    f'{ceil_["agreement"]}) first exceeds 1/2 at h={ceil_["exact_first_depth_T_above_half"]}')
    family_verdict = (('RS_FAMILY_FINITE_FAILURE_DEPTH_EVERY_TESTED_MEMBER: ' if all_cert else
                       'RS_FAMILY_PARTIAL_CERTIFICATION: ') + 'preregistered rule: ' + '; '.join(pre)
                      + ' | post-plan (power rule, exact memoryless comparators): ' + '; '.join(post))
    resource = ('Necessity: with B fair fresh bits per slot and a time-independent update, T(h)->1 whenever the '
                'persistent state set is finite; so a controller keeping T(h) bounded below 1 at every depth needs '
                'the number of persistent states reachable within h slots, from a finite initial support, to grow '
                'without bound in h. Growth is not sufficient by itself: the a2_depth_v7 full-record memoryless '
                'controllers have growing state and T(h)->1. One controller with linearly growing private memory, '
                'the a2_depth_v7 retained-seed reset granted the target cuts, keeps T<=1/(2^B-2) at every depth for '
                'B>=2. The least sufficient growth rate is not determined here.')
    out = {
        'schema': 'oi.a2-bounded-memory-v8.v6',
        'protocol': 'prepare X+, then reads a,X,a,X,...; quantum agreement 4/5 per read; complete public record',
        'class_hypothesis': ('finite persistent state (carrier, private memory, any clock or record registers read); '
                             'time-independent deterministic update from state, one fresh block of B fair bits and '
                             'the setting; any initial law, the preparation read unconstrained'),
        'executed_controller_chain': {'states': 4, 'A': str(pa), 'B': str(pb),
                                      'closed_classes': [{'size': c['size'], 'least_mismatch': c['first_mismatch'],
                                                          'stationary_agreement_frequency': str(c['freq'])}
                                                         for c in exec_cls]},
        'step4_census': census,
        'step4_exact_frequency_examples': exact_freq,
        'family_RS': fam,
        'restart_mechanics': mech,
        'floor_truncated_decoder_member_post_review': floor_member,
        'independent_certificate_audit_post_recheck2': audit,
        'controls': {
            'K1_memoryless_reproduction': 'digest, A, B, exact T(1..4), T digests h<=64 equal; generic engine equal h<=12',
            'K2_retained_seed_values_matched': k2,
            'K6_retained_value_checks': k6,
            'K3_K4_base5': cc,
            'K5_exact_frequency_classes': n_freq,
            'K6': ('the unrestarted state machine equals the retained-seed law (B=2 h=6, B=3 h=4); block TV below '
                   '1/(2^B-2); RS(4,1) is the 13/16 reset and its T(4096) display equals a2_depth_v7'),
            'K7': ('square-root endpoints verified by squaring; Le Cam inequalities; exact product TV inside the '
                   'preregistered and power-rule brackets for n*k<=16; power rule checked against exact T(h) at k=1'),
            'counts': ('census chain counts equal C(2^B+2n-1,2n-1)^n; memory column bounds the persistent-state '
                       'count, which equals the explicit chain size where built'),
            'K8': 'explicit state machine and chain form equal the product of block laws'},
        'display_rule': 'decimal truncation toward zero',
        'scope': ('A2 only. The class theorem covers bounded persistent state with a time-independent update and B '
                  'fair fresh bits per slot, on this protocol; it gives no rate. Not covered: bounded private memory '
                  'with unbounded public state (an unbounded clock or full-record dependence), time-dependent '
                  'updates, growing per-slot blocks, non-dyadic sources, other protocols, A1 or OI. The RS depths '
                  'are certified for the tested members only; no growth law is fitted.'),
        'class_verdict': class_verdict,
        'family_verdict': family_verdict,
        'resource_statement': resource,
    }
    return out


def main():
    try:
        out = run()
    except Void as e:
        print('VOID: ' + str(e))
        sys.exit(2)
    except (KeyError, IndexError, ValueError, TypeError, ZeroDivisionError, StopIteration) as e:
        print('VOID: control failure from an internal inconsistency (' + type(e).__name__ + ')')
        sys.exit(2)
    text = json.dumps(out, sort_keys=True, separators=(',', ':'))
    if '--output' in sys.argv:
        with open(sys.argv[sys.argv.index('--output') + 1], 'w') as f:
            f.write(text + '\n')
    else:
        print(text)


if __name__ == '__main__':
    main()
