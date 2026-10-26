"""NP-AVG-1 Stage 0 Layer 2: the dry run (section 5b item 1; certificate item 7).

Computes, from the configuration constants alone, the index space, the orbit count (by
Burnside's lemma), the shard plan, the context-size histogram, the masking-equivalent
record count and the cost estimate. It imports neither the engine (s0geom) nor the
reference (s0ref): it constructs no Setup, no Context and no record through the guarded
entry points, and computes no closure (static check L2-S1 verifies the imports). Its
formulas are checked against the engine on the toy profile by l2selftest (L2-PLAN, L2-MASK,
L2-SHTIP, L2-INDEX, L2-SCOPE).

It also holds the closure-free C7 scope predicates of erratum E1 (item E1-F3), written from
the Layer-1 text with this module's own cone and tip code: Q0(R), In(R) and Out(R) under G,
'shared near tip', F_G, I_c and E_G. The shard driver uses them to select C7's set 2 and set 3
without any closure, so that a fault in the production closure cannot remove a record from
the set that is meant to catch it.

Usage: python3 -I -B l2plan.py --profile toy|v8 [--calib calib.json] [--out dryrun.json]
                               [--shared-tips] [--site-pair-counts FILE]
The shard plan is the deterministic subdivision by representative rank (subdivision_cuts), from
the site-pair counts of l2sitepairs: computed here for a non-v8 profile; on v8 read only from
FILE, a count l2sitepairs wrote under its own authorization (none exists: without FILE the v8 plan
is the index-even diagnostic and the per-job estimate is not computed).
--shared-tips enumerates the record space combinatorially (no closure) to count the C7
populations: I_A, I_G (initial-context shared near tip), F_G (in-frame shared near tip) and,
for information, E_G (records, and orbits). On v8's configuration class this enumeration is
not authorized: the option is refused before anything is computed, and the functions that
enumerate records refuse a space whose (dim, n, port) are v8's. The v8 estimate then states
the C7 term as a formula in the uncomputed inputs, each reported as "not computed (requires
authorization)".
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


V8_KEY_LITERAL = (3, 6, (0, 0, -3))
NOT_COMPUTED = 'not computed (requires authorization)'


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
        self.key = (self.dim, self.n, self.port)
        self.site_index = {x: i for i, x in enumerate(self.region)}
        self._frame = None
        self._mclass = None

    # -- the index space (s0geom.record_at's order, written independently) ---------------------
    def index_of(self, record):
        """The record index of a record (singles first, then two-site pairs by (site pair, t1,
        t2)); the inverse of s0geom.record_at, checked on every toy index by L2-INDEX."""
        nt, ns = len(self.slices), len(self.region)
        items = sorted(record)
        if len(items) == 1:
            x, t = items[0]
            return self.site_index[x]*nt + (t - self.slices[0])
        (x, t1), (y, t2) = items
        i, j = self.site_index[x], self.site_index[y]
        if not i < j:
            raise ValueError('not a record of the space: %r' % (record,))
        sp = i*(ns - 1) - i*(i - 1)//2 + (j - i - 1)
        return len(self.region)*nt + sp*nt*nt + (t1 - self.slices[0])*nt + (t2 - self.slices[0])

    def in_space(self, record):
        items = sorted(record)
        if not 1 <= len(items) <= self.k:
            return False
        if any(x not in self.site_index or t not in self.slices for x, t in items):
            return False
        return len({x for x, _ in items}) == len(items)

    # -- closure-free C7 predicates (E1-F3) ------------------------------------------------------
    def q0(self, record):
        """Q0(R): the non-fixed quantities of Ctx(R) (record samples after equivalences E1 and E2,
        and the even port samples)."""
        out = set(self.port_even - self.fixed)
        for x, t in record:
            out |= self.item_set(x, t)
        return out

    def frame(self):
        """The G frame (L1 section 2): the union of the G-convention cones (pair (-1, 0)) of the
        fixed quantities and the even port samples, by this module's own cone code."""
        if self._frame is None:
            fr = set()
            for q in sorted(self.removed):
                fr |= g_cone(q, self.dim)
            self._frame = fr
        return self._frame

    def eligible_G(self, u):
        return u not in self.frame()

    def has_seed_tip(self, q):
        """q has a seed tip: some near or far tip of q in the pair (-1, 0) lies outside the frame."""
        return any(self.eligible_G(u) for u in all_tips(q, -1))

    def in_out(self, record):
        """(In(R), Out(R)) under G: the quantities of Q0(R) without, and with, a seed tip."""
        q0 = self.q0(record)
        out = {q for q in q0 if self.has_seed_tip(q)}
        return q0 - out, out

    def c7_flags(self, record):
        """{'I_A', 'I_G', 'F_G', 'E_G'}: the closure-free C7 predicates of one record."""
        q0 = self.q0(record)
        In, Out = self.in_out(record)
        return {'I_A': shared_near(q0, self.n + 1), 'I_G': shared_near(q0, -1),
                'F_G': shared_near(In, -1), 'E_G': shared_near(Out, -1, self.eligible_G)}

    # -- masking equivalence per record (E1-F6) --------------------------------------------------
    def _m_of(self, x, t):
        st = self.item_set(x, t)
        return max(s for _, s in st) if st else None

    def masking_key(self, record):
        """The canonical form of PO-L2-6: each item (x, t) maps to (x, m), m the largest slice of its
        non-fixed, non-port sample set; items with an empty set map to nothing. Two records have
        equal contexts iff their canonical forms are equal."""
        best = {}
        for x, t in record:
            m = self._m_of(x, t)
            if m is not None:
                best[x] = max(m, best.get(x, m))
        return frozenset(best.items())

    def masking_class_count(self, key):
        """The number of records of the space whose canonical form is key (exact integers)."""
        if self._mclass is None:
            c = {x: Counter(self._m_of(x, t) for t in self.slices) for x in self.region}
            E = {x: c[x].get(None, 0) for x in self.region}
            self._mclass = (c, E, sum(E.values()))
        c, E, Etot = self._mclass
        key = sorted(key)
        if not key:
            return Etot + ((Etot*Etot - sum(v*v for v in E.values()))//2 if self.k == 2 else 0)
        if len(key) == 1:
            (x, m), = key
            return c[x][m] + (c[x][m]*(Etot - E[x]) if self.k == 2 else 0)
        if len(key) == 2 and self.k == 2:
            (x, m1), (y, m2) = key
            return c[x][m1]*c[y][m2]
        return 0

    def masking_equivalent_record(self, record):
        """E1-F6: R is masking-equivalent iff some record R' != R of the space has an equal
        even-class context (equivalences E1 and E2). Relative to the record space; a record
        outside it (a planted design record) is compared with the records of the space."""
        n = self.masking_class_count(self.masking_key(record))
        return n - (1 if self.in_space(record) else 0) >= 1

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
    """The index-even plan: S contiguous ranges of equal record count (r1-r4's plan; now a diagnostic)."""
    return [{'shard': s, 'lo': s*N//S, 'hi': (s + 1)*N//S, 'count': (s + 1)*N//S - s*N//S} for s in range(S)]


def site_pair_counts(sp, counts_file=None):
    """The per-site and per-site-pair representative counts (l2sitepairs' permitted outputs). For a
    non-v8 profile they are computed here by l2sitepairs.count (index metadata only). On v8 they are
    never computed here: they are read from a count file that l2sitepairs wrote under its own
    authorization (owner ruling 2026-10-26: conditionally approved, not dispatched), checked against
    the setup, N and Burnside's orbit count; without one, None."""
    import l2sitepairs as SPC
    _, so, po = sp.orbits_burnside()
    if sp.key == V8_KEY_LITERAL:
        if counts_file is None:
            return None
        with open(counts_file) as f:
            c = json.load(f)
        setup = {'dim': sp.dim, 'rho': sp.rho, 'tlast': sp.tlast, 'port': sp.port}
        if not SPC.validate(c, setup) or c['profile'] != 'v8' or c['authorization'] != 'ok' or \
                c['module_sha256'] != SPC.module_sha256():
            raise ValueError('the v8 site-pair count file is not a valid authorized count of this module')
    else:
        c = SPC.count({'dim': sp.dim, 'rho': sp.rho, 'tlast': sp.tlast, 'port': sp.port})
    if c['records_total'] != sp.n_records() or c['representatives_total'] != so + po or c['nt'] != len(sp.slices):
        raise ValueError('site-pair counts disagree with the index space')
    return c


class RepIndex:
    """Representative ranks over the record index space, from the site-pair counts alone. Within a
    block the representatives are fixed by the block's count: a single site's nt records are all or
    none; a site pair's nt^2 records are all (count nt^2), none (0), those with t1 <= t2 (count
    nt(nt + 1)/2, 'upper') or those with t1 < t2 (nt(nt - 1)/2, 'strict'), at offsets
    (t1 - slice0)*nt + (t2 - slice0) (l2sitepairs' docstring derives the four cases)."""

    def __init__(self, c):
        self.nt = nt = c['nt']
        self.blocks = []            # (lo, hi, kind, reps)
        lo = 0
        for n in c['singles_representatives']:
            self.blocks.append((lo, lo + nt, 'all' if n else 'none', n))
            lo += nt
        for n in c['pairs_representatives']:
            kind = 'all' if n == nt*nt else 'none' if n == 0 else 'upper' if n == nt*(nt + 1)//2 else \
                'strict' if n == nt*(nt - 1)//2 else None
            if kind is None:
                raise ValueError('a site-pair count is not 0, nt(nt - 1)/2, nt(nt + 1)/2 or nt^2')
            self.blocks.append((lo, lo + nt*nt, kind, n))
            lo += nt*nt
        self.N = lo
        self.R = sum(b[3] for b in self.blocks)
        self.prefix = [0]
        for b in self.blocks:
            self.prefix.append(self.prefix[-1] + b[3])
        self.starts = [b[0] for b in self.blocks]

    def _within(self, kind, off):
        """Representatives at offsets < off within a block of the given kind."""
        if kind == 'none':
            return 0
        if kind == 'all':
            return off
        nt = self.nt
        t1, t2 = divmod(off, nt)
        if kind == 'upper':
            return sum(nt - t for t in range(t1)) + max(0, t2 - t1)
        return sum(nt - 1 - t for t in range(t1)) + max(0, t2 - t1 - 1)

    def is_rep(self, idx):
        return self.before(idx + 1) - self.before(idx) == 1

    def before(self, idx):
        """Representatives with record index < idx."""
        if idx >= self.N:
            return self.R
        from bisect import bisect_right
        k = bisect_right(self.starts, idx) - 1
        lo, hi, kind, _ = self.blocks[k]
        return self.prefix[k] + self._within(kind, idx - lo)

    def index_of_rank(self, q):
        """The record index of the representative of rank q (0-based); N for q = R."""
        if q >= self.R:
            return self.N
        from bisect import bisect_right
        k = bisect_right(self.prefix, q) - 1
        while self.blocks[k][3] == 0:
            k += 1
        lo, hi, kind, _ = self.blocks[k]
        r = q - self.prefix[k]
        if kind == 'all':
            return lo + r
        nt, d = self.nt, (0 if kind == 'upper' else 1)
        for t1 in range(nt):
            if r < nt - t1 - d:
                return lo + t1*nt + t1 + d + r
            r -= nt - t1 - d
        raise AssertionError('rank outside its block')


def subdivision_cuts(ri, S, ranks=None):
    """The deterministic subdivision (r5, owner 2026-10-26): shard k starts at the representative of
    rank floor(k R / S), so shard k holds exactly floor((k+1)R/S) - floor(kR/S) representatives,
    whichever site pairs that splits; shard 0 starts at index 0 and the last ends at N. A pure function
    of the frozen inputs (region, slices, group, S). ranks: explicit cut ranks (a planted split)."""
    if ranks is None:
        ranks = [k*ri.R//S for k in range(1, S)]
    return [0] + [ri.index_of_rank(q) for q in ranks] + [ri.N]


def shard_of(index, cuts):
    """The shard holding a record index: the k with cuts[k] <= index < cuts[k + 1] (last such k)."""
    from bisect import bisect_right
    return bisect_right(cuts, index) - 1


def plan_from_cuts(ri, cuts):
    return [{'shard': k, 'lo': cuts[k], 'hi': cuts[k + 1], 'count': cuts[k + 1] - cuts[k],
             'representatives': ri.before(cuts[k + 1]) - ri.before(cuts[k])} for k in range(len(cuts) - 1)]


def plan_accounting(ri, plan):
    """The exact accounting of a shard plan: contiguous, from 0 to N, every record in exactly one
    shard (the counts sum to N), the representatives sum to R, and each shard's stated count of
    representatives is the count from the site-pair counts."""
    ok_cover = bool(plan) and plan[0]['lo'] == 0 and plan[-1]['hi'] == ri.N and all(
        plan[k]['hi'] == plan[k + 1]['lo'] for k in range(len(plan) - 1)) and all(
        sh['lo'] <= sh['hi'] and sh['count'] == sh['hi'] - sh['lo'] for sh in plan)
    reps = [ri.before(sh['hi']) - ri.before(sh['lo']) for sh in plan]
    return {'exact_cover': ok_cover, 'records_sum': sum(sh['count'] for sh in plan) == ri.N,
            'representatives_sum': sum(reps) == ri.R,
            'stated_representatives': all(sh.get('representatives') == r for sh, r in zip(plan, reps))}


def shard_context_weights(sp, ri, plan, weight):
    """For each shard of plan, the sum of weight(m) over its representatives, m being the record's
    number of non-fixed context quantities (port samples plus each item's samples; closure-free, the
    quantity of context_histogram). Uses the site-pair counts (ri) and the per-site item-set sizes
    only: no record, context or closure is formed. The cost model's per-representative closure cost is
    weight = t_A(m) + t_G(m) (estimate); here any weight function of m."""
    base = len(sp.port_even - sp.fixed)
    nt, ns = len(sp.slices), len(sp.region)
    a = [[len(sp.item_set(x, t)) for t in sp.slices] for x in sp.region]
    pair_sites = [(i, j) for i in range(ns) for j in range(i + 1, ns)]
    out = []
    for sh in plan:
        w = 0
        for k, (lo, hi, kind, n) in enumerate(ri.blocks):
            if n == 0 or hi <= sh['lo'] or lo >= sh['hi']:
                continue
            o1, o2 = max(lo, sh['lo']) - lo, min(hi, sh['hi']) - lo
            if k < ns:
                w += sum(weight(base + a[k][t]) for t in range(o1, o2))
                continue
            i, j = pair_sites[k - ns]
            for off in range(o1, o2):
                t1, t2 = divmod(off, nt)
                if kind == 'all' or (kind == 'upper' and t1 <= t2) or (kind == 'strict' and t1 < t2):
                    w += weight(base + a[i][t1] + a[j][t2])
        out.append(w)
    return out


def dry_shard_plan(sp, S, counts_file=None):
    """The dry run's shard plan: the deterministic subdivision where the site-pair counts are
    available; on v8 without an authorized count file the index-even plan is returned as a diagnostic
    only, with reps None, which leaves the per-job estimate, hence the launch, undecided (and
    l2cert refuses a run whose dry-run plan is not the profile's)."""
    c = site_pair_counts(sp, counts_file)
    if c is None:
        return shard_plan(sp.n_records(), S), None, None, {
            'kind': 'index_even (diagnostic only)',
            'reason': 'the v8 site-pair count is not available (conditionally approved, not dispatched)'}
    ri = RepIndex(c)
    plan = plan_from_cuts(ri, subdivision_cuts(ri, S))
    acc = plan_accounting(ri, plan)
    even = shard_plan(sp.n_records(), S)
    reps_even = [ri.before(sh['hi']) - ri.before(sh['lo']) for sh in even]
    return plan, [sh['representatives'] for sh in plan], reps_even, {
        'kind': 'representative_balanced', 'rule': 'shard k starts at the representative of rank floor(kR/S)',
        'accounting': acc, 'site_pair_counts': 'l2sitepairs.count' if 'module_sha256' not in c else c['module_sha256']}


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


def all_tips(q, E):
    """Every near and far tip cell of q for the pair (E, E+1) (plan section 2)."""
    c, t = q
    L = E + 1
    if t >= L:
        d, near, far = t - L, L, E
    else:
        d, near, far = E - t, E, L
    dim = len(c)
    out = set()
    for i in range(dim):
        for sg in (1, -1):
            e = tuple(sg if j == i else 0 for j in range(dim))
            out.add((tuple(a + d*b for a, b in zip(c, e)), near))
            if d >= 1:
                out.add((tuple(a + (d - 1)*b for a, b in zip(c, e)), far))
    return out


def g_cone(q, dim):
    """The G-convention cone (pair (-1, 0)) of q: F type from slice 0 with depth t (slice 0 within
    t, slice -1 within t - 1, with the radius's parity); a slice -1 quantity is B type at depth 0,
    its cone is itself (plan section 2)."""
    c, t = q
    if t <= -1:
        return {(c, -1)}
    out = set()
    for r, s in ((t, 0), (t - 1, -1)):
        for v in lball(r, dim):
            if (norm(v) - r) % 2 == 0:
                out.add((tuple(a + b for a, b in zip(c, v)), s))
    return out


def shared_near(qs, E, eligible=None):
    """True iff two distinct quantities of qs have the same e-near-tip for the same axis direction
    e in the pair (E, E+1); with eligible, only tips u with eligible(u) count (E1-F3)."""
    seen = {}
    for i, q in enumerate(sorted(qs)):
        for k in near_tips(q, E):
            if eligible is not None and not eligible(k[1]):
                continue
            if k in seen and seen[k] != i:
                return True
            seen[k] = i
    return False


def refuse_v8_enumeration(sp):
    """The record-enumerating counts (--shared-tips, the C7 populations) are refused on v8's
    configuration class, whatever its region or slices (keyed on (dim, n, port), as the engine's
    guard). Called first by every function that enumerates records; raises before any work."""
    if sp.key == V8_KEY_LITERAL:
        raise PermissionError('refused: enumerating v8\'s record space (shared tips, F_G) is not authorized')


def _records(sp):
    """Every record of the space, in index order (singles, then two-site pairs)."""
    refuse_v8_enumeration(sp)
    for x in sp.region:
        for t in sp.slices:
            yield ((x, t),)
    if sp.k == 2:
        for i, a in enumerate(sp.region):
            for b in sp.region[i + 1:]:
                for t1 in sp.slices:
                    for t2 in sp.slices:
                        yield ((a, t1), (b, t2))


def shared_tip_records(sp):
    """Records whose initial context (non-fixed quantities) has a cell that is the e-near-tip
    of two distinct quantities, per convention (A: pair (n+1, n+2); G: pair (-1, 0)).
    Enumerates the record space combinatorially; no closure. Refused on v8."""
    refuse_v8_enumeration(sp)
    out = {'A': 0, 'G': 0}
    for r in _records(sp):
        q0 = sp.q0(r)
        out['A'] += shared_near(q0, sp.n + 1)
        out['G'] += shared_near(q0, -1)
    return out


def c7_populations(sp):
    """The closure-free C7 populations (E1-F3): I_A, I_G, F_G and E_G, as records and as orbits
    (records equal to their canonical image). Enumerates the record space; no closure. Refused
    on v8: its sizes there need a separate authorization."""
    refuse_v8_enumeration(sp)
    grp = sp.group()
    out = {k: {'records': 0, 'orbits': 0} for k in ('I_A', 'I_G', 'F_G', 'E_G')}
    for r in _records(sp):
        f = sp.c7_flags(r)
        rs = tuple(sorted(r))
        rep = min(tuple(sorted((g(x), t) for x, t in rs)) for g in grp) == rs
        for k, v in f.items():
            if v:
                out[k]['records'] += 1
                out[k]['orbits'] += rep
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


def _frac(x):
    """An exact rational from an integer or a decimal string ('1.25'); None for a placeholder."""
    if x == CFG.OWNER or x is None:
        return None
    return Fraction(x)


def kappa_from_rule(rule):
    """kappa by the owner's approved method: u_cal x u_model, rounded up to one decimal. None while
    either component is a placeholder. The only source of kappa in Layer 2: launch_decision takes
    kappa from here and never adjusts it."""
    uc, um = _frac(rule.get('u_cal')), _frac(rule.get('u_model'))
    if uc is None or um is None:
        return None
    return Fraction(_ceil(uc*um*10), 10)


NOT_UNDERTAKEN = ('not undertaken for cost: the experiment must be reduced through a new reviewed design or '
                  'declared infeasible under this budget (owner, 2026-10-26); kappa is not lowered to fit')


def launch_decision(total, jobs, kappa, reserve, ceiling, timeouts):
    """The launch rule: launch iff kappa x total + reserve <= ceiling and kappa x each job <= its
    timeout. A job value is one estimate or a list of per-shard estimates; for a list every element is
    compared, so the heaviest shard decides (LAYER2-R4-REVIEW L-b). Returns (launch, decision text,
    the slack). Inputs are exact; kappa comes from kappa_from_rule and is never changed here. Any None
    input gives (None, reason)."""
    missing = [n for n, v in (('kappa', kappa), ('reserve', reserve), ('total', total)) if v is None]
    missing += ['job %s' % k for k, v in jobs.items() if v is None or (isinstance(v, list) and None in v)]
    if missing:
        return None, 'not decided: %s not available' % ', '.join(missing), None
    slack = ceiling - (kappa*total + reserve)
    jobs_ok = all(kappa*x <= timeouts[k] for k, v in jobs.items() for x in (v if isinstance(v, list) else [v]))
    if slack >= 0 and jobs_ok:
        return True, 'launch admitted', slack
    return False, NOT_UNDERTAKEN, slack


def per_shard_jobs(shared, per_shard_fixed, weights):
    """Per-shard job estimates: the representative-borne terms (closures, sampled gates, C7) split in
    proportion to each shard's weight, plus the per-shard survivor allowance (cap orbits, a per-shard
    maximum, not divided). The dry run's weights are the cost model's closure cost of each shard's
    representatives at their context sizes (shard_context_weights with t_A(m) + t_G(m)); a model
    assumption, stated in LAYER2-PLAN.md section 3.6, that the other shared terms follow the closures."""
    W = sum(weights)
    return [Fraction(shared)*w/W + per_shard_fixed for w in weights]


LEDGER_SCHEMA = 'np-avg-1/stage0/layer2/campaign-ledger/1'
LEDGER_KEYS = {'job', 'component', 'attempt', 'status', 'compute_seconds', 'started_at', 'ended_at', 'run'}
LEDGER_STATUS = {'success', 'failure', 'cancelled', 'timed_out'}


def ledger_spent(entries):
    """The campaign's measured compute time per component, from ledger entries (one per job attempt:
    job, component, attempt, status, compute_seconds, started_at, ended_at, run). Every entry counts,
    whatever its status: failed, cancelled and timed-out jobs and every retry (owner, 2026-10-26:
    "Record all measured compute time consistently, including failed jobs and retries"). Returns
    ({component: seconds}, problems)."""
    spent, bad = {}, []
    comps = set(CFG.CONFIG['budget']['ceiling_scope'])
    for i, e in enumerate(entries):
        if type(e) is not dict or set(e) != LEDGER_KEYS or e['component'] not in comps or \
                e['status'] not in LEDGER_STATUS or type(e['compute_seconds']) is not int or e['compute_seconds'] < 0:
            bad.append(i)
            continue
        c = 'retries' if e['attempt'] > 1 else e['component']
        spent[c] = spent.get(c, 0) + e['compute_seconds']
    return spent, bad


def campaign_decision(entries, planned, kappa, reserve, ceiling):
    """The campaign ledger's rule: projected = measured compute time so far (every entry) + the planned
    cost of every component not yet complete; continue iff kappa x projected + reserve <= ceiling.
    planned: {component: seconds or None} for the components still to run (retries: the allowance
    still unused). kappa multiplies the whole campaign, measured and planned, as the owner's formula
    states. Returns (decision True/False/None, text, projected)."""
    spent, bad = ledger_spent(entries)
    if bad:
        return None, 'not decided: malformed ledger entries %s' % bad, None
    if kappa is None or reserve is None or any(v is None for v in planned.values()):
        return None, 'not decided: kappa, the reserve or a planned component is not available', None
    projected = sum(spent.values()) + sum(Fraction(v) for v in planned.values())
    if kappa*projected + reserve <= ceiling:
        return True, 'within the campaign ceiling', projected
    return False, NOT_UNDERTAKEN, projected


def campaign_components(primary_total, n_jobs_primary):
    """The planned campaign components (runner-seconds), each with its status; None where an input is
    an owner placeholder or not yet measured."""
    cam = CFG.CONFIG['budget']['campaign']
    ov = cam['per_job_fixed_overhead_seconds']
    cal, cnt, mut = cam['calibration'], cam['count_pass'], cam['mutant_campaign']
    jobs = cal['jobs']*cal['launches'] + cnt['site_pair_count_jobs'] + cnt['population_count_jobs'] + \
        mut['jobs'] + n_jobs_primary
    comp = {
        'calibration': Fraction(cal['calibrations']*cal['launches']*cal['script_seconds_per_calibration']),
        'count_pass': None if cnt['population_count_seconds'] is None else
        Fraction(cnt['site_pair_count_seconds'] + cnt['population_count_seconds']),
        'primary_run': primary_total,
        'mutant_campaign': Fraction(mut['rule_mutants_seconds'] + mut['machinery_mutants']*mut['selftest_seconds']),
        'retries': _frac(cam['retry_allowance_runner_seconds']),
        'execution_overhead': None if ov is None else Fraction(ov*jobs),
    }
    status = {'calibration': cal['status'], 'count_pass': cnt['status'],
              'primary_run': 'l2plan.estimate (the cost model; unvalidated)', 'mutant_campaign': mut['status'],
              'retries': 'owner placeholder (planned allowance); measured retries replace it in the ledger',
              'execution_overhead': '%d jobs x the per-job fixed overhead: %s' % (jobs, cam['per_job_fixed_overhead_status']
                                                                                 if ov is None else 'measured')}
    return comp, status, jobs


def _wmean(table, allm, nrec):
    """The record-weighted mean over the context-size histogram of a calibrated time (ns)."""
    return Fraction(sum(c*_t(table, m) for m, c in allm), nrec)


def estimate(sp, hist, orbits, N, calib, prof, pops=None, shard_reps=None, ri=None, plan=None):
    """The complete cost estimate in runner-seconds (L2-R6, E1-F3), term by term; LAYER2-PLAN.md
    section 3.6 states each term and its formula. Fractions are exact and rounded up at the end.

    pops: the closure-free C7 populations (c7_populations) or None. On v8 they are not computed
    (their enumeration needs an authorization that does not exist), so the C7 term is reported
    as a formula with its coefficients, its uncomputed inputs are reported as NOT_COMPUTED, and
    no total, per-job estimate or launch decision is computed from an assumed value.
    shard_reps, ri, plan: representatives per shard of the dry run's plan, its RepIndex and the plan
    (dry_shard_plan), or None where the site-pair counts are not available (v8 without an authorized
    count file); the per-job shard input is then not computed, and the mean shard is reported only as a
    lower bound on the heaviest. With them, the shared terms are split by each shard's modelled closure
    cost (shard_context_weights), so the heaviest shard is the heaviest in the model, not in reps.
    The launch decision also needs kappa (owner-set, L2-R7); while kappa is an OWNER
    placeholder, launch_within_budget is None with the reason stated."""
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
    terms, formulas = {}, {}
    # 1. four closures per representative, analysis overhead, normal and -O
    base = sum(c*(2*_t(tA, m) + 2*_t(tG, m)) for m, c in allm)
    terms['closures'] = Fraction(base, NS)*scale*bud['gate_overhead_factor']*2
    formulas['closures'] = ('2 x overhead x sum_m count(m) x (orbits/N) x 2 [t_A(m) + t_G(m)]; overhead = %d is an '
                            'unmeasured judgement (design/overhead/ reports a local measurement)'
                            % bud['gate_overhead_factor'])
    # 2. sampled gates on representatives: C11 (i), C17, C18 at their rates, each costed as one
    #    reference closure per convention at the mean size; C8 on 1 in R orbits: 8 members x 4 closures
    rates = prof['sampling']
    ref_mean = _t(rA, mbar) + _t(rG, mbar)
    samp = sum(Fraction(1, rates[g]) for g in ('C11i', 'C17', 'C18'))*reps*ref_mean
    c8 = Fraction(1, rates['C8_orbits'])*reps*8*(2*_t(tA, mbar) + 2*_t(tG, mbar))
    terms['sampled_gates'] = (samp + c8)/NS*2
    formulas['sampled_gates'] = ('2 x [(1/R_C11i + 1/R_C17 + 1/R_C18) x orbits x (r_A + r_G)(m_mean) + '
                                 '(1/R_C8) x orbits x 8 x 2 (t_A + t_G)(m_mean)]')
    # 3. C7 on its E1-F3 scope, per record and per convention: a direct production L3prime closure
    #    and a full s0ref reference closure for every record in scope, normal and -O.
    c7rec = {'A': {'central': (_wmean(tA, allm, nrec) + _wmean(rA, allm, nrec))*2/NS,
                   'upper_at_m_max': Fraction(_t(tA, mmax) + _t(rA, mmax), NS)*2},
             'G': {'central': (_wmean(tG, allm, nrec) + _wmean(rG, allm, nrec))*2/NS,
                   'upper_at_m_max': Fraction(_t(tG, mmax) + _t(rG, mmax), NS)*2}}
    smp = prof['C7_samples']
    r100, r1000 = smp['H100']['rate'], smp['H1000']['rate']
    inputs = {'N': N, 'H1000_expected_records': str(Fraction(N, r1000)),
              'Surv_A': 'bounded by the survivor cap (term survivor_gates_cap): at most cap x shards x 8 records',
              'Surv_G': 'bounded by the survivor cap (term survivor_gates_cap): at most cap x shards x 8 records'}
    if pops is not None:
        inputs.update({'F_G': pops['F_G']['records'], 'F_G_orbits': pops['F_G']['orbits'],
                       'I_A': pops['I_A']['records'], 'I_G': pops['I_G']['records'],
                       'E_G_information_only': pops['E_G']['records']})
    else:
        inputs.update({'F_G': NOT_COMPUTED, 'F_G_orbits': NOT_COMPUTED, 'I_A': NOT_COMPUTED, 'I_G': NOT_COMPUTED,
                       'E_G_information_only': NOT_COMPUTED})
    sets = {'1_Surv': 'within survivor_gates_cap (every survivor record of a gated orbit; beyond the cap the '
                      'run is INCOMPLETE)',
            '2_set2_A': '0 beyond set 1 (T_A within Surv_A)',
            '2_set2_G': '|F_G| x c7_G (the part of set 2 outside Surv_G is within F_G)',
            '3_I_and_H100': '(|I_A| / %d) x c7_A + (|I_G| / %d) x c7_G (expected sample sizes)' % (r100, r100),
            '4_H1000': '(N / %d) x (c7_A + c7_G) (expected sample size)' % r1000}
    formulas['C7_scope'] = ('|F_G| x c7_G + (|I_A|/%d) x c7_A + (|I_G|/%d) x c7_G + (N/%d) x (c7_A + c7_G), with '
                            'c7_c = 2 x [t_c(m) + r_c(m)] per record (direct production closure and full s0ref '
                            'reference, normal and -O); set 1 is in survivor_gates_cap' % (r100, r100, r1000))
    c7 = {'scope': prof['C7_scope'], 'reference_form': CFG.CONFIG['C7']['reference_form'],
          'per_record_seconds': {c: {k: _ceil(v*1000)/1000 for k, v in d.items()} for c, d in c7rec.items()},
          'per_record_seconds_note': 'central: the record-weighted mean over the context-size histogram; '
                                     'upper_at_m_max: at the largest context size',
          'sets': sets, 'inputs': inputs}
    known_c7 = Fraction(N, r1000)*(c7rec['A']['central'] + c7rec['G']['central'])
    c7['set4_seconds_central'] = _ceil(known_c7)
    if pops is not None:
        v = {'central': pops['F_G']['records']*c7rec['G']['central'] +
             Fraction(pops['I_A']['records'], r100)*c7rec['A']['central'] +
             Fraction(pops['I_G']['records'], r100)*c7rec['G']['central'] + known_c7}
        terms['C7_scope'] = v['central']
        c7['seconds'] = {k: _ceil(x) for k, x in v.items()}
    else:
        terms['C7_scope'] = None
        c7['seconds'] = NOT_COMPUTED
        c7['coefficients_seconds_per_record_central'] = {
            'F_G': _ceil(c7rec['G']['central']*1000)/1000,
            'I_A': _ceil(c7rec['A']['central']/r100*10**6)/10**6,
            'I_G': _ceil(c7rec['G']['central']/r100*10**6)/10**6}
        c7['trivial_upper_bound_not_an_estimate'] = {
            'assumes': '|F_G| = |I_A| = |I_G| = N (the largest values the definitions allow)',
            'seconds_at_m_max': _ceil(N*c7rec['G']['upper_at_m_max'] + Fraction(N, r100)*(
                c7rec['A']['upper_at_m_max'] + c7rec['G']['upper_at_m_max']) + Fraction(N, r1000)*(
                c7rec['A']['upper_at_m_max'] + c7rec['G']['upper_at_m_max']))}
    # 4. survivor gates, bounded by the survivor cap per shard: per survivor orbit, up to 8 members
    #    x (4 closures + 2 conventions x 4 reference gates: C7 (set 1), C11 (i), C17, C18) at m_max
    per_orbit = 8*(2*_t(tA, mmax) + 2*_t(tG, mmax) + 4*(_t(rA, mmax) + _t(rG, mmax)))
    cap = prof['survivor_cap_per_shard']
    per_cap_unit = Fraction(S*per_orbit, NS)*2
    terms['survivor_gates_cap'] = None if cap == CFG.OWNER else cap*per_cap_unit
    formulas['survivor_gates_cap'] = ('2 x cap x shards x 8 x [2 (t_A + t_G) + 4 (r_A + r_G)](m_max), which '
                                      'includes C7 on set 1; cap is owner-set for v8')
    # 5. pre-flight and merge: stated allowances
    terms['preflight'] = Fraction(bud['preflight_seconds'])
    terms['merge'] = Fraction(bud['merge_seconds'])*2
    formulas['preflight'] = 'stated allowance (l2config budget.preflight_seconds)'
    formulas['merge'] = '2 x stated allowance (l2config budget.merge_seconds)'
    # 6. S1a: 4 bound closures; per bound three streamed reference passes (C17, C18 and the case
    #    2 (d) recomputation of L_A and L_G), each costed as a reference closure at the largest
    #    calibrated size scaled linearly to the universe size; and the per-line closures (2 per line)
    mU, lsizes = universe_sizes(sp)
    ks = max(rA)
    s1a = 2*_t(tA, mU) + 2*_t(tG, mU) + 3*2*(rA[ks] + rG[ks])*mU//ks + sum(_t(tA, m) + _t(tG, m) for m in lsizes)
    terms['s1a'] = Fraction(s1a, NS)*2
    formulas['s1a'] = ('2 x [2 (t_A + t_G)(|U|) + 3 streams x 2 rules x (r_A + r_G)(m_cal) x |U| / m_cal + '
                       'sum_lines (t_A + t_G)(m_line)]')
    unknown = sorted(k for k, v in terms.items() if v is None)
    total = None if unknown else sum(terms.values())
    shared = None if terms['C7_scope'] is None else terms['closures'] + terms['sampled_gates'] + terms['C7_scope']
    fixed = None if terms['survivor_gates_cap'] is None else terms['survivor_gates_cap']/S
    weights = None if shard_reps is None else shard_context_weights(sp, ri, plan, lambda m: _t(tA, m) + _t(tG, m))
    if shared is None or fixed is None or weights is None:
        shard_jobs = None
    else:
        shard_jobs = per_shard_jobs(shared, fixed, weights)
    jobs = {'shard': shard_jobs, 's1a': terms['s1a'], 'preflight': terms['preflight'], 'merge': terms['merge']}
    # the known shard-borne terms (closures and sampled gates; no C7 sets 2-3, no survivor term): their
    # mean per shard is a lower bound on the heaviest shard whatever the plan
    known_shared = terms['closures'] + terms['sampled_gates']
    shard_lb = {'mean_shard_known_terms_seconds': _ceil(known_shared/S),
                'note': 'closures and sampled gates only (C7 sets 2-3 and the survivor term excluded), split '
                        'evenly over the shards: a lower bound on the heaviest shard under any plan'}
    if weights is not None:
        R, W = sum(shard_reps), sum(weights)
        shard_lb['heaviest_shard_known_terms_seconds'] = _ceil(known_shared*max(weights)/W)
        shard_lb['heaviest_over_mean_representatives'] = str(Fraction(max(shard_reps)*len(shard_reps), R)) if R else None
        shard_lb['heaviest_over_mean_model_cost'] = '%.3f' % (max(weights)*len(weights)/W) if W else None
    tmo = {k: bud['timeout_minutes'][k]*60 for k in jobs}
    kappa = kappa_from_rule(bud['kappa_rule'])
    reserve = _frac(bud['reserve_runner_seconds'])
    ceiling = bud['runner_hours']*3600
    reasons = []
    if kappa is None:
        reasons.append('kappa is not fixed: u_cal or u_model is an OWNER placeholder (method approved, no value)')
    if reserve is None:
        reasons.append('the reserve is an OWNER placeholder; no default exists')
    if terms['C7_scope'] is None:
        reasons.append('the C7 term needs |F_G|, |I_A| and |I_G|: %s' % NOT_COMPUTED)
    if terms['survivor_gates_cap'] is None:
        reasons.append('the survivor cap is an OWNER placeholder; no default exists')
    if shard_reps is None:
        reasons.append('the heaviest shard needs the representatives per shard: on v8 they come only from the '
                       'site-pair count (l2sitepairs), conditionally approved and not dispatched')
    # the campaign ledger (owner, 2026-10-26): the primary run is one of six components
    n_primary_jobs = S + 4      # shards (normal and -O in one job), pre-flight, S1a, merge, certificate
    comp, comp_status, n_jobs = campaign_components(total, n_primary_jobs)
    missing_comp = sorted(k for k, v in comp.items() if v is None)
    campaign_total = None if missing_comp else sum(comp.values())
    for k in missing_comp:
        if k != 'primary_run':
            reasons.append('campaign component %s: %s' % (k, comp_status[k]))
    launch, decision, slack = launch_decision(campaign_total, jobs, kappa, reserve, ceiling, tmo)
    known = sum(v for v in terms.values() if v is not None)
    why_none = {'C7_scope': NOT_COMPUTED, 'survivor_gates_cap': 'not computed (owner placeholder: the survivor cap)'}
    return {'terms_runner_seconds': {k: (why_none[k] if v is None else _ceil(v)) for k, v in terms.items()},
            'formulas': formulas,
            'total_runner_seconds': 'not computed (needs the C7 inputs and the survivor cap)' if total is None
            else _ceil(total),
            'known_terms_runner_seconds': _ceil(known),
            'known_terms_plus_C7_set4_runner_seconds': _ceil(known + (known_c7 if terms['C7_scope'] is None else 0)),
            'per_job_seconds': {k: ('not computed (needs the C7 inputs, the survivor cap and, for shards, the '
                                    'representatives per shard)' if v is None else
                                    {'heaviest': _ceil(max(v)), 'per_shard': [_ceil(x) for x in v]}
                                    if isinstance(v, list) else _ceil(v)) for k, v in jobs.items()},
            'shard_job_bounds': shard_lb,
            'job_timeouts_seconds': tmo, 'budget_runner_seconds': ceiling, 'ceiling_status': bud['ceiling_status'],
            'reserve_runner_seconds': 'OWNER placeholder' if reserve is None else _ceil(reserve),
            'kappa': 'not fixed (method approved: u_cal x u_model)' if kappa is None else str(kappa),
            'kappa_rule': bud['kappa_rule'], 'C7': c7, 'mean_context_size_bucket_input': mbar, 'max_context_size': mmax,
            'universe_quantities': mU, 'survivor_cap_per_shard': cap,
            'survivor_gates_seconds_per_cap_unit': _ceil(per_cap_unit),
            'overhead_factor': {'value': bud['gate_overhead_factor'], 'status': bud['gate_overhead_factor_status']},
            'campaign_runner_seconds': {k: ('not computed' if v is None else _ceil(v)) for k, v in comp.items()},
            'campaign_status': comp_status, 'campaign_jobs': n_jobs,
            'campaign_total_runner_seconds': 'not computed (%s)' % ', '.join(missing_comp) if campaign_total is None
            else _ceil(campaign_total),
            'campaign_known_runner_seconds': _ceil(sum(v for v in comp.values() if v is not None)),
            'launch_rule': 'launch iff kappa x (calibration + count pass + primary run + mutant campaign + retries + '
                           'execution overhead) + reserve <= ceiling (24 runner-hours per complete campaign, aggregate '
                           'compute time) and kappa x each job, the heaviest shard included, <= its timeout; otherwise '
                           'not undertaken for cost (a new reviewed design, or infeasible under this budget); kappa is '
                           'never lowered and timeouts are never raised to fit',
            'launch_within_budget': launch, 'launch_decision': decision,
            'slack_runner_seconds': None if slack is None else _ceil(slack) if slack >= 0 else -_ceil(-slack),
            'launch_not_decided_because': reasons}


def main():
    args = sys.argv[1:]
    pname = args[args.index('--profile') + 1]
    prof = CFG.profile(pname)
    sp = Space(prof)
    if '--shared-tips' in args and sp.key == V8_KEY_LITERAL:
        # refused before anything is computed: v8's shared-tip and F_G counts need an authorization
        print(json.dumps({'label': 'VOID', 'refused': '--shared-tips on v8', 'reason': NOT_COMPUTED},
                         sort_keys=True))
        sys.exit(2)
    N = sp.n_records()
    gorder, so, po = sp.orbits_burnside()
    S = prof['shards']
    cfile = args[args.index('--site-pair-counts') + 1] if '--site-pair-counts' in args else None
    try:
        plan, reps_s, reps_even, plan_info = dry_shard_plan(sp, S, cfile)
    except (ValueError, KeyError, TypeError, OSError) as e:
        print(json.dumps({'label': 'VOID', 'refused': '--site-pair-counts', 'reason': str(e)}, sort_keys=True))
        sys.exit(2)
    singles, pairs = context_histogram(sp)
    out = {'schema': 'np-avg-1/stage0/layer2/dryrun/2', 'profile': pname, 'records': N,
           'group_order': gorder, 'orbits': so + po, 'single_orbits': so, 'pair_orbits': po,
           'shards': plan, 'shard_plan': plan_info,
           'representatives_per_shard': reps_s if reps_s is not None else NOT_COMPUTED,
           'index_even_plan_representatives_per_shard_diagnostic': reps_even if reps_even is not None
           else NOT_COMPUTED, 'context_quantities_singles': {str(k): v for k, v in sorted(singles.items())},
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
    pops = None
    if reps_s is not None:
        checks.update({'shard_plan_' + k: v for k, v in plan_info['accounting'].items()})
    if '--shared-tips' in args:
        out['shared_tip_records'] = shared_tip_records(sp)
        pops = out['C7_populations'] = c7_populations(sp)
    else:
        out['C7_populations'] = NOT_COMPUTED if prof['requires_authorization'] else 'not requested (--shared-tips)'
    if '--calib' in args:
        with open(args[args.index('--calib') + 1], 'rb') as f:
            raw = f.read()
        calib = json.loads(raw)
        out['calib_sha256'] = hashlib.sha256(raw).hexdigest()
        ri = RepIndex(site_pair_counts(sp, cfile)) if reps_s is not None else None
        out['cost'] = estimate(sp, (singles, pairs), so + po, N, calib, prof, pops, reps_s, ri, plan)
    out['pass'] = all(checks.values())
    text = json.dumps(out, sort_keys=True, indent=1)
    if '--out' in args:
        with open(args[args.index('--out') + 1], 'w') as f:
            f.write(text + '\n')
    print(text)
    sys.exit(0 if out['pass'] else 2)


if __name__ == '__main__':
    main()
