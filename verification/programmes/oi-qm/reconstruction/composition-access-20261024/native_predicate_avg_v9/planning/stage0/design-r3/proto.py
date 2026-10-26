"""Stage 0 design prototype (toys only; not v8's class). Dimension-generic L3 / L3'
closure for the second-order rule x_t = x_{t-2} ^ H(XOR of the 2*dim neighbours at t-1),
with the frozen rule options and the mutants. Standard library, exact integers."""

H = tuple(4*((v >> 1) & 1) + 2*(v & 1) + (((v >> 2) & 1) ^ ((v >> 1) & (v & 1) & 1)) for v in range(8))
assert sorted(H) == list(range(8))


def axes(dim):
    out = []
    for i in range(dim):
        for s in (1, -1):
            out.append(tuple(s if j == i else 0 for j in range(dim)))
    return out


def add(a, b, k=1):
    return tuple(i+k*j for i, j in zip(a, b))


def dist(a, b):
    return sum(abs(i-j) for i, j in zip(a, b))


def ball(r, dim):
    if dim == 0:
        return [()]
    out = []
    for x in range(-r, r+1):
        for rest in ball(r-abs(x), dim-1):
            out.append((x,)+rest)
    return out


class Geometry:
    """Pair (E, L) = (L-1, L). F: t >= L (depth t-L); B: t <= E (depth E-t).
    eligible(u) -> bool restricts which tips may eliminate (G convention: seeds only).
    Options: far (L3' far tips), offaxis in {'none','all','B'}, wrong_far, symmetric,
    nopar (cone parity test dropped), swap (near/far slices swapped)."""

    def __init__(self, dim, L, far=True, offaxis='none', wrong_far=False,
                 symmetric=False, nopar=False, swap=False, eligible=None):
        self.dim, self.L, self.E = dim, L, L-1
        self.AX = axes(dim)
        self.far, self.offaxis, self.wrong_far = far, offaxis, wrong_far
        self.symmetric, self.nopar, self.swap = symmetric, nopar, swap
        self.eligible = eligible or (lambda u: True)

    def depth(self, q):
        c, t = q
        return (t-self.L, 'F') if t >= self.L else (self.E-t, 'B')

    def slices(self, ty):
        near, far = (self.L, self.E) if ty == 'F' else (self.E, self.L)
        return (far, near) if self.swap else (near, far)

    def in_cone(self, u, q):
        (uc, us), (c, t) = u, q
        d, ty = self.depth(q)
        near, far = self.slices(ty)
        r = dist(uc, c)
        if us == near:
            rr = d
        elif us == far:
            rr = d if self.symmetric else d-1
        else:
            return False
        if r > rr or rr < 0:
            return False
        return self.nopar or (r-rr) % 2 == 0

    def tips(self, q):
        c, t = q
        d, ty = self.depth(q)
        near, far = self.slices(ty)
        out = {(add(c, e, d), near) for e in self.AX}
        if self.offaxis == 'all' or (self.offaxis == 'B' and ty == 'B'):
            if d >= 2:
                for e in self.AX:
                    for f in self.AX:
                        if f != e and f != tuple(-i for i in e):
                            out.add((add(add(c, e, d-1), f), near))
        if d >= 1:
            if self.wrong_far:
                out |= {(add(c, e, d), far) for e in self.AX}
            elif self.far:
                out |= {(add(c, e, d-1), far) for e in self.AX}
        return out

    def closure(self, fixed, quants):
        fixed = set(fixed)
        ret = fixed | set(quants)
        changed = True
        while changed:
            changed = False
            for q in sorted(ret - fixed):
                others = ret - {q}
                for u in self.tips(q):
                    if self.eligible(u) and not any(self.in_cone(u, o) for o in others):
                        ret.discard(q)
                        changed = True
                        break
        return ret - fixed


def even(q):
    return (sum(map(abs, q[0]))+q[1]) % 2 == 0


def evolve_value(init, q, cache, dim, E, L):
    """Native value of site-time q from the pair slices E, L given in init (dict),
    forward for t > L, backward for t < E. cache: dict."""
    if q in cache:
        return cache[q]
    c, t = q
    if (c, t) in init:
        return init[(c, t)]
    AX = axes(dim)
    if t > L:
        s = 0
        for e in AX:
            s ^= evolve_value(init, (add(c, e), t-1), cache, dim, E, L)
        v = evolve_value(init, (c, t-2), cache, dim, E, L) ^ H[s]
    elif t < E:
        s = 0
        for e in AX:
            s ^= evolve_value(init, (add(c, e), t+1), cache, dim, E, L)
        v = evolve_value(init, (c, t+2), cache, dim, E, L) ^ H[s]
    else:
        raise KeyError(q)
    cache[q] = v
    return v
