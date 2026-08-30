#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact classification probes for the [GR] two-branch Claim (D-gauge completeness).

The Claim's open step is a classification: with all gaps distinct, matching transition
probabilities force a frequency-preserving bijection mu of ordered mode pairs, and the
Claim says the only realizable mu are a mode relabeling (branch one) or the global pair
reversal (branch two). These probes decide the two finite stress tests EXACTLY, per the
programme's decision tree, without choosing random Hamiltonians: the correspondences
themselves are enumerated and classified.

STAGE 1 (n = 4, spectrum {0,1,4,6}, all gaps distinct): the turnpike enumeration and the
complete classification of every labeled correspondence. Result: 24 relabelings + 24
reversals, NOTHING ELSE -- the two-branch classification is exhaustively true at n = 4.

STAGE 2 (n = 6, the printed homometric Golomb pair {0,1,4,10,12,17} / {0,1,8,11,13,17}):
the one place a genuinely non-two-branch mu is FORCED to exist. The full kill chain, all
exact:
  * generic moduli die at the cheapest filter: of the 9 cokernel conditions of the K6
    edge-product system, 4 pull back to identities under mu and 5 are genuine constraints
    (e.g. p1^2 = p3*p4 on every row); the exceptional locus is EXACTLY the flat rows
    p = 1/6, so both eigenbases must be flat (Hadamard-type) unitaries;
  * on the flat locus the phase constraints (the pulled-back multiplicative relations
    z^{cd} z^{de} = |V_.d|^2 z^{ce}) admit a 21-dim solution space -- 10 dimensions
    beyond gauge, a genuine near-miss -- and the Smith normal form has NO torsion, so
    that real kernel IS the complete mod-2pi solution set; the Fourier matrix fails it
    for all 720 column assignments;
  * on the kernel, V has monomial rows V_ia = x_i^{u_a} y_i^{v_a} and V' is forced with
    exponent vectors w, so JOINT unitarity confines every pairwise difference to the
    common torus zeros of two mask polynomials sharing the factor 1 + x + x^2 y; the
    commons are EIGHT roots of unity, computed complete via an exact resultant;
  * the Cayley graph they generate (order 48) has max clique THREE < six: no joint pair
    of flat unitaries exists, so the forced homometric mu admits NO realization at all.

VERDICT ENCODED HERE: both stress tests support the universal two-branch Claim; the
homometric mu is killed by explicit polynomial identities, not by genericity.

  M1  Stage 1: turnpike solutions at n = 4 are exactly {E, reflection}; all 48 labeled
      correspondences classify as 24 relabelings + 24 reversals, zero others.
  M2  Stage 2 setup: the forced mu at n = 6 is an edge bijection induced by NO vertex
      bijection, and the spectra are not translates or reflections of each other.
  M3  the modulus filter: exact ranks (6, 11), 5 genuinely violated conditions, the
      p1^2 = p3*p4 exemplar, and the exceptional locus exactly span(1).
  M4  the phase system: rank 15, kernel 21 containing the 11-dim gauge, SNF torsion-free,
      and the DFT countercontrol 0/720 in exact Z6 arithmetic.
  M5  the monomial structure: the (xi | eta) pair space is spanned by (1|0), (0|1),
      (u2|w2), (u3|w3), the edge identity holds on all 15 edges, and both masks factor
      exactly over Z with the shared factor 1 + x + x^2 y.
  M6  completeness of the joint zeros: res_y of the cofactors is x^3 (x-1)^2 (x^2+1)^2
      by exact Sylvester determinant; each candidate quadratic factors over Z[zeta12]
      by exact Vieta; all 8 allowed differences are joint zeros in Z[t]/Phi12.
  M7  the clique bound: the 8 differences generate a group of order 48 whose Cayley
      graph has max clique 3 -- six mutually orthogonal rows are impossible.
  M8  cross-references: the same rulers as bohr_frequency_probe F6 and papers/GR.md.
  M9  THE RANK CENSUS of L_mu: over every non-congruent homometric Golomb pair enumerable at
      n = 4..8 (diameter bounds 20/25/32/36/40), the lattice of pulled-back K4 exponent
      relations has rank EXACTLY n - 1 -- the exceptional modulus locus is always just the
      flat row. No pairs exist at all except at n = 6, where every one of the 136 ordered
      pairs (the printed pair among them) is full-rank. This is outcome one of the
      programme's trichotomy: no exceptional modulus strata in the enumerable range, so the
      universal statement stays the target and no block-decomposition theorem is needed yet.
  M10 THE ORBIT CENSUS: under source/target vertex relabeling, ALL census correspondences --
      the printed mu, its inverse, and every other of the 136 -- form a SINGLE orbit, whose
      exact realization space {(E, E') : E'_d - E'_c = E_b - E_a on all 15 edges} has
      dimension 4 = two translations + TWO genuine parameters. This is the known continuous
      two-parameter six-mark family (Gilbert-Postpischil 1994 give its two-dimensional
      geometric model; Bekir-Golomb 2007 prove no further counterexamples to Piccard exist),
      re-derived here independently. Because the entire kill chain (M3-M7) consumes only mu's
      combinatorics and relabeling is a symmetry of every stage, the kernel-proved flat_locus
      and clique obstruction of OIBridge/HomometricSix.lean apply VERBATIM to the whole
      family -- the parameters u, v never enter the coefficient reconstruction.
  M11 THE PARAMETRIC MU-ORBIT BRIDGE: the exceptional-family formula quoted from a later
      peer-reviewed treatment citing Bekir-Golomb 2007 satisfies all 15 gap identities of
      the printed mu symbolically in (p1, p2), with e_S = id and the UNIQUE target
      transposition e_T = (3 4); p = (1, 6) reduces to the printed pair.
  M12 THE PRIMARY EXPANSION: the two-parameter factorization printed in Bekir-Golomb 2007
      (p. 2865) -- r = Phi1*Phi2, s = Phi1*Phi2star -- expands, in exact symbolic exponent
      arithmetic, to 0/1 polynomials whose exponent sets are EXACTLY M11's X and Y; Phi2star
      is the reversal of Phi2; (a, b) = (1, 6) reproduces the paper's printed numeric
      factorizations. The formula layer of the primary audit is thereby machine-confirmed;
      the remaining audit caveat (real-vs-integer scope, recorded in the ledger) is about
      the paper's quantification, not its formulas.

Usage:  python3 gap_correspondence_probe.py
"""
import itertools
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


# ---------------------------------------------------------------- exact linear algebra
def rref(M):
    R = [[Fraction(x) for x in row] for row in M]
    m = len(R)
    n = len(R[0]) if R else 0
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if R[i][c] != 0), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        pv = R[r][c]
        R[r] = [x / pv for x in R[r]]
        for i in range(m):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [x - f * y for x, y in zip(R[i], R[r])]
        piv.append(c)
        r += 1
        if r == m:
            break
    return r, R, piv


def nullspace(M):
    m, n = len(M), len(M[0])
    r, R, piv = rref(M)
    out = []
    for f in [c for c in range(n) if c not in piv]:
        v = [Fraction(0)] * n
        v[f] = Fraction(1)
        for i, c in enumerate(piv):
            v[c] = -R[i][f]
        out.append(v)
    return out


def snf_divisors(Min):
    """Elementary divisors of an integer matrix (Smith normal form diagonal)."""
    A = [r[:] for r in Min]
    m, n = len(A), len(A[0])
    t = 0
    while t < min(m, n):
        piv = None
        for i in range(t, m):
            for j in range(t, n):
                if A[i][j] and (piv is None or abs(A[i][j]) < abs(A[piv[0]][piv[1]])):
                    piv = (i, j)
        if piv is None:
            break
        i0, j0 = piv
        if i0 != t:
            A[t], A[i0] = A[i0], A[t]
        if j0 != t:
            for r in A:
                r[t], r[j0] = r[j0], r[t]
        dirty = False
        for i in range(t + 1, m):
            if A[i][t]:
                q = A[i][t] // A[t][t]
                if q:
                    A[i] = [x - q * y for x, y in zip(A[i], A[t])]
                if A[i][t]:
                    dirty = True
        for j in range(t + 1, n):
            if A[t][j]:
                q = A[t][j] // A[t][t]
                if q:
                    for r in A:
                        r[j] -= q * r[t]
                if A[t][j]:
                    dirty = True
        if dirty:
            continue
        viol = None
        for i in range(t + 1, m):
            if any(A[i][j] % A[t][t] for j in range(t + 1, n)):
                viol = i
                break
        if viol is not None:
            A[t] = [x + y for x, y in zip(A[t], A[viol])]
            continue
        t += 1
    return [abs(A[k][k]) for k in range(t)]


# ---------------------------------------------------------------- M1  stage 1: n = 4
E4 = (0, 1, 4, 6)


def diff_multiset(S):
    return sorted(abs(x - y) for x, y in itertools.combinations(S, 2))


target = diff_multiset(E4)
diam = max(target)
sols = sorted(set((0, x, y, diam) for x, y in itertools.combinations(range(1, diam), 2)
                  if diff_multiset((0, x, y, diam)) == target))
refl4 = tuple(sorted(diam - v for v in E4))
ok1 = len(set(target)) == 6                     # Golomb: the correspondence will be forced
ok1 &= sols == sorted([E4, refl4])              # turnpike: E and its reflection, nothing else

counts = {"relabeling": 0, "reversal": 0, "OTHER": 0}
total = 0
for S in sols:
    for lab in itertools.permutations(S):
        gapsS = {}
        for c in range(4):
            for d in range(4):
                if c != d:
                    gapsS[lab[c] - lab[d]] = (c, d)
        mu4 = {}
        good = True
        for a in range(4):
            for b in range(4):
                if a != b:
                    v = E4[a] - E4[b]
                    if v not in gapsS:
                        good = False
                        break
                    mu4[(a, b)] = gapsS[v]
            if not good:
                break
        if not good:
            continue
        total += 1
        kind = "OTHER"
        for sig in itertools.permutations(range(4)):
            if all(mu4[(a, b)] == (sig[a], sig[b]) for (a, b) in mu4):
                kind = "relabeling"
                break
            if all(mu4[(a, b)] == (sig[b], sig[a]) for (a, b) in mu4):
                kind = "reversal"
                break
        counts[kind] += 1
ok1 &= total == 48 and counts == {"relabeling": 24, "reversal": 24, "OTHER": 0}
check("M1", ok1,
      f"STAGE 1 (n = 4, E = {E4}, all gaps distinct): the exact turnpike enumeration finds "
      f"precisely E and its reflection {refl4}; every one of the {total} labeled candidate "
      f"spectra yields a forced correspondence, classifying as {counts['relabeling']} "
      f"relabelings + {counts['reversal']} reversals and {counts['OTHER']} others -- the "
      f"two-branch classification is EXHAUSTIVELY verified at n = 4")

# ---------------------------------------------------------------- M2  stage 2: the forced mu
R1 = [0, 1, 4, 10, 12, 17]
R2 = [0, 1, 8, 11, 13, 17]
g1 = {}
for a, b in itertools.combinations(range(6), 2):
    g1[R1[b] - R1[a]] = (a, b)
g2 = {}
for c, d in itertools.combinations(range(6), 2):
    g2[R2[d] - R2[c]] = (c, d)
ok2 = len(g1) == 15 and len(g2) == 15 and sorted(g1) == sorted(g2)   # Golomb + homometric
mu = {(a, b): g2[R1[b] - R1[a]] for a, b in itertools.combinations(range(6), 2)}
inv_mu = {v: k for k, v in mu.items()}
ok2 &= len(set(mu.values())) == 15
ok2 &= not any(sorted(x + t for x in R1) == R2 for t in range(-40, 41))
ok2 &= not any(sorted(t - x for x in R1) == R2 for t in range(-40, 41))
induced = [sig for sig in itertools.permutations(range(6))
           if all(frozenset(mu[(a, b)]) == frozenset((sig[a], sig[b]))
                  for (a, b) in mu)]
ok2 &= induced == []
check("M2", ok2,
      "STAGE 2 setup: the printed homometric Golomb pair {0,1,4,10,12,17} / {0,1,8,11,13,17} "
      "shares its 15-element gap set with all gaps distinct, so the frequency-preserving "
      "correspondence mu is FORCED and edge-bijective; no vertex bijection induces it (checked "
      "against all 720, in either orientation), and neither spectrum is a translate or a "
      "reflected translate of the other -- this is the unique finite place where a genuinely "
      "non-two-branch correspondence exists at the combinatorial level")

# ---------------------------------------------------------------- M3  the modulus filter
edges6 = list(itertools.combinations(range(6), 2))
N = [[1 if v in e else 0 for v in range(6)] for e in edges6]
A = [[1 if v in inv_mu[e] else 0 for v in range(6)] for e in edges6]
rank_N, _, _ = rref(N)
rank_NA, _, _ = rref([N[i] + A[i] for i in range(15)])
coker = 15 - rank_N
identities = 15 - rank_NA
violated = coker - identities
NT = [[N[i][j] for i in range(15)] for j in range(6)]
W_rows = [[sum(A[e][v] * y[e] for e in range(15)) for v in range(6)] for y in nullspace(NT)]
dim_W, _, _ = rref(W_rows)
locus = nullspace(W_rows)
flat_only = len(locus) == 1 and len(set(locus[0])) == 1 and locus[0][0] != 0
# the concrete exemplar on the K4 {b0,b1,b2,b3}: m01*m23 = m02*m13 pulls back to p1^2 = p3*p4
p = [Fraction(k) for k in (2, 3, 5, 7, 11, 13)]
mm = {e: p[inv_mu[e][0]] * p[inv_mu[e][1]]
      for e in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]}
generic_fails = mm[(0, 1)] * mm[(2, 3)] != mm[(0, 2)] * mm[(1, 3)]
exemplar = (mm[(0, 1)] * mm[(2, 3)]) / (mm[(0, 2)] * mm[(1, 3)]) == p[1] ** 2 / (p[3] * p[4])
ok3 = (rank_N, coker, rank_NA, identities, violated) == (6, 9, 11, 4, 5)
ok3 &= dim_W == 5 and flat_only and generic_fails and exemplar
check("M3", ok3,
      f"THE MODULUS FILTER, exact over Q: the K6 edge-product system has {coker} cokernel "
      f"conditions; under mu, {identities} pull back to identities and {violated} are genuine "
      f"constraints -- a generic row (p = 2,3,5,7,11,13) already fails the K4 condition, whose "
      f"pullback is the polynomial identity p1^2 = p3*p4 (verified as the exact ratio). The "
      f"violated exponent vectors span a 5-dim space whose orthogonal complement is EXACTLY "
      f"span(1): the only rows passing every filter are flat, and row sums force p = 1/6 -- "
      f"both eigenbases must be flat (Hadamard-type) unitaries")

# ---------------------------------------------------------------- M4  the phase system
tri6 = list(itertools.combinations(range(6), 3))
rows = []
for (c, d, e) in tri6:
    legs = [(inv_mu[(c, d)], 1), (inv_mu[(d, e)], 1), (inv_mu[(c, e)], -1)]
    for i in range(1, 6):
        row = [0] * 36
        for (a, b), s in legs:
            row[6 * i + a] += s
            row[6 * i + b] -= s
            row[a] -= s
            row[b] += s
        rows.append(row)
rank_M, _, _ = rref(rows)
nullity = 36 - rank_M
gauge = []
for i in range(6):
    g = [0] * 36
    for a in range(6):
        g[6 * i + a] = 1
    gauge.append(g)
for a in range(6):
    g = [0] * 36
    for i in range(6):
        g[6 * i + a] = 1
    gauge.append(g)
rank_G, _, _ = rref(gauge)
gauge_in = all(all(sum(r[k] * g[k] for k in range(36)) == 0 for r in rows) for g in gauge)
divisors = snf_divisors(rows)
torsion_free = len(divisors) == rank_M and all(d == 1 for d in divisors)
# DFT countercontrol in exact Z6: phi[i][a] = 2pi i sig(a)/6 solves the system mod 2pi
# iff every triangle's integer defect vanishes mod 6
dft_surv = 0
for sig in itertools.permutations(range(6)):
    if all((sig[inv_mu[(c, d)][0]] - sig[inv_mu[(c, d)][1]]
            + sig[inv_mu[(d, e)][0]] - sig[inv_mu[(d, e)][1]]
            - sig[inv_mu[(c, e)][0]] + sig[inv_mu[(c, e)][1]]) % 6 == 0
           for (c, d, e) in tri6):
        dft_surv += 1
ok4 = (rank_M, nullity, rank_G) == (15, 21, 11) and gauge_in and torsion_free
ok4 &= dft_surv == 0
check("M4", ok4,
      f"THE PHASE SYSTEM (the pulled-back multiplicative relations as triangle constraints): "
      f"{len(rows)} equations on the 36 phases, rank {rank_M}, kernel dim {nullity} containing "
      f"the {rank_G}-dim gauge -- TEN genuine phase dimensions survive, so the triangle stage "
      f"does NOT kill the flat locus. The Smith normal form is torsion-free (all divisors 1), "
      f"so that real kernel is the COMPLETE mod-2pi solution set; the 6x6 Fourier matrix "
      f"fails it for all 720 column assignments (exact Z6 defects), so any survivor would be "
      f"a non-Fourier flat unitary")

# ---------------------------------------------------------------- M5  the monomial structure
u2 = (0, 1, 0, 2, 4, 5)
u3 = (0, 0, 1, 2, 2, 3)
w2 = (-3, -2, 1, 0, 2, 2)
w3 = (-2, -2, -1, 0, 0, 1)
# the pair space: (xi, eta) with xi_a - xi_b = eta_c - eta_d on all 15 edges
Mp = []
for (c, d) in edges6:
    a, b = inv_mu[(c, d)]
    row = [0] * 12
    row[a] += 1
    row[b] -= 1
    row[6 + c] -= 1
    row[6 + d] += 1
    Mp.append(row)
pair_dim = len(nullspace(Mp))
claimed = [[1] * 6 + [0] * 6, [0] * 6 + [1] * 6,
           list(u2) + list(w2), list(u3) + list(w3)]
in_null = all(all(sum(r[k] * v[k] for k in range(12)) == 0 for r in Mp) for v in claimed)
rank_claimed, _, _ = rref(claimed)
edge_id = all(u2[a] - u2[b] == w2[c] - w2[d] and u3[a] - u3[b] == w3[c] - w3[d]
              for (a, b), (c, d) in mu.items())


def pmul(P, Q):
    R = {}
    for e1, c1 in P.items():
        for e2, c2 in Q.items():
            k = (e1[0] + e2[0], e1[1] + e2[1])
            R[k] = R.get(k, 0) + c1 * c2
    return {k: v for k, v in R.items() if v}


maskV = {(u2[a], u3[a]): 1 for a in range(6)}                     # F(x,y), V side
maskP = {(w2[c] + 3, w3[c] + 2): 1 for c in range(6)}             # x^3 y^2 * Ftilde, V' side
G6 = {(0, 0): 1, (1, 0): 1, (2, 1): 1}                            # 1 + x + x^2 y
H6 = {(0, 0): 1, (0, 1): 1, (1, 1): -1, (3, 2): 1}                # 1 + y - x y + x^3 y^2
Ht6 = {(0, 0): 1, (2, 1): -1, (3, 1): 1, (3, 2): 1}               # 1 - x^2 y + x^3 y + x^3 y^2
facts = pmul(G6, H6) == maskV and pmul(G6, Ht6) == maskP
ok5 = pair_dim == 4 and in_null and rank_claimed == 4 and edge_id and facts
check("M5", ok5,
      "THE MONOMIAL STRUCTURE: the (xi|eta) pair space has dim 4, spanned exactly by the two "
      "constants and (u2|w2), (u3|w3) with u2 = (0,1,0,2,4,5), u3 = (0,0,1,2,2,3), "
      "w2 = (-3,-2,1,0,2,2), w3 = (-2,-2,-1,0,0,1); the linkage identity "
      "xi_a - xi_b = eta_c - eta_d holds on all 15 edges. So on the kernel V and V' have "
      "monomial rows, joint unitarity is 15 shared difference conditions on two masks, and "
      "both masks factor EXACTLY over Z with the shared factor 1 + x + x^2*y: "
      "F = (1+x+x^2y)(1+y-xy+x^3y^2), Ftilde = (1+x+x^2y)(1-x^2y+x^3y+x^3y^2)")

# ---------------------------------------------------------------- M6  joint zeros, complete
# Z[t]/Phi12, Phi12 = t^4 - t^2 + 1; zeta12 = t, i = t^3, omega = t^4, -1 = t^6.
ZP = [None] * 12
ZP[0] = (1, 0, 0, 0)
ZP[1] = (0, 1, 0, 0)
ZP[2] = (0, 0, 1, 0)
ZP[3] = (0, 0, 0, 1)
ZP[4] = (-1, 0, 1, 0)         # t^4 = t^2 - 1
ZP[5] = (0, -1, 0, 1)         # t^5 = t^3 - t
for k in range(6, 12):        # t^6 = -1
    ZP[k] = tuple(-x for x in ZP[k - 6])


def cyc_add(u, v):
    return tuple(x + y for x, y in zip(u, v))


def cyc_mulz(u, k):
    """u * t^k."""
    out = (0, 0, 0, 0)
    for d in range(4):
        if u[d]:
            out = cyc_add(out, tuple(u[d] * c for c in ZP[(d + k) % 12]))
    return out


def eval_mask(mask, ax, ay):
    """mask at x = zeta12^ax, y = zeta12^ay, as an element of Z[t]/Phi12."""
    tot = (0, 0, 0, 0)
    for (px, py), coef in mask.items():
        tot = cyc_add(tot, tuple(coef * c for c in ZP[(px * ax + py * ay) % 12]))
    return tot


# the eight allowed differences, as (x, y) exponents of zeta12
DIFFS = [(4, 0), (8, 0),            # (omega, 1), (omega^-1, 1)      -- zeros of the shared factor
         (0, 3), (0, 9),            # (1, i), (1, -i)
         (3, 6), (9, 6),            # (i, -1), (-i, -1)
         (3, 9), (9, 3)]            # (i, -i), (-i, i)
joint = all(eval_mask(maskV, ax, ay) == (0, 0, 0, 0) and
            eval_mask(maskP, ax, ay) == (0, 0, 0, 0) for ax, ay in DIFFS)

# completeness 1: res_y(H, Ht) = x^3 (x-1)^2 (x^2+1)^2 by exact Sylvester determinant.
# H  = (x^3) y^2 + (1-x) y + 1,  Ht = (x^3) y^2 + (x^3-x^2) y + 1  as polys in y over Z[x].
def xp(*cs):                      # little univariate helper: xp(c0,c1,...) = sum ci x^i
    return {i: c for i, c in enumerate(cs) if c}


def xmul(P, Q):
    R = {}
    for i, a in P.items():
        for j, b in Q.items():
            R[i + j] = R.get(i + j, 0) + a * b
    return {k: v for k, v in R.items() if v}


def xsub(P, Q):
    R = dict(P)
    for k, v in Q.items():
        R[k] = R.get(k, 0) - v
    return {k: v for k, v in R.items() if v}


def det4(M):
    # Laplace along the first row, over Z[x]
    def det3(m):
        t1 = xmul(m[0][0], xsub(xmul(m[1][1], m[2][2]), xmul(m[1][2], m[2][1])))
        t2 = xmul(m[0][1], xsub(xmul(m[1][0], m[2][2]), xmul(m[1][2], m[2][0])))
        t3 = xmul(m[0][2], xsub(xmul(m[1][0], m[2][1]), xmul(m[1][1], m[2][0])))
        return xsub(xsub(t1, t2), xsub({}, t3))
    tot = {}
    for j in range(4):
        minor = [[M[r][c] for c in range(4) if c != j] for r in range(1, 4)]
        term = xmul(M[0][j], det3(minor))
        tot = xsub(tot, term) if j % 2 else xsub(tot, xsub({}, term))
    return tot


a2, a1, a0 = xp(0, 0, 0, 1), xp(1, -1), xp(1)
b2, b1, b0 = xp(0, 0, 0, 1), xp(0, 0, -1, 1), xp(1)
Z0 = {}
syl = [[a2, a1, a0, Z0], [Z0, a2, a1, a0], [b2, b1, b0, Z0], [Z0, b2, b1, b0]]
res = det4(syl)
expect = xmul(xp(0, 0, 0, 1), xmul(xmul(xp(-1, 1), xp(-1, 1)), xmul(xp(1, 0, 1), xp(1, 0, 1))))
res_ok = res == expect or res == {k: -v for k, v in expect.items()}
# so a common zero with x on the unit circle has x in {1, i, -i} (the factor x^3 has only
# the off-circle root 0, and both leading y-coefficients are x^3, nonvanishing on the circle).
# completeness 2: at each candidate x0 the quadratic H(x0, .) factors EXACTLY over Z[zeta12]
# with both roots on the torus and both shared with Ht -- verified by Vieta in the ring.
vieta = True
quad_cases = [
    (0, (3, 9)),      # x = 1:  H(1,y) = y^2 + 1,            roots  i, -i
    (3, (6, 9)),      # x = i:  roots -1, -i
    (9, (6, 3)),      # x = -i: roots -1,  i
]
for ax, (r1, r2) in quad_cases:
    A2 = ZP[(3 * ax) % 12]                                     # x^3
    A1 = cyc_add(ZP[0], tuple(-c for c in ZP[ax % 12]))        # 1 - x
    A0 = ZP[0]
    B1 = cyc_add(ZP[(3 * ax) % 12], tuple(-c for c in ZP[(2 * ax) % 12]))   # x^3 - x^2
    # H:  a2 (r1 + r2) = -a1  and  a2 r1 r2 = a0
    s = cyc_add(ZP[r1], ZP[r2])
    pr = ZP[(r1 + r2) % 12]
    lhs_s = (0, 0, 0, 0)
    for d in range(4):
        if s[d]:
            lhs_s = cyc_add(lhs_s, tuple(s[d] * c for c in cyc_mulz(A2, d)))
    vieta &= lhs_s == tuple(-c for c in A1)
    lhs_p = (0, 0, 0, 0)
    for d in range(4):
        if pr[d]:
            lhs_p = cyc_add(lhs_p, tuple(pr[d] * c for c in cyc_mulz(A2, d)))
    vieta &= lhs_p == A0
    # the second cofactor's quadratic has the same leading and constant coefficient, so
    # sharing both roots means b1 = a1 there too -- check Vieta against B1, then directly
    vieta &= lhs_s == tuple(-c for c in B1)
    for r in (r1, r2):
        vieta &= eval_mask(Ht6, ax, r) == (0, 0, 0, 0)
# the shared factor 1 + x + x^2 y on the torus: y = -(1+x)/x^2 needs |1+x| = 1, i.e.
# 2 + 2 Re x = 1, so x = omega^{+-1} exactly, and then y = -(1+omega)/omega^2 = 1.
gzeros = (eval_mask(G6, 4, 0) == (0, 0, 0, 0) and eval_mask(G6, 8, 0) == (0, 0, 0, 0))
ok6 = joint and res_ok and vieta and gzeros
check("M6", ok6,
      "COMPLETENESS OF THE JOINT ZEROS: all 8 allowed differences kill BOTH masks exactly in "
      "Z[t]/Phi12; the resultant res_y of the two cofactors equals x^3 (x-1)^2 (x^2+1)^2 by "
      "exact Sylvester determinant over Z[x] (leading y-coefficients x^3 never vanish on the "
      "circle, so common cofactor zeros need x in {1, i, -i}); at each such x the quadratic "
      "factors exactly over Z[zeta12] by Vieta with both roots fourth roots of unity shared by "
      "the second cofactor; and the shared factor 1 + x + x^2 y vanishes on the torus only at "
      "(omega, 1) and (omega^-1, 1), since |1+x| = 1 forces Re x = -1/2. Eight points, no more")

# ---------------------------------------------------------------- M7  the clique bound
conn = {(ax % 12, (ay // 3) % 4) for ax, ay in DIFFS}    # y is always a 4th root: store in Z4
conn = {(a, b) for (a, b) in conn}
symmetric = all(((-a) % 12, (-b) % 4) in conn for a, b in conn)
S = {(0, 0)}
changed = True
while changed:
    changed = False
    for gx, gy in list(conn):
        for hx, hy in list(S):
            e = ((gx + hx) % 12, (gy + hy) % 4)
            if e not in S:
                S.add(e)
                changed = True
Sl = sorted(S)
adj = {u: {v for v in Sl if v != u and ((u[0] - v[0]) % 12, (u[1] - v[1]) % 4) in conn}
       for u in Sl}
best = []


def grow(clique, cand):
    global best
    if len(clique) > len(best):
        best = clique[:]
    for idx, v in enumerate(cand):
        if len(clique) + len(cand) - idx <= len(best):
            break
        grow(clique + [v], [u for u in cand[idx + 1:] if u in adj[v]])


grow([], Sl)
ok7 = symmetric and len(Sl) == 48 and len(best) == 3
check("M7", ok7,
      f"THE CLIQUE BOUND: the 8 allowed differences are symmetric under inversion and generate "
      f"a group of order {len(Sl)} inside Z12 x Z4; exhaustive search puts the Cayley graph's "
      f"max clique at {len(best)} < 6. Six pairwise-orthogonal rows are impossible for V and V' "
      f"JOINTLY, so the forced homometric mu admits NO realization at any point of parameter "
      f"space: generic moduli die at the first filter, the flat locus dies here. The n = 6 "
      f"stress test therefore SUPPORTS the universal two-branch Claim, by explicit polynomial "
      f"identities rather than genericity")

# ---------------------------------------------------------------- M8  cross-references
fb = open(os.path.join(HERE, 'bohr_frequency_probe.py'), encoding='utf-8').read()
gr = open(os.path.join(HERE, '..', '..', 'papers', 'GR.md'), encoding='utf-8').read()
r1s, r2s = "0,1,4,10,12,17", "0,1,8,11,13,17"
ok8 = all(s in fb.replace(" ", "") for s in (r1s, r2s))
ok8 &= all(s in gr.replace(" ", "") for s in (r1s, r2s))
ok8 &= sorted(g1) == sorted(g2)
check("M8", ok8,
      "CROSS-REFERENCES: the rulers probed here are byte-identical (modulo whitespace) to the "
      "homometric pair in bohr_frequency_probe F6 and to the pair printed in papers/GR.md -- "
      "this probe stress-tests the manuscript's own example, not a private one")

# ---------------------------------------------------------------- M9  the rank census
def golomb_rulers(nn, dmax):
    out = []
    def rec(marks, diffs):
        if len(marks) == nn:
            out.append(tuple(marks))
            return
        for nxt in range(marks[-1] + 1, dmax + 1):
            nd = [nxt - m for m in marks]
            if len(set(nd)) == len(nd) and not (set(nd) & diffs):
                rec(marks + [nxt], diffs | set(nd))
    rec([0], set())
    return out


def rank_census(nn, dmax):
    buckets = {}
    for Rr in golomb_rulers(nn, dmax):
        key = tuple(sorted(Rr[j] - Rr[i] for i, j in itertools.combinations(range(nn), 2)))
        buckets.setdefault(key, []).append(Rr)
    out = []
    for key, group in buckets.items():
        for Aa, Bb in itertools.combinations(group, 2):
            Dd = max(Aa)
            if Bb != Aa and Bb != tuple(sorted(Dd - x for x in Aa)):
                for X, Y in ((Aa, Bb), (Bb, Aa)):
                    gY = {}
                    for cc, dd in itertools.combinations(range(nn), 2):
                        gY[Y[dd] - Y[cc]] = (cc, dd)
                    invm = {gY[X[bb] - X[aa]]: (aa, bb)
                            for aa, bb in itertools.combinations(range(nn), 2)}
                    edges = list(itertools.combinations(range(nn), 2))
                    Nm = [[1 if v in e else 0 for v in range(nn)] for e in edges]
                    Am = [[1 if v in invm[e] else 0 for v in range(nn)] for e in edges]
                    rN, _, _ = rref(Nm)
                    rNA, _, _ = rref([Nm[i] + Am[i] for i in range(len(edges))])
                    out.append((X, Y, rNA - rN))
    return out


census = {}
for nn, dmax in ((4, 20), (5, 25), (6, 32), (7, 36), (8, 40)):
    census[nn] = rank_census(nn, dmax)
ok9 = all(census[nn] == [] for nn in (4, 5, 7, 8))
ok9 &= len(census[6]) == 136
ok9 &= all(r == 5 for _, _, r in census[6])
ok9 &= any(X == tuple(R1) and Y == tuple(R2) for X, Y, _ in census[6])
check("M9", ok9,
      f"THE RANK CENSUS: non-congruent homometric Golomb pairs exist in the enumerated range "
      f"(n = 4..8, diameters up to 20/25/32/36/40) ONLY at n = 6 -- "
      f"{[len(census[nn]) for nn in (4, 5, 6, 7, 8)]} ordered pairs respectively -- and all "
      f"{len(census[6])} of them (the printed pair included) have rank L_mu = 5 = n - 1 "
      f"exactly: the pulled-back K4 exponent relations always cut the modulus locus down to "
      f"the flat row alone. Outcome one of the trichotomy: no exceptional modulus strata, the "
      f"universal two-branch statement stays the target")

# ---------------------------------------------------------------- M10  the orbit census
EDGES6 = list(itertools.combinations(range(6), 2))


def forced_mu6(Aa, Bb):
    gB = {}
    for cc, dd in itertools.combinations(range(6), 2):
        gB[Bb[dd] - Bb[cc]] = (cc, dd)
    return {(a, b): gB[Aa[b] - Aa[a]] for a, b in itertools.combinations(range(6), 2)}


def induced_tau6(g):
    tau = [None] * 6
    for v in range(6):
        s1 = set(g[tuple(sorted((v, (v + 1) % 6)))])
        s2 = set(g[tuple(sorted((v, (v + 2) % 6)))])
        common = s1 & s2
        if len(common) != 1:
            return None
        tau[v] = common.pop()
    if len(set(tau)) != 6:
        return None
    for e in EDGES6:
        if tuple(sorted(g[e])) != tuple(sorted((tau[e[0]], tau[e[1]]))):
            return None
    return tuple(tau)


def conjugate6(mua, mub):
    mu_u = {e: tuple(sorted(mua[e])) for e in EDGES6}
    nu_u = {e: tuple(sorted(mub[e])) for e in EDGES6}
    for sigma in itertools.permutations(range(6)):
        g = {}
        ok = True
        for e in EDGES6:
            se = tuple(sorted((sigma[e[0]], sigma[e[1]])))
            key = mu_u[e]
            val = nu_u[se]
            if key in g and g[key] != val:
                ok = False
                break
            g[key] = val
        if not ok or len(set(g.values())) != 15:
            continue
        if induced_tau6(g) is not None:
            return True
    return False


all_mus = []
for X, Y, _ in census[6]:
    all_mus.append(((X, Y), forced_mu6(X, Y)))
orbits = []
for pair, mm in all_mus:
    for orb in orbits:
        if conjugate6(orb[1], mm):
            orb[2].append(pair)
            break
    else:
        orbits.append([pair, mm, [pair]])
printed_mu = forced_mu6(tuple(R1), tuple(R2))
inv_printed = {tuple(sorted(v)): k for k, v in printed_mu.items()}
ok10 = len(orbits) == 1 and len(orbits[0][2]) == 136
ok10 &= conjugate6(orbits[0][1], printed_mu)
ok10 &= conjugate6(orbits[0][1], inv_printed)
# realization space of the orbit: E'_d - E'_c = E_b - E_a on all 15 edges
rl_rows = []
for (a, b), (c, d) in printed_mu.items():
    row = [0] * 12
    row[a] += 1
    row[b] -= 1
    row[6 + c] -= 1
    row[6 + d] += 1
    rl_rows.append(row)
real_dim = len(nullspace(rl_rows))
ok10 &= real_dim == 4
check("M10", ok10,
      f"THE ORBIT CENSUS: under source/target vertex relabeling all {len(all_mus)} census "
      f"correspondences form {len(orbits)} orbit(s); the printed mu AND its inverse lie in it. "
      f"Its exact realization space has dimension {real_dim} = 2 translations + 2 genuine "
      f"parameters -- the known continuous two-parameter six-mark family, re-derived "
      f"independently. The kill chain consumes only mu's combinatorics and relabeling is a "
      f"symmetry of every stage, so the kernel-proved flat_locus and clique obstruction apply "
      f"verbatim across the entire family: u, v never enter the coefficient reconstruction")

# ------------------------------------------------- M11  the parametric mu-orbit bridge (exact)
# The exceptional-family formula as QUOTED by a later peer-reviewed treatment citing
# Bekir-Golomb 2007 (the primary text is not yet audited; this check is about the quoted
# formula). Linear forms c0 + c1*p1 + c2*p2 as exact coefficient triples.
ok11 = True
PX = [(0, 0, 0), (0, 1, 0), (0, -2, 1), (0, -2, 2), (0, 0, 2), (0, -1, 3)]
PY = [(0, 0, 0), (0, 1, 0), (0, 2, 1), (0, 1, 2), (0, -1, 2), (0, -1, 3)]


def fsub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def fev(u, p1, p2):
    return u[0] + u[1] * p1 + u[2] * p2


SWAP34 = (0, 1, 2, 4, 3, 5)
# all 15 gap identities hold SYMBOLICALLY with e_S = id, e_T = (3 4)
for (a, b), (c, d) in printed_mu.items():
    ok11 &= fsub(PY[SWAP34[d]], PY[SWAP34[c]]) == fsub(PX[b], PX[a])
# (3 4) is the UNIQUE target relabeling that works; the identity fails without it
good = [s for s in itertools.permutations(range(6))
        if all(fsub(PY[s[d]], PY[s[c]]) == fsub(PX[b], PX[a])
               for (a, b), (c, d) in printed_mu.items())]
ok11 &= good == [SWAP34]
ok11 &= sum(1 for (a, b), (c, d) in printed_mu.items()
            if fsub(PY[d], PY[c]) != fsub(PX[b], PX[a])) == 9
# both families are symbolically Golomb: no two of the 15 ascending gap forms agree, in
# either sign -- so gap collisions happen only on finitely many lines in the (p1,p2) plane
for F in (PX, PY):
    gset = [fsub(F[b], F[a]) for a, b in itertools.combinations(range(6), 2)]
    ok11 &= len(set(gset)) == 15
    ok11 &= not any(g == tuple(-x for x in h)
                    for i, g in enumerate(gset) for h in gset[i:])
# the printed pair is the specialization p = (1, 6), with Y listed = sorted r2 o (3 4)
ok11 &= [fev(x, 1, 6) for x in PX] == list(R1)
ok11 &= [fev(y, 1, 6) for y in PY] == [R2[SWAP34[i]] for i in range(6)]
# countercontrol: perturbing one quoted coefficient breaks at least one identity symbolically
PYbad = PY[:2] + [(0, 2, 2)] + PY[3:]
ok11 &= any(fsub(PYbad[SWAP34[d]], PYbad[SWAP34[c]]) != fsub(PX[b], PX[a])
            for (a, b), (c, d) in printed_mu.items())
check("M11", ok11,
      "THE PARAMETRIC MU-ORBIT BRIDGE, exact: the quoted Bekir-Golomb exceptional family "
      "X = {0, p1, p2-2p1, 2p2-2p1, 2p2, 3p2-p1}, Y = {0, p1, 2p1+p2, p1+2p2, 2p2-p1, 3p2-p1} "
      "satisfies all 15 gap identities of the printed mu with e_S = id and the single target "
      "transposition e_T = (3 4), as polynomial identities in (p1, p2) -- and (3 4) is the "
      "UNIQUE relabeling that works (9 of 15 fail without it). Both families are symbolically "
      "Golomb, p = (1, 6) reduces to the printed pair, and a perturbed coefficient breaks the "
      "bridge. Kernel twin: OIBridge/PiccardBridge.lean (piccard_mu_bridge over any CommRing). "
      "The formula is confirmed against the primary 2007 text by M12")

# --------------------------------------- M12  the primary factorization expands to the family
# Bekir-Golomb 2007, p. 2865: r = Phi1*Phi2, s = Phi1*Phi2star with
#   Phi1 = 1 + x^a + x^b,  Phi2 = 1 + x^{b-2a} - x^{b-a} + x^{2b-a},
#   Phi2star = 1 - x^b + x^{b+a} + x^{2b-a}  (the reversal of Phi2).
# Exact arithmetic in the group algebra Z[x^{Z + Za + Zb}]: exponents are integer forms
# (c0, ca, cb) meaning c0 + ca*a + cb*b, coefficients are integers.
ok12 = True


def gmul(P, Q):
    R = {}
    for e1, c1 in P.items():
        for e2, c2 in Q.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            R[e] = R.get(e, 0) + c1 * c2
    return {e: c for e, c in R.items() if c != 0}


PHI1 = {(0, 0, 0): 1, (0, 1, 0): 1, (0, 0, 1): 1}
PHI2 = {(0, 0, 0): 1, (0, -2, 1): 1, (0, -1, 1): -1, (0, -1, 2): 1}
PHI2S = {(0, 0, 0): 1, (0, 0, 1): -1, (0, 1, 1): 1, (0, -1, 2): 1}
rpoly = gmul(PHI1, PHI2)
spoly = gmul(PHI1, PHI2S)
# the expansions are 0/1 polynomials whose exponent sets are EXACTLY the quoted families
ok12 &= rpoly == {e: 1 for e in [(0, 0, 0), (0, 1, 0), (0, -2, 1), (0, -2, 2),
                                 (0, 0, 2), (0, -1, 3)]}
ok12 &= spoly == {e: 1 for e in [(0, 0, 0), (0, 1, 0), (0, 2, 1), (0, 1, 2),
                                 (0, -1, 2), (0, -1, 3)]}
ok12 &= sorted(rpoly) == sorted(PX) and sorted(spoly) == sorted(PY)
# Phi2star is the reversal x^{2b-a} * Phi2(1/x)
ok12 &= {tuple(d - e for d, e in zip((0, -1, 2), exp)): c
         for exp, c in PHI2.items()} == PHI2S
# (a, b) = (1, 6) gives the paper's p. 2864 printed factorizations and the printed pair


def gev(P, a, b):
    R = {}
    for (c0, ca, cb), c in P.items():
        e = c0 + ca * a + cb * b
        R[e] = R.get(e, 0) + c
    return {e: c for e, c in R.items() if c != 0}


ok12 &= gev(PHI2, 1, 6) == {0: 1, 4: 1, 5: -1, 11: 1}
ok12 &= gev(PHI2S, 1, 6) == {0: 1, 6: -1, 7: 1, 11: 1}
ok12 &= sorted(gev(rpoly, 1, 6)) == list(R1) and all(c == 1 for c in gev(rpoly, 1, 6).values())
ok12 &= sorted(gev(spoly, 1, 6)) == list(R2) and all(c == 1 for c in gev(spoly, 1, 6).values())
# countercontrol: flipping the negative sign in Phi2 leaves an 8-term signed expansion --
# NOT a spanning-ruler polynomial, so the printed cancellation is load-bearing
PHI2BAD = dict(PHI2)
PHI2BAD[(0, -1, 1)] = 1
rbad = gmul(PHI1, PHI2BAD)
ok12 &= (len(rbad) != 6 or any(c != 1 for c in rbad.values()))
check("M12", ok12,
      "THE PRIMARY FACTORIZATION (Bekir-Golomb 2007, p. 2865) EXPANDS TO THE FAMILY, exact: "
      "Phi1*Phi2 and Phi1*Phi2star, computed in the group algebra with symbolic exponents "
      "(a, b), are 0/1 polynomials whose exponent sets are EXACTLY the quoted X and Y of M11 "
      "-- the mixed terms cancel in pairs; Phi2star is the reversal of Phi2; (a, b) = (1, 6) "
      "reproduces the paper's printed p. 2864 factorizations and the printed pair; flipping "
      "the one negative coefficient destroys the six-term cancellation. Kernel twins: "
      "piccard_factor_r / piccard_factor_s / piccardX_marks / piccardY_marks in "
      "OIBridge/PiccardBridge.lean, in chamber coordinates s = x^p1, t = x^(p2-2p1)")

print()
print('     [scope] Settled exactly, at probe level: (i) n = 4 -- every labeled correspondence')
print('     for the Golomb spectrum {0,1,4,6} is a relabeling or the reversal, exhaustively;')
print('     (ii) n = 6 -- the unique forced non-two-branch correspondence (the printed')
print('     homometric pair) admits NO realizing pair of eigenbases: generic moduli violate')
print('     explicit cokernel identities, the exceptional locus is exactly the flat rows, and')
print('     on it joint unitarity is blocked by a max-clique-3 bound over the 8 common mask')
print('     zeros. The n = 6 kill chain checked here numerically is now ALSO a kernel theorem:')
print('     OIBridge/HomometricKill.lean assembles homometricSix_unrealizable end to end, the')
print('     congruent-case assembly and the Fourier layer are kernel-closed, and the parametric')
print('     mu-orbit bridge to the quoted exceptional family is kernel-proved over any CommRing')
print('     (OIBridge/PiccardBridge.lean, probe twins M11/M12). The primary 2007 text has been')
print('     read: its exceptional-family formula is confirmed exactly (M12), its equivalence')
print('     notion (identical or mirror image) and distinct-difference hypothesis match the')
print('     Claim, and its classification argument is the cited external step. NOT settled:')
print('     the real-vs-integer scope reading of the primary text (its polynomial model is')
print('     integer-presented; the audit finding and the candidate closures are recorded in')
print('     the ledger) and strata where some overlaps V_ia vanish (the Claim assumes nonzero')
print('     overlaps); the Claim stays P-grade until the consumption decision is taken.')
print()
print("gap_correspondence_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
