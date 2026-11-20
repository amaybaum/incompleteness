#!/usr/bin/env python3
"""UNIV-2 exact checks: the controlled turn in the published rounded rule Q (q = 2**16).

All lattice arithmetic is exact integer arithmetic (numpy int32/int64, or Python integers and
fractions). No floating-point value decides any statement.

  RZ   y_{t+1}(i) = floor((sum_{j~i} y_t(j) + 1)/3) - y_{t-1}(i)   (integers; U1 Lemma 2.1 embeds
       it into Q at background c = 2**15 while |y| < 2**15)
  Q    the same recurrence mod 2**16 on the representatives 0..q-1 (re-run for any candidate)
  LIN  x_{t+1}(i) = 3^{-1} sum_{j~i} x_t(j) - x_{t-1}(i) mod 2**16 (control N4)
  LG   lattice billiard: four velocity channels, free streaming, fixed 90-degree mirrors (control P1)
  BBM  the U1 billiard-ball block rule (control P2)

Run from the record directory:
  python3 -I checks/univ2_checks.py              controls, A1, A2 on {-1,0,1} (a few seconds)
  python3 -I checks/univ2_checks.py --search     also A2 on {-2..2}, the families F1-F3 and the post hoc
                                                 checks X1-X3 (about 11 minutes)
Exit status 0 iff every check holds (a check is a control or a stated computed fact; a search
family's verdict is printed and is a check only of its own completeness and cross-check).
"""
import itertools
import math
import sys
from collections import Counter
from fractions import Fraction

import numpy as np

q = 2 ** 16
c = 2 ** 15
INV3 = pow(3, -1, q)
P = [-1, -1, 1, 1]          # W2 background pattern along a line (U1 E2), period 4
T1, TEXT, SPACING = 120, 60, 12
RESULTS = []


def check(name, ok, info=""):
    RESULTS.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}{('  ' + info) if info else ''}", flush=True)


def G(s):
    return np.floor_divide(s + 1, 3)


def nbsum(x, axes):
    return sum(np.roll(x, sh, ax) for ax in axes for sh in (1, -1))


# ======================================================================= rules (step / back)
class RZRule:
    """Two-slice state (prev, cur), integer values; 'zero' is 0."""
    name = "RZ"

    def __init__(self, batch=False):
        self.axes = (1, 2, 3) if batch else (0, 1, 2)

    def step(self, s):
        yp, y = s
        return y, G(nbsum(y, self.axes)) - yp

    def back(self, s):
        yp, y = s
        return G(nbsum(yp, self.axes)) - y, yp

    @staticmethod
    def nonzero(s):
        return (s[0] != 0) | (s[1] != 0)

    @staticmethod
    def maxabs(s):
        return int(max(np.abs(s[0]).max(), np.abs(s[1]).max()))


class LinRule(RZRule):
    """Exact linear member L_{2^16, 3^-1} written on y = x - c (mod q, centred)."""
    name = "LIN"

    def step(self, s):
        yp, y = s
        return y, (INV3 * nbsum(y, self.axes) - yp) % q

    def back(self, s):
        yp, y = s
        return (INV3 * nbsum(yp, self.axes) - y) % q, yp

    @staticmethod
    def nonzero(s):
        return (s[0] % q != 0) | (s[1] % q != 0)

    @staticmethod
    def maxabs(s):
        return 0


class PathOracle(RZRule):
    """Oracle for the classifier (review B1): the 1D line rule run along given site paths, every
    off-path site held at 0. Each path is a list of 3D sites; consecutive entries are path
    neighbours, the ends have one path neighbour. Not Q: R8 (the re-run in Q) must reject it."""
    name = "ORACLE"

    def __init__(self, J, paths):
        super().__init__()
        self.paths = [np.array([J.idx(p) for p in path]).T for path in paths]

    def _apply(self, prev, cur):
        out = np.zeros_like(cur)
        for ix in self.paths:
            c_ = cur[tuple(ix)]
            nb = np.zeros_like(c_)
            nb[1:] += c_[:-1]
            nb[:-1] += c_[1:]
            out[tuple(ix)] = G(nb) - prev[tuple(ix)]
        return out

    def step(self, s):
        return s[1], self._apply(s[0], s[1])

    def back(self, s):
        return self._apply(s[1], s[0]), s[0]


# ================================================================ geometry of a W2 junction
def parity(p):
    return (p[0] + p[1] + p[2]) % 2


class Junction:
    """A W2 line A along e1 ending at the origin, a line B (or none), a gadget region R."""

    def __init__(self, kind, phiB, LA=40, LB=80):
        self.kind = kind
        self.A = [(x, 0, 0) for x in range(-LA, 1)]
        if kind == "J1":
            self.B = [(0, y, 0) for y in range(1, LB + 1)]
            self.core = [(0, 0, 0)]
        elif kind == "J2":
            self.B = [(1, y, 0) for y in range(1, LB + 1)]
            self.core = [(0, 0, 0), (1, 1, 0)]
        elif kind == "J3":
            self.B = [(0, y, 1) for y in range(0, LB + 1)]
            self.core = [(0, 0, 0), (0, 0, 1)]
        elif kind == "DEAD":
            self.B = []
            self.core = [(0, 0, 0)]
        else:
            raise ValueError(kind)
        self.phiB = phiB
        self.LB = LB
        line = set(self.A) | set(self.B)
        zs = [p[2] for p in self.core]
        self.lo = np.array([-LA - 3, -4, min(zs) - 3])
        self.hi = np.array([4, LB + 4, max(zs) + 3])
        self.shape = tuple(int(v) for v in self.hi - self.lo + 1)

        def ball(r):
            out = set()
            for cp in self.core:
                for d in itertools.product(range(-r, r + 1), repeat=3):
                    out.add((cp[0] + d[0], cp[1] + d[1], cp[2] + d[2]))
            return out - line
        self.R = sorted(ball(1))
        self.Rplus = sorted(ball(2))
        self.mask_line = self._mask(line)
        self.mask_R = self._mask(self.R)
        self.mask_Rplus = self._mask(self.Rplus)
        self.farB = [p for p in self.B if 8 <= p[1] <= LB - 8]
        self.mask_farB = self._mask(self.farB)
        self.mask_A = self._mask(self.A)
        # B's ring offset: ring index k = y + off has the parity of the 3D site
        self.off = (parity(self.B[0]) - self.B[0][1]) % 2 if self.B else 0

    def idx(self, p):
        return tuple(int(v) for v in np.array(p) - self.lo)

    def _mask(self, pts):
        m = np.zeros(self.shape, bool)
        for p in pts:
            m[self.idx(p)] = True
        return m

    def put(self, s, p, v):
        """Write component value v at site p (current slice on even sites, previous on odd)."""
        (s[1] if parity(p) == 0 else s[0])[self.idx(p)] = v

    def get(self, s, p):
        return int((s[1] if parity(p) == 0 else s[0])[self.idx(p)])

    def background(self):
        s = (np.zeros(self.shape, np.int64), np.zeros(self.shape, np.int64))
        for p in self.A:
            self.put(s, p, P[(p[0] + 1) % 4])
        for p in self.B:
            self.put(s, p, P[(p[1] + self.phiB) % 4])
        return s

    def with_gadget(self, s, gadget):
        s = (s[0].copy(), s[1].copy())
        for p, v in gadget:
            self.put(s, p, v)
        return s

    def with_signal(self, s, xs):
        """Flip the background pair at x-positions xs on A (the W2 defect; K0 checks its motion)."""
        s = (s[0].copy(), s[1].copy())
        for x in xs:
            self.put(s, (x, 0, 0), -self.get(s, (x, 0, 0)))
        return s


SIG1 = (-11, -10)                       # first signal: window [-15, -8], 8 sites from the junction
SIG2 = (-11 - SPACING, -10 - SPACING)   # second signal, 12 sites behind (R5)
SIG_FAR = (-63, -62)                    # N3 (A02): window [-67, -60], cannot reach the junction by T1


def run(rule, s, T, on_tick=None):
    for t in range(1, T + 1):
        s = rule.step(s)
        if on_tick is not None and not on_tick(t, s):
            return s, t
    return s, None


# ================================================================ straight-line (1D) tools
def ring_step(s):
    yp, y = s
    return y, G(np.roll(y, 1) + np.roll(y, -1)) - yp


def ring_background(phi, off, L=160):
    """Two-slice ring with the W2 background P[(k - off + phi) mod 4] at ring index k."""
    yp = np.zeros(L, np.int64)
    y = np.zeros(L, np.int64)
    for k in range(L):
        v = P[(k - off + phi) % 4]
        (y if k % 2 == 0 else yp)[k] = v
    return yp, y


def glider(s, direction, pmax=48, smax=24):
    """(p, s) with state(t+p) = shift_s state(t), sign(s) = direction, values in {-1,0,1}; else None."""
    s0 = s
    cur = s
    for p in range(1, pmax + 1):
        cur = ring_step(cur)
        if max(np.abs(cur[0]).max(), np.abs(cur[1]).max()) > 1:
            return None
        for sh in range(1, smax + 1):
            d = direction * sh
            if np.array_equal(np.roll(s0[0], d), cur[0]) and np.array_equal(np.roll(s0[1], d), cur[1]):
                return p, d
    return None


def transplant(J, S, T):
    """B's far part of S at time T on a straight ring carrying B's background evolved to time T."""
    bg = ring_background(J.phiB, J.off)
    for _ in range(T):
        bg = ring_step(bg)
    yp, y = bg[0].copy(), bg[1].copy()
    for p in J.farB:
        k = p[1] + J.off
        yp[k] = S[0][J.idx(p)]
        y[k] = S[1][J.idx(p)]
    diff = [k for k in range(len(y)) if yp[k] != bg[0][k] or y[k] != bg[1][k]]
    return (yp, y), diff


# ================================================================ the canonical classifier
def classify_rz(J, gadget, rule=None, sig=SIG1, verbose=False):
    """Requirements R1-R8 (PREREG section 2, A01), in order; returns (passed, first_fail, info).

    Shared decision logic for every W2 geometry; the controls N1-N4 and the search use it."""
    rule = rule or RZRule()
    info = {}
    N0 = J.with_gadget(J.background(), gadget)
    if isinstance(rule, LinRule):
        N0 = (N0[0] % q, N0[1] % q)
    allowed_R = J.mask_line | J.mask_R
    allowed_Rp = J.mask_line | J.mask_Rplus
    # R1 quiescence
    Ns = [N0]
    s = N0
    for t in range(1, 9):
        s = rule.step(s)
        Ns.append(s)
        if (rule.nonzero(s) & ~allowed_R).any():
            return False, "R1", {"radiates_without_input_at": t}
    if not (np.array_equal(Ns[4][0], N0[0]) and np.array_equal(Ns[4][1], N0[1])):
        return False, "R1", {"N(4) != N(0)": True}
    N = lambda t: Ns[t % 4]
    # one-signal orbit
    S0 = J.with_signal(N0, sig)
    if isinstance(rule, LinRule):
        S0 = (S0[0] % q, S0[1] % q)
    mx = [rule.maxabs(S0)]

    def tick(t, st):
        mx.append(rule.maxabs(st))
        return not (rule.nonzero(st) & ~allowed_Rp).any() and mx[-1] < 2 ** 15
    S, bad = run(rule, S0, T1, tick)
    if bad is not None:
        return False, "R3", {"radiation_or_window_at": bad}
    # R2 transfer and R3 restoration at T1
    outside = ~J.mask_farB
    restored = np.array_equal(S[0][outside], N(T1)[0][outside]) and np.array_equal(S[1][outside], N(T1)[1][outside])
    if not J.B:
        return False, "R2", {"no line B": True}
    ring, diff = transplant(J, S, T1)
    if not diff:
        return False, "R2", {"no output on B": True, "restored_outside_farB": restored}
    if max(diff) - min(diff) + 1 > 12:
        return False, "R2", {"output window": max(diff) - min(diff) + 1}
    g = glider(ring, +1)
    if g is None:
        return False, "R2", {"far-B pattern is not an outgoing glider": diff}
    info["R2"] = {"glider (p, s)": g, "window": (min(diff) - J.off, max(diff) - J.off)}
    if not restored:
        return False, "R3", info
    # R4 continuation
    S4, bad = run(rule, S, TEXT, tick)
    if bad is not None:
        return False, "R4", {"radiation_at": T1 + bad}
    outside4 = np.array_equal(S4[0][outside], N(T1 + TEXT)[0][outside]) and \
        np.array_equal(S4[1][outside], N(T1 + TEXT)[1][outside])
    ring4, diff4 = transplant(J, S4, T1 + TEXT)
    if not (outside4 and diff4 and glider(ring4, +1) is not None and min(diff4) > min(diff)):
        return False, "R4", {}
    # R5 repeatability (two signals, 12 sites apart; reference after two transits is N)
    S20 = J.with_signal(J.with_signal(N0, sig), SIG2)
    T2 = T1 + 3 * SPACING
    S2, bad = run(rule, S20, T2, tick)
    if bad is not None:
        return False, "R5", {"radiation_at": bad}
    ok5 = np.array_equal(S2[0][outside], N(T2)[0][outside]) and np.array_equal(S2[1][outside], N(T2)[1][outside])
    ring2, diff2 = transplant(J, S2, T2)
    g2 = glider(ring2, +1) if diff2 else None
    if not (ok5 and g2 is not None and g2 == g):
        return False, "R5", {"restored": ok5, "glider": g2}
    info["R5"] = {"glider (p, s)": g2}
    # R7 reversibility: the backward rule from S(T1) returns S(0)
    B = S
    for _ in range(T1):
        B = rule.back(B)
    if not (np.array_equal(B[0], S0[0]) and np.array_equal(B[1], S0[1])):
        return False, "R7", {}
    # R8 embedding: max |y| < 2^15 (recorded by tick), and the Q orbit equals c + RZ orbit
    info["max|y|"] = max(mx)
    xs = ((S0[0] + c) % q, (S0[1] + c) % q)
    for _ in range(T1):
        xs = (xs[1], ((nbsum(xs[1], (0, 1, 2)) + 1) // 3 - xs[0]) % q)
    if not (np.array_equal(xs[0], (S[0] + c) % q) and np.array_equal(xs[1], (S[1] + c) % q)):
        return False, "R8", info
    return True, None, info


# ================================================================ lattice billiard (P1) and BBM (P2)
def classify_generic(step, back, nonzero, N0, S0, S20, allowed_R, allowed_Rp, farB_out_ok, T1g, T2g,
                     eq=lambda a, b: np.array_equal(a, b)):
    """The same decision logic (R1, R3 radiation, R2, R3, R4 omitted, R5, R7) for rules whose
    post-transit reference is N(t) and whose outgoing glider test is supplied by farB_out_ok."""
    Ns = [N0]
    s = N0
    for t in range(1, 9):
        s = step(s)
        Ns.append(s)
        if (nonzero(s) & ~allowed_R).any():
            return False, "R1"
    if not eq(Ns[4], N0):
        return False, "R1"
    N = lambda t: Ns[t % 4]
    s = S0
    for t in range(1, T1g + 1):
        s = step(s)
        if (nonzero(s) & ~allowed_Rp).any():
            return False, "R3"
    ok_out, outside = farB_out_ok(s, N(T1g))
    if not ok_out:
        return False, "R2"
    if not np.array_equal(s[..., outside], N(T1g)[..., outside]):
        return False, "R3"
    s2 = S20
    for t in range(1, T2g + 1):
        s2 = step(s2)
        if (nonzero(s2) & ~allowed_Rp).any():
            return False, "R5"
    ok2, _ = farB_out_ok(s2, N(T2g), two=True)
    if not (ok2 and np.array_equal(s2[..., outside], N(T2g)[..., outside])):
        return False, "R5"
    b = s
    for _ in range(T1g):
        b = back(b)
    if not np.array_equal(b, S0):
        return False, "R7"
    return True, None


def lg_controls():
    """P1: four channels (E, N, W, S) and a static mirror channel M on a 2D box; mirror sites
    exchange E<->N and W<->S (an involution), then every particle streams one site."""
    X, Y = 40, 60
    ox, oy = 30, 4                       # junction (mirror) at array index (30, 4)

    def collide(s):
        s = s.copy()
        m = s[4] == 1
        e, n, w, so = s[0].copy(), s[1].copy(), s[2].copy(), s[3].copy()
        s[0][m], s[1][m], s[2][m], s[3][m] = n[m], e[m], so[m], w[m]
        return s

    def stream(s, sign=1):
        s = s.copy()
        s[0] = np.roll(s[0], sign, 0)
        s[1] = np.roll(s[1], sign, 1)
        s[2] = np.roll(s[2], -sign, 0)
        s[3] = np.roll(s[3], -sign, 1)
        return s
    step = lambda s: stream(collide(s))
    back = lambda s: collide(stream(s, -1))
    nonzero = lambda s: s[:4].any(0)
    N0 = np.zeros((5, X, Y), np.int64)
    N0[4, ox, oy] = 1
    lineA = np.zeros((X, Y), bool)
    lineA[: ox + 1, oy] = True
    lineB = np.zeros((X, Y), bool)
    lineB[ox, oy + 1:] = True
    R = np.zeros((X, Y), bool)
    R[ox, oy] = True
    farB = np.zeros((X, Y), bool)
    farB[ox, oy + 8: Y - 8] = True
    S0 = N0.copy()
    S0[0, ox - 8, oy] = 1                # particle moving E along A, 8 sites from the mirror
    S20 = S0.copy()
    S20[0, ox - 8 - 12, oy] = 1

    def out_ok(s, n, two=False):
        d = s[:4] != n[:4]
        k = int(d.sum())
        good = k == (2 if two else 1) and not d[[0, 2, 3]].any() and (d[1] & farB).sum() == k
        return good, ~farB
    pos = classify_generic(step, back, nonzero, N0, S0, S20, lineA | lineB | R, lineA | lineB | R, out_ok, 30, 42)
    # the same lattice billiard with the mirror removed: the particle continues straight (no turn)
    N0b = N0.copy()
    N0b[4] = 0
    S0b, S20b = S0.copy(), S20.copy()
    neg = classify_generic(step, back, nonzero, N0b, S0b, S20b, lineA | lineB | R, lineA | lineB | R, out_ok, 30, 42)
    return pos, neg


def bbm_step(g, t):
    o = t % 2
    g = np.roll(g, (-o, -o), (0, 1))
    a, b, cc, d = g[0::2, 0::2], g[0::2, 1::2], g[1::2, 0::2], g[1::2, 1::2]
    cnt = a + b + cc + d
    na, nb, nc, nd = a.copy(), b.copy(), cc.copy(), d.copy()
    one = cnt == 1
    na[one], nb[one], nc[one], nd[one] = d[one], cc[one], b[one], a[one]
    d1 = (cnt == 2) & (a == 1) & (d == 1)
    d2 = (cnt == 2) & (b == 1) & (cc == 1)
    na[d1], nd[d1], nb[d1], nc[d1] = 0, 0, 1, 1
    nb[d2], nc[d2], na[d2], nd[d2] = 0, 0, 1, 1
    h = np.zeros_like(g)
    h[0::2, 0::2], h[0::2, 1::2], h[1::2, 0::2], h[1::2, 1::2] = na, nb, nc, nd
    return np.roll(h, (o, o), (0, 1))


def bbm_control():
    """P2: U1's collision turn. Signal A from (4,4) moving (+,+); the supplied constant particle
    from (13,13) moving (-,-) is the 'gadget'. The rule is time-dependent (partition parity), so
    the state carries the tick count."""
    n = 32

    def step(s):
        g, t = s[:-1].reshape(n, n), int(s[-1])
        return np.concatenate([bbm_step(g, t).ravel(), [t + 1]])

    def back(s):
        raise NotImplementedError
    nonzero = lambda s: s[:-1].reshape(n, n) != 0
    N0 = np.zeros(n * n + 1, np.int64)
    N0[13 * n + 13] = 1
    S0 = N0.copy()
    S0[4 * n + 4] = 1
    allowed = np.ones((n, n), bool)
    eq = lambda a, b: np.array_equal(a[:-1], b[:-1])
    out_ok = lambda s, nn, two=False: (False, np.ones((n, n), bool))
    return classify_generic(step, back, nonzero, N0, S0, S0, allowed, allowed, out_ok, 12, 12, eq=eq)


# ================================================================ A1, A2 (analytic branch)
def check_A1():
    """Components: the signal component (current on parity-t sites) evolves independently of the
    other component, in Q itself; a random perturbation of the other component leaves it unchanged."""
    rng = np.random.RandomState(3)
    n = 6
    par = np.indices((n, n, n)).sum(0) % 2
    ok = True
    for _ in range(5):
        xp = rng.randint(0, q, (n, n, n)).astype(np.int64)
        x = rng.randint(0, q, (n, n, n)).astype(np.int64)
        xp2, x2 = xp.copy(), x.copy()
        # perturb the other component at t=0: current on odd sites, previous on even sites
        x2[par == 1] = rng.randint(0, q, int((par == 1).sum()))
        xp2[par == 0] = rng.randint(0, q, int((par == 0).sum()))
        for t in range(1, 13):
            xp, x = x, ((nbsum(x, (0, 1, 2)) + 1) // 3 - xp) % q
            xp2, x2 = x2, ((nbsum(x2, (0, 1, 2)) + 1) // 3 - xp2) % q
            m = par == (t % 2)              # signal component: current slice on parity-t sites
            ok &= np.array_equal(x[m], x2[m]) and np.array_equal(xp[~m], xp2[~m])
    check("A1 components evolve independently in Q (5 random states, 12 ticks)", ok)


DIRS = [(d, sg) for d in range(3) for sg in (1, -1)]


def a2_system(alph, eps, Gf):
    A = list(alph)
    na = len(A)
    ix = {a: i for i, a in enumerate(A)}
    nu = 2 * na + 6 * na * na
    rows = set()
    for v in A:
        for ns in itertools.product(A, repeat=6):
            vp = Gf(sum(ns)) - v
            if vp not in ix:
                continue
            r = [0] * nu
            r[ix[vp]] += 6
            r[na + ix[v]] -= 6 * eps
            for k, (d, sg) in enumerate(DIRS):
                nb = ns[k]
                kneg = DIRS.index((d, -sg))
                r[2 * na + k * na * na + ix[vp] * na + ix[nb]] += 6
                r[2 * na + kneg * na * na + ix[nb] * na + ix[v]] -= 6 * eps
                r[na + ix[nb]] += 1
                r[ix[nb]] -= eps
            if any(r):
                rows.add(tuple(r))
    return nu, sorted(rows)


def nullspace_exact(nu, rows):
    """Nullspace over Q: elimination mod a prime, rational reconstruction, exact verification.
    Returns (basis, verified). Nullity over Q <= nullity mod p, so a verified lift of the full
    mod-p nullspace is the exact nullspace."""
    p = 2147483629
    M = np.array(rows, dtype=np.int64) % p
    piv = []
    r0 = 0
    for col in range(nu):
        nz = np.nonzero(M[r0:, col])[0]
        if len(nz) == 0:
            continue
        pr = r0 + nz[0]
        M[[r0, pr]] = M[[pr, r0]]
        M[r0] = (M[r0] * pow(int(M[r0, col]), -1, p)) % p
        f = M[:, col].copy()
        f[r0] = 0
        sel = np.nonzero(f)[0]
        for a in range(0, len(sel), 2048):
            ss = sel[a:a + 2048]
            M[ss] = (M[ss] - (f[ss, None] * M[r0][None, :]) % p) % p
        piv.append(col)
        r0 += 1
        if r0 == M.shape[0]:
            break
    basis = []
    for fj in [j for j in range(nu) if j not in piv]:
        v = [0] * nu
        v[fj] = 1
        for i, pc in enumerate(piv):
            v[pc] = int((-M[i, fj]) % p)
        basis.append(v)

    def rr(a):
        a %= p
        r_0, r_1, s0, s1 = p, a, 0, 1
        Bd = math.isqrt(p // 2)
        while r_1 > Bd:
            qq = r_0 // r_1
            r_0, r_1, s0, s1 = r_1, r_0 - qq * r_1, s1, s0 - qq * s1
        if s1 == 0 or abs(s1) > Bd:
            return None
        return Fraction(r_1, s1)
    Qb = [[rr(x) for x in b] for b in basis]
    ok = all(x is not None for b in Qb for x in b)
    if ok:
        R = np.array(rows, dtype=np.int64)
        for b in Qb:
            den = 1
            for x in b:
                den = den * x.denominator // math.gcd(den, x.denominator)
            iv = [int(x * den) for x in b]
            assert max(abs(v) for v in iv) * int(np.abs(R).max()) * len(iv) < 2 ** 62
            if np.any(R.dot(np.array(iv, dtype=np.int64)) != 0):
                ok = False
    return Qb, ok


def a2_features(w, A, nu):
    na = len(A)
    ix = {a: i for i, a in enumerate(A)}
    par = np.indices(w.shape).sum(0) % 2
    f = [0] * nu
    fresh = par == 0
    for a in A:
        f[ix[a]] = int(((w == a) & fresh).sum())
        f[na + ix[a]] = int(((w == a) & ~fresh).sum())
    for k, (d, sg) in enumerate(DIRS):
        nb = np.roll(w, -sg, d)
        for a in A:
            for b in A:
                f[2 * na + k * na * na + ix[a] * na + ix[b]] = int(((w == a) & (nb == b) & fresh).sum())
    return f


def rank_q(rows):
    rows = [[Fraction(x) for x in r] for r in rows]
    piv, R = [], []
    for row in rows:
        for pc, pr in zip(piv, R):
            if row[pc]:
                f = row[pc]
                row = [a - f * b for a, b in zip(row, pr)]
        nz = [j for j, x in enumerate(row) if x]
        if not nz:
            continue
        pc = nz[0]
        row = [x / row[pc] for x in row]
        for i in range(len(R)):
            if R[i][pc]:
                f = R[i][pc]
                R[i] = [a - f * b for a, b in zip(R[i], row)]
        piv.append(pc)
        R.append(row)
    return len(piv)


def a2_nontrivial(alph, basis, nu, nconf=300):
    """Dimension of the span of the conserved densities as functionals on configurations of a
    6^3 torus, modulo constants (evaluation rank on random configurations minus the zero one)."""
    if not basis:
        return 0
    rng = np.random.RandomState(1)
    A = list(alph)
    f0 = a2_features(np.zeros((6, 6, 6), np.int64), A, nu)
    Bm = np.array(basis, dtype=object)
    vals = []
    for _ in range(nconf):
        f = a2_features(rng.choice(A, (6, 6, 6)), A, nu)
        vals.append(list(np.array([a - b for a, b in zip(f, f0)], dtype=object).dot(Bm.T)))
    return rank_q(vals)


def check_A2(full):
    rz = lambda s: (s + 1) // 3
    lin = lambda s: s
    out = {}
    for alph in ((-1, 0, 1), (-2, -1, 0, 1, 2)) if full else ((-1, 0, 1),):
        for eps in (1, -1):
            nu, rows = a2_system(alph, eps, rz)
            basis, ok = nullspace_exact(nu, rows)
            nt = a2_nontrivial(alph, basis, nu)
            out[(len(alph), eps)] = (len(basis), ok, nt)
            check(f"A2 RZ star-local densities, alphabet {alph}, E(t+1) = {eps:+d} E(t): solution space "
                  f"{len(basis)} (exact lift {ok}); nontrivial as functionals: {nt}", ok and nt == 0)
    # countercontrol: the same template and test on the linear update v' = s - v (alpha = 1) finds
    # its quadratic energy, so the triviality test can return a positive
    nu, rows = a2_system((-1, 0, 1), 1, lin)
    basis, ok = nullspace_exact(nu, rows)
    nt = a2_nontrivial((-1, 0, 1), basis, nu)
    check("A2c countercontrol: the template finds a nontrivial conserved density for the linear update", ok and nt >= 1,
          f"solution space {len(basis)}, nontrivial {nt}")


# ================================================================ controls K0, N1-N4, P1, P2
def check_K0():
    # straight line: A extended through the origin to x = +40 (no junction); the signal moves +x
    J = Junction("DEAD", 0)
    J.A = [(x, 0, 0) for x in range(-40, 41)]
    J.hi = np.array([44, 4, 3])
    J.lo = np.array([-43, -4, -3])
    J.shape = tuple(int(v) for v in J.hi - J.lo + 1)
    N0 = J.background()
    S0 = J.with_signal(N0, SIG1)
    rule = RZRule()
    s = S0
    n = N0
    ok = True
    for t in range(1, 61):
        s, n = rule.step(s), rule.step(n)
        d = np.argwhere((s[0] != n[0]) | (s[1] != n[1]))
        ok &= len(d) <= 3 and (np.abs(s[0]).max() <= 1) and (np.abs(s[1]).max() <= 1)
        ok &= bool((d[:, 1:] == np.array([4, 3])).all())     # on the line (y = z = 0)
        if t % 3 == 0:
            ok &= bool(d[:, 0].min() + J.lo[0] == -11 + t // 3)  # moves +1 per 3 ticks
    check("K0 W2 signal on a straight A moves toward the junction at speed 1/3; background behind it is N(t)",
          ok)
    # the transplant/glider test reproduces U1 E2 on a straight B ring: an outgoing glider (3, +1)
    J1 = Junction("J1", 1)
    ring = ring_background(1, J1.off)
    yp, y = ring[0].copy(), ring[1].copy()
    # flip the (+1,+1) pair of B whose fresh (even) site is the outer one: it moves +y (as on A)
    k = next(k for k in range(20, 40) if k % 2 == 1 and (y if (k + 1) % 2 == 0 else yp)[k + 1] == 1
             and yp[k] == 1)
    yp[k], y[k + 1] = -yp[k], -y[k + 1]
    g = glider((yp, y), +1)
    # U1 E2: y(t+3) = -shift y(t), the whole line negated; without negation the period is 6, shift 2
    check("K0b straight-ring reference: a W2 defect on B is an outgoing glider (p, s) = (6, 2)", g == (6, 2), f"{g}")


def check_oracle():
    """Review B1: a positive/negative pair through classify_rz itself. The oracle runs the line rule
    along A -> corner -> B as one bent path (J1, B phase 1, which continues A's pattern round the
    corner), so the signal is transferred onto B by construction; R1-R7 must pass and R8 must reject
    it because it is not Q. With B cut off from the corner (A and B separate paths) the same
    signal stops at A's end: R2 must report no output on B."""
    J = Junction("J1", 1)
    bent = PathOracle(J, [J.A + J.B])
    ok_p, f_p, i_p = classify_rz(J, [], rule=bent)
    check("O1 bent-line oracle through classify_rz: passes R1-R7, first failure R8 (not Q)",
          (not ok_p) and f_p == "R8" and i_p.get("R2", {}).get("glider (p, s)") == (6, 2)
          and i_p.get("R5", {}).get("glider (p, s)") == (6, 2), f"{f_p} {i_p}")
    cut = PathOracle(J, [J.A, J.B])
    ok_n, f_n, i_n = classify_rz(J, [], rule=cut)
    check("O2 the same oracle with B cut off from the corner: first failure R2, no output on B",
          (not ok_n) and f_n == "R2" and "no output on B" in i_n, f"{f_n} {i_n}")


def check_controls():
    # N1 no input: J1 plain corner at every B phase; a phase passes R1 iff the corner is quiescent
    q1 = {}
    for phi in range(4):
        J = Junction("J1", phi)
        ok, fail, info = classify_rz(J, [])
        q1[phi] = fail
    # N2 dead end
    J = Junction("DEAD", 0)
    ok2, f2, i2 = classify_rz(J, [])
    check("N2 dead end (A alone, no B): classified fail", not ok2, f"first failing requirement {f2} {i2}")
    # N3 input that cannot reach the junction before T1 (A to x = -80)
    res3 = {}
    for phi in range(4):
        J = Junction("J1", phi, LA=80)
        ok3, f3, i3 = classify_rz(J, [], sig=SIG_FAR)
        res3[phi] = (ok3, f3)
    check("N3 J1 plain corner, signal 52+ sites away (no arrival by T1): classified fail at every B phase",
          not any(v[0] for v in res3.values()), f"{res3}")
    # N4 linear rule on the J1 plain corner
    res4 = {}
    for phi in range(4):
        J = Junction("J1", phi)
        ok4, f4, _ = classify_rz(J, [], rule=LinRule())
        res4[phi] = (ok4, f4)
    check("N4 linear member L_{2^16,3^-1}, same initial states: classified fail", not any(v[0] for v in res4.values()),
          f"{res4}")
    # P1 lattice billiard with a fixed mirror: pass; countercontrol without the mirror: fail
    pos, neg = lg_controls()
    check("P1 lattice billiard with one fixed 90-degree mirror: classified pass (R1-R3, R5, R7)", pos[0] is True,
          f"{pos}")
    check("P1b the same without the mirror (particle runs straight): classified fail", neg[0] is False, f"{neg}")
    f5 = bbm_control()
    check("P2 U1 collision turn with a supplied constant particle: classified fail (first failing R1)",
          f5 == (False, "R1"), f"{f5}")
    return q1


# ================================================================ batched prefilter and families
def family_candidates(name):
    if name == "F1":
        J = Junction("J1", 0)
        sites = [p for p in J.R if p[2] == 0]
        assert len(sites) == 6
        return "J1", [list(zip(sites, vals)) for vals in itertools.product(range(-2, 3), repeat=6)]
    if name == "F2":
        J = Junction("J1", 0)
        assert len(J.R) == 24
        out = []
        for k in range(4):
            for S in itertools.combinations(J.R, k):
                for vals in itertools.product((-1, 1), repeat=k):
                    out.append(list(zip(S, vals)))
        return "J1", out
    if name in ("F3-J2", "F3-J3"):
        kind = name[-2:]
        J = Junction(kind, 0)
        out = []
        for k in range(3):
            for S in itertools.combinations(J.R, k):
                for vals in itertools.product((-2, -1, 1, 2), repeat=k):
                    out.append(list(zip(S, vals)))
        return kind, out
    raise ValueError(name)


def expected_count(name):
    if name == "F1":
        return 5 ** 6
    if name == "F2":
        return 1 + 24 * 2 + math.comb(24, 2) * 4 + math.comb(24, 3) * 8
    kind = name[-2:]
    r = len(Junction(kind, 0).R)
    return 1 + 4 * r + 16 * math.comb(r, 2)


def prefilter(J, cands, batch=256):
    """R1, the radiation part of R3, and R2-window/R3 at T1, batched. Returns indices that pass."""
    rule = RZRule(batch=True)
    base = J.background()
    allowed_R = J.mask_line | J.mask_R
    allowed_Rp = J.mask_line | J.mask_Rplus
    outside = ~J.mask_farB
    keep = []
    stats = Counter()
    quiescent = []
    for a in range(0, len(cands), batch):
        idx = np.arange(a, min(a + batch, len(cands)))
        n = len(idx)
        yp = np.repeat(base[0][None], n, 0).astype(np.int32)
        y = np.repeat(base[1][None], n, 0).astype(np.int32)
        for b, ci in enumerate(idx):
            for p, v in cands[ci]:
                (y if parity(p) == 0 else yp)[(b,) + J.idx(p)] = v
        N = [(yp, y)]
        s = N[0]
        alive = np.ones(n, bool)
        for t in range(1, 9):
            s = rule.step(s)
            if t < 4:
                N.append(s)
            if t == 4:
                alive &= (s[0] == N[0][0]).reshape(n, -1).all(1) & (s[1] == N[0][1]).reshape(n, -1).all(1)
            alive &= ~(rule.nonzero(s) & ~allowed_R).reshape(n, -1).any(1)
        stats["quiescent (R1)"] += int(alive.sum())
        quiescent.extend(int(i) for i in idx[alive])
        if not alive.any():
            continue
        sel = np.nonzero(alive)[0]
        idx = idx[sel]
        N = [(u[0][sel], u[1][sel]) for u in N]
        s = (N[0][0].copy(), N[0][1].copy())
        for x in SIG1:
            p = (x, 0, 0)
            arr = s[1] if parity(p) == 0 else s[0]
            arr[(slice(None),) + J.idx(p)] *= -1
        for t in range(1, T1 + 1):
            s = rule.step(s)
            bad = (rule.nonzero(s) & ~allowed_Rp).reshape(len(idx), -1).any(1)
            bad |= (np.abs(s[1]) >= 2 ** 15).reshape(len(idx), -1).any(1)
            if bad.any():
                good = ~bad
                idx = idx[good]
                s = (s[0][good], s[1][good])
                N = [(u[0][good], u[1][good]) for u in N]
                if len(idx) == 0:
                    break
        stats["no radiation to T1"] += len(idx)
        if len(idx) == 0:
            continue
        nT = N[T1 % 4]
        for b in range(len(idx)):
            okr = np.array_equal(s[0][b][outside], nT[0][b][outside]) and np.array_equal(s[1][b][outside], nT[1][b][outside])
            d = np.argwhere((s[0][b] != nT[0][b]) | (s[1][b] != nT[1][b]))
            okw = len(d) > 0 and bool(J.mask_farB[tuple(d.T)].all()) and (d[:, 1].max() - d[:, 1].min() + 1 <= 12)
            if okr and okw:
                keep.append(int(idx[b]))
            stats["restored outside far B"] += int(okr)
            stats["output on far B (window <= 12)"] += int(okw)
    return keep, stats, quiescent


def first_escape(J, gadget):
    """Post hoc (not preregistered): the first tick at which the one-signal orbit has a nonzero
    value outside lines and R+, and the class of those sites by their line neighbours."""
    rule = RZRule()
    S = J.with_signal(J.with_gadget(J.background(), gadget), SIG1)
    allowed = J.mask_line | J.mask_Rplus
    A, B = set(J.A), set(J.B)
    for t in range(1, T1 + 1):
        S = rule.step(S)
        bad = np.argwhere(rule.nonzero(S) & ~allowed)
        if len(bad):
            cls = set()
            for b in bad:
                p = tuple(int(v) for v in b + J.lo)
                nb = [(p[0] + d[0], p[1] + d[1], p[2] + d[2]) for d in
                      ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))]
                if p in A or p in B:
                    cls.add("on a line")
                elif any(n in B for n in nb):
                    cls.add("beside B")
                elif any(n in A for n in nb):
                    cls.add("beside A")
                else:
                    cls.add("off the lines")
            return t, tuple(sorted(cls))
    return None, ()


posthoc = {}
quiescent_table = {}
escape_after_24 = []
EXPECTED_QUIESCENT = {"F1": [0, 28, 12, 0], "F2": [102, 822, 369, 24], "F3-J2": [8, 450, 482, 8],
                      "F3-J3": [0, 6, 403, 6]}


def check_D1():
    """One instance (RESULT section 3): J1 plain corner, B phase 1. The inner-corner site (-1,1,0)
    first leaves its no-input value at t = 28; the first escape from lines and R+ is at t = 30, in
    the row beside B, after the disturbance has moved one site per tick along (-1, y, 0)."""
    J = Junction("J1", 1)
    rule = RZRule()
    N = J.background()
    S = J.with_signal(N, SIG1)
    first_inner = None
    row = {}
    nbvals = {}
    for t in range(1, 31):
        if t == 28:   # values entering the inner corner's update at t = 28: the current slice at 27
            nbvals = {p: (int(S[1][J.idx(p)]), int(N[1][J.idx(p)])) for p in ((-1, 0, 0), (0, 1, 0))}
        N, S = rule.step(N), rule.step(S)
        for y in (1, 2, 3):
            i = J.idx((-1, y, 0))
            if y not in row and (S[0][i] != N[0][i] or S[1][i] != N[1][i]):
                row[y] = t
        if first_inner is None and 1 in row:
            first_inner = row[1]
    t_esc, cls = first_escape(J, [])
    sv = [v[0] for v in nbvals.values()]
    nv = [v[1] for v in nbvals.values()]
    equal = sv[0] == sv[1] != 0 and sum(nv) == 0
    check("D1 J1 plain corner, phase 1: inner corner's two line neighbours equal and nonzero (sum 0 without "
          "input); kicked at t=28; disturbance along (-1,y,0) one site per tick; first escape t=30 beside B",
          equal and first_inner == 28 and row == {1: 28, 2: 29, 3: 30} and t_esc == 30 and cls == ("beside B",),
          f"line neighbours (with, without signal) {nbvals}; row first-change times {row}, escape {t_esc} {cls}")


def run_family(name, q1):
    kind, cands = family_candidates(name)
    n_exp = expected_count(name)
    check(f"{name} completeness: {len(cands)} gadgets enumerated, PREREG count {n_exp}", len(cands) == n_exp)
    tally = Counter()
    passing = []
    survivors_all = []
    rng = np.random.RandomState(20261120)
    sample = rng.choice(len(cands), 100, replace=False)
    agree = True
    for phi in range(4):
        J = Junction(kind, phi)
        keep, st, quiet = prefilter(J, cands)
        print(f"  {name} phi={phi}: {dict(st)}", flush=True)
        # post hoc (not preregistered): every quiescent gadget through the canonical classifier,
        # and where its first escape occurs; this changes no verdict
        allq = Counter()
        esc = Counter()
        for k in quiet:
            ok, fail, info = classify_rz(J, cands[k])
            allq[fail or "pass"] += 1
            t, cls = first_escape(J, cands[k])
            esc[(t is not None and t > 24, cls)] += 1
            escape_after_24.append(t is not None and t > 24)
        quiescent_table.setdefault(name, []).append(len(quiet))
        print(f"  {name} phi={phi} post hoc: classifier on all {len(quiet)} quiescent gadgets {dict(allq)}; "
              f"first escape (after the signal's arrival window t > 24, site class): {dict(esc)}", flush=True)
        posthoc[name] = posthoc.get(name, Counter()) + allq
        survivors_all += [(phi, k) for k in keep]
        for k in keep:
            ok, fail, info = classify_rz(J, cands[k])
            tally[fail or "pass"] += 1
            if ok:
                passing.append((phi, cands[k], info))
        # cross-check on the seeded sample (phi = 0 only, by the order of A01 item 5's sample)
        if phi == 0:
            ks = set(keep)
            for k in sample:
                ok, fail, info = classify_rz(J, cands[k])
                pre_should = fail not in ("R1", "R3") and not (fail == "R2" and (
                    "no output on B" in info or "output window" in info))
                agree &= (k in ks) == pre_should
    check(f"{name} prefilter agrees with the classifier on 100 seeded candidates", agree)
    print(f"RESULT {name}: {len(cands)} gadgets x 4 B-phases; prefilter survivors {len(survivors_all)}; "
          f"classifier outcomes on survivors {dict(tally)}; passing {len(passing)}", flush=True)
    for phi, g, info in passing[:10]:
        print(f"  PASS phi={phi} gadget={g} info={info}", flush=True)
    return passing, survivors_all


def main():
    check_A1()
    check_K0()
    q1 = check_controls()
    print(f"N1 J1 plain corner, no input: first failing requirement by B phase {q1} "
          f"(None = quiescent and passes R1)")
    check_oracle()
    check_D1()
    check_A2("--search" in sys.argv)
    if "--search" in sys.argv:
        for name in ("F1", "F2", "F3-J2", "F3-J3"):
            run_family(name, q1)
    if "--search" in sys.argv:
        tot = sum(posthoc.values(), Counter())
        check("X1 (post hoc) every quiescent gadget of F1-F3 fails the classifier first at R3 (radiation)",
              set(tot) == {"R3"}, f"{dict(tot)}")
        total = sum(sum(v) for v in quiescent_table.values())
        check("X2 quiescent (R1) counts per family and B phase equal the RESULT table; total 2720",
              quiescent_table == EXPECTED_QUIESCENT and total == 2720 == sum(tot.values()),
              f"{quiescent_table}, total {total}")
        check("X3 every quiescent gadget's first escape occurs after t = 24",
              len(escape_after_24) == 2720 and all(escape_after_24), f"{sum(escape_after_24)}/{len(escape_after_24)}")
    bad = [n for n, ok in RESULTS if not ok]
    print(f"{len(RESULTS) - len(bad)}/{len(RESULTS)} checks pass")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
