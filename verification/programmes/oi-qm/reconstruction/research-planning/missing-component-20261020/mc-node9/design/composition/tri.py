"""Triangular first-light CA: row T holds current-slice sources at cells (i, T-i, 0), i=0..T; row T-1 previous-slice
sources at (i, T-1-i, 0). u_l(i) = H(u_(l+1)(i) xor u_(l+1)(i+1)); output D of u_0(0)."""
import numpy as np
from engine import vars_tt
def H3(a,b,d): return b,d,a^(b&d)
def run_tri(T,srcs,n):
    """srcs: list of (row in {T,T-1}, i, field, j or 'one'); returns the triple at the apex (truth tables)."""
    vs,full=vars_tt(n); W=len(full)
    row=[[np.zeros(W,np.uint64) for _ in range(3)] for _ in range(T+1)]
    inj=[[np.zeros(W,np.uint64) for _ in range(3)] for _ in range(T)]
    for r,i,f,j in srcs:
        val=full if j=='one' else vs[j]
        if r==T: row[i][f]=row[i][f]^val
        else: inj[i][f]=inj[i][f]^val
    for l in range(T-1,-1,-1):
        new=[]
        for i in range(l+1):
            s=[row[i][f]^row[i+1][f] for f in range(3)]
            a,b,d=H3(*s)
            if l==T-1: a,b,d=a^inj[i][0],b^inj[i][1],d^inj[i][2]
            new.append([a,b,d])
        row=new
    return row[0],full
