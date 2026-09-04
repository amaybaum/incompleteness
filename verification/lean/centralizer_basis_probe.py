#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CT3-R2B step 1: the exact local-centralizer basis, and the first-moment test that fails.

CT3-R1 certified that the width-2 local centralizer of the update permutation P is 7-dimensional
over Q. CT3-R2A killed the function-of-P branch, leaving exactly 1 of those 7 dimensions (the
identity) spectral and 6 acting nontrivially inside degenerate P-eigenspaces. R2-B is the question
of whether any of those 6 directions can carry a static local generator, and everything in it
consumes one artifact: an EXACT basis of that space. This probe builds and freezes it.

WHAT IS BUILT. Integer coefficient vectors h spanning the centralizer, each verified against EVERY
defining equation exactly over Z -- no modular step in the certificate. Their images are
Q-independent because their reductions are independent mod p, and the count matches the R1 census
dimension, so the basis is complete and not merely contained.

THE ARITHMETIC CONDITION R2-B HAS TO SATISFY. If exp(-iH) = exp(i theta) P and P^m = I then
exp(-i m H) = exp(i m theta) I, so EVERY eigenvalue of H lies in

    -theta + (2 pi / m) Z,

one global arithmetic lattice rather than m separate 2 pi-cosets. The P-eigenspaces then only fix
which residue class each block occupies: on the omega^r eigenspace the integer n in
nu = -theta + (2 pi/m) n satisfies n = -r (mod m), so WITHIN one block the eigenvalue differences
are multiples of 2 pi, and only BETWEEN blocks does the finer 2 pi/m spacing appear.

THE CHEAPEST TEST, AND WHY IT DOES NOT WORK HERE. Summing that condition over a block gives, with
t the single offset that absorbs both the scalar part of H and theta,

    tr(Pi_r B(a)) + t d_r + 2 pi r d_r / m  in  2 pi Z,

which is LINEAR in the coefficient vector a and needs no diagonalization: since P^m = I the
spectral projector is Pi_r = (1/m) sum_k omega^(-rk) P^k, so every block trace is a finite Fourier
transform of the numbers tr(P^k B) = sum_b B[sigma^k b, b] -- single matrix entries summed along
orbits, nonzero only where (sigma^k b, b) is a local pair. Those are computed here as exact
integers.

The test then fails to bite, and that is this probe's actual finding. The map sending a direction in
the 7-dimensional centralizer to its vector of block traces has rank

    2  at L = 5   (5 of the 7 directions have every block trace zero or dependent)
    1  at L = 6   (6 of the 7 directions are invisible)

So first moments see almost nothing of the space they are supposed to constrain, and the k = 1
block-trace test cannot decide R2-B at either volume. Escalation to the second block moments
tr(Pi_r H^2) is mandatory rather than optional. Recording that here saves the next round from
starting at k = 1 and concluding nothing.

WHAT IS PINNED. The first-moment subspace -- the row space of the block-trace vectors, in canonical
reduced form over Q -- is an invariant of the centralizer space, not of the basis chosen for it. It
is checked against stored values so that a later change to the basis construction cannot silently
move the object every subsequent round is about.

  C1  an exact integer basis, every element verified to commute with P over Z
  C2  the basis is complete: its rank matches the R1 census dimension, so 7 = 1 + 6 with the
      identity spectral and 6 directions left for R2-B
  C3  the identity lies in the span, so "modulo scalars" is well defined
  C4  the block traces tr(P^k B) are exact integers, computed without diagonalizing
  C5  THE FINDING: the first-moment map has rank 2 at L = 5 and rank 1 at L = 6, so the k = 1
      test cannot decide R2-B and second moments are required
  C6  the first-moment subspace, canonical over Q, pinned against stored values
"""

import sys
import time
from fractions import Fraction
from math import lcm

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from static_generator_probe import (Lat, Ansatz, centralizer_rows, nullspace_mod_p,   # noqa: E402
                                    redundancy_dim, local_pairs, lift_to_integers,
                                    verify_integer_kernel, census)

PRIME = 2147483647
FAILURES = []


def check(label, ok, msg):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}")
    if not ok:
        FAILURES.append(label)


def rank_Q(rows):
    """Exact rank over Q of a list of integer row vectors."""
    piv = {}
    for r0 in rows:
        r = {c: Fraction(v) for c, v in enumerate(r0) if v}
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
    return len(piv), piv


def canonical_rowspace(rows, width):
    """The row space in canonical reduced form: a sorted tuple of Fraction tuples."""
    _, piv = rank_Q(rows)
    out = []
    for c in sorted(piv):
        row = piv[c]
        out.append(tuple(row.get(j, Fraction(0)) for j in range(width)))
    # fully reduce so the form depends only on the space
    for i in range(len(out) - 1, -1, -1):
        lead = next(j for j in range(width) if out[i][j])
        for k in range(i):
            f = out[k][lead]
            if f:
                out[k] = tuple(out[k][j] - f * out[i][j] for j in range(width))
    return tuple(out)


def orbit(lat):
    perm = [lat.enc(lat.leap(lat.dec(i))) for i in range(lat.N)]
    seen = [False] * lat.N
    lens = []
    for i in range(lat.N):
        if seen[i]:
            continue
        c, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            c += 1
        lens.append(c)
    m = 1
    for c in lens:
        m = lcm(m, c)
    return perm, m


def exact_basis(L, q, w, rule='wave'):
    """Integer coefficient vectors spanning the centralizer, each verified over Z."""
    lat = Lat(L, q, rule)
    ans = Ansatz(lat, w)
    rows = centralizer_rows(lat, ans)
    nullb = nullspace_mod_p(rows, ans.U, PRIME)
    target = len(nullb) - redundancy_dim(lat, ans, 'all')
    pairs = local_pairs(lat, ans)
    import random
    rng = random.Random(20260904)
    probes = [(lat.dec(rng.randrange(lat.N)),) * 2 for _ in range(200)]
    tries = 0
    while len(probes) < 400 and tries < 8000:
        tries += 1
        ab = pairs[rng.randrange(len(pairs))]
        if ab[0] != ab[1]:
            probes.append(ab)
    forms = [ans.form(a, b) for (a, b) in probes]
    piv, chosen = {}, []
    for hv in nullb:
        r = {i: v for i, v in enumerate(
            sum(c * hv[k] for k, c in f.items()) % PRIME for f in forms) if v}
        while r:
            c = min(r)
            pr = piv.get(c)
            if pr is None:
                piv[c] = r
                chosen.append(hv)
                break
            f = r[c] * pow(pr[c], PRIME - 2, PRIME) % PRIME
            for cc, vv in pr.items():
                nv = (r.get(cc, 0) - f * vv) % PRIME
                if nv:
                    r[cc] = nv
                elif cc in r:
                    del r[cc]
        if len(chosen) == target:
            break
    out = [iv for iv in (lift_to_integers(hv, PRIME) for hv in chosen)
           if iv is not None and verify_integer_kernel(rows, iv)]
    return lat, ans, out, target, forms


def block_traces(lat, ans, hv, m, perm):
    """tr(P^k B) = sum_b B[sigma^k b, b], as exact integers. No diagonalization."""
    cfg = [lat.dec(i) for i in range(lat.N)]
    idx = list(range(lat.N))
    out = []
    for _ in range(m):
        out.append(sum(sum(c * hv[k] for k, c in ans.form(cfg[idx[b]], cfg[b]).items())
                       for b in range(lat.N)))
        idx = [perm[x] for x in idx]
    return out


def identity_vector(lat, ans):
    """The coefficient vector of the identity: h_x[u,u] = 1 at every site and window value."""
    hv = [0] * ans.U
    for x in range(lat.L):
        for u in range(ans.Dw):
            hv[ans.key(x, u, u)] = 1
    return hv


PINNED = {
    (5, 2, 2): ((Fraction(1), Fraction(0), Fraction(1, 256), Fraction(0), Fraction(1, 256),
                 Fraction(1, 2), Fraction(1, 256), Fraction(0), Fraction(1, 256), Fraction(0)),
                (Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0),
                 Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1))),
    (6, 2, 2): ((Fraction(1), Fraction(1, 1024), Fraction(1, 256), Fraction(1, 64),
                 Fraction(1, 256), Fraction(1, 1024)),),
}


def main():
    t0 = time.time()
    print("centralizer_basis_probe: CT3-R2B step 1, the exact basis and the first-moment map")
    print()
    cases = [(5, 2, 2), (6, 2, 2)]
    data = {}
    for (L, q, w) in cases:
        lat, ans, B, target, _ = exact_basis(L, q, w)
        perm, m = orbit(lat)
        T = [block_traces(lat, ans, hv, m, perm) for hv in B]
        data[(L, q, w)] = (lat, ans, B, target, perm, m, T)

    ok = all(len(d[2]) == d[3] for d in data.values())
    check('C1', ok,
          "an exact integer basis of the width-2 local centralizer, every element verified against "
          "EVERY defining equation exactly over Z -- no modular step in the certificate: "
          + "; ".join(f"L={L}: {len(data[(L,q,w)][2])}/{data[(L,q,w)][3]}" for (L, q, w) in cases))

    ok = all(d[3] == census(L, q, 'wave', w) for (L, q, w), d in data.items())
    check('C2', ok,
          "the basis is COMPLETE, not merely contained: its size matches the CT3-R1 census "
          "dimension at each volume, so the space is 7 = 1 + 6 with the identity the only "
          "function-of-P direction (CT3-R2A) and 6 directions left as the R2-B search space")

    ok = True
    for (L, q, w), (lat, ans, B, target, perm, m, T) in data.items():
        idv = identity_vector(lat, ans)
        _, _, _, _, forms = exact_basis(L, q, w)
        imgs = [[sum(c * hv[k] for k, c in f.items()) for f in forms] for hv in B]
        with_id = imgs + [[sum(c * idv[k] for k, c in f.items()) for f in forms]]
        ok &= (rank_Q(imgs)[0] == rank_Q(with_id)[0] == target)
    check('C3', ok,
          "the identity lies in the span of the basis, so quotienting by scalars is well defined "
          "and the R2-B search space is exactly 6-dimensional at each volume")

    ok = all(all(isinstance(x, int) for x in row) for d in data.values() for row in d[6])
    check('C4', ok,
          "the block traces tr(P^k B) are exact integers, computed as sums of single matrix "
          "entries along orbits rather than by diagonalizing: Pi_r = (1/m) sum_k omega^(-rk) P^k, "
          "so every block trace is a finite Fourier transform of them. "
          + "; ".join(f"L={L}: ord={data[(L,q,w)][5]}" for (L, q, w) in cases))

    ranks = {(L, q, w): rank_Q(d[6])[0] for (L, q, w), d in data.items()}
    ok = ranks[(5, 2, 2)] == 2 and ranks[(6, 2, 2)] == 1
    check('C5', ok,
          f"THE FINDING. The map from a centralizer direction to its vector of block traces has "
          f"rank {ranks[(5,2,2)]} at L = 5 and {ranks[(6,2,2)]} at L = 6, against a space of "
          f"dimension 7. So {7-ranks[(5,2,2)]} and {7-ranks[(6,2,2)]} of the seven directions are "
          f"INVISIBLE to first moments, and the linear k = 1 block-trace test -- the cheapest form "
          f"of the arithmetic spectrum condition -- cannot decide R2-B at either volume. "
          f"Escalation to the second block moments tr(Pi_r H^2) is mandatory, not optional. This "
          f"is a fact about the test, not about whether a static generator exists")

    ok = True
    for key, pin in PINNED.items():
        if key in data:
            got = canonical_rowspace(data[key][6], data[key][5])
            ok &= (got == pin)
    check('C6', ok,
          "the first-moment subspace -- the row space of the block-trace vectors in canonical "
          "reduced form over Q -- is an invariant of the centralizer space rather than of the "
          "basis chosen for it, and it matches the pinned value, so a later change to the basis "
          "construction cannot silently move the object every subsequent round is about")

    print()
    if FAILURES:
        print(f"centralizer_basis_probe: FAILED -> {', '.join(FAILURES)}  [{time.time()-t0:.1f}s]")
        return 1
    print(f"centralizer_basis_probe: ALL CHECKS PASS  [{time.time()-t0:.1f}s]")
    return 0


if __name__ == '__main__':
    sys.exit(main())
