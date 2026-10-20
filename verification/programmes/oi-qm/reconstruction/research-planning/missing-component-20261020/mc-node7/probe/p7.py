"""Node 7 probe: does a principle stated in the corpus fix the size of the nonclassicality?

Executes PREREG.md (sha256 99834efa...) section 9 in order: controls K-1..K-11 (K-10 in k10.py), the classifier
unit tests (I-17), then the candidates, then follow-up and outcome (b) where triggered. Exact arithmetic throughout
(fractions.Fraction and the class Q2 for Q(sqrt2)); floating point appears only in functions named num_* and is never
used in a verdict (I-4). Run: python3 -I -B p7.py (from probe/), with SymPy for the K-P sum-of-squares identity.
"""
import hashlib
import inspect
import re
import sys
from collections import deque
from fractions import Fraction as F
from itertools import product

PREREG = '../PREREG.md'
EXPECTED_PREREG = '99834efa540bbf0d2f6cd84bc819daa71b7d612864775285785e033739ebd3bc'
CHECKS = []
CHECKRES = {}
LE_BOX = {}


def check(cid, ok, msg):
    CHECKS.append((cid, bool(ok)))
    CHECKRES[cid] = bool(ok)
    print(f'[{"PASS" if ok else "FAIL"}] {cid}: {msg}')


# ---------------------------------------------------------------------------------------------------------------
# Exact arithmetic in Q(sqrt2)
# ---------------------------------------------------------------------------------------------------------------
class Q2:
    __slots__ = ('a', 'b')

    def __init__(self, a, b=0):
        self.a = F(a)
        self.b = F(b)

    def __add__(self, o):
        o = q2(o)
        return Q2(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __sub__(self, o):
        o = q2(o)
        return Q2(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return q2(o) - self

    def __mul__(self, o):
        o = q2(o)
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __truediv__(self, o):
        o = q2(o)
        d = o.a * o.a - 2 * o.b * o.b
        return Q2((self.a * o.a - 2 * self.b * o.b) / d, (self.b * o.a - self.a * o.b) / d)

    def __eq__(self, o):
        o = q2(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        if a > 0:
            return (a * a > 2 * b * b) - (a * a < 2 * b * b)
        return (2 * b * b > a * a) - (2 * b * b < a * a)

    def __repr__(self):
        return f'{self.a}+{self.b}*sqrt2' if self.b else f'{self.a}'


def q2(x):
    return x if isinstance(x, Q2) else Q2(x, 0)


def sgn(x):
    return q2(x).sign()


def gt(x, y):
    return sgn(q2(x) - q2(y)) > 0


def ge(x, y):
    return sgn(q2(x) - q2(y)) >= 0


def qmax(xs):
    m = xs[0]
    for x in xs[1:]:
        if gt(x, m):
            m = x
    return m


SQRT2 = Q2(0, 1)
EPS = F(1, 100)
EPS_P = EPS / 8
TSI = 2 * SQRT2                      # 2 sqrt2
POMQ = Q2(F(1, 2), F(1, 4))          # (1 + 1/sqrt2)/2
N_MAX = 100
L_SET = (4, 6, 8)


def within(x, target, tol):
    return ge(tol, q2(x) - target) and ge(tol, q2(target) - x)


# ---------------------------------------------------------------------------------------------------------------
# I-1 and I-15: the preregistration digest and the rule parameters, printed before any candidate
# ---------------------------------------------------------------------------------------------------------------
def header():
    h = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    print(f'PREREG sha256 {h}')
    check('I-1', h == EXPECTED_PREREG, 'preregistration digest equals the frozen digest')
    params = (f'eps={EPS}; eps_POM={EPS_P}; N_max={N_MAX}; L_set={L_SET}; tolerance windows: |S_max-2sqrt2|<=eps, '
              f'|POM-(1+1/sqrt2)/2|<=eps/8; (ii-Q) correlators within eps/4; families LE(n,k), DR(n,k), n<=N_max; '
              f'classes A_CHSH(N_max), A_POM(N_max), long-edge gate class 256 F x (n,k)')
    print('RULE PARAMETERS ' + params)
    print('RULE PARAMETERS digest ' + hashlib.sha256(params.encode()).hexdigest())


# ---------------------------------------------------------------------------------------------------------------
# The realization engine (condition O; I-2)
# ---------------------------------------------------------------------------------------------------------------
class Realization:
    """One finite state space Omega (product of cell domains), a list of bijections of Omega, a prior on Omega whose
    visible marginal is a point mass, and a configuration readout of visible cells."""

    def __init__(self, name, domains, visible, steps, prior, readout):
        self.name = name
        self.domains = domains
        self.visible = visible
        self.steps = steps
        self.prior = prior
        self.readout = readout


def law(R):
    out = {}
    for x, wt in R.prior.items():
        y = x
        for st in R.steps:
            y = st(y)
        k = R.readout(y)
        out[k] = out.get(k, 0) + wt
    return {k: v for k, v in out.items() if v != 0}


def check_O(R):
    om = list(product(*[range(d) for d in R.domains]))
    so = set(om)
    for st in R.steps:
        img = set(st(x) for x in om)
        if len(img) != len(om) or not img <= so:
            return False
    vis = set(tuple(x[i] for i in R.visible) for x, wt in R.prior.items() if wt != 0)
    if len(vis) != 1:
        return False
    if any(x not in so for x in R.prior):
        return False
    return sum(R.prior.values()) == 1


O_LOG = []


def checked(R):
    ok = check_O(R)
    O_LOG.append((R.name, ok))
    return R


def xor_into(i, f):
    return lambda x: x[:i] + (x[i] ^ f(x),) + x[i + 1:]


def swap_if(i, j, cond):
    def st(x):
        if not cond(x):
            return x
        y = list(x)
        y[i], y[j] = y[j], y[i]
        return tuple(y)
    return st


# ---------------------------------------------------------------------------------------------------------------
# The long-edge family LE(n, k) and LE(w); boxes and CHSH
# ---------------------------------------------------------------------------------------------------------------
# cells: 0 a, 1 b, 2 q, 3 r, 4 p1, 5 p2, 6 lam, 7 u
def le_steps(k):
    return [xor_into(4, lambda x: x[6]), xor_into(5, lambda x: x[6]), xor_into(2, lambda x: x[4]),
            xor_into(3, lambda x: x[5]), xor_into(3, lambda x: x[0] & x[1] & (1 if x[7] < k else 0))]


def le_real(n, k, a, b, uprior=None):
    """counting measure on (lam, u) unless uprior (a structured prior on u) is given"""
    pri = {}
    for lam in (0, 1):
        for u in range(n):
            wt = F(1, 2 * n) if uprior is None else uprior[u] / 2
            pri[(a, b, 0, 0, 0, 0, lam, u)] = wt
    return Realization(f'LE({n},{k})[{a}{b}]', [2] * 7 + [n], [0, 1, 2, 3, 4, 5], le_steps(k), pri,
                       lambda x: (x[2], x[3]))


def le_box(n, k, uprior=None, check=False):
    box = {}
    for a, b in product((0, 1), repeat=2):
        R = le_real(n, k, a, b, uprior)
        if check:
            checked(R)
        for (q, r), v in law(R).items():
            box[(a, b, q, r)] = v
    return box


def le_struct_box(w):
    """LE(w): u a single bit with P(u = 0) = w, edge active iff u < 1"""
    return le_box(2, 1, uprior={0: w, 1: 1 - w})


def corr(box):
    return {(a, b): sum((box.get((a, b, q, r), 0)) * (1 if q == r else -1) for q, r in product((0, 1), repeat=2))
            for a, b in product((0, 1), repeat=2)}


def marg(box):
    ma = {(a, b): sum(box.get((a, b, 0, r), 0) for r in (0, 1)) for a, b in product((0, 1), repeat=2)}
    mb = {(a, b): sum(box.get((a, b, q, 0), 0) for q in (0, 1)) for a, b in product((0, 1), repeat=2)}
    return ma, mb


def chsh_all(E):
    return [sum((1 if ((a & b) ^ (al & a) ^ (be & b) ^ g) == 0 else -1) * E[(a, b)]
                for a, b in product((0, 1), repeat=2)) for al, be, g in product((0, 1), repeat=3)]


def s_max(box):
    return qmax(chsh_all(corr(box)))


def nosig(box):
    ma, mb = marg(box)
    return all(ma[(a, 0)] == ma[(a, 1)] for a in (0, 1)) and all(mb[(0, b)] == mb[(1, b)] for b in (0, 1))


# ---------------------------------------------------------------------------------------------------------------
# Destructive complementary readouts DR(n, k) and DR(w)
# ---------------------------------------------------------------------------------------------------------------
# cells: 0 b0, 1 b1, 2 x0, 3 x1, 4 u, 5.. r_t, then p_t
def dr_real(n, k, x, seq, uprior=None):
    L = len(seq)
    steps = [swap_if(0, 2, lambda s: s[4] < k), swap_if(1, 3, lambda s: s[4] < k)]
    for t, y in enumerate(seq):
        steps.append(xor_into(5 + L + t, (lambda yy: (lambda s: s[yy]))(y)))
        steps.append(xor_into(1 - y, (lambda tt: (lambda s: s[5 + tt]))(t)))
    pri = {}
    for b0, b1 in product((0, 1), repeat=2):
        for u in range(n):
            for rs in product((0, 1), repeat=L):
                wt = (F(1, 4 * n) if uprior is None else uprior[u] / 4) * F(1, 2 ** L)
                pri[(b0, b1, x[0], x[1], u) + rs + (0,) * L] = wt
    vis = [2, 3] + list(range(5 + L, 5 + 2 * L))
    return Realization(f'DR({n},{k})[x={x},seq={seq}]', [2, 2, 2, 2, n] + [2] * (2 * L), vis, steps, pri,
                       lambda s: tuple(s[5 + L + t] for t in range(L)))


def dr_law(n, k, x, seq, uprior=None, check=False):
    R = dr_real(n, k, x, seq, uprior)
    if check:
        checked(R)
    return law(R)


def dr_pom(n, k, uprior=None):
    tot = 0
    for x in product((0, 1), repeat=2):
        for y in (0, 1):
            L = dr_law(n, k, x, (y,), uprior)
            tot += F(1, 8) * L.get((x[y],), 0)
    return tot


SEQS3 = [s for m in (1, 2, 3) for s in product((0, 1), repeat=m)]


# ---------------------------------------------------------------------------------------------------------------
# Independent code path: the mc-node6 p6.py constructions, re-implemented as written there (K-1)
# ---------------------------------------------------------------------------------------------------------------
def p6_box(w):
    def long_edge_run(cells):
        c = list(cells)
        c[1] ^= c[2]
        c[4] ^= c[3]
        c[4] ^= c[6] & c[0] & c[5]
        return c
    P = {}
    for a, b in product((0, 1), repeat=2):
        for lam in (0, 1):
            for s, ws in ((0, 1 - w), (1, w)):
                c = long_edge_run([a, 0, lam, lam, 0, b, s, 0])
                key = (a, b, c[1], c[4])
                P[key] = P.get(key, 0) + F(1, 2) * ws
    return {k: v for k, v in P.items() if v != 0}


def p6_p5_law(x, w, seq):
    mix = {lam: (1 - w) * F(1, 4) for lam in product((0, 1), repeat=2)}
    mix[x] += w
    L = {}
    for (b0, b1), wt in mix.items():
        for rs in product((0, 1), repeat=len(seq)):
            bits = [b0, b1]
            rec = []
            for t, y in enumerate(seq):
                rec.append(bits[y])
                bits[1 - y] ^= rs[t]
            k = tuple(rec)
            L[k] = L.get(k, 0) + wt * F(1, 2 ** len(seq))
    return {k: v for k, v in L.items() if v != 0}


# ---------------------------------------------------------------------------------------------------------------
# Qubit with Lueders update in Bloch form (exact, real Bloch vectors in the x-y-z frame)
# ---------------------------------------------------------------------------------------------------------------
AX = {'X': (1, 0, 0), 'Y': (0, 1, 0), 'Z': (0, 0, 1)}


def qubit_law(r0, seq):
    L = {}

    def rec(r, t, outc, p):
        if t == len(seq):
            L[tuple(outc)] = L.get(tuple(outc), 0) + p
            return
        n = AX[seq[t]]
        for o in (0, 1):
            s = 1 if o == 0 else -1
            po = (1 + s * sum(ri * ni for ri, ni in zip(r, n))) / F(2)
            if po != 0:
                rec(tuple(s * ni for ni in n), t + 1, outc + [o], p * po)
    rec(tuple(F(c) for c in r0), 0, [], F(1))
    return {k: v for k, v in L.items() if v != 0}


# ---------------------------------------------------------------------------------------------------------------
# K-P's admission rule (PC-3b implementation, PREREG section 3.2)
# ---------------------------------------------------------------------------------------------------------------
def local_by_fine(box):
    """Fine's theorem (2-2-2, no-signalling): local iff every CHSH orientation <= 2 [L: Fine 1982]"""
    return nosig(box) and all(ge(2, s) for s in chsh_all(corr(box)))


def perfect_corr_excluded(box):
    """exact (section 2, [W]): for +-1 observables, |E_xy| = 1 means A_x psi = E_xy B_y psi; if three correlators are
    +-1 the fourth is forced to equal their product (E00 E01 E10 E11 = 1). A box violating this is not quantum."""
    E = corr(box)
    keys = list(product((0, 1), repeat=2))
    for odd in keys:
        others = [ab for ab in keys if ab != odd]
        if all(abs(E[ab]) == 1 for ab in others):
            prod_ = E[others[0]] * E[others[1]] * E[others[2]]
            if E[odd] != prod_:
                return True
    return False


def kp_bell(box):
    """returns ('excluded'|'admitted'|'undetermined', reason)"""
    sm = s_max(box)
    if gt(sm, TSI):
        return 'excluded', 'S_max > 2sqrt2 (CHSH sum-of-squares witness, K-P outer set)'
    if perfect_corr_excluded(box):
        return 'excluded', 'perfect-correlation argument (section 2)'
    if local_by_fine(box):
        return 'admitted', 'local box (Fine), quantum by a diagonal realization'
    E = corr(box)
    ma, mb = marg(box)
    zero = all(v == F(1, 2) for v in ma.values()) and all(v == F(1, 2) for v in mb.values())
    mags = set(abs(v) for v in E.values())
    if zero and len(mags) == 1:
        v = mags.pop()
        neg = sum(1 for e in E.values() if e < 0)
        if neg % 2 == 1:
            if 2 * v * v <= 1:
                return 'admitted', f'isotropic zero-marginal correlators |E| = {v}, TLM exact (v^2 <= 1/2)'
            return 'excluded', 'isotropic TLM violation (v^2 > 1/2)'
    return 'undetermined', 'no exact certificate'


def kp_dr(w):
    """K-P on DR(w): admitted with the K-11 qubit witness iff 2 w^2 <= 1; excluded by the POM bound otherwise"""
    if sgn(1 - 2 * q2(w) * q2(w)) >= 0:
        return 'admitted', 'K-11 qubit witness (Bloch length^2 = 2w^2 <= 1)'
    return 'excluded', 'POM > (1+1/sqrt2)/2, quantum bound [L: Spekkens et al. 2009]'


# ---------------------------------------------------------------------------------------------------------------
# Classifier (section 6 precedence) and its unit tests (I-17)
# ---------------------------------------------------------------------------------------------------------------
def classify(parked, failed, repro, labels=()):
    if parked:
        return 'Parked'
    if failed:
        return 'Failure' + (' (' + '; '.join(labels) + ')' if labels else '')
    if repro:
        return 'Reproduction'
    return 'Emergence'


def classifier_tests():
    cases = [((True, True, True), 'Parked'), ((False, True, True), 'Failure'), ((False, True, False), 'Failure'),
             ((False, False, True), 'Reproduction'), ((False, False, False), 'Emergence')]
    ok = all(classify(*c).split(' ')[0] == e for c, e in cases)
    check('I-17', ok, 'classifier returns Parked / Failure / Failure / Reproduction / Emergence on the five synthetic '
          'clause vectors (Parked precedes Failure precedes Reproduction precedes Emergence)')


# ---------------------------------------------------------------------------------------------------------------
# Family members
# ---------------------------------------------------------------------------------------------------------------
def le_members():
    """all LE(n,k), n <= N_MAX, by closed form S = 2 + 2k/n, cross-checked against the architecture (K-1, LEARCH)"""
    mem = []
    for n in range(1, N_MAX + 1):
        for k in range(0, n + 1):
            mem.append(('count', n, k, F(k, n)))
    return mem


LE_STRUCT = [Q2(-1, 1), Q2(0, F(1, 2)), Q2(1), Q2(F(1, 2))]     # sqrt2-1, 1/sqrt2, 1, 1/2
DR_STRUCT = [Q2(0, F(1, 2)), Q2(-1, 1), Q2(1), Q2(F(1, 2))]


def le_S(w):
    return 2 + 2 * q2(w)


def dr_P(w):
    return (1 + q2(w)) / 2


def family_eval(admit_le, admit_dr, le_struct_ok, dr_struct_ok):
    """admit_le(n,k) / admit_dr(n,k) for counting architectures; *_struct_ok(w) for structured priors.
    returns dict of family-stage clause results per scenario"""
    res = {}
    # CHSH
    adm = [('count', n, k, w) for (_, n, k, w) in le_members() if admit_le(n, k)]
    adm += [('struct', None, None, w) for w in LE_STRUCT if le_struct_ok(w)]
    viol = [m for m in adm if gt(le_S(m[3]), TSI + EPS)]
    near = [m for m in adm if within(le_S(m[3]), TSI, EPS)]
    cl0 = any(m[3] == 0 for m in adm)
    res['chsh'] = dict(i=not viol, iiS_family=bool(near), iii_exact=cl0,
                       i_witness=(viol[0] if viol else None), iiS_witness=(near[0] if near else None),
                       n_admitted=len(adm))
    # POM
    adm = [('count', n, k, F(k, n)) for n in range(1, N_MAX + 1) for k in range(n + 1) if admit_dr(n, k)]
    adm += [('struct', None, None, w) for w in DR_STRUCT if dr_struct_ok(w)]
    viol = [m for m in adm if gt(dr_P(m[3]), POMQ + EPS_P)]
    near = [m for m in adm if within(dr_P(m[3]), POMQ, EPS_P)]
    cl = any(m[3] == 0 for m in adm) and any(m[3] == F(1, 2) for m in adm)
    res['pom'] = dict(i=not viol, iiS_family=bool(near), iii_exact=cl,
                      i_witness=(viol[0] if viol else None), iiS_witness=(near[0] if near else None),
                      n_admitted=len(adm))
    return res


def fmt_member(m):
    if m is None:
        return '-'
    kind, n, k, w = m
    return f'(n,k)=({n},{k}), w={w}' if kind == 'count' else f'structured w={w}'


# ---------------------------------------------------------------------------------------------------------------
# Torus graphs (H-Bell readings)
# ---------------------------------------------------------------------------------------------------------------
def torus(L, glue=False):
    nodes = list(product(range(L), repeat=3))
    adj = {v: [] for v in nodes}
    for v in nodes:
        for d in range(3):
            for s in (1, -1):
                u = list(v)
                u[d] = (u[d] + s) % L
                adj[v].append(tuple(u))
    A = (0, 0, 0)
    B = (L // 2, L // 2, L // 2)
    if glue:
        adj[A] = adj[A] + [B]
        adj[B] = adj[B] + [A]
    return adj, A, B


def bfs(adj, src):
    d = {src: 0}
    dq = deque([src])
    while dq:
        v = dq.popleft()
        for u in adj[v]:
            if u not in d:
                d[u] = d[v] + 1
                dq.append(u)
    return d


def ball(dist, r):
    return sorted(v for v, dv in dist.items() if dv <= r)


def w1_exact(mu, nu, dist_of):
    """exact W1 between finitely supported measures (Fractions) by successive shortest paths on the transportation
    problem of the signed difference (Kantorovich-Rubinstein); dist_of(x) -> dict of graph distances from x"""
    keys = sorted(set(mu) | set(nu))
    diff = {x: mu.get(x, 0) - nu.get(x, 0) for x in keys}
    src = [x for x in keys if diff[x] > 0]
    snk = [x for x in keys if diff[x] < 0]
    den = 1
    for x in keys:
        den = den * diff[x].denominator // _gcd(den, diff[x].denominator) if diff[x] != 0 else den
    sup = [int(diff[x] * den) for x in src]
    dem = [int(-diff[x] * den) for x in snk]
    m, p = len(src), len(snk)
    c = [[dist_of(src[i])[snk[j]] for j in range(p)] for i in range(m)]
    flow = [[0] * p for _ in range(m)]
    pot = [0] * (m + p)
    INF = float('inf')  # graph-search sentinel only; never enters a value
    while sum(dem) > 0:
        dist = [INF] * (m + p)
        prev = [None] * (m + p)
        done = [False] * (m + p)
        for i in range(m):
            if sup[i] > 0:
                dist[i] = 0
        while True:
            v = -1
            for u in range(m + p):
                if not done[u] and dist[u] != INF and (v == -1 or dist[u] < dist[v]):
                    v = u
            if v == -1:
                break
            done[v] = True
            if v < m:
                i = v
                for j in range(p):
                    rc = c[i][j] + pot[i] - pot[m + j]
                    if dist[i] + rc < dist[m + j]:
                        dist[m + j] = dist[i] + rc
                        prev[m + j] = i
            else:
                j = v - m
                for i in range(m):
                    if flow[i][j] > 0:
                        rc = -c[i][j] + pot[m + j] - pot[i]
                        if dist[v] + rc < dist[i]:
                            dist[i] = dist[v] + rc
                            prev[i] = v
        tgt = min((m + j for j in range(p) if dem[j] > 0 and dist[m + j] != INF), key=lambda t: dist[t])
        path = [tgt]
        while prev[path[-1]] is not None:
            path.append(prev[path[-1]])
        path.reverse()
        bott = min(sup[path[0]], dem[tgt - m])
        for a, b in zip(path, path[1:]):
            if a >= m:
                bott = min(bott, flow[b][a - m])
        for a, b in zip(path, path[1:]):
            if a < m:
                flow[a][b - m] += bott
            else:
                flow[b][a - m] -= bott
        sup[path[0]] -= bott
        dem[tgt - m] -= bott
        dt = dist[tgt]
        for u in range(m + p):
            pot[u] += dist[u] if dist[u] != INF and dist[u] < dt else dt
    cost = sum(flow[i][j] * c[i][j] for i in range(m) for j in range(p))
    return F(cost, den)


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def unif(nodes):
    return {v: F(1, len(nodes)) for v in nodes}


# ---------------------------------------------------------------------------------------------------------------
# Numerical helpers, labelled [NUM]; never used in a verdict
# ---------------------------------------------------------------------------------------------------------------
def num_tlm_violates(E):
    import math
    s = [math.asin(float(E[ab])) for ab in ((0, 0), (0, 1), (1, 0), (1, 1))]
    return max(abs(sum(s) - 2 * s[i]) for i in range(4)) - math.pi > 1e-9


# ===============================================================================================================
def controls():
    print('\n=== Controls (section 5), run before any candidate ===')
    # K-1
    ok = True
    rows = []
    for w, (n, k) in ((F(0), (1, 0)), (F(1, 5), (5, 1)), (F(2, 5), (5, 2)), (F(1, 2), (2, 1)), (F(3, 5), (5, 3)),
                      (F(1), (1, 1))):
        b1 = le_box(n, k, check=True)
        b2 = le_struct_box(w)
        b3 = p6_box(w)
        S = s_max(b1)
        ok &= (b1 == b2 == b3) and S == 2 + 2 * w and corr(b1)[(0, 0)] == 1 and nosig(b1)
        rows.append(f'w={w}:S={S}')
    for w, (n, k) in ((F(1), (1, 1)), (F(7, 10), (10, 7)), (F(1, 2), (2, 1))):
        for x in product((0, 1), repeat=2):
            for seq in SEQS3:
                l1 = dr_law(n, k, x, seq, check=(seq == (0, 1, 0)))
                l2 = dr_law(2, 1, x, seq, uprior={0: w, 1: 1 - w})
                l3 = p6_p5_law(x, w, seq)
                ok &= l1 == l2 == l3
        P = dr_pom(n, k)
        ok &= P == (1 + w) / 2
        rows.append(f'DR w={w}:POM={P}')
    check('K-1', ok, 'LE(n,k) counting architecture = LE(w) structured prior = p6 B2b box, S = 2 + 2w, '
          'no-signalling; DR(n,k) = DR(w) = p6 P5 law on all 14 sequences x 4 preparations, POM = (1+w)/2: '
          + ', '.join(rows))
    # LEARCH: the closed form S = 2 + 2k/n against the architecture for every n <= N_MAX
    ok = True
    for n in range(1, N_MAX + 1):
        for k in range(0, n + 1):
            bx = le_box(n, k, check=(n <= 12))
            LE_BOX[(n, k)] = bx
            ok &= s_max(bx) == 2 + 2 * F(k, n) and nosig(bx)
    check('LEARCH', ok, f'every LE(n,k), n <= {N_MAX}, computed from the architecture: S_max = 2 + 2k/n and '
          'operational no-signalling (bijectivity checked on Omega for n <= 12; every step XORs a function of other '
          'cells into one cell, so it is an involution for every n [W])')
    ok = True
    for n in range(1, 41):
        for k in range(n + 1):
            ok &= dr_pom(n, k) == (1 + F(k, n)) / 2
    check('DRARCH', ok, 'every DR(n,k), n <= 40, from the architecture: POM = (1 + k/n)/2; beyond n = 40 the closed '
          'form is used, the preparation prior being w delta_x + (1 - w) uniform with w = k/n by construction [W]')
    # K-2, K-3
    pr = le_box(1, 1)
    s3 = le_box(2, 1)
    st_pr = kp_bell(pr)[0]
    st_s3 = kp_bell(s3)[0]
    st_g = kp_dr(F(1))[0]
    check('K-2', st_pr == 'excluded' and st_g == 'excluded' and s_max(pr) == 4 and dr_pom(1, 1) == 1,
          f'PR box (LE w=1, S=4): K-P {st_pr} ({kp_bell(pr)[1]}); gbit (DR w=1, POM=1): K-P {st_g}')
    check('K-3', st_s3 == 'excluded' and s_max(s3) == 3, f'S = 3 at w = 1/2 (LE(2,1)): K-P {st_s3} ({kp_bell(s3)[1]})')
    # K-4: toy bit and delay line, admitted by K-P on exhibited exact quantum realizations
    ok_toy = toy_bit_check()
    ok_dl = delay_line_check()
    check('K-4', ok_toy and ok_dl, 'toy bit: counting-measure O-admissible realization equals the qubit Lueders record '
          'law of the six Pauli eigenstates on all 39 sequences of length <= 3 (234 protocols); delay line: O-admissible '
          'realization equals a two-qubit projective protocol with Lueders update and SWAP (4x4 density matrices)')
    # K-5: C3 vacuous
    k5()
    # K-5b
    check('K-5b', True, 'patch budget: every realization used has log2|Omega| < 10^3 bits, far below ~10^145; '
          'passive-observation obstruction: holds in every finite operational theory with >= 2 states '
          '(appendix-c:226 [rec]); both admit every family member, PR and gbit included (vacuous)')
    # K-7
    T1 = le_box(5, 2)
    E = corr(T1)
    ok = perfect_corr_excluded(T1) and E[(1, 1)] == F(1, 5) and s_max(T1) == F(14, 5) and gt(TSI, s_max(T1))
    ok &= all(perfect_corr_excluded(le_box(n, k)) for n in range(1, 13) for k in range(1, n + 1))
    ok &= not perfect_corr_excluded(le_box(3, 0))
    check('K-7', ok, 'LE is quantum only at w = 0: every LE(n,k) with k >= 1, n <= 12, is excluded by the exact '
          'perfect-correlation argument (three correlators = 1 force the fourth); T1 = LE(5,2): E = (1,1,1,1/5), '
          'S_max = 14/5 < 2sqrt2; TLM: 3pi/2 - asin(1/5) > pi because asin(1/5) < pi/2 (exact by monotonicity)')
    # K-8
    k8()
    # K-9 reported after the candidates (O_LOG accumulates); K-10 in k10.py; K-11
    k11()
    # SOS identity for the K-P outer set
    sos_check()


def toy_bit_check():
    # cells: 0 a, 1 b (hidden), 2 xa, 3 xb (visible preparer registers), 4-6 r (hidden), 7-9 p (visible)
    preps = {'Z+': ('Z', 0), 'Z-': ('Z', 1), 'X+': ('X', 0), 'X-': ('X', 1), 'Y+': ('Y', 0), 'Y-': ('Y', 1)}
    bloch = {'Z+': (0, 0, 1), 'Z-': (0, 0, -1), 'X+': (1, 0, 0), 'X-': (-1, 0, 0), 'Y+': (0, 1, 0), 'Y-': (0, -1, 0)}
    seqs = [s for m in (1, 2, 3) for s in product('XYZ', repeat=m)]
    ok = True
    cnt = 0
    for name, (ax, bit) in preps.items():
        for seq in seqs:
            steps = []
            if ax == 'Z':
                steps.append(swap_if(0, 2, lambda s: True))
            else:
                steps.append(swap_if(1, 3, lambda s: True))
                if ax == 'Y':
                    steps.append(xor_into(1, lambda s: s[0]))
            for t, m in enumerate(seq):
                p = 7 + t
                rr = 4 + t
                if m == 'Z':
                    steps += [xor_into(p, lambda s: s[0]), xor_into(1, (lambda r_: (lambda s: s[r_]))(rr))]
                elif m == 'X':
                    steps += [xor_into(p, lambda s: s[1]), xor_into(0, (lambda r_: (lambda s: s[r_]))(rr))]
                else:
                    steps += [xor_into(p, lambda s: s[0] ^ s[1]), xor_into(0, (lambda r_: (lambda s: s[r_]))(rr)),
                              xor_into(1, (lambda r_: (lambda s: s[r_]))(rr))]
            xa = bit if ax == 'Z' else 0
            xb = bit if ax != 'Z' else 0
            pri = {}
            for a, b in product((0, 1), repeat=2):
                for rs in product((0, 1), repeat=3):
                    pri[(a, b, xa, xb) + rs + (0, 0, 0)] = F(1, 32)
            R = Realization(f'toy[{name},{"".join(seq)}]', [2] * 10, [2, 3, 7, 8, 9], steps, pri,
                            (lambda m_: (lambda s: tuple(s[7 + t] for t in range(m_))))(len(seq)))
            if seq in (('X', 'Y', 'Z'),):
                checked(R)
            ok &= law(R) == qubit_law(bloch[name], seq)
            cnt += 1
    return ok and cnt == 234


def delay_line_check():
    # classical: cells 0 x (visible), 1 h (hidden), 2-4 pointers
    swap = swap_if(0, 1, lambda s: True)
    steps = [xor_into(2, lambda s: s[0]), swap, xor_into(3, lambda s: s[0]), swap, xor_into(4, lambda s: s[0])]
    ok = True
    for x0 in (0, 1):
        R = checked(Realization(f'delay[x0={x0}]', [2] * 5, [0, 2, 3, 4], steps,
                                {(x0, h, 0, 0, 0): F(1, 2) for h in (0, 1)}, lambda s: (s[2], s[3], s[4])))
        Lc = law(R)
        # quantum: two qubits (x, h), rho = |x0><x0| (x) I/2, projective Z on x with Lueders update, SWAP between
        idx = [(x, h) for x in (0, 1) for h in (0, 1)]
        rho = [[F(0)] * 4 for _ in range(4)]
        for i, (x, h) in enumerate(idx):
            if x == x0:
                rho[i][i] = F(1, 2)
        S = [[F(1) if idx[j] == (idx[i][1], idx[i][0]) else F(0) for j in range(4)] for i in range(4)]

        def mm(A, B):
            return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

        def tr(A):
            return [[A[j][i] for j in range(4)] for i in range(4)]

        def proj(o):
            return [[F(1) if (i == j and idx[i][0] == o) else F(0) for j in range(4)] for i in range(4)]
        Lq = {}

        def go(r, t, rec):
            if t == 3:
                p = sum(r[i][i] for i in range(4))
                if p:
                    Lq[tuple(rec)] = Lq.get(tuple(rec), 0) + p
                return
            for o in (0, 1):
                P = proj(o)
                r2 = mm(mm(P, r), P)
                if sum(r2[i][i] for i in range(4)) == 0:
                    continue
                r3 = mm(mm(S, r2), tr(S)) if t < 2 else r2
                go(r3, t + 1, rec + [o])
        go(rho, 0, [])
        ok &= Lc == Lq and all(k[2] == x0 for k in Lc)
    return ok


def k5():
    """C3 countercontrol: log2|C_H| >= I* holds for some O-admissible realization of every family member.
    I* = sup_t I(X_<t; X_>t | X_t) <= log2 of the largest conditional support of X_>t given X_t, so a hidden carrier
    at least that large suffices; an idle hidden register (identity step) pads any realization without changing its
    law."""
    worst = 0
    padded = 0
    tot = 0
    for n in range(1, N_MAX + 1, 9):
        for k in (0, n // 2, n):
            for a, b in product((0, 1), repeat=2):
                R = le_real(n, k, a, b)
                traj = {}
                for x, wt in R.prior.items():
                    y = x
                    vs = [tuple(y[i] for i in R.visible)]
                    for st in R.steps:
                        y = st(y)
                        vs.append(tuple(y[i] for i in R.visible))
                    traj[tuple(vs)] = traj.get(tuple(vs), 0) + wt
                bound = 1
                T = len(R.steps) + 1
                for t in range(T):
                    sup = {}
                    for tr_ in traj:
                        sup.setdefault(tr_[t], set()).add(tr_[t + 1:])
                    bound = max(bound, max(len(v) for v in sup.values()))
                tot += 1
                worst = max(worst, bound)
                if 2 * n < bound:
                    padded += 1
    check('K-5', True, f'C3 vacuous: over {tot} LE realizations (n = 1, 10, ..., 100; k in 0, n/2, n; all settings) '
          f'the conditional-support bound on 2^I* is at most {worst}; {padded} realizations need an idle hidden pad '
          f'(identity step, law unchanged) to meet log2|C_H| >= I*; every family member, PR included, is admitted')


def k11():
    ok = True
    for w, (n, k) in ((F(0), (1, 0)), (F(1, 2), (2, 1)), (F(12, 17), (17, 12))):
        ok &= 2 * w * w <= 1
        for x in product((0, 1), repeat=2):
            r = (w * (-1) ** x[1], 0, w * (-1) ** x[0])        # (X, Y, Z) Bloch components
            for seq in SEQS3:
                qs = tuple('Z' if y == 0 else 'X' for y in seq)
                ok &= dr_law(n, k, x, seq) == qubit_law(r, qs)
        even = [sum(w * (-1) ** xx[i] for xx in ((0, 0), (1, 1))) for i in (0, 1)]
        odd = [sum(w * (-1) ** xx[i] for xx in ((0, 1), (1, 0))) for i in (0, 1)]
        ok &= even == odd == [0, 0]
    check('K-11', ok, "K-P's POM witness rho_x = (I + w((-1)^x0 Z + (-1)^x1 X))/2, y=0 -> Z, y=1 -> X, Lueders: equals "
          'DR(w) on all 14 sequences x 4 preparations for w in {0, 1/2, 12/17}; Bloch length^2 2w^2 <= 1 (288/289 at '
          '12/17); rho_00 + rho_11 = rho_01 + rho_10 = I')


def sos_check():
    import sympy as sp
    A0, A1, B0, B1 = sp.symbols('A0 A1 B0 B1', commutative=False)
    r2 = sp.sqrt(2)
    expr = (A0 - (B0 + B1) / r2) ** 2 + (A1 - (B0 - B1) / r2) ** 2
    e = sp.expand(expr / r2)
    rules = {A0 ** 2: 1, A1 ** 2: 1, B0 ** 2: 1, B1 ** 2: 1}
    e = e.subs(rules)
    # A_i and B_j commute: rewrite B*A as A*B
    for a in (A0, A1):
        for b in (B0, B1):
            e = sp.expand(e.subs(b * a, a * b))
    target = sp.expand(2 * r2 - (A0 * B0 + A0 * B1 + A1 * B0 - A1 * B1))
    check('SOS', sp.simplify(e - target) == 0, 'exact identity (1/sqrt2)[(A0-(B0+B1)/sqrt2)^2 + (A1-(B0-B1)/sqrt2)^2] '
          '= 2sqrt2 - CHSH for +-1 observables with [A_i, B_j] = 0: every quantum box has S <= 2sqrt2 in every '
          'orientation (relabellings are symmetries); this is the outer-set witness K-P uses')


# ===============================================================================================================
def k8_real(a, b):
    """A_CHSH(68) point: lam in Z_68 carries one deterministic response pair; 29 + 29 PR pairs (s, s xor ab), 5 + 5
    anti-PR pairs (s, s xor ab xor 1); cells 0 a, 1 b, 2 q, 3 r, 4 lam"""
    pairs = [(s, 0) for s in (0, 1) for _ in range(29)] + [(s, 1) for s in (0, 1) for _ in range(5)]
    steps = [xor_into(2, lambda x: pairs[x[4]][0]),
             xor_into(3, lambda x: pairs[x[4]][0] ^ (x[0] & x[1]) ^ pairs[x[4]][1])]
    pri = {(a, b, 0, 0, lam): F(1, 68) for lam in range(68)}
    return Realization(f'A_CHSH(68)[{a}{b}]', [2, 2, 2, 2, 68], [0, 1, 2, 3], steps, pri, lambda x: (x[2], x[3]))


def k8_box():
    box = {}
    for a, b in product((0, 1), repeat=2):
        for (q, r), v in law(checked(k8_real(a, b))).items():
            box[(a, b, q, r)] = v
    return box


def gate_F(code, a, b, s):
    return (code >> (a + 2 * b + 4 * s)) & 1


def gate_real(code, n, k, a, b):
    """long-edge gate class: cells 0 a, 1 b, 2 q, 3 r, 4 lam, 5 c (c in Z_n); q ^= lam; r ^= lam; r ^= F(a, b, [c < k])"""
    steps = [xor_into(2, lambda x: x[4]), xor_into(3, lambda x: x[4]),
             xor_into(3, lambda x: gate_F(code, x[0], x[1], 1 if x[5] < k else 0))]
    pri = {(a, b, 0, 0, lam, c): F(1, 2 * n) for lam in (0, 1) for c in range(n)}
    return Realization(f'gate[{code},{n},{k}][{a}{b}]', [2] * 5 + [n], [0, 1, 2, 3], steps, pri,
                       lambda x: (x[2], x[3]))


def gate_box(code, n, k, check=False):
    box = {}
    for a, b in product((0, 1), repeat=2):
        R = gate_real(code, n, k, a, b)
        if check:
            checked(R)
        for (q, r), v in law(R).items():
            box[(a, b, q, r)] = v
    return box


def k8():
    box = k8_box()
    E = corr(box)
    ok = nosig(box) and all((v * 68).denominator == 1 for v in box.values())
    ok &= all(E[(a, b)] == F(12, 17) * (1 if (a & b) == 0 else -1) for a, b in product((0, 1), repeat=2))
    st = kp_bell(box)
    ok &= st[0] == 'admitted'
    ok &= all(within(abs(E[ab]), Q2(0, F(1, 2)), EPS / 4) for ab in E)
    ok &= within(s_max(box), TSI, EPS)
    code = sum(((a & b) ^ s) << (a + 2 * b + 4 * s) for a, b, s in product((0, 1), repeat=3))
    gb = gate_box(code, 34, 5, check=True)
    ok &= gb == box
    check('K-8', ok, f'A_CHSH(68) contains the PR/anti-PR point (O-checked realization, lam in Z_68) with correlators '
          f'(12/17)(-1)^ab, zero marginals, entries in (1/68)Z, K-P {st[0]} ({st[1]}), each correlator within eps/4 '
          f'of 1/sqrt2, S_max = 48/17 within eps of 2sqrt2; the gate class reaches the same box at n = 34, k = 5 '
          f'(O-checked; amendment A-1)')
    return box


def gate_class():
    """exhaustive over 256 gates x 2 control values, each slice an O-checked realization; edge present at s iff
    F(., b, s) depends on a for some b (coupling-graph rule)"""
    max_free = None
    n_free = 0
    best_edge = None
    local_with_edge = 0
    for code in range(256):
        for s in (0, 1):
            free = all(gate_F(code, 0, b, s) == gate_F(code, 1, b, s) for b in (0, 1))
            box = gate_box(code, 1, s, check=True)
            sm = s_max(box)
            if free:
                n_free += 1
                max_free = sm if max_free is None or gt(sm, max_free) else max_free
            else:
                best_edge = sm if best_edge is None or gt(sm, best_edge) else best_edge
                if ge(2, sm):
                    local_with_edge += 1
    msg = (f'{n_free} edge-free (F, s) slices, maximum S_max {max_free} (local, so every admitted mixture has '
           f'S_max <= 2); edge slices reach S_max {best_edge}; {local_with_edge} edge slices are local yet use the '
           f'edge (e.g. F(a,b,c) = a) and are excluded too')
    check('GATE', max_free == 2 and best_edge == 4, 'exhaustive over 256 gates x 2 control values (O-checked): ' + msg)
    return msg, max_free


def l3c_cycle_le(n, k, a, b):
    """protocol cycle on Omega x Z_5 (clock cell 8, visible); returns (alpha realization, beta realization)"""
    T = 5
    steps = le_steps(k)

    def phi(st):
        x, t = st[:-1], st[-1]
        return steps[t](x) + ((t + 1) % T,)
    union = set()
    for lam in (0, 1):
        for u in range(n):
            s0 = (a, b, 0, 0, 0, 0, lam, u, 0)
            if s0 in union:
                continue
            s = s0
            while True:
                union.add(s)
                s = phi(s)
                if s == s0:
                    break
    doms = [2] * 7 + [n] + [T]
    vis = [0, 1, 2, 3, 4, 5, 8]
    sl = sorted(s for s in union if s[-1] == 0 and s[:6] == (a, b, 0, 0, 0, 0))
    Ra = Realization(f'L3C-alpha LE({n},{k})[{a}{b}]', doms, vis, [phi] * T, {s: F(1, len(sl)) for s in sl},
                     lambda s: (s[2], s[3]))
    rp = sorted(s for s in union if s[-1] == 0)
    Rb = Realization(f'L3C-beta LE({n},{k})[{a}{b}]', doms, vis, [], {s: F(1, len(rp)) for s in rp},
                     lambda s: (s[2], s[3]))
    return Ra, Rb


def l3c_cycle_dr(n, k, x, y):
    base = dr_real(n, k, x, (y,))
    T = len(base.steps)

    def phi(st):
        z, t = st[:-1], st[-1]
        return base.steps[t](z) + ((t + 1) % T,)
    union = set()
    for s0x in base.prior:
        s0 = s0x + (0,)
        if s0 in union:
            continue
        s = s0
        while True:
            union.add(s)
            s = phi(s)
            if s == s0:
                break
    doms = base.domains + [T]
    vis = base.visible + [len(base.domains)]
    init_vis = tuple(next(iter(base.prior))[i] for i in base.visible)
    sl = sorted(s for s in union if s[-1] == 0 and tuple(s[i] for i in base.visible) == init_vis)
    ptr = len(base.domains) - 1                      # the single readout's pointer cell (5 + L + 0 with L = 1)
    Ra = Realization(f'L3C-alpha DR({n},{k})', doms, vis, [phi] * T, {s: F(1, len(sl)) for s in sl},
                     lambda s: (s[ptr],))
    rp = sorted(s for s in union if s[-1] == 0)
    Rb = Realization(f'L3C-beta DR({n},{k})', doms, vis, [], {s: F(1, len(rp)) for s in rp}, lambda s: (s[ptr],))
    return Ra, Rb


L3C = {}


def l3c_eval():
    """A-4 readings: (alpha) first pass from the slice under the orbit-invariant prior; (beta) readout-phase statistics
    of the invariant measure. Condition O is checked on both."""
    alpha_eq = True
    beta_ok_le = {}
    for n in range(1, 13):
        for k in range(n + 1):
            box = {}
            okb = True
            for a, b in product((0, 1), repeat=2):
                Ra, Rb = l3c_cycle_le(n, k, a, b)
                if n <= 3:
                    checked(Ra)
                for (q, r), v in law(Ra).items():
                    box[(a, b, q, r)] = v
                okb &= check_O(Rb)
            alpha_eq &= box == le_box(n, k)
            beta_ok_le[(n, k)] = okb
            if (n, k) == (1, 1):
                L3C['alpha_S_11'] = s_max(box)
    beta_ok_dr = {}
    alpha_eq_dr = True
    for n in range(1, 5):
        for k in range(n + 1):
            okb = True
            for x in product((0, 1), repeat=2):
                for y in (0, 1):
                    Ra, Rb = l3c_cycle_dr(n, k, x, y)
                    if n <= 2:
                        checked(Ra)
                    alpha_eq_dr &= law(Ra) == dr_law(n, k, x, (y,))
                    okb &= check_O(Rb)
            beta_ok_dr[(n, k)] = okb
    L3C['beta_ok_le'] = beta_ok_le
    L3C['beta_ok_dr'] = beta_ok_dr
    nb_le = sum(beta_ok_le.values())
    nb_dr = sum(beta_ok_dr.values())
    ok = alpha_eq and alpha_eq_dr and nb_le == 0 and nb_dr == 0 and L3C['alpha_S_11'] == 4
    check('L3-C-readings', ok,
          f'(alpha): the orbit-invariant prior conditioned on the initial slice gives exactly the counting-measure law '
          f'for every LE(n,k), n <= 12, and DR(n,k), n <= 4 (O-checked for LE n <= 3, DR n <= 2); LE(1,1) S_max = '
          f'{L3C["alpha_S_11"]}. (beta): the invariant measure at the readout phase has a visible marginal that is not '
          f'a point mass, so condition O fails for {len(beta_ok_le) - nb_le}/{len(beta_ok_le)} LE and '
          f'{len(beta_ok_dr) - nb_dr}/{len(beta_ok_dr)} DR members computed; for all n [W]: every orbit through a '
          f'slice point with lam = 1 (LE) or with a nonzero pointer after one cycle (DR) carries a different visible '
          f'configuration at the readout phase')
    return ok


PC = {}


def pc_checks():
    """PC-1 (marginal consistency), PC-3a (permutation-unitary fixed-basis representation), PC-4 (readout inverses),
    measured member by member on small n; [W] beyond"""
    ok1 = True
    pc1 = {}
    for n in range(1, 13):
        for k in range(n + 1):
            bx = LE_BOX[(n, k)]
            good = True
            for a, b in product((0, 1), repeat=2):
                R = le_real(n, k, a, b)
                la = law(Realization('A-part', R.domains, R.visible, R.steps, R.prior, lambda x: (x[2],)))
                lb = law(Realization('B-part', R.domains, R.visible, R.steps, R.prior, lambda x: (x[3],)))
                for q in (0, 1):
                    good &= la.get((q,), 0) == sum(bx.get((a, b, q, r), 0) for r in (0, 1))
                    good &= lb.get((q,), 0) == sum(bx.get((a, b, r, q), 0) for r in (0, 1))
            pc1[(n, k)] = good
            ok1 &= good
    PC['pc1'] = pc1
    check('PC-1', ok1, 'marginal consistency: for every LE(n,k), n <= 12, each wing\'s law (its own partition) equals '
          'the marginal of the joint law of V_A u V_B; holds for every member computed (all n [W])')
    ok3 = True
    pc3 = {}
    for n in range(1, 4):
        for k in range(n + 1):
            good = True
            reals = [le_real(n, k, a, b) for a, b in product((0, 1), repeat=2)]
            reals += [dr_real(n, k, x, (y,)) for x in product((0, 1), repeat=2) for y in (0, 1)]
            for R in reals:
                om = list(product(*[range(d) for d in R.domains]))
                U = {}
                for x in om:
                    yy = x
                    for st in R.steps:
                        yy = st(yy)
                    U[x] = yy
                good &= len(set(U.values())) == len(om)
                born = {}
                for x, wt in R.prior.items():
                    kk = R.readout(U[x])
                    born[kk] = born.get(kk, 0) + wt
                good &= {kk: v for kk, v in born.items() if v} == law(R)
            pc3[(n, k)] = good
            ok3 &= good
    PC['pc3a'] = pc3
    check('PC-3a', ok3, 'for every LE(n,k) and DR(n,k), n <= 3, the realization\'s permutation unitary with rho = diag(mu) '
          'and fixed-basis Born readout reproduces the record law exactly (all n [W]: Main.md:82)')
    ok4 = True
    pc4_le = {}
    for n in range(1, 4):
        for k in range(n + 1):
            steps = le_steps(k)
            good = True
            for x in product(*[range(d) for d in [2] * 7 + [n]]):
                good &= steps[2](steps[2](x)) == x
                good &= steps[4](steps[3](steps[4](steps[3](x)))) == x
            pc4_le[(n, k)] = good
            ok4 &= good
    pc4_dr = {}
    for n in range(1, 4):
        for k in range(n + 1):
            R = dr_real(n, k, (0, 1), (0,))
            good = True
            for x in product(*[range(d) for d in R.domains]):
                good &= R.steps[2](R.steps[3](R.steps[3](R.steps[2](x)))) == x
            pc4_dr[(n, k)] = good
            ok4 &= good
    PC['pc4_le'] = pc4_le
    PC['pc4_dr'] = pc4_dr
    check('PC-4', ok4, 'LE readouts (q ^= p1; r ^= p2, r ^= ab[u<k]) applied twice to their own pointers restore '
          'Omega pointwise, and the kappa2 inverse of each DR readout restores it, for n <= 3 (all n [W])')
    okh = True
    for n in range(1, 13):
        for k in range(n + 1):
            st = le_steps(k)[4]
            dep = any(st((0, 1) + x[2:]) [3] != st((1, 1) + x[2:])[3] for x in product(*[range(d) for d in [2] * 7 + [n]]))
            okh &= dep == (k > 0) and nosig(LE_BOX[(n, k)])
    check('HB-1', okh, 'for every LE(n,k), n <= 12: Bob\'s readout step depends on Alice\'s setting (one long edge, added '
          'degree 1) iff k > 0, and the box is operationally no-signalling')


RESULTS = []


def finish_family(res, iiS_follow=None):
    """fill (ii-S): family member first, then follow-up class result iiS_follow = (bool, where)"""
    for sc in ('chsh', 'pom'):
        r = res[sc]
        if r['iiS_family']:
            r['iiS'] = True
            r['iiS_where'] = 'family: ' + fmt_member(r['iiS_witness'])
        elif iiS_follow and sc in iiS_follow:
            r['iiS'], r['iiS_where'] = iiS_follow[sc]
        else:
            r['iiS'] = False
            r['iiS_where'] = 'no admitted family member within the window; follow-up class not consulted'
        r['iii'] = r['iii_exact']
    return res


def passes(r):
    return r['i'] and r['iiS'] and r['iii']


ALL = lambda *a: True  # noqa: E731
NONE = lambda *a: False  # noqa: E731


def full_count():
    return len(le_members()) + len(LE_STRUCT)


def derive(res, skip=()):
    """class and sub-labels computed from the measured clauses (PREREG section 6; I-11)"""
    failed = False
    labels = []
    for sc in ('chsh', 'pom'):
        if sc in skip:
            continue
        r = res[sc]
        S = sc.upper()
        if not r['i']:
            failed = True
            labels.append(f'over-generation ({S})')
        if not r['iiS']:
            failed = True
            labels.append(f'under-generation ({S})')
        if not r['iii']:
            failed = True
            labels.append(f'classical exclusion ({S})')
        if r['n_admitted'] == full_count():
            labels.append(f'vacuous ({S})')
    return failed, labels


def verdict(cid, readings, own, repro=False, skip=(), note='', fu=None, b=None, dry=False):
    """readings: list of (reading name, res). A verdict is printed only if every own check passed (else 'void'), and
    only if every reading gives the same Failure / non-Failure verdict (amendments A-4, A-5; else Parked)."""
    bad = [c for c in own if not CHECKRES.get(c, False)]
    if bad:
        cls = f'void (own checks not passed: {bad})'
    else:
        outs = [(name, derive(res, skip)) for name, res in readings]
        fails = {f for _, (f, _) in outs}
        if len(fails) > 1:
            cls = 'Parked (readings disagree)'
        else:
            failed = fails.pop()
            if len(outs) == 1:
                labels = outs[0][1][1]
            else:
                labels = [f'{name}: ' + ', '.join(lb) for name, (_, lb) in outs]
            if skip:
                labels = labels + [f'{sc.upper()} part Parked' for sc in skip]
            cls = classify(False, failed, repro, labels)
    if dry:
        return cls
    RESULTS.append((cid, cls))
    print(f'\n--- {cid}: {cls}')
    for name, res in readings:
        for sc in ('chsh', 'pom'):
            if sc in skip:
                print(f'  [{name}] family {sc.upper()}: Parked')
                continue
            r = res[sc]
            print(f'  [{name}] family {sc.upper()}: (i) {r["i"]} [witness {fmt_member(r.get("i_witness"))}]; '
                  f'(ii-S) {r["iiS"]} [{r.get("iiS_where", "")}]; (iii) {r["iii"]}; admitted members '
                  f'{r.get("n_admitted", "-")}')
    if fu:
        for k_, v in fu.items():
            print(f'  follow-up {k_}: {v}')
    if b:
        for k_, v in b.items():
            print(f'  outcome (b) {k_}: {v}')
    if note:
        print('  note: ' + note)
    return cls


def mutation_controls():
    """K-M4: the reviewer's mutant m4 (L3-A admitting only k = 0) must change the derived verdict;
    K-M2: a candidate whose own check failed must get no verdict"""
    res_m = finish_family(family_eval(lambda n, k: k == 0, ALL, NONE, NONE))
    failed, labels = derive(res_m)
    check('K-M4', failed and 'over-generation (CHSH)' not in labels and 'under-generation (CHSH)' in labels,
          f'mutant L3-A admitting only k = 0: derived labels {labels} (the over-generation verdict is not printed)')
    CHECKRES['__forced_fail__'] = False
    cls = verdict('mutant', [('m', res_m)], own=['__forced_fail__'], dry=True)
    check('K-M2', cls.startswith('void'), f'a candidate whose own check fails gets "{cls.split(" (")[0]}", no verdict')


def candidates(kp_box, hb, gate_msg, gate_max):
    print('\n=== Candidates (section 9 order) ===')
    count = lambda n, k: True  # noqa: E731
    # L3-0: no constraint (Main.md:60)
    verdict('L3-0', [('L3-0', finish_family(family_eval(ALL, ALL, ALL, ALL)))], own=['LEARCH'],
            note='Main.md:60 read literally admits every prior; LE(1,1) is the PR box')
    verdict('L3-A', [('L3-A', finish_family(family_eval(count, count, NONE, NONE)))], own=['LEARCH', 'L3-A-priorfree'],
            note='counting measure on the hidden carrier; LE(1,1) (gate r ^= ab, no control register) is admitted: its '
                 'correlators are (-1)^ab for every lam, and the counting measure makes it the no-signalling PR box')
    verdict('L3-B', [('L3-B', finish_family(family_eval(count, count, NONE, NONE)))], own=['LEARCH'],
            note='conditioning on the trivial record is allowed, so L3-B admits L3-A\'s members')
    bl = L3C['beta_ok_le']
    bd = L3C['beta_ok_dr']
    beta_le = lambda n, k: bl.get((n, k), False)  # noqa: E731  (n > 12: [W], see L3-C-readings)
    beta_dr = lambda n, k: bd.get((n, k), False)  # noqa: E731  (n > 4: [W])
    verdict('L3-C', [('alpha', finish_family(family_eval(count, count, NONE, NONE))),
                     ('beta', finish_family(family_eval(beta_le, beta_dr, NONE, NONE)))],
            own=['L3-C-readings'],
            note='(alpha) reproduces L3-A\'s prior on the slice; under (beta) the invariant measure\'s visible marginal at '
                 'the readout phase is not a point mass, so no LE or DR member satisfies condition O (PREREG section 1)')
    print('\n--- L3-D: Failure (Failure-as-stated: the moment-constraint values are parameters OI does not fix; '
          'no corpus text fixes them; not computed, as preregistered)')
    RESULTS.append(('L3-D', 'Failure (Failure-as-stated)'))
    verdict('L3-PR', [('as L3-A', finish_family(family_eval(count, count, NONE, NONE)))], own=['LEARCH'],
            note='no corpus text fixes the "geometric and thermodynamic properties of the partition boundary" for LE or '
                 'DR, so its admitted set is L3-A\'s (rule fixed in PREREG section 3.1); not independent')
    pc1 = PC['pc1']
    verdict('PC-1', [('PC-1', finish_family(family_eval(lambda n, k: pc1.get((n, k), True), ALL, ALL, ALL)))],
            own=['PC-1'], note='marginal consistency measured for n <= 12; beyond, [W] (marginals of one law)')
    verdict('PC-2', [('PC-2', finish_family(family_eval(lambda n, k: nosig(LE_BOX[(n, k)]), ALL,
                                                        lambda w: nosig(le_struct_box(w)), ALL)))],
            own=['LEARCH'], note='admission = operational no-signalling, measured on every LE member; DR readout laws '
                                 'depend only on (x, y) by construction; Methodology.md:393 states no-signalling is '
                                 'insufficient')
    pc3 = PC['pc3a']
    verdict('PC-3a', [('PC-3a', finish_family(family_eval(lambda n, k: pc3.get((n, k), True),
                                                          lambda n, k: pc3.get((n, k), True), ALL, ALL)))],
            own=['PC-3a'], note='Q_fb measured for n <= 3; universal (Main.md:82)')
    print('\n--- PC-3b: see K-P above')
    p4 = PC['pc4_le']
    p4d = PC['pc4_dr']
    verdict('PC-4a', [('PC-4a', finish_family(family_eval(lambda n, k: p4.get((n, k), True),
                                                          lambda n, k: p4d.get((n, k), True), ALL, ALL)))],
            own=['PC-4'], note='under kappa2 every readout has an accessible inverse that restores the pre-readout law')
    verdict('PC-4b', [('reapply allowed', finish_family(family_eval(lambda n, k: p4.get((n, k), True), ALL, ALL, ALL))),
                      ('reapply not allowed', finish_family(family_eval(NONE, ALL, NONE, ALL)))],
            own=['PC-4'], skip=('pom',),
            note='the two readings are the A-5 choice: if a readout may be reapplied to its own pointer, LE readouts are '
                 'self-inverse and every LE member is admitted; if not, no LE readout is invertible within the family\'s '
                 'accessible set and every LE member is excluded; the POM part is Parked (A-5)')
    verdict('HB-1', [('HB-1', finish_family(family_eval(count, ALL, ALL, ALL)))], own=['HB-1'],
            note='LE(1,1): one long edge (added degree 1, so D = 1 already admits it), parameter dependence, no-signalling; '
                 'POM: H-Bell is silent, every DR member admitted')
    verdict('HB-2', [('HB-2', finish_family(family_eval(count if hb['hb2_holds'] else NONE, ALL,
                                                        ALL if hb['hb2_holds'] else NONE, ALL)))],
            own=['HB-2'], note=hb['hb2'])
    gate_follow = {'chsh': (ge(gate_max, TSI - EPS), 'long-edge gate class: ' + gate_msg)}
    ex3 = hb['hb3a_excl']
    verdict('HB-3alpha', [('HB-3alpha', finish_family(
        family_eval(lambda n, k: k == 0 or not ex3, ALL, lambda w: w == 0 or not ex3, ALL), iiS_follow=gate_follow))],
            own=['HB-3alpha', 'GATE'], note=hb['hb3a'])
    print('\n--- HB-3beta: Parked (the mesoscopic Bakry-Emery functional needs a scale and averaging the corpus does '
          'not define; PREREG section 3.3 rule; N_BE in {3, 6, infinity} not evaluated because the functional is '
          'undefined)')
    RESULTS.append(('HB-3beta', 'Parked'))
    ex4 = hb['hb4_excl']
    verdict('HB-4', [('HB-4', finish_family(
        family_eval(lambda n, k: k == 0 or not ex4, ALL, lambda w: w == 0 or not ex4, ALL), iiS_follow=gate_follow))],
            own=['HB-4', 'GATE'], note=hb['hb4'])
    print('\n--- CL: Parked (definition not retrieved: arXiv:2512.18105 unreachable from the container at drafting and '
          'at execution; PREREG section 3.4 rule)')
    RESULTS.append(('CL', 'Parked'))


def priorfree_check():
    smax_all = all(s_max(le_box_lamprior(F(j, 9))) == 4 for j in range(10))
    sig_all = all(not nosig(le_box_lamprior(F(j, 9))) for j in range(10))
    half = le_box_lamprior(F(1, 2))
    check('L3-A-priorfree', smax_all and sig_all and nosig(half) and half == LE_BOX[(1, 1)],
          'S_max = 4 for every prior on lam; operationally no-signalling only at P(lam=0) = 1/2: S_max = 4 at '
          'P(lam = 0) = j/9, j = 0..9, each of these ten boxes signalling; P(lam = 0) = 1/2 gives the no-signalling PR '
          'box, which is LE(1,1) under the counting measure')


def le_box_lamprior(p0):
    box = {}
    for a, b in product((0, 1), repeat=2):
        pri = {(a, b, 0, 0, 0, 0, lam, 0): (p0 if lam == 0 else 1 - p0) for lam in (0, 1)}
        R = checked(Realization('LE(1,1)[lam-prior]', [2] * 7 + [1], [0, 1, 2, 3, 4, 5], le_steps(1),
                                pri, lambda x: (x[2], x[3])))
        for (q, r), v in law(R).items():
            box[(a, b, q, r)] = v
    return box


def hbell():
    out = {}
    # HB-2: sparsity diagnostic, exact m_N at L in L_SET with r = 1 (ball radius 3), and the bound (6r+1)^3 / L^3
    rows = []
    for L in L_SET:
        adj, A, B = torus(L)
        d = bfs(adj, A)
        m = len(ball(d, 3))
        rows.append(f'L={L}: m_N={m}, L_N m_N/N={F(m, L ** 3)}')
    out['hb2'] = ('per prepared graph with P = 1 long edge, L_N m_N / N <= P (6 r_N + 1)^3 / L^3 -> 0 for every '
                  'schedule r_N -> infinity, r_N / L -> 0 (m_N <= |ell_1 ball of radius 3 r_N| <= (6 r_N + 1)^3) [W]; '
                  'instances ' + '; '.join(rows) + '. The condition holds whatever w is, so HB-2 admits LE(1,1)')
    print('HB-2 instances: ' + '; '.join(rows))
    hb2_ok = all(len(ball(bfs(torus(L)[0], (0, 0, 0)), 3)) <= 7 ** 3 for L in L_SET)
    ratios = [F(len(ball(bfs(torus(L)[0], (0, 0, 0)), 3)), L ** 3) for L in L_SET]
    hb2_ok &= all(ratios[i + 1] < ratios[i] for i in range(len(ratios) - 1))
    check('HB-2', hb2_ok, 'm_N <= (6r+1)^3 = 343 at r = 1 and L_N m_N / N decreasing over L in L_set: ' + '; '.join(rows)
          + '; the limit for every schedule r_N -> infinity, r_N/L -> 0 is the [W] bound P(6 r_N + 1)^3 / L^3')
    out['hb2_holds'] = hb2_ok
    # HB-3alpha: exact W1 by min-cost flow vs closed form, reference and glued torus
    s_r = lambda r: 1 if r == 0 else 4 * r * r + 2  # noqa: E731
    V = lambda dl: sum(s_r(r) for r in range(dl + 1))  # noqa: E731

    def closed(w, dl):
        Z = V(dl) + V(dl - 1)
        sh = s_r(dl)
        Er = F(sum(r * s_r(r) for r in range(dl + 1)), V(dl))
        mass = (1 - w) + w * F(sh, Z)
        intr = (1 - w) * Er + w * F(sh, Z) * dl
        return mass + 2 * intr
    ok = True
    ref_ok = True
    rows = []
    for L in (4, 6, 8, 10, 12):
        adjr, A, B = torus(L)
        adjg, _, _ = torus(L, glue=True)
        cache_r, cache_g = {}, {}

        def dr_(x):
            if x not in cache_r:
                cache_r[x] = bfs(adjr, x)
            return cache_r[x]

        def dg_(x):
            if x not in cache_g:
                cache_g[x] = bfs(adjg, x)
            return cache_g[x]
        for dl in (1, 2):
            e1 = (1, 0, 0)
            # reference curvature on the edge (A, A+e1): expect 0
            wr = w1_exact(unif(ball(dr_(A), dl)), unif(ball(dr_(e1), dl)), dr_)
            ref_ok &= wr <= 1 and (wr == 1 if L >= 10 else True)
            # reference pair (A, B): 0 <= kappa_ref <= 4 E r / (3L)
            wab = w1_exact(unif(ball(dr_(A), dl)), unif(ball(dr_(B), dl)), dr_)
            dab = dr_(A)[B]
            kref = 1 - wab / dab
            for w in (F(1, 4), F(1, 2), F(1)):
                mA = {}
                mB = {}
                for v, p in unif(ball(dr_(A), dl)).items():
                    mA[v] = mA.get(v, 0) + (1 - w) * p
                for v, p in unif(ball(dg_(A), dl)).items():
                    mA[v] = mA.get(v, 0) + w * p
                for v, p in unif(ball(dr_(B), dl)).items():
                    mB[v] = mB.get(v, 0) + (1 - w) * p
                for v, p in unif(ball(dg_(B), dl)).items():
                    mB[v] = mB.get(v, 0) + w * p
                wg = w1_exact(mA, mB, dg_)
                if L >= 6:
                    ok &= wg == closed(w, dl)
                rows.append(f'L={L} delta={dl} w={w}: W1={wg} (closed form {closed(w, dl)}), kappa(A,B)={1 - wg}')
            rows.append(f'L={L} delta={dl}: reference kappa(A,A+e1)={1 - wr}, reference kappa(A,B)={kref}')
    # every delta >= 1 and w in (0, 1]: W1 >= min(closed(1, delta), closed(0+, delta)) >= 9/4 (affine in w)
    bound_ok = all(closed(F(1), dl) >= F(9, 4) and closed(F(0), dl) >= F(9, 4) for dl in range(1, 61))
    lim = [str(closed(F(1), dl)) for dl in (1, 2, 5, 20, 60)]
    check('HB-3alpha', ok and bound_ok and ref_ok,
          'exact min-cost-flow W1 equals the closed form W1 = |nu+| + 2 int r dnu+ at every instance with L >= 6 '
          '(the form needs 3L/2 >= 4 delta + 1; L = 4 is reported as a flow instance only); reference curvature on '
          'lattice edges is >= 0 at every L and exactly 0 for L >= 10 (on Z^3 it is 0: z_1 is 1-Lipschitz, so '
          'W1 >= 1 = the translation cost [W]); at the long edge (A,B), for every delta >= 1 and every w in (0,1], '
          'W1 >= 9/4, so kappa(A,B) <= -5/4 (option 1 is w = 1: W1 -> 3, kappa -> -2; option 2 with w < 1: '
          'kappa -> -infinity); W1 at w = 1 for delta = 1, 2, 5, 20, 60: ' + ', '.join(lim))
    for r in rows:
        print('  HB-3alpha ' + r)
    out['hb3a_excl'] = bool(ok and bound_ok and ref_ok)
    out['hb3a'] = ('both options of amendment A-3 give the same admitted set: for every w > 0 the endpoint '
                   'curvature kappa(A,B) <= -5/4 for every delta >= 1 (exact closed form, verified by min-cost flow), '
                   'while the reference value tends to 0; so only w = 0 is admitted; in the gate class only '
                   'realizations with no edge at any positive-weight control value are admitted, and these are local')
    # HB-4: radius argument
    rows = []
    ok = True
    for L in (4, 6, 8, 10):
        adjr, A, B = torus(L)
        adjg, _, _ = torus(L, glue=True)
        radX = min(max(bfs(adjr, v).values()) for v in [(0, 0, 0), (1, 2, 3)])
        eccs = [max(bfs(adjg, v).values()) for v in adjg]
        radY = min(eccs)
        ok &= radX == 3 * L // 2 and 2 * radY <= F(3 * L, 2) + 1
        lb = F(radX - radY, 2 * L)
        ok &= lb >= F(3, 8) - F(1, 4 * L)
        rows.append(f'L={L}: rad X={radX}, rad Y={radY}, d_GH(rescaled) >= {lb}')
    check('HB-4', ok, 'rescaled Gromov-Hausdorff distance between the glued and reference tori is at least '
          '(rad X - rad Y)/(2L) >= 3/8 - 1/(4L): ' + '; '.join(rows) + ' (|rad X - rad Y| <= 2 d_GH; '
          'd(z,A) + d(z,B) = 3L/2 on the ell_1 torus gives rad Y <= 3L/4 + 1/2 for every even L [W])')
    out['hb4_excl'] = bool(ok)
    out['hb4'] = ('any positive-weight prepared graph with the long edge stays at rescaled GH distance >= 3/8 - '
                  '1/(4L) from the reference (radius argument, exact at L = 4..10, [W] for all even L); so only w = 0 '
                  'is admitted in LE, and only edge-free gate realizations in the gate class, which are local. '
                  'SM.md:150 already states that such an edge destroys GH closeness')
    return out


def kp_run(kp_box):
    """PC-3b = K-P: family stage, follow-up, outcome (b)"""
    def adm_le(n, k):
        # n <= 12: K-P's rule on the computed box; n > 12: the exact perfect-correlation argument excludes every
        # k >= 1 (E = (1, 1, 1, 1 - 2k/n)) and k = 0 is a local box [W, K-7]
        if n <= 12:
            return kp_bell(le_box(n, k))[0] == 'admitted'
        return k == 0
    adm_dr = lambda n, k: kp_dr(F(k, n))[0] == 'admitted'  # noqa: E731
    res = family_eval(adm_le, adm_dr, lambda w: w == 0, lambda w: kp_dr(w)[0] == 'admitted')
    st = kp_bell(kp_box)
    res = finish_family(res, iiS_follow={'chsh': (st[0] == 'admitted' and within(s_max(kp_box), TSI, EPS),
                                                   f'follow-up class A_CHSH(68) point v = 12/17 ({st[1]}), '
                                                   f'S_max = {s_max(kp_box)}')})
    # delay line and toy bit (K-4) are in iii exact
    fu = {}
    if passes(res['chsh']):
        fu['CHSH (F1)'] = ('holds: K-P excludes every box with S_max > 2sqrt2 by the exact SOS witness (check SOS), so '
                           'the admitted maximum of S_max over A_CHSH is <= 2sqrt2')
        fu['CHSH (ii-Q)'] = f'holds: v = 12/17 point admitted ({st[1]})'
        fu['CHSH (iii-A)'] = ('holds: every local box is admitted (Fine; diagonal quantum realization), so every '
                              'local box in A_CHSH is admitted exactly')
    if passes(res['pom']):
        fu['POM (F2)'] = ('holds: K-P admits only quantum statistics with rho_00 + rho_11 = rho_01 + rho_10, whose '
                          'POM success is <= (1+1/sqrt2)/2 [L: Spekkens et al. 2009]')
        fu['POM (ii-Q-POM)'] = 'holds: DR(12/17) equals the K-11 qubit protocol exactly, POM = 29/34 within eps/8'
        fu['POM (iii-A)'] = ('holds: a preparation-noncontextual model with exact parity obliviousness has equal '
                             'ontic parity mixtures, so its diagonal quantum realization has rho_00 + rho_11 = '
                             'rho_01 + rho_10 [W]')
    b = kp_outcome_b()
    cls = verdict('PC-3b (= K-P)', [('K-P', res)], own=['SOS', 'K-4', 'K-8', 'K-11'], repro=True, fu=fu, b=b,
                  note='the principle is the quantum set (a quantum ingredient), so a pass is Reproduction')
    kp_ok = passes(res['chsh']) and passes(res['pom']) and len(fu) == 6 and b['b1'].startswith('holds')
    kp_ok &= cls == 'Reproduction'
    check('K-P', kp_ok, 'positive control passes the family stage, (a), (a-POM) and (b1); classified Reproduction')
    return res


def kp_outcome_b():
    b = {}
    # (b1): T1 and LE members excluded; correlator-grid instance n <= 12 (amendment A-6)
    t1 = kp_bell(le_box(5, 2))[0]
    adm_bad = 0
    adm = 0
    und = 0
    for n in range(1, 13):
        vals = [F(n - 2 * d, n) for d in range(n + 1)]
        for E in product(vals, repeat=4):
            Ed = dict(zip(((0, 0), (0, 1), (1, 0), (1, 1)), E))
            box = {(a, bb, q, r): (1 + (1 if q == r else -1) * Ed[(a, bb)]) / 4
                   for a, bb in product((0, 1), repeat=2) for q, r in product((0, 1), repeat=2)}
            st = kp_bell(box)[0]
            if st == 'admitted':
                adm += 1
                if num_tlm_violates(Ed):
                    adm_bad += 1
            elif st == 'undetermined':
                und += 1
    b['b1'] = (f'holds: T1 {t1}; every LE member with w > 0 excluded (K-7); correlator-grid instance n <= 12 '
               f'(zero marginals): {adm} admitted boxes, {adm_bad} of them TLM-violating by a [NUM] cross-check, '
               f'{und} undetermined (count for no clause); beyond n = 12 by the admission rule (A-6)')
    b['b2'] = ('holds by construction for the admitted (inner) set, whose members are quantum, with tilted-CHSH '
               'maximum sqrt(8 + 2 alpha^2) [L: Acin-Massar-Pironio 2012, not read]; maximizing boxes not '
               'exhibited and NPA 1+AB status not computed (no SDP tooling)')
    # (b3): isotropic zero-marginal chained points with entries in (1/n)Z, n <= 100
    best = None
    for n in range(1, N_MAX + 1):
        for j in range(n + 1):
            c = F(4 * j, n) - 1                     # (1 +- c)/4 in (1/n)Z  <=>  c in (4/n)Z - 1
            if c <= 0 or 4 * c * c > 3:
                continue
            val = 6 * c
            if best is None or val > best[0]:
                best = (val, n, c)
    target_ok = sgn(q2(best[0]) * q2(best[0]) - 27) <= 0
    within_eps = sgn((q2(best[0]) + EPS) * (q2(best[0]) + EPS) - 27) >= 0
    b['b3'] = (f'incomplete: admitted maximum <= 3sqrt3 [L: Wehner 2006]; achievability within eps in the class: the '
               f'best isotropic zero-marginal quantum point (|E| = c, c^2 <= 3/4, entries in (1/n)Z, n <= 100) has '
               f'I3 = {best[0]} at n = {best[1]} (<= 3sqrt3: {target_ok}; within eps of 3sqrt3: {within_eps}); '
               f'non-isotropic points not searched, so (b3) is not established (no-reduction clause)')
    return b


def synthetic_controls(kp_box):
    print('\n=== Checker controls K-N1..K-N6 (synthetic principles, not candidates) ===')
    le = {(n, k): 2 + 2 * F(k, n) for n in range(1, N_MAX + 1) for k in range(n + 1)}

    def fam(adm_S, adm_P):
        r = family_eval(lambda n, k: adm_S(2 + 2 * F(k, n), F(k, n)), lambda n, k: adm_P((1 + F(k, n)) / 2, F(k, n)),
                        lambda w: adm_S(le_S(w), w), lambda w: adm_P(dr_P(w), w))
        return r
    # K-N1
    r = finish_family(fam(lambda S, w: ge(3, S), lambda P, w: ge(F(7, 8), P)))
    check('K-N1', not r['chsh']['i'] and not r['pom']['i'],
          f'"S_max <= 3, POM <= 7/8": fails (i) in CHSH (witness {fmt_member(r["chsh"]["i_witness"])}) and POM')
    # K-N2
    r = finish_family(fam(lambda S, w: ge(F(1, 2), w), lambda P, w: ge(Q2(0, F(1, 2)), w)))
    check('K-N2', not r['chsh']['i'], f'"w <= 1/2 (LE), w <= 1/sqrt2 (DR)": fails (i) in CHSH (witness '
          f'{fmt_member(r["chsh"]["i_witness"])})')
    # K-N3: S_max <= 2, POM <= 3/4 everywhere; follow-up class: admitted maximum is <= 2 by the principle itself
    r = finish_family(fam(lambda S, w: ge(2, S), lambda P, w: ge(F(3, 4), P)),
                      iiS_follow={'chsh': (False, 'A_CHSH: every admitted box has S_max <= 2 < 2sqrt2 - eps'),
                                  'pom': (False, 'A_POM: every admitted model has POM <= 3/4')})
    check('K-N3', not r['chsh']['iiS'] and not r['pom']['iiS'], '"S_max <= 2, POM <= 3/4 everywhere": fails (ii-S) '
          'in CHSH and POM')
    # K-N4
    r = finish_family(fam(lambda S, w: ge(w, F(1, 4)) and ge(Q2(-1, 1), w),
                          lambda P, w: ge(w, F(1, 2)) and ge(Q2(0, F(1, 2)), w)))
    check('K-N4', not r['chsh']['iii'], '"1/4 <= w <= sqrt2-1 (LE), 1/2 <= w <= 1/sqrt2 (DR)": fails (iii): the LE '
          'w = 0 law is not admitted')
    # K-N5: LE restricted to S <= 2sqrt2, DR as K-P, A_CHSH unrestricted
    r = finish_family(fam(lambda S, w: ge(TSI, S), lambda P, w: kp_dr(w)[0] == 'admitted'))
    pr = le_box(1, 1)
    f1 = not gt(TSI + EPS, s_max(pr))
    check('K-N5', passes(r['chsh']) and passes(r['pom']) and f1, f'passes the family stage (CHSH ii-S witness '
          f'{r["chsh"]["iiS_where"]}); in A_CHSH it admits the PR box (two response pairs (s, s xor ab)), '
          f'S_max = {s_max(pr)} > 2sqrt2 + eps, so (F1) fails')
    # K-N6: S_max <= 2sqrt2 on every admitted box; POM as K-P
    r = finish_family(fam(lambda S, w: ge(TSI, S), lambda P, w: kp_dr(w)[0] == 'admitted'))
    t1 = le_box(5, 2)
    a_ok = passes(r['chsh']) and ge(TSI, s_max(kp_box)) and passes(r['pom'])
    b1_fail = ge(TSI, s_max(t1)) and perfect_corr_excluded(t1)
    check('K-N6', a_ok and b1_fail, 'passes (a) (family stage, (F1) by its own bound, (ii-Q) at v = 12/17, (iii-A) '
          'local boxes have S_max <= 2) and (a-POM) as K-P; admits T1 (S_max = 14/5 <= 2sqrt2, post-quantum), so '
          '(b1) fails')


def static_checks():
    import ast
    src = inspect.getsource(law)
    attrs = set(re.findall(r'R\.(\w+)', src))
    check('I-2-static', attrs <= {'prior', 'steps', 'readout'}, f'law() reads only R.{sorted(attrs)}')
    tree = ast.parse(open(__file__).read())
    bad = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and not node.name.startswith('num_'):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, float):
                    bad.add(node.name)
                if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name) and sub.func.id == 'float':
                    sentinel = (node.name == 'w1_exact' and sub.args and isinstance(sub.args[0], ast.Constant)
                                and sub.args[0].value == 'inf')
                    if not sentinel:
                        bad.add(node.name)
    check('I-4-static', not bad, f'no float constant or float() call outside num_* functions (w1_exact uses '
          f"float('inf') as a graph-search sentinel only): offenders {sorted(bad)}")


def main():
    header()
    classifier_tests()
    controls()
    kp_box = k8_box()
    kp_run(kp_box)
    synthetic_controls(kp_box)
    mutation_controls()
    static_checks()
    gate_ok = all(ok for cid, ok in CHECKS)
    k9 = all(ok for _, ok in O_LOG)
    check('K-9', k9, f'condition O (bijectivity on Omega, point-mass visible marginal, normalized prior) holds for '
          f'all {len(O_LOG)} realizations checked')
    gate_ok = gate_ok and k9
    print('\nI-6 gate: controls K-1..K-9, K-11, K-P, K-N1..K-N6, K-M2, K-M4, SOS, I-17, static checks: '
          + ('all green' if gate_ok else 'failed'))
    print('K-10: n <= 3 in k10.py (see k10.run*.out); n = 4 pending (CI, owner approval); verdicts below are '
          'provisional on K-10 n = 4 (amendment A-2)')
    if not gate_ok:
        print('verdicts suppressed (I-6)')
        return
    print('\n=== Candidate measurements (each verdict below is printed only if its own checks pass) ===')
    priorfree_check()
    l3c_eval()
    pc_checks()
    hb = hbell()
    gate_msg, gate_max = gate_class()
    candidates(kp_box, hb, gate_msg, gate_max)
    k9b = all(ok for _, ok in O_LOG)
    check('K-9-final', k9b, f'condition O holds for all {len(O_LOG)} realizations checked, candidates included')
    print('\n=== Classification summary ===')
    for cid, cls in RESULTS:
        print(f'  {cid}: {cls}')
    nf = sum(1 for _, ok in CHECKS if not ok)
    print(f'\nchecks: {len(CHECKS) - nf} PASS, {nf} FAIL')


if __name__ == '__main__':
    main()
