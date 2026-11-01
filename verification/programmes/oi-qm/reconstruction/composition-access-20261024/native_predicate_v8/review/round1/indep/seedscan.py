"""Reviewer: independent old-q9 seed scan. python3 -I -B seedscan.py"""
import sys, importlib.util
spec = importlib.util.spec_from_file_location('rd', sys.argv[1]); rd = importlib.util.module_from_spec(spec); spec.loader.exec_module(rd)
def oldq9(seed):
    prev, cur = rd.background(seed)
    for f in rd.src: cur.pop(f, None)
    sl = {-1: prev, 0: cur}
    for t in range(1, rd.n+1):
        new = {}
        for x in rd.ball(rd.n - t):
            acc = 0
            for d in rd.nbr: acc ^= sl[t-1].get((x[0]+d[0], x[1]+d[1], x[2]+d[2]), 0)
            new[x] = sl[t-2].get(x, 0) ^ rd.H(acc)
        sl[t] = new
    return sl[rd.n][(0,0,0)]
chosen, cnt = [], {0:0, 1:0}
for seed in range(1, 60):
    p = oldq9(seed)
    if p >> 2 == 0 and cnt[p >> 1 & 1] < 8:
        chosen.append(seed); cnt[p >> 1 & 1] += 1
    if cnt[0] == 8 and cnt[1] == 8: break
print(chosen)
