"""Exact exploratory census. Standard library; stdout only; no randomness.

Checks deliberately use require(), so python -O does not disable them.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product, combinations

def require(x, message):
    if not x:
        raise RuntimeError(message)

D = ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))
def add(x,y):
    return tuple(a+b for a,b in zip(x,y))
def orbit(x):
    pairs = [((x>>(2*j))&1)+((x>>(2*j+1))&1) for j in range(3)]
    return tuple(pairs.count(k) for k in range(3))
ORB = sorted({orbit(x) for x in range(64)})
def table(code):
    return [(code>>ORB.index(orbit(x)))&1 for x in range(64)]
def degree(f):
    a = f[:]
    for j in range(6):
        for x in range(64):
            if x&(1<<j):
                a[x] ^= a[x^(1<<j)]
    return max((x.bit_count() for x in range(64) if a[x]), default=0)

def symmetry_check():
    # Explicit 48 signed coordinate permutations, independent of occupancy labels.
    group=[]
    for p in permutations(range(3)):
        for signs in product((-1,1), repeat=3):
            group.append([D.index(tuple(signs[j]*v[p[j]] for j in range(3))) for v in D])
    require(len({tuple(g) for g in group})==48, 'group size')
    for x in range(64):
        images={sum(((x>>j)&1)<<g[j] for j in range(6)) for g in group}
        require(images=={y for y in range(64) if orbit(y)==orbit(x)}, 'orbit completeness')
    print('Cubic group: 48 transformations; 10 complete orbits; 1024 invariant rules')

def three_tick(f):
    # Sum the 12 shared radius-two bits, analytically sum 6 private axial bits.
    shared=sorted({add(a,b) for a in D for b in D if sum(abs(v) for v in add(a,b))==2 and max(abs(v) for v in add(a,b))==1})
    require(len(shared)==12, 'shared site count')
    corr=[sum(f[a]==0 and f[a^g]==0 for a in range(64)) for g in range(64)]
    out=[]
    for h in (0,1):
        patterns=Counter()
        for b in range(1<<12):
            fixed=free=0
            for j,v in enumerate(D):
                masks=[]
                for axial in (0,1):
                    mask=0
                    for k,d in enumerate(D):
                        site=add(v,d)
                        if site==(0,0,0): val=h
                        elif site==add(v,v): val=axial
                        else: val=(b>>shared.index(site))&1
                        mask |= val<<k
                    masks.append(f[mask])
                if masks[0]!=masks[1]: free |= 1<<j
                elif masks[0]: fixed |= 1<<j
            patterns[fixed,free]+=1
        total=0
        for (fixed,free),multiplicity in patterns.items():
            gs=[g for g in range(64) if (g & (63^free))==fixed]
            total += multiplicity * (1<<(6-free.bit_count())) * sum(corr[g] for g in gs)
        out.append(F(total,1<<24))
    return out

EXPECTED={270:(F(8339,32768),F(8259,32768)),298:(F(1,4),F(1,4)),330:(F(8259,32768),F(8339,32768)),412:(F(1,4),F(131513,524288)),440:(F(32507,131072),F(135895,524288)),472:(F(29907,131072),F(146359,524288))}

def local_gate(f):
    # Return explicit two-input AND slice, allowing input/output bit complements.
    for i,j in combinations(range(6),2):
        for base in range(64):
            if base&((1<<i)|(1<<j)): continue
            vals=[f[base|(a<<i)|(b<<j)] for a,b in product((0,1),repeat=2)]
            for ci,cj,co in product((0,1),repeat=3):
                if vals==[((a^ci)&(b^cj))^co for a,b in product((0,1),repeat=2)]:
                    return i,j,base,ci,cj,co
    return None

def raw_recursion(f):
    # Deterministic varied full phases on L=7, not probability sampling.
    L=7
    sites=list(product(range(L),repeat=3)); lookup={x:i for i,x in enumerate(sites)}
    nei=[[lookup[tuple((x[k]+d[k])%L for k in range(3))] for d in D] for x in sites]
    def step(p,c):
        return [p[i]^f[sum(c[j]<<k for k,j in enumerate(ns))] for i,ns in enumerate(nei)]
    for seed in range(24):
        def bit(i):
            z=(i+1)*0x9e3779b1+(seed+1)*0x85ebca77
            z=(z^(z>>16))*0xc2b2ae3d
            return (z^(z>>13)).bit_count()&1
        p=[bit(i) for i in range(len(sites))]; c=[bit(i+len(sites)) for i in range(len(sites))]
        p[0]=c[0]=0
        u1=step(p,c); u2=step(c,u1); u3=step(u1,u2)
        a=sum(c[j]<<k for k,j in enumerate(nei[0]))
        g=0
        for k,j in enumerate(nei[0]):
            g|=f[sum(u1[l]<<q for q,l in enumerate(nei[j]))]<<k
        require(u1[0]==f[a] and u3[0]==(f[a^g]^f[a]), 'raw cone comparison')
    # Actual uniform background plus one flipped site, old background unchanged.
    pops=[]
    for background in (0,1):
        p=[background]*len(sites);c=p[:];c[0]^=1
        nxt=step(p,c)
        pops.append(sum(x!=background for x in nxt))
    return pops

def triangular_check():
    # Three-component second-order rule on a two-site test graph.
    # A'=neighbor(A) xor Aold; B' similarly;
    # D'=neighbor(D) xor (neighbor(A) & neighbor(B)) xor Dold.
    def force(c):
        a0,a1,b0,b1,d0,d1=c
        return (a1,a0,b1,b0,d1^(a1&b1),d0^(a0&b0))
    def xor(a,b): return tuple(x^y for x,y in zip(a,b))
    images=set()
    for bits in product((0,1),repeat=12):
        p,c=bits[:6],bits[6:];n=xor(force(c),p)
        require(xor(force(c),n)==p,'inverse')
        images.add(c+n)
    require(len(images)==4096,'triangular bijection')
    truth=[]
    for a,b in product((0,1),repeat=2):
        c=(0,a,0,1-b,0,0)
        truth.append(force(c)[4])
    require(truth==[0,0,1,0],'crossing slice')
    print('Triangular three-field escape: 4096/4096 bijection; crossing gate',truth)

def main():
    symmetry_check()
    candidates=[code for code in range(1024) if table(code)[0]==0 and table(code)[1]==1 and sum(table(code))==32]
    require(candidates==sorted(EXPECTED),'census')
    fresh=[];flip=[]
    print('code degree parity_distance P00 P10 three_tick_TV flip_covariant pulse/hole')
    for code in candidates:
        f=table(code);p=tuple(three_tick(f));require(p==EXPECTED[code],'three-tick counts')
        tv=sum(abs(x-F(1,4)) for x in p)
        cov=all(f[x]==f[x^63] for x in range(64))
        if not tv:fresh.append(code)
        if cov:flip.append(code)
        pulse=raw_recursion(f)
        gate=local_gate(f)
        require((gate is None)==(code==298),'nonlinear gate capability')
        print(code,degree(f),sum(f[x]!=(x.bit_count()%2) for x in range(64)),*map(str,p),str(tv),cov,pulse)
        if gate: print('  AND slice: i,j,other_bits,input_flips,output_flip =',gate)
    require(fresh==[298] and flip==[298],'restricted classification')
    triangular_check()
    print('PASS: exact three-tick freshness selects XOR within the stated scalar class only')

if __name__=='__main__': main()
