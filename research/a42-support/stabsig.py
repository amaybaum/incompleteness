from lib42 import *
def deph16(M):
    M = [[M[i][j] * M[i][0].conj() for j in range(16)] for i in range(16)]
    return [[M[i][j] * M[0][j].conj() for j in range(16)] for i in range(16)]
def key16(M): return tuple(x.key() for r in M for x in r)
K0 = key16(deph16(SIG))
def transport(p, s_, inverse=False):
    out = [[None]*16 for _ in range(16)]
    for t in range(256):
        i, j = divmod(t, 16); i2, j2 = divmod(p[t], 16)
        v = SIG[i][j] if s_ == 1 else SIG[i][j].conj()
        if inverse: out[i][j] = SIG[i2][j2] if s_ == 1 else SIG[i2][j2].conj()
        else: out[i2][j2] = v
    return out
import collections
c = collections.Counter()
for p, s_ in elems:
    a = key16(deph16(transport(p, s_))) == K0
    b = key16(deph16(transport(p, s_, True))) == K0
    c[(a, b)] += 1
print('(forward preserves SIG up to dephasing, inverse preserves):', c)
