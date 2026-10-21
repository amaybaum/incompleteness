"""Task 1: independent exact re-derivation of card-table facts (engine at 17115cc) and book Sec. 1.11 table.
Exact arithmetic only (fractions.Fraction). No import of the card-table code."""
from fractions import Fraction as F
from itertools import product, permutations
from collections import Counter

def P(cases):  # list of (weight, bool)
    tot = sum(w for w, _ in cases); return sum(w for w, b in cases if b) / tot

swap = lambda s: (s[1], s[0])
print("== swap core: state (v,h), v visible, h hidden; v0,h0 independent fair bits (engine dealHand) ==")
one = [(F(1,4), swap((v,h))[0]==v) for v,h in product((0,1),repeat=2)]
two = [(F(1,4), swap(swap((v,h)))[0]==v) for v,h in product((0,1),repeat=2)]
# engine peek: after swap1 look at v, replace h by a fresh fair bit, swap2
pk = [(F(1,8), swap((swap((v,h))[0], f))[0]==v) for v,h,f in product((0,1),repeat=3)]
# chained divisible prediction: one-step match matrix applied twice
T1 = {(a,b): sum(F(1,2) for h in (0,1) if swap((a,h))[0]==b) for a in (0,1) for b in (0,1)}  # P(v1=b|v0=a)
chain = sum(F(1,2)*T1[(a,m)]*T1[(m,a)] for a in (0,1) for m in (0,1))
print("one shuffle:", P(one), "| two shuffles:", P(two), "| chained through middle:", chain, "| peek(engine):", P(pk))
print("engine 'peek' enumeration size:", len(pk), "(book says 'sixteen cases in the longest protocol')")

print("\n== intervention table between swap1 and swap2 (return prob: final v == dealt v0) ==")
def run(interv):
    cases = []
    for v0, h0, f in product((0,1), repeat=3):
        v, h = swap((v0, h0)); rec = None
        if interv == "none": pass
        elif interv == "look_visible": rec = v
        elif interv == "copy_visible_to_record": rec = (v, v)
        elif interv == "burn_replace_visible": rec = v; v = f          # the revealed card is the one burned
        elif interv == "replace_hidden_memory": h = f                   # memory card replaced, nothing seen
        elif interv == "engine_peek": rec = v; h = f                    # engine dealHand: seen=v, h fresh
        v, h = swap((v, h)); cases.append((F(1,8), v == v0))
    return P(cases)
for iv in ["none","look_visible","copy_visible_to_record","burn_replace_visible","replace_hidden_memory","engine_peek"]:
    print(f"  {iv:26s} {run(iv)}")

print("\n== swap core dealt from a finite two-colour deck with depletion (book: 'dealt'; engine: fair independent bits) ==")
for N in (2, 4, 6, 24):
    deck = [0]*(N//2) + [1]*(N//2)        # distinct physical cards, colours 0/1; counting measure on orderings
    one_c, peek_c = [], []
    idx = range(N)
    for i in idx:                          # ordered draws of the first three distinct cards (uniform)
        for j in idx:
            if j == i: continue
            v0, h0 = deck[i], deck[j]
            v, h = swap((v0, h0)); one_c.append((F(1), v == v0))
            for k in idx:
                if k in (i, j): continue
                v2, h2 = swap((v, deck[k])); peek_c.append((F(1), v2 == v0))
    print(f"  N={N:2d}: one-shuffle match {P(one_c)} (formula (N/2-1)/(N-1) = {F(N//2-1, N-1)}); "
          f"engine-peek with replacement from remaining deck: match {P(peek_c) if peek_c else 'n/a (deck empty)'}; two-shuffle match 1")

print("\n== line game (Euchre 24 cards, m = +-1..6, red negative), exact ==")
M = []
for v in range(1,7):
    for si in range(4):
        red = si in (1,2); M.append(-v if red else v)
blind = Counter(); peek = Counter()
for i in range(24):
    for j in range(24):
        if j == i: continue
        blind[2*M[i]+2*M[j]] += 1
        for k in range(24):
            if k in (i,j): continue
            for l in range(24):
                if l in (i,j,k): continue
                peek[M[i]+M[j]+M[k]+M[l]] += 1
tb, tp = sum(blind.values()), sum(peek.values())
print("  blind deals:", tb, "| all displacements even:", all(d % 2 == 0 for d in blind), "| odd mass:", F(sum(c for d,c in blind.items() if d%2), tb))
print("  peeked deals:", tp, "| odd-position total probability:", F(sum(c for d,c in peek.items() if d%2), tp))
print("  blind distinct nonzero heights:", len(set(blind.values())))
print("  peek: unreachable positions in [-24,24]:", [x for x in range(-24,25) if peek[x]==0])
print("  blind: unreachable positions:", [x for x in range(-24,25) if blind[x]==0][:4], "... count", sum(1 for x in range(-24,25) if blind[x]==0))
exp_blind = [2,0,8,0,10,0,16,0,18,0,24,0,18,0,24,0,26,0,32,0,34,0,40,0,48,0,40,0,34,0,32,0,26,0,24,0,18,0,24,0,18,0,16,0,10,0,8,0,2]
print("  blind matches engine.test.js EXPECTED_BLIND:", [blind[x] for x in range(-24,25)] == exp_blind)
print("  P(+24 blind) =", F(blind[24], tb), "; P(+-24 peek) =", F(peek[24]+peek[-24], tp))
print("\n== cat protocol: catOdds(p) = (1-p)*1 + p*(1/2), exact at the five dial stops ==")
print("  ", [(str(p), str((1-p)*1 + p*F(1,2))) for p in (F(0),F(1,4),F(1,2),F(3,4),F(1))])

exp_peek = [0,0,24,96,216,384,720,960,1392,1728,2376,2880,3792,4800,5928,7008,8136,9120,9888,10656,11616,12288,13080,13440,13968,13440,13080,12288,11616,10656,9888,9120,8136,7008,5928,4800,3792,2880,2376,1728,1392,960,720,384,216,96,24,0,0]
print("\n  peek distribution matches engine.test.js EXPECTED_PEEK (independent Python enumeration):", [peek[x] for x in range(-24,25)] == exp_peek)
print("  blind zero positions filled by peek:", sum(1 for x in range(-24,25) if blind[x]==0 and peek[x]>0), "of", sum(1 for x in range(-24,25) if blind[x]==0))
