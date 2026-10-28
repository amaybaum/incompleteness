#!/usr/bin/env python3
"""SC-39: exact check of the restricted card-game Bell sentence and of why each condition is needed.

A two-player card table: a deal Omega (a tuple of hidden cards, red = +1 / black = -1), settings a, b in
{0, 1}, and each player's outcome in {+1, -1}. CHSH = E00 + E01 + E10 - E11, in exact Fractions.

  K1  Under the book's conditions -- deterministic shuffles and moves; once the deal is down every
      shuffle, move and setting choice acts on one player's own cards only; each outcome read from that
      player's own cards, +-1 in every run; settings independent of the deal -- every outcome is
      q_a(own cards), r_b(own cards). Over every pair of deterministic local response tables (4 x 4 = 16
      pairs) and hence every deal distribution, |CHSH| <= 2 (exact, vertex enumeration; the set of such
      models is the convex hull of these).
  K2  An explicit deal with shared hidden cards (the coin-and-burn style correlation written at the deal)
      reaches CHSH = 2 exactly: the ceiling is attained, not just respected.
  Countercontrols (each drops one condition and must exceed 2):
  X1  a shared move after the settings acting on both hands (setting-dependent global dynamics,
      Main §3.3's PR-box remark): CHSH = 4.
  X1' the players' moves stay on their own cards, but the game-rule shuffle between streets, after the
      settings, is a deterministic whole-deck permutation that carries A's setting card into B's hand:
      CHSH = 4. So the shuffle, not only the players' moves, must stay on one player's cards.
  X2  a deal chosen with knowledge of the settings (measurement dependence): CHSH = 4.
  X3  runs without a +-1 outcome discarded (no outcome in every run): CHSH = 4 on the kept runs.
  ADM An admissibility checker for the book's condition "once the deal is down every operation, including
      each shuffle the rules prescribe, each move and each setting choice, acts on one player's own cards
      only": a deterministic map on the whole deck is admitted iff, for one player's region R, it leaves
      every card outside R unchanged and sets the cards in R as a function of the cards in R alone. X1''s
      whole-deck shuffle is rejected by it.
  E   Exhaustive check on a four-card deck (A: hand, setting card; B: hand, setting card; cards 0/1):
      every deal (16), the setting writes, then EVERY sequence of length <= 2 of admitted operations drawn
      from all 256 + 256 own-region maps and all 24 whole-deck position permutations (the checker admits 3),
      interleaved in any order, then every +-1 readout of each player's own region (16 each). E1' shows
      these reach all 65,536 product maps, a set closed under composition, so every longer sequence is
      covered too.
      E1 (the reduction, checked): after every such sequence, A's final region is a function of A's dealt
         hand and a alone, and B's of B's dealt hand and b alone, so every admitted strategy induces a
         response-table pair q_a(own hand), r_b(own hand), which is the K1 class.
      E2 every induced pair and every deal gives |CHSH term| <= 2, so every deal law gives |CHSH| <= 2
         (CHSH is linear in the deal law).
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
check("K1 every pair of local deterministic response tables has |CHSH| <= 2 (4 x 4 = 16 pairs, exact)",
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

# X1': a five-card deck. Positions 0-1 are A's region (hand, setting card); positions 2-4 are B's region
# (hand, setting card, spare). The deal puts a copy of the shared card c1 in each hand and a blank (0) in
# B's spare. Each player writes the setting onto its own setting card (own-card move). The game-rule
# shuffle between streets is a fixed deterministic permutation of the whole deck that swaps positions 1
# and 4, carrying A's setting card into B's region. B reads its outcome from its own region by a fixed
# rule: flip the hand card iff its own setting card and its spare are both 1. Every player action is
# own-card; only the shuffle crosses the hands.
A_REGION, B_REGION = (0, 1), (2, 3, 4)
SHUFFLE = [0, 4, 2, 3, 1]                  # new position of the card at each old position; a bijection
assert sorted(SHUFFLE) == list(range(5))
def shuffle_play(omega, a, b):
    c1, _ = omega
    deck = [c1, 0, c1, 0, 0]               # the deal
    deck[1] = a                            # A's own-card setting move
    deck[3] = b                            # B's own-card setting move
    new = [None] * 5
    for old, pos in enumerate(SHUFFLE):
        new[pos] = deck[old]
    hand_A = [new[i] for i in A_REGION]
    hand_B = [new[i] for i in B_REGION]
    q = hand_A[0]
    r = -hand_B[0] if (hand_B[1] == 1 and hand_B[2] == 1) else hand_B[0]
    return q, r
E = {(a, b): sum(p * shuffle_play(o, a, b)[0] * shuffle_play(o, a, b)[1] for o, p in deal.items()) for a in S for b in S}
check("X1' CONTROL (must exceed 2): own-card moves but a whole-deck shuffle after the settings gives CHSH = 4",
      chsh(E) == 4)


def admissible(deck_map, n, regions):
    """deck_map: function on tuples of length n with entries in a finite card set (enumerated over VALUES).
    Admitted iff for some region R it changes nothing outside R and sets R from R alone."""
    decks = list(product(VALUES, repeat=n))
    for R in regions:
        out = [i for i in range(n) if i not in R]
        ok, seen = True, {}
        for d in decks:
            e = deck_map(d)
            if any(e[i] != d[i] for i in out):
                ok = False
                break
            key = tuple(d[i] for i in R)
            val = tuple(e[i] for i in R)
            if seen.setdefault(key, val) != val:
                ok = False
                break
        if ok:
            return True
    return False


VALUES = (-1, 0, 1)
def perm_map(perm):
    def f(d):
        e = [None] * len(d)
        for old, pos in enumerate(perm):
            e[pos] = d[old]
        return tuple(e)
    return f
check("ADM1 the X1' whole-deck shuffle (positions 1 <-> 4) is rejected by the own-cards condition",
      not admissible(perm_map(SHUFFLE), 5, (A_REGION, B_REGION)))
check("ADM2 CONTROL (must admit): a shuffle within B's region (positions 3 <-> 4) is admitted",
      admissible(perm_map([0, 1, 2, 4, 3]), 5, (A_REGION, B_REGION)))

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

# E: exhaustive own-region operation sequences on a four-card deck, bits 0/1.
# Positions: 0 A hand, 1 A setting card, 2 B hand, 3 B setting card. Deck state = 4-bit tuple.
RA, RB = (0, 1), (2, 3)
VALUES = (0, 1)
STATES = list(product((0, 1), repeat=4))
IDX = {st: i for i, st in enumerate(STATES)}
def as_table(f):
    return tuple(IDX[f(st)] for st in STATES)
ops = set()
for R in (RA, RB):
    regs = list(product((0, 1), repeat=2))
    for images in product(regs, repeat=4):               # all 4^4 = 256 maps of a two-card region
        g = dict(zip(regs, images))
        def f(st, R=R, g=g):
            e = list(st)
            e[R[0]], e[R[1]] = g[(st[R[0]], st[R[1]])]
            return tuple(e)
        assert admissible(f, 4, (RA, RB))
        ops.add(as_table(f))
from itertools import permutations
n_perm_adm = 0
for perm in permutations(range(4)):                      # every whole-deck position permutation
    if admissible(perm_map(perm), 4, (RA, RB)):
        n_perm_adm += 1
        ops.add(as_table(perm_map(perm)))
check("E0 the checker admits exactly 3 of the 24 whole-deck permutations (identity, swap within A, within B)",
      n_perm_adm == 3)
ops = sorted(ops)
ident = tuple(range(16))
seqs = {ident}
for o in ops:
    seqs.add(o)
for o1 in ops:
    for o2 in ops:
        seqs.add(tuple(o2[o1[i]] for i in range(16)))   # o1 then o2, any interleaving of the two players
a_maps, b_maps, red_ok = set(), set(), True
for M in seqs:
    fa, fb = {}, {}
    for st in STATES:
        for a in S:
            for b in S:
                w = list(st)
                w[1], w[3] = a, b                       # the setting writes, each on its own card
                fin = STATES[M[IDX[tuple(w)]]]
                ka, va = (st[0], a), (fin[0], fin[1])
                kb, vb = (st[2], b), (fin[2], fin[3])
                if fa.setdefault(ka, va) != va or fb.setdefault(kb, vb) != vb:
                    red_ok = False
    a_maps.add(tuple(sorted(fa.items())))
    b_maps.add(tuple(sorted(fb.items())))
check(f"E1 reduction: after all {len(seqs)} distinct admitted sequence maps each player's final cards depend only on its own hand and setting",
      red_ok)
check("E1' closure: the length-<=2 sequences already reach all 256 x 256 product maps f_A x f_B, a set closed under "
      "composition that contains every admitted operation, so longer sequences add no strategy",
      len(seqs) == 256 * 256)
regs = list(product((0, 1), repeat=2))
readouts = list(product((1, -1), repeat=4))
def tables(maps):
    out = set()
    for m in maps:
        m = dict(m)
        for ro in readouts:
            g = dict(zip(regs, ro))
            out.add(tuple(g[m[(h, x)]] for h in (0, 1) for x in S))   # q[(h, setting)]
    return out
TA, TB = tables(a_maps), tables(b_maps)
worst = 0
for qa in TA:
    for rb in TB:
        for hA in (0, 1):
            for hB in (0, 1):
                q = {x: qa[2 * hA + x] for x in S}
                r = {y: rb[2 * hB + y] for y in S}
                worst = max(worst, abs(q[0] * r[0] + q[0] * r[1] + q[1] * r[0] - q[1] * r[1]))
check(f"E2 every admitted strategy pair ({len(TA)} x {len(TB)} induced tables) and every deal: |CHSH| <= 2",
      worst == 2, f"max |CHSH term| = {worst}")

print("\ncard_bell_check:", "ALL CHECKS PASS" if not FAIL else f"{len(FAIL)} FAILURE(S): {FAIL}")
sys.exit(1 if FAIL else 0)
