"""NP-AVG-1 Stage 0 Layer 2: the dry run (section 5b item 1; certificate item 7).

Computes, from the configuration constants alone, the index space, the orbit count (by
Burnside's lemma), the shard plan, the context-size histogram, the masking-equivalent
record count and the cost estimate. It imports neither the engine (s0geom) nor the
reference (s0ref): it constructs no Setup, no Context and no record through the guarded
entry points, and computes no closure (static check L2-S1 verifies the imports). Its
formulas are checked against the engine on the toy profile by l2selftest (L2-PLAN, L2-MASK).

Usage: python3 -I -B l2plan.py --profile toy|v8 [--calib calib.json] [--out dryrun.json]
                               [--shared-tips]
--shared-tips enumerates the record space combinatorially (no closure) to count records with
a shared near tip (C7's scope). For v8 it is part of the owner's F3 decision and is not run
locally; the estimate then states the C7 term per percent of representatives.
"""
import hashlib
import json
import os
import sys
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l2config as CFG  # noqa: E402


def lball(r, dim):
    if r < 0:
        return []
    if dim == 0:
        return [()]
    return [(x,) + rest for x in range(-r, r + 1) for rest in lball(r - abs(x), dim - 1)]


def norm(c):
    return sum(abs(i) for i in c)


class Space:
    def __init__(self, prof):
        s = prof['setup']
        self.dim, self.n, self.rho, self.tlast = s['dim'], s['n'], s['rho'], s['tlast']
        self.port = tuple(s['port'])
        self.k = prof['k']
        self.region = sorted(lball(self.rho, self.dim))
        self.slices = list(range(-1, self.tlast + 1))
        o = (0,)*self.dim
        six = []
        for i in range(self.dim):
            for sg in (1, -1):
                six.append((tuple(sg if j == i else 0 for j in range(self.dim)), self.n + 1))
        self.fixed = set(six) | {(o, self.n + 2), (o, self.n)}
        self.port_even = {(self.port, s) for s in range(0, self.n + 1) if (norm(self.port) + s) % 2 == 0}
        self.removed = self.fixed | self.port_even

    def n_records(self):
        ni, ns, nt = len(self.region)*len(self.slices), len(self.region), len(self.slices)
        return ni + (ns*(ns - 1)//2)*nt*nt if self.k == 2 else ni

    def item_set(self, x, t):
        return {(x, s) for s in range(-1, t + 1) if (norm(x) + s) % 2 == 0} - self.removed

    def group(self):
        dim = self.dim
        q8 = tuple(-1 if j == dim - 1 else 0 for j in range(dim))
        q10 = tuple(1 if j == dim - 1 else 0 for j in range(dim))
        reg = set(self.region)
        out = []
        for pp in permutations(range(dim)):
            for ss in product((1, -1), repeat=dim):
                def a(c, pp=pp, ss=ss):
                    return tuple(ss[i]*c[pp[i]] for i in range(dim))
                if {a(c) for c in reg} == reg and a(self.port) == self.port and a(q8) == q8 and a(q10) == q10:
                    out.append(a)
        return out

    def orbits_burnside(self):
        grp = self.group()
        nt = len(self.slices)
        fix1 = sum(sum(1 for x in self.region if g(x) == x)*nt for g in grp)
        fix2 = 0
        for g in grp:
            nf = sum(1 for x in self.region if g(x) == x)
            swaps = sum(1 for x in self.region if g(x) != x and g(g(x)) == x)//2
            fix2 += (nf*(nf - 1)//2)*nt*nt + swaps*nt
        single = fix1//len(grp)
        pair = fix2//len(grp) if self.k == 2 else 0
        return len(grp), single, pair


def shard_plan(N, S):
    return [{'shard': s, 'lo': s*N//S, 'hi': (s + 1)*N//S, 'count': (s + 1)*N//S - s*N//S} for s in range(S)]


def context_histogram(sp):
    """Histogram of the number of non-fixed context quantities over all records (singles and
    two-site pairs), from per-item sample counts."""
    base = len(sp.port_even - sp.fixed)
    per_site = {x: Counter(len(sp.item_set(x, t)) for t in sp.slices) for x in sp.region}
    singles = Counter()
    for h in per_site.values():
        for a, c in h.items():
            singles[base + a] += c
    pairs = Counter()
    if sp.k == 2:
        tot = Counter()
        for h in per_site.values():
            tot.update(h)
        for a, ca in tot.items():
            for b, cb in tot.items():
                pairs[base + a + b] += ca*cb
        for h in per_site.values():
            for a, ca in h.items():
                for b, cb in h.items():
                    pairs[base + a + b] -= ca*cb
        pairs = Counter({k: v//2 for k, v in pairs.items() if v})
    return singles, pairs


def masking_equivalent(sp, merge_fixed=True):
    """Number of records in masking-equivalence classes of size >= 2 (E2). With merge_fixed
    (the plan's reading, 'equal even-class contexts'), samples that are fixed quantities or
    port samples are merged with them (E1); with merge_fixed False, records are compared by
    their even record samples alone (the code-r5 design-evidence reading). Exact integers.
    Canonical form: an item (x, t) maps to (x, m), m the largest slice of its sample set
    (empty sets map to nothing); two records have equal sample sets iff their canonical
    forms are equal (LAYER2-PLAN.md PO-L2-7)."""
    rem = sp.removed if merge_fixed else set()

    def m_of(x, t):
        st = {(x, s) for s in range(-1, t + 1) if (norm(x) + s) % 2 == 0} - rem
        return max(s for _, s in st) if st else None
    c = {x: Counter(m_of(x, t) for t in sp.slices) for x in sp.region}
    E = {x: c[x].get(None, 0) for x in sp.region}
    Etot = sum(E.values())
    total = 0

    def add(size):
        return size if size >= 2 else 0
    # empty class: singles with empty sets and pairs of empty items at distinct sites
    empty = Etot + ((Etot*Etot - sum(v*v for v in E.values()))//2 if sp.k == 2 else 0)
    total += add(empty)
    for x in sp.region:
        for m, cxm in c[x].items():
            if m is None:
                continue
            total += add(cxm + (cxm*(Etot - E[x]) if sp.k == 2 else 0))
    if sp.k == 2:
        reg = sp.region
        for i in range(len(reg)):
            for j in range(i + 1, len(reg)):
                for m1, c1 in c[reg[i]].items():
                    if m1 is None:
                        continue
                    for m2, c2 in c[reg[j]].items():
                        if m2 is not None:
                            total += add(c1*c2)
    return total


def near_tips(q, E):
    """{(e, tip)} of q's near tips for the pair (E, E+1) (plan section 2)."""
    c, t = q
    L = E + 1
    d, near = (t - L, L) if t >= L else (E - t, E)
    dim = len(c)
    out = set()
    for i in range(dim):
        for sg in (1, -1):
            e = tuple(sg if j == i else 0 for j in range(dim))
            out.add((e, (tuple(a + d*b for a, b in zip(c, e)), near)))
    return out


def shared_tip_records(sp):
    """Records whose initial context (non-fixed quantities) has a cell that is the e-near-tip
    of two distinct quantities, per convention (A: pair (n+1, n+2); G: pair (-1, 0)).
    Enumerates the record space combinatorially; no closure."""
    out = {}
    for conv, E in (('A', sp.n + 1), ('G', -1)):
        port_q = sp.port_even - sp.fixed

        def tipsets(qs):
            return [near_tips(q, E) for q in sorted(qs)]

        def shared(qs):
            seen = {}
            for i, ts in enumerate(tipsets(qs)):
                for k in ts:
                    if k in seen and seen[k] != i:
                        return True
                    seen[k] = i
            return False
        items = [(x, t) for x in sp.region for t in sp.slices]
        sets = {it: sp.item_set(*it) for it in items}
        n = sum(shared(port_q | sets[it]) for it in items)
        if sp.k == 2:
            for i, a in enumerate(sp.region):
                for b in sp.region[i + 1:]:
                    for t1 in sp.slices:
                        for t2 in sp.slices:
                            n += shared(port_q | sets[(a, t1)] | sets[(b, t2)])
        out[conv] = n
    return out


def _ceil(fr):
    fr = Fraction(fr)
    return -((-fr.numerator)//fr.denominator)


def _t(table, m):
    """Calibrated time (ns) at size m: the smallest calibrated size >= m; beyond the largest,
    scaled quadratically (the closure's cover computation is tips x quantities)."""
    ks = sorted(table)
    hi = [k for k in ks if k >= m]
    if hi:
        return table[hi[0]]
    return table[ks[-1]]*m*m//(ks[-1]*ks[-1])


def universe_sizes(sp):
    """Non-fixed quantities of the S1a contexts: the global union, and each axis line."""
    port_q = sp.port_even - sp.fixed
    U = set(port_q)
    for x in sp.region:
        U |= sp.item_set(x, sp.tlast)
    lines = {}
    for x in sp.region:
        for i in range(sp.dim):
            lines.setdefault((i, tuple(x[j] for j in range(sp.dim) if j != i)), []).append(x)
    sizes = []
    for sites in lines.values():
        q = set(port_q)
        for x in sites:
            q |= sp.item_set(x, sp.tlast)
        sizes.append(len(q))
    return len(U), sizes


def estimate(sp, hist, orbits, N, calib, prof, shared=None):
    """The complete cost estimate in runner-seconds (L2-R6), term by term; LAYER2-PLAN.md section
    3.6 states each term. Fractions are exact and rounded up at the end. The launch decision needs
    kappa (owner-set, L2-R7) and the C7 term under the chosen scope (F3); while either is an OWNER
    placeholder, launch_within_budget is None and the reason is stated."""
    bud = CFG.CONFIG['budget']
    singles, pairs = hist
    tA = {int(k): v for k, v in calib['closure_ns_A'].items()}
    tG = {int(k): v for k, v in calib['closure_ns_G'].items()}
    rA = {int(k): v for k, v in calib['ref_c7_ns_A'].items()}
    rG = {int(k): v for k, v in calib['ref_c7_ns_G'].items()}
    NS = 10**9
    scale = Fraction(orbits, N)
    allm = list(singles.items()) + list(pairs.items())
    nrec = sum(c for _, c in allm)
    mbar = _ceil(Fraction(sum(m*c for m, c in allm), nrec))
    mmax = max(m for m, _ in allm)
    reps = Fraction(orbits)
    S = prof['shards']
    terms = {}
    # 1. four closures per representative, analysis overhead, normal and -O
    base = sum(c*(2*_t(tA, m) + 2*_t(tG, m)) for m, c in allm)
    terms['closures'] = Fraction(base, NS)*scale*bud['gate_overhead_factor']*2
    # 2. sampled gates: C7, C11 (i), C17, C18 at their rates, each costed as one reference closure
    #    per convention at the mean size; C8 on 1 in R orbits: 8 members x 4 closures
    rates = prof['sampling']
    ref_mean = _t(rA, mbar) + _t(rG, mbar)
    samp = sum(Fraction(1, rates[g]) for g in ('C7', 'C11i', 'C17', 'C18'))*reps*ref_mean
    c8 = Fraction(1, rates['C8_orbits'])*reps*8*(2*_t(tA, mbar) + 2*_t(tG, mbar))
    terms['sampled_gates'] = (samp + c8)/NS*2
    # 3. C7 on shared-tip representatives, by scope (F3)
    per_pct = {'A': Fraction(reps*_t(rA, mbar), 100*NS)*2, 'G': Fraction(reps*_t(rG, mbar), 100*NS)*2}
    c7 = {'seconds_per_percent_of_representatives': {k: _ceil(v) for k, v in per_pct.items()}}
    scope = prof['C7_scope']
    c7['scope'] = scope
    if shared is not None:
        shr = {conv: Fraction(shared[conv])*scale for conv in ('A', 'G')}
        by = {'initial_context': (shr['A']*_t(rA, mbar) + shr['G']*_t(rG, mbar))/NS*2}
        by['sampled_initial_context_1_in_100'] = by['initial_context']/100
        c7['by_scope_seconds'] = {k: _ceil(v) for k, v in by.items()}
        c7['shared_tip_representatives_estimated'] = {k: _ceil(v) for k, v in shr.items()}
        terms['C7_scope'] = by.get(scope)
    else:
        c7['by_scope_seconds'] = None
        c7['pending'] = 'the shared-tip count (l2plan --shared-tips) is not computed'
        terms['C7_scope'] = None
    # 4. survivor gates, bounded by the survivor cap per shard: per survivor orbit, up to 8 members
    #    x (4 closures + 2 conventions x 4 reference gates) at the largest context size
    per_orbit = 8*(2*_t(tA, mmax) + 2*_t(tG, mmax) + 4*(_t(rA, mmax) + _t(rG, mmax)))
    terms['survivor_gates_cap'] = Fraction(bud['survivor_cap_per_shard']*S*per_orbit, NS)*2
    # 5. pre-flight and merge: stated allowances
    terms['preflight'] = Fraction(bud['preflight_seconds'])
    terms['merge'] = Fraction(bud['merge_seconds'])*2
    # 6. S1a: 4 bound closures and 4 streamed reference checks at the universe size, and the
    #    per-line closures (2 per line), normal and -O
    mU, lsizes = universe_sizes(sp)
    ks = max(rA)
    s1a = 2*_t(tA, mU) + 2*_t(tG, mU) + 2*(rA[ks] + rG[ks])*mU//ks + sum(_t(tA, m) + _t(tG, m) for m in lsizes)
    terms['s1a'] = Fraction(s1a, NS)*2
    total = None if any(v is None for v in terms.values()) else sum(terms.values())
    shard_job = None if terms['C7_scope'] is None else \
        (terms['closures'] + terms['sampled_gates'] + terms['C7_scope'] + terms['survivor_gates_cap'])/S
    jobs = {'shard': shard_job, 's1a': terms['s1a'], 'preflight': terms['preflight'], 'merge': terms['merge']}
    tmo = {k: bud['timeout_minutes'][k]*60 for k in jobs}
    kappa = bud['kappa']
    if kappa == CFG.OWNER:
        launch, why = None, 'kappa is an OWNER placeholder (L2-R7)'
    elif total is None:
        launch, why = None, 'the C7 term under the chosen scope is not available'
    else:
        launch = kappa*total <= bud['runner_hours']*3600 and all(kappa*v <= tmo[k] for k, v in jobs.items())
        why = 'kappa * total <= budget and kappa * each job <= its timeout'
    return {'terms_runner_seconds': {k: (None if v is None else _ceil(v)) for k, v in terms.items()},
            'total_runner_seconds': None if total is None else _ceil(total),
            'total_without_C7_scope_term': _ceil(sum(v for k, v in terms.items() if k != 'C7_scope')),
            'per_job_seconds': {k: (None if v is None else _ceil(v)) for k, v in jobs.items()},
            'job_timeouts_seconds': tmo, 'budget_runner_seconds': bud['runner_hours']*3600,
            'kappa': kappa, 'C7': c7, 'mean_context_size_bucket_input': mbar, 'max_context_size': mmax,
            'universe_quantities': mU, 'survivor_cap_per_shard': bud['survivor_cap_per_shard'],
            'launch_within_budget': launch, 'launch_rule': why}


def main():
    args = sys.argv[1:]
    pname = args[args.index('--profile') + 1]
    prof = CFG.profile(pname)
    sp = Space(prof)
    N = sp.n_records()
    gorder, so, po = sp.orbits_burnside()
    S = prof['shards']
    singles, pairs = context_histogram(sp)
    out = {'schema': 'np-avg-1/stage0/layer2/dryrun/1', 'profile': pname, 'records': N,
           'group_order': gorder, 'orbits': so + po, 'single_orbits': so, 'pair_orbits': po,
           'shards': shard_plan(N, S), 'context_quantities_singles': {str(k): v for k, v in sorted(singles.items())},
           'context_quantities_pairs': {str(k): v for k, v in sorted(pairs.items())},
           'max_context_quantities': max(list(singles) + list(pairs)),
           'max_context_with_fixed': max(list(singles) + list(pairs)) + len(sp.fixed),
           'closures_computed': 0, 'contexts_constructed': 0, 'engine_imported': 'l2plan imports no engine',
           'config_sha256': CFG.config_sha256()}
    if not prof['requires_authorization']:
        # a reported count (section 6, C8); computed in the dry run for the toy profile only. For
        # v8 the merge computes it in the authorized run.
        out['masking_equivalent_records'] = masking_equivalent(sp, True)
        out['masking_equivalent_records_record_sample_reading'] = masking_equivalent(sp, False)
    exp = CFG.CONFIG['expected'].get(pname, {})
    checks = {}
    for k_exp, k_out in (('records', 'records'), ('orbits', 'orbits'), ('group_order', 'group_order')):
        if k_exp in exp:
            checks[k_exp] = exp[k_exp] == out[k_out]
    out['expected_checks'] = checks
    shared = None
    if '--shared-tips' in args:
        shared = out['shared_tip_records'] = shared_tip_records(sp)
    if '--calib' in args:
        with open(args[args.index('--calib') + 1], 'rb') as f:
            raw = f.read()
        calib = json.loads(raw)
        out['calib_sha256'] = hashlib.sha256(raw).hexdigest()
        out['cost'] = estimate(sp, (singles, pairs), so + po, N, calib, prof, shared)
    out['pass'] = all(checks.values())
    text = json.dumps(out, sort_keys=True, indent=1)
    if '--out' in args:
        with open(args[args.index('--out') + 1], 'w') as f:
            f.write(text + '\n')
    print(text)
    sys.exit(0 if out['pass'] else 2)


if __name__ == '__main__':
    main()
