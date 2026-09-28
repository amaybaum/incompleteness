import numpy as np, collections
msize = np.load('msize.npy')
ALL = (1 << 16) - 1
hist = collections.Counter(); surv = []
for R in range(1, 1 << 16):
    if R & 1: continue      # row 0 zero
    Z = ALL ^ R
    lb = sum(int(msize[i, Z]) for i in range(16) if (R >> i) & 1)
    r = bin(R).count('1')
    hist[(r, min(lb, 99))] += 1
    if lb <= 47: surv.append((R, lb))
byr = collections.defaultdict(list)
for (r, lb), c in hist.items(): byr[r].append((lb, c))
for r in sorted(byr): print(r, sorted(byr[r])[:12])
print('surviving R (LB<=47):', len(surv), collections.Counter(bin(R).count('1') for R, lb in surv))
np.save('survR.npy', np.array(surv))
