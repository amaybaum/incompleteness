import sys, time, random
from dfs42 import *
t0 = time.time()
G = global_rows(); print('global rows', len(G[0]), '%.0fs' % (time.time() - t0), flush=True)
budget = int(sys.argv[1]); nprobe = int(sys.argv[2])
S = Search(G, (0, 0), 0, budget)
print('candidate sizes', S.sizes, '%.0fs' % (time.time() - t0), flush=True)
rng = random.Random(1); ests = []
for k in range(nprobe):
    ests.append(S.run(lambda a, u: None, knuth=True, rng=rng))
    print(k, 'est %.3g mean %.3g' % (ests[-1], sum(ests) / len(ests)), '%.0fs' % (time.time() - t0), flush=True)
