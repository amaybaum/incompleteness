"""Reviewer check (exact, independent of g1lib/eng/coordinator): brute-force enumeration of every automorphism
of E covering each card map, for C=Z2 (real Pauli) and C=Z4 (complex Pauli), n=2,3; B1 locality tested
element-wise on R_sigmabar built by group closure. No word-level / distribution computation is done."""
import sys
from itertools import product
def make(n,C):
    # element (k,x,z): i^k X^x Z^z, x,z bitmasks; Z2 case: k in {0,2}
    def mul(g,h):
        k1,x1,z1=g; k2,x2,z2=h
        s=bin(z1&x2).count('1')&1
        return ((k1+k2+2*s)%4,x1^x2,z1^z2)
    ks=(0,2) if C==2 else (0,1,2,3)
    elems=[(k,x,z) for k in ks for x in range(1<<n) for z in range(1<<n)]
    return mul,elems
def closure(mul,gens,ident=(0,0,0)):
    S={ident}|set(gens); fr=list(S)
    while fr:
        new=[]
        for g in fr:
            for h in list(S):
                for p in (mul(g,h),mul(h,g)):
                    if p not in S: S.add(p); new.append(p)
        fr=new
    return S
def cardmap(n,op):
    # returns function on labels (x,z) -> (x',z'); bit j = system j
    kind=op[0]
    def f(x,z):
        if kind=='s':
            j=op[1]; bx=(x>>j)&1; bz=(z>>j)&1
            x=(x&~(1<<j))|(bz<<j); z=(z&~(1<<j))|(bx<<j); return x,z
        j,k=op[1],op[2]  # couple_jk: q_k ^= q_j, p_j ^= p_k ; X_j->X_jX_k, Z_k->Z_jZ_k
        if (x>>j)&1: x^=1<<k
        if (z>>k)&1: z^=1<<j
        return x,z
    return f
def enumerate_lifts(n,C,op):
    mul,elems=make(n,C); f=cardmap(n,op)
    gens=[(0,1<<j,0) for j in range(n)]+[(0,0,1<<j) for j in range(n)]
    def fiber(x,z): return [(k,x,z) for k in ((0,2) if C==2 else (0,1,2,3))]
    imgs=[fiber(*f(g[1],g[2])) for g in gens]
    iimgs=[(1,0,0)] if C==2 else [(1,0,0),(3,0,0)]   # image of i (Z2: only -1=(2,0,0), fixed)
    # normal form of element: i^k * prod_j X_j^{x_j} * prod_j Z_j^{z_j}
    lifts=[]
    for choice in product(*imgs):
        for ii in iimgs:
            def phi(e,choice=choice,ii=ii):
                k,x,z=e; r=(0,0,0)
                if C==2: r=(k,0,0)  # -1 central and fixed
                else:
                    for _ in range(k): r=mul(r,ii)
                for j in range(n):
                    if (x>>j)&1: r=mul(r,choice[j])
                for j in range(n):
                    if (z>>j)&1: r=mul(r,choice[n+j])
                return r
            table={e:phi(e) for e in elems}
            if len(set(table.values()))!=len(elems): continue
            ok=True
            for g in gens+([(1,0,0)] if C==4 else []):
                for h in elems:
                    if table[mul(g,h)]!=mul(table[g],table[h]): ok=False; break
                if not ok: break
            if ok: lifts.append((table, C==4 and ii==(3,0,0)))
    return mul,elems,lifts
def report(n,C,ops):
    out={}
    for op in ops:
        mul,elems,lifts=enumerate_lifts(n,C,op)
        touched={op[1]} if op[0]=='s' else {op[1],op[2]}
        spect=[k for k in range(n) if k not in touched]
        gensR=[(1,0,0) if C==4 else (2,0,0)]+[(0,1<<k,0) for k in spect]+[(0,0,1<<k) for k in spect]
        R=closure(mul,gensR)
        smask=sum(1<<k for k in spect)
        pre={e for e in elems if (e[1]&~smask)==0 and (e[2]&~smask)==0}
        assert R==pre, 'R_sigmabar != full preimage of V_sigmabar'
        if C==4:
            for k in spect: assert (1,1<<k,1<<k) in R  # i*X_k*Z_k (= Y_k up to the X^xZ^z ordering)
        # mutant record algebra: only <d(X_k),d(Z_k)> (no C adjoined beyond what they generate)
        Rm=closure(mul,[(0,1<<k,0) for k in spect]+[(0,0,1<<k) for k in spect])
        triv=[t for t,inv in lifts if not inv]; invl=[t for t,inv in lifts if inv]
        loc=lambda t,RR: all(t[e]==e for e in RR)
        gen_only=lambda t: all(t[g]==g for g in gensR)
        row=dict(total_trivC=len(triv),total_invC=len(invl),
                 B1_trivC=sum(loc(t,R) for t in triv),B1_invC=sum(loc(t,R) for t in invl),
                 genonly_trivC=sum(gen_only(t) for t in triv),
                 mutantB1_noC_trivC=sum(loc(t,Rm) for t in triv),mutantB1_noC_invC=sum(loc(t,Rm) for t in invl),
                 R_size=len(R),Rm_size=len(Rm))
        out[op]=row
        print('n=%d C=Z%d op=%s spectators=%s'%(n,C,op,spect),row); sys.stdout.flush()
    return out
if __name__=='__main__':
    for n,ops in [(2,[('s',0),('s',1),('c',0,1)]),(3,[('s',0),('s',1),('s',2),('c',0,1),('c',1,2)])]:
        for C in (2,4):
            r=report(n,C,ops)
            prod_=1
            for op in ops: prod_*=r[op]['B1_trivC']+r[op]['B1_invC']
            print('n=%d C=Z%d product of B1-local counts over declared lifted ops = %d'%(n,C,prod_))
