#!/usr/bin/env python3
"""p0_ls_exact.py -- P0 locality sources: the exact run of RULES.md (standard library, exact arithmetic).

The substratum is the kernel's second-order leap (p, c) -> (c, F c - p) over V = Z/q, with a linear link-coupled
finite-range rule F c i = sum_{j in N i} M_ij c_j. In each region the visible datum is the tuple of current components
c and the hidden datum the tuple of previous components p. Laws are exact (Fraction). Every token is printed from the
measurements; a failed control voids the verdict. Cells are those of RULES.md and of amendments/amendment-1.md
(HI-rec).
"""
import sys
from fractions import Fraction
from math import gcd

results = []


def check(name, ok, detail=''):
    results.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''))
    return bool(ok)


# ---------------------------------------------------------------- substrata
class Sub:
    """Sites 0..L-1, each with state (p, c) in V x V, encoded s = p*q + c; a configuration is base q^2 digits,
    site 0 the lowest digit. nbrs[i] is a list of (j, m): F c i = sum m * c_j."""

    def __init__(self, q, L, nbrs):
        self.q, self.L, self.nbrs = q, L, nbrs
        self.base = q * q
        self.size = self.base ** L
        self._phi = None

    def decode(self, x):
        out = []
        for _ in range(self.L):
            s = x % self.base
            out.append((s // self.q, s % self.q))
            x //= self.base
        return out

    def encode(self, cfg):
        x = 0
        for p, c in reversed(cfg):
            x = x * self.base + p * self.q + c
        return x

    def step_cfg(self, cfg):
        q = self.q
        cs = [c for _, c in cfg]
        return [(c, (sum(m * cs[j] for j, m in self.nbrs[i]) - p) % q) for i, (p, c) in enumerate(cfg)]

    @property
    def phi(self):
        if self._phi is None:
            self._phi = [self.encode(self.step_cfg(self.decode(x))) for x in range(self.size)]
        return self._phi


def chain(q, L, alpha, extra=None):
    nb = {i: [(j, alpha) for j in (i - 1, i + 1) if 0 <= j < L] for i in range(L)}
    if extra:
        for i, j, m in extra:
            nb[i] = nb[i] + [(j, m)]
    return Sub(q, L, nb)


def iso(q):
    return Sub(q, 1, {0: []})


def edge(q, a):
    return Sub(q, 2, {0: [(1, a)], 1: [(0, a)]})


class Pair:
    """Two regions placed side by side with no edge across: the joint configuration is x1 + n1 * x2."""

    def __init__(self, r1, r2):
        assert r1.q == r2.q
        self.r1, self.r2, self.q = r1, r2, r1.q
        nb = {i: list(v) for i, v in r1.nbrs.items()}
        for i, v in r2.nbrs.items():
            nb[i + r1.L] = [(j + r1.L, m) for j, m in v]
        self.full = Sub(r1.q, r1.L + r2.L, nb)
        self.n1, self.n2 = r1.size, r2.size

    def split(self, x):
        return x % self.n1, x // self.n1

    def join(self, x1, x2):
        return x1 + self.n1 * x2


def vis(sub, x):
    return tuple(c for _, c in sub.decode(x))


# ---------------------------------------------------------------- K-leap
c6 = chain(3, 6, 1)
k1 = c6.step_cfg([(1, 2), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0)]) == [(2, 0), (1, 2), (0, 1), (0, 0), (0, 0), (0, 0)]
ue = Pair(edge(3, 1), edge(3, 2)).full
k2 = ue.step_cfg([(0, 1), (2, 2), (1, 1), (0, 2)]) == [(1, 2), (2, 2), (1, 0), (2, 2)]
k3 = iso(3).step_cfg([(1, 0)]) == [(0, 2)]
bij = all(len(set(s.phi)) == s.size for s in
          (iso(3), iso(5), edge(3, 1), edge(3, 2), Pair(iso(3), iso(3)).full, ue, chain(3, 4, 1)))
check('K-leap', k1 and k2 and k3 and bij, 'three hand-computed steps and bijectivity on the frozen Conf sets')

# ---------------------------------------------------------------- K-free
kf = True
for q in (3, 5):
    s = iso(q)
    for x in range(1, s.size):
        y = x
        orb = [x]
        for _ in range(4):
            y = s.phi[y]
            orb.append(y)
        kf &= orb[4] == x and orb[2] != x and orb[1] != x
check('K-free', kf, 'the isolated-site leap has order exactly 4 on every nonzero (p, c), q = 3, 5')


# ---------------------------------------------------------------- orbits
def orbits_iter(n, f):
    seen = bytearray(n)
    out = []
    for x in range(n):
        if not seen[x]:
            o = []
            y = x
            while not seen[y]:
                seen[y] = 1
                o.append(y)
                y = f(y)
            out.append(o)
    return out


def orbits_uf(n, f):
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for x in range(n):
        a, b = find(x), find(f(x))
        if a != b:
            parent[a] = b
    groups = {}
    for x in range(n):
        groups.setdefault(find(x), []).append(x)
    return list(groups.values())


def canon(orbs):
    return sorted(tuple(sorted(o)) for o in orbs)


# ---------------------------------------------------------------- laws and tests
def push(law, f):
    out = {}
    for x, w in law.items():
        y = f(x)
        out[y] = out.get(y, 0) + w
    return out


def marg(law, g):
    out = {}
    for x, w in law.items():
        k = g(x)
        out[k] = out.get(k, 0) + w
    return out


def is_product_entry(joint):
    """Entrywise against the product of marginals (zeros included)."""
    m1, m2 = {}, {}
    for (a, b), w in joint.items():
        m1[a] = m1.get(a, 0) + w
        m2[b] = m2.get(b, 0) + w
    return all(joint.get((a, b), 0) == wa * wb for a, wa in m1.items() for b, wb in m2.items())


def is_product_minor(joint):
    """All 2x2 minors of the joint matrix vanish (rank at most one)."""
    rows = sorted({a for a, _ in joint})
    cols = sorted({b for _, b in joint})
    M = [[joint.get((a, b), 0) for b in cols] for a in rows]
    for i in range(len(rows)):
        for k in range(i + 1, len(rows)):
            for j in range(len(cols)):
                for l in range(j + 1, len(cols)):
                    if M[i][j] * M[k][l] != M[i][l] * M[k][j]:
                        return False
    return True


prod_disagree = [0]


def is_product(joint):
    a, b = is_product_entry(joint), is_product_minor(joint)
    if a != b:
        prod_disagree[0] += 1
    return a


# K-prod
pl = {(a, b): Fraction(1 + a, 6) * Fraction(1 + 2 * b, 4) for a in range(3) for b in range(2)}
cl = {(0, 0): Fraction(1, 2), (1, 1): Fraction(1, 2)}
check('K-prod', is_product_entry(pl) and is_product_minor(pl) and not is_product_entry(cl)
      and not is_product_minor(cl), 'both product tests accept a product law and reject a correlated one')


class Model:
    """A Pair with the visible and hidden data and the laws over it."""

    def __init__(self, pair):
        self.P = pair
        f = pair.full
        self.phi = f.phi
        self.v1 = [vis(pair.r1, pair.split(x)[0]) for x in range(f.size)]
        self.v2 = [vis(pair.r2, pair.split(x)[1]) for x in range(f.size)]

    def evolve(self, law, t):
        for _ in range(t):
            law = push(law, lambda x: self.phi[x])
        return law

    def jvis(self, law):
        return marg(law, lambda x: (self.v1[x], self.v2[x]))

    def kernel_product(self, law):
        """Gamma(v'|v) = Gamma1(v1'|v1) Gamma2(v2'|v2) on the support of the visible law."""
        two = marg(law, lambda x: ((self.v1[x], self.v2[x]), (self.v1[self.phi[x]], self.v2[self.phi[x]])))
        pv = {}
        for (v, _), w in two.items():
            pv[v] = pv.get(v, 0) + w
        t1, t2, p1, p2 = {}, {}, {}, {}
        for ((a1, a2), (b1, b2)), w in two.items():
            t1[(a1, b1)] = t1.get((a1, b1), 0) + w
            t2[(a2, b2)] = t2.get((a2, b2), 0) + w
            p1[a1] = p1.get(a1, 0) + w
            p2[a2] = p2.get(a2, 0) + w
        outs1 = sorted({b for _, b in t1})
        outs2 = sorted({b for _, b in t2})
        for (a1, a2), w in pv.items():
            for b1 in outs1:
                for b2 in outs2:
                    lhs = two.get(((a1, a2), (b1, b2)), 0) / w
                    rhs = (t1.get((a1, b1), 0) / p1[a1]) * (t2.get((a2, b2), 0) / p2[a2])
                    if lhs != rhs:
                        return False
        return True

    def region1_series(self, law, T):
        """Region 1's visible law at t = 0..T and its two-time law at t = 0..T-1."""
        out = []
        cur = law
        for t in range(T + 1):
            out.append(marg(cur, lambda x: self.v1[x]))
            if t < T:
                out.append(marg(cur, lambda x: (self.v1[x], self.v1[self.phi[x]])))
                cur = push(cur, lambda x: self.phi[x])
        return out

    def sel_split(self, law, T):
        """True iff conditioning on region 2's visible value changes region 1's visible law at some t <= T."""
        cur = law
        for t in range(T + 1):
            m1 = marg(cur, lambda x: self.v1[x])
            j = self.jvis(cur)
            p2 = {}
            for (a, b), w in j.items():
                p2[b] = p2.get(b, 0) + w
            for b, wb in p2.items():
                for a in m1:
                    if j.get((a, b), 0) / wb != m1[a]:
                        return True
            cur = push(cur, lambda x: self.phi[x])
        return False


def site_interventions(q):
    """Permutations of one site's state s = p*q + c: translations, the exchange, one transposition."""
    out = []
    for a in range(q):
        for b in range(q):
            if (a, b) != (0, 0):
                out.append(('T(%d,%d)' % (a, b), [((s // q + a) % q) * q + (s % q + b) % q for s in range(q * q)]))
    out.append(('X', [(s % q) * q + s // q for s in range(q * q)]))
    tr = list(range(q * q))
    tr[0], tr[1] = 1, 0
    out.append(('tau', tr))
    return out


def intervene_region2(pair, site_local, perm):
    """The permutation of the full Conf applying perm to region 2's site `site_local`."""
    r2 = pair.r2
    base = r2.base
    shift = base ** site_local

    def g(x):
        x1, x2 = pair.split(x)
        s = (x2 // shift) % base
        x2n = x2 + (perm[s] - s) * shift
        return pair.join(x1, x2n)
    return g


def uniform(states):
    w = Fraction(1, len(states))
    return {x: w for x in states}


# ---------------------------------------------------------------- the uncoupled models
T = 8
models = {}
for q in (3, 5):
    models['U-free(%d)' % q] = Model(Pair(iso(q), iso(q)))
for a in (1, 2):
    for b in (1, 2):
        models['U-edge(3,%d,%d)' % (a, b)] = Model(Pair(edge(3, a), edge(3, b)))


def regional_orbits(sub):
    return orbits_iter(sub.size, lambda y: sub.phi[y])


def ensembles(name, M):
    P = M.P
    f = P.full
    ens = [('E-cnt', uniform(range(f.size)))]
    o1, o2 = regional_orbits(P.r1), regional_orbits(P.r2)
    for i, A in enumerate(o1):
        for j, B in enumerate(o2):
            ens.append(('E-reg[%d,%d]' % (i, j), uniform([P.join(a, b) for a in A for b in B])))
    for k, O in enumerate(orbits_iter(f.size, lambda y: M.phi[y])):
        ens.append(('E-orb[%d]' % k, uniform(O)))
    # E-pri: p-tuple of region 1 equal to the p-tuple of region 2, c free
    pri = [x for x in range(f.size)
           if [p for p, _ in P.r1.decode(P.split(x)[0])] == [p for p, _ in P.r2.decode(P.split(x)[1])]]
    ens.append(('E-pri', uniform(pri)))
    return ens


# ---------------------------------------------------------------- FAC
def depends_across(sub, R1, R2):
    """True iff the next state of some R1 site depends on the configuration of R2 (exhaustive)."""
    by_r1 = {}
    for x in range(sub.size):
        cfg = sub.decode(x)
        key = tuple(cfg[i] for i in R1)
        img = sub.decode(sub.phi[x])
        val = tuple(img[i] for i in R1)
        if by_r1.setdefault(key, val) != val:
            return True
    return False


fac_ok = True
fac_detail = []
for name, M in models.items():
    P = M.P
    eq = all(P.split(M.phi[x]) == (P.r1.phi[P.split(x)[0]], P.r2.phi[P.split(x)[1]]) for x in range(P.full.size))
    fac_ok &= eq
fam_fac = True
for q in (3, 5):
    types = [('iso', iso(q))] + [('edge%d' % a, edge(q, a)) for a in range(1, q)]
    for _, r1 in types:
        for _, r2 in types:
            P = Pair(r1, r2)
            f = P.full
            fam_fac &= all(P.split(f.phi[x]) == (r1.phi[P.split(x)[0]], r2.phi[P.split(x)[1]])
                           for x in range(f.size))
            f._phi = None
cut = chain(3, 4, 1)
cut_dep = depends_across(cut, [0, 1], [2, 3]) and depends_across(cut, [2, 3], [0, 1])
unc_dep = not depends_across(Pair(edge(3, 1), edge(3, 2)).full, [0, 1], [2, 3]) and \
    not depends_across(Pair(edge(3, 1), edge(3, 2)).full, [2, 3], [0, 1])
fac_cell = check('FAC', fac_ok and fam_fac and cut_dep and unc_dep,
                 'phi = phi1 x phi2 on U-free, U-edge and FAM; C-cut depends across the cut in both directions')

# ---------------------------------------------------------------- TC and K-cone-neg
def tc_check(sub, src_site, dst_site, dist):
    """From every point mass, every site intervention at src leaves dst's (p, c) unchanged for t < dist; returns
    (holds, some intervention changes dst's c at t = dist)."""
    base = sub.base
    shift = base ** src_site
    dshift = base ** dst_site
    phi = sub.phi
    ivs = site_interventions(sub.q)
    holds, arrives = True, False
    for x in range(sub.size):
        traj = [x]
        for _ in range(dist):
            traj.append(phi[traj[-1]])
        s = (x // shift) % base
        for _, perm in ivs:
            y = x + (perm[s] - s) * shift
            for t in range(dist + 1):
                a = (traj[t] // dshift) % base
                b = (y // dshift) % base
                if t < dist and a != b:
                    holds = False
                if t == dist and a % sub.q != b % sub.q:
                    arrives = True
                if t < dist:
                    y = phi[y]
        if not holds:
            break
    return holds, arrives


tc_holds, tc_arr = tc_check(chain(3, 6, 1), 5, 0, 5)
neg_holds, _ = tc_check(chain(3, 6, 1, extra=[(0, 3, 1)]), 5, 0, 5)
check('K-cone-neg', not neg_holds, 'site 0 reading site 3 breaks the cone check on C-chain')
tc_cell = tc_holds and tc_arr
print('     TC on C-chain: unchanged for t < 5 from every point mass: %s; some intervention reaches c0 at t = 5: %s'
      % (tc_holds, tc_arr))

# ---------------------------------------------------------------- INS, HI, SEL on the uncoupled models
ins_ok = True
hi_default = True
orb_nonprod_ins = []
pri_nonprod_ins = []
sel_default_split = False
sel_corr_split = []
counts = {}
for name, M in models.items():
    P = M.P
    f = P.full
    ivs = site_interventions(P.q)
    gs = [(lab, intervene_region2(P, 0, perm)) for lab, perm in ivs]
    ens = ensembles(name, M)
    n_orb = n_orb_np = 0
    for lab, law in ens:
        base_series = M.region1_series(law, T)
        ins_here = True
        for _, g in gs:
            if M.region1_series(push(law, g), T) != base_series:
                ins_here = False
                break
        ins_ok &= ins_here
        # an invariant law has the same visible law and kernel at every tick, so one tick decides all of them
        invariant = push(law, lambda x: M.phi[x]) == law
        tt = 1 if invariant else T
        prod_vis = all(is_product(M.jvis(M.evolve(law, t))) for t in range(tt + (0 if invariant else 1)))
        prod_ker = all(M.kernel_product(M.evolve(law, t)) for t in range(tt))
        if lab == 'E-cnt' or lab.startswith('E-reg'):
            hi_default &= prod_vis and prod_ker
            sel_default_split |= M.sel_split(law, T)
        if lab.startswith('E-orb'):
            n_orb += 1
            if not (prod_vis and prod_ker):
                n_orb_np += 1
                if ins_here:
                    orb_nonprod_ins.append((name, lab))
        if lab == 'E-pri' and not prod_ker and ins_here:
            pri_nonprod_ins.append(name)
        if (lab.startswith('E-orb') or lab == 'E-pri') and M.sel_split(law, T):
            sel_corr_split.append((name, lab))
    # point masses
    phi = M.phi
    for x in range(f.size):
        tr = [x]
        for _ in range(T):
            tr.append(phi[tr[-1]])
        base1 = [M.v1[y] for y in tr]
        for _, g in gs:
            y = g(x)
            s1 = []
            for _ in range(T + 1):
                s1.append(M.v1[y])
                y = phi[y]
            if s1 != base1:
                ins_ok = False
    counts[name] = (len(ens), n_orb, n_orb_np)
    print('     %s: %d ensembles (%d orbit laws, %d with a non-product visible law or kernel), %d point masses, '
          '%d interventions' % (name, len(ens), n_orb, n_orb_np, f.size, len(gs)))

# coupled countercontrol for INS
cutsub = chain(3, 4, 1)
ins_neg = False
for x in range(cutsub.size):
    y0 = cutsub.phi[x]
    cfg = cutsub.decode(x)
    for _, perm in site_interventions(3):
        s = cfg[2][0] * 3 + cfg[2][1]
        cfg2 = list(cfg)
        cfg2[2] = (perm[s] // 3, perm[s] % 3)
        y1 = cutsub.phi[cutsub.encode(cfg2)]
        if [c for _, c in cutsub.decode(y0)[:2]] != [c for _, c in cutsub.decode(y1)[:2]]:
            ins_neg = True
            break
    if ins_neg:
        break
check('K-INS-neg', ins_neg, 'on C-cut a region-2 intervention changes region 1\'s visible value at t = 1')

# ---------------------------------------------------------------- HI-orbit (a): W4 on FAM, and K-orbit
w4_ok = True
w4_counts = []
korb = True
for q in (3, 5):
    types = [('iso', iso(q))] + [('edge%d' % a, edge(q, a)) for a in range(1, q)]
    n_orbits = n_prod = n_exc = 0
    for _, r1 in types:
        reg1 = {x: o for o in regional_orbits(r1) for x in o}
        for _, r2 in types:
            reg2 = {x: o for o in regional_orbits(r2) for x in o}
            P = Pair(r1, r2)
            n = P.n1 * P.n2
            p1, p2 = r1.phi, r2.phi
            n1 = P.n1

            def fj(x, p1=p1, p2=p2, n1=n1):
                return p1[x % n1] + n1 * p2[x // n1]
            orbs = orbits_iter(n, fj)
            korb &= canon(orbs) == canon(orbits_uf(n, fj))
            for O in orbs:
                pr1 = {x % n1 for x in O}
                pr2 = {x // n1 for x in O}
                x1, x2 = O[0] % n1, O[0] // n1
                full_proj = pr1 == set(reg1[x1]) and pr2 == set(reg2[x2])
                product = len(O) == len(pr1) * len(pr2)
                crit = gcd(len(reg1[x1]), len(reg2[x2])) == 1
                n_orbits += 1
                n_prod += product
                if not full_proj or product != crit or len(O) != len(reg1[x1]) * len(reg2[x2]) // gcd(
                        len(reg1[x1]), len(reg2[x2])):
                    n_exc += 1
    w4_ok &= n_exc == 0
    w4_counts.append('q=%d: %d joint orbits, %d with a product law, %d exceptions' % (q, n_orbits, n_prod, n_exc))
check('K-orbit', korb, 'iteration and union-find agree on every joint orbit of FAM(3) and FAM(5)')
print('     W4 on FAM: ' + '; '.join(w4_counts))
print('     product-test disagreements between the two methods: %d' % prod_disagree[0])
kprod_runtime = prod_disagree[0] == 0
check('K-prod-agree', kprod_runtime, 'the entrywise and minor tests agree on every law tested')

# ---------------------------------------------------------------- HI-rec (amendment 1)
hi_rec = True
rec_counts = []
for name, M in models.items():
    P = M.P
    f = P.full
    orbs = orbits_iter(f.size, lambda y: M.phi[y])
    oid = [0] * f.size
    for k, O in enumerate(orbs):
        for x in O:
            oid[x] = k
    records = {}
    for x in range(f.size):
        records.setdefault((M.v1[x], M.v2[x]), []).append(x)
    n_rec = n_unc_np = 0
    for (a, b), R in sorted(records.items()):
        meet = sorted({oid[x] for x in R})
        U = [x for k in meet for x in orbs[k]]
        muR = uniform(U)
        assert push(muR, lambda x: M.phi[x]) == muR
        Rs = set(R)
        zr = sum(w for x, w in muR.items() if x in Rs)
        cond = {x: w / zr for x, w in muR.items() if x in Rs}
        n_rec += 1
        if not is_product_entry(marg(muR, lambda x: P.split(x))):
            n_unc_np += 1
        ok = all(is_product(M.jvis(M.evolve(cond, t))) for t in range(T + 1)) and \
            all(M.kernel_product(M.evolve(cond, t)) for t in range(T)) and not M.sel_split(cond, T)
        hi_rec &= ok
    rec_counts.append('%s: %d records, %d unconditioned laws not a product on Conf' % (name, n_rec, n_unc_np))
print('     HI-rec: ' + '; '.join(rec_counts))

# ---------------------------------------------------------------- cells and tokens
controls = all(ok for name, ok in results if name.startswith('K-'))
cells = {
    'TC': tc_cell,
    'FAC': fac_cell,
    'INS': ins_ok and ins_neg,
    'HI-default': hi_default,
    'HI-rec': hi_rec,
    'HI-orbit': w4_ok and bool(orb_nonprod_ins),
    'HI-prior': 'U-free(3)' in pri_nonprod_ins,
    'SEL': (not sel_default_split) and bool(sel_corr_split),
}
tokens = {'TC': 'LS-TC', 'FAC': 'LS-FAC', 'INS': 'LS-INS-ALL-PRIORS', 'HI-default': 'LS-HI-DEFAULT', 'HI-rec': 'LS-HI-REC',
          'HI-orbit': 'LS-HI-ORBIT-FAILS', 'HI-prior': 'LS-HI-PRIOR-FAILS', 'SEL': 'LS-SEL-SPLIT'}
print('     orbit laws non-product with INS: %d (first: %s)' % (len(orb_nonprod_ins), orb_nonprod_ins[:3]))
print('     E-pri non-product kernel with INS: %s' % pri_nonprod_ins)
print('     selection-dependent correlated laws: %d (first: %s); default laws selection-dependent: %s'
      % (len(sel_corr_split), sel_corr_split[:3], sel_default_split))
for k, v in cells.items():
    print('CELL %-10s %s' % (k, 'positive' if v else 'negative'))
if not controls:
    print('VERDICT VOID (a control failed)')
    sys.exit(1)
for k, v in cells.items():
    if v:
        print('TOKEN %s' % tokens[k])
split = cells['INS'] and cells['HI-default'] and cells['HI-rec'] and cells['HI-orbit'] and cells['HI-prior']
print('VERDICT ' + ('LS-SPLIT' if split else 'LS-NOT-SPLIT'))
fails = sum(1 for _, ok in results if not ok)
print('checks: %d, failures: %d' % (len(results), fails))
sys.exit(0)
