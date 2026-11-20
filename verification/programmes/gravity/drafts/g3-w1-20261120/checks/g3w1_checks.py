#!/usr/bin/env python3
"""G3-W1: conserved additive quantities of the d = 3 rounded rule (PREREG.md).

Rule RZ on Z^3: F(p, y) = (y, G(S y) - p), G(s) = floor((s + 1)/3), S the six-neighbour sum.
Q is the same rule mod 2^16 on representatives 0..2^16-1.

For a class of densities with n unknown coefficients, every periodic integer configuration c
gives the necessary linear equation  sum_windows f(F c) - f(c) = 0  on the coefficient vector
(f: integer features).  A class is certified when n - rank_p(E) = rank_p(T), T the span of the
constant and the coboundaries; then ker_Q(E) = T (PREREG §3), i.e. every conserved quantity of
the class is trivial on all periodic configurations.  Ranks are computed mod a prime p < 2^20 in
float64 arithmetic whose every partial sum is asserted below 2^53, so they are exact mod p.

Run:  python3 -I g3w1_checks.py --part A|B|C|D  (writes results-<part>.json next to this file)
      python3 -I g3w1_checks.py --render        (merges the parts, evaluates P1, P2, C1-C3 and
                                                 coverage, writes results.json with the verdict)
      python3 -I g3w1_checks.py --only LABEL    (one class, diagnostics only; writes nothing)
Parts: A = K1, K2 and families G1, G2; B, C = family G3; D = the 3D classes with the
preregistered trivial space; D2 = the same with the trivial space of amendment A01.
Exit status 0 iff every control passes.
"""
import itertools
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

P1_PRIME = 1048573
P2_PRIME = 1048571
Q = 2 ** 16
C0 = 2 ** 15
TWO53 = 2 ** 53
HERE = os.path.dirname(os.path.abspath(__file__))

CONTROLS = []


def control(cid, ok, info=""):
    CONTROLS.append({"id": cid, "pass": bool(ok), "info": info})
    print(f"CONTROL {cid}: {'PASS' if ok else 'FAIL'}  {info}", flush=True)


def G(s):
    return np.floor_divide(s + 1, 3)


# ============================================================ rules
def s1d(y, kind):
    ym, yp = np.roll(y, 1, -1), np.roll(y, -1, -1)
    if kind == "ax":
        return ym + yp + 4 * y
    if kind == "fd":
        return 2 * (ym + y + yp)
    if kind == "bd":
        return 3 * (ym + yp)
    raise ValueError(kind)


def step1d(p, y, kind):
    return y, G(s1d(y, kind)) - p


def back1d(p, y, kind):
    return G(s1d(p, kind)) - y, p


def S3(y):
    return sum(np.roll(y, sh, ax) for ax in (-3, -2, -1) for sh in (1, -1))


def step3(p, y, rule="RZ"):
    if rule == "RZ":
        return y, G(S3(y)) - p
    if rule == "LIN":
        return y, S3(y) - p
    raise ValueError(rule)


def back3(p, y):
    return G(S3(p)) - y, p


def step3q(xp, x):
    return x, np.mod(G(S3(x)) - xp, Q)


# ============================================================ modular elimination (RREF, mod p)
def mod_matmul(A, B, p):
    """(A @ B) mod p for float64 arrays with entries in [0, p); exact (partial sums < 2^53)."""
    k = A.shape[1]
    blk = max(1, int((TWO53 - 1) // ((p - 1) ** 2)) - 1)
    assert blk * (p - 1) ** 2 < TWO53
    out = np.zeros((A.shape[0], B.shape[1]))
    for a in range(0, k, blk):
        out = np.fmod(out + np.fmod(A[:, a:a + blk] @ B[a:a + blk], p), p)
    return out


class Elim:
    def __init__(self, n, p):
        self.n, self.p = n, p
        self.R = np.zeros((0, n))
        self.piv = []

    @property
    def rank(self):
        return len(self.piv)

    def add(self, rows_int):
        p = self.p
        C = np.mod(np.asarray(rows_int, dtype=np.int64), p).astype(np.float64)
        added = 0
        for a in range(0, C.shape[0], 128):
            B = C[a:a + 128]
            if self.piv:
                B = np.fmod(B - mod_matmul(B[:, self.piv], self.R, p) + p, p)
            newrows, newpiv = [], []
            B = B.copy()
            for i in range(B.shape[0]):
                row = B[i]
                nz = np.nonzero(row)[0]
                if len(nz) == 0:
                    continue
                j = int(nz[0])
                inv = pow(int(row[j]), -1, p)
                row = np.fmod(row * inv, p)
                # eliminate column j from the remaining rows of the block and from earlier new rows
                rest = B[i + 1:]
                f = rest[:, j].copy()
                if np.any(f):
                    B[i + 1:] = np.fmod(rest - np.fmod(np.outer(f, row), p) + p, p)
                for t, r0 in enumerate(newrows):
                    if r0[j]:
                        newrows[t] = np.fmod(r0 - np.fmod(r0[j] * row, p) + p, p)
                newrows.append(row)
                newpiv.append(j)
            if newrows:
                Nr = np.array(newrows)
                if self.piv:
                    self.R = np.fmod(self.R - mod_matmul(self.R[:, newpiv], Nr, p) + p, p)
                self.R = np.vstack([self.R, Nr])
                self.piv += newpiv
                added += len(newrows)
        return added

    def nullspace(self):
        free = [j for j in range(self.n) if j not in set(self.piv)]
        out = []
        for f in free:
            v = np.zeros(self.n)
            v[f] = 1
            for i, pc in enumerate(self.piv):
                v[pc] = (-self.R[i, f]) % self.p
            out.append(v.astype(np.int64))
        return out


def rat_rec(a, p):
    a %= p
    r0, r1, s0, s1 = p, a, 0, 1
    bd = math.isqrt(p // 2)
    while r1 > bd:
        qq = r0 // r1
        r0, r1, s0, s1 = r1, r0 - qq * r1, s1, s0 - qq * s1
    if s1 == 0 or abs(s1) > bd:
        return None
    return Fraction(r1, s1)


# ============================================================ class Q_v(m, D, mu): 1D features
def monomials(nvar, D):
    out = []
    for deg in range(D + 1):
        for comb in itertools.combinations_with_replacement(range(nvar), deg):
            e = [0] * nvar
            for c in comb:
                e[c] += 1
            out.append(tuple(e))
    return out


class Class1D:
    def __init__(self, kind, m, D, mu):
        self.kind, self.m, self.D, self.mu = kind, m, D, mu
        self.nvar = 2 * m
        self.mons = monomials(self.nvar, D)
        self.nmon = len(self.mons)
        self.npat = mu ** self.nvar
        self.n = self.npat * self.nmon
        self.label = f"{kind}:Q({m},{D},{mu})"

    def window(self, P, Y):
        cols = []
        for j in range(self.m):
            cols.append(np.roll(P, -j, -1))
            cols.append(np.roll(Y, -j, -1))
        return np.stack(cols, -1)  # (b, L, 2m)

    def features(self, P, Y):
        W = self.window(P, Y)
        b, L, _ = W.shape
        if self.mu > 1:
            R = np.mod(W, self.mu)
            pat = np.zeros((b, L), dtype=np.int64)
            for i in range(self.nvar):
                pat = pat * self.mu + R[..., i]
        else:
            pat = np.zeros((b, L), dtype=np.int64)
        f = np.zeros((b, self.n), dtype=np.int64)
        bidx = np.repeat(np.arange(b), L)
        for mi, e in enumerate(self.mons):
            val = np.ones((b, L), dtype=np.int64)
            for i, ei in enumerate(e):
                if ei:
                    val = val * W[..., i] ** ei
            np.add.at(f, (bidx, (pat * self.nmon + mi).ravel()), val.ravel())
        return f

    def rows(self, P, Y):
        P2, Y2 = step1d(P, Y, self.kind)
        return self.features(P2, Y2) - self.features(P, Y), max(int(np.abs(P).max()), int(np.abs(Y).max()),
                                                               int(np.abs(Y2).max()))

    def sample(self, rng, count):
        B = max(6, 6 * self.mu)
        out = []
        by_L = {}
        for _ in range(count):
            L = int(rng.integers(1, 13))
            by_L[L] = by_L.get(L, 0) + 1
        for L, c in sorted(by_L.items()):
            P = rng.integers(-B, B + 1, size=(c, L))
            Y = rng.integers(-B, B + 1, size=(c, L))
            out.append((P, Y))
        return out

    def phi(self, P, Y, v):
        """exact value of the quantity with coefficient vector v (list of Fractions/ints) on each config"""
        return exact_rows_dot(self.features(P, Y), v)

    def tgen(self):
        """constant + coboundaries of Q(m-1, D, mu), in this class's coordinates"""
        gens = []
        const = np.zeros(self.n, dtype=np.int64)
        for r in range(self.npat):
            const[r * self.nmon + self.mons.index(tuple([0] * self.nvar))] = 1
        gens.append(const)
        if self.m == 1:
            return gens
        mons_s = monomials(self.nvar - 2, self.D)
        mi = {e: i for i, e in enumerate(self.mons)}
        pats = list(itertools.product(range(self.mu), repeat=self.nvar))
        for rs in itertools.product(range(self.mu), repeat=self.nvar - 2):
            for es in mons_s:
                if self.mu == 1 and sum(es) == 0:
                    continue
                g = np.zeros(self.n, dtype=np.int64)
                for r_idx, r in enumerate(pats):
                    # b on cells 2..m (shifted) minus b on cells 1..m-1
                    if tuple(r[2:]) == rs:
                        g[r_idx * self.nmon + mi[tuple([0, 0] + list(es))]] += 1
                    if tuple(r[:-2]) == rs:
                        g[r_idx * self.nmon + mi[tuple(list(es) + [0, 0])]] -= 1
                if np.any(g):
                    gens.append(g)
        return gens

    def vec_from_density(self, dens):
        """coefficient vector for a density given as {(pattern-free) monomial exps: coeff} applied to all
        residue patterns, or as a callable (residue tuple) -> {exps: coeff}"""
        v = [Fraction(0)] * self.n
        mi = {e: i for i, e in enumerate(self.mons)}
        pats = list(itertools.product(range(self.mu), repeat=self.nvar))
        for r_idx, r in enumerate(pats):
            d = dens(r) if callable(dens) else dens
            for e, c in d.items():
                v[r_idx * self.nmon + mi[e]] += Fraction(c)
        return v


def ex(nvar, **kw):
    e = [0] * nvar
    for k, val in kw.items():
        e[int(k[1:])] = val
    return tuple(e)


# ============================================================ class P3 / P3r: 3D features
OFFS = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


class Class3D:
    """variables: index 2*i = p at OFFS[i], 2*i+1 = y at OFFS[i]"""

    def __init__(self, rule, D, resid, full_T=False):
        self.rule, self.D, self.resid, self.full_T = rule, D, resid, full_T
        self.nvar = 14
        self.mons = monomials(14, D)
        self.nmon = len(self.mons)
        self.npat = 9 if resid else 1
        self.n = self.npat * self.nmon
        self.label = f"3D-{rule}:P3{'r' if resid else ''}({D})"
        self.kind = rule

    @staticmethod
    def shifted(x, o):
        # value at n + o
        for ax, d in enumerate(o):
            if d:
                x = np.roll(x, -d, ax - 3)
        return x

    def features(self, P, Y):
        b = P.shape[0]
        Wv = []
        for o in OFFS:
            Wv.append(self.shifted(P, o).reshape(b, -1))
            Wv.append(self.shifted(Y, o).reshape(b, -1))
        W = np.stack(Wv, -1)  # (b, N, 14)
        N = W.shape[1]
        if self.resid:
            pat = np.mod(S3(Y), 3).reshape(b, -1) * 3 + np.mod(S3(P), 3).reshape(b, -1)
        else:
            pat = np.zeros((b, N), dtype=np.int64)
        f = np.zeros((b, self.n), dtype=np.int64)
        bidx = np.repeat(np.arange(b), N)
        for mi, e in enumerate(self.mons):
            val = np.ones((b, N), dtype=np.int64)
            for i, ei in enumerate(e):
                if ei:
                    val = val * W[..., i] ** ei
            np.add.at(f, (bidx, (pat * self.nmon + mi).ravel()), val.ravel())
        return f

    def rows(self, P, Y):
        P2, Y2 = step3(P, Y, self.rule)
        return self.features(P2, Y2) - self.features(P, Y), max(int(np.abs(P).max()), int(np.abs(Y).max()),
                                                               int(np.abs(Y2).max()))

    def sample(self, rng, count):
        B = 6
        by = {}
        for _ in range(count):
            sh = tuple(int(x) for x in rng.integers(1, 5, size=3))
            by[sh] = by.get(sh, 0) + 1
        out = []
        for sh, c in sorted(by.items()):
            out.append((rng.integers(-B, B + 1, size=(c,) + sh), rng.integers(-B, B + 1, size=(c,) + sh)))
        return out

    def phi(self, P, Y, v):
        return exact_rows_dot(self.features(P, Y), v)

    def tgen(self):
        return self.tgen_full() if self.full_T else self.tgen_prereg()

    def tgen_full(self):
        """amendment A01: constant + every translation coboundary m o tau_a - m with m and m o tau_a
        both monomials of the star class (uniform across residue patterns for P3r)"""
        mi = {e: i for i, e in enumerate(self.mons)}
        gens = []
        const = np.zeros(self.n, dtype=np.int64)
        for r in range(self.npat):
            const[r * self.nmon + mi[tuple([0] * 14)]] = 1
        gens.append(const)
        offs_set = set(OFFS)
        for e in self.mons:
            if sum(e) == 0:
                continue
            used = [k for k, x in enumerate(e) if x]
            o0 = OFFS[used[0] // 2]
            for o2 in OFFS:
                a = tuple(o2[i] - o0[i] for i in range(3))
                if a == (0, 0, 0):
                    continue
                new, ok = [0] * 14, True
                for k in used:
                    o = OFFS[k // 2]
                    t = tuple(o[i] + a[i] for i in range(3))
                    if t not in offs_set:
                        ok = False
                        break
                    new[2 * OFFS.index(t) + k % 2] += e[k]
                if not ok:
                    continue
                g = np.zeros(self.n, dtype=np.int64)
                for r in range(self.npat):
                    g[r * self.nmon + mi[tuple(new)]] += 1
                    g[r * self.nmon + mi[e]] -= 1
                gens.append(g)
        return gens

    def tgen_prereg(self):
        mi = {e: i for i, e in enumerate(self.mons)}
        idx = {o: i for i, o in enumerate(OFFS)}
        gens = []
        const = np.zeros(self.n, dtype=np.int64)
        for r in range(self.npat):
            const[r * self.nmon + mi[tuple([0] * 14)]] = 1
        gens.append(const)
        for j in range(3):
            ej = tuple(1 if a == j else 0 for a in range(3))
            mej = tuple(-x for x in ej)
            # b on variables (p,y) at P = {0, -e_j}: 4 variables; shifted copy at {e_j, 0}
            src = [2 * idx[(0, 0, 0)], 2 * idx[(0, 0, 0)] + 1, 2 * idx[mej], 2 * idx[mej] + 1]
            dst = [2 * idx[ej], 2 * idx[ej] + 1, 2 * idx[(0, 0, 0)], 2 * idx[(0, 0, 0)] + 1]
            for e4 in monomials(4, self.D):
                if sum(e4) == 0:
                    continue
                es, ed = [0] * 14, [0] * 14
                for k in range(4):
                    es[src[k]] += e4[k]
                    ed[dst[k]] += e4[k]
                g = np.zeros(self.n, dtype=np.int64)
                for r in range(self.npat):
                    g[r * self.nmon + mi[tuple(ed)]] += 1
                    g[r * self.nmon + mi[tuple(es)]] -= 1
                if np.any(g):
                    gens.append(g)
        return gens

    def vec_from_density(self, dens):
        v = [Fraction(0)] * self.n
        mi = {e: i for i, e in enumerate(self.mons)}
        for r in range(self.npat):
            for e, c in dens.items():
                v[r * self.nmon + mi[e]] += Fraction(c)
        return v


def energy3d_density(coupling):
    """y_0^2 + p_0^2 - coupling * y_0 * sum_{o != 0} p_o, in star variables"""
    d = {ex(14, e1=2): 1, ex(14, e0=2): 1}
    for i in range(1, 7):
        e = [0] * 14
        e[1] += 1
        e[2 * i] += 1
        d[tuple(e)] = d.get(tuple(e), 0) - Fraction(coupling)
    return d


# ============================================================ helpers
def exact_rows_dot(rows, v):
    """exact dot of integer rows with a Fraction vector: rows @ (den * v) in int64 when the bound
    max|row| * sum|den * v| < 2^62 holds (asserted), else with Python integers; divided by den"""
    den = 1
    for c in v:
        if c:
            den = den * Fraction(c).denominator // math.gcd(den, Fraction(c).denominator)
    iv = np.array([int(Fraction(c) * den) for c in v], dtype=object)
    nz = np.nonzero(iv != 0)[0]
    rows = np.asarray(rows)
    if rows.ndim == 1:
        rows = rows[None, :]
    sub = rows[:, nz]
    ivn = iv[nz]
    bound = (int(np.abs(sub).max()) if sub.size else 0) * int(sum(abs(int(x)) for x in ivn))
    if bound < 2 ** 62:
        vals = sub.astype(np.int64) @ np.array([int(x) for x in ivn], dtype=np.int64)
        vals = [int(x) for x in vals]
    else:
        vals = [sum(int(a) * int(b) for a, b in zip(r, ivn)) for r in sub]
    return [Fraction(x, den) for x in vals]


def nontrivial_witness(cls, v, rng, tries=400):
    """two configurations with different Phi/N (exact), or None"""
    seen = None
    for chunk in cls.sample(rng, tries):
        P, Y = chunk
        N = int(np.prod(P.shape[1:]))
        vals = cls.phi(P, Y, v)
        for i, val in enumerate(vals):
            r = val / N
            if seen is None:
                seen = r
            elif r != seen:
                return True
    # also uniform states
    return False


def run_class(cls, seed, vec_checks=(), prime=P1_PRIME, max_chunks=40):
    """feed equations until certified / stall / cap.  vec_checks: list of (name, vector) to be
    verified in ker E exactly on every equation used."""
    rng = np.random.default_rng(seed)
    t0 = time.time()
    el = Elim(cls.n, prime)
    T = cls.tgen()
    elT = Elim(cls.n, prime)
    elT.add(np.array(T))
    rT = elT.rank
    Tm = np.mod(np.array(T, dtype=np.int64), prime).astype(np.float64).T  # n x |T|
    chunk = max(256, -(-cls.n // 4))
    stall, used, maxval = 0, 0, 0
    c3_ok, vec_ok = True, {name: True for name, _ in vec_checks}
    sample_rows = []
    certified = False
    for ci in range(max_chunks):
        rows = []
        for P, Y in cls.sample(rng, chunk):
            r, mv = cls.rows(P, Y)
            rows.append(r)
            maxval = max(maxval, mv)
        rows = np.vstack(rows)
        used += rows.shape[0]
        # C3: T in ker E, mod p on all rows, exactly on a sample
        Rm = np.mod(rows, prime).astype(np.float64)
        if np.any(mod_matmul(Rm, Tm, prime)):
            c3_ok = False
        if len(sample_rows) < 200:
            sample_rows.extend(rows[:200 - len(sample_rows)])
        for name, v in vec_checks:
            if any(x != 0 for x in exact_rows_dot(rows, v)):
                vec_ok[name] = False
        added = el.add(rows)
        if cls.n - el.rank == rT:
            certified = True
            break
        stall = stall + 1 if added == 0 else 0
        if stall >= 3:
            break
    # exact C3 on the sample
    for g in T:
        gi = [int(x) for x in g]
        for r in sample_rows:
            if sum(int(a) * b for a, b in zip(r, gi) if b) != 0:
                c3_ok = False
                break
    rec = {"rule": cls.kind, "label": cls.label, "n": cls.n, "rank_E": el.rank, "rank_T": rT,
           "excess": cls.n - el.rank - rT, "certified": certified, "equations": used,
           "max_abs_value": maxval, "prime": prime, "seconds": round(time.time() - t0, 1),
           "c3_T_in_kerE": c3_ok, "c3_exact_sample": len(sample_rows)}
    if hasattr(cls, "m"):
        rec.update({"family": "G1" if cls.mu == 1 else ("G3" if cls.D == 0 else "G2"),
                    "m": cls.m, "D": cls.D, "mu": cls.mu})
    else:
        rec.update({"family": "P3r" if cls.resid else "P3", "D": cls.D})
    print(f"CLASS {cls.label}: n={cls.n} rank_E={el.rank} rank_T={rT} excess={rec['excess']} "
          f"certified={certified} eqs={used} max|v|={maxval} C3={c3_ok} {rec['seconds']}s", flush=True)
    return rec, vec_ok, el


def examine_excess(cls, el, seed):
    """lift the mod-p nullspace by rational reconstruction; check survivors exactly on fresh
    configurations and for nontriviality"""
    rng = np.random.default_rng(seed + 7)
    out = []
    for v in el.nullspace()[:50]:
        q = [rat_rec(int(x), el.p) for x in v]
        if any(x is None for x in q):
            out.append({"lift": False})
            continue
        ok = True
        for P, Y in cls.sample(rng, 200):
            r, _ = cls.rows(P, Y)
            if any(x != 0 for x in exact_rows_dot(r, q)):
                ok = False
                break
        nt = nontrivial_witness(cls, q, rng) if ok else None
        out.append({"lift": True, "exact_on_fresh": ok, "nontrivial": nt,
                    "support": [j for j, x in enumerate(q) if x][:20]})
    return out


# ============================================================ controls
def control_K1():
    rng = np.random.default_rng(101)
    ok, maxabs = True, 0
    for kind in ("ax", "fd", "bd"):
        for _ in range(20):
            L = int(rng.integers(2, 9))
            p = rng.integers(-6, 7, size=L)
            y = rng.integers(-6, 7, size=L)
            if kind == "ax":
                emb = lambda u: u[:, None, None].copy()
            elif kind == "fd":
                emb = lambda u: u[(np.arange(L)[:, None] + np.arange(L)[None, :]) % L][:, :, None].copy()
            else:
                ii = np.arange(L)
                emb = lambda u: u[(ii[:, None, None] + ii[None, :, None] + ii[None, None, :]) % L].copy()
            P3, Y3 = emb(p), emb(y)
            Xp, X = np.mod(C0 + P3, Q), np.mod(C0 + Y3, Q)
            pp, yy = p.copy(), y.copy()
            for t in range(30):
                pp, yy = step1d(pp, yy, kind)
                P3, Y3 = step3(P3, Y3)
                Xp, X = step3q(Xp, X)
                maxabs = max(maxabs, int(np.abs(yy).max()))
                if not (np.array_equal(Y3, emb(yy)) and np.array_equal(P3, emb(pp))):
                    ok = False
                if maxabs < C0 and not np.array_equal(X, np.mod(C0 + Y3, Q)):
                    ok = False
    control("K1", ok and maxabs < C0, f"ax/fd/bd x 20 states x 30 steps, 3D RZ = reduced 1D, Q = 2^15 + RZ; "
                                       f"max|y| = {maxabs}")


def control_K2():
    ok = True
    for s in range(-300, 301):
        fr = Fraction(s, 3)
        near = math.floor(fr + Fraction(1, 2))
        if int(G(np.int64(s))) != near:
            ok = False
    rng = np.random.default_rng(102)
    for _ in range(50):
        for kind in ("ax", "fd", "bd"):
            L = int(rng.integers(1, 10))
            p, y = rng.integers(-50, 51, L), rng.integers(-50, 51, L)
            a, b = step1d(p, y, kind)
            c, d = back1d(a, b, kind)
            ok &= np.array_equal(c, p) and np.array_equal(d, y)
        sh = tuple(int(x) for x in rng.integers(1, 5, 3))
        p, y = rng.integers(-50, 51, sh), rng.integers(-50, 51, sh)
        a, b = step3(p, y)
        c, d = back3(a, b)
        ok &= np.array_equal(c, p) and np.array_equal(d, y)
    control("K2", ok, "G = nearest-integer rounding of s/3 on [-300, 300]; inverse map undoes F (1D x3, 3D), 50 states")


def bd_invariant(cls):
    """sum_k phi(u_{k+1} - p_k), in Q(m, D, mu) coordinates (cells 1,2 of the window: vars 0..3 =
    p_k, u_k, p_{k+1}, u_{k+1})"""
    nv = cls.nvar
    if cls.D >= 2:
        # (u_{k+1} - p_k)^2 = u_{k+1}^2 - 2 u_{k+1} p_k + p_k^2
        e_u2 = [0] * nv; e_u2[3] = 2
        e_p2 = [0] * nv; e_p2[0] = 2
        e_up = [0] * nv; e_up[3] = 1; e_up[0] = 1
        return cls.vec_from_density({tuple(e_u2): 1, tuple(e_p2): 1, tuple(e_up): -2}), "sum (u_{k+1}-p_k)^2"
    mu = cls.mu
    zero = tuple([0] * nv)
    return cls.vec_from_density(lambda r: {zero: 1} if (r[3] - r[0]) % mu == 1 % mu else {}), \
        f"sum [u_(k+1) - p_k = 1 mod {mu}]"


def lin_energy_1d(cls):
    """plane-wave linear energy, coupling 1/3: sum y_k^2 + p_k^2 - (1/3) y_k (sum of reduced neighbours of p)."""
    nv = cls.nvar
    w = {"ax": (1, 4), "fd": (2, 2), "bd": (3, 0)}[cls.kind]  # (weight of k+-1, weight of k)
    d = {}

    def add(e, c):
        d[tuple(e)] = d.get(tuple(e), 0) + Fraction(c)
    e = [0] * nv; e[1] = 2; add(e, 1)
    e = [0] * nv; e[0] = 2; add(e, 1)
    e = [0] * nv; e[1] = 1; e[0] = 1; add(e, Fraction(-w[1], 3))
    # y_k p_{k+1} and y_{k+1} p_k each with weight -(w0/3) (the bond carries both k->k+1 and k+1->k)
    e = [0] * nv; e[1] = 1; e[2] = 1; add(e, Fraction(-w[0], 3))
    e = [0] * nv; e[3] = 1; e[0] = 1; add(e, Fraction(-w[0], 3))
    return cls.vec_from_density(d)


def delta_witness(cls, v, rng, tries=400):
    for P, Y in cls.sample(rng, tries):
        r, _ = cls.rows(P, Y)
        vals = exact_rows_dot(r, v)
        for i, x in enumerate(vals):
            if x != 0:
                return {"shape": list(P.shape[1:]), "p": P[i].tolist(), "y": Y[i].tolist(), "dPhi": str(x)}
    return None


# ============================================================ grid
GRID = {
    "G1": [(2, 2, 1), (3, 2, 1), (4, 2, 1), (2, 4, 1), (3, 4, 1), (4, 4, 1)],
    "G2": [(2, 2, 3), (2, 3, 3), (2, 4, 3)],
    "G3": [(2, 0, 2), (2, 0, 3), (2, 0, 4), (2, 0, 5), (2, 0, 6), (2, 0, 8), (2, 0, 9),
           (3, 0, 2), (3, 0, 3), (3, 0, 4), (4, 0, 2), (4, 0, 3), (5, 0, 2)],
}


PARTS = {
    "A": [("1D", fam, t) for fam in ("G1", "G2") for t in GRID[fam]],
    "B": [("1D", "G3", t) for t in GRID["G3"][:7]],
    "C": [("1D", "G3", t) for t in GRID["G3"][7:]],
    "D": [("3D", None, t) for t in (("LIN", 2, False), ("RZ", 2, False), ("RZ", 3, False), ("RZ", 2, True))],
    # amendment A01: the same classes, seeds and equations, with the enlarged trivial space T3'
    "D2": [("3D", None, t + (True,)) for t in (("LIN", 2, False), ("RZ", 2, False), ("RZ", 3, False),
                                               ("RZ", 2, True))],
}
DECISION_PARTS = ("A", "B", "C", "D2")


def seed_of(label):
    return 1000 + sum((i + 1) * ord(ch) for i, ch in enumerate(label)) % 100000


def do_1d(m, D, mu, kind):
    cls = Class1D(kind, m, D, mu)
    seed = seed_of(cls.label)
    vec_checks = []
    if kind == "bd":
        v, vname = bd_invariant(cls)
        vec_checks = [(vname, v)]
    rec, vec_ok, el = run_class(cls, seed, vec_checks)
    if kind == "bd":
        nt = nontrivial_witness(cls, v, np.random.default_rng(seed + 3))
        rec["p1"] = {"invariant": vname, "in_kerE_exact": vec_ok[vname], "nontrivial": nt,
                     "pass": (not rec["certified"]) and vec_ok[vname] and nt}
        T = cls.tgen()
        t = [Fraction(int(x)) for x in T[1]]
        triv = not nontrivial_witness(cls, t, np.random.default_rng(seed + 4), tries=200)
        vt = [a + b for a, b in zip(v, t)]
        ntt = nontrivial_witness(cls, vt, np.random.default_rng(seed + 5), tries=200)
        rec["c2"] = {"coboundary_trivial": triv, "invariant_plus_coboundary_nontrivial": ntt,
                     "pass": triv and ntt}
    else:
        rng = np.random.default_rng(seed + 3)
        wits = {}
        vb, _ = bd_invariant(cls)
        wits["bd invariant"] = delta_witness(cls, vb, rng)
        if D >= 2:
            wits["linear energy 1/3"] = delta_witness(cls, lin_energy_1d(cls), rng)
        rec["c1"] = {"witnesses": wits, "pass": all(w is not None for w in wits.values())}
        if not rec["certified"]:
            rec2, _, _ = run_class(cls, seed, (), prime=P2_PRIME)
            rec["second_prime"] = {k: rec2[k] for k in ("rank_E", "rank_T", "excess", "certified", "prime")}
            if rec2["certified"]:
                rec["certified"] = True
                rec["certified_by"] = P2_PRIME
            else:
                rec["excess_examined"] = examine_excess(cls, el, seed)
    return rec


def do_3d(rule, D, resid, full_T=False):
    cls = Class3D(rule, D, resid, full_T)
    seed = seed_of(cls.label)
    vec_checks = []
    if rule == "LIN":
        vE = cls.vec_from_density(energy3d_density(1))
        vec_checks = [("y.y + p.p - y.Sp", vE)]
    rec, vec_ok, el = run_class(cls, seed, vec_checks)
    rec["T"] = "T3' (A01)" if full_T else "T (PREREG)"
    if rule == "LIN":
        nt = nontrivial_witness(cls, vE, np.random.default_rng(seed + 3))
        rec["p2"] = {"in_kerE_exact": vec_ok["y.y + p.p - y.Sp"], "nontrivial": nt,
                     "pass": (not rec["certified"]) and vec_ok["y.y + p.p - y.Sp"] and nt}
    else:
        w = delta_witness(cls, cls.vec_from_density(energy3d_density(Fraction(1, 3))),
                          np.random.default_rng(seed + 3))
        rec["c1"] = {"witnesses": {"linear-wave energy 1/3": w}, "pass": w is not None}
        if not rec["certified"]:
            rec2, _, _ = run_class(cls, seed, (), prime=P2_PRIME)
            rec["second_prime"] = {k: rec2[k] for k in ("rank_E", "rank_T", "excess", "certified", "prime")}
            if rec2["certified"]:
                rec["certified"] = True
                rec["certified_by"] = P2_PRIME
            else:
                rec["excess_examined"] = examine_excess(cls, el, seed)
    return rec


def render():
    parts = {}
    for k in sorted(PARTS):
        with open(os.path.join(HERE, f"results-{k}.json")) as fh:
            parts[k] = json.load(fh)
    controls = [c for k in sorted(parts) for c in parts[k]["controls"]]
    classes = [c for k in DECISION_PARTS for c in parts[k]["classes"]]
    prereg_D = parts["D"]["classes"]
    bd = [c for c in classes if c["rule"] == "bd"]
    lin3 = [c for c in classes if c["rule"] == "LIN"]
    rounded = [c for c in classes if c["rule"] in ("ax", "fd", "RZ")]
    n1d = sum(len(v) for v in GRID.values())
    expected = 3 * n1d + 4
    new = [
        {"id": "P1", "pass": len(bd) == n1d and all(c["p1"]["pass"] for c in bd),
         "info": f"bd (linear) reduction, {len(bd)} classes: none certified; invariant in ker E exactly and "
                 f"nontrivial in each"},
        {"id": "P2", "pass": len(lin3) == 1 and lin3[0]["p2"]["pass"],
         "info": "3D linear rule y' = Sy - p in P3(2): not certified; y.y + p.p - y.Sp in ker E exactly and nontrivial"},
        {"id": "C1", "pass": all(c["c1"]["pass"] for c in rounded),
         "info": "every rounded class: the bd invariant (1D) and the 1/3-coupling linear energy (1D with D >= 2, "
                 "and 3D) have exact witnesses with dPhi != 0"},
        {"id": "C2", "pass": all(c["c2"]["pass"] for c in bd),
         "info": "bd classes: planted coboundary classified trivial; invariant + coboundary nontrivial"},
        {"id": "C3", "pass": all(c["c3_T_in_kerE"] for c in classes),
         "info": "every T generator annihilates every equation mod p, and a sample exactly"},
        {"id": "COVER", "pass": len(classes) == expected,
         "info": f"{len(classes)} of {expected} preregistered classes present"},
    ]
    controls += new
    for c in prereg_D:
        print(f"RUN D (preregistered T): {c['label']} certified={c['certified']} excess={c['excess']}")
    for c in controls:
        print(f"CONTROL {c['id']}: {'PASS' if c['pass'] else 'FAIL'}  {c['info']}")
    green = all(c["pass"] for c in controls)
    cert = [c["label"] for c in rounded if c["certified"]]
    uncert = [(c["label"], c["excess"]) for c in rounded if not c["certified"]]
    cand = [c["label"] for c in rounded if any(e.get("exact_on_fresh") and e.get("nontrivial")
                                                for e in c.get("excess_examined", []))]
    if not green:
        verdict = "VOID: a control failed; no verdict."
    else:
        lines = []
        if cert:
            lines.append(f"Decision (ii) met for {len(cert)} of {len(rounded)} rounded classes (certified: every "
                         f"conserved additive quantity in the class is trivial on its periodic configurations): "
                         + ", ".join(cert) + ".")
        if uncert:
            lines.append("Not certified (excess): " + ", ".join(f"{l} ({e})" for l, e in uncert) + ".")
        else:
            lines.append("No rounded class is uncertified.")
        if cand:
            lines.append("Candidates surviving the exact check: " + ", ".join(cand) + ".")
        else:
            lines.append("Decision (i) not met: no candidate conserved quantity in any rounded class.")
        if not cert:
            lines.append("Decision (ii) not met; scoped recorded negative.")
        verdict = " ".join(lines)
    print("VERDICT", verdict)
    out = {"snapshot_D": "b9168ef0408b5f55b935a4df17cb0841877e221a", "controls": controls,
           "classes": classes, "classes_run_D_prereg_T": prereg_D, "controls_green": green, "verdict": verdict,
           "cpu_seconds_by_part": {k: parts[k]["cpu_seconds"] for k in parts}}
    with open(os.path.join(HERE, "results.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    return 0 if green else 1


def main():
    if "--render" in sys.argv:
        return render()
    if "--only" in sys.argv:
        lab = sys.argv[sys.argv.index("--only") + 1]
        for part, items in PARTS.items():
            for dim, fam, t in items:
                if dim == "1D":
                    for kind in ("bd", "ax", "fd"):
                        if Class1D(kind, *t).label == lab:
                            print(json.dumps(do_1d(*t, kind), default=str)[:3000])
                elif Class3D(*t).label == lab:
                    print(json.dumps(do_3d(*t), default=str)[:3000])
                    break
        return 0
    part = sys.argv[sys.argv.index("--part") + 1]
    t_start = time.process_time()
    if part == "A":
        control_K1()
        control_K2()
    classes = []
    for dim, fam, t in PARTS[part]:
        if dim == "1D":
            for kind in ("bd", "ax", "fd"):
                classes.append(do_1d(*t, kind))
        else:
            classes.append(do_3d(*t))
    out = {"part": part, "controls": CONTROLS, "classes": classes,
           "cpu_seconds": round(time.process_time() - t_start, 1)}
    with open(os.path.join(HERE, f"results-{part}.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    ok = all(c["pass"] for c in CONTROLS)
    print(f"PART {part} done, cpu {out['cpu_seconds']} s, controls in part green: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
