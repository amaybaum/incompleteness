"""Coordinator checks of the aggregation-components handoff v1 (independent code; numpy).

Layouts are transcribed from the handoff's REPORT.md table (not from its checker); RECORDS.json is evaluated by a
separate polynomial evaluator. Usage: coordinator_aggregation_checks.py <path to RECORDS.json>

H1  full-torus simulation of each layout (L = 6T+3) on two new dense backgrounds, all 2^n inputs at once: the
    complete device record (all fields on B_2T, ticks -1..T) equals the published polynomials; the D register at the
    receiver is AND_n with algebraic degree n (Moebius transform); every input-caused write at tick t lies in
    B_(T+t).
H2  joint Cartesian check, n = 4 and n = 5: every input x every reserved-frontier assignment (frontier along -y from
    q, the handoff uses +x) on the full torus with a dense background: the receiver output is correct in every run,
    and for each input the 8^T source words are all distinct and form the same set for every input.
H3  the readiness count recomputed: zero pins, copy equalities and J.
H4  probe: the readiness the output register alone needs. Upper bound (by causality): pin the receiver's own
    initial cone (current B_T, previous B_(T-1)) except inputs and copies. Sensitivity count (not a lower bound, since
    the rule is nonlinear): the pins in that cone whose release to 1 alone, every other pin at zero, makes the output
    wrong for some input.
"""
import sys, json
import numpy as np
from itertools import product
rng=np.random.default_rng(20261024)
# (size added, initial tick, field, position, input index) -- REPORT.md table; receiver positions per size
TABLE=[(3,0,'B',(1,1,0),0),(3,0,'D',(1,-1,0),1),(3,0,'D',(0,0,2),2),(4,0,'A',(0,0,4),3),(4,-1,'B',(0,0,3),2),
       (5,0,'B',(4,-1,1),4),(5,-1,'B',(0,2,1),2),(6,0,'D',(-6,-1,1),5),(6,-1,'A',(-1,-5,1),4)]
RECV={4:(3,(0,0,1)),5:(4,(0,-1,1)),6:(5,(-1,-1,1))}
FI={'A':0,'B':1,'D':2}
def layout(n):
    T,r=RECV[n]
    return T,[(s,FI[f],tuple(a-b for a,b in zip(x,r)),j) for k,s,f,x,j in TABLE if k<=n]
def S(X):
    o=np.zeros_like(X)
    for ax in (-3,-2,-1): o^=np.roll(X,1,ax)^np.roll(X,-1,ax)
    return o
def step(p,c):
    sa,sb,sd=S(c[0]),S(c[1]),S(c[2]); return (p[0]^sb,p[1]^sd,p[2]^sa^(sb&sd))
def l1(L):
    r=np.arange(L); d=np.minimum(r,L-r); return d[:,None,None]+d[None,:,None]+d[None,None,:]
def vol(r): return sum(1 for v in product(range(-r,r+1),repeat=3) if sum(map(abs,v))<=r)
def prepare(n,L,batch_inputs,bgseed=None):
    """returns (prev, cur) with readiness imposed, background dense random (same for every batch row)"""
    T,rows=layout(n); d=l1(L); q=(3*T+1,)*3; N=len(batch_inputs)
    g=np.random.default_rng(bgseed)
    p=[np.repeat(g.integers(0,2,(1,L,L,L),dtype=np.uint8),N,0) for _ in range(3)]
    c=[np.repeat(g.integers(0,2,(1,L,L,L),dtype=np.uint8),N,0) for _ in range(3)]
    for f in range(3):
        c[f][:,d<=3*T]=0; p[f][:,d<=3*T-1]=0; c[f][(slice(None),)+q]=0; p[f][(slice(None),)+q]=0
    u=np.array(batch_inputs)
    for s,f,x,j in rows:
        x=tuple(v%L for v in x)
        (c if s==0 else p)[f][(slice(None),)+x]=(u>>j)&1
    return p,c,q
def evaluate(masks,u):
    out=np.zeros(len(u),np.uint8)
    for m in masks:
        out^=np.all(((u[:,None]>>np.arange(8))&1)[:,[i for i in range(8) if m>>i&1]]==1,axis=1).astype(np.uint8) if m else np.uint8(1)
    return out
def moebius_deg(v,n):
    a=v.copy()
    for i in range(n):
        for m in range(1<<n):
            if m>>i&1: a[m]^=a[m^(1<<i)]
    return max((bin(m).count('1') for m in range(1<<n) if a[m]),default=-1)
def H1(rec):
    ok=True; rows=[]
    for n in (4,5,6):
        T,_=RECV[n][0],None; L=6*T+3; d=l1(L); inside=d<=2*T
        u=np.arange(1<<n)
        snaps=rec[str(n)]
        for bg in range(2):
            p,c,q=prepare(n,L,list(u),bgseed=1000*n+bg)
            def check(fields,snap):
                want=[np.zeros((len(u),L,L,L),np.uint8) for _ in range(3)]
                for x,f,masks in snap:
                    want[f][(slice(None),)+tuple(v%L for v in x)]=evaluate(masks,u)
                return all(np.array_equal(fields[f][:,inside],want[f][:,inside]) for f in range(3))
            ok&=check(p,snaps[0]) and check(c,snaps[1])
            for t in range(1,T+1):
                p,c=c,step(p,c)
                ok&=check(c,snaps[t+1])
                var=np.zeros((L,L,L),bool)
                for f in range(3): var|=(c[f]!=c[f][:1]).any(0)
                ok&=bool((d[var]<=T+t).all())
            out=c[2][:,0,0,0]
            ok&=bool(np.array_equal(out,(u==(1<<n)-1).astype(np.uint8))) and moebius_deg(out,n)==n
        rows.append(n)
    print('H1  n=4,5,6, full torus L=6T+3, two new dense backgrounds, all 2^n inputs: device record on B_2T at every tick equals RECORDS.json, output = AND_n with degree n, input-caused writes at tick t within B_(T+t): %s'%ok)
    return ok
def H2():
    ok=True; info=[]
    for n in (4,5):
        T=RECV[n][0]; L=6*T+3; nf=8**T; chunk=1024
        sets=[]
        for ui in range(1<<n):
            words=[]
            for start in range(0,nf,chunk):
                fr=np.arange(start,min(nf,start+chunk))
                p,c,q=prepare(n,L,[ui]*len(fr),bgseed=77+n)
                for t in range(1,T+1):
                    for f in range(3): c[f][:,q[0],(q[1]-t)%L,q[2]]=(fr>>(3*(t-1)+f))&1
                P,C=tuple(p),tuple(c); w=np.zeros(len(fr),np.int64)
                for t in range(T):
                    P,C=C,step(P,C)
                    w|=sum(C[f][:,q[0],q[1],q[2]].astype(np.int64)<<f for f in range(3))<<(3*t)
                ok&=bool((C[2][:,0,0,0]==int(ui==(1<<n)-1)).all())
                words.append(w)
            w=np.concatenate(words); ok&=len(np.unique(w))==nf; sets.append(np.sort(w).tobytes())
        ok&=len(set(sets))==1; info.append('%d inputs x %d frontier'%(1<<n,nf))
    print('H2  joint Cartesian product on the full torus, dense background, frontier along -y (%s): output correct in every run; per input all source words distinct, same set for every input: %s'%('; '.join(info),ok))
    return ok
def H3():
    ok=True; out=[]
    for n in (4,5,6):
        T,rows=layout(n); m=sum(1 for s,f,x,j in rows if s==-1)
        M=3*(vol(3*T)+vol(3*T-1)); J=M-n+6; zeros=M-n-m+6
        ok&=(J,zeros,m)=={4:(5978,5977,1),5:(14017,14015,2),6:(27240,27237,3)}[n]
        ok&=all(sum(map(abs,x))<=(T if s==0 else T-1) for s,f,x,j in rows)
        out.append('n=%d: %d zero pins + %d copies = J %d'%(n,zeros,m,J))
    print('H3  readiness recount (%s); every slot inside the receiver cone: %s'%('; '.join(out),ok))
    return ok
def H4():
    res=[]
    for n in (4,5,6):
        T,rows=layout(n); L=2*T+5; slots={(s,f,tuple(v%L for v in x)) for s,f,x,j in rows}
        d=l1(L); u=np.arange(1<<n)
        cone=[(0,f,tuple(int(v) for v in x)) for f in range(3) for x in zip(*np.nonzero(d<=T))]+[(-1,f,tuple(int(v) for v in x)) for f in range(3) for x in zip(*np.nonzero(d<=T-1))]
        pins=[k for k in cone if k not in slots]
        def run(extra):
            N=len(u)*len(extra)
            p=[np.zeros((N,L,L,L),np.uint8) for _ in range(3)]; c=[np.zeros((N,L,L,L),np.uint8) for _ in range(3)]
            uu=np.tile(u,len(extra))
            for s,f,x,j in rows: (c if s==0 else p)[f][(slice(None),)+tuple(v%L for v in x)]=(uu>>j)&1
            for k,(s,f,x) in enumerate(extra): (c if s==0 else p)[f][(slice(k*len(u),(k+1)*len(u)),)+x]=1
            P,C=tuple(p),tuple(c)
            for t in range(T): P,C=C,step(P,C)
            return C[2][:,0,0,0].reshape(len(extra),len(u))
        want=(u==(1<<n)-1).astype(np.uint8)
        bad=0
        for start in range(0,len(pins),64):
            outs=run(pins[start:start+64])
            bad+=int((outs!=want[None]).any(1).sum())
        res.append((n,T,len(pins)+sum(1 for s,f,x,j in rows if s==-1),bad,3*(vol(3*T)+vol(3*T-1))-n))
    print('H4  probe, output register alone (source pins excluded): (n, T, receiver-cone constraints incl. copies [upper bound], pins that alone break the output [sensitivity count], full-record buffer constraints) %s'%res)
    return res
if __name__=='__main__':
    rec=json.loads(open(sys.argv[1]).read())
    print(__doc__.strip().splitlines()[0])
    r=[H1(rec),H3()]; H4(); r.append(H2())
    print('coordinator positive checks:','green' if all(r) else 'RED')
