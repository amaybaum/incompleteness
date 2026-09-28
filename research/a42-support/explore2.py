from lib42 import *
from linalg42 import *
import collections, time
t0=time.time()
rows = []
for i in range(16):
    for i2 in range(i+1,16):
        for arr in (CRE, CIM):
            v = [0]*256
            for k in range(16):
                v[i*16+k] += int(arr[i,i2,k]); v[i2*16+k] -= int(arr[i,i2,k])
            rows.append(v)
R, piv = rref(rows, 256)
print('rank', len(piv), 'dim T', 256-len(piv), '%.1fs'%(time.time()-t0))
ns = nullspace(rows, 256)
Rb, pb = rref(ns, 256)
parent = list(range(256))
def f(x):
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
for r in Rb:
    sup = [j for j in range(256) if r[j]!=0]
    for j in sup[1:]: parent[f(j)] = f(sup[0])
comps = collections.Counter(f(j) for j in range(256))
print('components of T (with gauge):', sorted(comps.values()))
import pickle; pickle.dump(ns, open('T_basis.pkl','wb'))
