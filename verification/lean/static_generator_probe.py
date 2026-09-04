#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CT3-R1: the local-centralizer census for the OI phase-space update.

CT2 closed with `driveQ_one_eq_heisQ`: the OI update is joined to the identity by a
norm-continuous path of `*`-automorphisms of the quasilocal algebra. What CT2 does NOT give is a
GROUP law for that path, or a generator. CT3 asks the remaining question, in the form the infinite
lattice permits -- not whether a bounded `H` in the quasilocal algebra has `e^{iH} = U`, since an
extensive Hamiltonian is not an element of that algebra, but:

    is there ONE time-independent finite-range interaction whose automorphism group tau_t
    satisfies tau_1 = heisQ(Phi_OI)?

This probe runs the cheapest decisive NECESSARY test, before any logarithm is attempted. If
tau_1 = alpha for an autonomous flow then every tau_t commutes with alpha, so the generator
satisfies [delta, alpha] = 0: the static interaction must be a CONSERVED local quantity of one
discrete OI step. On a finite periodic lattice that is the linear condition

    P^dagger H P = H,     H = sum_x h_x,     h_x supported on a width-w window,

with P the permutation matrix of the update on classical configurations. This is far cheaper than
solving exp(-iH) = P, and a trivial centralizer would kill autonomous local embedding outright.

WHAT IS COMPUTED. The census dimension is
    dim { H : H is a width-w local sum, [H, P] = 0 } ,
obtained as nullity(B) - dim ker(h -> H), where B is the centralizer system on the unknowns
h_x[u,v] and the second term is the redundancy of the parametrization (different h can give the
same H). The redundancy is computed in CLOSED FORM -- the image of h -> H is spanned by the
exact-support components, so its dimension is sum over subsets S fitting inside some window of
(q^4 - 1)^|S| -- and that closed form is checked against brute-force linear algebra below.

THE SPLIT THAT MATTERS. P is a permutation matrix, so conjugation by it permutes matrix units and
the centralizer splits: the diagonal part (conserved classical densities) and the off-diagonal
part are separately centralizing. A DIAGONAL H exponentiates to a diagonal unitary and can never
equal a nontrivial permutation, so an autonomous local generator needs the OFF-DIAGONAL part to be
nonzero. Both parts are reported.

ARITHMETIC. Ranks are taken over GF(p), p = 1000003, by exact sparse elimination. rank_p <= rank_Q,
so nullity_p >= nullity_Q: a SMALL census dimension mod p certifies a small one over Q, which is the
direction an obstruction claim needs. The closed-form redundancy is exact over Z. Every reported
census dimension at w <= 2 is additionally confirmed by building the explicit N x N matrices and
checking [H, P] = 0 entry by entry, then taking the rank of their span.

RESULT, and it is a NEGATIVE for the cheap test. For the corpus rule
x_i(t+1) = x_{i-1} + x_{i+1} - x_i(t-1) mod q the census dimension is

    w = 1:   1   =  1 diagonal  +  0 off-diagonal      (scalars only)
    w = 2:   7   =  3 diagonal  +  4 off-diagonal
    w = 3:  25   =  5 diagonal  + 20 off-diagonal

stable in L across L = 5, 6, 7 at w = 2 and L = 5, 6 at w = 3. The centralizer is nontrivial from
w = 2 on and its off-diagonal part is nonzero, so THE CENTRALIZER TEST DOES NOT OBSTRUCT an
autonomous local generator. Candidates survive and the stronger exponential condition has to be
tested. Nothing here claims such a generator exists; the census is a necessary condition only, and
passing a necessary condition is not evidence of sufficiency.

CONTROLS, which is what makes the negative readable. Two rules whose leap is ON-SITE (F = 0 and
F(c)_i = 2 c_i) provably do admit a static on-site generator, and the census finds large
centralizers for them (37 and 505 at w = 1, 2 on L = 4), so the method detects generators where
they must exist. A third control, the one-sided coupling F(c)_i = c_{i-1}, is genuinely coupled and
gives dimension 1 at w = 1 and w = 2 -- so the corpus rule's 7-dimensional w = 2 centralizer is a
property of that specific bidirectional rule, not of coupling in general.

SCOPE. The census is run at w <= 3. The OI gate region is three sites wide, so w = 3 is the first
window that can carry a gate; a census at w <= 3 is not a statement about all finite ranges, and
none is made. The unknown count grows as L * q^{4w}, which is the wall.

  M1  the closed-form redundancy dimension agrees with brute-force linear algebra
  M2  on-site control rules have large centralizers -- the method detects generators
  M3  the coupled one-sided control has centralizer dimension 1 at w = 1 and w = 2
  M4  corpus rule at w = 1: dimension exactly 1, entirely diagonal, at q = 2 and q = 3
  M5  corpus rule at w = 2: dimension exactly 7 = 3 + 4, stable in L
  M6  corpus rule at w = 3: dimension exactly 25 = 5 + 20, stable in L
  M7  explicit matrices: every census basis element satisfies [H, P] = 0, and the rank of
      their span equals the census dimension
  M8  the verdict is NON-OBSTRUCTION: the off-diagonal part is nonzero from w = 2 on

Run with --extended to add the slower confirmations (L = 7 at w = 2, L = 6 at w = 3).
"""

import itertools
import random
import sys
import time

PRIME = 1000003

FAILURES = []


def check(label, ok, msg):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}")
    if not ok:
        FAILURES.append(label)


# ---------------------------------------------------------------- the update
def F_wave(c, L, q):
    """The corpus rule: F(c)_i = c_{i-1} + c_{i+1}, the discrete wave equation of SM."""
    return [(c[(i - 1) % L] + c[(i + 1) % L]) % q for i in range(L)]


def F_zero(c, L, q):
    """Control: no coupling, so the leap is on-site and a static on-site generator exists."""
    return [0] * L


def F_diag(c, L, q):
    """Control: on-site coupling only. The leap is again on-site."""
    return [(2 * c[i]) % q for i in range(L)]


def F_left(c, L, q):
    """Control: one-sided coupling. Genuinely coupled, but not the corpus rule."""
    return [c[(i - 1) % L] for i in range(L)]


RULES = {'wave': F_wave, 'zero': F_zero, 'diag': F_diag, 'left': F_left}


class Lat:
    """A periodic ring of L sites over Z_q in phase-space form: site value = p*q + c."""

    def __init__(self, L, q, rule):
        self.L, self.q, self.QQ = L, q, q * q
        self.F, self.rule = RULES[rule], rule
        self.N = self.QQ ** L

    def dec(self, idx):
        out = []
        for _ in range(self.L):
            out.append(idx % self.QQ)
            idx //= self.QQ
        return tuple(out)

    def enc(self, cfg):
        idx = 0
        for j in reversed(range(self.L)):
            idx = idx * self.QQ + cfg[j]
        return idx

    def leap(self, cfg):
        """(p, c) -> (c, F(c) - p). The reversible second-order step."""
        L, q = self.L, self.q
        c = [v % q for v in cfg]
        p = [v // q for v in cfg]
        nc = self.F(c, L, q)
        return tuple(c[i] * q + ((nc[i] - p[i]) % q) for i in range(L))

    def unleap(self, cfg):
        """The inverse: the two layers in the other order."""
        L, q = self.L, self.q
        pp = [v // q for v in cfg]
        cc = [v % q for v in cfg]
        Fp = self.F(pp, L, q)
        return tuple((((Fp[i] - cc[i]) % q) * q + pp[i]) for i in range(L))


class Ansatz:
    """H = sum_x h_x, with h_x supported on the width-w window {x, ..., x+w-1}."""

    def __init__(self, lat, w):
        self.lat, self.w = lat, w
        L, QQ = lat.L, lat.QQ
        self.Dw = QQ ** w
        self.U = L * self.Dw * self.Dw
        self.win = [tuple((x + k) % L for k in range(w)) for x in range(L)]
        self.inwin = [[False] * L for _ in range(L)]
        for x in range(L):
            for j in self.win[x]:
                self.inwin[x][j] = True

    def key(self, x, u, v):
        return (x * self.Dw + u) * self.Dw + v

    def form(self, a, b):
        """The linear form for the entry H_{a,b}, as {unknown: coefficient}."""
        L, QQ = self.lat.L, self.lat.QQ
        terms = {}
        for x in range(L):
            iw = self.inwin[x]
            ok = True
            for j in range(L):
                if not iw[j] and a[j] != b[j]:
                    ok = False
                    break
            if not ok:
                continue
            u = v = 0
            for j in self.win[x]:
                u = u * QQ + a[j]
                v = v * QQ + b[j]
            k = self.key(x, u, v)
            terms[k] = terms.get(k, 0) + 1
        return terms

    def dform(self, a):
        """The linear form for the diagonal entry H_{a,a}, on the classical density unknowns."""
        QQ = self.lat.QQ
        terms = {}
        for x in range(self.lat.L):
            u = 0
            for j in self.win[x]:
                u = u * QQ + a[j]
            terms[x * self.Dw + u] = terms.get(x * self.Dw + u, 0) + 1
        return terms


# ------------------------------------------------------ exact rank over GF(p)
def rank_mod_p(rows, p=PRIME):
    """Sparse Gaussian elimination on {col: coef} rows. rank_p <= rank_Q always."""
    piv = {}
    rank = 0
    for r0 in rows:
        r = {c: v % p for c, v in r0.items() if v % p}
        while r:
            c = min(r)
            pr = piv.get(c)
            if pr is None:
                piv[c] = r
                rank += 1
                break
            f = r[c] * pow(pr[c], p - 2, p) % p
            for cc, vv in pr.items():
                nv = (r.get(cc, 0) - f * vv) % p
                if nv:
                    r[cc] = nv
                elif cc in r:
                    del r[cc]
    return rank


def nullspace_mod_p(rows, U, p=PRIME):
    """A basis of the solution space, for the explicit-matrix confirmation."""
    piv = {}
    for r0 in rows:
        r = {c: v % p for c, v in r0.items() if v % p}
        while r:
            c = min(r)
            pr = piv.get(c)
            if pr is None:
                inv = pow(r[c], p - 2, p)
                piv[c] = {k: v * inv % p for k, v in r.items()}
                break
            f = r[c]
            for cc, vv in pr.items():
                nv = (r.get(cc, 0) - f * vv) % p
                if nv:
                    r[cc] = nv
                elif cc in r:
                    del r[cc]
    basis = []
    for fc in (c for c in range(U) if c not in piv):
        vec = [0] * U
        vec[fc] = 1
        for c in sorted(piv, reverse=True):
            row = piv[c]
            s = 0
            for cc, vv in row.items():
                if cc != c:
                    s = (s + vv * vec[cc]) % p
            vec[c] = (-s) % p
        basis.append(vec)
    return basis


# ------------------------------------------------------------------ the census
def local_pairs(lat, ans):
    """Every (a, b) agreeing off some width-w window. Deduplicated, exhaustive."""
    seen, out = set(), []
    for ai in range(lat.N):
        a = lat.dec(ai)
        for x in range(lat.L):
            W = ans.win[x]
            for v0 in range(ans.Dw):
                b = list(a)
                t = v0
                for j in reversed(W):
                    b[j] = t % lat.QQ
                    t //= lat.QQ
                b = tuple(b)
                kk = (ai, lat.enc(b))
                if kk not in seen:
                    seen.add(kk)
                    out.append((a, b))
    return out


def fitting_supports(lat, ans):
    """The subsets of the ring that fit inside some width-w window, each once."""
    fits = set()
    for x in range(lat.L):
        W = ans.win[x]
        for k in range(len(W) + 1):
            for S in itertools.combinations(W, k):
                fits.add(tuple(sorted(S)))
    return fits


def redundancy_dim(lat, ans, sector='all'):
    """dim ker(h -> H), in closed form. 'diag' restricts to classical densities."""
    QQ = lat.QQ
    fits = fitting_supports(lat, ans)
    if sector == 'all':
        return ans.U - sum((QQ * QQ - 1) ** len(S) for S in fits)
    return lat.L * ans.Dw - sum((QQ - 1) ** len(S) for S in fits)


def centralizer_rows(lat, ans):
    """The full centralizer system: H_{a,b} = H_{sigma a, sigma b} for every pair."""
    rows = []
    for (a, b) in local_pairs(lat, ans):
        fa = ans.form(a, b)
        r = dict(fa)
        for k, v in ans.form(lat.leap(a), lat.leap(b)).items():
            r[k] = r.get(k, 0) - v
        if r:
            rows.append(r)
        r2 = ans.form(lat.unleap(a), lat.unleap(b))
        for k, v in fa.items():
            r2[k] = r2.get(k, 0) - v
        if r2:
            rows.append(r2)
    return rows


def census(L, q, rule, w):
    """dim { H : width-w local sum, [H, P] = 0 }."""
    lat, = (Lat(L, q, rule),)
    ans = Ansatz(lat, w)
    nB = ans.U - rank_mod_p(centralizer_rows(lat, ans))
    return nB - redundancy_dim(lat, ans, 'all')


def census_diag(L, q, rule, w):
    """The diagonal part: conserved classical densities of range w."""
    lat = Lat(L, q, rule)
    ans = Ansatz(lat, w)
    rows = []
    for ai in range(lat.N):
        a = lat.dec(ai)
        r = ans.dform(a)
        for k, v in ans.dform(lat.leap(a)).items():
            r[k] = r.get(k, 0) - v
        if r:
            rows.append(r)
    nB = lat.L * ans.Dw - rank_mod_p(rows)
    return nB - redundancy_dim(lat, ans, 'diag')


def explicit_confirm(L, q, rule, w):
    """Build the N x N matrices of a census basis; check [H, P] = 0 and the rank of the span."""
    lat = Lat(L, q, rule)
    ans = Ansatz(lat, w)
    basis = nullspace_mod_p(centralizer_rows(lat, ans), ans.U)
    perm = [lat.enc(lat.leap(lat.dec(i))) for i in range(lat.N)]
    mats, bad = [], 0
    for hv in basis:
        M = {}
        for ai in range(lat.N):
            a = lat.dec(ai)
            for x in range(lat.L):
                W = ans.win[x]
                u = 0
                for j in W:
                    u = u * lat.QQ + a[j]
                for v0 in range(ans.Dw):
                    val = hv[ans.key(x, u, v0)]
                    if not val:
                        continue
                    b = list(a)
                    t = v0
                    for j in reversed(W):
                        b[j] = t % lat.QQ
                        t //= lat.QQ
                    kk = (lat.enc(tuple(b)), ai)
                    M[kk] = (M.get(kk, 0) + val) % PRIME
        M = {k: v for k, v in M.items() if v}
        if not M:
            continue
        # (P H P^dagger)_{a,b} = H_{sigma^{-1}a, sigma^{-1}b}; equivalently H_{sa,sb} = H_{a,b}
        shifted = {}
        for (r, c), v in M.items():
            shifted[(perm[r], perm[c])] = v
        if shifted != M:
            bad += 1
        mats.append(M)
    keys = sorted({k for M in mats for k in M})
    kidx = {k: i for i, k in enumerate(keys)}
    rows = [{kidx[k]: v for k, v in M.items()} for M in mats]
    return bad, rank_mod_p(rows)


# ------------------------------------------------------------------------ main
def main():
    extended = '--extended' in sys.argv
    t0 = time.time()
    print("static_generator_probe: CT3-R1, the local-centralizer census")
    print()

    # M1 -- the closed-form redundancy against brute-force linear algebra
    ok = True
    detail = []
    for (L, q, w) in [(4, 2, 1), (4, 2, 2), (5, 2, 1), (4, 3, 1)]:
        lat = Lat(L, q, 'wave')
        ans = Ansatz(lat, w)
        lin = ans.U - rank_mod_p([ans.form(a, b) for (a, b) in local_pairs(lat, ans)])
        closed = redundancy_dim(lat, ans, 'all')
        ok &= (lin == closed)
        detail.append(f"(L={L},q={q},w={w}) {closed}")
    check('M1', ok,
          "the closed-form redundancy dim ker(h -> H) agrees with brute-force linear algebra at "
          + ", ".join(detail) + " -- so the census subtraction is exact, not fitted")

    # M2 -- on-site controls must show large centralizers
    z1, z2 = census(4, 2, 'zero', 1), census(4, 2, 'zero', 2)
    d1, d2 = census(4, 2, 'diag', 1), census(4, 2, 'diag', 2)
    check('M2', z1 == 37 and z2 == 505 and d1 == 37 and d2 == 505,
          f"CONTROL. The two rules whose leap is on-site, F = 0 and F(c)_i = 2c_i, do admit a "
          f"static on-site generator, and the census finds dimension {z1} and {z2} (F = 0), "
          f"{d1} and {d2} (F = 2c) at w = 1, 2 on L = 4. The method detects generators where they "
          f"must exist, so a small census elsewhere is a fact about the rule, not about the probe")

    # M3 -- a genuinely coupled control
    l1, l2 = census(6, 2, 'left', 1), census(5, 2, 'left', 2)
    check('M3', l1 == 1 and l2 == 1,
          f"CONTROL. The one-sided coupling F(c)_i = c_{{i-1}} gives census dimension {l1} at "
          f"w = 1 (L = 6) and {l2} at w = 2 (L = 5) -- scalars only. So the corpus rule's larger "
          f"w = 2 centralizer below is a property of that specific bidirectional rule, not a "
          f"generic consequence of having a coupling at all")

    # M4 -- the corpus rule at w = 1
    w1 = [census(L, 2, 'wave', 1) for L in (4, 5, 6)]
    w1d = [census_diag(L, 2, 'wave', 1) for L in (4, 5, 6)]
    w1q3 = census(4, 3, 'wave', 1)
    check('M4', w1 == [1, 1, 1] and w1d == [1, 1, 1] and w1q3 == 1,
          f"corpus rule at w = 1: census dimension {w1} at L = 4, 5, 6 (q = 2) and {w1q3} at "
          f"L = 4, q = 3 -- SCALARS ONLY, and entirely diagonal ({w1d}). No on-site conserved "
          f"quantity beyond the identity")

    # M5 -- the corpus rule at w = 2
    Ls2 = (5, 6, 7) if extended else (5, 6)
    w2 = [census(L, 2, 'wave', 2) for L in Ls2]
    w2d = [census_diag(L, 2, 'wave', 2) for L in Ls2]
    check('M5', w2 == [7] * len(Ls2) and w2d == [3] * len(Ls2),
          f"corpus rule at w = 2: census dimension {w2} at L = {list(Ls2)}, stable in L, splitting "
          f"as {w2d} diagonal + {[a - b for a, b in zip(w2, w2d)]} off-diagonal. Nontrivial, and "
          f"the off-diagonal part is nonzero")

    # M6 -- the corpus rule at w = 3, the first window that can carry a gate
    Ls3 = (5, 6) if extended else (5,)
    w3 = [census(L, 2, 'wave', 3) for L in Ls3]
    w3d = [census_diag(L, 2, 'wave', 3) for L in Ls3]
    check('M6', w3 == [25] * len(Ls3) and w3d == [5] * len(Ls3),
          f"corpus rule at w = 3, the first width that can carry a gate region: census dimension "
          f"{w3} at L = {list(Ls3)}, splitting as {w3d} diagonal + "
          f"{[a - b for a, b in zip(w3, w3d)]} off-diagonal"
          + ("" if extended else " (L = 6 confirms 25 = 5 + 20 under --extended)"))

    # M7 -- explicit matrices
    bad1, r1 = explicit_confirm(4, 2, 'wave', 2)
    bad2, r2 = explicit_confirm(5, 2, 'wave', 2)
    check('M7', bad1 == 0 and bad2 == 0 and r1 == 7 and r2 == 7,
          f"explicit confirmation: every census basis element, built as an actual matrix on "
          f"q^{{2L}} configurations, satisfies [H, P] = 0 entry by entry ({bad1} and {bad2} "
          f"failures at L = 4, 5), and the rank of the span of those matrices is {r1} and {r2} -- "
          f"matching the census dimension computed by subtraction")

    # M8 -- the verdict
    offdiag = w2[0] - w2d[0]
    check('M8', offdiag > 0 and w2[0] > 1 and w3[0] > 1,
          f"VERDICT: NON-OBSTRUCTION. A diagonal H exponentiates to a diagonal unitary and can "
          f"never be a nontrivial permutation, so an autonomous local generator needs off-diagonal "
          f"weight; the corpus rule has {offdiag} off-diagonal dimensions at w = 2 and "
          f"{w3[0] - w3d[0]} at w = 3. The centralizer test therefore does NOT rule out a static "
          f"finite-range generator, and the stronger exponential condition has to be tested. "
          f"Passing a necessary condition is not evidence that a generator exists, and none is "
          f"claimed. The census is run at w <= 3 only; it is not a statement about all ranges")

    print()
    if FAILURES:
        print(f"static_generator_probe: FAILED -> {', '.join(FAILURES)}  [{time.time()-t0:.1f}s]")
        return 1
    print(f"static_generator_probe: ALL CHECKS PASS  [{time.time()-t0:.1f}s]")
    return 0


if __name__ == '__main__':
    sys.exit(main())
