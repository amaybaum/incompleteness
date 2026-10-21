"""M1 witnesses giving P(a1=R) = 3/4 in the base theory (within the bound), with an explicit preparation protocol,
its herald probability, the decomposition of the A-marginal into preparable A-states, and the three readings."""
from fractions import Fraction as F
from collections import defaultdict
from cardtheory import *
for deck in [(3,1),(3,2),(3,3),(4,1),(4,2),(5,1)]:
    A, B = ["a1","a2"], ["b1","b2"]
    m = Model([deck], {"a": A, "b": B})
    nodes, depth, bp, st = closure(m)
    print(f"== deck {deck[0]}R{deck[1]}B, A={A}, B={B}: closure {st} ==")
    res, ext, PAB, PA, margA = analyse(m, A, B, nodes, depth, bp, verbose=True)
    # explicit protocol: reveal the top n-4 deck cards, herald on the record being all-but-(3R1B) consistent, deal a1 a2 b1 b2
    n = sum(deck); need_r = deck[0] - 3; need_b = deck[1] - 1
    d = m.initial(); keep = defaultdict(F)
    for s, p in d.items():
        rec = []; cur = s
        for _ in range(n - 4):
            o, cur = m.apply(("peekdeck", 0), cur); rec.append(o)
        if rec.count(0) != need_r or rec.count(1) != need_b: continue
        for sl in A + B: _, cur = m.apply(("deal", sl, 0), cur)
        keep[tuple(cur[0])] += p
    tot = sum(keep.values()); psi = {k: v / tot for k, v in keep.items()}
    print(f"  protocol: reveal the top {n-4} deck cards; herald on {need_r} R + {need_b} B revealed (Pr = {tot}); deal a1,a2,b1,b2")
    print(f"  prepared psi = {fmt(psi)}; extreme in conv(Prep(AB)): {is_extreme(psi, [v[0] for v in PAB.values()], all_arrangements(m, A+B))}; "
          f"P(a1=R) = {sum(v for k,v in psi.items() if k[0]==0)}")
