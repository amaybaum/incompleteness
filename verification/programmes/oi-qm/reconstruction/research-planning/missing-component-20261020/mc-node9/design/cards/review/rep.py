"""Independent replication (reviewer), written without importing cardtheory/exactlp.
Exact Fractions. Ontic state: (deck string top-first, slots tuple; '.' empty). Colours 'R','B'.
Menu (superset of the report's BASE): deal(slot) from top; move/swap between ANY two slots (across systems too);
deck shuffles cyc (top->bottom) and tsw (swap top two); peek(slot) destructive; peekdeck; discard(slot);
discardtop; content-controlled bijections cs1: if a1=='R' swap(b1,b2), cs2: if deck top=='R' swap(a1,a2).
Flags: NDP adds ndp(slot) (reveal, card stays). VIS adds visible slots av,bv with free read (no change)."""
import itertools, sys
from fractions import Fraction as F
from collections import defaultdict

def initial(r, b, nslots):
    seqs = set(itertools.permutations('R' * r + 'B' * b))
    w = F(1, len(seqs))
    return {(''.join(s), ('.',) * nslots): w for s in seqs}

class Menu:
    def __init__(self, slots, flags=()):
        self.slots = slots; self.ix = {s: i for i, s in enumerate(slots)}; self.flags = set(flags)
        ops = []
        for s in slots: ops += [('deal', s), ('peek', s), ('discard', s)]
        for s, t in itertools.permutations(slots, 2): ops.append(('move', s, t))
        for s, t in itertools.combinations(slots, 2): ops.append(('swap', s, t))
        ops += [('cyc',), ('tsw',), ('peekdeck',), ('discardtop',)]
        if 'a1' in slots and 'b1' in slots and 'b2' in slots: ops.append(('cs1',))
        if 'a1' in slots and 'a2' in slots: ops.append(('cs2',))
        if 'NDP' in self.flags:
            for s in slots: ops.append(('ndp', s))
        if 'VIS' in self.flags:
            for s in slots:
                if s.endswith('v'): ops.append(('read', s))
        self.ops = ops

    def act(self, op, st):
        """returns None if not applicable, else (outcome, newstate)"""
        deck, sl = st; sl = list(sl); I = self.ix; t = op[0]
        if t == 'deal':
            i = I[op[1]]
            if sl[i] != '.' or not deck: return None
            sl[i] = deck[0]; return (None, (deck[1:], tuple(sl)))
        if t in ('peek', 'discard', 'ndp', 'read'):
            i = I[op[1]]
            if sl[i] == '.': return None
            o = sl[i]
            if t in ('ndp', 'read'): return (o, st)
            sl[i] = '.'
            return ((o if t == 'peek' else None), (deck, tuple(sl)))
        if t == 'move':
            i, j = I[op[1]], I[op[2]]
            if sl[i] == '.' or sl[j] != '.': return None
            sl[j], sl[i] = sl[i], '.'; return (None, (deck, tuple(sl)))
        if t == 'swap':
            i, j = I[op[1]], I[op[2]]
            if sl[i] == '.' or sl[j] == '.': return None
            sl[i], sl[j] = sl[j], sl[i]; return (None, (deck, tuple(sl)))
        if t == 'cyc':
            if len(deck) < 2: return None
            return (None, (deck[1:] + deck[:1], tuple(sl)))
        if t == 'tsw':
            if len(deck) < 2: return None
            return (None, (deck[1] + deck[0] + deck[2:], tuple(sl)))
        if t == 'peekdeck':
            if not deck: return None
            return (deck[0], (deck[1:], tuple(sl)))
        if t == 'discardtop':
            if not deck: return None
            return (None, (deck[1:], tuple(sl)))
        if t == 'cs1':
            a1, b1, b2 = I['a1'], I['b1'], I['b2']
            if '.' in (sl[a1], sl[b1], sl[b2]): return None
            if sl[a1] == 'R': sl[b1], sl[b2] = sl[b2], sl[b1]
            return (None, (deck, tuple(sl)))
        if t == 'cs2':
            a1, a2 = I['a1'], I['a2']
            if '.' in (sl[a1], sl[a2]) or not deck: return None
            if deck[0] == 'R': sl[a1], sl[a2] = sl[a2], sl[a1]
            return (None, (deck, tuple(sl)))
        raise ValueError(op)

def key(d): return frozenset(d.items())

def closure(menu, start, cap=400000):
    seen = {key(start)}; nodes = [start]; frontier = [start]; depth = 0; branchp = set()
    while frontier:
        nxt = []
        for d in frontier:
            for op in menu.ops:
                res = [(menu.act(op, s), p) for s, p in d.items()]
                app = [r is not None for r, _ in res]
                if not any(app): continue
                assert all(app), ('mixed applicability', op)
                split = defaultdict(lambda: defaultdict(F))
                for (o, ns), p in res: split[o][ns] += p
                for o, sub in split.items():
                    tot = sum(sub.values())
                    if tot != 1: branchp.add(tot)
                    c = {k: v / tot for k, v in sub.items()}
                    k = key(c)
                    if k not in seen:
                        seen.add(k); nodes.append(c); nxt.append(c)
                        if len(nodes) > cap: raise RuntimeError('cap')
        frontier = nxt; depth += 1
    return nodes, depth - 1, branchp

def exchangeable(d):
    """invariance of the in-play colour distribution under permutations of in-play positions (deck + filled slots)"""
    pats = {(len(deck), tuple(c == '.' for c in sl)) for deck, sl in d}
    if len(pats) != 1: return False
    byM = defaultdict(dict)
    for (deck, sl), p in d.items():
        inplay = deck + ''.join(c for c in sl if c != '.')
        byM[(inplay.count('R'), len(inplay))][(deck, sl)] = p
    for (r, n), sub in byM.items():
        narr = len(set(itertools.permutations('R' * r + 'B' * (n - r))))
        if len(sub) != narr or len(set(sub.values())) != 1: return False
    return True

def marg(d, slots, ix):
    out = defaultdict(F)
    for (deck, sl), p in d.items():
        k = tuple(sl[ix[s]] for s in slots)
        if '.' in k: return None
        out[k] += p
    return {k: v for k, v in out.items() if v}

def solve(rows, rhs):
    """exact Gaussian elimination: solve sum_j x_j * rows-cols ... rows is list of columns; returns unique x or None"""
    m = len(rhs); n = len(rows)
    A = [[rows[j][i] for j in range(n)] + [rhs[i]] for i in range(m)]
    piv = []; r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None: return None
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]; A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
    if any(A[i][n] != 0 for i in range(r, m)): return None
    return [A[i][n] for i in range(n)]

def in_conv(target, cands):
    """Caratheodory enumeration (independent of a simplex code): target in conv(cands)?"""
    supp = set(target)
    cs = [c for c in cands if set(c) <= supp]
    if not cs: return False
    basis = sorted(supp)
    cols = [[c.get(b, F(0)) for b in basis] for c in cs]
    tv = [target[b] for b in basis]
    for k in range(1, min(len(cs), len(basis)) + 1):
        for sub in itertools.combinations(range(len(cs)), k):
            x = solve([cols[j] for j in sub], tv)
            if x is not None and all(v >= 0 for v in x):
                return True
    return False

def extreme(target, pool):
    return not in_conv(target, [c for c in pool if c != target])

def E(r, n):
    seqs = set(itertools.permutations('R' * r + 'B' * (n - r)))
    return {tuple(s): F(1, len(seqs)) for s in seqs}

def realization(r, b, na, nb, flags=()):
    A = [f'a{i+1}' for i in range(na)]; B = [f'b{i+1}' for i in range(nb)]
    slots = A + B + (['av', 'bv'] if 'VIS' in flags else [])
    menu = Menu(slots, flags)
    nodes, depth, bp = closure(menu, initial(r, b, len(slots)))
    nonex = sum(1 for d in nodes if not exchangeable(d))
    PAB = []; PA = []
    for d in nodes:
        m = marg(d, A + B, menu.ix)
        if m is not None and m not in PAB: PAB.append(m)
        m = marg(d, A, menu.ix)
        if m is not None and m not in PA: PA.append(m)
    extAB = [c for c in PAB if extreme(c, PAB)]
    extA = [c for c in PA if extreme(c, PA)]
    wit = []
    for c in extAB:
        ma = defaultdict(F)
        for k, v in c.items(): ma[k[:na]] += v
        ma = {k: v for k, v in ma.items() if v}
        if ma not in extA: wit.append((c, ma))
    nonE = [c for c in extAB if not any(c == E(rr, na + nb) for rr in range(na + nb + 1))]
    return dict(nodes=len(nodes), depth=depth, nonex=nonex, PAB=len(PAB), PA=len(PA), extAB=len(extAB),
                wit=wit, nonE=len(nonE), bp=bp, PABl=PAB, PAl=PA)

if __name__ == '__main__':
    flags = tuple(sys.argv[1:])
    tot = dict(real=0, withwit=0, nonex=0, nonE=0, ext=0); vals = set(); w34 = []
    for n in range(2, 7):
        for r in range(n + 1):
            for na, nb in [(1, 1), (1, 2), (2, 1), (2, 2)]:
                if n < na + nb: continue
                res = realization(r, n - r, na, nb, flags)
                tot['real'] += 1; tot['nonex'] += res['nonex']; tot['nonE'] += res['nonE']; tot['ext'] += res['extAB']
                ps = sorted({sum(v for k, v in ma.items() if k[0] == 'R') for c, ma in res['wit']})
                if res['wit']: tot['withwit'] += 1
                vals |= set(ps)
                if F(3, 4) in ps: w34.append(f'{r}R{n-r}B A{na}B{nb}')
                print(f'{r}R{n-r}B A{na}B{nb}: nodes={res["nodes"]} depth={res["depth"]} nonexch={res["nonex"]} '
                      f'|PAB|={res["PAB"]} |PA|={res["PA"]} extAB={res["extAB"]} nonE_ext={res["nonE"]} '
                      f'M1wit={len(res["wit"])} P(a1=R)={[str(x) for x in ps]}', flush=True)
    print('TOTAL', flags, tot, 'P values', sorted(str(v) for v in vals), '3/4 at', w34)
