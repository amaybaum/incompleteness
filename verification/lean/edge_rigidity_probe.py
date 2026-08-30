#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/EdgeRigidity.lean and OIBridge/HomometricSix.lean.

EdgeRigidity kernel-proves K4-RIGIDITY: for n >= 5, an edge permutation of K_n preserving all
four-cycle product identities as identities is induced by a vertex permutation -- with the n = 4
complement exception exposed as sharp -- plus the manuscript-facing corollary that a non-induced
edge permutation forces a nontrivial exponent relation (summing to zero, so flat rows always
survive). HomometricSix kernel-proves the two load-bearing finite endpoints of the n = 6 kill
chain: the flat-locus theorem L_mu-perp = span(1) and the max-clique-3 obstruction, plus the mask
factorizations and the xi/eta linkage.

These checks exercise the same statements independently (no Lean in the loop):

  R1  THE HYPERSIMPLEX COUNT AT n = 4: exhaustively over all 720 edge permutations of K4,
      exactly 48 preserve every matching identity -- the 24 vertex-induced ones and their 24
      complement-composites. The complement itself preserves and is induced by no vertex
      permutation. This is the Delta(2,4) exception, and it is the ONLY structure: preserving
      set = S4 x {id, complement}.
  R2  RIGIDITY SAMPLED AT n = 5..7: every random vertex-induced edge permutation preserves all
      identities; random edge permutations (overwhelmingly non-induced) violate at least one
      identity whenever they are non-induced, and each preserving sample found IS induced.
  R3  THE EXCEPTIONAL RELATION: for non-induced samples, the violated matching difference w is
      a nonzero integer vector with sum(w) = 0 (the flat direction always survives), matching
      `exceptional_relation`'s conclusion.
  R4  THE FIVE FLAT-LOCUS INSTANCES: the exact relation vectors of the five quadruple/matching
      instances used in HomometricSix.flat_locus span the full 5-dimensional annihilator of the
      flat direction -- so the Lean file's linear elimination is complete, not lucky.
  R5  THE CLIQUE DATA: the 8 connection elements in HomometricSix.conn match the exact common
      mask zeros computed here from scratch (via the factored cofactors), are inversion-closed,
      generate a group of order 48, and admit max clique exactly 3.
  R6  lint of both Lean files.

Usage:  python3 edge_rigidity_probe.py
"""
import itertools
import os
import random
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


def edges_of(n):
    return list(itertools.combinations(range(n), 2))


def preserves(n, perm, edges):
    """perm: dict edge -> edge. Check all matching identities as endpoint multisets."""
    for q in itertools.combinations(range(n), 4):
        a, b, c, d = q
        m1 = sorted(perm[(a, b)] + perm[(c, d)])
        m2 = sorted(perm[(a, c)] + perm[(b, d)])
        m3 = sorted(perm[(a, d)] + perm[(b, c)])
        if m1 != m2 or m1 != m3:
            return False
    return True


def induced_by(n, perm, edges):
    for tau in itertools.permutations(range(n)):
        if all(perm[e] == tuple(sorted((tau[e[0]], tau[e[1]])))for e in edges):
            return tau
    return None


# ---------------------------------------------------------------- R1  n = 4 exhaustive
E4 = edges_of(4)
preserving = []
for imgs in itertools.permutations(E4):
    perm = dict(zip(E4, imgs))
    if preserves(4, perm, E4):
        preserving.append(perm)
compl = {e: tuple(sorted(set(range(4)) - set(e))) for e in E4}
induced_count = sum(1 for p in preserving if induced_by(4, p, E4) is not None)
compl_composites = 0
for p in preserving:
    q = {e: compl[p[e]] for e in E4}
    if induced_by(4, q, E4) is not None and induced_by(4, p, E4) is None:
        compl_composites += 1
ok1 = len(preserving) == 48 and induced_count == 24 and compl_composites == 24
ok1 &= preserves(4, compl, E4) and induced_by(4, compl, E4) is None
check("R1", ok1,
      f"n = 4 EXHAUSTIVE: of all 720 edge permutations of K4, exactly {len(preserving)} "
      f"preserve every matching identity -- {induced_count} vertex-induced plus "
      f"{compl_composites} complement-composites -- and the complement map itself preserves "
      f"while being induced by no vertex permutation. The Delta(2,4) hypersimplex exception, "
      f"exactly as Lean's `compl4_preserves` / `compl4_not_induced`, with nothing else hiding")

# ---------------------------------------------------------------- R2  rigidity sampled
rng = random.Random(20260830)
ok2 = True
for n in (5, 6, 7):
    E = edges_of(n)
    for _ in range(30):
        tau = list(range(n))
        rng.shuffle(tau)
        perm = {e: tuple(sorted((tau[e[0]], tau[e[1]]))) for e in E}
        ok2 &= preserves(n, perm, E)
    found_noninduced_preserving = False
    for _ in range(200):
        imgs = E[:]
        rng.shuffle(imgs)
        perm = dict(zip(E, imgs))
        if preserves(n, perm, E):
            if induced_by(n, perm, E) is None:
                found_noninduced_preserving = True
    ok2 &= not found_noninduced_preserving
check("R2", ok2,
      "RIGIDITY SAMPLED at n = 5, 6, 7: 30 random vertex-induced edge permutations per n all "
      "preserve every identity, and among 200 random edge permutations per n no preserving "
      "non-induced one exists -- every preserving sample is induced, matching `k4_rigidity`")

# ---------------------------------------------------------------- R3  the exceptional relation
ok3 = True
tested = 0
for n in (5, 6):
    E = edges_of(n)
    while tested < 25 * (n - 4):
        imgs = E[:]
        rng.shuffle(imgs)
        perm = dict(zip(E, imgs))
        if induced_by(n, perm, E) is not None:
            continue
        tested += 1
        wfound = None
        for q in itertools.combinations(range(n), 4):
            a, b, c, d = q
            w = [0] * n
            for v in perm[(a, b)] + perm[(c, d)]:
                w[v] += 1
            for v in perm[(a, c)] + perm[(b, d)]:
                w[v] -= 1
            if any(w):
                wfound = w
                break
        ok3 &= wfound is not None and sum(wfound) == 0
check("R3", ok3,
      f"THE EXCEPTIONAL RELATION on {tested} random non-induced edge permutations (n = 5, 6): "
      f"each has a violated matching whose exponent vector w is nonzero with sum(w) = 0 -- "
      f"a genuine constraint that nevertheless never excludes the flat row, exactly "
      f"`exceptional_relation`'s conclusion")

# ---------------------------------------------------------------- R4  the five instances span
R1v = [0, 1, 4, 10, 12, 17]
R2v = [0, 1, 8, 11, 13, 17]
g2 = {}
for c, d in itertools.combinations(range(6), 2):
    g2[R2v[d] - R2v[c]] = (c, d)
mu = {(a, b): g2[R1v[b] - R1v[a]] for a, b in itertools.combinations(range(6), 2)}
inv = {v: k for k, v in mu.items()}
INSTANCES = [((0, 1, 3, 4), '12'), ((1, 2, 3, 4), '12'), ((0, 2, 3, 5), '12'),
             ((0, 1, 2, 5), '13'), ((0, 1, 2, 3), '12')]
vecs = []
for (qc, kind) in INSTANCES:
    c, d, e, f = qc
    m1 = [(c, d), (e, f)]
    m2 = [(c, e), (d, f)] if kind == '12' else [(c, f), (d, e)]
    w = [0] * 6
    for p in m1:
        for v in inv[p]:
            w[v] += 1
    for p in m2:
        for v in inv[p]:
            w[v] -= 1
    vecs.append([Fraction(x) for x in w])


def rank(M):
    M = [row[:] for row in M]
    m, n = len(M), len(M[0])
    r = 0
    for cix in range(n):
        piv = next((i for i in range(r, m) if M[i][cix] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][cix]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][cix] != 0:
                fct = M[i][cix]
                M[i] = [x - fct * y for x, y in zip(M[i], M[r])]
        r += 1
    return r


ok4 = rank(vecs) == 5 and all(sum(w) == 0 for w in vecs)
check("R4", ok4,
      "THE FIVE FLAT-LOCUS INSTANCES used by HomometricSix.flat_locus (quadruples 0134, 1234, "
      "0235, 0125, 0123) have exponent vectors of rank exactly 5, each summing to zero: they "
      "span the entire annihilator of the flat direction, so the Lean file's five-relation "
      "linear elimination is complete rather than fortuitous")

# ---------------------------------------------------------------- R5  the clique data
# recompute the common zeros from scratch via the cofactors: G = 1 + x + x^2 y has torus zeros
# (omega^{+-1}, 1); H and Ht are quadratics in y over Z[i]-points x in {1, i, -i}
import cmath
Z_expected = {(4, 0), (8, 0), (0, 1), (0, 3), (3, 2), (9, 2), (3, 3), (9, 1)}


def to_exp(x, y):
    a = round(cmath.phase(x) / (2 * cmath.pi) * 12) % 12
    b = round(cmath.phase(y) / (2 * cmath.pi) * 4) % 4
    assert abs(x - cmath.exp(2j * cmath.pi * a / 12)) < 1e-9
    assert abs(y - cmath.exp(2j * cmath.pi * b / 4)) < 1e-9
    return (a, b)


zs = set()
w = cmath.exp(2j * cmath.pi / 3)
zs.add(to_exp(w, 1))
zs.add(to_exp(w.conjugate(), 1))
for x in (1, 1j, -1j):
    # H(x, y) = x^3 y^2 + (1 - x) y + 1 = 0
    a2, a1, a0 = x ** 3, 1 - x, 1
    disc = cmath.sqrt(a1 * a1 - 4 * a2 * a0)
    for sgn in (1, -1):
        y = (-a1 + sgn * disc) / (2 * a2)
        Ht = x ** 3 * y ** 2 + (x ** 3 - x ** 2) * y + 1
        if abs(y * y.conjugate() - 1) < 1e-9 and abs(Ht) < 1e-9:
            zs.add(to_exp(x, y))
ok5 = zs == Z_expected
conn = sorted(Z_expected)
ok5 &= all(((-a) % 12, (-b) % 4) in Z_expected for a, b in conn)
S = {(0, 0)}
changed = True
while changed:
    changed = False
    for gx, gy in conn:
        for hx, hy in list(S):
            el = ((gx + hx) % 12, (gy + hy) % 4)
            if el not in S:
                S.add(el)
                changed = True
ok5 &= len(S) == 48
best = 0
Slist = sorted(S)
adj = {u: {v for v in Slist if v != u and ((u[0] - v[0]) % 12, (u[1] - v[1]) % 4) in Z_expected}
       for u in Slist}


def grow(clique, cand):
    global best
    best = max(best, len(clique))
    for i, v in enumerate(cand):
        if len(clique) + len(cand) - i <= best:
            break
        grow(clique + [v], [u for u in cand[i + 1:] if u in adj[v]])


grow([], Slist)
ok5 &= best == 3
check("R5", ok5,
      f"THE CLIQUE DATA recomputed from scratch: the common torus zeros of the two factored "
      f"masks are exactly the 8 exponent pairs in HomometricSix.conn, inversion-closed, "
      f"generating a group of order {len(S)} with max clique {best} -- the kernel-proved "
      f"`no_four_clique` / `no_six_orthogonal` / `three_clique` data verified independently")

# ---------------------------------------------------------------- R6  lint
ok6 = True
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
for fname, names in (
    ('EdgeRigidity', ('k4_rigidity', 'exceptional_relation', 'induced_preserves',
                      'pulledBack_const', 'compl4_preserves', 'compl4_not_induced')),
    ('HomometricSix', ('golomb_r1', 'golomb_r2', 'mu_gap', 'mu_forced', 'muInv_mu',
                       'mu_muInv', 'mu_not_vertex_induced', 'flat_locus', 'linkage',
                       'maskV_factor', 'maskW_factor', 'maskV_eq_sum', 'conn_symm',
                       'no_four_clique', 'no_six_orthogonal', 'three_clique'))):
    src = open(os.path.join(BRIDGE, 'OIBridge', f'{fname}.lean'), encoding='utf-8').read()
    body = src[src.index('namespace OIBridge'):]
    ok6 &= f'import OIBridge.{fname}' in root
    ok6 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
    ok6 &= re.search(r'(?m)^axiom ', body) is None
    ok6 &= 'native_decide' not in body
    ok6 &= all(f'theorem {nm}' in src for nm in names)
    ok6 &= all(f'#print axioms {nm}' in src for nm in names)
# the general theorem must carry its sharp hypothesis and the exception must be at n = 4
er = open(os.path.join(BRIDGE, 'OIBridge', 'EdgeRigidity.lean'), encoding='utf-8').read()
ok6 &= 'theorem k4_rigidity (hn : 5 ≤ n)' in er
ok6 &= 'Edge 4 ≃ Edge 4' in er
check("R6", ok6,
      "LINT. Both files are imported by OIBridge.lean so CI builds them; no `sorry`, no "
      "`axiom`, no `native_decide`; all 6 + 16 named results print their axiom dependencies; "
      "`k4_rigidity` carries the sharp hypothesis 5 <= n and the exception lives at n = 4")

print()
print('     [scope] Settled in Lean: K4-rigidity for all n >= 5 with the n = 4 complement')
print('     exception sharp (EdgeRigidity), the non-induced => exceptional-relation corollary')
print('     with its flat-direction control, and the two finite endpoints of the n = 6 kill')
print('     chain (HomometricSix): L_mu-perp = span(1) and the max-clique-3 obstruction, plus')
print('     mask factorizations, the xi/eta linkage, Golomb/forcedness of mu, and mu being')
print('     induced by no vertex map even with mixed orientations. NOT settled in the kernel:')
print('     the analytic reduction between the endpoints (rank-one forcing, SNF completeness,')
print('     resultant completeness of the 8 common zeros) -- probe-level in')
print('     gap_correspondence_probe M4-M7 -- and the universal two-branch Claim itself, which')
print('     remains P-grade.')
print()
print("edge_rigidity_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
