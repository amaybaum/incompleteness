"""NP-AVG-1 Stage 0 independent reference closure (C7). Written from the plan text;
imports nothing from s0geom. Cones are explicit cell sets; tips are enumerated
from the definitions; the greatest self-supporting subset is found by brute force
over subsets (small contexts) or by synchronous deletion (larger ones).
Standard library, exact integers."""
from itertools import combinations


def unit(dim, i, s):
    v = [0]*dim
    v[i] = s
    return tuple(v)


def shift(c, v, k):
    return tuple(a + k*b for a, b in zip(c, v))


def cells_within(c, r, parity):
    """All cells at l1 distance <= r from c with distance = parity (mod 2)."""
    dim = len(c)
    out = set()

    def rec(prefix, left):
        if len(prefix) == dim:
            dist = sum(abs(x) for x in prefix)
            if dist % 2 == parity % 2:
                out.add(tuple(a + b for a, b in zip(c, prefix)))
            return
        for x in range(-left, left + 1):
            rec(prefix + [x], left - abs(x))
    if r >= 0:
        rec([], r)
    return out


class RefGeometry:
    """pair = (earlier slice, later slice)."""

    def __init__(self, dim, earlier):
        self.dim, self.E, self.L = dim, earlier, earlier + 1

    def kind(self, q):
        t = q[1]
        if t >= self.L:
            return 'F', t - self.L, self.L, self.E
        return 'B', self.E - t, self.E, self.L

    def cone(self, q):
        c = q[0]
        _, d, near, far = self.kind(q)
        out = {(x, near) for x in cells_within(c, d, d)}
        if d >= 1:
            out |= {(x, far) for x in cells_within(c, d - 1, d - 1)}
        return out

    def tipset(self, q):
        c = q[0]
        _, d, near, far = self.kind(q)
        out = set()
        for i in range(self.dim):
            for s in (1, -1):
                out.add((shift(c, unit(self.dim, i, s), d), near))
                if d >= 1:
                    out.add((shift(c, unit(self.dim, i, s), d - 1), far))
        return out


def self_supporting(S, fixed, geo, eligible, cones):
    pool = set(S) | set(fixed)
    for q in S:
        for u in geo.tipset(q):
            if eligible(u) and not any(u in cones[o] for o in pool if o != q):
                return False
    return True


def greatest(fixed, quants, geo, eligible, brute_limit=8):
    fixed = set(fixed)
    nonfixed = sorted(set(quants) - fixed)
    cones = {q: geo.cone(q) for q in set(nonfixed) | fixed}
    if len(nonfixed) <= brute_limit:
        best = set()
        for k in range(len(nonfixed), 0, -1):
            for S in combinations(nonfixed, k):
                if set(S) <= best:
                    continue
                if self_supporting(S, fixed, geo, eligible, cones):
                    best |= set(S)
        return best, 'brute'
    S = set(nonfixed)
    while True:
        drop = set()
        for q in S:
            for u in geo.tipset(q):
                if eligible(u) and not any(u in cones[o] for o in (S | fixed) if o != q):
                    drop.add(q)
                    break
        if not drop:
            return S, 'synchronous'
        S -= drop


V8_REF = (3, 6, (0, 0, -3))   # v8's (dim, n, port): refused by content


def ref_context(dim, n, port, record, conv, authorized_v8=False):
    """Plan text: Phi = 2*dim neighbours of the origin at n+1 and V at n+2; p at n; port
    samples at slices 0..n; record samples at slices -1..t, even class only. Refuses v8's
    configuration (by content) unless authorized_v8=True, which no code passes."""
    if (dim, n, port) == V8_REF and not authorized_v8:
        raise PermissionError('refused: v8 configuration not authorized')
    o = tuple([0]*dim)
    six = {(shift(o, unit(dim, i, s), 1), n + 1) for i in range(dim) for s in (1, -1)}
    fixed = six | {(o, n + 2), (o, n)}

    def ev(q):
        return (sum(abs(a) for a in q[0]) + q[1]) % 2 == 0
    portq = {(port, s) for s in range(0, n + 1)} if port is not None else set()
    portq = {q for q in portq if ev(q)}
    rec = {(x, s) for x, t in record for s in range(-1, t + 1) if ev((x, s))}
    quants = (portq | rec) - fixed
    if conv == 'A':
        geo = RefGeometry(dim, n + 1)
        return fixed, quants, geo, (lambda u: True)
    geo = RefGeometry(dim, -1)
    frame = set()
    for f in fixed | portq:
        frame |= geo.cone(f)
    return fixed, quants, geo, (lambda u, frame=frame: u not in frame)


def ref_retained(dim, n, port, record, conv, brute_limit=8):
    fixed, quants, geo, elig = ref_context(dim, n, port, record, conv)
    ret, how = greatest(fixed, quants, geo, elig, brute_limit)
    return ret, how


def ref_direction_table(q, others, geo, eligible):
    """Per-direction tip status from the plan text: for each axis e, the near tip at
    distance d and (d >= 1) the far tip at distance d - 1; 'ineligible', 'free' (in no
    cone of any quantity in others) or 'covered'."""
    c = q[0]
    _, d, near, far = geo.kind(q)
    tb = {}
    for i in range(geo.dim):
        for s in (1, -1):
            e = unit(geo.dim, i, s)
            kinds = [('near', (shift(c, e, d), near))]
            if d >= 1:
                kinds.append(('far', (shift(c, e, d - 1), far)))
            for kind, u in kinds:
                if not eligible(u):
                    st = 'ineligible'
                elif any(u in geo.cone(o) for o in others):
                    st = 'covered'
                else:
                    st = 'free'
                tb[(e, kind)] = st
    return tb


def _near_tip(q, e, geo):
    _, d, near, _ = geo.kind(q)
    return (shift(q[0], e, d), near)


def pa_dir_violations(S, geo, eligible, phi_cover):
    """P_A-dir / P_G-dir on a retained non-fixed set S: for every axis direction e, the
    elements of the dominant type at the maximal reach c.e + d must have their e-tip
    shared with another element of S of the same type, or ineligible, or covered by a
    fixed Phi site-time (phi_cover). Returns the violations [(q, e)]."""
    viol = []
    S = sorted(S)
    for i in range(geo.dim):
        for s in (1, -1):
            e = unit(geo.dim, i, s)
            reach = {q: sum(a*b for a, b in zip(q[0], e)) + geo.kind(q)[1] for q in S}
            kind = {q: geo.kind(q)[0] for q in S}
            M = {k: max([reach[q] for q in S if kind[q] == k], default=None) for k in ('F', 'B')}
            top = max(v for v in M.values() if v is not None) if S else None
            for q in S:
                if M[kind[q]] != top or reach[q] != top:
                    continue
                u = _near_tip(q, e, geo)
                ok = (not eligible(u)) or u in phi_cover or any(
                    o != q and kind[o] == kind[q] and _near_tip(o, e, geo) == u for o in S)
                if not ok:
                    viol.append((q, e))
    return viol


def pa_aligned_violations(S, geo, eligible, phi_cover):
    """Aggregate P_A / P_G exactly as stated: every rho-maximal element (rho = max |c_i| + d)
    has each of its aligned near tips shared with another element of S of the same type.
    (No ineligible or Phi exit: under A the aligned tip of a non-fixed quantity is never a
    Phi site-time (PO5), and under G the aligned tip of an S_G element is a seed (P_G).)
    eligible and phi_cover are accepted for a uniform signature and not used."""
    viol = []
    S = sorted(S)
    if not S:
        return viol
    rho = {q: max(abs(x) for x in q[0]) + geo.kind(q)[1] for q in S}
    R = max(rho.values())
    for q in S:
        if rho[q] != R:
            continue
        m = max(abs(x) for x in q[0])
        dirs = [unit(geo.dim, i, s) for i in range(geo.dim) for s in (1, -1)
                if (m == 0) or (q[0][i] == s*m)]
        for e in dirs:
            u = _near_tip(q, e, geo)
            ok = any(o != q and geo.kind(o)[0] == geo.kind(q)[0] and _near_tip(o, e, geo) == u for o in S)
            if not ok:
                viol.append((q, e))
    return viol
