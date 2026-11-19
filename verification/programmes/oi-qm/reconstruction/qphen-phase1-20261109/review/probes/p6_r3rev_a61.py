"""p6_r3rev_a61 -- independent r3 reviewer probe for QX-6 Lemma A6.1 (no p1-p5 imports).

Exact, exhaustive over pre-setting configurations and settings for every generated model.
(1) random time-dependent, setting-dependent tick maps on binary sites satisfying (D) and (L'),
    with dependency graphs G_t computed exactly from the maps (union over settings, symmetrized);
    whenever (R) holds, check the readout configuration on R_A (resp. R_B) never depends on b (resp. a).
(2) adversarial family: B-components read from arbitrary far sites (allowed by (L')), settings at
    staggered ticks, non-bijective maps, readout regions placed at exactly the (R) boundary.
(3) the one-tick composite op_A . phi . op_B (Q6-D1): (L) and single-graph (R) hold, (L') fails, S = 4.
(4) the same operations on three ticks: (L') holds, (R) fails at equality, S = 4.
(5) Main's form: one setting tick u_a x u_b x id then k iterates of a fixed phi; (R) in G_B equals
    Main's d_phi; and a single-graph instance where Main's (iii) holds but single-graph (R) fails.
"""
import itertools, random
from collections import deque

def dist(adj, src, dst):
    src = set(src); dst = set(dst)
    if src & dst: return 0
    seen = set(src); q = deque((s, 0) for s in src)
    while q:
        u, d = q.popleft()
        for v in adj.get(u, ()):
            if v not in seen:
                if v in dst: return d + 1
                seen.add(v); q.append((v, d + 1))
    return float('inf')

class Model:
    """ticks[t] = dict site -> (reads tuple, table dict keyed by (a,b,inputs)) ; config is tuple of bits"""
    def __init__(self, n, ticks):
        self.n = n; self.ticks = ticks
    def step(self, t, x, a, b):
        out = list(x)
        for i, (reads, fn) in self.ticks[t].items():
            out[i] = fn(a, b, tuple(x[j] for j in reads))
        return tuple(out)
    def run(self, x0, a, b, T):
        x = x0
        for t in range(T): x = self.step(t, x, a, b)
        return x
    def map_differs(self, t, s1, s2):
        for x in itertools.product((0, 1), repeat=self.n):
            if self.step(t, x, *s1) != self.step(t, x, *s2): return True
        return False
    def dep_graph(self, t):
        """exact dependency graph: i~j iff output i depends on input j for some x and some settings"""
        adj = {i: set() for i in range(self.n)}
        for a, b in itertools.product((0, 1), repeat=2):
            for x in itertools.product((0, 1), repeat=self.n):
                y = self.step(t, x, a, b)
                for j in range(self.n):
                    xj = list(x); xj[j] ^= 1
                    yj = self.step(t, tuple(xj), a, b)
                    for i in range(self.n):
                        if i != j and y[i] != yj[i]:
                            adj[i].add(j); adj[j].add(i)
        return adj
    def first_tick(self, which, T):
        for t in range(T):
            pairs = ([((a, 0), (a, 1)) for a in (0, 1)] if which == 'B' else [((0, b), (1, b)) for b in (0, 1)])
            if any(self.map_differs(t, p, q) for p, q in pairs): return t + 1   # ticks numbered from 1
        return None
    def Lprime(self, A, B, T):
        for t in range(T):
            for x in itertools.product((0, 1), repeat=self.n):
                for a in (0, 1):
                    y0, y1 = self.step(t, x, a, 0), self.step(t, x, a, 1)
                    if any(y0[i] != y1[i] for i in range(self.n) if i not in B): return False
                for b in (0, 1):
                    y0, y1 = self.step(t, x, 0, b), self.step(t, x, 1, b)
                    if any(y0[i] != y1[i] for i in range(self.n) if i not in A): return False
        return True

def rand_fn(k, rng):
    tab = {}
    for a, b in itertools.product((0, 1), repeat=2):
        for inp in itertools.product((0, 1), repeat=k):
            tab[(a, b, inp)] = rng.randint(0, 1)
    return tab

def make_site(reads, tab, kind):
    if kind == 'A':   # depends on a only
        return (reads, lambda a, b, inp, tab=tab: tab[(a, 0, inp)])
    if kind == 'B':
        return (reads, lambda a, b, inp, tab=tab: tab[(0, b, inp)])
    return (reads, lambda a, b, inp, tab=tab: tab[(0, 0, inp)])

def random_model(n, A, B, T, rng, maxread=2, setting_prob=0.5, far_prob=0.0):
    ticks = []
    for t in range(T):
        tk = {}
        for i in range(n):
            if rng.random() < 0.35:   # identity at this site this tick
                continue
            k = rng.randint(1, maxread)
            if rng.random() < far_prob:
                reads = tuple(rng.sample(range(n), k))
            else:
                pool = [j for j in range(n) if abs(j - i) <= 1] + [i]
                reads = tuple(sorted(set(rng.choice(pool) for _ in range(k))))
            kind = 'N'
            if i in A and rng.random() < setting_prob: kind = 'A'
            if i in B and rng.random() < setting_prob: kind = 'B'
            tk[i] = make_site(reads, rand_fn(len(reads), rng), kind)
        ticks.append(tk)
    return Model(n, ticks)

def check_model(m, A, B, T, RA, RB, TA, TB):
    """returns (R_holds_A, depA, R_holds_B, depB)"""
    tA, tB = m.first_tick('A', T), m.first_tick('B', T)
    graphs = [m.dep_graph(t) for t in range(T)]
    def union(from_tick):  # union of G_t for t > from_tick (ticks numbered from 1)
        adj = {i: set() for i in range(m.n)}
        for t in range(from_tick, T):   # tick index t+1 > from_tick
            for i, s in graphs[t].items(): adj[i] |= s
        return adj
    res = []
    for (R, Tw, src_tick, src, varyB) in ((RA, TA, tB, B, True), (RB, TB, tA, A, False)):
        if src_tick is None:
            Rholds = True
        elif Tw < src_tick:
            Rholds = True
        else:
            Rholds = dist(union(src_tick), src, R) > Tw - src_tick
        dep = False
        for x0 in itertools.product((0, 1), repeat=m.n):
            for own in (0, 1):
                outs = set()
                for oth in (0, 1):
                    a, b = (own, oth) if varyB else (oth, own)
                    xT = m.run(x0, a, b, Tw)
                    outs.add(tuple(xT[i] for i in R))
                if len(outs) > 1: dep = True; break
            if dep: break
        res += [Rholds, dep]
    return res

def chsh_from_table(fA, fB, lam_list):
    E = {}
    for a, b in itertools.product((0, 1), repeat=2):
        E[(a, b)] = sum((1 - 2 * fA(l, a, b)) * (1 - 2 * fB(l, a, b)) for l in lam_list) / len(lam_list)
    return E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]

def main():
    rng = random.Random(20261109)
    n = 7
    stats = dict(models=0, Lp=0, R_cases=0, R_viol=0, notR_cases=0, notR_dep=0)
    for trial in range(1500):
        A = {0, 1}; B = {5, 6}
        if trial % 3 == 1: A, B = {0}, {6}
        if trial % 3 == 2: A, B = {1, 2}, {5}
        T = rng.randint(1, 4)
        far = 0.25 if trial % 2 else 0.0
        m = random_model(n, A, B, T, rng, far_prob=far)
        stats['models'] += 1
        if not m.Lprime(A, B, T):
            continue
        stats['Lp'] += 1
        RA = set(rng.sample([i for i in range(n) if i not in B], rng.randint(1, 2)))
        RB = set(rng.sample([i for i in range(n) if i not in A], rng.randint(1, 2)))
        TA = rng.randint(1, T); TB = rng.randint(1, T)
        ra, da, rb, db = check_model(m, A, B, T, RA, RB, TA, TB)
        for r, d in ((ra, da), (rb, db)):
            if r:
                stats['R_cases'] += 1; stats['R_viol'] += d
            else:
                stats['notR_cases'] += 1; stats['notR_dep'] += d

    # (2b) boundary-targeted: R_A = all sites at G_B-distance exactly T_A - t_B + 1 from B
    bstats = dict(cases=0, dep=0)
    for trial in range(400):
        A, B = {0, 1}, {5, 6}
        T = rng.randint(2, 4)
        m = random_model(n, A, B, T, rng, far_prob=0.3 if trial % 2 else 0.0, maxread=3)
        tB = m.first_tick('B', T)
        if tB is None: continue
        graphs = [m.dep_graph(t) for t in range(T)]
        GB = {i: set() for i in range(n)}
        for t in range(tB, T):
            for i, s_ in graphs[t].items(): GB[i] |= s_
        for TA in range(tB, T + 1):
            ring = [i for i in range(n) if i not in B and dist(GB, B, {i}) == TA - tB + 1]
            if not ring: continue
            bstats['cases'] += 1
            for x0 in itertools.product((0, 1), repeat=n):
                for a in (0, 1):
                    o = {tuple(m.run(x0, a, b, TA)[i] for i in ring) for b in (0, 1)}
                    if len(o) > 1: bstats['dep'] += 1; break
                else: continue
                break
    print('(2b) boundary-targeted (R) cases:', bstats)
    assert bstats['dep'] == 0
    print('(1)-(2) random/adversarial (L\') models:', stats)
    assert stats['R_viol'] == 0, 'A6.1 counterexample found'
    assert stats['notR_dep'] > 0, '(R) vacuous in sample'

    # (3) one-tick composite op_A . phi . op_B ; sites: 0=A0 (lam), 1=A1, 2=B0, 3=B1 (lam copy)
    def tick_composite(x, a, b):
        A0, A1, B0, B1 = x
        B0 = B0 ^ b                 # op_B: reads/writes B only
        A1 = A1 ^ B0                # fixed phi: copies B0 into A1
        A0 = A0 ^ (a & A1)          # op_A: reads/writes A only
        return (A0, A1, B0, B1)
    lam = [0, 1]
    fA = lambda l, a, b: tick_composite((l, 0, 0, l), a, b)[0]
    fB = lambda l, a, b: tick_composite((l, 0, 0, l), a, b)[3]
    S3 = chsh_from_table(fA, fB, lam)
    # dependency graph of the one tick
    adj = {i: set() for i in range(4)}
    for a, b in itertools.product((0, 1), repeat=2):
        for x in itertools.product((0, 1), repeat=4):
            y = tick_composite(x, a, b)
            for j in range(4):
                xj = list(x); xj[j] ^= 1; yj = tick_composite(tuple(xj), a, b)
                for i in range(4):
                    if i != j and y[i] != yj[i]: adj[i].add(j); adj[j].add(i)
    d_single = dist(adj, {2, 3}, {0})
    Lp = all(tick_composite(x, a, 0)[i] == tick_composite(x, a, 1)[i]
             for x in itertools.product((0, 1), repeat=4) for a in (0, 1) for i in (0, 1))
    print('(3) one-tick composite: S =', S3, '; single-graph d(B,R_A) =', d_single, '> T_A - t_B = 0 ; (L\') holds:', Lp)
    assert S3 == 4 and d_single > 0 and not Lp

    # (4) three ticks: op_B at tick1, phi at tick2, op_A at tick3
    def run3(x, a, b):
        A0, A1, B0, B1 = x
        B0 ^= b
        A1 ^= B0
        A0 ^= (a & A1)
        return (A0, A1, B0, B1)
    fA = lambda l, a, b: run3((l, 0, 0, l), a, b)[0]
    fB = lambda l, a, b: run3((l, 0, 0, l), a, b)[3]
    S4 = chsh_from_table(fA, fB, lam)
    GB = {0: {1}, 1: {0, 2}, 2: {1}, 3: set()}   # ticks 2,3: phi edge A1-B0, op_A edge A0-A1
    dGB = dist(GB, {2, 3}, {0})
    print('(4) three ticks: S =', S4, '; d_GB(B,R_A) =', dGB, '; T_A - t_B =', 3 - 1)
    assert S4 == 4 and dGB == 2

    # (5) Main's form, and the single-graph distinction
    # sites: 0=A1, 1=A2, 2=B0, 3=mid ; phi edges: B0-A1 only (A2 isolated from B under phi)
    def phi(x):
        A1, A2, B0, M = x
        return (A1 ^ B0, A2, B0, M)
    def setting(x, a, b):
        A1, A2, B0, M = x
        if a: A1, A2 = A2, A1         # u_a: permutes A's sites (reads/writes A only): edge A1-A2
        return (A1, A2, B0 ^ b, M)    # u_b on B
    k = 2
    dep = set()
    for x in itertools.product((0, 1), repeat=4):
        for a in (0, 1):
            outs = set()
            for b in (0, 1):
                y = setting(x, a, b)
                for _ in range(k): y = phi(y)
                outs.add(y[1])        # R_A = {A2}
            dep.add(len(outs) > 1)
    single = {0: {2, 1}, 1: {0}, 2: {0}, 3: set()}
    print('(5) Main instance: d_phi(B,{A2}) =', dist({0: {2}, 2: {0}, 1: set(), 3: set()}, {2}, {1}),
          '; single-graph d =', dist(single, {2}, {1}), '<= k =', k, '; readout depends on b:', True in dep)
    assert True not in dep and dist(single, {2}, {1}) == 2
    print('ALL A6.1 CHECKS PASS')

if __name__ == '__main__':
    main()
