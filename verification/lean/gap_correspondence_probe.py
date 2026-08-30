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

print()
print('     [scope] Settled exactly, at probe level: (i) n = 4 -- every labeled correspondence')
print('     for the Golomb spectrum {0,1,4,6} is a relabeling or the reversal, exhaustively;')
print('     (ii) n = 6 -- the unique forced non-two-branch correspondence (the printed')
print('     homometric pair) admits NO realizing pair of eigenbases: generic moduli violate')
print('     explicit cokernel identities, the exceptional locus is exactly the flat rows, and')
print('     on it joint unitarity is blocked by a max-clique-3 bound over the 8 common mask')
print('     zeros. NOT settled: the universal claim for all n (these are two instances, not an')
print('     induction); strata where some overlaps V_ia vanish (the Claim assumes nonzero')
print('     overlaps, and the modulus-lattice argument here uses positivity); and the kernel')
print('     formalization itself -- the Claim stays P-grade until the classification is a Lean')
print('     theorem. The kill chain above is the candidate theorem statement.')
print()
print("gap_correspondence_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
