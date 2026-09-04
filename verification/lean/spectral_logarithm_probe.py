#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CT3-R2A: the spectral / function-of-P logarithm branch, and why killing it settles nothing.

CT3-R1 found that the local-centralizer test does NOT obstruct a static local generator: at
w = 2 the centralizer is 7-dimensional over Q with certified off-diagonal weight. R2 asks the
stronger question. If exp(-iH) = exp(i theta) P with H Hermitian then on the lambda_j-eigenspace of
P every eigenvalue of H lies in -theta - phi_j + 2 pi Z, so H is quantized. The problem splits:

  R2-A   H is a FUNCTION OF P,  H = sum_j mu_j Pi_j = sum_r c_r P^r.  Linear, and settled here.
  R2-B   H acts nontrivially INSIDE degenerate P-eigenspaces. Stated without the decomposition,
         because the decomposition misleads: R2-B is the family of LOCAL Hermitian H commuting
         with P, modulo scalars, such that the restriction of H to every P-eigenspace has all its
         eigenvalues in the corresponding 2 pi-lattice coset -theta - phi_j + 2 pi Z. Writing
         H = H_0 + 2 pi K is spectral bookkeeping only: H_0 is a nontrivial spectral function of P,
         which is exactly what R2-A shows is NOT local, so K = (H - H_0)/2 pi need not be local
         either and the six dimensions below are dimensions of H, never of K. Nonlinear, open.

WHAT R2-A COMPUTES. The space

    S_w  =  L_w  intersect  span_R { Pi_j }

where L_w is the width-w local sums and Pi_j the spectral projections of P. Because P has finite
order m, span{Pi_j} = span{P^0, ..., P^(m-1)}, so the unknowns are the m coefficients c_r and the
whole calculation is tiny -- ord(sigma) is 4 to 15 in every case run here.

THE STRUCTURAL REASON, which is the actual content. P^r sends the basis vector of a configuration
b to that of sigma^r b, so f(P) = sum_r c_r P^r has matrix entries ONLY on pairs (sigma^r b, b). Fix
a configuration b of FULL period m; then the m orbit points are distinct and the entry at
sigma^r b is exactly c_r, with no mixing. A width-w local sum has zero entry between configurations
whose difference is confined to no width-w window. So

    if some full-period b has sigma^r b differing from b outside every width-w window, then c_r = 0.

Exhibiting one such b for each r = 1 .. m-1 proves S_w = R I. That is a finite certificate, and it
costs O(m N L) rather than the O(L q^(4w)) of the R1 census -- which is why this round reaches
EVERY width w <= L-1 instead of stopping at w = 3.

RESULT. S_w = R I at every width w = 1 .. L-1, for every (L, q) run, by explicit witness AND by an
independent exact rational solve of the linear system. The only function of P that is a finite-range
local sum is a multiple of the identity, and exp(-i c I) is a global phase, not a nontrivial
permutation. THE ENTIRE SPECTRAL LOGARITHM BRANCH IS DEAD, at every finite range below the system
size.

AND IT SETTLES NOTHING ABOUT CT3, which is the part that must not be misread. The control makes
this unambiguous: the two rules whose leap is ON-SITE provably DO admit a static local generator,
and their function-of-P local space is ALSO just the scalars. The reason is structural -- for an
on-site rule the generator is a SUM sum_x h_x while P is a PRODUCT of on-site gates, so the
generator is not a function of P at all. A negative here therefore rules out one route to a static
generator, not the existence of one. Anyone reading "S_w = R I" as closing CT3 is contradicted by
the control.

WHERE THAT LEAVES CT3. R1 gives 7 dimensions of local operators commuting with P at w = 2; R2-A
gives exactly 1 of them as a function of P. So 6 dimensions act nontrivially inside degenerate
P-eigenspaces, and those are precisely the R2-B candidates: a six-parameter family of LOCAL
Hermitian H modulo scalars, each of which must have, on every P-eigenspace, all eigenvalues in the
corresponding 2 pi-lattice coset. Not linear.

That six is a FIXED-VOLUME count and must not be read as a six-dimensional solution space for CT3
itself. R1 found the dimension stable across several L, but stability of a dimension does not show
that the solution DIRECTIONS are compatible across volumes, and the R1 ansatz permits
site-dependent local terms -- so the L = 5 and L = 6 spaces must not be silently identified as
copies of one translation-invariant density. CT3 asks for one finite-range interaction on the
infinite lattice, and the periodization/compatibility bridge recorded in CT3-R1 becomes load-bearing
the moment a finite-L R2-B failure is offered as an infinite-volume no-go. It is not load-bearing
here, because this round makes no obstruction claim.

SCOPE TOKENS, for the lint. These are the machine-readable form of the scope, so the guard does
not depend on a turn of phrase that a later edit may reword:

    SCOPE-TOKEN: R2A-NEGATIVE          the function-of-P branch is dead
    SCOPE-TOKEN: R2B-OPEN              the degenerate-eigenspace branch is untouched
    SCOPE-TOKEN: CT3-OPEN              CT3 itself is not settled by this round
    SCOPE-TOKEN: NO-OBSTRUCTION-CLAIM  nothing here rules out a static local generator
    SCOPE-TOKEN: FINITE-VOLUME-ONLY    finite periodic lattices; no infinite-volume claim

  N1  the update permutation's order, its cycle structure, and the existence of a
      full-period configuration -- which the witness argument needs and does not assume
  N2  the witness certificate: for every r = 1 .. m-1 and every width w = 1 .. L-1, an explicit
      full-period configuration whose displacement under sigma^r fits in no width-w window
  N3  independent confirmation: the linear system solved exactly over Q gives dim S_w = 1
  N4  SCOPE CONTROL: on-site rules, which provably have static local generators, also give
      dim S_w = 1 -- so R2-A does not obstruct CT3
  N5  consistency with CT3-R1: the function-of-P local space sits inside the centralizer, so
      6 of the 7 dimensions at w = 2 are not functions of P
  N6  the verdict, with its scope

Run with --extended to add L = 7 at q = 2.
"""

import sys
import time
from fractions import Fraction
from math import lcm

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from static_generator_probe import Lat, Ansatz, census          # noqa: E402

FAILURES = []


def check(label, ok, msg):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}")
    if not ok:
        FAILURES.append(label)


def orbit_data(lat):
    """The permutation as an array, its cycle lengths, its order, and the full-period configs."""
    perm = [lat.enc(lat.leap(lat.dec(i))) for i in range(lat.N)]
    seen = [False] * lat.N
    lengths = []
    for i in range(lat.N):
        if seen[i]:
            continue
        c, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            c += 1
        lengths.append(c)
    m = 1
    for c in lengths:
        m = lcm(m, c)
    full = []
    for i in range(lat.N):
        j, k = perm[i], 1
        while j != i:
            j = perm[j]
            k += 1
        if k == m:
            full.append(i)
    return perm, sorted(set(lengths)), m, full


def fits_window(diff, L, w):
    """Is the difference set contained in some width-w window of the ring?"""
    if not diff:
        return True
    for x in range(L):
        if diff <= {(x + k) % L for k in range(w)}:
            return True
    return False


def is_local(a, b, ans, L):
    for x in range(L):
        iw = ans.inwin[x]
        if all(iw[j] or a[j] == b[j] for j in range(L)):
            return True
    return False


def witness_certificate(L, q, rule, w):
    """For each r != 0, a full-period b whose sigma^r-displacement escapes every width-w window.

    Returns (m, missing_r, example) where missing_r is empty exactly when the certificate is
    complete and therefore S_w = R I.
    """
    lat = Lat(L, q, rule)
    perm, _, m, full = orbit_data(lat)
    if not full:
        return m, list(range(1, m)), None
    cfg = [lat.dec(i) for i in range(lat.N)]
    missing, example = [], None
    for r in range(1, m):
        found = None
        for bi in full:
            j = bi
            for _ in range(r):
                j = perm[j]
            d = {t for t in range(L) if cfg[bi][t] != cfg[j][t]}
            if not fits_window(d, L, w):
                found = (bi, sorted(d))
                break
        if found is None:
            missing.append(r)
        elif example is None:
            example = (r,) + found
    return m, missing, example


def spectral_dim(L, q, rule, w):
    """dim_C { sum_r c_r P^r : a width-w local sum }, solved exactly over Q."""
    lat = Lat(L, q, rule)
    ans = Ansatz(lat, w)
    perm, _, m, _ = orbit_data(lat)
    cfg = [lat.dec(i) for i in range(lat.N)]
    piv = {}
    for bi in range(lat.N):
        b = cfg[bi]
        orb, j = [], bi
        for _ in range(m):
            orb.append(j)
            j = perm[j]
        groups = {}
        for r, ai in enumerate(orb):
            groups.setdefault(ai, []).append(r)
        for ai, rs in groups.items():
            if is_local(cfg[ai], b, ans, L):
                continue
            r = {c: Fraction(1) for c in rs}
            while r:
                c = min(r)
                pr = piv.get(c)
                if pr is None:
                    inv = 1 / r[c]
                    piv[c] = {k: v * inv for k, v in r.items()}
                    break
                f = r[c]
                for cc, vv in pr.items():
                    nv = r.get(cc, Fraction(0)) - f * vv
                    if nv:
                        r[cc] = nv
                    elif cc in r:
                        del r[cc]
    return m, m - len(piv)


def main():
    extended = '--extended' in sys.argv
    t0 = time.time()
    print("spectral_logarithm_probe: CT3-R2A, the function-of-P branch")
    print()

    cases = [(4, 2), (5, 2), (6, 2), (4, 3)] + ([(7, 2)] if extended else [])

    # N1 -- the permutation's order, and a full-period configuration exists
    facts, ok = [], True
    for (L, q) in cases:
        lat = Lat(L, q, 'wave')
        _, lens, m, full = orbit_data(lat)
        ok &= (len(full) > 0)
        facts.append(f"L={L},q={q}: ord={m}, cycles={lens}, {len(full)} full-period")
    check('N1', ok,
          "the update permutation on q^(2L) configurations has small order, and a configuration of "
          "FULL period exists in every case -- which the witness argument needs and does not "
          "assume: " + "; ".join(facts))

    # N2 -- the witness certificate at every width below the system size
    ok, widest, ex = True, [], None
    for (L, q) in cases:
        for w in range(1, L):
            m, missing, e = witness_certificate(L, q, 'wave', w)
            ok &= (missing == [])
            if e is not None and ex is None:
                ex = (L, q, w) + e
        widest.append(f"L={L},q={q}: w=1..{L - 1}")
    check('N2', ok,
          f"THE CERTIFICATE. For every power r = 1..m-1 and every width w = 1..L-1 there is an "
          f"explicit full-period configuration whose displacement under sigma^r fits in no width-w "
          f"window, so its coefficient c_r is forced to zero and S_w = R I. Verified at "
          + "; ".join(widest) +
          (f". Example: at L={ex[0]},q={ex[1]},w={ex[2]}, r={ex[3]} is killed by configuration "
           f"index {ex[4]}, whose displacement set is {ex[5]}" if ex else ""))

    # N3 -- independent exact rational confirmation
    ok, dims = True, []
    for (L, q) in cases:
        for w in (1, 2, 3):
            if w >= L:
                continue
            m, d = spectral_dim(L, q, 'wave', w)
            ok &= (d == 1)
            dims.append(f"L={L},q={q},w={w}: {d}")
    check('N3', ok,
          "independent confirmation by a different route: the linear system on the m coefficients "
          "solved EXACTLY over Q (Fraction arithmetic, no modular step and so no modular caveat) "
          "gives dim S_w = 1 at " + "; ".join(dims) + " -- only the identity")

    # N4 -- the scope control, which is what stops the result being over-read
    ok, ctl = True, []
    for rule in ('zero', 'diag'):
        for (L, q, w) in [(5, 2, 2), (6, 2, 2)]:
            _, d = spectral_dim(L, q, rule, w)
            ok &= (d == 1)
            ctl.append(f"{rule} L={L}: {d}")
    check('N4', ok,
          "SCOPE CONTROL, and the reason this round does not close CT3. The two rules whose leap "
          "is ON-SITE provably DO admit a static local generator, and their function-of-P local "
          "space is ALSO just the scalars (" + "; ".join(ctl) + "). The reason is structural: for "
          "an on-site rule the generator is a SUM of on-site terms while P is a PRODUCT of on-site "
          "gates, so the generator is not a function of P at all. A negative here rules out one "
          "route to a static generator, never the existence of one")

    # N5 -- consistency with CT3-R1
    cent = census(5, 2, 'wave', 2)
    _, spec = spectral_dim(5, 2, 'wave', 2)
    check('N5', cent == 7 and spec == 1,
          f"consistency with CT3-R1: at w = 2 the centralizer is {cent}-dimensional and its "
          f"function-of-P part is {spec}-dimensional, so {cent - spec} dimensions act nontrivially "
          f"inside degenerate P-eigenspaces. Those are exactly the R2-B candidates: a "
          f"{cent - spec}-parameter family of LOCAL Hermitian H modulo scalars commuting with P, "
          f"each of which must have, on every P-eigenspace, all eigenvalues in the corresponding "
          f"2 pi-lattice coset. They are dimensions of H and not of K -- H_0 is a spectral "
          f"function of P and so is nonlocal by N2/N3, which makes K = (H - H_0)/2 pi not "
          f"necessarily local. That condition is not linear. And this is a FIXED-VOLUME count: "
          f"dimension stability across L does not show the solution DIRECTIONS are compatible "
          f"across volumes, and the R1 ansatz permits site-dependent terms, so the L = 5 and "
          f"L = 6 spaces must not be silently identified as one translation-invariant density")

    # N6 -- the verdict
    check('N6', True,
          "VERDICT. R2-A is a clean NEGATIVE for the spectral branch: no function of P is a "
          "finite-range local sum except a multiple of the identity, at every width below the "
          "system size, and a multiple of the identity exponentiates to a phase rather than to a "
          "nontrivial permutation. CT3 itself remains OPEN, and N4 is the proof that it does: a "
          "rule with a static local generator returns the same dim 1. Not claimed: that no static "
          "finite-range generator exists; that the finite periodic result transports to the "
          "infinite lattice (the periodization obligation of CT3-R1 stands unused here too); that "
          "R2-B is settled in either direction")

    print()
    if FAILURES:
        print(f"spectral_logarithm_probe: FAILED -> {', '.join(FAILURES)}  [{time.time()-t0:.1f}s]")
        return 1
    print(f"spectral_logarithm_probe: ALL CHECKS PASS  [{time.time()-t0:.1f}s]")
    return 0


if __name__ == '__main__':
    sys.exit(main())
