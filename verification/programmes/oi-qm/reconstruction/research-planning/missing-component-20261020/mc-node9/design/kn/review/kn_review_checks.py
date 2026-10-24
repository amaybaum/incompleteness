"""Independent exact checks for the K_n form of M0 (review of 1dcbde1d). Fractions/integers only.
Point x of Z2^{2n}: bit 2i = q_i, bit 2i+1 = p_i (same convention as design/kn). Constraint masks a act by a.x."""
from fractions import Fraction as F
from itertools import product, combinations
import sys

def par(x): return bin(x).count('1') & 1
def om(a, b, n):  # symplectic bracket of two constraint masks
    s = 0
    for i in range(n):
        s += ((a >> 2*i) & 1) * ((b >> (2*i+1)) & 1) + ((a >> (2*i+1)) & 1) * ((b >> 2*i) & 1)
    return s & 1

def iso_subspaces(n):
    N = 2*n; seen = {frozenset([0])}; level = [frozenset([0])]
    while level:
        nxt = []
        for S in level:
            for a in range(1, 1 << N):
                if a in S or any(om(a, b, n) for b in S): continue
                T = frozenset(S | {s ^ a for s in S})
                if T not in seen: seen.add(T); nxt.append(T)
        level = nxt
    return seen

def qbin(n, k, q=2):
    num = den = 1
    for i in range(k): num *= q**(n-i) - 1; den *= q**(i+1) - 1
    return num // den
def iso_count_formula(n, k):
    r = qbin(n, k)
    for i in range(n-k+1, n+1): r *= 2**i + 1
    return r

def states_from(subs, n):
    N = 2*n; out = set()
    for A in subs:
        for x0 in range(1 << N):
            out.add(frozenset(x for x in range(1 << N) if all(par(a & (x ^ x0)) == 0 for a in A)))
    return out

ok = True
def check(cond, msg):
    global ok
    print(('ok   ' if cond else 'FAIL ') + msg)
    ok = ok and cond

# 1. census
STATES = {}
for n in (1, 2, 3):
    subs = iso_subspaces(n)
    byk = {}
    for A in subs:
        k = len(A).bit_length() - 1; byk[k] = byk.get(k, 0) + 1
    check(all(byk[k] == iso_count_formula(n, k) for k in byk) and len(byk) == n+1,
          f'n={n}: isotropic subspaces by dim {dict(sorted(byk.items()))} match q-binomial formula; total {len(subs)}')
    sts = states_from(subs, n); STATES[n] = sts
    pred = sum(iso_count_formula(n, k) * 2**k for k in range(n+1))
    lag = sum(1 for s in sts if len(s) == 2**n)
    check(len(sts) == pred, f'n={n}: uniform isotropic affine states {len(sts)} (formula {pred}); Lagrangian cosets {lag}')
n = 4
print('n=4 by formula: subspaces', sum(iso_count_formula(4, k) for k in range(5)),
      ' states', sum(iso_count_formula(4, k) * 2**k for k in range(5)), ' Lagrangian cosets', iso_count_formula(4, 4) * 16)

# every non-Lagrangian isotropic state is an equal mixture of Lagrangian ones (so 6/60/1080 vertices suffice)
for n in (1, 2, 3):
    lags = [s for s in STATES[n] if len(s) == 2**n]
    good = True
    for s in STATES[n]:
        if len(s) == 2**n: continue
        parts = [L for L in lags if L <= s]
        # direct: s is a coset of D; some Lagrangian L inside s has direction D' <= D; cosets of D' partition s
        L = parts[0]; d = {min(L) ^ y for y in L}
        cos = {frozenset(x ^ t for t in d) for x in s}
        found = all(c in STATES[n] for c in cos) and sum(len(c) for c in cos) == len(s)
        good = good and found
    check(good, f'n={n}: every isotropic uniform state is an equal mixture of Lagrangian coset states')

# 2. K1 = {p : p_x <= 1/2}: enumerate vertices of that polytope exactly (basic solutions) and compare
verts = set()
cons = [('lo', x) for x in range(4)] + [('hi', x) for x in range(4)]
for tight in combinations(cons, 3):
    # solve p with sum=1 and the 3 tight constraints
    fixed = {}; bad = False
    for t, x in tight:
        v = F(0) if t == 'lo' else F(1, 2)
        if x in fixed and fixed[x] != v: bad = True
        fixed[x] = v
    free = [x for x in range(4) if x not in fixed]
    if bad or len(free) != 1: continue
    p = dict(fixed); p[free[0]] = 1 - sum(fixed.values())
    if all(F(0) <= p[x] <= F(1, 2) for x in range(4)):
        verts.add(tuple(p[x] for x in range(4)))
two_pt = {tuple(F(1, 2) if x in s else F(0) for x in range(4)) for s in STATES[1] if len(s) == 2}
check(verts == two_pt, f'K1 polytope {{p>=0, sum 1, p_x<=1/2}} has exactly the {len(verts)} two-point uniform vertices = the 6 line states')

# 3. exact LP with certificates (phase-I simplex, Bland's rule)
def lp_member(x, gens):
    m = len(x); k = len(gens)
    T = [[F(g[i]) for g in gens] + [F(1) if j == i else F(0) for j in range(m)] + [F(x[i])] for i in range(m)]
    basis = [k + i for i in range(m)]
    cost = [F(0)] * k + [F(1)] * m
    while True:
        cb = [cost[b] for b in basis]
        red = [cost[j] - sum(cb[i] * T[i][j] for i in range(m)) for j in range(k + m)]
        enter = next((j for j in range(k + m) if red[j] < 0), None)
        if enter is None: break
        rows = [(T[i][-1] / T[i][enter], basis[i], i) for i in range(m) if T[i][enter] > 0]
        _, _, r = min(rows)
        pv = T[r][enter]; T[r] = [v / pv for v in T[r]]
        for i in range(m):
            if i != r and T[i][enter] != 0:
                f = T[i][enter]; T[i] = [a - f * b for a, b in zip(T[i], T[r])]
        basis[r] = enter
    cb = [cost[b] for b in basis]
    obj = sum(cb[i] * T[i][-1] for i in range(m))
    if obj == 0:
        lam = [F(0)] * k
        for i, b in enumerate(basis):
            if b < k: lam[b] = T[i][-1]
        return True, lam
    y = [sum(cb[i] * T[i][k + j] for i in range(m)) for j in range(m)]
    return False, y

def verify(x, gens, res):
    member, cert = res
    if member:
        return all(l >= 0 for l in cert) and sum(cert) == 1 and all(
            sum(l * g[i] for l, g in zip(cert, gens)) == x[i] for i in range(len(x)))
    return all(sum(a * b for a, b in zip(cert, g)) <= 0 for g in gens) and sum(a * b for a, b in zip(cert, x)) > 0

def gens_of(n): return [[F(1, len(s)) if p in s else F(0) for p in range(1 << 2*n)] for s in sorted(STATES[n], key=sorted)]
G = {1: gens_of(1), 2: gens_of(2)}
def vec(d, n): return [F(d.get(p, 0)) for p in range(1 << 2*n)]
def pt(*bits):  # bits in order q1,p1,q2,p2
    return sum(b << i for i, b in enumerate(bits))

def uniform(S): return {x: F(1, len(S)) for x in S}
def mix(*parts):
    out = {}
    for w, d in parts:
        for x, p in d.items(): out[x] = out.get(x, 0) + w * p
    return out
def coset(n, eqs):  # eqs: list of (mask, value)
    return [x for x in range(1 << 2*n) if all(par(a & x) == c for a, c in eqs)]
q = lambda i: 1 << 2*(i-1); p_ = lambda i: 1 << (2*(i-1)+1)

cases = {}
for pr in (F(1, 4), F(99, 100), F(1, 2)):
    cases[f'K-BIAS-MASK p={pr}'] = (1, {pt(0, 0): pr, pt(0, 1): 1 - pr}, pr == F(1, 2))
cases['K-COMP2'] = (2, uniform(coset(2, [(q(1) | q(2), 0), (p_(1), 0)])), False)
cases['new K-MIX2 (1/2 U[q1=q2=0] + 1/2 U[p1=p2=0])'] = (2, mix((F(1, 2), uniform(coset(2, [(q(1), 0), (q(2), 0)]))),
                                                           (F(1, 2), uniform(coset(2, [(p_(1), 0), (p_(2), 0)])))), True)
cases['new K-CORR2 (on q1=q2=0, weights 3/8,1/8,1/8,3/8 on p1p2=00,01,10,11)'] = (
    2, {pt(0, a, 0, b): (F(3, 8) if a == b else F(1, 8)) for a in (0, 1) for b in (0, 1)}, False)
cases['report9 heralded target (2/5,2/5,1/10,1/10)'] = (1, {pt(0, 0): F(2, 5), pt(1, 0): F(2, 5), pt(0, 1): F(1, 10), pt(1, 1): F(1, 10)}, True)
cases['uniform on 3 points, n=1'] = (1, uniform([pt(0, 0), pt(0, 1), pt(1, 0)]), True)
cases['uniform on 3 points, n=2'] = (2, uniform([0, 1, 2]), False)
L1 = coset(2, [(q(1), 0), (q(2), 0)]); L2 = coset(2, [(q(1), 1), (p_(2), 0)])
cases['uniform on disjoint union U[q1=q2=0] u U[q1=1,p2=0] (not affine), n=2'] = (2, uniform(L1 + L2), True)

def support(d): return frozenset(x for x, v in d.items() if v)
def marg_K1(d, n):
    for i in range(n):
        m = {}
        for x, v in d.items(): k = (x >> 2*i) & 3; m[k] = m.get(k, 0) + v
        if any(v > F(1, 2) for v in m.values()): return False
    return True
checkers = {
    'support>=2^n': lambda d, n: len(support(d)) >= 2**n,
    'vertex-only (d is a uniform isotropic state)': lambda d, n: support(d) in STATES[n] and len(set(v for v in d.values() if v)) == 1,
    'support is isotropic affine (weights ignored)': lambda d, n: support(d) in STATES[n],
    'support contains an isotropic support + marginals in K1': lambda d, n: any(s <= support(d) for s in STATES[n]) and marg_K1(d, n),
    'point prob <= 2^-n + marginals in K1': lambda d, n: max(d.values()) <= F(1, 2**n) and marg_K1(d, n),
}
print('\nexact K_n membership with verified certificates')
truth = {}
for name, (n, d, exp) in cases.items():
    x = vec(d, n); assert sum(x) == 1
    res = lp_member(x, G[n]); v = verify(x, G[n], res); truth[name] = res[0]
    check(v and res[0] == exp, f'{name}: in K{n} = {res[0]} (expected {exp}); certificate verified = {v}; support {len(support(d))}, max p {max(d.values())}, marginals in K1 {marg_K1(d, n)}')
    if not res[0] and name.startswith(('K-BIAS', 'K-COMP2', 'new K-CORR2')):
        print('      separating functional y (y.v<=0 on all generators, y.x>0):', [str(c) for c in res[1]])

ctrl_old = [k for k in cases if k.startswith(('K-BIAS', 'K-COMP2'))]
ctrl_new = [k for k in cases if k.startswith('new ') or k.startswith('report9')]
print('\nweaker checkers vs controls (pass = agrees with exact K_n on every control in the set)')
for cname, f in checkers.items():
    agree = {k: f(cases[k][1], cases[k][0]) == truth[k] for k in cases}
    print(f'  {cname:58s} old controls pass: {all(agree[k] for k in ctrl_old)};'
          f' caught by: {[k.split(" (")[0] for k in ctrl_new if not agree[k]]}')
# the design/kn docstring claim: uniform target in K_n iff its support is an isotropic support
cex = [k for k in cases if k.startswith('uniform on') and truth[k] != (support(cases[k][1]) in STATES[cases[k][0]])]
check(len(cex) > 0, f'design/kn in_Kn_by_support "necessary-and-sufficient for uniform targets" is false: counterexamples {cex}')

# 4. marginal closure: projecting a uniform isotropic state onto a subset of pairs gives a uniform isotropic state
def proj(s, keep):
    out = {}
    for x in s:
        y = 0
        for j, i in enumerate(keep): y |= ((x >> 2*i) & 3) << 2*j
        out[y] = out.get(y, 0) + F(1, len(s))
    return out
good = True
for n, keeps in ((2, [(0,), (1,)]), (3, [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2)])):
    for s in STATES[n]:
        for keep in keeps:
            d = proj(s, keep); S = support(d)
            good = good and S in STATES[len(keep)] and len(set(d.values())) == 1
check(good, 'K_n closed under marginals onto any subset of whole toy pairs (n=2,3 exhaustive)')
# a marginal onto a single coordinate of a pair is outside K's domain: e.g. q1 alone of U[q1=0] is a point mass
print('note: discarding one coordinate of a pair leaves h outside every K_m (K_n is defined on whole pairs)')

# 5. K-POS under K_1 (report8 dynamics, with multiplicities), and K-POS-RET
from collections import defaultdict
def nb(E, x): return [b for a, b in E if a == x] + [a for a, b in E if b == x]
def step(st, E, N):
    u, v = st; return (tuple((sum(u[z] for z in nb(E, x)) + v[x]) % 2 for x in range(N)), u)
def traj(st, E, N, T):
    out = [st]
    for _ in range(T): st = step(st, E, N); out.append(st)
    return out
def fibers(states, E, N, T, rec, at):
    fib = defaultdict(lambda: defaultdict(int))
    for st in states:
        tr = traj(st, E, N, T); fib[rec(tr)][(tr[at][0][1], tr[at][1][1])] += 1
    return [{k: F(c, sum(f.values())) for k, c in f.items()} for f in fib.values()]
E5 = [(0, 1), (1, 2), (0, 3), (1, 4)]; V5 = (0, 2, 3, 4)
S5 = [((a, b, c, 0, 0), (d, e, f, g, h)) for a, b, c, d, e, f, g, h in product((0, 1), repeat=8)]
E4 = [(0, 1), (1, 2), (0, 3)]; V4 = (0, 2, 3)
S4 = [((a, b, c, 0), (d, e, f, 0)) for a, b, c, d, e, f in product((0, 1), repeat=6)]
up = lambda tr, t, V: tuple(tr[t][0][x] for x in V)
k1 = lambda d: all(v <= F(1, 2) for v in d.values())
pos5 = all(k1(d) for t in range(16) for d in fibers(S5, E5, 5, t, lambda tr, t=t: up(tr, t, V5), t))
pos4 = all(k1(d) for t in range(10) for d in fibers(S4, E4, 4, t, lambda tr, t=t: up(tr, t, V4), t))
check(pos5 and pos4, 'K-POS: every u-only terminal record fiber is in K1 (all t in each period), weights included')
ret5 = all(not k1(d) for d in fibers(S5, E5, 5, 3, lambda tr: up(tr, 2, V5) + up(tr, 3, V5), 3))
ret4 = all(not k1(d) for d in fibers(S4, E4, 4, 3, lambda tr: up(tr, 2, V4) + up(tr, 3, V4), 3))
check(ret5 and ret4, 'K-POS-RET: every retained two-time fiber is outside K1')
print('ALL OK' if ok else 'SOME CHECK FAILED'); sys.exit(0 if ok else 1)
