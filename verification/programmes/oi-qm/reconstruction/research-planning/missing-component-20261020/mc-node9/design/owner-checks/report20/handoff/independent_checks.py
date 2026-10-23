"""Independent checks of composition checkpoint 43400ea7.

Reads the reviewed builder as the candidate under test. Does not import its
simulation, truth-table, group composition, or degree implementations.
Standard library only after importing builder (also standard library).
Writes stdout only; all checks remain active with -O.
"""
import sys
from pathlib import Path
from itertools import product, permutations
from math import comb
from random import Random

sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parent/'source'))
import builder


def check(ok,msg):
    if not ok: raise RuntimeError(msg)


def perm_step(p,v):
    ans=[]
    for s in p:
        a,b,d=((s^v)>>2)&1,((s^v)>>1)&1,(s^v)&1
        ans.append(4*b+2*d+(a^(b&d)))
    return bytes(ans)


def group_checks():
    identity=bytes(range(8))
    seen={identity}; todo=[identity]
    for p in todo:
        for v in range(8):
            q=perm_step(p,v)
            if q not in seen: seen.add(q); todo.append(q)
    check(len(seen)==40320,'independent group closure')
    compose=lambda p,q: bytes(p[q[i]] for i in range(8))
    inverse=lambda p: bytes(p.index(i) for i in range(8))
    for rho in builder.CYC:
        check(bool(builder.PAIRS[rho]),'commutator existence')
        for a,b in builder.PAIRS[rho]:
            comm=compose(compose(a,b),compose(inverse(a),inverse(b)))
            check(tuple(comm)==rho,'independent commutator check')
        m=builder.block_len(rho)
        check(m in (6,8),'leaf length')
        for target in (tuple(range(8)),rho):
            p=identity
            for v in builder.word(target,m): p=perm_step(p,v)
            check(tuple(p)==target,'independent word evaluation')
    for length in (6,8,10):
        p=identity
        for v in builder.word(tuple(range(8)),length): p=perm_step(p,v)
        check(p==identity,'padding identity')
    print('I1 group closure 40320; all 24 leaf cycles and their commutators; identity padding 6/8/10: PASS')


def variables(n):
    full=(1<<(1<<n))-1
    vs=[sum(1<<a for a in range(1<<n) if a>>j&1) for j in range(n)]
    return vs,full


def affine(value,vs,full):
    const,indices=value
    z=full if const else 0
    for j in indices: z^=vs[j]
    return z


def inward(n,T,sources):
    vs,full=variables(n)
    layer={}
    for pos,f,val in sources:
        check(sum(abs(x) for x in pos)==T,'shell source')
        layer.setdefault(pos,[0,0,0])[f]^=affine(val,vs,full)
    for depth in range(T):
        parents={}
        for pos,u in layer.items():
            for axis,x in enumerate(pos):
                if not x: continue
                y=list(pos); y[axis]-=1 if x>0 else -1; y=tuple(y)
                acc=parents.setdefault(y,[0,0,0])
                for f in range(3): acc[f]^=u[f]
        layer={p:(b,d,a^(b&d)) for p,(a,b,d) in parents.items()
               if a or b or d}
    return layer.get((0,0,0),(0,0,0))


def degree(table,n):
    # Scalar finite-difference transform; independent of numpy unpacking.
    coeff=[(table>>i)&1 for i in range(1<<n)]
    for j in range(n):
        for mask in range(1<<n):
            if mask>>j&1: coeff[mask]^=coeff[mask^(1<<j)]
    return max((i.bit_count() for i,c in enumerate(coeff) if c),default=-1)


def gf_rank(rows):
    basis={}
    for row in rows:
        while row:
            k=row.bit_length()-1
            if k in basis: row^=basis[k]
            else: basis[k]=row; break
    return len(basis)


def scalar_h(z):
    return (z[1],z[2],z[0]^(z[1]&z[2]))


def independent_torus():
    # Unpacked scalar triples, full 3D torus, no use of source engine.
    n=2; T,src=builder.realize(n); L=2*T+3
    sites=list(product(range(L),repeat=3)); lookup={x:i for i,x in enumerate(sites)}
    index=lambda x:lookup[tuple(v%L for v in x)]
    dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    adjacent=[[index(tuple(a+b for a,b in zip(x,e))) for e in dirs] for x in sites]
    rng=Random(88543400)
    for trial in range(2):
        bg1=[tuple(rng.randrange(2) for _ in range(3)) for x in sites]
        bg0=[tuple(rng.randrange(2) for _ in range(3)) for x in sites]
        for inp in range(4):
            old=bg1.copy(); now=bg0.copy()
            for i,x in enumerate(sites):
                r=sum(min(a,L-a) for a in x)
                if r<=T: now[i]=(0,0,0)
                if r<=T-1: old[i]=(0,0,0)
            for pos,f,(c,inds) in src:
                v=c
                for j in inds: v^=(inp>>j)&1
                z=list(now[index(pos)]); z[f]^=v; now[index(pos)]=tuple(z)
            for t in range(T):
                nxt=[]
                for i,ns in enumerate(adjacent):
                    acc=[0,0,0]
                    for k in ns:
                        for f in range(3): acc[f]^=now[k][f]
                    z=scalar_h(acc)
                    nxt.append(tuple(z[f]^old[i][f] for f in range(3)))
                old,now=now,nxt
                if t<T-1: check(now[0]==(0,0,0),'silent receiver prefix')
            check(now[0]==((inp&1),(inp>>1),int(inp==3)),'dense scalar torus')
    print('I2 separate scalar full-torus update: n=2, all inputs, two dense backgrounds and silent prefix: PASS')


def check_sources():
    sizes=(2,3,4,5,6,7,8,9,10,11,12,13)
    for n in sizes:
        T,src=builder.realize(n)
        vs,full=variables(n)
        k=(n+1)//2
        f1=f2=full
        for x in vs[:k]: f1&=x
        for x in vs[k:]: f2&=x
        expected=(f1,f2,f1&f2)
        got=inward(n,T,src)
        check(got==expected,'whole terminal triple n='+str(n))
        check(degree(got[2],n)==n,'degree n='+str(n))
        check(gf_rank([sum(1<<j for j in s) for p,f,(c,s) in src])==n,'source rank')
        altered=src+[((T,0,0),2,(1,frozenset()))]
        check(inward(n,T,altered)[2]!=got[2],'released chain pin countercontrol')
        print('I3 n=%d T=%d sources=%d rank=%d degree=%d full terminal triple and countercontrol PASS'
              %(n,T,len(src),n,n),flush=True)


def boundary_checks():
    # Check arbitrary 3D shell data, not just the builder's planar wings.
    rng=Random(12345)
    dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    for T in range(1,7):
        for trial in range(4):
            # Full raw second-order recursion on its exact backward cone.
            initial={x:tuple(rng.randrange(2) for _ in range(3))
                     for x in product(range(-T,T+1),repeat=3)
                     if sum(map(abs,x))==T}
            from functools import lru_cache
            @lru_cache(None)
            def raw(t,x):
                if t==-1: return (0,0,0)
                if t==0: return initial.get(x,(0,0,0))
                acc=[0,0,0]
                for e in dirs:
                    y=tuple(a+b for a,b in zip(x,e))
                    v=raw(t-1,y)
                    for f in range(3): acc[f]^=v[f]
                z=scalar_h(acc); prior=raw(t-2,x)
                return tuple(a^b for a,b in zip(z,prior))
            src=[(x,f,(z[f],frozenset())) for x,z in initial.items() for f in range(3) if z[f]]
            out=inward(1,T,src)
            check(tuple(v&1 for v in out)==raw(T,(0,0,0)),'raw backward-cone recursion')
    print('I4 first-light reduction: 24 arbitrary 3D shell cases against raw second-order recursion: PASS')


def accounting():
    # Pure arithmetic only; do not allocate these arrays.
    for n,T in [(9,169),(12,241)]:
        count=3*(2*T+3)**3*(2**n//64)*8
        print('I5 n=%d all-input packed array bytes=%d'%(n,count))
    # Any even difference >=6 has a 6/8/10 identity decomposition.
    for d in range(6,1002,2):
        steps=[]
        padded=builder.pad_identity(steps,d)
        check(len(padded)==d,'padding termination')
    print('I5 padding finite check through 1000: PASS; general proof in REVIEW.md')
    from functools import lru_cache
    @lru_cache(None)
    def weight(k):
        return 1 if k==1 else 2*weight((k+1)//2)+2*weight(k//2)
    for k in range(1,129):
        h=k.bit_length()-1
        check(weight(k)==2**h*(3*k-2**(h+1)),'closed weight formula')
    for n in range(2,33):
        p,q=builder.chains(n); T=len(p)+1; k=(n+1)//2
        check(len(p)==len(q),'equal chain length')
        check(6*weight(k)+1<=T<=8*weight(k)+7,'all-size latency bounds')
        v=lambda r:(4*r**3+6*r*r+8*r+3)//3
        check(3*(v(T)+v(T-1))-n==8*T**3+16*T-n,'codimension formula')
    print('I6 recursion weight through 128; latency and cone formulas n=2..32: PASS')


if __name__=='__main__':
    group_checks()
    independent_torus()
    boundary_checks()
    check_sources()
    accounting()
    print('ALL INDEPENDENT CHECKS PASS')
