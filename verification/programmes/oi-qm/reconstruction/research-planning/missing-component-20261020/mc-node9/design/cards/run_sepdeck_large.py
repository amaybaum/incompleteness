"""Pressure test of the SEPDECK witnesses found within the bound: do they survive more cards (scarcity artifact?)"""
from cardtheory import *
import time
for d1, d2 in [((1,1),(2,2)), ((2,2),(2,2)), ((3,1),(1,3)), ((2,1),(1,2)), ((2,1),(2,1)), ((3,1),(3,1)), ((2,2),(3,1))]:
    for na, nb in [(1,1),(1,2),(2,1),(2,2)]:
        A = [f"a{i+1}" for i in range(na)]; B = [f"b{i+1}" for i in range(nb)]
        m = Model([d1, d2], {"a": A, "b": B}); t = time.time()
        nodes, depth, bp, st = closure(m, s_max=400000)
        res = analyse(m, A, B, nodes, depth, bp, verbose=False)[0]
        print(f"  SEPDECK d1={d1} d2={d2} A={na} B={nb} {st['status']}@{st['depth']} nodes={len(nodes)} |PAB|={res['n_PAB']} ext={res['n_extreme']} "
              f"M1wit(ext)={res['n_M1_witness_extreme']} P(a1=R)={','.join(res['witness_P(a1=R) values'])} [{time.time()-t:.1f}s]", flush=True)
