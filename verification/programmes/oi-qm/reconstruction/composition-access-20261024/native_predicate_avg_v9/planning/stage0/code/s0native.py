"""NP-AVG-1 Stage 0 independent native evaluator and exact checks. Imports nothing
from s0geom or s0ref. Evaluates the rule x_t = x_{t-2} ^ H(XOR of axis neighbours at
t-1) forward and backward from a pair of slices, either per world (scalar) or over
all worlds of a finite window at once (bit-sliced Python integers). Standard
library, exact integers."""
from collections import Counter

HT = tuple(4*((v >> 1) & 1) + 2*(v & 1) + (((v >> 2) & 1) ^ ((v >> 1) & (v & 1) & 1)) for v in range(8))


def nbrs(c):
    for i in range(len(c)):
        for s in (1, -1):
            v = list(c)
            v[i] += s
            yield tuple(v)


def scalar_value(init, q, E, L, cache=None):
    """init: {(cell, slice): triple} on slices E and L. Raises KeyError if q's dependence
    leaves init."""
    if cache is None:
        cache = {}
    if q in cache:
        return cache[q]
    if q in init:
        return init[q]
    c, t = q
    if t > L:
        s = 0
        for m in nbrs(c):
            s ^= scalar_value(init, (m, t - 1), E, L, cache)
        v = scalar_value(init, (c, t - 2), E, L, cache) ^ HT[s]
    elif t < E:
        s = 0
        for m in nbrs(c):
            s ^= scalar_value(init, (m, t + 1), E, L, cache)
        v = scalar_value(init, (c, t + 2), E, L, cache) ^ HT[s]
    else:
        raise KeyError(q)
    cache[q] = v
    return v


class Sliced:
    """All 8^|window| worlds at once: each pair variable's three bits are integer
    planes over 2^(3|window|) lanes."""

    def __init__(self, window, E, L):
        self.window, self.E, self.L = list(window), E, L
        self.nbits = 3*len(self.window)
        self.N = 1 << self.nbits
        self.full = (1 << self.N) - 1
        pats = []
        for j in range(self.nbits):
            block = 1 << j
            unit = ((1 << block) - 1) << block          # lanes whose bit j is 1, in a 2^(j+1) period
            pat, period = 0, block << 1
            reps = self.N // period
            # build by doubling
            pat = unit
            width = period
            while width < self.N:
                pat |= pat << width
                width <<= 1
            pats.append(pat & self.full)
        self.var = {}
        for i, v in enumerate(self.window):
            self.var[v] = (pats[3*i + 2], pats[3*i + 1], pats[3*i])   # (A, B, D) planes
        self.cache = dict(self.var)

    def H(self, a, b, d):
        return b, d, a ^ (b & d)

    def value(self, q):
        if q in self.cache:
            return self.cache[q]
        c, t = q
        if t > self.L:
            sa = sb = sd = 0
            for m in nbrs(c):
                a, b, d = self.value((m, t - 1))
                sa ^= a
                sb ^= b
                sd ^= d
            ha, hb, hd = self.H(sa, sb, sd)
            oa, ob, od = self.value((c, t - 2))
            v = (oa ^ ha, ob ^ hb, od ^ hd)
        elif t < self.E:
            sa = sb = sd = 0
            for m in nbrs(c):
                a, b, d = self.value((m, t + 1))
                sa ^= a
                sb ^= b
                sd ^= d
            ha, hb, hd = self.H(sa, sb, sd)
            oa, ob, od = self.value((c, t + 2))
            v = (oa ^ ha, ob ^ hb, od ^ hd)
        else:
            raise KeyError(q)
        self.cache[q] = v
        return v

    _TABLE = [bytes((b >> i) & 1 for i in range(8)) for b in range(256)]

    def _expand(self, plane):
        packed = plane.to_bytes(max(1, self.N // 8), 'little')
        return int.from_bytes(b''.join(self._TABLE[b] for b in packed)[:self.N], 'little')

    def bytes_of(self, q):
        """Per-world value (0..7) of quantity q, one byte per world."""
        key = ('bytes', q)
        if key not in self.cache:
            a, b, d = self.value(q)
            v = self._expand(d) | (self._expand(b) << 1) | (self._expand(a) << 2)
            self.cache[key] = v.to_bytes(self.N, 'little')
        return self.cache[key]


def exact_independent(sl, elim, ret):
    """True iff the eliminated quantities are jointly uniform and independent of the
    retained ones, over all worlds of the window (exact integer counting)."""
    elim, ret = sorted(elim), sorted(ret)
    if not elim:
        return True
    E = [sl.bytes_of(q) for q in elim]
    R = [sl.bytes_of(q) for q in ret]
    joint = Counter(zip(*E, *R))
    marg = Counter(zip(*R)) if R else Counter({(): sl.N})
    ne = 8**len(elim)
    k = len(E)
    if len(joint) != ne*len(marg):
        return False
    return all(cnt*ne == marg[key[k:]] for key, cnt in joint.items())
