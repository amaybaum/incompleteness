"""Fast triangular CA on packed truth tables held as Python ints (n<=8 -> 256-bit ints)."""
def tt_vars(n):
    N=1<<n; full=(1<<N)-1
    vs=[]
    for j in range(n):
        v=0
        for a in range(N):
            if a>>j&1: v|=1<<a
        vs.append(v)
    return vs,full
def apex(T,srcs,vs,full):
    rowA=[0]*(T+1); rowB=[0]*(T+1); rowD=[0]*(T+1)
    injA=[0]*T; injB=[0]*T; injD=[0]*T
    for r,i,f,j in srcs:
        val=full if j<0 else vs[j]
        if r==T: (rowA,rowB,rowD)[f][i]^=val
        else: (injA,injB,injD)[f][i]^=val
    for l in range(T-1,-1,-1):
        nA=[0]*(l+1); nB=[0]*(l+1); nD=[0]*(l+1)
        for i in range(l+1):
            a=rowA[i]^rowA[i+1]; b=rowB[i]^rowB[i+1]; d=rowD[i]^rowD[i+1]
            nA[i]=b; nB[i]=d; nD[i]=a^(b&d)
            if l==T-1: nA[i]^=injA[i]; nB[i]^=injB[i]; nD[i]^=injD[i]
        rowA,rowB,rowD=nA,nB,nD
    return rowA[0],rowB[0],rowD[0]
