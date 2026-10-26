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


def ref_context(dim, n, port, record, conv):
    """Plan text: Phi = 2*dim neighbours of the origin at n+1 and V at n+2; p at n; port
    samples at slices 0..n; record samples at slices -1..t, even class only."""
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
