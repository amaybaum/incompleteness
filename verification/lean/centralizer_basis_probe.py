#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CT3-R2B step 1: the exact centralizer basis, and a first-moment obstruction at width 2.

CT3-R1 certified that the width-2 local centralizer of the update permutation P is 7-dimensional
over Q. CT3-R2A killed the function-of-P branch, leaving 1 spectral direction (the identity) and 6
acting inside degenerate P-eigenspaces. R2-B asks whether any of those can carry a static local
generator. Everything in it consumes one artifact -- an exact basis of that space -- so the basis is
built and frozen here, and then the cheapest necessary condition is applied to it exactly.

THE ARITHMETIC CONDITION. exp(-iH) = exp(i theta) P with P^m = I gives exp(-i m H) = exp(i m theta)I,
so every eigenvalue of H lies in the SINGLE lattice -theta + (2 pi/m) Z rather than in m separate
2 pi-cosets. The eigenspaces only fix which residue class each block occupies: on the omega^r block
the integer n in nu = -theta + (2 pi/m) n satisfies n = -r (mod m). So within a block eigenvalue
differences are multiples of 2 pi, and only between blocks does the finer 2 pi/m spacing appear.

Summing over a block gives, with t the single offset absorbing both the scalar part of H and theta,

    tr(Pi_r H) + t d_r + 2 pi r d_r / m  in  2 pi Z,

which is LINEAR in the coefficients and needs no diagonalization: P^m = I makes
Pi_r = (1/m) sum_k omega^(-rk) P^k, so every block trace is a finite Fourier transform of
tr(P^k B) = sum_b B[sigma^k b, b] -- single matrix entries summed along orbits, nonzero only where
(sigma^k b, b) is a local pair. Those are exact integers here, and the tie to R2-A is direct: its
displacement witnesses are the statement that many of them vanish.

THE SEARCH SPACE IS HERMITIAN, AND SPLITS. The centralizer is a complex space closed under
transpose, so it splits into a real-symmetric part and a real-antisymmetric part, and its HERMITIAN
elements are (real-symmetric) + i(real-antisymmetric). The two sectors behave differently under the
block traces: for real-symmetric S the projector identity gives T_{m-r}(S) = T_r(S), while for
i times a real-antisymmetric A one gets T_{m-r}(iA) = -T_r(iA). Getting this wrong is the easy
mistake here -- a witness built for the symmetric sector does not annihilate the antisymmetric one.
At width 2 the question is settled by computation rather than assumed: the antisymmetric sector's
block traces are IDENTICALLY ZERO at both volumes, so the symmetric analysis covers the whole
Hermitian space. That computed fact is what confines this round to width 2.

THE OBSTRUCTION. Because complex-conjugate eigenvalues of a real matrix have equal multiplicities,
d_{m-r} = d_r, and the integer covector k = e_{m-r} - e_r annihilates every Hermitian block-trace
column. Applying it to the condition above leaves

    (m - 2r) d_r / m  in  Z,

with no free parameters left. Nothing on this path is computed numerically: the annihilation is
licensed by three INTEGER facts -- the symmetric sector's orbit traces are palindromic, t_k =
t_(m-k), which holds because P^(-k) = (P^k)^T and S^T = S; the antisymmetric sector's orbit traces
vanish; and d_(m-r) = d_r. No spectral block trace is ever formed. When the pairing fails for some
r, no Hermitian H in the space -- of any coefficients, with the offset free -- can satisfy even the
first moment of the spectrum condition.
It fails for the corpus rule at both volumes tested:

    L = 5:  m = 10,  r = 1,  d_1 = 51   ->  8 * 51 / 10 = 204/5   not an integer
    L = 6:  m = 6,   r = 1,  d_1 = 670  ->  4 * 670 / 6 = 1340/3  not an integer

so WIDTH-2 R2-B IS OBSTRUCTED AT L = 5 AND L = 6. The certificate is the integer covector, checked
against every column, so the negative is exact and needs no search.

THE CONTROL, WHICH IS WHAT MAKES THE NEGATIVE READABLE. The two rules whose leap is on-site provably
DO admit a static local generator, and the test does NOT obstruct them: their update has m = 2, so
the only indices are r = 0 and r = m/2 = 1 and there is no conjugate pair with r != 0, m/2 to build
a witness from. A test that obstructed those would be wrong, and this one does not.

RANK WAS THE WRONG DIAGNOSTIC. The map from a centralizer direction to its block-trace vector has
rank 2 at L = 5 and 1 at L = 6, against a space of dimension 7. Read alone that looks like a weak
test -- most directions invisible. It is the opposite: a low-rank trace map means the coefficients
have almost no influence on the block traces, so the residue condition falls back on the block
dimensions alone and becomes HARDER to satisfy, not easier. Rank plus affine lattice arithmetic is
decisive here; rank by itself is not a diagnostic at all.

SCOPE TOKENS, so the lint does not depend on prose:

    SCOPE-TOKEN: W2-OBSTRUCTED        width 2 fails the first-moment condition at L = 5 and L = 6
    SCOPE-TOKEN: WIDER-RANGE-OPEN     w >= 3 is untouched; the antisymmetric fact is width-2 only
    SCOPE-TOKEN: CT3-OPEN             CT3 itself is not settled by this round
    SCOPE-TOKEN: FINITE-VOLUME-ONLY   finite periodic lattices; no infinite-volume claim

  C1  an exact integer basis, every element verified to commute with P over Z
  C2  the basis is complete: its rank matches the R1 census dimension, so 7 = 1 + 6
  C3  the identity lies in the span, so "modulo scalars" is well defined
  C4  the block traces tr(P^k B) are exact integers, computed without diagonalizing
  C5  the Hermitian sector split, and the computed fact the obstruction rests on: the
      antisymmetric sector has identically zero block traces at width 2
  C6  THE OBSTRUCTION: an integer covector annihilating every Hermitian block-trace column
      whose pairing with the residue vector is not an integer, at L = 5 and L = 6
  C7  CONTROL: the on-site rules, which do have static local generators, are NOT obstructed
  C8  the first-moment subspace, canonical over Q, pinned against stored values
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



def block_dims(lat, perm, m):
    """Multiplicity of the eigenvalue omega^r, from the cycle structure alone."""
    from collections import Counter
    import math as _m
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
    cnt = Counter(lens)
    return [sum(k for d, k in cnt.items() if d % (m // _m.gcd(r, m) if r else 1) == 0)
            for r in range(m)]


def palindromic(t, m):
    """t_k = t_(m-k) for every k, over the integers.

    For real-symmetric S this is a theorem, not a coincidence: P^(-k) = (P^k)^T and S^T = S give
    tr(P^(-k) S) = tr(P^k S). Checking it over Z is what licenses the annihilator below without
    ever forming a spectral block trace numerically.
    """
    return all(t[k] == t[(m - k) % m] for k in range(m))


def sector_parts(lat, ans, hv):
    """Real-symmetric and real-antisymmetric parts of a coefficient vector, kept integral."""
    sym = [0] * ans.U
    asym = [0] * ans.U
    for x in range(lat.L):
        for u in range(ans.Dw):
            for v in range(ans.Dw):
                a, b = ans.key(x, u, v), ans.key(x, v, u)
                sym[a] = hv[a] + hv[b]
                asym[a] = hv[a] - hv[b]
    return sym, asym


def obstruction_pairing(d, m):
    """The exact rational (m - 2r) d_r / m for the first admissible r where it is not an integer.

    The covector k = e_(m-r) - e_r annihilates every Hermitian block-trace column whenever the
    symmetric sector's orbit traces are palindromic and the antisymmetric sector's vanish -- both
    checked over Z. Pairing it with the residue vector u_r = r d_r / m and using d_(m-r) = d_r
    leaves exactly this rational, with every free parameter gone, the offset included. No spectral
    transform is computed anywhere on this path.
    """
    for r in range(1, m):
        if 2 * r == m:
            continue
        if d[(m - r) % m] != d[r]:
            continue
        val = Fraction((m - 2 * r) * d[r], m)
        if val.denominator != 1:
            return r, val
    return None


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
    sectors = {}
    for (L, q, w), (lat, ans, B, target, perm, m, T) in data.items():
        S, A = zip(*(sector_parts(lat, ans, hv) for hv in B))
        tS = [block_traces(lat, ans, h, m, perm) for h in S]
        tA = [block_traces(lat, ans, h, m, perm) for h in A]
        sectors[(L, q, w)] = (rank_Q(tS)[0], rank_Q(tA)[0], tS, tA)
    ok = all(rA == 0 for (_, rA, _, _) in sectors.values())
    check('C5', ok,
          f"the Hermitian search space splits: the centralizer is closed under transpose, so its "
          f"Hermitian elements are (real-symmetric) + i(real-antisymmetric), and the two sectors "
          f"behave oppositely under the block traces -- T_(m-r) = +T_r on the first, -T_r on the "
          f"second. At width 2 the antisymmetric sector has IDENTICALLY ZERO block traces "
          f"(rank {[sectors[k][1] for k in sectors]}), so the symmetric analysis covers the whole "
          f"Hermitian space. That is a computed fact, not an assumption, and it is what confines "
          f"this round to width 2. The symmetric sector has rank "
          f"{[sectors[k][0] for k in sectors]}, matching the full trace-map ranks "
          f"{[ranks[k] for k in sorted(ranks)]}")

    obstr = {}
    for (L, q, w), (lat, ans, B, target, perm, m, T) in data.items():
        d = block_dims(lat, perm, m)
        rS, rA, tS, tA = sectors[(L, q, w)]
        pal = all(palindromic(t, m) for t in tS)          # exact, over Z
        zero = all(all(x == 0 for x in t) for t in tA)    # exact, over Z
        conj = all(d[(m - r) % m] == d[r] for r in range(m))
        obstr[(L, q, w)] = (m, d, pal, zero, conj, obstruction_pairing(d, m))
    ok = all(o[2] and o[3] and o[4] and o[5] is not None for o in obstr.values())
    detail = "; ".join(
        f"L={L}: m={o[0]}, r={o[5][0]}, d_r={o[1][o[5][0]]}, (m-2r)d_r/m={o[5][1]}"
        for (L, q, w), o in sorted(obstr.items()))
    check('C6', ok,
          f"THE OBSTRUCTION, with no floating arithmetic on the load-bearing path. Three integer "
          f"facts license the covector k = e_(m-r) - e_r: the symmetric sector's orbit traces are "
          f"PALINDROMIC over Z, t_k = t_(m-k), which is a theorem since P^(-k) = (P^k)^T and "
          f"S^T = S, and which forces T_(m-r) = T_r without computing a spectral transform; the "
          f"antisymmetric sector's orbit traces VANISH over Z, so its columns are zero; and "
          f"d_(m-r) = d_r since conjugate eigenvalues of a real matrix share multiplicities. So k "
          f"annihilates every Hermitian block-trace column. Pairing it with the residue vector "
          f"then leaves the exact rational (m - 2r) d_r / m with every free parameter gone, the "
          f"offset included, and it is not an integer: {detail}. WIDTH-2 R2-B IS OBSTRUCTED at "
          f"both volumes, by an integer certificate rather than a search")

    # The control needs no basis. A witness has to annihilate EVERY column, so testing against
    # FEWER columns can only make witnesses easier to find -- the conservative direction. The
    # identity is always in the centralizer and its block-trace column is exactly (d_r), so if no
    # witness survives even that single constraint, none survives the full space.
    ctl = {}
    for rule in ('zero', 'diag'):
        for (L, q, w) in cases:
            lat = Lat(L, q, rule)
            perm, m = orbit(lat)
            ctl[(rule, L)] = (m, obstruction_pairing(block_dims(lat, perm, m), m))
    ok = all(v[1] is None for v in ctl.values())
    check('C7', ok,
          f"CONTROL, and what makes the negative readable. The two rules whose leap is on-site "
          f"provably DO admit a static local generator, and the test does NOT obstruct them: their "
          f"update has m = 2, so the only indices are r = 0 and r = m/2 and there is no conjugate "
          f"pair to build a covector from ("
          + ', '.join(f'{r} L={L}: m={v[0]}, no witness' for (r, L), v in sorted(ctl.items()))
          + "). A test that obstructed a rule with a generator sitting in plain sight would be "
            "wrong; this one does not")

    ok = True
    for key, pin in PINNED.items():
        if key in data:
            got = canonical_rowspace(data[key][6], data[key][5])
            ok &= (got == pin)
    check('C8', ok,
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
