"""Nonlinear-feedback/frontier tests. Standard library, stdout only."""
from collections import Counter
from itertools import product
from random import Random

DIRS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
O=(0,0,0)

def require(ok,label):
    if not ok:raise RuntimeError(label)

def H(v):
    a,b,d=v
    return b,d,a^(b&d)

def Hinv(v):
    x,y,z=v
    return z^(x&y),x,y

def shift(field,L):
    out=set()
    for x in field:
        for d in DIRS:
            y=tuple((a+b)%L for a,b in zip(x,d))
            if y in out:out.remove(y)
            else:out.add(y)
    return out

def force(cur,L,bad=False):
    a,b,d=[shift(v,L) for v in cur]
    return [b,d,(b&d) if bad else a^(b&d)]

def step(old,cur,L,bad=False):
    return [p^f for p,f in zip(old,force(cur,L,bad))]

def inverse(cur,nxt,L):
    return [n^f for n,f in zip(nxt,force(cur,L))]

def read(cur,x):return tuple(int(x in f) for f in cur)

def ball(k):
    return [x for x in product(range(-k,k+1),repeat=3) if sum(map(abs,x))<=k]

def law_checks():
    table=list(product((0,1),repeat=3))
    require(len({H(x) for x in table})==8,'H bijective')
    require(all(Hinv(H(x))==x for x in table),'H inverse')
    rng=Random(1817);count=0
    for L in (3,4,5):
        sites=list(product(range(L),repeat=3))
        p=[{x for x in sites if rng.getrandbits(1)} for _ in range(3)]
        c=[{x for x in sites if rng.getrandbits(1)} for _ in range(3)]
        for _ in range(8):
            n=step(p,c,L)
            require(inverse(c,n,L)==p,'global inverse')
            p,c=c,n;count+=1
    print('Rule PASS: H permutes all eight triples; raw global inverse on',count,'dense transitions')

def source_checks():
    # Each cone background is fixed arbitrarily; enumerate only the 3K frontier bits.
    rng=Random(1818);cases=0
    for K in (1,2,3):
        L=2*K+3;q=O
        cone={tuple(v%L for v in x) for x in ball(K)}
        frontier={tuple(v%L for v in (t,0,0)) for t in range(1,K+1)}
        for background in (0,1):
            old=[set() for _ in range(3)];cur=[set() for _ in range(3)]
            if background:
                for x in cone:
                    if x==q:continue
                    for f in range(3):
                        if rng.getrandbits(1):old[f].add(x)
                        if x not in frontier and rng.getrandbits(1):cur[f].add(x)
            counts=Counter()
            for bits in product((0,1),repeat=3*K):
                p=[set(f) for f in old];c=[set(f) for f in cur]
                for t in range(1,K+1):
                    for f in range(3):
                        if bits[3*(t-1)+f]:c[f].add((t,0,0))
                word=[]
                for _ in range(K):
                    p,c=c,step(p,c,L);word.append(read(c,q))
                counts[tuple(word)]+=1
            require(len(counts)==8**K and set(counts.values())=={1},'nonlinear frontier bijection')
            if K==3:
                # First tick 1 or 2 with source A=1, recording the full past triples.
                stopped=Counter();prefix_totals=Counter()
                for word,mass in counts.items():
                    w=next((i+1 for i in range(2) if word[i][0]),None)
                    if w is None:continue
                    key=(w,word[:w])
                    stopped[key,word[w]]+=mass;prefix_totals[key]+=mass
                require(all(stopped[key,z]*8==mass for key,mass in prefix_totals.items()
                            for z in product((0,1),repeat=3)),'nonlinear stopping-history control')
            cases+=1
    # Non-bijective H still gives a reversible second-order global map, but loses freshness.
    counts=Counter()
    for bits in product((0,1),repeat=3):
        p=[set() for _ in range(3)];c=[{(1,0,0)} if b else set() for b in bits]
        n=step(p,c,5,bad=True)
        require([a^b for a,b in zip(n,force(c,5,bad=True))]==p,'bad-H global inverse')
        counts[read(n,O)]+=1
    require(len(counts)==4 and set(counts.values())=={2},'nonpermutive source countercontrol')
    print('Source PASS:',cases,'full frontier enumerations, K=1,2,3; every source word occurs once')
    print('Stopping control PASS: next triple uniform after first A=1 at tick 1 or 2, with full prefix visible')
    print('Countercontrol PASS: non-bijective H keeps global reversibility but source TV=1/2')

def joint_checks():
    K=2;L=17;q=(8,0,0)
    pa,pb,pc=(1,1,0),(1,L-1,0),(0,0,2)
    for complemented in (False,True):
        seen=Counter()
        for bits in product((0,1),repeat=9):
            inputs=bits[:3]
            a,b,c=[1-x if complemented else x for x in inputs]
            old=[set() for _ in range(3)];cur=[set(),{pa} if a else set(),set()]
            if b:cur[2].add(pb)
            if c:cur[2].add(pc)
            for t in range(1,3):
                for f in range(3):
                    if bits[3+3*(t-1)+f]:cur[f].add((q[0]+t,0,0))
            word=[];receivers=[]
            for _ in range(2):
                old,cur=cur,step(old,cur,L)
                word.append(read(cur,q));receivers.append(read(cur,O))
            require(receivers==[(0,0,0),(c,a*b,a*b*c)],'raw two-stage gate')
            require(receivers[-1][2]==(int(inputs==(0,0,0)) if complemented else a*b*c),
                    'three-input zero flag')
            seen[inputs,tuple(word),tuple(receivers)]+=1
        require(len(seen)==512 and set(seen.values())=={1},'full joint record')
    J=3*(len(ball(2))+len(ball(1)))-3+6
    require(J==99,'shared readiness cost')
    print('Joint PASS: 512 assignments each for AND3 and zero-detection; 64 source words per input')
    print('Receiver record: (0,0,0), (c,ab,abc); shared readiness exponent J=99')

def dense_joint_checks():
    L=17;q=(8,0,0);sites=list(product(range(L),repeat=3));rng=Random(1820)
    current_zero={tuple(v%L for v in x) for x in ball(2)}|{q}
    old_zero={tuple(v%L for v in x) for x in ball(1)}|{q}
    pa,pb,pc=(1,1,0),(1,L-1,0),(0,0,2)
    count=0
    for _ in range(2):
        old=[{x for x in sites if x not in old_zero and rng.getrandbits(1)} for f in range(3)]
        cur=[{x for x in sites if x not in current_zero and rng.getrandbits(1)} for f in range(3)]
        source_words=set()
        for a,b,c in product((0,1),repeat=3):
            p=[set(f) for f in old];v=[set(f) for f in cur]
            if a:v[1].add(pa)
            if b:v[2].add(pb)
            if c:v[2].add(pc)
            word=[];record=[]
            for t in range(2):
                p,v=v,step(p,v,L);record.append(read(v,O));word.append(read(v,q))
            require(record==[(0,0,0),(c,a*b,a*b*c)],'joint full dense background')
            source_words.add(tuple(word));count+=1
        require(len(source_words)==1,'source independent of receiver input intervention')
    print('Dense joint PASS:',count,'full 17^3 initial backgrounds/input runs')

def degree(truth,n):
    co=[(truth>>i)&1 for i in range(1<<n)]
    for j in range(n):
        for i in range(1<<n):
            if i>>j&1:co[i]^=co[i^(1<<j)]
    return max((i.bit_count() for i,v in enumerate(co) if v),default=0)

def degree_probe():
    # Bit-packed truth tables: no conjugacy or degree assumption in the dynamics.
    L=5;n=6;N=L**3;mask=(1<<(1<<n))-1;rng=Random(1819)
    sites=list(product(range(L),repeat=3));index={x:i for i,x in enumerate(sites)}
    neighbors=[[index[tuple((a+b)%L for a,b in zip(x,d))] for d in DIRS] for x in sites]
    old=[[mask if rng.getrandbits(1) else 0 for _ in sites] for f in range(3)]
    cur=[[mask if rng.getrandbits(1) else 0 for _ in sites] for f in range(3)]
    chosen=rng.sample(range(6*N),n)
    for j,k in enumerate(chosen):
        phase,k=divmod(k,3*N);f,i=divmod(k,N)
        (old if phase==0 else cur)[f][i]=sum(((a>>j)&1)<<a for a in range(1<<n))
    maxima=[]
    for t in range(1,9):
        sums=[[0]*N for _ in range(3)]
        for f in range(3):
            for i,ns in enumerate(neighbors):
                for j in ns:sums[f][i]^=cur[f][j]
        sa,sb,sd=sums
        nxt=[[old[0][i]^sb[i] for i in range(N)],
             [old[1][i]^sd[i] for i in range(N)],
             [old[2][i]^sa[i]^(sb[i]&sd[i]) for i in range(N)]]
        old,cur=cur,nxt
        maxima.append(max(degree(v,n) for f in cur for v in f))
    require(max(maxima)>2,'degree escapes previous ceiling')
    print('Degree probe PASS: exact six-input max degrees at ticks 1..8:',maxima)
    print('Scope: finite degree evidence, not a proof of unbounded degree or universal computation')

def main():
    law_checks();source_checks();joint_checks();dense_joint_checks();degree_probe()
    print('PASS: nonlinear feedback, bounded exact freshness and raw AND3 coexist conditionally')

if __name__=='__main__':main()
