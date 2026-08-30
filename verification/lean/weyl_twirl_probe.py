#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/WeylTwirl.lean.

LAYER 1 of [Main] Theorem (separability threshold): the symplectic phase space, the Weyl
operators, and the exact twirl identity

    Phi_G(W v) = W v   if v in G-perp,      0 otherwise.

Everything here is exact finite algebra over the integers -- no floating point anywhere, since
every quantity is a signed integer matrix entry. Checks are EXHAUSTIVE at s = 1 and s = 2: all 4
and all 16 phase-space vectors, and all isotropic subspaces.

  W1  the Weyl product rule  W u W v = (-1)^{u2.v1} W(u+v),  every pair.
  W2  the conjugation character  W u W v W u^dagger = (-1)^{omega(u,v)} W v,  every pair -- the
      identity the whole theorem runs on.
  W3  commutation is exactly vanishing of the symplectic form, every pair.
  W4  the twirl identity, for every isotropic subspace and every Weyl operator.
  W5  COUNTERCONTROL for the subgroup hypothesis: over a subset that is not closed under addition
      the character sum is not |S| or 0, and the twirl is not a projection.
  W6  COUNTERCONTROL for the modelling choice: {X^a Z^b} is NOT closed under multiplication --
      (XZ)^2 = -1 -- so "a subgroup of order 2^t" is not a statement about that set, which is why
      the Lean file takes an isotropic SUBSPACE and not a Pauli subgroup.
  W7  the dimension count  dim G-perp = 2s - dim G,  and G isotropic iff G <= G-perp.
  W8  the self-adjoint normalization H(u) = i^{b.a} W(u): Hermitian, squaring to 1, and commuting
      whenever omega vanishes -- the interface the maximal-isotropic diagonalization will consume.
  W9  lint.

Usage:  python3 weyl_twirl_probe.py
"""
import itertools
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


# ---------------------------------------------------------------- exact integer matrices
def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def dagger(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A))]     # real entries


def dagger_c(A):
    """Conjugate transpose, for the complex-valued H below."""
    return [[A[j][i].conjugate() if isinstance(A[j][i], complex) else A[j][i]
             for j in range(len(A))] for i in range(len(A))]


def scal(c, A):
    return [[c * x for x in row] for row in A]


def add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def eq(A, B):
    return all(a == b for ra, rb in zip(A, B) for a, b in zip(ra, rb))


def zeros(n):
    return [[0] * n for _ in range(n)]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) % 2


def omega(u, v, s):
    return (dot(u[s:], v[:s]) + dot(v[s:], u[:s])) % 2


def W(u, s):
    """X^a Z^b as an exact +-1/0 integer matrix, in the same convention as the Lean file:
    entry (x, y) is (-1)^{b.y} when x = y + a and 0 otherwise."""
    d = 2 ** s
    bits = [tuple(int(c) for c in format(k, '0%db' % s)) for k in range(d)]
    idx = {b: k for k, b in enumerate(bits)}
    a, b = u[:s], u[s:]
    M = zeros(d)
    for k, y in enumerate(bits):
        x = tuple((y[i] + a[i]) % 2 for i in range(s))
        M[idx[x]][k] = -1 if dot(b, y) else 1
    return M


def phase_space(s):
    return [tuple(int(c) for c in format(k, '0%db' % (2 * s))) for k in range(4 ** s)]


def subspaces(s):
    n = 2 * s
    seen = {}
    vecs = phase_space(s)
    for r in range(n + 1):
        for gens in itertools.combinations(vecs[1:], r):
            span = {tuple([0] * n)}
            for g in gens:
                span |= {tuple((x[i] + g[i]) % 2 for i in range(n)) for x in span}
            seen[frozenset(span)] = None
    return [sorted(S) for S in seen]


# ---------------------------------------------------------------- W1 / W2 / W3
ok1 = ok2 = ok3 = True
for s in (1, 2):
    PS = phase_space(s)
    for u in PS:
        Wu = W(u, s)
        for v in PS:
            Wv, uv = W(v, s), tuple((u[i] + v[i]) % 2 for i in range(2 * s))
            sign = -1 if dot(u[s:], v[:s]) else 1
            ok1 &= eq(mat_mul(Wu, Wv), scal(sign, W(uv, s)))
            csign = -1 if omega(u, v, s) else 1
            ok2 &= eq(mat_mul(mat_mul(Wu, Wv), dagger(Wu)), scal(csign, Wv))
            ok3 &= (eq(mat_mul(Wu, Wv), mat_mul(Wv, Wu))) == (omega(u, v, s) == 0)
check("W1", ok1,
      "THE WEYL PRODUCT RULE, exhaustively at s = 1 and s = 2 (all 4 and all 16 phase-space "
      "vectors, so 16 + 256 pairs): W u . W v = (-1)^{u2.v1} W(u+v), in exact integer arithmetic. "
      "This is Lean's `W_mul`")
check("W2", ok2,
      "THE CONJUGATION CHARACTER, over the same 272 pairs: W u . W v . W u^dagger = "
      "(-1)^{omega(u,v)} W v. This single identity is what both halves of the separability theorem "
      "run on, and it is what makes the twirl a projection onto the symplectic complement. Lean's "
      "`W_conj`")
check("W3", ok3,
      "COMMUTATION IS THE SYMPLECTIC FORM, over the same pairs and in both directions: two Weyl "
      "operators commute exactly when omega vanishes. This is the bridge from the manuscript's "
      "'abelian' to the Lean file's 'isotropic' -- `W_commute_iff` there, and `isotropic_iff_commute` "
      "on top of it")

# ---------------------------------------------------------------- W4  the twirl identity
ok4 = True
counts = {}
for s in (1, 2):
    d = 2 ** s
    PS = phase_space(s)
    for G in subspaces(s):
        if any(omega(u, v, s) for u in G for v in G):
            continue                                        # isotropic only
        counts.setdefault((s, len(G)), 0)
        counts[(s, len(G))] += 1
        perp = [v for v in PS if all(omega(u, v, s) == 0 for u in G)]
        for v in PS:
            Wv = W(v, s)
            acc = zeros(d)
            for g in G:
                Wg = W(g, s)
                acc = add(acc, mat_mul(mat_mul(Wg, Wv), dagger(Wg)))
            # the twirl divides by |G|; the sum is |G| * (result), exactly
            target = scal(len(G), Wv) if v in perp else zeros(d)
            ok4 &= eq(acc, target)
check("W4", ok4,
      f"THE TWIRL IDENTITY, for EVERY isotropic subspace at s = 1 and s = 2 and every Weyl "
      f"operator: the mixture fixes W v when v lies in the symplectic complement and annihilates "
      f"it otherwise. Isotropic subspace counts by dimension: "
      f"{ {k: v for k, v in sorted(counts.items())} } — 1/3 at s=1 and 1/15/15 at s=2, the second "
      f"matching the 15 Lagrangians of Sp(4,2) = (2+1)(2^2+1). Lean's `twirl_W`")

# ---------------------------------------------------------------- W5  the subgroup hypothesis
# The identity is character orthogonality and needs G closed under addition. Over a subset that is
# not, the sum is neither |S| nor 0.
s = 2
PS = phase_space(s)
S = [(0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0)]        # closed under nothing: (1,0,0,0)+(0,1,0,0) missing
ok5 = any(tuple((S[1][i] + S[2][i]) % 2 for i in range(4)) not in S for _ in (0,))
bad = []
for v in PS:
    tot = sum(-1 if omega(g, v, s) else 1 for g in S)
    if tot not in (0, len(S)):
        bad.append((v, tot))
ok5 &= len(bad) > 0
# and the twirl over that subset is not idempotent as a map on Weyl operators
d = 2 ** s
v0 = bad[0][0]
acc = zeros(d)
for g in S:
    Wg = W(g, s)
    acc = add(acc, mat_mul(mat_mul(Wg, W(v0, s)), dagger(Wg)))
ok5 &= not eq(acc, scal(len(S), W(v0, s))) and not eq(acc, zeros(d))
check("W5", ok5,
      f"COUNTERCONTROL for the subgroup hypothesis. The twirl identity is character orthogonality, "
      f"and it needs G closed under addition. Over the subset {{00,X1,X2}} — which omits "
      f"X1+X2 — the character sum takes the value {bad[0][1]} at some v, neither |S| = {len(S)} nor "
      f"0, and the mixture there is neither W v scaled nor zero. So `char_sum` genuinely uses "
      f"`G.add_mem`, and the Lean statement is over a `Submodule` rather than a `Finset`")

# ---------------------------------------------------------------- W6  the modelling choice
# {X^a Z^b} is not closed under multiplication: (XZ)^2 = -1. So "a subgroup of order 2^t" is not a
# statement about that set, which is why the Lean file uses an isotropic SUBSPACE.
s = 1
XZ = W((1, 1), 1)
sq = mat_mul(XZ, XZ)
ok6 = eq(sq, scal(-1, W((0, 0), 1)))
ok6 &= not any(eq(sq, W(u, 1)) for u in phase_space(1))     # the square is NOT a Weyl operator
# whereas the phase-space image IS closed: (1,1) + (1,1) = (0,0)
ok6 &= tuple((1 + 1) % 2 for _ in range(2)) == (0, 0)
check("W6", ok6,
      "COUNTERCONTROL for the modelling choice. (XZ)^2 = -1, which is NOT in {X^a Z^b}: that set "
      "is not closed under multiplication, so 'an abelian subgroup of the Weyl group of order 2^t' "
      "is not a statement about it and the phrase 'modulo phases' in the manuscript is doing real "
      "work. The phase-space image IS closed — (1,1) + (1,1) = (0,0) — which is why the Lean file "
      "represents G as an isotropic subspace of F_2^{2s} and never forms a quotient")

# ---------------------------------------------------------------- W7  dimensions
ok7 = True
for s in (1, 2):
    PS = phase_space(s)
    for G in subspaces(s):
        perp = [v for v in PS if all(omega(u, v, s) == 0 for u in G)]
        # perp is a subspace of the complementary dimension
        ok7 &= all(tuple((x[i] + y[i]) % 2 for i in range(2 * s)) in perp for x in perp for y in perp)
        ok7 &= len(G) * len(perp) == 4 ** s
        iso = not any(omega(u, v, s) for u in G for v in G)
        ok7 &= iso == all(g in perp for g in G)
        # the double complement returns G exactly
        pp = [v for v in PS if all(omega(u, v, s) == 0 for u in perp)]
        ok7 &= sorted(pp) == sorted(G)
        if iso:
            ok7 &= len(G) <= 2 ** s                       # the t <= s bound
            # maximality is exactly self-duality
            ok7 &= (len(G) == 2 ** s) == (sorted(perp) == sorted(G))
            # and below maximality the anticommuting partner is guaranteed inside G-perp
            for v in perp:
                if v not in G:
                    ok7 &= any(omega(v, w, s) == 1 for w in perp)
check("W7", ok7,
      "THE DIMENSION COUNT. For every subspace at s = 1, 2: the symplectic complement is a "
      "subspace, |G| . |G-perp| = 4^s so dim G-perp = 2s - dim G, and G is isotropic exactly when "
      "G <= G-perp — which is Lean's `isotropic_iff_le_perp`. Isotropy then forces t <= s, the "
      "bound the manuscript reads off first; |G| = 2^s holds exactly when G-perp = G; and "
      "(G-perp)-perp = G, so any v in G-perp outside G has an anticommuting partner inside G-perp "
      "— the witness the non-maximal direction will be built from")

# ---------------------------------------------------------------- W8  the H interface
def Hop(u, s):
    """H(u) = i^{b.a} W(u), as an exact Gaussian-integer matrix (entries in Z[i])."""
    ph = 1j if dot(u[s:], u[:s]) else 1
    return [[ph * v for v in row] for row in W(u, s)]


ok8 = True
nontrivial = 0
for s in (1, 2):
    d = 2 ** s
    ident = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    for u in phase_space(s):
        Hu = Hop(u, s)
        ok8 &= eq(dagger_c(Hu), Hu)                       # Hermitian
        ok8 &= eq(mat_mul(Hu, Hu), ident)                 # an involution
        if dot(u[s:], u[:s]):
            nontrivial += 1
            # and W itself is NOT Hermitian there, so the phase is doing work
            ok8 &= not eq(dagger_c(W(u, s)), W(u, s))
        for v in phase_space(s):
            if omega(u, v, s) == 0:
                ok8 &= eq(mat_mul(Hu, Hop(v, s)), mat_mul(Hop(v, s), Hu))
check("W8", ok8,
      f"THE SELF-ADJOINT NORMALIZATION. H(u) = i^{{b.a}} W(u) is Hermitian and squares to the "
      f"identity at every one of the 4 + 16 phase-space points, and any two with omega = 0 commute "
      f"-- so an isotropic subspace supplies a commuting family of self-adjoint involutions, which "
      f"is the input a joint-eigenspace decomposition wants. At the {nontrivial} points where "
      f"b.a = 1 the bare W is NOT Hermitian, so the phase is load-bearing rather than cosmetic. "
      f"W keeps its real-sign convention; H is a separate interface, which is why the twirl above "
      f"is unaffected")

# ---------------------------------------------------------------- W9  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'WeylTwirl.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
NAMES = ('W_mul', 'W_conjTranspose', 'W_conj', 'W_commute_iff', 'isotropic_iff_commute',
         'char_sum', 'twirl_W', 'H_conjTranspose', 'H_mul_self', 'H_commute',
         'sum_chi_dotF', 'trace_W', 'card_mul_card_perp', 'perp_perp', 'card_le_of_isotropic',
         'perp_eq_self_of_card', 'H_mul', 'H_not_multiplicative', 'twirl_add', 'twirl_smul')
ok9 = 'import OIBridge.WeylTwirl' in root
ok9 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok9 &= re.search(r'(?m)^axiom ', body) is None
ok9 &= all(f'theorem {n}' in src for n in NAMES)
ok9 &= all(f'#print axioms {n}' in src for n in NAMES)
ok9 &= 'native_decide' not in body
# G MUST BE A SUBMODULE, not a Pauli subgroup, and the twirl identity must be the pointwise one
ok9 &= 'G : Submodule (ZMod 2) (PS s)' in src
tw = src[src.index('theorem twirl_W'):]
ok9 &= 'twirl G (W v) = if v ∈ perp G then W v else 0' in tw[:tw.index(':= by')]
# NO WITT, NO CLIFFORD -- the route the file claims to avoid must actually be absent
for banned in ('Witt', 'Clifford', 'witt', 'clifford'):
    ok9 &= banned not in body
ok9 &= 'NO WITT, NO CLIFFORD' in src            # and the claim is made in the header
# isotropy must be stated on the form, with the commutation bridge proved rather than assumed
ok9 &= 'def Isotropic : Prop := ∀ u ∈ G, ∀ v ∈ G, omega u v = 0' in src
ic = src[src.index('theorem isotropic_iff_commute'):]
ok9 &= 'W u * W v = W v * W u' in ic[:ic.index(':=')]
check("W9", ok9,
      f"LINT. The file is imported by OIBridge.lean so CI builds it; no `sorry`, no `axiom`, no "
      f"`native_decide`; all {len(NAMES)} named results print their axiom dependencies. G is a "
      f"`Submodule (ZMod 2) (PS s)` — an isotropic subspace, not a phase-sensitive Pauli subgroup — "
      f"with `Isotropic` stated on the symplectic form and `isotropic_iff_commute` proving that is "
      f"the manuscript's 'abelian' rather than assuming it. The twirl identity is the pointwise "
      f"`twirl G (W v) = if v ∈ perp G then W v else 0`. And the route the header claims to avoid "
      f"is actually absent: neither Witt's extension theorem nor the Clifford group appears "
      f"anywhere in the proofs")

print()
print('     [scope] Settled in Lean: the phase space, the Weyl operators, the product and')
print('     conjugation rules, commutation as the symplectic form, and the exact twirl identity')
print('     Phi_G(W v) = [v in G-perp] W v, for every isotropic subspace and with no Witt')
print('     extension and no Clifford group. NOT settled: everything about entanglement. The')
print('     separability layer, the t = s direction through joint eigenspaces, and the t < s')
print('     negative-partial-transpose witness are the remaining layers of [Main] Theorem')
print('     (separability threshold), which stays at GAP until they land.')
print()
print("weyl_twirl_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
