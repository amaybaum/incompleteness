"""NP-AVG-1 Stage 0 production geometry: contexts, cones, tips, L3/L3' closure and
survivor analysis for the second-order rule x_t = x_{t-2} ^ H(XOR of the 2*dim axis
neighbours at t-1). Dimension-generic. Standard library, exact integers, no floats,
no file reads.

Layer 2 copy of stage0/code-r5/s0geom.py (blob 231272ab at f33d8d63). The geometry,
the closure and the Rule fields are unchanged. The one change is the v8 guard:

The v8 configuration is refused by content, not by an object flag (R4-2): any Setup whose
(dim, n, port) equal v8's, whatever its region, slice range or sources, is refused
(PermissionError) by Context, num_records, record_at and record_samples. The comparison is
against a literal, so rebinding the module constant V8_KEY does not disable it. In Layer 2
the refusal is lifted only by a V8Grant instance (exact type, not a subclass, not a truthy
value): authorized_v8=True is refused. A V8Grant is constructed only by
l2auth.issue_grant, after it has verified an owner-designated authorization artifact
against the exact commit, the Layer-2 manifest and the configuration digest; static check
L2-S1 verifies that no other module constructs one. The guard is a module function that
reads the Setup's attributes directly and accepts only the exact Setup type, so a subclass
overriding key() or guard() is refused. The geometry primitives (in_cone, tips, closure)
take no setup and are not guarded; the Layer-2 manifest (certificate item 1) is the gate
for them. The second change is performance only: Context memoizes the G eligibility test per
(pair, frame sources), a pure function of the tip once those are fixed.
"""

NO_V8 = 'refused: enumeration of v8\'s configuration class is not authorized'


def axes(dim):
    out = []
    for i in range(dim):
        for s in (1, -1):
            out.append(tuple(s if j == i else 0 for j in range(dim)))
    return tuple(out)


def vadd(a, b, k=1):
    return tuple(i + k*j for i, j in zip(a, b))


def l1(a, b=None):
    if b is None:
        return sum(abs(i) for i in a)
    return sum(abs(i - j) for i, j in zip(a, b))


def lball(r, dim):
    if r < 0:
        return []
    if dim == 0:
        return [()]
    out = []
    for x in range(-r, r + 1):
        for rest in lball(r - abs(x), dim - 1):
            out.append((x,) + rest)
    return out


class Rule:
    """The frozen rule is Rule(). Every other setting is a mutant."""

    def __init__(self, far=True, offaxis='none', wrong_far=False, far_cone=True,
                 delta=0, swap=False, keep_odd=False, stop_after=None,
                 nopar=False, symblind=False, blind_dir=None, ignore_fixed_dir=None,
                 decide_blind_dir=None, decide_ignore_fixed_dir=None, blind_only_type=None,
                 blind_only_G=False, decide_inelig_free_dir=None):
        self.far, self.offaxis, self.wrong_far, self.far_cone = far, offaxis, wrong_far, far_cone
        self.delta, self.swap, self.keep_odd, self.stop_after = delta, swap, keep_odd, stop_after
        self.nopar, self.symblind = nopar, symblind
        self.blind_dir = blind_dir      # mutant only: tips in this direction are treated as covered
        self.ignore_fixed_dir = ignore_fixed_dir    # mutant: tips in this direction ignore fixed covers
        self.decide_blind_dir = decide_blind_dir    # mutant: decision ignores free tips in this direction
        self.decide_ignore_fixed_dir = decide_ignore_fixed_dir  # mutant: decision ignores fixed covers there
        self.blind_only_type, self.blind_only_G = blind_only_type, blind_only_G   # restrict blind_dir
        # mutant (R4-1): the decision treats an ineligible tip in this direction as free when no
        # other retained non-fixed quantity covers it, ignoring frame and fixed cover; table truthful
        self.decide_inelig_free_dir = decide_inelig_free_dir

    def name(self):
        ref ={'far': True, 'offaxis': 'none', 'wrong_far': False, 'far_cone': True, 'delta': 0,
               'swap': False, 'keep_odd': False, 'stop_after': None, 'nopar': False, 'symblind': False,
               'blind_dir': None, 'ignore_fixed_dir': None, 'decide_blind_dir': None,
               'decide_ignore_fixed_dir': None, 'blind_only_type': None, 'blind_only_G': False,
               'decide_inelig_free_dir': None}
        d = {k: v for k, v in vars(self).items() if ref[k] != v}
        return 'frozen' if not d else ','.join('%s=%s' % kv for kv in sorted(d.items()))


FROZEN = Rule()


class Pair:
    def __init__(self, E):
        self.E, self.L = E, E + 1

    def depth(self, q):
        t = q[1]
        return (t - self.L, 'F') if t >= self.L else (self.E - t, 'B')


def _slices(pair, ty, rule):
    near, far = (pair.L, pair.E) if ty == 'F' else (pair.E, pair.L)
    return (far, near) if rule.swap else (near, far)


def in_cone(u, q, pair, rule=FROZEN):
    (uc, us), (c, t) = u, q
    d, ty = pair.depth(q)
    near, far = _slices(pair, ty, rule)
    r = l1(uc, c)
    if us == near:
        rr, par = d + rule.delta, True
    elif us == far:
        if not rule.far_cone:
            return False
        rr = (d if rule.symblind else d - 1) + rule.delta
        par = not rule.symblind
    else:
        return False
    if rr < 0 or r > rr:
        return False
    return rule.nopar or not par or (r - rr) % 2 == 0


def tip_labels(q, pair, dim, rule=FROZEN):
    """Labelled tips: ((e, 'near'), cell), ((e, 'far'), cell) and, for mutants only,
    ((e, f, 'offaxis'), cell)."""
    c, t = q
    d, ty = pair.depth(q)
    near, far = _slices(pair, ty, rule)
    AX = axes(dim)
    out = [((e, 'near'), (vadd(c, e, d), near)) for e in AX]
    if rule.offaxis == 'all' or (rule.offaxis == 'B' and ty == 'B'):
        if d >= 2:
            for e in AX:
                for f in AX:
                    if f != e and f != tuple(-i for i in e):
                        out.append(((e, f, 'offaxis'), (vadd(vadd(c, e, d - 1), f), near)))
    if d >= 1:
        if rule.wrong_far:
            out += [((e, 'far'), (vadd(c, e, d), far)) for e in AX]
        elif rule.far:
            out += [((e, 'far'), (vadd(c, e, d - 1), far)) for e in AX]
    return out


def tips(q, pair, dim, rule=FROZEN):
    return sorted({u for _, u in tip_labels(q, pair, dim, rule)})


def closure(fixed, quants, pair, dim, rule=FROZEN, eligible=None, final_tables=None):
    """Iterated elimination to the fixed point (worklist on cover counts).
    Returns (retained non-fixed set, elimination log [(q, tip, table)]), where table maps
    every tip label of q to 'free', 'covered' or 'ineligible' as the closure decided it at
    that moment. If final_tables is a dict, it receives the table of every retained
    quantity at the fixed point."""
    fixed = frozenset(fixed)
    allq = sorted(fixed | set(quants))
    nonfixed = [q for q in allq if q not in fixed]
    lab_of = {q: tip_labels(q, pair, dim, rule) for q in nonfixed}
    all_tips = sorted({u for q in nonfixed for _, u in lab_of[q] if eligible is None or eligible(u)})
    covers = {q: {u for u in all_tips if in_cone(u, q, pair, rule)} for q in allq}
    count = {u: 0 for u in all_tips}
    fcount = {u: 0 for u in all_tips}
    for q in allq:
        for u in covers[q]:
            count[u] += 1
            if q in fixed:
                fcount[u] += 1
    retained = set(nonfixed)
    log = []

    def table(q):
        tb = {}
        for lab, u in lab_of[q]:
            if eligible is not None and not eligible(u):
                st = 'ineligible'
            elif rule.blind_dir is not None and lab[0] == rule.blind_dir and \
                    (rule.blind_only_type is None or pair.depth(q)[1] == rule.blind_only_type) and \
                    (not rule.blind_only_G or pair.E == -1):
                st = 'covered'
            elif rule.ignore_fixed_dir is not None and lab[0] == rule.ignore_fixed_dir and \
                    count[u] - fcount[u] - (1 if u in covers[q] else 0) == 0:
                st = 'free'
            elif count[u] - (1 if u in covers[q] else 0) == 0:
                st = 'free'
            else:
                st = 'covered'
            tb[lab] = st
        return tb

    changed = True
    while changed:
        changed = False
        for q in sorted(retained):
            if rule.stop_after is not None and len(log) >= rule.stop_after:
                if final_tables is not None:
                    final_tables.update({r: table(r) for r in retained})
                return retained, log
            tb = table(q)
            free = [u for lab, u in lab_of[q] if tb[lab] == 'free'
                    and not (rule.decide_blind_dir is not None and lab[0] == rule.decide_blind_dir)]
            if rule.decide_ignore_fixed_dir is not None:
                free += [u for lab, u in lab_of[q] if lab[0] == rule.decide_ignore_fixed_dir
                         and tb[lab] == 'covered' and (eligible is None or eligible(u))
                         and count[u] - fcount[u] - (1 if u in covers[q] else 0) == 0]
            if rule.decide_inelig_free_dir is not None:
                free += [u for lab, u in lab_of[q] if lab[0] == rule.decide_inelig_free_dir
                         and tb[lab] == 'ineligible'
                         and not any(in_cone(u, o, pair, rule) for o in retained if o != q)]
            if free:
                retained.discard(q)
                log.append((q, free[0], tb))
                for w in covers[q]:
                    count[w] -= 1
                changed = True
    if final_tables is not None:
        final_tables.update({r: table(r) for r in retained})
    return retained, log


# ---------------------------------------------------------------------------
# Setups and contexts.

class Setup:
    """n: the stage time (Phi neighbours at n+1, V at n+2, p at n); rho: region radius;
    tlast: last item slice; port: site or None; sources: G source sites at slice 0."""

    def __init__(self, dim, n, rho, tlast, port, sources, v8=False):
        self.dim, self.n, self.rho, self.tlast = dim, n, rho, tlast
        self.port, self.sources, self.v8 = port, tuple(sources), v8
        self.origin = tuple(0 for _ in range(dim))
        self.region = sorted(lball(rho, dim))
        self.slices = tuple(range(-1, tlast + 1))
        self.items = [(x, t) for x in self.region for t in self.slices]

    def params(self):
        return (self.dim, self.n, self.rho, self.tlast, self.port, tuple(sorted(self.sources)))

    def key(self):
        """What the closure of a record depends on: (dim, n, port)."""
        return (self.dim, self.n, None if self.port is None else tuple(self.port))

    def guard(self, authorized_v8):
        _guard(self, authorized_v8)

    def phi(self):
        o = self.origin
        six = [(vadd(o, e), self.n + 1) for e in axes(self.dim)]
        return six, (o, self.n + 2), (o, self.n)          # (six, V, p)

    def port_old(self):
        if self.port is None:
            return []
        return [(self.port, s) for s in range(0, self.n + 1)]


class V8Grant:
    """Authorization token for v8's configuration class. Constructed only by
    l2auth.issue_grant (static check L2-S1). The engine checks its exact type, its key and
    the shape of its fields; the binding to the commit, the manifest and the configuration
    is verified by l2auth before construction."""
    __slots__ = ('key', 'commit', 'manifest_sha256', 'config_sha256', 'designation')

    def __init__(self, commit, manifest_sha256, config_sha256, designation):
        self.key = (3, 6, (0, 0, -3))
        self.commit, self.manifest_sha256 = commit, manifest_sha256
        self.config_sha256, self.designation = config_sha256, designation


def _hex(s, n):
    return type(s) is str and len(s) == n and all(ch in '0123456789abcdef' for ch in s)


def _granted(a):
    return (type(a) is V8Grant and getattr(a, 'key', None) == (3, 6, (0, 0, -3))
            and _hex(getattr(a, 'commit', None), 40) and _hex(getattr(a, 'manifest_sha256', None), 64)
            and _hex(getattr(a, 'config_sha256', None), 64))


def _guard(setup, authorized_v8):
    if type(setup) is not Setup:
        raise PermissionError(NO_V8 + ' (only the exact Setup type is accepted)')
    port = setup.port
    key = (setup.dim, setup.n, None if port is None else tuple(port))
    if key == (3, 6, (0, 0, -3)) and not _granted(authorized_v8):
        raise PermissionError(NO_V8)


V8_PARAMS = (3, 6, 4, 23, (0, 0, -3), tuple(sorted(((-7, 0, -1), (-7, 0, 1), (-8, 0, 0)))))
V8_KEY = (3, 6, (0, 0, -3))     # documentation only: guard() compares against the literal
V8 = Setup(3, 6, 4, 23, (0, 0, -3), ((-7, 0, -1), (-7, 0, 1), (-8, 0, 0)), v8=True)


def even(q):
    return (l1(q[0]) + q[1]) % 2 == 0


def record_samples(setup, record, rule=FROZEN, authorized_v8=False):
    _guard(setup, authorized_v8)
    out = set()
    for x, t in record:
        for s in range(-1, t + 1):
            q = (x, s)
            if rule.keep_odd or even(q):
                out.add(q)
    return out


def num_records(setup, k=2, authorized_v8=False):
    _guard(setup, authorized_v8)
    ni, ns, nt = len(setup.items), len(setup.region), len(setup.slices)
    return ni + (ns*(ns - 1)//2)*nt*nt if k == 2 else ni


def record_at(setup, idx, authorized_v8=False):
    """Bijective index -> record: singles first, then two-site pairs by (site pair, t1, t2)."""
    _guard(setup, authorized_v8)
    ni = len(setup.items)
    if idx < ni:
        return (setup.items[idx],)
    idx -= ni
    nt = len(setup.slices)
    ns = len(setup.region)
    sp, rest = divmod(idx, nt*nt)
    i = 0
    while sp >= ns - 1 - i:
        sp -= ns - 1 - i
        i += 1
    j = i + 1 + sp
    t1, t2 = divmod(rest, nt)
    return ((setup.region[i], setup.slices[t1]), (setup.region[j], setup.slices[t2]))


_ELIG_CACHE = {}


class Context:
    def __init__(self, setup, record, conv, rule=FROZEN, authorized_v8=False):
        _guard(setup, authorized_v8)
        self.setup, self.record, self.conv, self.rule = setup, tuple(record), conv, rule
        six, V, p = setup.phi()
        self.phi_cells = set(six) | {V}
        self.fixed = set(six) | {V, p}
        self.port = set(q for q in setup.port_old() if rule.keep_odd or even(q))
        self.rec = record_samples(setup, record, rule, authorized_v8)
        self.in_clear = self.rec & self.fixed
        self.quants = (self.port | self.rec) - self.fixed
        if conv == 'A':
            self.pair = Pair(setup.n + 1)
            self.eligible = None
        elif conv == 'G':
            self.pair = Pair(-1)
            frame_src = sorted(self.fixed | self.port)
            pair = self.pair
            # Layer 2: eligibility is a function of (pair, frame sources, u) only, so its values are
            # memoized per (pair, frame sources); the frame does not depend on the record.
            cache = _ELIG_CACHE.setdefault((pair.E, tuple(frame_src)), {})

            def eligible(u, frame_src=frame_src, pair=pair, cache=cache):
                v = cache.get(u)
                if v is None:
                    v = not any(in_cone(u, f, pair, FROZEN) for f in frame_src)
                    cache[u] = v
                return v
            self.eligible = eligible
        else:
            raise ValueError(conv)

    def run(self):
        self.final_tables = {}
        ret, log = closure(self.fixed, self.quants, self.pair, self.setup.dim, self.rule, self.eligible,
                           self.final_tables)
        self.retained, self.log = ret, log
        return ret


def analyse(ctx):
    """Survivor status and classification attributes for one context."""
    ret = ctx.run()
    s = ctx.setup
    dim, pair, rule = s.dim, ctx.pair, ctx.rule
    if ctx.conv == 'A':
        S = set(ret)
    else:
        S = {q for q in ret if any(ctx.eligible(u) for u in tips(q, pair, dim, rule))}
    six, V, p = s.phi()
    j_cells = {six[i] for i in range(len(six)) if six[i][0] in ((0,)*(dim - 1) + (-1,), (0,)*(dim - 1) + (1,))}
    out = {'survivor': bool(S), 'n_retained': len(ret), 'n_survivor': len(S),
           'retained': sorted(ret), 'survivors': sorted(S), 'in_clear': sorted(ctx.in_clear),
           'n_eliminated': len(ctx.log)}
    if ctx.conv == 'A':
        out['phi_linked'] = any(in_cone(c, q, pair, FROZEN) for q in S for c in ctx.phi_cells)
        out['j_linked'] = any(in_cone(c, q, pair, FROZEN) for q in S for c in j_cells)
    else:
        src = [(x, 0) for x in s.sources]
        out['g_linked'] = any(in_cone(c, q, pair, FROZEN) for q in S for c in src)
        out['truncated'] = sorted(q for q in ret - S if q in ctx.rec)
    public = sorted((ret & (ctx.rec | ctx.port)) | ctx.in_clear | {V, p})
    out['public_retained'] = public
    priv = set(six) - set(ctx.in_clear)
    if ctx.conv == 'A':
        dep = {c for c in priv for q in public if q not in ctx.fixed and in_cone(c, q, pair, FROZEN)}
        out['private_phi'] = sorted(dep | (set(ctx.in_clear) & set(six)))
        out['private_J'] = sorted(c for c in out['private_phi'] if c in j_cells)
    else:
        src = [(x, 0) for x in s.sources]
        out['source_cells'] = sorted({c for c in src for q in public if q not in ctx.fixed and in_cone(c, q, pair, FROZEN)})
    return out
