"""Finite aggregation components. Standard library, reads included record tables, stdout only."""
from itertools import product
from pathlib import Path
from random import Random
import json

DIRS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
FIELDS=('A','B','D')
P3=[(0,1,(1,1,0),0),(0,2,(1,-1,0),1),(0,2,(0,0,2),2)]
P4=P3+[(0,0,(0,0,4),3),(-1,1,(0,0,3),2)]
P5=P4+[(0,1,(4,-1,1),4),(-1,1,(0,2,1),2)]
P6=P5+[(0,2,(-6,-1,1),5),(-1,0,(-1,-5,1),4)]
DESIGNS=[(4,3,(0,0,1),P4),(5,4,(0,-1,1),P5),(6,5,(-1,-1,1),P6)]

def require(ok,label):
    if not ok:raise RuntimeError(label)

def ball(r):
    return [x for x in product(range(-r,r+1),repeat=3) if sum(map(abs,x))<=r]

def vol(r):return (4*r**3+6*r*r+8*r+3)//3

def normalized(design):
    n,T,p,program=design
    return [(s,f,tuple(a-b for a,b in zip(x,p)),j) for s,f,x,j in program]

def poly_xor(a,b):return a^b

def poly_mul(a,b):
    out=set()
    for x in a:
        for y in b:
            z=x|y
            if z in out:out.remove(z)
            else:out.add(z)
    return out

def pxor_into(mapping,key,terms):
    if not terms:return
    mapping[key]=mapping.get(key,set())^terms
    if not mapping[key]:del mapping[key]

def polynomial_run(design,extra=None):
    """Independent sparse algebraic-normal-form evolution on the infinite lattice."""
    n,T,p,program=design
    rows=normalized(design)+([extra] if extra else [])
    old={};cur={}
    for phase,f,x,j in rows:pxor_into(old if phase==-1 else cur,(x,f),{0 if j==-1 else 1<<j})
    snapshots=[old,cur]
    for t in range(1,T+1):
        sums={}
        for (x,f),terms in cur.items():
            for d in DIRS:pxor_into(sums,(tuple(a+b for a,b in zip(x,d)),f),terms)
        nxt={k:set(v) for k,v in old.items()}
        for (x,f),terms in sums.items():pxor_into(nxt,(x,(f-1)%3),terms)
        points={x for x,f in sums if f==1}
        for x in points:pxor_into(nxt,(x,2),poly_mul(sums.get((x,1),set()),sums.get((x,2),set())))
        old,cur=cur,nxt;snapshots.append(cur)
    return snapshots

def serialize(snapshots):
    return [[[list(x),f,sorted(terms)] for (x,f),terms in sorted(s.items())] for s in snapshots]

def truth_variables(n):
    width=1<<n;mask=(1<<width)-1
    return mask,[((mask//((1<<(1<<j))+1))<<(1<<j)) for j in range(n)]

def poly_truth(terms,n):
    mask,variables=truth_variables(n);out=0
    for monomial in terms:
        v=mask
        for j in range(n):
            if monomial>>j&1:v &= variables[j]
        out ^= v
    return out

def degree_of_truth(truth,n):
    coeff=[(truth>>a)&1 for a in range(1<<n)]
    for j in range(n):
        for a in range(1<<n):
            if a>>j&1:coeff[a]^=coeff[a^(1<<j)]
    return max((a.bit_count() for a,v in enumerate(coeff) if v),default=0)

def geometry(L):
    sites=list(product(range(L),repeat=3))
    def index(x):
        a,b,c=(v%L for v in x)
        return (a*L+b)*L+c
    neighbors=[[index(tuple(a+b for a,b in zip(x,d))) for d in DIRS] for x in sites]
    return sites,index,neighbors

def raw_step(old,cur,neighbors):
    N=len(neighbors);nxt=[[0]*N for _ in range(3)]
    for i,ns in enumerate(neighbors):
        a=b=d=0
        for j in ns:a^=cur[0][j];b^=cur[1][j];d^=cur[2][j]
        nxt[0][i]=old[0][i]^b
        nxt[1][i]=old[1][i]^d
        nxt[2][i]=old[2][i]^a^(b&d)
    return nxt

def full_torus_check(design,snapshots,seed):
    n,T,p,program=design;L=6*T+3;q=(3*T+1,)*3
    sites,index,neighbors=geometry(L);N=len(sites)
    mask,variables=truth_variables(n);rng=Random(seed)
    previous_ready={index(x) for x in ball(3*T-1)}|{index(q)}
    current_ready={index(x) for x in ball(3*T)}|{index(q)}
    # Identical dense arbitrary complement across the full 2^n input cube.
    old=[[0 if i in previous_ready else mask*rng.getrandbits(1) for i in range(N)] for f in range(3)]
    cur=[[0 if i in current_ready else mask*rng.getrandbits(1) for i in range(N)] for f in range(3)]
    for phase,f,x,j in normalized(design):(old if phase==-1 else cur)[f][index(x)]^=variables[j]
    initial_old,initial_cur=old,cur
    device=ball(2*T);source=[]
    def check_record(fields,snapshot):
        for x in device:
            for f in range(3):
                require(fields[f][index(x)]==poly_truth(snapshot.get((x,f),set()),n),'complete device record')
    check_record(old,snapshots[0]);check_record(cur,snapshots[1])
    for t in range(1,T+1):
        old,cur=cur,raw_step(old,cur,neighbors)
        check_record(cur,snapshots[t+1])
        source.append(tuple(cur[f][index(q)] for f in range(3)))
        require(all(v in (0,mask) for v in source[-1]),'source independent of every input')
    require(cur[2][index((0,0,0))]==1<<((1<<n)-1),'raw ANDn on full torus')
    require(degree_of_truth(cur[2][index((0,0,0))],n)==n,'direct raw algebraic degree')
    return initial_old,initial_cur,index,q

def frontier_check(design,initial):
    """All 8^T frontier assignments; exact causal evaluation of a dense full-torus state."""
    n,T,p,program=design;L=6*T+3
    bg_old,bg_cur,index,q=initial
    allbits,variables=truth_variables(3*T)
    old={x:tuple(allbits if bg_old[f][index(tuple(a+b for a,b in zip(q,x)))] else 0 for f in range(3)) for x in ball(T-1)}
    cur={x:tuple(allbits if bg_cur[f][index(tuple(a+b for a,b in zip(q,x)))] else 0 for f in range(3)) for x in ball(T)}
    for t in range(1,T+1):cur[t,0,0]=tuple(variables[3*(t-1)+f] for f in range(3))
    outputs=[]
    for t in range(1,T+1):
        nxt={}
        for x in ball(T-t):
            a=b=d=0
            for delta in DIRS:
                triple=cur[tuple(v+w for v,w in zip(x,delta))]
                a^=triple[0];b^=triple[1];d^=triple[2]
            prev=old[x];nxt[x]=(prev[0]^b,prev[1]^d,prev[2]^a^(b&d))
        old,cur=cur,nxt;outputs.extend(cur[0,0,0])
    size=1<<(3*T);codes=[0]*size
    for bit,plane in enumerate(outputs):
        data=plane.to_bytes((size+7)//8,'little')
        for a in range(size):codes[a]|=((data[a//8]>>(a%8))&1)<<bit
    require(len(set(codes))==size,'all source words exactly once')
    return size

def check_design(design,saved):
    n,T,p,program=design;rows=normalized(design)
    require(len({(s,f,x) for s,f,x,j in rows})==len(rows),'distinct encoded slots')
    require(all(sum(map(abs,x))<=T+(s==-1)*(-1) for s,f,x,j in rows),'input cones')
    require(sorted(j for s,f,x,j in rows if s==0)==list(range(n)),'one independent current slot per input')
    snapshots=polynomial_run(design)
    require(serialize(snapshots)==saved[str(n)],'published complete polynomial record')
    require(snapshots[-1].get(((0,0,0),2),set())=={(1<<n)-1},'pure conjunction polynomial')
    require(all(sum(map(abs,x))<=2*T for s in snapshots for x,f in s),'all input-caused writes recorded')
    for background in range(2):
        initial=full_torus_check(design,snapshots,19000+100*n+background)
        words=frontier_check(design,initial)
    M=3*(vol(3*T)+vol(3*T-1));copies=len(rows)-n
    J=M-n+6;zeros=M-len(rows)+6
    require(zeros+copies==J,'fixed and copy constraint accounting')
    counter=None
    for axis in DIRS:
        x=tuple(T*v for v in axis)
        for f in range(3):
            if any((s,ff,xx)==(0,f,x) for s,ff,xx,j in rows):continue
            changed=polynomial_run(design,(0,f,x,-1))[-1].get(((0,0,0),2),set())
            errors=(poly_truth(changed,n)^(1<<((1<<n)-1))).bit_count()
            if errors:counter=(FIELDS[f],x,errors);break
        if counter:break
    require(counter is not None,'workspace countercontrol')
    print('n=%d T=%d L=%d J=%d: all %d inputs, two dense full-torus backgrounds; degree=%d' % (n,T,6*T+3,J,1<<n,n))
    print('  Complete record: %d nonzero coordinate-time polynomials; %d zero pins + %d affine copy constraints' % (sum(len(s) for s in snapshots),zeros,copies))
    print('  Source: all %d words once on each dense complement; joint factorization by disjoint cones' % words)
    print('  Released-pin control: field=%s position=%s gives %d/%d incorrect flags when set to 1' % (*counter,1<<n))

def main():
    saved=json.loads(Path(__file__).with_name('RECORDS.json').read_text())
    for design in DESIGNS:check_design(design,saved)
    print('PASS: finite AND4/AND5/AND6 components, complete specified records, bounded independent source')
    print('SCALING NOT ESTABLISHED: no all-n layout, clock, native preparation, or reuse protocol')

if __name__=='__main__':main()
