"""rev910b: separate-engine review of native_decode_v14 (#910, author 7f843073).

Imports no author or earlier-review code.  Part 1 (native_table.py, this
directory) regenerates the 4096-row q10 table from the native rule.  Part 2
(here) decides fixed readouts with a cube-splitting solver: contexts that
differ only in a cube seed (u, mY, mR [, s]) are paired, the paired value
sets are intersected after translation by that seed's coefficient column,
and the three (a,b) patterns left at the end carry independent free values
g00=c0, g10=c0^c4, g11=c0^c4^c5.  Controls: literal brute force over
restricted feature sets (real and planted tables), a planted full-rank law,
direct table checks of every solution, sign-erased table.

Usage:  python3 -I review_checks.py <programme-root>     (writes JSON to stdout)
"""
import hashlib
import json
import random
import sys
from collections import Counter
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from native_table import q10_table, need, ROWS  # reviewer's own engine

FEAT = ('1', 'u', 'mY', 'mR', 'a', 'b')
CTX = [k for k in product((0, 1), repeat=5) if (k[3], k[4]) != (0, 1)]


def idx(x, k, e, n):
    u, my, mr, a, b = k
    r = (((((x * 2 + u) * 2 + my) * 2 + mr) * 2 + a) * 2 + b)
    return (r * 8 + e) * 8 + n


def kernel(tab):
    # K[s][k] = list over v=8e+n of raw code, x = s^u^a
    return {s: {k: [tab[idx(s ^ k[0] ^ k[3], k, v >> 3, v & 7)] for v in range(64)] for k in CTX} for s in (0, 1)}


def xlate(m, c, width=6):
    # {v : v^c in m}
    for i in range(width):
        if (c >> i) & 1:
            sh = 1 << i
            lo = 0
            for blk in range(0, 1 << width, 2 * sh):
                lo |= ((1 << sh) - 1) << blk
            m = ((m & lo) << sh) | ((m >> sh) & lo)
    return m


def solve(sets, allowed, width=6, collect=False, cube=('u', 'mY', 'mR'), extra=None):
    """sets: dict context-key -> mask over 2^width values.  Context key is
    (cube bits tuple, (a,b)).  allowed: set of feature names with free
    coefficients.  Returns count (and the list of coefficient dicts)."""
    V = 1 << width
    out = []
    total = 0

    def rec(cur, dims, path):
        nonlocal total
        if not dims:
            G = {ab: cur[(tuple(0 for _ in cube), ab)] for ab in ((0, 0), (1, 0), (1, 1))}
            fa, fb = 'a' in allowed, 'b' in allowed
            c0_free = '1' in allowed
            need(c0_free, 'constant always allowed')
            if fa and fb:
                cnt = bin(G[0, 0]).count('1') * bin(G[1, 0]).count('1') * bin(G[1, 1]).count('1')
            elif fa:
                cnt = bin(G[0, 0]).count('1') * bin(G[1, 0] & G[1, 1]).count('1')
            elif fb:
                cnt = bin(G[0, 0] & G[1, 0]).count('1') * bin(G[1, 1]).count('1')
            else:
                cnt = bin(G[0, 0] & G[1, 0] & G[1, 1]).count('1')
            total += cnt
            if collect and cnt:
                for g00 in range(V):
                    if not (G[0, 0] >> g00) & 1:
                        continue
                    for g10 in (range(V) if fa else [g00]):
                        if not (G[1, 0] >> g10) & 1:
                            continue
                        for g11 in (range(V) if fb else [g10]):
                            if not (G[1, 1] >> g11) & 1:
                                continue
                            col = dict(path)
                            col['1'] = g00
                            col['a'] = g10 ^ g00
                            col['b'] = g11 ^ g10
                            out.append(col)
            return
        j = dims[0]
        pos = cube.index(j)
        for c in (range(V) if j in allowed else [0]):
            nxt = {}
            ok = True
            for key, m in cur.items():
                bits, ab = key
                if bits[pos] == 1:
                    continue
                b1 = bits[:pos] + (1,) + bits[pos + 1:]
                mm = m & xlate(cur[(b1, ab)], c, width)
                if not mm:
                    ok = False
                    break
                nxt[key] = mm
            if ok:
                rec(nxt, dims[1:], path + ((j, c),))
    rec(sets, list(cube), ())
    return total, out


def key_of(k, s=None, cube=('u', 'mY', 'mR')):
    u, my, mr, a, b = k
    d = {'u': u, 'mY': my, 'mR': mr, 's': s}
    return tuple(d[c] for c in cube), (a, b)


def readout_sets(K, D):
    return {key_of(k): sum(1 << v for v in range(64) if not (D >> K[0][k][v]) & 1 and (D >> K[1][k][v]) & 1) for k in CTX}


def law_value(col, k, s=None):
    u, my, mr, a, b = k
    f = {'1': 1, 'u': u, 'mY': my, 'mR': mr, 'a': a, 'b': b, 's': s}
    v = 0
    for name, c in col.items():
        if f[name]:
            v ^= c
    return v


def field_coeffs(col):
    # per source field (EA,EB,ED,NA,NB,ND = bits 5..0 of v), bit j for feature FEAT[j]
    return [sum(((col.get(fn, 0) >> (5 - f)) & 1) << j for j, fn in enumerate(FEAT)) for f in range(6)]


def anf_degree(D):
    f = [(D >> c) & 1 for c in range(8)]
    for i in range(3):
        for c in range(8):
            if (c >> i) & 1:
                f[c] ^= f[c ^ (1 << i)]
    return max((bin(c).count('1') for c in range(8) if f[c]), default=0)


def brute(K, chosen):
    """Literal enumeration of all 64^m maps over chosen features."""
    names = [FEAT[i] for i in chosen]
    # per context and v: 256-bit set of readouts D with D(T0)=0, D(T1)=1
    rmask = {}
    for k in CTX:
        for v in range(64):
            o0, o1 = K[0][k][v], K[1][k][v]
            rmask[k, v] = sum(1 << D for D in range(256) if not (D >> o0) & 1 and (D >> o1) & 1)
    counts = Counter()
    diag = 0
    feats = []
    for k in CTX:
        u, my, mr, a, b = k
        fv = {'1': 1, 'u': u, 'mY': my, 'mR': mr, 'a': a, 'b': b}
        feats.append([fv[n] for n in names])
    for cols in product(range(64), repeat=len(chosen)):
        acc = (1 << 256) - 1
        dist = True
        for k, fv in zip(CTX, feats):
            v = 0
            for c, f in zip(cols, fv):
                if f:
                    v ^= c
            acc &= rmask[k, v]
            if dist and K[0][k][v] == K[1][k][v]:
                dist = False
            if not acc and not dist:
                break
        diag += dist
        while acc:
            lb = acc & -acc
            counts[lb.bit_length() - 1] += 1
            acc ^= lb
    return [counts[D] for D in range(1, 255)], diag


def distinct_sets(K):
    return {key_of(k): sum(1 << v for v in range(64) if K[0][k][v] != K[1][k][v]) for k in CTX}


def main():
    root = Path(sys.argv[1])
    res = {}
    tab_hex, q9_hex, info = q10_table()
    digest = hashlib.sha256(tab_hex.encode()).hexdigest()
    need(digest == 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc', 'regenerated table digest')
    v13 = json.loads((root / 'native_route_v13/result.json').read_text())
    need(v13['q10_table_hex'] == tab_hex, 'regenerated table equals retained v13 hex')
    old = json.loads((root / 'native_seed_v12/result.json').read_text())['q10_table_hex']
    need(''.join(tab_hex[i] for i, r in enumerate(ROWS) if r[6] == 0) == old, 'E=000 rows equal Native B table')
    need(all(q9_hex[i] == q9_hex[idx(r[0], r[1:6], 0, 0)] for i, r in enumerate(ROWS)), 'q9 at L independent of E,N')
    res['native_table'] = dict(info, sha256=digest, rows=len(tab_hex), E0_rows_match_native_B=512)
    tab = [int(ch, 16) for ch in tab_hex]
    K = kernel(tab)
    full = set(FEAT)
    # ---------------- primary: all readouts, full affine class
    counts = {}
    sols = {}
    for D in range(1, 255):
        c, out = solve(readout_sets(K, D), full, collect=True)
        need(c == len(out), 'enumeration complete')
        for col in out:  # direct table check
            for k in CTX:
                v = law_value(col, k)
                for s in (0, 1):
                    need((D >> K[s][k][v]) & 1 == s, 'direct table check')
        counts[D] = c
        sols[D] = out
    pos = [D for D in counts if counts[D]]
    res['readouts_with_solutions'] = len(pos)
    res['total_solutions'] = sum(counts.values())
    deg = Counter(anf_degree(D) for D in pos)
    res['positive_by_degree'] = dict(sorted(deg.items()))
    res['degree_one_total'] = sum(1 for D in range(1, 255) if anf_degree(D) == 1)
    names = {}
    for D in range(1, 255):
        if anf_degree(D) == 1:
            lin = [f for f, bit in (('A', 4), ('B', 2), ('D', 1)) if ((D >> bit) & 1) != (D & 1)]
            names[D] = ('NOT ' if D & 1 else '') + '^'.join(lin)
    res['degree_one_counts'] = {names[D]: counts[D] for D in sorted(names)}
    QA = 0b11110000
    need(counts[QA] == len(sols[QA]), 'qA enumeration')
    res['qA_equals_s_laws'] = counts[QA]
    target = [1, 5, 1, 4, 1, 5]
    res['mY_only_law_present'] = any(field_coeffs(c) == target for c in sols[QA])
    # minimal seed support among qA laws
    def support(col):
        return sorted({n for n, c in col.items() if n != '1' and c})
    sup = Counter(len(support(c)) for c in sols[QA])
    res['qA_seed_support_sizes'] = dict(sorted(sup.items()))
    res['qA_single_seed_laws'] = [[support(c), field_coeffs(c)] for c in sols[QA] if len(support(c)) <= 1]
    # post-hoc author items
    every = [(D, c) for D in pos for c in sols[D]]
    res['solutions_E_identically_000'] = sum(1 for D, c in every if all(((x >> 3) & 7) == 0 for x in c.values()))
    res['solutions_E_constant'] = sum(1 for D, c in every if all(((x >> 3) & 7) == 0 for n, x in c.items() if n != '1'))
    res['solutions_N_constant'] = sum(1 for D, c in every if all((x & 7) == 0 for n, x in c.items() if n != '1'))
    # ---------------- Q1 nontriviality controls
    q1 = {}
    const_counts = {D: solve(readout_sets(K, D), {'1'})[0] for D in range(1, 255)}
    q1['constant_sources_total_solutions'] = sum(const_counts.values())
    q1['constant_sources_qA'] = const_counts[QA]
    # sign-erased
    Ke = {0: K[0], 1: K[0]}
    q1['sign_erased_total'] = sum(solve(readout_sets(Ke, D), full)[0] for D in range(1, 255))
    q1['sign_erased_diagnostic'] = solve(distinct_sets(Ke), full)[0]
    # sources depending on s directly: features (1,u,mY,mR,a,b,s), 48 (s,k) points
    cube_s = ('u', 'mY', 'mR', 's')
    def sdep_sets(D):
        return {key_of(k, s, cube_s): sum(1 << v for v in range(64) if ((D >> K[s][k][v]) & 1) == s)
                for k in CTX for s in (0, 1)}
    c_sdep, _ = solve(sdep_sets(QA), full | {'s'}, cube=cube_s)
    q1['s_dependent_sources_qA_laws_of_2^42'] = c_sdep
    # s-only copy: E,N depend on s alone (no seeds)
    c_sonly, _ = solve(sdep_sets(QA), {'1', 's'}, cube=cube_s)
    q1['s_only_sources_qA_laws'] = c_sonly
    # is s special? targets x ^ f(k) for all 64 affine f (incl. f=u^a, i.e. s)
    tgt = {}
    for fcoef in range(64):
        def f(k):
            fv = (1,) + k
            return sum(fv[j] for j in range(6) if (fcoef >> j) & 1) & 1
        sets = {}
        for k in CTX:
            m = 0
            for v in range(64):
                ok = True
                for x in (0, 1):
                    if ((QA >> tab[idx(x, k, v >> 3, v & 7)]) & 1) != (x ^ f(k)):
                        ok = False
                if ok:
                    m |= 1 << v
            sets[key_of(k)] = m
        tgt[fcoef] = solve(sets, full)[0]
    need(tgt[0b010010] == counts[QA], 'target x^u^a reproduces qA count')
    q1['qA_targets_x_xor_affine_seed_fn_nonzero'] = sum(1 for v in tgt.values() if v)
    q1['qA_target_counts_x_xor_f'] = {format(fc, '06b')[::-1]: c for fc, c in tgt.items() if c}
    # E=000 forced (Native B single-N class)
    sets0 = readout_sets(K, QA)
    q1['E_forced_000_any_readout'] = sum(solve({kk: m & 0xff for kk, m in readout_sets(K, D).items()}, full)[0]
                                         for D in range(1, 255))
    # x-dependence of q10.A per (k, v)
    xdep = sum(1 for k in CTX for v in range(64) if (K[0][k][v] >> 2) != (K[1][k][v] >> 2))
    q1['qA_depends_on_x_rows_of_1536'] = xdep
    res['Q1'] = q1
    # ---------------- Q3: other fields under qA laws
    q3 = Counter()
    bd_ctx = []
    b_ctx = []
    d_ctx = []
    bd_reveal_all = 0
    for col in sols[QA]:
        nb = nd = nbd = 0
        for k in CTX:
            v = law_value(col, k)
            o0, o1 = K[0][k][v], K[1][k][v]
            nb += ((o0 >> 1) & 1) != ((o1 >> 1) & 1)
            nd += (o0 & 1) != (o1 & 1)
            nbd += (o0 & 3) != (o1 & 3)
        b_ctx.append(nb); d_ctx.append(nd); bd_ctx.append(nbd)
        bd_reveal_all += nbd == 24
    res['Q3'] = {'laws': len(sols[QA]),
                 'min_max_contexts_BD_depend_on_s': [min(bd_ctx), max(bd_ctx)],
                 'min_max_contexts_B_depends_on_s': [min(b_ctx), max(b_ctx)],
                 'min_max_contexts_D_depends_on_s': [min(d_ctx), max(d_ctx)],
                 'laws_with_B_sign_free_all_contexts': sum(1 for x in b_ctx if x == 0),
                 'laws_with_D_sign_free_all_contexts': sum(1 for x in d_ctx if x == 0),
                 'laws_with_BD_sign_free_all_contexts': sum(1 for x in bd_ctx if x == 0),
                 'laws_BD_reveal_s_on_all_24_contexts': bd_reveal_all}
    # ---------------- Q2 earliest tick: decode at q10 for t=L (E,N not yet arrived) is computed in native_table extension
    # ---------------- controls: planted full-rank law
    rnd = random.Random(910)
    synth = list(tab)
    plant = {'1': 37, 'u': 12, 'mY': 55, 'mR': 41, 'a': 22, 'b': 7}
    for k in CTX:
        v = law_value(plant, k)
        for s in (0, 1):
            synth[idx(s ^ k[0] ^ k[3], k, v >> 3, v & 7)] = 5 if s else 2
    Ks = kernel(synth)
    cpl, outpl = solve(readout_sets(Ks, QA), full, collect=True)
    need(any(c == plant for c in outpl), 'planted law recovered')
    res['controls'] = {'planted_full_rank_qA_count': cpl}
    # brute force, real and planted tables
    bfs = []
    for label, chosen, pl in (('real', (0, 1), None), ('real', (0, 1, 4), None), ('real', (0, 2, 3), None),
                              ('real', (0, 4, 5), None), ('planted', (0, 1, 4), {'1': 5, 'u': 3, 'a': 6}),
                              ('planted', (0, 2, 5), {'1': 9, 'mY': 33, 'b': 17})):
        allowed = {FEAT[i] for i in chosen}
        tb = list(tab)
        if pl:
            for k in CTX:
                v = law_value(pl, k)
                for s in (0, 1):
                    tb[idx(s ^ k[0] ^ k[3], k, v >> 3, v & 7)] = 5 if s else 2
        Kb = kernel(tb)
        bc, bd = brute(Kb, chosen)
        mine = [solve(readout_sets(Kb, D), allowed)[0] for D in range(1, 255)]
        md = solve(distinct_sets(Kb), allowed)[0]
        need(bc == mine, 'brute force per-readout counts %s %s' % (label, chosen))
        need(bd == md, 'brute force diagnostic %s %s' % (label, chosen))
        if pl:
            need(sum(bc) > 0, 'planted brute force nonvacuous')
        bfs.append([label, [FEAT[i] for i in chosen], sum(bc), sum(1 for x in bc if x), bd])
    res['controls']['brute_force_label_features_total_readouts_diagnostic'] = bfs
    # raw-pair reproduction: singleton readouts; E-only projection counts
    e_total = joint_total = 0
    ncommon = 0
    for o0, o1 in product(range(8), repeat=2):
        if o0 == o1:
            continue
        sets = {key_of(k): sum(1 << v for v in range(64) if K[0][k][v] == o0 and K[1][k][v] == o1) for k in CTX}
        if all(sets.values()):
            ncommon += 1
        joint_total += solve(sets, full)[0]
        esets = {kk: sum(1 << e for e in range(8) if (m >> (8 * e)) & 0xff) for kk, m in sets.items()}
        e_total += solve(esets, full, width=3)[0]
    res['controls']['raw_pair'] = {'common_injective_pairs': ncommon, 'affine_E_maps': e_total, 'joint': joint_total}
    need(ncommon == 32 and e_total == 16 and joint_total == 0, 'raw-pair reproduction')
    # diagnostic (known-seed readout) and constant witness E=001,N=000
    res['diagnostic_count_full'] = solve(distinct_sets(K), full)[0]
    res['diagnostic_const_E001_N000_ok'] = all(K[0][k][8] != K[1][k][8] for k in CTX)
    res['diagnostic_const_E001_N000_distinct_pairs'] = len({(K[0][k][8], K[1][k][8]) for k in CTX})
    # author result comparison
    auth = json.loads((root / 'native_decode_v14/result.json').read_text())
    need(auth['readout_solution_counts'] == [counts[D] for D in range(1, 255)], 'per-readout counts equal author')
    res['author_per_readout_counts_equal'] = True
    print(json.dumps(res, sort_keys=True, indent=1))


if __name__ == '__main__':
    main()
