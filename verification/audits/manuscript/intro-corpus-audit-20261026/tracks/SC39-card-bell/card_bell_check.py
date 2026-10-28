#!/usr/bin/env python3
"""SC-39: exact check of the restricted card-game Bell sentence and of why each condition is needed.

A two-player card table: a deal Omega (a tuple of hidden cards, red = +1 / black = -1), settings a, b in
{0, 1}, and each player's outcome in {+1, -1}. CHSH = E00 + E01 + E10 - E11, in exact Fractions.

  K1  Under the book's conditions -- deterministic moves; after the deal each player's moves and setting
      choice act only on that player's own cards; each outcome read from that player's own cards, +-1 in
      every run; settings independent of the deal -- every outcome is q_a(own cards), r_b(own cards).
      Over every deterministic local response pair (16 tables) and hence every deal distribution,
      |CHSH| <= 2 (exact, vertex enumeration; the set of such models is the convex hull of these).
  K2  An explicit deal with shared hidden cards (the coin-and-burn style correlation written at the deal)
      reaches CHSH = 2 exactly: the ceiling is attained, not just respected.
  Countercontrols (each drops one condition and must exceed 2):
  X1  a shared move after the settings acting on both hands (setting-dependent global dynamics,
      Main §3.3's PR-box remark): CHSH = 4.
  X2  a deal chosen with knowledge of the settings (measurement dependence): CHSH = 4.
  X3  runs without a +-1 outcome discarded (no outcome in every run): CHSH = 4 on the kept runs.
Usage: python3 -I card_bell_check.py
"""
import sys
from fractions import Fraction as F
from itertools import product

FAIL = []
def check(name, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + name + ((" : " + msg) if msg else ""))
    if not ok:
        FAIL.append(name)

S = (0, 1)
def chsh(E):
    return E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]

# K1: local deterministic responses q_a(Omega_A), r_b(Omega_B); every deal fixes one such pair of tables.
tables = list(product((1, -1), repeat=2))           # (q_0, q_1)
vals = []
for q in tables:
    for r in tables:
        vals.append(chsh({(a, b): F(q[a] * r[b]) for a in S for b in S}))
check("K1 every local deterministic response pair has |CHSH| <= 2 (16 x 16 tables, exact)",
      max(abs(v) for v in vals) == 2, f"values {sorted(set(vals))}")

# K2: a deal of two shared hidden cards c1, c2 copied into both hands; outcomes read from own copy.
deal = {(c1, c2): F(1, 4) for c1 in (1, -1) for c2 in (1, -1)}
def local_play(omega, a, b):
    c1, c2 = omega
    hand_A, hand_B = (c1, c2), (c1, c2)            # each player holds own copies, written at the deal
    q = hand_A[0]                                  # A's outcome: first card, either setting
    r = hand_B[0]                                  # B likewise
    return q, r
E = {(a, b): sum(p * local_play(o, a, b)[0] * local_play(o, a, b)[1] for o, p in deal.items()) for a in S for b in S}
check("K2 a shared-deal local game attains CHSH = 2", chsh(E) == 2)

# X1: after both settings, one move acts on both hands: B's card is flipped iff a = b = 1.
def global_play(omega, a, b):
    c1, _ = omega
    q = c1
    r = -c1 if (a == 1 and b == 1) else c1          # needs both settings: crosses the wings
    return q, r
E = {(a, b): sum(p * global_play(o, a, b)[0] * global_play(o, a, b)[1] for o, p in deal.items()) for a in S for b in S}
check("X1 CONTROL (must exceed 2): a post-setting move on both hands gives CHSH = 4", chsh(E) == 4)

# X2: the deal is drawn from a law that depends on (a, b); play is local.
def dependent_deal(a, b):
    return {(c, -c if (a == 1 and b == 1) else c): F(1, 2) for c in (1, -1)}
def split_play(omega, a, b):
    return omega[0], omega[1]                       # A reads card 1, B reads card 2: local
E = {(a, b): sum(p * split_play(o, a, b)[0] * split_play(o, a, b)[1] for o, p in dependent_deal(a, b).items())
     for a in S for b in S}
check("X2 CONTROL (must exceed 2): a deal that depends on the settings gives CHSH = 4", chsh(E) == 4)

# X3: local deterministic play, but A reports an outcome only on some runs (a rule on A's own cards and
# setting), and runs without an outcome are discarded: no +-1 outcome in every run.
deal3 = {(c, s): F(1, 4) for c in (1, -1) for s in (1, -1)}
def lossy_local(omega, a, b):
    c, s = omega
    q = c
    r = c if b == 0 else c * s
    kept = (s == 1) if a == 0 else (s == -1)        # depends only on A's own cards and setting
    return q, r, kept
E = {}
for a in S:
    for b in S:
        num = sum(p * lossy_local(o, a, b)[0] * lossy_local(o, a, b)[1] for o, p in deal3.items() if lossy_local(o, a, b)[2])
        den = sum(p for o, p in deal3.items() if lossy_local(o, a, b)[2])
        E[(a, b)] = num / den
check("X3 CONTROL (must exceed 2): local play with runs lacking an outcome discarded gives CHSH = 4 on kept runs",
      chsh(E) == 4)

print("\ncard_bell_check:", "ALL CHECKS PASS" if not FAIL else f"{len(FAIL)} FAILURE(S): {FAIL}")
sys.exit(1 if FAIL else 0)
