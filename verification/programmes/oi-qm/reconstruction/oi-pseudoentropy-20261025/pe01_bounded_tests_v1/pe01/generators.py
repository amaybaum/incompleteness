"""The PE-01 generators (PLAN.md §1): phi = tau_f o kappa_sigma on C_V x C_H, and the mutant G_tape(N).

State encoding: s = x + 2*h, with x in {0,1} the visible bit and h the hidden index. For the
LFSR generators h is the integer with bit i = h_i. For G_tape(N), h = u + 2^N * c with u the tape
(bit t = u_t) and c the clock in Z_{N+1}.

phi(x, h) = (x XOR f(sigma_x(h)), sigma_x(h)): first kappa_sigma, then tau_f.
"""
import numpy as np

from . import gf2

FAMILIES = ("lin", "filt", "clk")


class Gen:
    """A generator given by its tables sigma[x][h] and f[h], with an explicit prior on seeds."""

    def __init__(self, name, family, n, p, sig, f, H, prior=None, gid=None):
        self.name = name
        self.family = family
        self.n = n
        self.p = p
        self.sig = sig          # (2, H) int64
        self.f = f              # (H,) uint8
        self.H = H
        self.S = 2 * H
        self.gid = gid or name
        if prior is None:
            # mu uniform on C_V x C_H: every state is a seed of weight 1.
            s = np.arange(self.S, dtype=np.int64)
            self.seed_x = (s & 1).astype(np.uint8)
            self.seed_h = (s >> 1).astype(np.int64)
            self.seed_w = np.ones(self.S, dtype=np.int64)
        else:
            self.seed_x, self.seed_h, self.seed_w = prior
        self.M = int(self.seed_w.sum())
        self._rec = None

    # -- the bijection as a table --
    def phi_table(self):
        s = np.arange(self.S, dtype=np.int64)
        x = s & 1
        h = s >> 1
        h2 = self.sig[x, h]
        x2 = x ^ self.f[h2]
        return x2 + 2 * h2

    def step(self, x, h):
        h2 = self.sig[x, h]
        return (x ^ self.f[h2]).astype(np.uint8), h2

    def records(self, kcap):
        """X[seed, t] for t = 0..kcap, the visible trajectory of every prior seed."""
        if self._rec is not None and self._rec.shape[1] > kcap:
            return self._rec[:, :kcap + 1]
        X = np.empty((len(self.seed_x), kcap + 1), dtype=np.uint8)
        x = self.seed_x.astype(np.int64)
        h = self.seed_h.copy()
        X[:, 0] = x
        for t in range(1, kcap + 1):
            h = self.sig[x, h]
            x = x ^ self.f[h]
            X[:, t] = x
        self._rec = X
        return X

    def desc(self):
        d = {"name": self.name, "family": self.family, "n": self.n, "id": self.gid}
        if self.p is not None:
            d["p"] = gf2.poly_str(self.p)
        return d


def companion_table(p, n):
    """Fibonacci companion map L_p: (h_0..h_{n-1}) -> (h_1..h_{n-1}, sum_i c_i h_i), p = z^n + sum c_i z^i."""
    cmask = p & ((1 << n) - 1)
    h = np.arange(1 << n, dtype=np.int64)
    par = np.zeros(1 << n, dtype=np.int64)
    t = h & cmask
    while True:
        nz = t != 0
        if not nz.any():
            break
        par ^= (t & 1)
        t >>= 1
    return (h >> 1) | (par << (n - 1))


def ell_table(n):
    h = np.arange(1 << n, dtype=np.int64)
    return (h & 1).astype(np.uint8)


def g_table(n):
    h = np.arange(1 << n, dtype=np.int64)
    return ((h & 1) ^ (((h >> 1) & 1) & ((h >> 2) & 1))).astype(np.uint8)


def make(family, n, p, name=None):
    L = companion_table(p, n)
    H = 1 << n
    if family == "lin":
        sig, f = np.stack([L, L]), ell_table(n)
    elif family == "filt":
        sig, f = np.stack([L, L]), g_table(n)
    elif family == "clk":
        sig, f = np.stack([L, L[L]]), ell_table(n)
    elif family == "dec":
        sig, f = np.stack([L, L]), np.zeros(H, dtype=np.uint8)
    else:
        raise ValueError(family)
    gid = "%s(%s)" % (family, gf2.poly_str(p))
    return Gen(name or gid, family, n, p, sig, f, H, gid=gid)


def p_n(n):
    return gf2.poly(gf2.P_EXPS[n])


def pr_n(n):
    return gf2.poly(gf2.PR_EXPS[n])


def named(n):
    """The five named generators of PLAN.md §1 at degree n (G_tape separately)."""
    p, pr = p_n(n), pr_n(n)
    return {
        "G_lin": make("lin", n, p, "G_lin"),
        "G_filt": make("filt", n, p, "G_filt"),
        "G_clk": make("clk", n, p, "G_clk"),
        "G_lin_sib": make("lin", n, pr, "G_lin_sib"),
        "G_dec": make("dec", n, p, "G_dec"),
    }


def family(fam, n):
    """The K0 family F_fam(n): one generator per primitive p of degree n, ascending p."""
    return [make(fam, n, p) for p in gf2.primitive_polys(n)]


def tape(N):
    """G_tape(N): C_H = {0,1}^N x Z_{N+1}, sigma_x(u,c) = (u, c+1), f(u,c) = u_{c-1} (c >= 1), 0 (c = 0).

    Prior: x_0 uniform, independent of a uniform tape, clock at 0.
    """
    U = 1 << N
    H = U * (N + 1)
    h = np.arange(H, dtype=np.int64)
    u = h % U
    c = h // U
    c2 = (c + 1) % (N + 1)
    nxt = u + U * c2
    sig = np.stack([nxt, nxt])
    f = np.where(c >= 1, (u >> np.maximum(c - 1, 0)) & 1, 0).astype(np.uint8)
    # prior: x in {0,1}, u in {0,1}^N, c = 0
    xs = np.repeat(np.array([0, 1], dtype=np.uint8), U)
    hs = np.tile(np.arange(U, dtype=np.int64), 2)
    ws = np.ones(2 * U, dtype=np.int64)
    return Gen("G_tape(%d)" % N, "tape", None, None, sig, f, H, prior=(xs, hs, ws), gid="tape(%d)" % N)


def is_bijection(table, size):
    """EX1: image cardinality equals the domain size (a boolean mark array, no sort)."""
    if len(table) != size:
        return False
    seen = np.zeros(size, dtype=bool)
    if table.min() < 0 or table.max() >= size:
        return False
    seen[table] = True
    return bool(seen.all())


def orbit_lengths(table):
    """Orbit length of every point of a permutation table."""
    S = len(table)
    out = np.zeros(S, dtype=np.int64)
    seen = np.zeros(S, dtype=bool)
    tl = table.tolist()
    for s0 in range(S):
        if seen[s0]:
            continue
        cyc = [s0]
        seen[s0] = True
        t = tl[s0]
        while t != s0:
            cyc.append(t)
            seen[t] = True
            t = tl[t]
        out[cyc] = len(cyc)
    return out
