"""LOC-1 preflight, leg S: independent count of the linear decompositions of F_3^4.

Shares no code with f34_enum.py.  Vectors are integer codes 0..80 (base-3 digits), projective points are
normalised by their LAST nonzero digit, and independence is decided by span closure (the set of all
linear combinations), not by elimination or determinants.  It counts ordered independent 4-tuples of
projective points by depth-first extension and divides by 4!; it also counts unordered sets directly.
Run:  python3 -I f34_count_indep.py
"""
q, n = 3, 4
SIZE = q ** n


def digits(code):
    return [(code // q ** k) % q for k in range(n)]


def code_of(ds):
    return sum(d * q ** k for k, d in enumerate(ds))


def add(u, v):
    return code_of([(a + b) % q for a, b in zip(digits(u), digits(v))])


def scale(c, u):
    return code_of([(c * a) % q for a in digits(u)])


def last_nonzero_one(u):
    ds = digits(u)
    nz = [d for d in ds if d]
    return bool(nz) and nz[-1] == 1


POINTS = [u for u in range(1, SIZE) if last_nonzero_one(u)]


_CACHE = {}


def extend_span(span, v):
    """span is a frozenset of codes closed under linear combination; return span + <v> (memoised)."""
    key = (span, v)
    if key not in _CACHE:
        new = set(span)
        for s in span:
            for c in range(1, q):
                new.add(add(s, scale(c, v)))
        _CACHE[key] = frozenset(new)
    return _CACHE[key]


def count_ordered():
    def rec(span, depth):
        if depth == n:
            return 1
        return sum(rec(extend_span(span, v), depth + 1) for v in POINTS if v not in span)
    return rec(frozenset([0]), 0)


def count_unordered():
    def rec(span, depth, start):
        if depth == n:
            return 1
        tot = 0
        for k in range(start, len(POINTS)):
            v = POINTS[k]
            if v not in span:
                tot += rec(extend_span(span, v), depth + 1, k + 1)
        return tot
    return rec(frozenset([0]), 0, 0)


if __name__ == "__main__":
    print("projective points (last nonzero digit 1):", len(POINTS))
    o = count_ordered()
    u = count_unordered()
    print("ordered independent 4-tuples of points:", o)
    print("ordered / 4! =", o // 24, "(remainder %d)" % (o % 24))
    print("unordered independent 4-sets of points:", u)
    ok = len(POINTS) == 40 and o % 24 == 0 and o // 24 == u == 63180
    print("INDEPENDENT COUNT:", "AGREES (63180)" if ok else "DISAGREES")
