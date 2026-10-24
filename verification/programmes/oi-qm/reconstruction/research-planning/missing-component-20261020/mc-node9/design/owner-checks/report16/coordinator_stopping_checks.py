"""Coordinator checks of the rule-census and stopping-readiness handoffs v1 (independent code; numpy).

P1  rule census, own derivation: the 48 signed permutations and their orbits on the 64 neighbour patterns, all 1024
    invariant rules, the three conditions (quiescent, pulse, balanced), and the exact three-tick law of each survivor
    by direct vectorized enumeration of all 2^24 (A, B) assignments in the reduced cone.
P2  rule census, against the actual dynamics: the port's three-tick law on a 9^3 torus by Monte Carlo (uniform
    phases with the port pair zero), for XOR (298) and the most biased survivor (472); statistical evidence for the
    light-cone reduction, not certification.
S1  stopping theorem, exact: per field, the rows of every readiness intersection over the initial wave bits, built
    by evolving delta initial data (S is symmetric); for all six geometries and all 48 intersections the payload and
    the K future source triples raise the rank by 2 + 3K, and the receiver identities lie in the span of E_w.
S2  stopping theorem, raw: K = 3, L = 25. A uniform raw state at tick w satisfying the raw readiness predicate is
    run backwards with the explicit inverse of the raw rule (no linear-wave coordinates) to check failures at
    earlier ticks, and forwards K ticks; receiver record exact; payload and source marginals by chi-square.
S3  the stopped law versus the fixed-start law: TV between conditioning on W = w and on E_w is
    1 - P(W = w)/P(E_w), exact from the ranks.
S4  first-hit versus return: random permutations up to 3000 states and random events; the mean first hit from a
    uniform start on Sat(E) equals sum l(l - 1)/(2|Sat|), the mean return equals |Sat|/|E|, and the deadline bound.
"""
import numpy as np
from itertools import permutations, product
from fractions import Fraction as F
from math import comb
rng=np.random.default_rng(20261023)
D6=((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))

# ---------------- rule census ----------------
def P1():
    G=[]
    for p in permutations(range(3)):
        for s in product((-1,1),repeat=3):
            G.append([D6.index(tuple(s[i]*v[p[i]] for i in range(3))) for v in D6])
    orb={}; lab=[None]*64
    for x in range(64):
        if lab[x] is not None: continue
        o={sum(((x>>j)&1)<<g[j] for j in range(6)) for g in G}
        k=len(orb); orb[k]=o
        for y in o: lab[y]=k
    nr=len(orb); surv=[]
    for code in range(1<<nr):
        f=np.array([(code>>lab[x])&1 for x in range(64)],np.uint8)
        if f[0]==0 and f[1]==1 and f.sum()==32: surv.append(f)
    # reduced cone: A = six current neighbours of the root at t=0; B = 18 even radius-two sites at t=1.
    even=sorted({tuple(a+b for a,b in zip(u,v)) for u in D6 for v in D6}-{(0,0,0)})
    assert len(even)==18
    idxB={s:i for i,s in enumerate(even)}
    Bs=np.arange(1<<18,dtype=np.int64)
    res=[]
    for f in surv:
        counts=np.zeros((2,2),np.int64)
        for h in (0,1):
            g=np.zeros(1<<18,np.int64)
            for j,v in enumerate(D6):
                m=np.zeros(1<<18,np.int64)
                for k,d in enumerate(D6):
                    s=tuple(a+b for a,b in zip(v,d))
                    bit=np.full(1<<18,h,np.int64) if s==(0,0,0) else (Bs>>idxB[s])&1
                    m|=bit<<k
                g|=f[m].astype(np.int64)<<j
            ghist=np.bincount(g,minlength=64)
            for a in range(64):
                if f[a]!=h: continue
                h3=f[a^np.arange(64)]^f[a]
                counts[h,0]+=ghist[h3==0].sum(); counts[h,1]+=ghist[h3==1].sum()
        res.append((f,counts))
    print('P1  rule census: %d group elements, %d orbits, %d invariant rules, %d survivors'%(len(G),nr,1<<nr,len(surv)))
    ok=len(G)==48 and nr==10 and len(surv)==6
    table={}
    for f,c in res:
        lin=all(f[x]==bin(x).count('1')%2 for x in range(64))
        p0,p1=F(int(c[0,0]),1<<24),F(int(c[1,0]),1<<24)
        tv=abs(p0-F(1,4))+abs(p1-F(1,4))
        table[lin]=table.get(lin,[])+[tv]
        print('    %s P(h1=0,h3=0)=%s P(h1=1,h3=0)=%s TV=%s'%('XOR     ' if lin else 'nonlinear',p0,p1,tv))
    ok&= table[True]==[0] and all(t>0 for t in table[False]) and min(table[False])==F(441,524288)
    print('P1  only XOR has three-tick TV 0; smallest nonlinear TV 441/524288: %s'%ok)
    return ok,res

def P2(res):
    L=9; N=200000; out={}
    lin_of=lambda f:all(f[x]==bin(x).count('1')%2 for x in range(64))
    nonlin=[r for r in res if not lin_of(r[0])]
    worst=max(nonlin,key=lambda r:abs(F(int(r[1][0,0]),1<<24)-F(1,4))+abs(F(int(r[1][1,0]),1<<24)-F(1,4)))
    for f,cts in [r for r in res if lin_of(r[0])]+[worst]:
        lin=lin_of(f)
        cnt=np.zeros(8,np.int64); done=0
        while done<N:
            n=20000
            p=rng.integers(0,2,(n,L,L,L),dtype=np.uint8); c=rng.integers(0,2,(n,L,L,L),dtype=np.uint8)
            p[:,0,0,0]=0; c[:,0,0,0]=0
            hs=[]
            for _ in range(3):
                m=np.zeros_like(c,dtype=np.int64)
                for k,(ax,sh) in enumerate(((-3,1),(-3,-1),(-2,1),(-2,-1),(-1,1),(-1,-1))):
                    m|=np.roll(c,sh,ax).astype(np.int64)<<k
                p,c=c,f[m]^p; hs.append(c[:,0,0,0].astype(np.int64))
            cnt+=np.bincount(hs[0]*4+hs[1]*2+hs[2],minlength=8); done+=n
        exact=(F(int(cts[0,0]),1<<24),F(int(cts[1,0]),1<<24))
        out['XOR' if lin else 'worst']=(cnt,exact)
    return out

# ---------------- stopping theorem ----------------
def S_(X):
    o=np.zeros_like(X)
    for ax in (-3,-2,-1): o^=np.roll(X,1,ax)^np.roll(X,-1,ax)
    return o
def l1(L):
    r=np.arange(L); d=np.minimum(r,L-r); return d[:,None,None]+d[None,:,None]+d[None,None,:]
def rowbuilder(L):
    W=-(-2*L**3//8)*8
    def rows(items):
        """items: (t, site) with t >= -1; returns packed row ints over (u(0), u(-1)), via delta responses."""
        out=[None]*len(items)
        for start in range(0,len(items),48):
            chunk=items[start:start+48]; n=len(chunk); T=max(max(t for t,_ in chunk),0)
            resp=[]
            for which in (0,1):
                cur=np.zeros((n,L,L,L),np.uint8); old=np.zeros_like(cur)
                for k,(t,s) in enumerate(chunk): (cur if which==0 else old)[(k,)+s]=1
                got=np.zeros((n,L,L,L),np.uint8)
                for k,(t,s) in enumerate(chunk):
                    if t==0: got[k]=cur[k]
                    if t==-1: got[k]=old[k]
                for t in range(1,T+1):
                    cur,old=S_(cur)^old,cur
                    for k,(tt,s) in enumerate(chunk):
                        if tt==t: got[k]=cur[k]
                resp.append(got.reshape(n,-1))
            M=np.concatenate(resp,1)
            for k in range(n): out[start+k]=int.from_bytes(np.packbits(M[k]).tobytes(),'big')
        return out
    return rows
def reduce_(piv,v):
    while v:
        h=v.bit_length()-1
        if h in piv: v^=piv[h]
        else: return v
    return 0
def add_rows(piv,rs):
    piv=dict(piv); added=0
    for v in rs:
        v=reduce_(piv,v)
        if v: piv[v.bit_length()-1]=v; added+=1
    return piv,added
def ball(R,L):
    d=l1(L); return [tuple(int(v) for v in s) for s in zip(*np.nonzero(d<=R))]
def wrap(s,L): return tuple(v%L for v in s)
def S1():
    cases=[(1,0,1),(2,1,2),(3,2,3),(1,2,3),(2,3,5),(3,3,6)]; ok=True; n_int=0; rk={}
    for K,Bc,R in cases:
        L=8*R+1; q=(4*R,0,0); rows=rowbuilder(L); bK=ball(K,L); bK1=ball(K-1,L)
        pA,pB=(K,0,0),(0,K,0)
        def ready(field,t):
            ex={'A':pA,'B':pB,'C':None}[field]
            return [(t,s) for s in bK if s!=ex]+[(t-1,s) for s in bK1]+[(t,q),(t-1,q)]
        cache={}
        def R_(field,t):
            if (field,t) not in cache: cache[(field,t)]=rows(ready(field,t))
            return cache[(field,t)]
        for w in range(Bc+1):
            outs={'A':[(w,pA)]+[(w+t,q) for t in range(1,K+1)],'B':[(w,pB)]+[(w+t,q) for t in range(1,K+1)],'C':[(w+t,q) for t in range(1,K+1)]}
            orow={f:rows(outs[f]) for f in 'ABC'}
            for mask in range(1<<w):
                ts=[w]+[i for i in range(w) if mask>>i&1]; rank=0; inc=0
                for f in 'ABC':
                    piv,r=add_rows({},[x for t in ts for x in R_(f,t)]); rank+=r
                    _,a=add_rows(piv,orow[f]); inc+=a
                ok&= inc==2+3*K; n_int+=1
                if (K,Bc,R)==(3,2,3): rk[tuple(sorted(ts))]=rank
            # receiver identities on E_w
            for f in 'ABC':
                piv,_=add_rows({},R_(f,w))
                rr=rows([(w+t,(0,0,0)) for t in range(K+1)])
                pay=rows([(w,pA if f=='A' else pB)])[0] if f!='C' else 0
                for t,v in enumerate(rr):
                    if t==K: v^=pay
                    ok&= reduce_(piv,v)==0
    print('S1  per-field ranks, six geometries, %d readiness intersections: payload and future source raise the rank by 2+3K in every one, receiver identities in the span of E_w: %s'%(n_int,ok))
    print('    K=3, L=25 intersection ranks: %s'%rk)
    ok&= n_int==48 and rk[(0,)]==268 and rk[(0,1)]==385 and rk[(0,2)]==442 and rk[(0,1,2)]==502
    return ok,rk

def raw_step(p,c):
    (Ap,Bp,Dp),(A,B,D)=p,c; sa,sb=S_(A),S_(B)
    return (sa^Ap,sb^Bp,S_(D)^Dp^S_(A&B)^(sa&sb)^(sa&Bp)^(sb&Ap))
def raw_back(c,n):
    (A,B,D),(An,Bn,Dn)=c,n; sa,sb=S_(A),S_(B); Ap=sa^An; Bp=sb^Bn
    return (Ap,Bp,Dn^S_(D)^S_(A&B)^(sa&sb)^(sa&Bp)^(sb&Ap))
def S2():
    K=3; L=25; q=(12,0,0); d=l1(L); inK=d<=K; inK1=d<=K-1
    exA=np.zeros((L,L,L),bool); exA[K,0,0]=True; exB=np.zeros((L,L,L),bool); exB[0,K,0]=True
    def is_ready(p,c):
        okv=np.ones(p[0].shape[0],bool)
        for f,ex in zip(range(3),(exA,exB,np.zeros_like(exA))):
            okv&=~(c[f][:,inK&~ex].any(1)); okv&=~(p[f][:,inK1].any(1))
            okv&=(c[f][:,q[0],q[1],q[2]]==0)&(p[f][:,q[0],q[1],q[2]]==0)
        return okv
    ok=True; stats={}
    for w in (0,1,2):
        pay=np.zeros(4,np.int64); src=np.zeros((K,8),np.int64); joint=np.zeros((4,8),np.int64); n_all=0; rejected=0
        for _ in range(12):
            n=256
            p=[rng.integers(0,2,(n,L,L,L),dtype=np.uint8) for _ in range(3)]; c=[rng.integers(0,2,(n,L,L,L),dtype=np.uint8) for _ in range(3)]
            for f,ex in zip(range(3),(exA,exB,np.zeros_like(exA))):
                c[f][:,inK&~ex]=0; p[f][:,inK1]=0; c[f][:,q[0],q[1],q[2]]=0; p[f][:,q[0],q[1],q[2]]=0
            P,C=tuple(p),tuple(c)
            ok&=bool(is_ready(P,C).all())
            # backwards: slices (t-1,t) for t = w-1, ..., 0 must fail readiness
            bp,bc=P,C; fail=np.ones(n,bool)
            for t in range(w-1,-1,-1):
                bp,bc=raw_back(bp,bc),bp
                fail&=~is_ready(bp,bc)
            # forward from the backward image reproduces the tick-w state (inverse control)
            fp,fc=bp,bc
            for t in range(w): fp,fc=fc,raw_step(fp,fc)
            ok&=all(np.array_equal(x,y) for x,y in zip(fc,C)) and all(np.array_equal(x,y) for x,y in zip(fp,P))
            rejected+=int((~fail).sum()); keep=fail
            a=C[0][:,K,0,0].astype(np.int64); b=C[1][:,0,K,0].astype(np.int64)
            rec=[]; srcw=[]
            for t in range(K):
                P,C=C,raw_step(P,C)
                rec.append([x[:,0,0,0] for x in C]); srcw.append(sum(C[f][:,q[0],q[1],q[2]].astype(np.int64)<<f for f in range(3)))
            for t in range(K):
                want=a*b if t==K-1 else 0*a
                ok&=bool(np.all(rec[t][0]==(a if t==K-1 else 0))) and bool(np.all(rec[t][1]==(b if t==K-1 else 0))) and bool(np.all(rec[t][2]==want))
            pid=a*2+b
            pay+=np.bincount(pid[keep],minlength=4)
            for t in range(K): src[t]+=np.bincount(srcw[t][keep],minlength=8)
            np.add.at(joint,(pid[keep],srcw[0][keep]),1)
            n_all+=int(keep.sum())
        def chi2(obs):
            e=obs.sum()/obs.size; return float(((obs-e)**2/e).sum())
        stats[w]=(n_all,rejected,chi2(pay),[round(chi2(s),1) for s in src],chi2(joint))
    print('S2  raw rule and its inverse, K=3, L=25, 3072 states per w: every sampled state satisfies the raw readiness predicate at tick w, the inverse round trip is exact, and the receiver reads (0,0,0),(0,0,0),(a,b,ab) in every run: %s'%ok)
    print('    (states ready at an earlier tick are rejected; none occur, as P(E_i | E_w) <= 2^-117)')
    for w,(n_all,rej,cp,cs,cj) in stats.items():
        print('    w=%d: kept %d, rejected %d; chi-square payload %.1f (3 dof), source triples per tick %s (7 dof), payload x first triple %.1f (31 dof)'%(w,n_all,rej,cp,cs,cj))
    return ok

def S3(rk):
    p=lambda *ts:F(1,2**rk[tuple(sorted(ts))])
    P1_=p(1)-p(0,1); P2_=p(2)-p(0,2)-p(1,2)+p(0,1,2)
    e1=1-P1_*2**268; e2=1-P2_*2**268
    ok=e1==F(1,2**117) and e2==F(1,2**117)+F(1,2**174)-F(1,2**234)
    print('S3  TV(law | W=w, law | E_w) = 1 - P(W=w)/2^-268: w=1 2^-117, w=2 2^-117 + 2^-174 - 2^-234 (exact): %s'%ok)
    return ok

def S4():
    ok=True; n_cases=0
    for n in (10,100,1000,3000):
        for _ in range(20):
            perm=rng.permutation(n); E=set(rng.choice(n,size=max(1,n//int(rng.integers(2,40))),replace=False).tolist())
            # first hit for every state (inf if never)
            wait=np.full(n,-1)
            for x in range(n):
                y=x; w=0; seen=0
                while y not in E and seen<=n: y=perm[y]; w+=1; seen+=1
                wait[x]=w if y in E else -1
            sat=[x for x in range(n) if wait[x]>=0]
            gaps=[]
            for x in E:
                y=perm[x]; l=1
                while y not in E: y=perm[y]; l+=1
                gaps.append(l)
            ok&= sum(gaps)==len(sat)
            ok&= F(int(sum(wait[x] for x in sat)),len(sat))==F(sum(l*(l-1)//2 for l in gaps),len(sat))
            for B in (0,1,5):
                ok&= int(((wait>=0)&(wait<=B)).sum())<=min(n,(B+1)*len(E))
            n_cases+=1
    print('S4  %d random permutations (n up to 3000): Kac return sum |Sat|, first-hit mean sum l(l-1)/(2|Sat|), deadline union bound: %s'%(n_cases,ok))
    return ok

if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    a,res=P1()
    mc=P2(res)
    xor=mc['XOR'][0]; e=xor.sum()/8; chi=float(((xor-e)**2/e).sum())
    v,(p0,p1)=mc['worst']; n=v.sum()
    # index = h1*4 + h2*2 + h3
    e0=(v[0]+v[2])/n; e1=(v[4]+v[6])/n
    z=[(e0-float(p0))/np.sqrt(float(p0)*(1-float(p0))/n),(e1-float(p1))/np.sqrt(float(p1)*(1-float(p1))/n)]
    print('P2  9^3 torus Monte Carlo, 200000 phases per rule: XOR (h1,h2,h3) chi-square %.1f (7 dof); most biased nonlinear rule: P(h1=0,h3=0) %.5f vs exact %.5f, P(h1=1,h3=0) %.5f vs exact %.5f (z = %.2f, %.2f)'%(chi,e0,float(p0),e1,float(p1),*z))
    b,rk=S1(); c=S2(); d=S3(rk); e_=S4()
    print('coordinator positive checks:','green' if all([a,b,c,d,e_]) else 'RED')
