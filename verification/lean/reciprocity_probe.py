#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/Reciprocity.lean.

[SM] Theorem 19 (reciprocity of visible transition counts):

    N_ij = N_{theta j, theta i}   for all visible i, j and at every time scale n,

for a T-invariant substratum bijection phi on V x H (phi^-1 = T phi T) whose time reversal
preserves the partition (T = theta x theta_H) and with the counting-measure hidden prior.

Everything is exact integer counting over explicit finite bijections; no probability, no
tolerance. The small-size sweeps are EXHAUSTIVE: every permutation of the substratum, every
product-form involution T.

TWO SIDE CONDITIONS ARE THE POINT, and each gets a countercontrol.

First, [GR 3.2]'s: detailed balance N_ij = N_ji is the theta = id reading and FAILS off it. R2
exhibits the failure on a deliberately simple T-invariant substratum whose visible dynamics is a
deterministic 3-cycle: with theta a transposition, N_02 = |H| against N_20 = 0.

Second, one the manuscript leaves implicit: the printed proof passes from phi^-1 = T phi T to
phi = T phi^-1 T and later cancels T T, and both steps need T to be an INVOLUTION, which "the
induced action of T" supplies physically but no clause of the printed statement states. R4 shows
it is not removable: on Z_4 with theta a rotation by one and phi the same rotation, the equation
phi^-1 = T phi T holds and the conclusion is false. The Lean statement carries hthetaV/hthetaH
explicitly.

  R1  EXHAUSTIVE: over every permutation of V x H at |V| = 3, |H| = 2 and |V| = 2, |H| = 3, and
      every product-form involution T, the T-invariant ones satisfy N_ij(n) = N_{theta j, theta i}(n)
      for n = 1..6 -- and every T-invariant one with theta = id satisfies detailed balance.
  R2  COUNTERCONTROL for the T-even side condition: a T-invariant substratum, theta a
      transposition, where detailed balance fails while the (theta j, theta i) form holds.
  R3  COUNTERCONTROL for T-invariance: a drift substratum where phi^-1 != T phi T and the
      conclusion fails.
  R4  COUNTERCONTROL for involutivity: a non-involutive T with phi^-1 = T phi T where the
      conclusion fails -- the hypothesis the manuscript leaves implicit is load-bearing.
  R5  the wave-equation substratum of [SM]: (a, b) -> (Sa - b, a) on (Z_q^L)^2, T = register swap,
      checkerboard partition; the theta-form holds exactly for n = 1..8 at L = 4, q = 2, 3 -- and
      theta is a genuine swap on the visible data, so this instance lives OFF theta = id.
  R6  lint.

Usage:  python3 reciprocity_probe.py
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


# ---------------------------------------------------------------- machinery
def counts(states, phi_map, nV, n):
    """N_ij(n) as a dict: iterate the bijection n times."""
    N = {}
    for s in states:
        t = s
        for _ in range(n):
            t = phi_map[t]
        key = (s[0], t[0])
        N[key] = N.get(key, 0) + 1
    return N


def reciprocity_holds(states, phi_map, theta, nV, nH, nmax):
    for n in range(1, nmax + 1):
        N = counts(states, phi_map, nV, n)
        for i in range(nV):
            for j in range(nV):
                if N.get((i, j), 0) != N.get((theta[j], theta[i]), 0):
                    return False
    return True


def involutions(n):
    """All involutions of {0..n-1} as tuples."""
    out = []
    for p in itertools.permutations(range(n)):
        if all(p[p[k]] == k for k in range(n)):
            out.append(p)
    return out


# ---------------------------------------------------------------- R1  exhaustive
ok1 = True
tested = 0
db_all = True
for nV, nH in ((3, 2), (2, 3)):
    states = [(i, h) for i in range(nV) for h in range(nH)]
    idx = {s: k for k, s in enumerate(states)}
    for theta in involutions(nV):
        for thetaH in involutions(nH):
            def Tmap(s):
                return (theta[s[0]], thetaH[s[1]])
            for perm in itertools.permutations(range(len(states))):
                phi = {states[k]: states[perm[k]] for k in range(len(states))}
                inv = {v: k for k, v in phi.items()}
                # T-invariance: phi^-1 = T o phi o T
                if any(inv[s] != Tmap(phi[Tmap(s)]) for s in states):
                    continue
                tested += 1
                ok1 &= reciprocity_holds(states, phi, theta, nV, nH, 6)
                if all(theta[k] == k for k in range(nV)):
                    N = counts(states, phi, nV, 1)
                    db_all &= all(N.get((i, j), 0) == N.get((j, i), 0)
                                  for i in range(nV) for j in range(nV))
ok1 &= db_all and tested > 0
check("R1", ok1,
      f"EXHAUSTIVE. Over every permutation of the substratum at |V| = 3, |H| = 2 and |V| = 2, "
      f"|H| = 3 and every product-form involution T -- {tested} T-invariant bijections in all -- "
      f"N_ij(n) = N_(theta j, theta i)(n) holds exactly for n = 1..6, and every T-invariant "
      f"bijection with theta = id satisfies detailed balance N_ij = N_ji. Lean's `theorem_19` and "
      f"`detailed_balance`")

# ---------------------------------------------------------------- R2  the T-even side condition
# V = Z_3, theta = (0 1), theta_H = id, and phi = c x id with c the 3-cycle 0 -> 2 -> 1 -> 0.
# theta c theta = c^-1, so phi is T-invariant; the visible dynamics is deterministic, so
# N_02 = |H| while N_20 = 0.
ok2 = True
for nH in (1, 2, 3):
    states = [(i, h) for i in range(3) for h in range(nH)]
    c = {0: 2, 2: 1, 1: 0}
    theta = (1, 0, 2)
    phi = {(i, h): (c[i], h) for i, h in states}
    inv = {v: k for k, v in phi.items()}
    def Tmap(s):
        return (theta[s[0]], s[1])
    ok2 &= all(inv[s] == Tmap(phi[Tmap(s)]) for s in states)          # T-invariant
    N = counts(states, phi, 3, 1)
    ok2 &= N.get((0, 2), 0) == nH and N.get((2, 0), 0) == 0           # detailed balance FAILS
    ok2 &= reciprocity_holds(states, phi, theta, 3, nH, 6)            # the theta-form holds
check("R2", ok2,
      "COUNTERCONTROL for the T-even side condition, [GR 3.2]'s precision note. On the T-invariant "
      "substratum phi = (3-cycle) x id with theta the transposition (0 1): N_02 = |H| against "
      "N_20 = 0, so the symmetric form N_ij = N_ji is FALSE -- the visible states carry T-odd "
      "data -- while N_ij = N_(theta j, theta i) holds exactly at every n. Detailed balance is the "
      "theta = id reading and only that")

# ---------------------------------------------------------------- R3  T-invariance load-bearing
states = [(i, h) for i in range(3) for h in range(2)]
phi = {(i, h): ((i + 1) % 3, h) for i, h in states}                   # a drift
inv = {v: k for k, v in phi.items()}
ok3 = any(inv[s] != phi[s] for s in states)                           # NOT T-invariant (theta = id)
N = counts(states, phi, 3, 1)
ok3 &= N.get((0, 1), 0) == 2 and N.get((1, 0), 0) == 0                # and the conclusion fails
check("R3", ok3,
      "COUNTERCONTROL for the T-invariance hypothesis. The drift i -> i + 1 with theta = id is not "
      "T-invariant, and reciprocity fails outright: N_01 = |H|, N_10 = 0. The hypothesis "
      "phi^-1 = T phi T is doing the work")

# ---------------------------------------------------------------- R4  involutivity load-bearing
# V = Z_4, |H| = 1, theta = rotation by one (NOT an involution), phi = the same rotation.
# phi^-1 = T phi T holds: both sides are rotation by three. The conclusion fails.
states = [(i, 0) for i in range(4)]
theta = tuple((v + 1) % 4 for v in range(4))
phi = {(i, 0): ((i + 1) % 4, 0) for i in range(4)}
inv = {v: k for k, v in phi.items()}
def Tmap4(s):
    return (theta[s[0]], 0)
ok4 = any(theta[theta[v]] != v for v in range(4))                     # T is NOT an involution
ok4 &= all(inv[s] == Tmap4(phi[Tmap4(s)]) for s in states)            # yet phi^-1 = T phi T holds
N = counts(states, phi, 4, 1)
ok4 &= N.get((0, 1), 0) == 1
ok4 &= N.get((theta[1], theta[0]), 0) == 0                            # N_(theta 1, theta 0) = N_21
ok4 &= N.get((0, 1), 0) != N.get((theta[1], theta[0]), 0)             # conclusion FAILS
check("R4", ok4,
      "COUNTERCONTROL for involutivity -- the hypothesis the printed statement leaves implicit in "
      "'the induced action of T'. On Z_4 with theta a rotation by one and phi the same rotation, "
      "phi^-1 = T phi T holds exactly, T is not an involution, and the conclusion is false: "
      "N_01 = 1 against N_(theta 1, theta 0) = N_21 = 0. The Lean statement carries "
      "hthetaV/hthetaH explicitly, and this is why they cannot be dropped")

# ---------------------------------------------------------------- R5  the wave-equation substratum
# (a, b) -> (Sa - b, a) on (Z_q^L)^2 with (Sa)_n = a_(n-1) + a_(n+1), periodic. T swaps the two
# registers; U^-1 = T U T is checked exactly. The checkerboard partition takes the EVEN sites of
# both registers as visible; T then swaps the two visible halves, so theta is a genuine
# transposition on the visible data -- this instance lives off theta = id.
ok5 = True
for q in (2, 3):
    L = 4
    even = (0, 2)
    odd = (1, 3)
    vecs = list(itertools.product(range(q), repeat=L))
    def S(a):
        return tuple((a[(n - 1) % L] + a[(n + 1) % L]) % q for n in range(L))
    def U(s):
        a, b = s[:L], s[L:]
        return tuple((x - y) % q for x, y in zip(S(a), b)) + a
    def Uinv(s):
        ap, a = s[:L], s[L:]
        return a + tuple((x - y) % q for x, y in zip(S(a), ap))
    def Tswap(s):
        return s[L:] + s[:L]
    allstates = [a + b for a in vecs for b in vecs]
    ok5 &= all(Uinv(s) == Tswap(U(Tswap(s))) for s in allstates)      # U^-1 = T U T, exactly
    def vis(s):
        return tuple(s[n] for n in even) + tuple(s[L + n] for n in even)
    # theta on visible data: swap the a-half and the b-half
    def theta_vis(v):
        return v[2:] + v[:2]
    # T preserves the partition: vis(T s) = theta(vis s), exactly
    ok5 &= all(vis(Tswap(s)) == theta_vis(vis(s)) for s in allstates)
    ok5 &= any(theta_vis(v) != v for v in set(vis(s) for s in allstates))   # theta != id
    for n in range(1, 9):
        N = {}
        for s in allstates:
            t = s
            for _ in range(n):
                t = U(t)
            key = (vis(s), vis(t))
            N[key] = N.get(key, 0) + 1
        ok5 &= all(N[k] == N.get((theta_vis(k[1]), theta_vis(k[0])), 0) for k in N)
check("R5", ok5,
      "THE WAVE-EQUATION SUBSTRATUM of [SM]: (a, b) -> (Sa - b, a) on (Z_q^L)^2, with U^-1 = T U T "
      "checked exactly, the checkerboard partition (even sites of both registers visible) checked "
      "to be preserved by T, and N_ij(n) = N_(theta j, theta i)(n) holding exactly for n = 1..8 at "
      "L = 4, q = 2, 3. Note theta is a genuine swap of the two visible registers -- velocity-like "
      "data -- so this physical instance lives off theta = id and needs the general form")

# ---------------------------------------------------------------- R6  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'Reciprocity.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = src[src.index('namespace OIBridge'):]

NAMES = ('Tm_involutive', 'key', 'count_reciprocity', 'hT_pow', 'theorem_19', 'detailed_balance')
ok6 = 'import OIBridge.Reciprocity' in root
ok6 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok6 &= re.search(r'(?m)^axiom ', body) is None
ok6 &= all(f'theorem {n}' in src for n in NAMES)
ok6 &= all(f'#print axioms {n}' in src for n in NAMES)
ok6 &= 'native_decide' not in body
# the visible sector must NOT be assumed finite -- only the hidden sector is counted over
ok6 &= 'Fintype V' not in src and '[Fintype H]' in src
# involutivity must be explicit in the wrapper's hypotheses
tw = src[src.index('theorem theorem_19'):]
tsig = tw[:tw.index(':= by')]
ok6 &= 'hθV : ∀ v, θ (θ v) = v' in tsig and 'hθH : ∀ h, θH (θH h) = h' in tsig
# both printed clauses: the count form at every n, and the probability form divided by |H|
ok6 &= 'N (φ ^ n) i j = N (φ ^ n) (θ j) (θ i)' in tsig
ok6 &= '/ (Fintype.card H : ℚ)' in tsig
# detailed balance must be the theta = id specialization, not a separate assumption set
db = src[src.index('theorem detailed_balance'):]
ok6 &= 'Tm id θH' in db[:db.index(':=\n') if ':=\n' in db else len(db)]
ok6 &= 'N (φ ^ n) i j = N (φ ^ n) j i' in db
check("R6", ok6,
      f"LINT. The file is imported by OIBridge.lean so CI builds it; no `sorry`, no `axiom`, no "
      f"`native_decide`; all {len(NAMES)} named results print their axiom dependencies. The "
      f"visible sector is not assumed finite; involutivity of both components of T is an explicit "
      f"hypothesis of `theorem_19`; the wrapper carries both printed clauses -- counts at every "
      f"time scale and the probability form divided by |H| -- and `detailed_balance` is the "
      f"theta = id specialization of the same theorem, not a statement with its own hypotheses")

print()
print('     [scope] Settled in Lean: [SM] Theorem 19 in full -- reciprocity of the visible')
print('     transition counts at every time scale, the probability form, and the detailed-balance')
print('     reading at theta = id -- with the involutivity of the induced T-action explicit and')
print('     countercontrolled. NOT settled: Proposition 20 (reciprocity does not imply a')
print('     T-invariant Hamiltonian) and Theorem 21, which consume this theorem and remain GAP.')
print()
print("reciprocity_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
