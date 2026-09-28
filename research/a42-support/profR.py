import sys, time
sys.argv = [sys.argv[0], '47'] + sys.argv[1:]
from dfsR import *
Rs = [int(x) for x in open('Rreps_47.txt').read().split()]
lo, hi = int(sys.argv[2]), int(sys.argv[3])
for n in range(lo, hi):
    R = Rs[n]; t0 = time.time(); S = RSearch(R)
    sizes = {i: len(S.C[i][0]) for i in S.rows}
    t1 = time.time()
    print(n, hex(R), 'r', len(S.rows), 'ms', S.ms, 'cand sizes', sizes, 'build %.1fs' % (t1 - t0), flush=True)
