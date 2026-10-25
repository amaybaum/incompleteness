"""Reviewer engine, part 1: regenerate the native_route_v13 q10 table.

Written for the rev910b review. Imports no author or earlier-review code.
Field values are stored as three bit-planes (A, B, D), one Python int each,
one lane per assignment; the earlier review used interleaved 3-bit lanes and
memoised recursion, the author a strip evaluator. Here the upper cluster is
evaluated by an explicit backward dependency closure followed by a forward
sweep in time, the lower first front by a (y, z) dynamic programme.
Inherited (not re-derived): source positions/payloads of the upper cluster
and of the four first-front selector sources, and the two large-time period
reductions (upper strip 12*840^20, written proof reviewed in v13/review).
The lower-front period is re-measured exactly here (minimal cycle lengths).
"""
from itertools import product

T = 185
P = 12 * 840 ** 185
S = P + T
R = S + 68
L = R + 9
NB = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def need(ok, why):
    if not ok:
        raise SystemExit('CONTROL FAILED: ' + why)


def Hp(a, b, d):
    # H(A,B,D) = (B, D, A xor B*D) on bit-planes
    return b, d, a ^ (b & d)


def Hpow(v, k):
    for _ in range(k % 12):
        v = Hp(*v)
    return v


def xor3(u, v):
    return u[0] ^ v[0], u[1] ^ v[1], u[2] ^ v[2]


Z3 = (0, 0, 0)


def h_exponent_check():
    for q in range(8):
        v = (q >> 2 & 1, q >> 1 & 1, q & 1)
        w = v
        for _ in range(12):
            w = Hp(*w)
        need(w == v, 'H^12 = id')
    need(any(Hpow((q >> 2 & 1, q >> 1 & 1, q & 1), 6) != (q >> 2 & 1, q >> 1 & 1, q & 1) for q in range(8)), 'H^6 != id')
    need(any(Hpow((q >> 2 & 1, q >> 1 & 1, q & 1), 4) != (q >> 2 & 1, q >> 1 & 1, q & 1) for q in range(8)), 'H^4 != id')


def planes(values):
    """values: list of 3-bit codes 4A+2B+D, lane i -> planes."""
    a = b = d = 0
    for i, c in enumerate(values):
        if c & 4: a |= 1 << i
        if c & 2: b |= 1 << i
        if c & 1: d |= 1 << i
    return a, b, d


def code_at(v, i):
    return ((v[0] >> i) & 1) << 2 | ((v[1] >> i) & 1) << 1 | ((v[2] >> i) & 1)


def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])


def native_closure(sources, requests):
    """Exact native values at the requested (t, p) nodes by backward closure
    + forward sweep.  U_{t+1}(v) = U_{t-1}(v) xor H(xor_{w~v} U_t(w)),
    U_0 = sources, U_{-1} = 0.  Nodes outside every source cone are zero."""
    spos = list(sources)

    def live(t, p):
        return t >= 0 and min(manhattan(p, q) for q in spos) <= t

    need_at = {}
    frontier = {}
    for t, p in requests:
        if live(t, p):
            frontier.setdefault(t, set()).add(p)
    tmax = max(frontier)
    for t in range(tmax, 0, -1):
        cur = frontier.get(t, set())
        need_at[t] = cur
        for p in cur:
            if live(t - 2, p):
                frontier.setdefault(t - 2, set()).add(p)
            for d in NB:
                q = (p[0] + d[0], p[1] + d[1], p[2] + d[2])
                if live(t - 1, q):
                    frontier.setdefault(t - 1, set()).add(q)
    need_at[0] = frontier.get(0, set())
    val = {}
    for p in need_at[0]:
        val[0, p] = sources.get(p, Z3)
    for t in range(1, tmax + 1):
        for p in need_at.get(t, ()):
            acc = Z3
            for d in NB:
                q = (p[0] + d[0], p[1] + d[1], p[2] + d[2])
                w = val.get((t - 1, q))
                if w is not None:
                    acc = xor3(acc, w)
            out = Hp(*acc)
            w = val.get((t - 2, p))
            if w is not None:
                out = xor3(out, w)
            val[t, p] = out
    nodes = len(val)
    return {(t, p): val.get((t, p), Z3) for t, p in requests}, nodes


UPPER_LANES = [(u, a, b, n) for u in (0, 1) for a in (0, 1) for b in (0, 1) for n in range(8)]


def upper_sources():
    # Native B upper cluster in the reduced axial frame (x, y, n); N at n=-20.
    def pl(f):
        return planes([f(u, a, b, n) for u, a, b, n in UPPER_LANES])
    return {
        (0, 0, 0): pl(lambda u, a, b, n: 4 * u + 1),                       # Q (u,0,1)
        (0, 0, -14): pl(lambda u, a, b, n: 4 * u + u),                     # C (u,0,u)
        (0, 0, -16): pl(lambda u, a, b, n: 4 * u + 2 * (1 ^ u) + 1),       # G (u,1^u,1)
        (0, 0, -18): pl(lambda u, a, b, n: 4 * (u ^ b) + 2 * a + (u ^ a)),  # J
        (1, 0, -17): pl(lambda u, a, b, n: 5 * (a ^ b)),                   # K+
        (-1, 0, -17): pl(lambda u, a, b, n: 7 * (a ^ b)),                  # K-
        (0, 0, -20): pl(lambda u, a, b, n: n),                             # N
    }


LOWER_LANES = [(x, e) for x in (0, 1) for e in range(8)]


def lower_front(gap_w=76, gap_e=78, ymax=176):
    """F(y,z) on the first front x=0, t=y+z, from initial data on y+z=0:
    O=(0,0,0) payload (0,x,0), W=(0,-gw,gw) payload 111, E=(0,-ge,ge) payload E.
    F(y,z)=H(F(y-1,z) xor F(y,z-1)); returns dict over z in {gw,gw+1,ge}."""
    O = planes([2 * x for x, e in LOWER_LANES])
    Wv = planes([7 for _ in LOWER_LANES])
    Ev = planes([e for x, e in LOWER_LANES])
    init = {(0, 0): O, (-gap_w, gap_w): Wv, (-gap_e, gap_e): Ev}
    F = {}
    zmax = gap_e
    for s_ in range(0, ymax + zmax + 1):  # s_ = y + z
        for z in range(0, zmax + 1):
            y = s_ - z
            if y < -gap_e or y > ymax:
                continue
            if s_ == 0:
                F[y, z] = init.get((y, z), Z3)
            else:
                F[y, z] = Hp(*xor3(F.get((y - 1, z), Z3), F.get((y, z - 1), Z3)))
    return F, O, Wv, Ev


def lower_period_check():
    """Exact minimal period of the joint (F(j,76),F(j,77),F(j,78)) sequence for j>=1
    per lane, forcing F(j,75) computed exactly from the O-only front."""
    F, O, Wv, Ev = lower_front(ymax=1)
    # O-only first-front value at (j,75): binom(j+75,75) mod 2 * H^(j+75)(0,x,0)
    # proof: single-source front values stay in {0, H^t v}; H(0)=0.
    def forcing(j):
        return Hpow(O, j + 75) if (j & 75) == 0 else Z3
    # verify the forcing formula on a direct O-only DP up to j=600
    Fo = {}
    for s_ in range(0, 600 + 76):
        for z in range(0, 76):
            y = s_ - z
            if y < 0 or y > 600:
                continue
            Fo[y, z] = O if s_ == 0 else Hp(*xor3(Fo.get((y - 1, z), Z3), Fo.get((y, z - 1), Z3)))
    for j in range(0, 601):
        need(Fo[j, 75] == forcing(j), 'O-only Lucas forcing formula')
    start = (F[0, 76], F[0, 77], F[0, 78])
    periods = []
    for lane in range(16):
        st = tuple(tuple((v >> lane) & 1 for v in lev) for lev in start)
        def block(state):
            f0, f1, f2 = state
            for j in range(1, 385):
                fj = forcing(j)
                fl = tuple((v >> lane) & 1 for v in fj)
                f0 = Hp(*xor3(f0, fl))
                f1 = Hp(*xor3(f1, f0))
                f2 = Hp(*xor3(f2, f1))
            return f0, f1, f2
        s0 = st
        cyc = 0
        cur = s0
        while True:
            cur = block(cur)
            cyc += 1
            need(cyc <= 512, 'block map cycle bound')
            if cur == s0:
                break
        periods.append(384 * cyc)
    from math import lcm
    per = 1
    for q in periods:
        per = lcm(per, q)
    need(P % per == 0, 'P divisible by exact lower period')
    need((384 * 840 ** 3) % per == 0, 'exact lower period divides 384*840^3')
    return per


def ball(c, r):
    return [(c[0] + i, c[1] + j, c[2] + k) for i in range(-r, r + 1) for j in range(-r, r + 1)
            for k in range(-r, r + 1) if abs(i) + abs(j) + abs(k) <= r]


ROWS = [(x, u, my, mr, a, b, e, n) for x, u, my, mr, a, b in product((0, 1), repeat=6)
        for e in range(8) for n in range(8)]


def lucas3(ds):
    acc = 0
    for q in ds:
        if acc & q:
            return False
        acc |= q
    return True


def q10_table():
    h_exponent_check()
    need(P % (12 * 840 ** 20) == 0, 'upper strip period divides P')
    # Upper requests in the reduced frame.
    centre = (0, 0, 10)
    balls = {-2: ball(centre, 10), -1: ball(centre, 11)}
    req = []
    for dt, cells in balls.items():
        for p in cells:
            req.append((253 + dt, (p[0], p[1], 253 - p[2])))
    up, nodes = native_closure(upper_sources(), req)
    lf, O, Wv, Ev = lower_front()
    lower_period = lower_period_check()
    nrows = len(ROWS)
    # expansion masks
    umask = [0] * 64
    lmask = [0] * 16
    uidx = {r: i for i, r in enumerate(UPPER_LANES)}
    for i, (x, u, my, mr, a, b, e, n) in enumerate(ROWS):
        umask[uidx[u, a, b, n]] |= 1 << i
        lmask[8 * x + e] |= 1 << i

    def expand(v, masks):
        out = []
        for pl in v:
            acc = 0
            j = 0
            while pl:
                if pl & 1:
                    acc |= masks[j]
                pl >>= 1
                j += 1
            out.append(acc)
        return tuple(out)

    def rowplane(f):
        m = 0
        for i, r in enumerate(ROWS):
            if f(*r):
                m |= 1 << i
        return m
    XM = rowplane(lambda x, u, my, mr, a, b, e, n: x)
    MYM = rowplane(lambda x, u, my, mr, a, b, e, n: my)
    MRM = rowplane(lambda x, u, my, mr, a, b, e, n: mr)
    # first-front selector sources (local coords; absolute = (p0, S+p1, 68+p2)); all pure-B
    signals = [((0, -S, -68), (0, XM, 0)), ((0, S, -68), (0, MYM ^ MRM, 0)),
               ((T, P, -68), (0, MYM, 0)), ((-T, P, -68), (0, MRM, 0))]
    lower_srcs_local = [(0, -S, -68), (0, -76 - S, 8), (0, -78 - S, 10)]  # O, W, E in local coords
    entries = {(0, -9, 8): (176, 76), (0, -10, 9): (175, 77), (0, -11, 10): (174, 78)}
    upos = list(upper_sources())
    init = {}
    sep_checked = 0
    for dt, cells in balls.items():
        t = R + dt
        for p in cells:
            rp = (p[0], p[1], 253 - p[2])
            ureach = min(manhattan(rp, q) for q in upos) <= 253 + dt
            lreach = any(manhattan(p, q) <= t for q, _ in signals) or any(manhattan(p, q) <= t for q in lower_srcs_local)
            need(not (ureach and lreach), 'upper/lower clusters overlap before R')
            sep_checked += 1
            v = expand(up[253 + dt, rp], umask)
            for q, bits in signals:
                ds = tuple(abs(pi - qi) for pi, qi in zip(p, q))
                if sum(ds) <= t:
                    need(sum(ds) == t, 'selector only at first front')
                    if lucas3(ds):
                        v = xor3(v, Hpow(bits, t))
            if dt == -1 and p in entries:
                j, z = entries[p]
                need(v == (Hpow((0, XM, 0), t) if lucas3((0, S + p[1], 68 + p[2])) else Z3), 'entry: only O background')
                v = expand(lf[j, z], lmask)
            else:
                # W/E reach no other cell of the two balls
                for q in lower_srcs_local[1:]:
                    need(manhattan(p, q) > t, 'W/E reach outside entries')
            init[dt, p] = v
    # E entry exactly one cell
    e_local = (0, -78 - S, 10)
    hits = [(dt, p) for dt, cells in balls.items() for p in cells if manhattan(p, e_local) <= R + dt]
    need(hits == [(-1, (0, -11, 10))], 'E enters only (0,-11,10) at R-1')
    old = {p: init[-2, p] for p in balls[-2]}
    now = {p: init[-1, p] for p in balls[-1]}
    slices = {}
    for tick in range(11):
        nxt = {}
        for p in ball(centre, 10 - tick):
            acc = Z3
            for d in NB:
                acc = xor3(acc, now[p[0] + d[0], p[1] + d[1], p[2] + d[2]])
            nxt[p] = xor3(old[p], Hp(*acc))
        slices[R + tick] = nxt
        old, now = now, nxt
    q10 = now[centre]
    table = ''.join(format(code_at(q10, i), 'x') for i in range(nrows))
    q9 = slices[R + 9][(0, 0, 9)]
    q9tab = ''.join(format(code_at(q9, i), 'x') for i in range(nrows))
    q10_ticks = {tick: ''.join(format(code_at(slices[R + tick][centre], i), 'x') for i in range(nrows)) for tick in range(11)}
    q10_table.ticks = q10_ticks
    return table, q9tab, {'upper_nodes': nodes, 'upper_requests': len(req), 'separation_cells': sep_checked,
                          'lower_exact_period': lower_period}


if __name__ == '__main__':
    import hashlib, time
    t0 = time.time()
    tab, q9tab, info = q10_table()
    print(hashlib.sha256(tab.encode()).hexdigest(), info, round(time.time() - t0, 1))
