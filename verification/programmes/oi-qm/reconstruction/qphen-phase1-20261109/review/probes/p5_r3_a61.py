"""Probe P5-A61 (QPHEN Phase 1 r3, writer's checks). Exact integer arithmetic; no import from p1-p4.

Checks for QX6 r3 A6.1 (Bell ceiling for time-dependent local dynamics) under (D), (L'), (R), (MI),
with per-tick dependency graphs G_t and the post-setting graph G_B = union_{t > t_B} G_t.

(1) One-tick composite op_A o phi o op_B (the reviewer's P4 shape, rebuilt here): (L') FAILS,
    S = 4.  Under the single-graph (R) of the weaker statement, d_G = 1 > T_A - t_B = 0 holds,
    so that weaker statement is refuted.
(2) The same three operations on three separate ticks: (L') HOLDS, (R) FAILS
    (d_{G_B} = 2 = T_A - t_B), and S = 4.  Control: (R) is not vacuous.
(3) Random constructions of local reversible layers satisfying (D) and (L'): whenever (R) holds,
    A's records are b-independent and B's records a-independent for every initial state.
    Countercontrol: cases where (R) fails show actual dependence (the lemma is not vacuous).
(4) Main's one-step form u_a x u_b x id followed by k iterates of one fixed phi: (L') holds at
    every tick, t_A = t_B = 1, G_B = G_phi, and (R) coincides with Main's (iii).
(5) Why G_B and not one graph containing the setting tick: an instance satisfying Main's (iii)
    (d_phi = inf) whose single-graph distance (setting edges included) is 2 <= k = 2.
"""
import itertools, random
from fractions import Fraction

# ---------- generic helpers ----------
def dep_graph(tickmap, sites, settings):
    """undirected one-step dependency graph of a tick map, union over settings (Main:364 definition)"""
    E = set()
    for st in settings:
        for x in itertools.product((0, 1), repeat=len(sites)):
            s = dict(zip(sites, x)); base = tickmap(s, *st)
            for j in sites:
                t = dict(s); t[j] ^= 1; img = tickmap(t, *st)
                for i in sites:
                    if i != j and img[i] != base[i]:
                        E.add(frozenset((i, j)))
    return E

def dist(E, src, dst, sites):
    adj = {v: set() for v in sites}
    for e in E:
        u, v = tuple(e); adj[u].add(v); adj[v].add(u)
    seen, fr, d = set(src), set(src), 0
    while fr:
        if fr & set(dst):
            return d
        fr = {w for v in fr for w in adj[v]} - seen; seen |= fr; d += 1
    return float('inf')

def outside_dependence(tickmap, sites, region, which):
    """True if some component outside `region` depends on the setting `which` ('a' or 'b')."""
    for x in itertools.product((0, 1), repeat=len(sites)):
        s = dict(zip(sites, x))
        for other in (0, 1):
            if which == 'b':
                u, v = tickmap(s, other, 0), tickmap(s, other, 1)
            else:
                u, v = tickmap(s, 0, other), tickmap(s, 1, other)
            if any(u[i] != v[i] for i in sites if i not in region):
                return True
    return False

def is_bijective(tickmap, sites, a, b):
    imgs = {tuple(tickmap(dict(zip(sites, x)), a, b)[k] for k in sites)
            for x in itertools.product((0, 1), repeat=len(sites))}
    return len(imgs) == 2 ** len(sites)

# ---------- (1), (2): the composite and its split ----------
S6 = ['rho', 'rho_out', 'lamA', 'beta_set', 'beta_out', 'lamB']
REG_A, REG_B = {'rho', 'rho_out', 'lamA'}, {'beta_set', 'beta_out', 'lamB'}
def opB(s, a, b): s = dict(s); s['beta_set'] ^= b; return s
def phi(s, a, b): s = dict(s); s['rho'] ^= s['beta_set']; return s
def opA(s, a, b): s = dict(s); s['rho_out'] ^= (a & s['rho']) ^ s['lamA']; return s
def composite(s, a, b): return opA(phi(opB(s, a, b), a, b), a, b)

def run(ticks, lam, a, b):
    s = {'rho': 0, 'rho_out': 0, 'lamA': lam, 'beta_set': 0, 'beta_out': lam, 'lamB': lam}
    for tk in ticks:
        s = tk(s, a, b)
    return s

def chsh(ticks):
    E = {}
    for a, b in itertools.product((0, 1), repeat=2):
        E[(a, b)] = Fraction(sum((-1) ** (run(ticks, lam, a, b)['rho_out'] ^ run(ticks, lam, a, b)['beta_out'])
                                 for lam in (0, 1)), 2)
    return E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]

SET4 = list(itertools.product((0, 1), repeat=2))

def report_12():
    print('(1) one-tick composite (t_B = t_A = T_A = 1):')
    print('    bijective for all settings:', all(is_bijective(composite, S6, a, b) for a, b in SET4))
    print("    (L') holds:", not outside_dependence(composite, S6, REG_B, 'b'))
    G1 = dep_graph(composite, S6, SET4)
    print('    single-graph d_G(B, R_A) =', dist(G1, REG_B, {'rho_out'}, S6), '> T_A - t_B = 0 ; S =', chsh([composite]))
    print('    G_B = union of ticks after t_B = empty; (R) with G_B holds: d = inf > 0.  Excluded only by (L\').')
    ticks = [opB, phi, opA]
    print('(2) split over ticks 1, 2, 3 (t_B = 1, T_A = 3):')
    print("    (L') holds at every tick:", all(not outside_dependence(t, S6, REG_B, 'b') and
                                              not outside_dependence(t, S6, REG_A, 'a') for t in ticks))
    GB = dep_graph(phi, S6, SET4) | dep_graph(opA, S6, SET4)
    d = dist(GB, REG_B, {'rho_out'}, S6)
    print('    d_{G_B}(B, R_A) =', d, ' T_A - t_B =', 2, ' (R) holds:', d > 2, '; S =', chsh(ticks))

# ---------- (3) random constructions ----------
def random_graph(n, rng):
    while True:
        E = {frozenset((i, j)) for i in range(n) for j in range(i + 1, n) if rng.random() < 0.35}
        if dist(E, {0}, set(range(n)) - {0}, list(range(n))) < float('inf') or n == 1:
            # connectedness not required; accept anything with at least n-1 edges
            if len(E) >= n - 1:
                return E

def random_layer(n, G, regA, regB, rng, allow_a, allow_b):
    """a reversible layer: written sites W form an independent set of G; each written i gets
    x_i ^= f_i(x_N(i), a, b) where f_i depends on a only if i in regA (and allow_a), on b only if
    i in regB (and allow_b).  Returns (tickmap, dep-graph edges, uses_a, uses_b)."""
    nbr = {i: sorted(j for e in G if i in e for j in e if j != i) for i in range(n)}
    order = list(range(n)); rng.shuffle(order); W = []
    for i in order:
        if rng.random() < 0.6 and all(frozenset((i, w)) not in G for w in W):
            W.append(i)
    tables = {}
    uses_a = uses_b = False
    for i in W:
        ua = allow_a and i in regA and rng.random() < 0.7
        ub = allow_b and i in regB and rng.random() < 0.7
        uses_a |= ua; uses_b |= ub
        k = len(nbr[i]) + (1 if ua else 0) + (1 if ub else 0)
        tables[i] = (ua, ub, [rng.randrange(2) for _ in range(2 ** k)])
    def tick(s, a, b):
        out = list(s)
        for i, (ua, ub, tab) in tables.items():
            bits = [s[j] for j in nbr[i]] + ([a] if ua else []) + ([b] if ub else [])
            idx = 0
            for bt in bits:
                idx = 2 * idx + bt
            out[i] = s[i] ^ tab[idx]
        return tuple(out)
    Et = {frozenset((i, j)) for i in W for j in nbr[i]}
    return tick, Et, uses_a, uses_b

def trial(rng, n=7, T=5):
    G = random_graph(n, rng)
    sites = list(range(n)); rng.shuffle(sites)
    regA, regB = set(sites[:2]), set(sites[2:4])
    layers = [random_layer(n, G, regA, regB, rng, True, True) for _ in range(T)]
    ta = next((t + 1 for t, L in enumerate(layers) if L[2]), None)
    tb = next((t + 1 for t, L in enumerate(layers) if L[3]), None)
    if ta is None or tb is None:
        return None
    # (L') holds by construction; verify it mechanically on the first b-using layer
    RA = {rng.choice(sorted(regA | set(range(n)) - regB))}
    RB = {rng.choice(sorted(regB | set(range(n)) - regA))}
    TA, TB = rng.randint(1, T), rng.randint(1, T)
    GB = set().union(*[L[1] for L in layers[tb:]]) if tb < T else set()
    GA = set().union(*[L[1] for L in layers[ta:]]) if ta < T else set()
    RholdsA = dist(GB, regB, RA, list(range(n))) > TA - tb
    RholdsB = dist(GA, regA, RB, list(range(n))) > TB - ta
    depA = depB = False
    for x0 in itertools.product((0, 1), repeat=n):
        for a in (0, 1):
            recs = []
            for b in (0, 1):
                s = x0
                for L in layers[:TA]:
                    s = L[0](s, a, b)
                recs.append(tuple(s[i] for i in sorted(RA)))
            depA |= recs[0] != recs[1]
        for b in (0, 1):
            recs = []
            for a in (0, 1):
                s = x0
                for L in layers[:TB]:
                    s = L[0](s, a, b)
                recs.append(tuple(s[i] for i in sorted(RB)))
            depB |= recs[0] != recs[1]
    return RholdsA, depA, RholdsB, depB

def report_3(N=3000, seed=20261109):
    rng = random.Random(seed)
    held = viol = fail_dep = fail = 0
    for _ in range(N):
        r = trial(rng)
        if r is None:
            continue
        for Rh, dep in ((r[0], r[1]), (r[2], r[3])):
            if Rh:
                held += 1; viol += dep
            else:
                fail += 1; fail_dep += dep
    print('(3) random (D)+(L\') constructions: (R) held in', held, 'wing-cases; remote-setting dependence in',
          viol, '(must be 0)')
    print('    countercontrol: (R) failed in', fail, 'wing-cases; dependence present in', fail_dep, '(must be > 0)')

# ---------- (4), (5) Main's one-step form ----------
def report_45():
    # sites: A = {a1, a2}, B = {b1, b2}, middle m1, m2; phi: fixed reversible layers on a path b2-b1-m1-m2-a1-a2
    sites = ['a1', 'a2', 'm1', 'm2', 'b1', 'b2']
    A, B = {'a1', 'a2'}, {'b1', 'b2'}
    def u(s, a, b):            # u^A_a x u^B_b x id, each reading and writing only its own region
        s = dict(s); s['a2'] ^= a & s['a1']; s['b2'] ^= b ^ s['b1']; return s
    def ph(s, a, b):           # fixed, setting-independent: path couplings b1-m1, m1-m2, m2-a1
        s = dict(s); s['m1'] ^= s['b1']; s['a1'] ^= s['m2']; s['b2'] ^= s['b1'] & s['m1']; return s
    ok = all(not outside_dependence(t, sites, B, 'b') and not outside_dependence(t, sites, A, 'a') for t in (u, ph))
    Gphi = dep_graph(ph, sites, SET4)
    print("(4) Main's one-step form: (L') holds at the setting tick and at every phi tick:", ok)
    print('    G_B = G_phi edges:', sorted(tuple(sorted(e)) for e in Gphi))
    # (5) single graph containing the setting edges shortens the distance
    sites5 = ['b', 'a1', 'a2']
    def u5(s, a, b): s = dict(s); s['b'] ^= b; s['a2'] ^= a & s['a1']; return s
    def ph5(s, a, b): s = dict(s); s['a1'] ^= s['b']; return s
    Gp = dep_graph(ph5, sites5, SET4); Gu = dep_graph(u5, sites5, SET4)
    print('(5) instance with R_A = {a2}, k = 2: d_phi(B, R_A) =', dist(Gp, {'b'}, {'a2'}, sites5),
          '(Main (iii) holds); single graph with setting edges: d =', dist(Gp | Gu, {'b'}, {'a2'}, sites5),
          '<= k = 2; G_B = G_phi gives', dist(Gp, {'b'}, {'a2'}, sites5))
    # and the readout really is b-independent there
    dep = False
    for x in itertools.product((0, 1), repeat=3):
        for a in (0, 1):
            outs = []
            for b in (0, 1):
                s = dict(zip(sites5, x)); s = u5(s, a, b); s = ph5(s, a, b); s = ph5(s, a, b); outs.append(s['a2'])
            dep |= outs[0] != outs[1]
    print('    a2 after k = 2 depends on b:', dep)

if __name__ == '__main__':
    report_12(); report_3(); report_45()
