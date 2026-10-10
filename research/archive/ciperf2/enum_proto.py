"""Scratch prototype (diagnosis only): enumerate_candidates of the landed A41 production probe with the per-subset
value-set construction vectorized. Executes the landed probe whole (as r2a_landed.py does), then runs the landed
enumerate_candidates and the prototype on the same orientation data and compares (cands items in insertion order, stats).

usage: python3 enum_proto.py <repo root>
"""
import contextlib, io, os, sys, time, itertools, random
import numpy as np
REPO = sys.argv[1]
PROBE = os.path.join(REPO, 'verification', 'lean', 'dita_index_map_probe.py')
NS = {'__name__': 'landed_production', '__file__': PROBE}
t0 = time.time()
with contextlib.redirect_stdout(io.StringIO()):
    try: exec(compile(open(PROBE, encoding='utf-8').read(), PROBE, 'exec'), NS)
    except SystemExit: pass
print('landed probe executed (%.0fs)' % (time.time() - t0), flush=True)
g = NS
orientations, enumerate_candidates = g['orientations'], g['enumerate_candidates']
TORUS, Empty, ksub, vsub, meet_or_none = g['TORUS'], g['Empty'], g['ksub'], g['vsub'], g['meet_or_none']
PAIRS, SHAPES3 = g['PAIRS'], g['SHAPES3']
COMB = {n: np.array(list(itertools.combinations(range(16), n)), dtype=np.int64) for n in (2, 4, 8)}


def enumerate_candidates_fast(OR):
    cache = {}
    def pbf(vals):
        if vals in cache: return cache[vals]
        d0, e0 = vals[0]
        try:
            F = TORUS
            for d, e in vals[1:]: F = F.add(ksub(d, d0), vsub(e0, e))
            r = F
        except Empty: r = None
        cache[vals] = r; return r
    cands = {}; stats = {}
    for form, (Km, Cm) in OR.items():
        de = {p: [(ksub(Km[p[0]][j], Km[p[1]][j]), vsub(Cm[p[0]][j], Cm[p[1]][j])) for j in range(16)] for p in PAIRS}
        # per pair: the distinct values in sorted order and each column's bit; a subset's sorted value set is then
        # determined by the OR of its columns' bits (ids follow the sorted order, so bit order = sorted order)
        srt = {p: sorted(set(de[p])) for p in PAIRS}
        bit = np.array([[1 << srt[p].index(de[p][j]) for j in range(16)] for p in PAIRS], dtype=np.int64)   # (120, 16)
        for m, n in SHAPES3:
            Sbs = COMB[n]
            masks = np.bitwise_or.reduce(bit[:, Sbs], axis=2).T                    # (C, 120)
            # flat per (pair, mask), computed once
            FL = {}
            for t, p in enumerate(PAIRS):
                for mk in np.unique(masks[:, t]).tolist():
                    vals = tuple(v for k_, v in enumerate(srt[p]) if (mk >> k_) & 1)
                    FL[(t, mk)] = pbf(vals)
            good = {}
            for row, Sb in zip(masks.tolist(), map(tuple, Sbs.tolist())):
                loc = {}
                for t, mk in enumerate(row):
                    F = FL[(t, mk)]
                    if F is not None: loc[PAIRS[t]] = F
                def rec(rem, classes, F):
                    if not rem: good.setdefault(tuple(classes), []).append((Sb, F)); return
                    i = min(rem)
                    nb = sorted(j for j in rem if j != i and (i, j) in loc)
                    for rest in itertools.combinations(nb, m - 1):
                        cl = (i,) + rest; Gf = F
                        for a, b in itertools.combinations(cl, 2):
                            Gf = meet_or_none(Gf, loc[(a, b)])
                            if Gf is None: break
                        if Gf is None: continue
                        rec(rem - set(cl), classes + [cl], Gf)
                rec(frozenset(range(16)), [], TORUS)
            nb0 = len(cands)
            for P, blocks in good.items():
                def cover(rem, chosen, F):
                    if not rem: cands[(form, (m, n), tuple(sorted(chosen)), P)] = F; return
                    first = min(rem)
                    for Sb, Gf in blocks:
                        if Sb[0] == first and set(Sb) <= rem:
                            Hf = meet_or_none(F, Gf)
                            if Hf is not None: cover(rem - set(Sb), chosen + [Sb], Hf)
                cover(frozenset(range(16)), [], TORUS)
            stats[(form, (m, n))] = len(cands) - nb0
    return cands, stats


# the exponent matrices r2a_landed.py feeds through arc(), plus act 39's H3 orientation data and act 36's W
def E40_entry(i, j):
    a, b, c, d = i // 4, i % 4, j // 4, j % 4
    return -int(b == 0 and c == 0) + int(a == 2 and b % 2 == 1 and d % 2 == 0) - int(a % 2 == 0 and c % 2 == 1 and d == 0)
E40 = [[E40_entry(i, j) for j in range(16)] for i in range(16)]
def piece(f): return [[f(i // 4, i % 4, j // 4, j % 4) for j in range(16)] for i in range(16)]
P = piece(lambda a, b, c, d: int(b == 0 and c == 0))
Q = piece(lambda a, b, c, d: int(a == 2 and b % 2 == 1 and d % 2 == 0))
T = piece(lambda a, b, c, d: int(a % 2 == 0 and c % 2 == 1 and d == 0))
def add(*Ms, coef):
    return [[sum(c * M[i][j] for c, M in zip(coef, Ms)) for j in range(16)] for i in range(16)]
rng = random.Random(4242)
al = [rng.randint(-3, 3) for _ in range(16)]; be = [rng.randint(-3, 3) for _ in range(16)]
Eg = [[E40[i][j] + al[i] + be[j] for j in range(16)] for i in range(16)]
Z16 = g['Z16']
CASES = [('E40', (E40, Z16, Z16)), ('EE', (g['EE'], Z16, Z16)), ('PA', (g['PA'], Z16, Z16)), ('P', (P, Z16, Z16)),
         ('Q', (Q, Z16, Z16)), ('T', (T, Z16, Z16)), ('Eg', (Eg, Z16, Z16)), ('-P+Q', (add(P, Q, coef=[-1, 1]), Z16, Z16)),
         ('-P-T', (add(P, T, coef=[-1, -1]), Z16, Z16)), ('Q-T', (add(Q, T, coef=[1, -1]), Z16, Z16)),
         ('H3', (g['PA'], g['PB'], g['PC'])), ('W', (g['WM'], Z16, Z16))]
to = tn = 0.0; bad = 0
for nm, args in CASES:
    OR = orientations(*args)
    t = time.perf_counter(); c1, s1 = enumerate_candidates(OR); d1 = time.perf_counter() - t
    t = time.perf_counter(); c2, s2 = enumerate_candidates_fast(OR); d2 = time.perf_counter() - t
    same = list(c1.items()) == list(c2.items()) and list(s1.items()) == list(s2.items())
    bad += not same; to += d1; tn += d2
    print('%-6s candidates %3d  old %6.1fs  new %6.1fs  identical (keys, flats, insertion order, stats): %s'
          % (nm, len(c1), d1, d2, same), flush=True)
print('TOTAL old %.1fs new %.1fs; mismatching cases %d' % (to, tn, bad))
