"""Exploration (not evidence): what are the extra 9 dimensions of V1?"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eqclib import *
NU=240
def cond_rows(x, y):
    w = vec(prodState(x, y))
    hmx_ = [Fr(1)] + [-F(c) for c in x]
    hmy_ = [Fr(1)] + [-F(c) for c in y]
    rows = []
    for n in range(4):
        row = [Fr(0)] * NU
        for m in range(4):
            r = 4*m+n
            if r == 0: continue
            for c in range(16):
                if w[c] != 0: row[(r-1)*16+c] += hmx_[m]*w[c]
        rows.append(row)
    for m in range(4):
        row = [Fr(0)] * NU
        for n in range(4):
            r = 4*m+n
            if r == 0: continue
            for c in range(16):
                if w[c] != 0: row[(r-1)*16+c] += hmy_[n]*w[c]
        rows.append(row)
    return rows
pool = [unit_vector(s, t) for (s, t) in [(0,0),(1,0),(0,1),(2,0),(0,3),(1,1),(Fr(1,2),2),(3,-1),(-2,Fr(1,3)),(Fr(2,5),Fr(-3,4)),(5,7),(-1,-4)]]
pool += [[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0]]
inc = IncRank(NU)
for x in pool:
    for y in pool:
        for r in cond_rows(x,y): inc.add(r)
ns = inc.nullspace()
print("dim", len(ns))
def toX(v):
    X = zeros(16,16)
    for k,val in enumerate(v):
        X[k//16+1][k%16] = val
    return X
L_ = [ad_herm(SIG2[(i, 0)]) for i in (1, 2, 3)] + [ad_herm(SIG2[(0, j)]) for j in (1, 2, 3)]
M1 = [ad_herm(SIG2[(i, j)]) for i in (1, 2, 3) for j in (1, 2, 3)]
RB = actT_mat(REFLY)
M2 = [matmul(matmul(RB, m), RB) for m in M1]
known = [flat(X) for X in L_+M1+M2]
# find complement directions: reduce nullspace vectors modulo known span
kn = IncRank(256)
for v in known: kn.add(v)
extra = []
for v in ns:
    X = toX(v)
    if kn.add(flat(X)):
        extra.append(X)
print("extra count", len(extra))
blocks = {'11':[0],'31':[4,8,12],'13':[1,2,3],'33':[5,6,7,9,10,11,13,14,15]}
def blk(i):
    for k,v in blocks.items():
        if i in v: return k
for X in extra[:9]:
    nz = {}
    for r in range(16):
        for c in range(16):
            if X[r][c] != 0:
                key = (blk(r), blk(c))
                nz[key] = nz.get(key,0)+1
    print(nz)
# print one extra element fully
X = extra[0]
for r in range(16):
    print([str(X[r][c]) for c in range(16)])
