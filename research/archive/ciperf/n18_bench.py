"""Read-only benchmark of A42 part_n18: the landed algorithm (old) against an equivalent rewrite (new).
Usage: python3 n18_bench.py <wt-root> <k> old|new|both [--modp]
Writes n18_<k>_<mode>.json beside this file: per-subspace match lists and perf_counter splits.
Imports the landed tools read-only; changes nothing in the worktree."""
import sys, os, json, time
from fractions import Fraction as Fr
WT, K, MODE = sys.argv[1], int(sys.argv[2]), sys.argv[3]
MODP = '--modp' in sys.argv
TOOLS = os.path.join(WT, 'verification/lean/a42')
sys.path.insert(0, TOOLS)
import lib42 as L
import triples as T
HERE = os.path.dirname(os.path.abspath(__file__))
P = (1 << 61) - 1

def rank_old(rows):                       # verbatim from part_n18
    M = [[Fr(x) for x in r] for r in rows if any(r)]; r = 0; ncol = len(M[0]) if M else 0
    for c in range(ncol):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]; pv = M[r][c]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / pv; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r

def vec(eq):
    v = [0] * 256
    for kk, (i, j) in eq: v[i * 16 + j] += kk
    return v

def _norm(v):
    from math import gcd
    g = 0
    for x in v: g = gcd(g, x)
    if g > 1: v = [x // g for x in v]
    return v

class IntEchelon:
    """fraction-free integer echelon basis: rows kept primitive; reduce(v) eliminates v against the basis exactly"""
    def __init__(self): self.rows = []          # list of (pivot col, row)
    def reduce(self, v):
        v = list(v)
        for c, r in self.rows:
            if v[c]:
                a, b = r[c], v[c]
                v = [a * x - b * y for x, y in zip(v, r)]
                v = _norm(v)
        return v
    def add(self, v):
        v = self.reduce(v)
        if any(v):
            c = next(i for i, x in enumerate(v) if x)
            if v[c] < 0: v = [-x for x in v]
            # keep earlier rows reduced at the new pivot so later reductions stay exact
            self.rows.append((c, v)); return True
        return False

def rank_int(rows):
    E = IntEchelon(); return sum(E.add(r) for r in rows if any(r))

def rank_p(rows):
    R = [[x % P for x in r] for r in rows if any(r)]; rk = 0
    for c in range(256):
        pr = next((i for i in range(rk, len(R)) if R[i][c]), None)
        if pr is None: continue
        R[rk], R[pr] = R[pr], R[rk]; inv = pow(R[rk][c], P - 2, P); R[rk] = [(x * inv) % P for x in R[rk]]
        for i in range(len(R)):
            if i != rk and R[i][c]:
                f = R[i][c]; R[i] = [(x - f * y) % P for x, y in zip(R[i], R[rk])]
        rk += 1
    return rk

def canon(groups): return tuple(sorted(tuple(sorted(g)) for g in groups))

def run(mode):
    t = {'census': 0.0, 'index': 0.0, 'identity_eqs': 0.0, 'rank': 0.0, 'modp': 0.0}
    t0 = time.perf_counter(); CEN = T.census(); t['census'] = time.perf_counter() - t0
    mine = L.STRUCTS[K::3]; out = {}; ncand = 0; nrej = 0
    if mode == 'new':
        t0 = time.perf_counter(); IDX = {}
        for key, ths in CEN.items():
            form, mn2, blocks, classes = key
            IDX.setdefault((form, mn2, canon(blocks), canon(classes)), []).append((key, ths))
        t['index'] = time.perf_counter() - t0
        memo = {}
    for nm, tr, s in mine:
        mn, cp, rows = s
        old = [[int(x) for x in r] for r in L.SMAT[(nm, tr, True)]]   # Python ints: numpy int64 would overflow in integer elimination
        t0 = time.perf_counter()
        if mode == 'old':
            ro = rank_old(old)
        else:
            assert all(type(x) is int for r in old for x in r), 'non-Python-int coefficient in old rows'
            EO = IntEchelon(); ro = sum(EO.add(r) for r in old if any(r))
        t['rank'] += time.perf_counter() - t0
        matches = []
        if mode == 'old':
            cands = []
            for key, ths in CEN.items():
                form, mn2, blocks, classes = key
                if form != ('row' if tr else 'column') or mn2 != mn: continue
                if sorted(map(sorted, blocks)) != sorted(map(sorted, cp)) or sorted(map(sorted, classes)) != sorted(map(sorted, rows)): continue
                cands.append((key, ths))
        else:
            cands = IDX.get(('row' if tr else 'column', mn, canon(cp), canon(rows)), [])
        for key, ths in cands:
            for th in ths:
                ncand += 1
                t0 = time.perf_counter()
                if mode == 'old':
                    new = [vec(e) for e in T.identity_eqs(key, th)]
                else:
                    mk = (key, tuple(map(tuple, th)))
                    new = memo.get(mk)
                    if new is None:
                        new = memo[mk] = [vec(e) for e in T.identity_eqs(key, th)]
                        assert all(type(x) is int for r in new for x in r), 'non-Python-int coefficient in new rows'
                t['identity_eqs'] += time.perf_counter() - t0
                if mode == 'old':
                    t0 = time.perf_counter(); ok = rank_old(new) == ro and rank_old(old + new) == ro
                    t['rank'] += time.perf_counter() - t0
                else:
                    if MODP:
                        t0 = time.perf_counter(); rej = rank_p(old + new) > ro; t['modp'] += time.perf_counter() - t0
                        if rej: nrej += 1; continue      # one-sided: rank_p <= rank_Q, so rank_Q(old+new) > ro too
                    t0 = time.perf_counter()
                    ok = all(not any(EO.reduce(v)) for v in new if any(v)) and rank_int(new) == ro
                    t['rank'] += time.perf_counter() - t0
                if ok: matches.append([list(x) for x in th])
        out['%s %s' % (nm, 'row' if tr else 'column')] = {'rank': ro, 'matches': sorted(matches)}
    return {'mode': mode, 'k': K, 'modp': MODP, 'candidates': ncand, 'modp_rejected': nrej, 'times': t, 'results': out}

if __name__ == '__main__':
    for mode in (['old', 'new'] if MODE == 'both' else [MODE]):
        s = time.perf_counter(); res = run(mode); res['total'] = time.perf_counter() - s
        fn = os.path.join(HERE, 'n18_%d_%s%s.json' % (K, mode, '_modp' if (MODP and mode == 'new') else ''))
        json.dump(res, open(fn, 'w'), indent=1, sort_keys=True)
        print(mode, 'total %.1fs' % res['total'], {k: round(v, 1) for k, v in res['times'].items()}, 'candidates', res['candidates'], 'modp_rejected', res['modp_rejected'])
