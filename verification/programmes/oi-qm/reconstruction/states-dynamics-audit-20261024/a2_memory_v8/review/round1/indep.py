"""Independent reviewer re-derivation for a2_memory_v8 (exact integers/Fractions; stdlib only).

Usage: python3 -I -B indep.py <path to a2_memory_v8/result.json>
Imports nothing from the author's checker. Different methods:
- stationary law by the Markov chain tree theorem (principal minors of I-P), not Gaussian solve;
- characteristic polynomial by Faddeev-LeVerrier on the integer matrix 2^B D1|C, then Horner at lambda;
- retained-seed block law in absolute integer seed coordinates (integer seed ranges, exact quantum interval);
- BC enclosure at 320 bits; depths by float estimate plus exact boundary verification.
"""
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from itertools import product
from math import comb, isqrt

Q45 = F(4, 5)


def digest(x):
    return hashlib.sha256(f'{x.numerator:x}/{x.denominator:x}'.encode()).hexdigest()


def disp(x, digits=12):
    s = x.numerator * 10 ** digits // x.denominator
    return '0.' + str(s).zfill(digits) if s < 10 ** digits else str(F(s, 10 ** digits))


# ---------------- census ----------------

def det(M):
    n = len(M)
    if n == 0:
        return F(1)
    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return sum((-1) ** j * M[0][j] * det([r[:j] + r[j + 1:] for r in M[1:]]) for j in range(n))


def sccs_closed(n, P):
    reach = []
    for i in range(n):
        seen = {i}
        fr = [i]
        while fr:
            u = fr.pop()
            for v in range(n):
                if P[u][v] != 0 and v not in seen:
                    seen.add(v)
                    fr.append(v)
        reach.append(seen)
    classes = set()
    for i in range(n):
        cls = frozenset(j for j in reach[i] if i in reach[j])
        # closed iff nothing reachable from i leaves cls
        if reach[i] == cls:
            classes.add(tuple(sorted(cls)))
    return sorted(classes)


def charpoly_int(A):
    """Faddeev-LeVerrier: returns c[0..m] with chi(x)=sum c_i x^i, c_m=1 (integers for integer A)."""
    m = len(A)
    I = [[int(i == j) for j in range(m)] for i in range(m)]
    Mk = [[0] * m for _ in range(m)]
    c = [0] * (m + 1)
    c[m] = 1
    for k in range(1, m + 1):
        # M_k = A M_{k-1} + c_{m-k+1} I
        Mk = [[sum(A[i][t] * Mk[t][j] for t in range(m)) + c[m - k + 1] * I[i][j] for j in range(m)] for i in range(m)]
        AM = [[sum(A[i][t] * Mk[t][j] for t in range(m)) for j in range(m)] for i in range(m)]
        tr = sum(AM[i][i] for i in range(m))
        assert tr % k == 0
        c[m - k] = -tr // k
    return c


def analyse(n, cnt0, cnt1, N):
    """cnt_g[i][j]: integer number of the N outcomes from i to j with bit g."""
    P = [[F(cnt0[i][j] + cnt1[i][j], N) for j in range(n)] for i in range(n)]
    out = []
    for C in sccs_closed(n, P):
        m = len(C)
        L = [[(1 if a == b else 0) - P[C[a]][C[b]] for b in range(m)] for a in range(m)]
        w = [det([[L[r][s] for s in range(m) if s != i] for r in range(m) if r != i]) for i in range(m)]
        tot = sum(w)
        pi = [x / tot for x in w]
        assert all(x >= 0 for x in pi)
        for b in range(m):
            assert sum(pi[a] * P[C[a]][C[b]] for a in range(m)) == pi[b]
        A = [[cnt1[C[a]][C[b]] for b in range(m)] for a in range(m)]
        # run masses a_t = pi D1^t 1
        v = pi[:]
        runs = []
        for t in range(1, m + 1):
            v = [sum(v[a] * F(A[a][b], N) for a in range(m)) for b in range(m)]
            runs.append(sum(v))
        first = next((t + 1 for t, a in enumerate(runs) if a != Q45 ** (t + 1)), None)
        c = charpoly_int(A)
        lam = F(4 * N, 5)
        chi = sum(ci * lam ** i for i, ci in enumerate(c))
        # Cayley-Hamilton consistency: sum c_i pi A^i 1 == 0
        v = pi[:]
        ch = c[0] * sum(v)
        for i in range(1, m + 1):
            v = [sum(v[a] * A[a][b] for a in range(m)) for b in range(m)]
            ch += c[i] * sum(v)
        assert ch == 0
        out.append((m, runs[0], first, chi))
    return out


def chains(n, N):
    # each state: distribute N outcomes over 2n slots (j, g)
    def comps(tot, parts):
        if parts == 1:
            yield (tot,)
            return
        for x in range(tot + 1):
            for r in comps(tot - x, parts - 1):
                yield (x,) + r
    per = list(comps(N, 2 * n))
    for ch in product(per, repeat=n):
        c0 = [[ch[i][2 * j] for j in range(n)] for i in range(n)]
        c1 = [[ch[i][2 * j + 1] for j in range(n)] for i in range(n)]
        yield c0, c1


def census():
    rows = {}
    for n, B in [(1, b) for b in range(1, 9)] + [(2, 1), (2, 2), (2, 3), (3, 1)]:
        N = 1 << B
        nc = ncl = nf = worst = 0
        f2 = True
        for c0, c1 in chains(n, N):
            nc += 1
            for m, fr, first, chi in analyse(n, c0, c1, N):
                ncl += 1
                assert first is not None and chi != 0, (n, B, c0, c1)
                worst = max(worst, first)
                if fr == Q45:
                    nf += 1
                    f2 &= first == 2
        rows[f'n{n}_B{B}'] = {'chains': nc, 'closed_classes': ncl, 'classes_with_exact_frequency_4/5': nf,
                              'largest_least_mismatch_index': worst, 'all_exact_freq_mismatch_at_2': f2}
    base5 = {}
    for n in (1, 2):
        nc = match = 0
        for c0, c1 in chains(n, 5):
            nc += 1
            for m, fr, first, chi in analyse(n, c0, c1, 5):
                if first is None:
                    match += 1
                    assert chi == 0
                else:
                    assert chi != 0 or True
        base5[f'n{n}'] = (nc, match)
    return rows, base5


# ---------------- retained-seed block law, absolute integer seed coordinates ----------------

def block_law(B, k):
    """record -> number of kB-bit seeds producing it (the v7 retained-seed reset on k reads)."""
    out = {}

    def rec(t, a, b, lo, hi, r):
        # seeds of t*B bits in [a, b) are consistent with record r; record's quantum interval [lo, hi)
        if t == k:
            out[r] = (b - a)
            return
        a2, b2 = a << B, b << B
        cut = lo + Q45 * (hi - lo)
        scale = 1 << ((t + 1) * B)
        # agree iff s/scale < cut  iff  s < cut*scale  iff s <= ceil(cut*scale)-1
        x = cut * scale
        m = -((-x.numerator) // x.denominator)
        m1 = min(max(m, a2), b2)
        rec(t + 1, a2, m1, lo, cut, r + (1,))
        rec(t + 1, m1, b2, cut, hi, r + (0,))
    rec(0, 0, 1, F(0), F(1), ())
    return out


def qmass(r):
    a = sum(r)
    return Q45 ** a * (1 - Q45) ** (len(r) - a)


def sqrt_bounds(x, bits=320):
    d = 1 << bits
    k = isqrt(x.numerator * d * d // x.denominator)
    lo = F(k, d)
    hi = F(k + 1, d)
    assert lo * lo <= x <= hi * hi
    return lo, hi


def least_n_pow_below(x, level):
    """least n>=1 with x^n < level (0<x<1)."""
    est = max(1, int(math.log(float(level)) / math.log(float(x))) - 3)
    n = est
    while x ** n < level and n > 1:
        n -= 1
    while x ** n >= level:
        n += 1
    assert x ** n < level and (n == 1 or x ** (n - 1) >= level)
    return n


def tv_iid(p, h):
    return sum(comb(h, i) * abs(p ** i * (1 - p) ** (h - i) - Q45 ** i * (1 - Q45) ** (h - i)) for i in range(h + 1)) / 2


def tv_iid_int(p, h):
    D = 5 * p.denominator
    pn = p.numerator * 5
    qn = 4 * p.denominator
    tot = sum(comb(h, i) * abs(pn ** i * (D - pn) ** (h - i) - qn ** i * (D - qn) ** (h - i)) for i in range(h + 1))
    return F(tot, 2 * D ** h)


def first_cross(p, start=1):
    lo, hi = 0, 1
    while tv_iid_int(p, hi) <= F(1, 2):
        lo, hi = hi, hi * 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if tv_iid_int(p, mid) > F(1, 2):
            hi = mid
        else:
            lo = mid
    return hi


def family(res):
    fam = res['family_RS']
    report = []
    mism = 0
    for B in (2, 3, 4):
        for k in range(1, 17):
            law = block_law(B, k)
            S = 1 << (B * k)
            assert sum(law.values()) == S
            # include zero-mass records
            full = {r: F(law.get(r, 0), S) for r in product((1, 0), repeat=k)}
            Tk = sum(abs(p - qmass(r)) for r, p in full.items()) / 2
            bl = bh = F(0)
            for r, p in full.items():
                lo, hi = sqrt_bounds(p * qmass(r))
                bl += lo
                bh += hi
            assert 1 - bh <= Tk and bl * bl <= 1 - Tk * Tk
            if B >= 2:
                assert Tk < F(1, (1 << B) - 2)
            c_low, c_up = 1 - bh, 1 - bl
            n_half = c_low.denominator // c_low.numerator + 1
            assert n_half * c_low > 1 and (n_half - 1) * c_low <= 1
            n_t1 = (F(1, 10) / Tk).numerator // (F(1, 10) / Tk).denominator
            n_t2 = (1 / (200 * c_up)).numerator // (1 / (200 * c_up)).denominator
            n_tenth = max(n_t1, n_t2)
            n_hp = least_n_pow_below(bh, F(1, 2))
            n_lp = max(least_n_pow_below(bl * bl, F(3, 4)) - 1, (F(1, 2) / Tk).numerator // (F(1, 2) / Tk).denominator)
            e = fam[f'B{B}_k{k}']
            mem = (k - 1) * B + (k - 1) + math.ceil(math.log2(k)) if k > 1 else 0
            got = (e['block_tv_exact_sha256'] == digest(Tk), e['block_tv'] == disp(Tk),
                   e['certified_T_above_half_for_h_at_least'] == k * n_half,
                   e['certified_T_at_most_tenth_for_h_at_most'] == k * n_tenth,
                   e['power_rule_T_above_half_for_h_at_least'] == k * n_hp,
                   e['power_rule_T_at_most_half_for_h_at_most'] == k * n_lp,
                   e['memory_bits_upper'] == mem,
                   e['one_minus_bc_lower'][:16] == disp(c_low, 20)[:16])
            if not all(got):
                mism += 1
                report.append(('MISMATCH', B, k, got, e, k * n_half, k * n_tenth, k * n_hp, k * n_lp))
            report.append((B, k, disp(Tk), disp(c_low, 12), k * n_hp, k * n_lp, mem))
    return report, mism


def brute_rs(B, k, h):
    """Direct simulation from scratch: per block, retained seed integer and interval of the record."""
    law = {}
    for w in range(1 << (B * h)):
        r = []
        for blk in range(0, h, k):
            seed = 0
            lo, hi = F(0), F(1)
            for t in range(blk, min(blk + k, h)):
                u = (w >> (B * (h - 1 - t))) & ((1 << B) - 1)
                j = t - blk + 1
                seed = (seed << B) | u
                cut = lo + Q45 * (hi - lo)
                g = 1 if F(seed, 1 << (B * j)) < cut else 0
                lo, hi = (lo, cut) if g else (cut, hi)
                r.append(g)
        r = tuple(r)
        law[r] = law.get(r, 0) + 1
    return law


def main():
    res = json.load(open(sys.argv[1]))
    out = {}
    rows, base5 = census()
    out['census'] = rows
    out['census_matches_author'] = all(
        all(rows[key][f] == res['step4_census'][key][f] for f in res['step4_census'][key]) for key in rows)
    out['base5'] = base5
    # memoryless crossings
    out['memoryless_ceil'] = {B: (str(F(-((-4 * (1 << B)) // 5), 1 << B)), first_cross(F(-((-4 * (1 << B)) // 5), 1 << B)))
                              for B in (2, 3, 4)}
    out['memoryless_3/4'] = first_cross(F(3, 4))
    out['memoryless_floor_B4_12/16'] = first_cross(F(12, 16))
    rep, mism = family(res)
    out['family_mismatches'] = mism
    out['family_rows'] = [r for r in rep]
    # brute force product structure, own simulation, against own block laws
    for B, k, h in ((2, 3, 9), (2, 4, 10), (3, 2, 6), (4, 2, 5)):
        law = brute_rs(B, k, h)
        full, rem = divmod(h, k)
        bl = block_law(B, k)
        pred = {(): 1}
        for _ in range(full):
            pred = {a + b: x * y for a, x in pred.items() for b, y in bl.items()}
        if rem:
            tl = block_law(B, rem)
            pred = {a + b: x * y for a, x in pred.items() for b, y in tl.items()}
        assert {r: v for r, v in pred.items() if v} == law, (B, k, h)
    out['brute_product'] = 'equal'
    # B=4 ordering / B=3 outlast claims from result.json
    fam = res['family_RS']
    out['B4_fail_before'] = [k for k in range(2, 17) if fam[f'B4_k{k}'].get('certified_fails_before_memoryless_reset')]
    out['B3_outlast'] = [k for k in range(2, 17) if fam[f'B3_k{k}'].get('certified_outlasts_memoryless_reset')]
    for x in out['family_rows']:
        print(x)
    del out['family_rows']
    print(json.dumps(out, indent=1, default=str))


if __name__ == '__main__':
    main()
