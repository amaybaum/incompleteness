import time; t0=time.time()
from lib42 import *
print('loaded %.1fs' % (time.time()-t0))
for E, nm in ((A38,'A'),(B38,'B'),(C38,'C'),(WIT38,'A+B+C'),(WMAT,'W')):
    print(nm, 'support', support(E), 'straight', straight(E), straight_direct(E), 'strict', memberships(E, False), 'relaxed', memberships(E, True))
# minimal vanishing subsets per row pair
import collections
MINV = {}
for i in range(16):
    for i2 in range(i+1,16):
        V = vanishing(i,i2); vm = np.flatnonzero(V)[1:]  # exclude 0
        vs = set(vm.tolist()); mins = []
        for m in sorted(vs, key=lambda x: bin(x).count('1')):
            # minimal iff no nonempty proper submask vanishing: check via mins found so far (mins are smaller)
            if not any((mm & m) == mm for mm in mins): mins.append(m)
        MINV[(i,i2)] = mins
        print((i,i2), 'nvanishing', len(vs), 'minimal', len(mins), 'sizes', dict(collections.Counter(bin(m).count('1') for m in mins)))
print('%.1fs' % (time.time()-t0))
