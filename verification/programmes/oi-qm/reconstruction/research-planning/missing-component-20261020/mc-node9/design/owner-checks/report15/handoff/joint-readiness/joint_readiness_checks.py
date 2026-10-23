"""Exact source/readiness/detector diagnostics; standard library, stdout only."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from fractions import Fraction as F

DIRS=((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))
O=(0,0,0)
E=(1,0,0)
def require(x,why):
    if not x: raise RuntimeError(why)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def xor(*sets):
    out=set()
    for x in sets: out.symmetric_difference_update(x)
    return frozenset(out)
def mul(a,b):
    # Boolean ANF: square-free monomials, duplicate products cancel.
    out=set()
    for x in a:
        for y in b:
            z=frozenset(x|y)
            if z in out: out.remove(z)
            else: out.add(z)
    return frozenset(out)
def ready_zero(field,time,site):
    if field in ('A','B'):
        return site==O or (time==0 and site in DIRS and site!=E)
    return site==O or (time==0 and site in DIRS)
def variable(field,time,site): return (field,time,*site)

@lru_cache(None)
def poly(field,t,site,blank=False):
    if t in (-1,0):
        if ready_zero(field,t,site) or (blank and field=='D'): return frozenset()
        return frozenset((frozenset((variable(field,t,site),)),))
    ns=[add(site,d) for d in DIRS]
    terms=[poly(field,t-2,site,blank)]+[poly(field,t-1,n,blank) for n in ns]
    if field=='D': terms += [mul(poly('A',t-1,n,blank),poly('B',t-1,n,blank)) for n in ns]
    return xor(*terms)
def support(p): return set().union(*p) if p else set()

def symbolic_checks():
    p1=mul(poly('A',1,O),poly('B',1,O))
    require(poly('D',1,O)==p1,'first shared-preparation gate')
    print('Shared readiness: 22 fixed initial bits; probability 1/4194304; D(1)=A(1)B(1)')
    for t in range(1,7):
        a=variable('A',0,(t,0,0)); b=variable('B',0,(t,0,0))
        for field,v in [('A',a),('B',b)]:
            p=poly(field,t,O)
            require(frozenset((v,)) in p,'source frontier coefficient')
            require(all(len(m)==1 for m in p),'source linearity')
        for s in range(t):
            for field in ('A','B','D'):
                require(not ({a,b}&support(poly(field,s,O))),'past record sees future frontier')
        for blank in (False,True):
            p=poly('D',t,O,blank)
            require(all(len(m)<=2 for m in p),'detector degree')
            c=int(frozenset((a,b)) in p)
            require(c==t%2,'detector frontier coefficient')
        print('tick',t,'source frontier: 1,1; past exclusion: PASS; detector pair coefficient:',t%2)
    # Exhaust all affine functions of two independent bits.
    errors=[]
    for c,a,b in product((0,1),repeat=3):
        errors.append(sum((c^(a*x)^(b*y))!=(x*y) for x,y in product((0,1),repeat=2)))
    require(set(errors)=={1,3},'affine-vs-AND exact bound')
    print('Even-tick raw AND error: at least 1/4, for each fixed remainder of the initial state')

def shift(s,L):
    out=set()
    for x in s:
        for d in DIRS:
            y=tuple((a+b)%L for a,b in zip(x,d))
            if y in out: out.remove(y)
            else: out.add(y)
    return out
def simulate(initial,steps,L=19):
    # Independent actual torus evolution, no symbolic polynomial evaluation.
    p={f:{tuple(v%L for v in x) for x in initial.get((f,-1),set())} for f in ('A','B','D')}
    c={f:{tuple(v%L for v in x) for x in initial.get((f,0),set())} for f in ('A','B','D')}
    record=[tuple(int(O in c[f]) for f in ('A','B','D'))]
    for _ in range(steps):
        n={f:shift(c[f],L)^p[f] for f in ('A','B','D')}
        n['D'] ^= shift(c['A']&c['B'],L)
        p,c=c,n
        record.append(tuple(int(O in c[f]) for f in ('A','B','D')))
    return record

def joint_enumeration():
    # Exact ten-variable conditional slice; every unlisted initial bit is zero.
    free=[(f,0,(j,0,0)) for f in ('A','B') for j in (1,2,3)]
    free += [(f,0,(0,2,0)) for f in ('A','B')]
    free += [('D',0,(2,0,0)),('D',-1,E)]
    hist=[defaultdict(Counter) for _ in range(4)]
    current=Counter()
    for bits in product((0,1),repeat=len(free)):
        initial=defaultdict(set)
        for bit,(f,t,x) in zip(bits,free):
            if bit: initial[f,t].add(x)
        rec=simulate(initial,3,L=9)
        current[rec[1]]+=1
        for t in range(1,4): hist[t][tuple(rec[:t])][rec[t][:2]]+=1
        # Check a separate direct evaluation against the symbolic polynomials.
        ones={variable(f,t,x) for bit,(f,t,x) in zip(bits,free) if bit}
        for t in range(1,4):
            for k,f in enumerate(('A','B','D')):
                got=sum(m<=ones for m in poly(f,t,O))%2
                require(got==rec[t][k],'ANF vs native torus recursion')
    for t in range(1,4):
        for row in hist[t].values():
            require(set(row)==set(product((0,1),repeat=2)) and len(set(row.values()))==1,'history-conditioned uniformity')
        print('Native torus slice: tick',t,'all',len(hist[t]),'past-record classes have uniform next source pair')
    require(current==Counter({(0,0,0):256,(0,1,0):256,(1,0,0):256,(1,1,1):256}),'same-tick detector conditioning')
    print('Same-tick selection countercontrol: D(1)=1 forces source pair 11; TV from uniform=3/4')

def witnesses():
    for t in (2,4,6,8):
        outputs=[]
        for a,b in product((0,1),repeat=2):
            initial={('A',0):{(t,0,0)} if a else set(),('B',0):{(t,0,0)} if b else set()}
            r=simulate(initial,t,L=2*t+3)[t]
            outputs.append(r)
        require(outputs==[(0,0,0),(0,1,0),(1,0,0),(1,1,0)],'even blank-detector witness')
        print('Completely blank detector, tick',t,': raw AND error exactly 1/4 on the frontier slice')
    r=simulate({('A',0):{(-3,0,0)},('B',0):{(0,-3,0)}},3,L=9)
    require(r==[(0,0,0),(0,0,0),(0,0,0),(1,1,0)],'odd two-direction witness')
    print('Odd-tick countercontrol: distinct distance-three pulses give (A,B,D)=(1,1,0) at tick 3')
    # Neighbor access makes the next source pair deterministic from the update.
    counts=defaultdict(Counter)
    for a,b in product(range(64),repeat=2):
        counts[a,b][(a.bit_count()%2,b.bit_count()%2)]+=1
    require(all(len(row)==1 for row in counts.values()),'neighbor access control')
    print('Neighbor access countercontrol: next source pair deterministic; TV from uniform=3/4')

def unscreened_control():
    joint=Counter()
    for a,b in product(range(64),repeat=2):
        joint[a.bit_count()%2,b.bit_count()%2,(a&b).bit_count()%2]+=1
    expected={(0,0,0):544,(0,0,1):480}
    expected.update({(a,b,z):512 for a,b in ((0,1),(1,0),(1,1)) for z in (0,1)})
    require(joint==Counter(expected),'unscreened six-neighbor law')
    succ=sum(v for (a,b,d),v in joint.items() if d)
    marginal=F(sum(v for (a,b,d),v in joint.items() if d and a),succ)
    require(F(succ,4096)==F(63,128) and marginal==F(32,63),'herald selection bias')
    print('Without the ten source-neighbor zero constraints: P(D=1)=63/128; P(A=1|D=1)=32/63')

def rank(rows):
    pivots={}
    for x in rows:
        while x:
            j=x.bit_length()-1
            if j in pivots: x ^= pivots[j]
            else:
                pivots[j]=x
                break
    return len(pivots)

def second_tick_law():
    # Independent coefficient rank from the actual symbolic update.
    err=xor(poly('D',2,O,True),mul(poly('A',2,O,True),poly('B',2,O,True)))
    av=sorted(v for v in support(err) if v[0]=='A')
    bv=sorted(v for v in support(err) if v[0]=='B')
    rows=[0 for _ in av]
    for m in err:
        require(len(m)==2,'bilinear second-tick error')
        a=next(v for v in m if v[0]=='A'); b=next(v for v in m if v[0]=='B')
        rows[av.index(a)] ^= 1<<bv.index(b)
    r=rank(rows)
    require(r==12,'second-tick error rank')
    require((1-F(1,2**r))/2==F(4095,8192),'rank probability')
    # Separate probability calculation after invertible source coordinates:
    # H2=parity(R), M2=parity(Q), D2=U.V XOR R.Q, with U,V,R,Q iid 6-bit.
    noise=Counter((u&v).bit_count()%2 for u,v in product(range(64),repeat=2))
    law=Counter()
    for u,v in product(range(64),repeat=2):
        a,b=u.bit_count()%2,v.bit_count()%2
        z=(u&v).bit_count()%2
        for n,c in noise.items(): law[a,b,z^n]+=c
    exact={k:F(v,1<<24) for k,v in law.items()}
    expected={(0,0,0):F(1025,8192),(0,0,1):F(1023,8192)}
    expected.update({(a,b,z):F(1,8) for a,b in ((0,1),(1,0),(1,1)) for z in (0,1)})
    require(exact==expected,'complete second-tick law')
    error=sum(v for (a,b,z),v in exact.items() if z!=(a*b))
    require(error==F(4095,8192),'enumerated error probability')
    # With only local readiness, a free detector frontier gives an independent mask.
    dv=variable('D',0,(2,0,0))
    require(frozenset((dv,)) in poly('D',2,O),'free detector frontier')
    require(dv not in support(poly('D',1,O)),'mask not in first detector record')
    print('Tick 2, completely blank detector: error rank 12; raw AND error 4095/8192')
    print('Tick 2, local readiness only: independent detector mask; raw AND error 1/2')

def repaired_gate():
    # Full six-neighbor polynomial identity: no single-neighbor simplification.
    def atom(i): return frozenset((frozenset((i,)),))
    aa=[atom(i) for i in range(6)];bb=[atom(i+6) for i in range(6)]
    dd=[atom(i+12) for i in range(6)];ap,bp,dp=map(atom,(18,19,20))
    sa=xor(*aa);sb=xor(*bb);sd=xor(*dd);sab=xor(*(mul(a,b) for a,b in zip(aa,bb)))
    expanded=xor(sd,dp,sab,mul(sa,sb),mul(sa,bp),mul(sb,ap))
    conjugate=xor(sd,sab,dp,mul(ap,bp),mul(xor(sa,ap),xor(sb,bp)))
    require(expanded==conjugate,'full cubic local identity')
    # Independent complete two-site phase enumeration of the conjugated map.
    # Site order: A0,A1,B0,B1,D0,D1; S swaps the two sites.
    def xor_tuple(a,b): return tuple(x^y for x,y in zip(a,b))
    def g(v):
        a,b,c,d,e,f=v
        return (a,b,c,d,e^(a*c),f^(b*d))
    def linear(v):
        return (v[1],v[0],v[3],v[2],v[5],v[4])
    def step(p,c):
        sa=(c[1],c[0]);sb=(c[3],c[2]);sd=(c[5],c[4])
        an=tuple(sa[i]^p[i] for i in range(2))
        bn=tuple(sb[i]^p[i+2] for i in range(2))
        dn=tuple(sd[i]^p[i+4]^(c[1-i]*c[3-i])^(sa[i]*sb[i])^(sa[i]*p[i+2])^(sb[i]*p[i]) for i in range(2))
        return an+bn+dn
    images=set();clean=0
    for v in product((0,1),repeat=12):
        p,c=v[:6],v[6:];n=step(p,c)
        require(n==g(xor_tuple(linear(g(c)),g(p))),'expanded rule vs conjugation')
        restored=g(xor_tuple(g(n),linear(g(c))))
        require(restored==p,'conjugate inverse')
        images.add(c+n)
        if all(g(x)[4:]==(0,0) for x in (p,c)):
            clean+=1
            for _ in range(8):
                p,c=c,step(p,c)
                require(c[4:]==(c[0]*c[2],c[1]*c[3]),'repeated raw product gate')
    require(len(images)==4096 and clean==256,'complete repaired-map census')
    # Explicit dirty-C countercontrol, with zero sources throughout.
    p=(0,)*6;c=(0,0,0,0,1,0)
    require(step(p,c)[4:]==(0,1),'dirty clean-field control')
    print('Repaired local rule: 4096/4096 phases invert; all 256 clean phases track D=AB for 8 ticks')
    print('Repaired-rule countercontrol: a nonzero C=D XOR AB wave causes a raw-product error')
    # Actual cubic updates, including nonzero C, against an independent linear C wave.
    L=7;sites=list(product(range(L),repeat=3))
    for seed in range(16):
        def bits(offset):
            return {x for i,x in enumerate(sites) if (((i+1)*1103515245+(seed+offset+1)*12345)^((i+seed+offset)<<7)).bit_count()%2}
        pa,pb,pc=bits(0),bits(1),bits(2)
        ca,cb,cc=bits(3),bits(4),bits(5)
        if seed%2==0: pc=cc=set()
        pd=pc^(pa&pb);cd=cc^(ca&cb)
        for _ in range(8):
            sa,sb,sd=shift(ca,L),shift(cb,L),shift(cd,L)
            na,nb,nc=sa^pa,sb^pb,shift(cc,L)^pc
            nd=sd^pd^shift(ca&cb,L)^(sa&sb)^(sa&pb)^(sb&pa)
            require(nd==(nc^(na&nb)),'native cubic repaired rule')
            pa,pb,pc,pd=ca,cb,cc,cd
            ca,cb,cc,cd=na,nb,nc,nd
    print('Full cubic repair: 21-variable symbolic identity and 16 phases x 8 native ticks agree')
    # All 16 Boolean functions admit the same construction; no AND selection theorem.
    for code in range(16):
        def gg(a,b): return (code>>((a<<1)|b))&1
        def transform(v): return v[:4]+tuple(v[i+4]^gg(v[i],v[i+2]) for i in range(2))
        for src in product((0,1),repeat=8):
            p=src[:4]+tuple(gg(src[i],src[i+2]) for i in range(2))
            c=src[4:]+tuple(gg(src[i+4],src[i+6]) for i in range(2))
            for _ in range(4):
                n=transform(xor_tuple(linear(transform(c)),transform(p)))
                require(n[4:]==tuple(gg(n[i],n[i+2]) for i in range(2)),'arbitrary Boolean predicate')
                p,c=c,n
    print('Selection countercontrol: all 16 two-input Boolean functions track exactly under their conjugated rules')

def main():
    symbolic_checks();joint_enumeration();witnesses();unscreened_control();second_tick_law();repaired_gate()
    print('PASS: original repeated gate fails; conjugated local repair works with its different readiness')
if __name__=='__main__': main()
