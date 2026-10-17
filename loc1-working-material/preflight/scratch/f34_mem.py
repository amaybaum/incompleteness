import sys, tracemalloc, time
sys.path.insert(0, sys.argv[1])
import f34_enum as F
tracemalloc.start()
t=time.perf_counter()
pts, decs = F.enumerate_decomps()
cur, peak = tracemalloc.get_traced_memory()
print("enumeration: %d decompositions, tracemalloc current %.1f MB peak %.1f MB" % (len(decs), cur/1e6, peak/1e6))
tracemalloc.reset_peak()
M = F.eye(4); M[0][1] = 1
h = {}
for B, Bi in decs:
    dm = F.coupling(F.gmat(B, Bi, M))[0]; h[dm] = h.get(dm, 0) + 1
cur, peak = tracemalloc.get_traced_memory()
print("streaming coupling graphs for one synthetic rule: peak above enumeration %.1f MB" % ((peak-cur)/1e6))
