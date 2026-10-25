"""The composite bijection phi' on C_V' x C_H, built from register-level maps (PLAN.md §3, §5).

Visible registers: sys bit x, memory v (m bits), clock clk (c bits), output out (1 bit). The full
state index is s = vis + Vsize * h with vis = x | v << 1 | clk << (1 + m) | out << (1 + m + c).

Component maps, each a table over all of C_V' x C_H:
  Readout_{F,K}: out <- out XOR (1[clk == K] AND 1[(v, x) in F])   (clocked composites only)
  Rho:           v <- rho_x(v)
  Act:           x <- x XOR a(v)
  Gen:           (x, h) <- phi(x, h)
  Tick:          clk <- clk + 1 mod 2^c
One application of phi' = Tick o Gen o Act o Rho o Readout. The clock starts at 0 and counts
rounds, so after K + 1 applications out = 1[(v_K, x_K) in F]. These tables are the full-state path
of IM3; the sweep in embedded.py is the aggregated path. Nothing here is shared with it except the
observer and generator tables themselves.
"""
import numpy as np


def clock_bits(K):
    return (K).bit_length() if K > 0 else 0   # = ceil(log2(K + 1))


class Layout:
    def __init__(self, m, c, H):
        self.m, self.c, self.H = m, c, H
        self.registers = [("sys", 1), ("mem", m), ("clk", c), ("out", 1)]
        self.Vsize = 1
        for _, w in self.registers:
            self.Vsize <<= w
        self.S = self.Vsize * H
        s = np.arange(self.S, dtype=np.int64)
        vis = s % self.Vsize
        self.h = s // self.Vsize
        self.x = vis & 1
        self.v = (vis >> 1) & ((1 << m) - 1)
        self.clk = (vis >> (1 + m)) & ((1 << c) - 1)
        self.out = (vis >> (1 + m + c)) & 1

    def enc(self, x, v, clk, out, h):
        m, c = self.m, self.c
        return (x | (v << 1) | (clk << (1 + m)) | (out << (1 + m + c))) + self.Vsize * h

    def footprint(self):
        """FP: total bit width of the visible registers, less the system bit, read from the layout."""
        assert self.Vsize & (self.Vsize - 1) == 0
        return (self.Vsize.bit_length() - 1) - 1


def t_rho(L, R):           # R: (V,) pair rows R[x][v]
    return L.enc(L.x, R[L.x, L.v], L.clk, L.out, L.h)


def t_act(L, a):
    return L.enc(L.x ^ a[L.v], L.v, L.clk, L.out, L.h)


def t_gen(L, gen):
    h2 = gen.sig[L.x, L.h]
    x2 = L.x ^ gen.f[h2]
    return L.enc(x2, L.v, L.clk, L.out, h2)


def t_tick(L):
    return L.enc(L.x, L.v, (L.clk + 1) % (1 << L.c) if L.c else L.clk, L.out, L.h)


def t_readout(L, Fcells, K):
    """Fcells: (V, 2) 0/1 array, F's indicator over (v, x)."""
    fire = (L.clk == K) & (Fcells[L.v, L.x] == 1)
    return L.enc(L.x, L.v, L.clk, L.out ^ fire.astype(np.int64), L.h)


def is_perm(T):
    if T.ndim == 1:
        T = T[None, :]
    return bool((np.sort(T, axis=1) == np.arange(T.shape[1])[None, :]).all())


def ex8_observer_map(L, T):
    """EX8 for an observer map: h-component identity and visible component constant across h."""
    if T.ndim == 1:
        T = T[None, :]
    s = np.arange(L.S, dtype=np.int64)[None, :]
    hid = (T // L.Vsize) == (s // L.Vsize)
    vis = (T % L.Vsize).reshape(T.shape[0], L.H, L.Vsize)
    const = (vis == vis[:, :1, :]).all()
    return bool(hid.all() and const)


def ex8_generator_map(L, T):
    """EX8 converse: the generator step is the identity on (v, clk, out)."""
    s = np.arange(L.S, dtype=np.int64)
    return bool((((T % L.Vsize) >> 1) == ((s % L.Vsize) >> 1)).all())


def compose(*tables):
    """compose(T1, T2, ..., Tk) = Tk o ... o T1 (T1 applied first)."""
    out = tables[0]
    for T in tables[1:]:
        out = T[out]
    return out


def prior_dist(L, gen):
    """mu (x) delta_{v=0, clk=0, out=0} as integer counts over the full state space."""
    d = np.zeros(L.S, dtype=np.int64)
    s = L.enc(gen.seed_x.astype(np.int64), np.zeros_like(gen.seed_h), np.zeros_like(gen.seed_h),
              np.zeros_like(gen.seed_h), gen.seed_h)
    np.add.at(d, s, gen.seed_w)
    return d


def ex7_prior(L, gen, d):
    """EX7 (with EX8) and the AR prior assumption: the joint prior is mu (x) delta_{v0}; mu has h
    uniform and independent of x_0; memory, clock and output start at fixed values."""
    t = d.reshape(L.H, L.Vsize)
    regs_fixed = bool((t[:, (np.arange(L.Vsize) >> 1) != 0] == 0).all())
    mu = t[:, :2]                                   # (H, 2) counts of (h, x) with v = clk = out = 0
    tot = int(mu.sum())
    px = mu.sum(axis=0)
    ph = mu.sum(axis=1)
    product = bool((mu * tot == np.outer(ph, px)).all())
    h_uniform = bool((ph == ph[0]).all())
    return {"registers_fixed": regs_fixed, "product": product, "h_uniform": h_uniform,
            "pass": regs_fixed and product}


class Witness:
    """The clocked composite of one witness (phi, O = (rho_0, rho_1, a, F), K)."""

    def __init__(self, gen, m, R, a, chi, K):
        self.gen, self.m, self.K = gen, m, K
        V = 1 << m
        self.c = clock_bits(K)
        L = Layout(m, self.c, gen.H)
        self.L = L
        R = np.asarray(R, dtype=np.int64)
        a = np.asarray(a, dtype=np.int64)
        self.chi = np.asarray(chi, dtype=np.int64)
        F = np.zeros((V, 2), dtype=np.int64)
        F[np.arange(V), self.chi] = 1              # F = graph of chi
        self.F = F
        self.maps = {"readout": t_readout(L, F, K), "rho": t_rho(L, R), "act": t_act(L, a),
                     "gen": t_gen(L, gen), "tick": t_tick(L)}
        self.phi = compose(self.maps["readout"], self.maps["rho"], self.maps["act"], self.maps["gen"],
                           self.maps["tick"])

    def checks(self):
        L = self.L
        ex1 = all(is_perm(T) for T in self.maps.values()) and is_perm(self.phi) and len(self.phi) == L.S
        ex8 = all(ex8_observer_map(L, self.maps[k]) for k in ("readout", "rho", "act", "tick")) \
            and ex8_generator_map(L, self.maps["gen"])
        d0 = prior_dist(L, self.gen)
        e7 = ex7_prior(L, self.gen, d0)
        return {"EX1": ex1, "EX8": ex8, "EX7": bool(ex8 and e7["pass"]), "prior": e7}

    def simulate(self):
        """Full-state simulation through the composite table: every prior seed's full state is
        iterated by phi'. Returns hits[t] = #seeds with x_t = chi(v_t) (t = 0..K), the number with
        out = 1 after K + 1 applications, and M."""
        L = self.L
        g = self.gen
        z = np.zeros_like(g.seed_h)
        s = L.enc(g.seed_x.astype(np.int64), z, z, z, g.seed_h)
        w = g.seed_w
        M = int(w.sum())
        hits = []
        for t in range(self.K + 2):
            if t <= self.K:
                ok = self.chi[L.v[s]] == L.x[s]
                hits.append(int(w[ok].sum()))
            s = self.phi[s]
        out1 = int(w[L.out[s] == 1].sum())
        return hits, out1, M

    def table_size_bits(self):
        m = self.m
        return 2 * m * (1 << m) + (1 << m) + (1 << (m + 1)) + self.c


class FullState:
    """IM3 full-state path for a chunk of observers (unclocked composites; the readout is not
    needed for (v_K, x_K)): per generator the round table Gen o Act o Rho, iterated on mu (x) delta."""

    def __init__(self, obs, idx, gens):
        self.gens = gens
        self.m = obs.m
        self.V = obs.V
        self.Ls = []
        self.T = []
        self.d = []
        R = obs.R[idx]
        A = obs.Aact[idx]
        c = len(idx)
        for g in gens:
            L = Layout(obs.m, 0, g.H)
            # build per-observer tables from register-level definitions
            rho = L.enc(L.x[None, :], R[np.arange(c)[:, None], L.x[None, :], L.v[None, :]], L.clk[None, :],
                        L.out[None, :], L.h[None, :])
            x1 = L.x[None, :] ^ A[np.arange(c)[:, None], L.v[None, :]]
            act = L.enc(x1, L.v[None, :], L.clk[None, :], L.out[None, :], L.h[None, :])
            gen = t_gen(L, g)
            T = gen[act[np.arange(c)[:, None], rho]]
            self.Ls.append(L)
            self.T.append(T)
            d0 = prior_dist(L, g)
            self.d.append(np.broadcast_to(d0[None, :], (c, L.S)).copy())
        self.c = c

    def counts(self, gi):
        L = self.Ls[gi]
        d = self.d[gi].reshape(self.c, L.H, 2, self.V, 2)   # (o, h, out, v, x)
        return d.sum(axis=(1, 2))

    def compare(self, K, Cs):
        for gi, C in Cs.items():
            if not np.array_equal(self.counts(gi), C):
                return False, "gen %d" % gi
        return True, ""

    def step(self):
        for gi in range(len(self.gens)):
            T = self.T[gi]
            d = self.d[gi]
            nd = np.zeros_like(d)
            nd[np.arange(self.c)[:, None], T] = d
            self.d[gi] = nd


def exhaustive_maps(obs, gen, chunk=4096):
    """EX1 and EX8 for every observer of obs against gen (unclocked composite, n <= 4)."""
    L = Layout(obs.m, 0, gen.H)
    ok1 = True
    ok8 = True
    gT = t_gen(L, gen)
    ok1 &= is_perm(gT)
    ok8 &= ex8_generator_map(L, gT)
    for st in range(0, obs.n, chunk):
        idx = np.arange(st, min(obs.n, st + chunk))
        c = len(idx)
        R = obs.R[idx]
        A = obs.Aact[idx]
        ar = np.arange(c)[:, None]
        rho = L.enc(L.x[None, :], R[ar, L.x[None, :], L.v[None, :]], L.clk[None, :], L.out[None, :], L.h[None, :])
        act = L.enc(L.x[None, :] ^ A[ar, L.v[None, :]], L.v[None, :], L.clk[None, :], L.out[None, :], L.h[None, :])
        ok1 &= is_perm(rho) and is_perm(act)
        ok8 &= ex8_observer_map(L, rho) and ex8_observer_map(L, act)
        rnd = gT[act[ar, rho]]
        ok1 &= is_perm(rnd)
    return ok1, ok8


def exhaustive_readout(m, gen, Fs, K=1):
    """EX1 and EX8 of the clocked readout (and the clock tick) for every F in Fs (cells bitmasks)."""
    c = clock_bits(K)
    L = Layout(m, c, gen.H)
    V = 1 << m
    ok1 = is_perm(t_tick(L))
    ok8 = ex8_observer_map(L, t_tick(L))
    cell = L.v * 2 + L.x
    fire_base = (L.clk == K)
    for Fm in Fs:
        bit = (np.int64(Fm) >> cell) & 1 if Fm < (1 << 62) else np.array([(Fm >> int(k)) & 1 for k in cell])
        T = L.enc(L.x, L.v, L.clk, L.out ^ (fire_base & (bit == 1)).astype(np.int64), L.h)
        ok1 &= is_perm(T)
        ok8 &= ex8_observer_map(L, T)
    return ok1, ok8
