"""Coordinator checks of the emission-map handoff v1 (independent code; standard library and fractions only).

E1  the exact-time witness at n = 63, m = 256, recomputed by reducing every timestamp D/P with a gcd (no closed-form
    count): per-trial success, the denominator event, the full-record event probabilities, and the exact gap > 1/2.
E2  mixtures at n = 3 with the full three-component enumeration: for X-mix and R-mix, every menu read is exactly
    unbiased conditional on each exact timestamp; positive control X-mix against Y-mix (the same arithmetic up to
    the swap x <-> y): the (success, timestamp, read along a) laws are identical for every a; X-mix against R-mix:
    the single-trial (success, timestamp) laws differ.
E3  the 16-bin herald record (attempt index and bin, or all-fail) TV at n = 63, m = 256, from bins computed as
    ceil(16 D / P) for every depth.
E4  probe (gem-finding): the attempt index alone, or all-fail. Per-trial success p_w = E[(5 w.S)_+]/M differs between
    the X and R stations at finite n, so the number of trials leaks the preparation even without any timestamp.
    With a continuous uniform depth the timestamp given success is uniform, so this attempt-only distance is then the
    entire herald-record distance.
"""
from fractions import Fraction as F
from math import comb, gcd, ceil
from itertools import product

def M_of(n): return 1<<(9*n-1).bit_length()
def P_of(st,x,y,z):
    return {'+X':5*x,'-X':-5*x,'+Y':5*y,'-Y':-5*y,'+R':4*x+3*y,'-R':-(4*x+3*y)}[st]
def vals(n): return [(2*k-n,comb(n,k)) for k in range(n+1)]

def station_xy(n,st):
    """Exact counts over (S_x, S_y) (S_z integrates out): success weight, denominator event and 16 bins, by direct
    reduction of each timestamp."""
    succ=0; ev=0; bins=[0]*16
    for x,mx in vals(n):
        for y,my in vals(n):
            P=P_of(st,x,y,0)
            if P<=0: continue
            m=mx*my; succ+=m*P
            e=0
            for D in range(1,P+1):
                den=P//gcd(D,P)
                if den%5==0: e+=1
                bins[ceil(16*D/P)-1]+=m
            ev+=m*e
    return succ,ev,bins

def E1():
    n,m=63,256; M=M_of(n); base=M*4**n
    sx,ex,_=station_xy(n,'+X'); sr,er,_=station_xy(n,'+R')
    px,pr=F(sx,base),F(sr,base)
    cx,cr=1-(1-px)**m,1-(1-pr)**m
    fx,fr=cx*F(ex,sx),cr*F(er,sr)
    gap=fx-fr
    ok= gap>F(1,2) and '%.12f'%float(fx)=='0.819346363181' and '%.12f'%float(fr)=='0.164250679444'
    print('E1  n=63, M=%d, m=256, gcd reduction of every timestamp: completion %.12f %.12f; event %.12f %.12f; gap %.12f > 1/2 (exact): %s'%(M,float(cx),float(cr),float(fx),float(fr),float(gap),ok))
    return ok
def E2():
    n=3; M=M_of(n); ok=True
    def law(st):
        """single trial: {(T, a, read): weight} plus the failure weight, over the full (x, y, z) enumeration"""
        out={}; fail=0; tl={}
        for (x,mx),(y,my),(z,mz) in product(vals(n),vals(n),vals(n)):
            w=mx*my*mz; P=P_of(st,x,y,z)
            reads={'X':x>0,'Y':y>0,'Z':z>0,'R':4*x+3*y>0}
            for D in range(1,M+1):
                if 0<D<=P:
                    T=F(D,P); tl[T]=tl.get(T,0)+w
                    for a,r in reads.items(): out[(T,a,r)]=out.get((T,a,r),0)+w
                else: fail+=w
        return out,fail,tl
    L={st:law(st) for st in ('+X','-X','+Y','-Y','+R','-R')}
    def mix(a,b):
        o={};f=L[a][1]+L[b][1];t={}
        for s in (a,b):
            for k,v in L[s][0].items(): o[k]=o.get(k,0)+v
            for k,v in L[s][2].items(): t[k]=t.get(k,0)+v
        return o,f,t
    X,Y,R=mix('+X','-X'),mix('+Y','-Y'),mix('+R','-R')
    unb=True
    for mx_ in (X,R):
        for T,wt in mx_[2].items():
            for a in 'XYZR': unb&= 2*mx_[0].get((T,a,True),0)==wt
    same=(X[0]==Y[0] and X[1]==Y[1])
    diff=(X[2]!=R[2])
    tot=2*M_of(n)*8**n
    tvT=F(abs(X[1]-R[1])+sum(abs(X[2].get(T,0)-R[2].get(T,0)) for T in set(X[2])|set(R[2])),2*tot)
    ok=unb and same and diff
    print('E2  n=3 full enumeration: menu reads unbiased given every timestamp for X-mix and R-mix: %s; X-mix = Y-mix on (success, timestamp, read): %s; X-mix and R-mix single-trial timestamp laws differ: %s (TV %s = %.6f)'%(unb,same,diff,tvT,float(tvT)))
    return ok
def E3():
    n,m=63,256; M=M_of(n); base=M*4**n
    _,_,bx=station_xy(n,'+X'); _,_,br=station_xy(n,'+R')
    qx=[F(b,base) for b in bx]; qr=[F(b,base) for b in br]
    fx=1-sum(qx); fr=1-sum(qr)
    tv=abs(fx**m-fr**m); ax=F(1); ar=F(1)
    for a in range(m):
        tv+=sum(abs(ax*u-ar*v) for u,v in zip(qx,qr)); ax*=fx; ar*=fr
    tv/=2
    ok='%.12f'%float(tv)=='0.015685376946'
    print('E3  16-bin herald record, n=63, m=256, bins from ceil(16 D/P): TV %.15f (owner 0.015685376946): %s'%(float(tv),ok))
    return ok,tv
def E4():
    rows=[]
    for n in (7,15,31,63,127):
        M=M_of(n); base=M*4**n; m=256
        s={}
        for st in ('+X','+R'):
            tot=0
            for x,mx in vals(n):
                for y,my in vals(n):
                    P=P_of(st,x,y,0)
                    if P>0: tot+=mx*my*P
            s[st]=F(tot,base)
        px,pr=s['+X'],s['+R']
        tv=abs((1-px)**m-(1-pr)**m); ax=F(1); ar=F(1)
        for a in range(m):
            tv+=abs(ax*px-ar*pr); ax*=1-px; ar*=1-pr
        tv/=2
        rows.append((n,float(px),float(pr),float(tv)))
    print('E4  attempt-index-only record (m=256): (n, p_X, p_R, TV) %s'%['(%d, %.6f, %.6f, %.3e)'%r for r in rows])
    return rows
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    a=E1(); b=E2(); c,tv16=E3(); rows=E4()
    r63=[r for r in rows if r[0]==63][0]
    print('    consistency: attempt-only TV at n=63 (%.6e) <= 16-bin TV (%.6e), as a coarsening must be: %s'%(r63[3],float(tv16),r63[3]<=float(tv16)))
    print('coordinator checks:','green' if a and b and c and r63[3]<=float(tv16) else 'RED')
