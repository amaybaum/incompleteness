"""{0,1} straight lines with row 0 = 0: admissible rows per index and pair-compatibility sizes, then DFS."""
import sys, time, pickle; sys.path.insert(0, 'a38')
from lib38 import *
t0 = time.time()
FULL = (1 << 16) - 1
masks = np.arange(1 << 16, dtype=np.int64)
adm = {}
for i in range(1, 16):
    V = vanishing(0, i)
    ok = V[masks] & V[FULL ^ masks]
    adm[i] = masks[ok]
    print('row', i, 'admissible {0,1} rows:', len(adm[i]))
# pair compatibility: rows v (index i), v' (index i2): masks v&~v', ~v&v', rest must vanish for pair (i,i2)
def compat(i, i2):
    V = vanishing(i, i2); A, B = adm[i], adm[i2]
    a = A[:, None]; b = B[None, :]
    m1 = a & ~b & FULL; m2 = ~a & b & FULL; m0 = FULL ^ m1 ^ m2
    return V[m1] & V[m2] & V[m0]
C = {}
for i in range(1, 16):
    for i2 in range(i + 1, 16):
        C[(i, i2)] = compat(i, i2)
        print('pair', (i, i2), 'compatible:', int(C[(i, i2)].sum()), 'of', C[(i, i2)].size)
print('%.1fs' % (time.time() - t0))
pickle.dump((adm, C), open('a38/stage1_tables.pkl', 'wb'))
