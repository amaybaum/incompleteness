"""Task 3/6 extras: (i) two independent decks (SEPDECK); (ii) K-CLASSICAL with the visible slots inside AB;
(iii) larger decks n = 7, 8 for the base theory (beyond the stated bound; robustness only);
(iv) are BASE's extreme AB states products? (shared depletion vs mixtures of preparable products)."""
import time, json, itertools
from fractions import Fraction as F
from cardtheory import *

def line(tag, m, A, B, req=(), kinds=("peek", "swap")):
    t = time.time()
    nodes, depth, bp, st = closure(m, s_max=400000)
    res, ext, PAB, PA, margA = analyse(m, A, B, nodes, depth, bp, require_filled=req, verbose=False)
    wr = lemma_w_rank(m, A + B, set(kinds))
    print(f"  {tag:34s} {st['status']}@{st['depth']:2d} nodes={len(nodes):6d} W={wr[0]}/{wr[1]} |PAB|={res['n_PAB']:4d} "
          f"ext={res['n_extreme']:3d} M1wit(ext)={res['n_M1_witness_extreme']:2d} M1wit(bud)={res['n_M1_witness_budget']:2d} "
          f"P(a1=R)={','.join(res['witness_P(a1=R) values'])} [{time.time()-t:.1f}s]", flush=True)
    return res, ext, PAB, PA, margA, nodes, depth, bp

print("== (i) SEPDECK: two independent decks; any slot may be dealt from either deck ==")
tot = 0; wit = 0
for d1 in [(1, 1), (2, 1), (1, 2), (2, 0), (0, 2), (1, 0), (0, 1)]:
    for d2 in [(1, 1), (2, 1), (1, 2), (2, 0), (0, 2), (1, 0), (0, 1)]:
        if d2 < d1: continue
        n = sum(d1) + sum(d2)
        if n > 6: continue
        for na, nb in [(1, 1), (1, 2), (2, 1), (2, 2)]:
            if n < na + nb: continue
            A = [f"a{i+1}" for i in range(na)]; B = [f"b{i+1}" for i in range(nb)]
            m = Model([d1, d2], {"a": A, "b": B})
            res = line(f"SEPDECK d1={d1} d2={d2} A={na} B={nb}", m, A, B)[0]
            tot += 1; wit += res["n_M1_witness_extreme"] > 0
print(f"  SUMMARY SEPDECK: realizations={tot} with M1 witness={wit}")

print("\n== (ii) K-CLASSICAL with the visible slots counted inside AB (A = {a1, av}, B = {b1, bv}) ==")
for deck in [(2, 2), (3, 1), (3, 2), (2, 3), (3, 3), (4, 2)]:
    m = Model([deck], {"a": ["a1"], "b": ["b1"]}, ("VIS",))
    line(f"VIS deck={deck} A=a1+av B=b1+bv", m, ["a1", "av"], ["b1", "bv"], kinds=("peek", "swap", "read"))

print("\n== (iii) base theory at n = 7, 8 (beyond the stated bound) ==")
for deck in [(4, 3), (5, 2), (6, 1), (4, 4), (5, 3), (6, 2)]:
    for na, nb in [(1, 1), (1, 2), (2, 2)]:
        m = Model([deck], {"a": [f"a{i+1}" for i in range(na)], "b": [f"b{i+1}" for i in range(nb)]})
        line(f"BASE deck={deck} A={na} B={nb}", m, [f"a{i+1}" for i in range(na)], [f"b{i+1}" for i in range(nb)])

print("\n== (iv) BASE: extreme AB states and whether each is a product of its marginals; decks 3R3B and 4R2B, A=2 B=2 ==")
for deck in [(3, 3), (4, 2), (2, 2)]:
    A, B = ["a1", "a2"], ["b1", "b2"]
    m = Model([deck], {"a": A, "b": B})
    nodes, depth, bp, st = closure(m)
    res, ext, PAB, PA, margA = analyse(m, A, B, nodes, depth, bp, verbose=False)
    for e in ext:
        mA, mB = {}, {}
        for k, v in e.items():
            mA[k[:2]] = mA.get(k[:2], F(0)) + v; mB[k[2:]] = mB.get(k[2:], F(0)) + v
        prod = all(e.get(a + b, F(0)) == mA.get(a, F(0)) * mB.get(b, F(0)) for a in itertools.product((0, 1), repeat=2) for b in itertools.product((0, 1), repeat=2))
        print(f"  deck={deck}: extreme {fmt(e)}  product={prod}")
