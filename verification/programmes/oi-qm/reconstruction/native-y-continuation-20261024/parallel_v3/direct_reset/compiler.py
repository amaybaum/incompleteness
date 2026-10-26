"""Fixed-rule Boolean compiler and first-arrival lattice realization.

Standard library. No I/O. Generalizes the reviewed composition construction
to AND/OR formulas with signed literals; source values remain affine.
"""
from itertools import permutations
from functools import lru_cache

IDENTITY=tuple(range(8))
def compose(a,b): return tuple(a[b[j]] for j in range(8))
def inverse(a): return tuple(a.index(j) for j in range(8))
def h(s):
    a,b,d=(s>>2)&1,(s>>1)&1,s&1
    return 4*b+2*d+(a^(b&d))
GEN={v:tuple(h(s^v) for s in range(8)) for v in range(8)}
LAYERS=[{IDENTITY:None}]
for depth in range(1,9):
    nxt={}
    for p in LAYERS[-1]:
        for v,g in GEN.items():
            q=compose(g,p)
            if q not in nxt: nxt[q]=(p,v)
    LAYERS.append(nxt)

def cycle(xs):
    p=list(IDENTITY)
    for j,x in enumerate(xs): p[x]=xs[(j+1)%len(xs)]
    return tuple(p)
CYCLES=tuple(cycle((0,)+p) for p in permutations((1,2,3,4)))
PAIRS={r:tuple((a,b) for a in CYCLES for b in CYCLES
               if compose(compose(a,b),compose(inverse(a),inverse(b)))==r) for r in CYCLES}

def word(r,length):
    out=[]
    for depth in range(length,0,-1):
        r,v=LAYERS[depth][r]; out.append(v)
    if r!=IDENTITY: raise RuntimeError('bad word')
    return tuple(reversed(out))

def leaf_length(r):
    return next(k for k in (6,8) if r in LAYERS[k] and IDENTITY in LAYERS[k])

def lit(j,positive=True): return ('lit',j,positive)
def AND(a,b): return ('and',a,b)
def OR(a,b): return ('or',a,b)
def NOT(f):
    if f[0]=='lit': return lit(f[1],not f[2])
    if f[0]=='const': return ('const',not f[1])
    return ('or' if f[0]=='and' else 'and',NOT(f[1]),NOT(f[2]))

@lru_cache(None)
def cost(f,r):
    op=f[0]
    if op=='lit': return leaf_length(r)
    if op=='const': return leaf_length(r) if f[1] else 0
    if op=='or': return cost(AND(NOT(f[1]),NOT(f[2])),inverse(r))+leaf_length(r)
    a,b=f[1:]
    return min(cost(a,p)+cost(a,inverse(p))+cost(b,q)+cost(b,inverse(q)) for p,q in PAIRS[r])

@lru_cache(None)
def program(f,r):
    op=f[0]
    if op=='const':
        return tuple((v,()) for v in word(r,leaf_length(r))) if f[1] else ()
    if op=='lit':
        j,positive=f[1:]; length=leaf_length(r)
        w0,w1=word(IDENTITY,length),word(r,length)
        if not positive: w0,w1=w1,w0
        return tuple((a,((j,a^b),)) for a,b in zip(w0,w1))
    if op=='or':
        return program(AND(NOT(f[1]),NOT(f[2])),inverse(r))+tuple((v,()) for v in word(r,leaf_length(r)))
    a,b=f[1:]
    p,q=min(PAIRS[r],key=lambda pq:cost(a,pq[0])+cost(a,inverse(pq[0]))+cost(b,pq[1])+cost(b,inverse(pq[1])))
    return program(b,inverse(q))+program(a,inverse(p))+program(b,q)+program(a,p)

def target(f,dest):
    return min((r for r in CYCLES if r[0]==dest),key=lambda r:cost(f,r))

def pad(prog,length):
    gap=length-len(prog)
    if gap==0: return prog
    # Identity length 10 is built by concatenating inverse five-step words.
    if gap<6 or gap%2: raise ValueError('unrepresentable gap')
    blocks=[]
    while gap not in (0,6,8,10): blocks.append(6); gap-=6
    if gap: blocks.append(gap)
    out=prog
    for k in blocks: out+=tuple((v,()) for v in identity_word(k))
    return out

@lru_cache(None)
def identity_word(k):
    if k in (6,8): return word(IDENTITY,k)
    # Avoid retaining all depth-9/10 tables: find two 5-step words with inverse products.
    if k!=10: raise ValueError(k)
    for p in LAYERS[5]:
        if inverse(p) in LAYERS[5]: return word(p,5)+word(inverse(p),5)
    raise RuntimeError('no identity padding')

def common_length(programs):
    base=max(map(len,programs))
    for extra in (0,6):
        goal=base+extra
        if all(goal-len(p)==0 or goal-len(p)>=6 and (goal-len(p))%2==0 for p in programs): return goal
    raise RuntimeError('padding failed')

def realize(programs):
    """Signed axis programs, each same length; single or opposite pair.

    Returns (deadline, {(position,field): affine bit mask}). Bit 0 of an
    affine mask is its constant, bit j+1 multiplies input j.
    """
    lengths={len(p) for p in programs.values()}
    if len(lengths)!=1: raise ValueError('unequal programs')
    T=lengths.pop()+1
    sources={}; axes=[0,0,0]
    order=(2,1,0)
    for sign,prog in programs.items():
        for wing,seed in enumerate((0,1,2)):
            profile=[]
            for d,(c,terms) in enumerate(prog):
                field=order[(order.index(seed)+d)%3]
                shift=2-field
                value=(c>>shift)&1
                for j,coefficient in terms:
                    if coefficient>>shift&1: value^=1<<(j+1)
                profile.append(value)
            for q in range(T-1):
                value=0
                # Lucas parity: binom(q,d) odd iff d is a submask of q.
                d=q
                while True:
                    value^=profile[d]
                    if d==0: break
                    d=(d-1)&q
                if not value: continue
                x=sign*(T-1-q)
                pos=((x,q+1,0),(x,-q-1,0),(x,0,q+1))[wing]
                key=(pos,seed); sources[key]=sources.get(key,0)^value
                if q & ~(T-1)==0: axes[wing]^=value
    for wing,value in enumerate(axes):
        if value:
            pos=((0,T,0),(0,-T,0),(0,0,T))[wing]
            sources[pos,wing]=sources.get((pos,wing),0)^value
    return T,{k:v for k,v in sources.items() if v}

# U = 8u3+4u2+2u1+u0. Input numbers 0..3 are u0..u3.
u0,u1,u2,u3=[lit(j) for j in range(4)]
SUCCESS=OR(NOT(u3),AND(NOT(u2),NOT(u1)))
LOW5=AND(NOT(u3),OR(NOT(u2),AND(NOT(u1),NOT(u0))))
LOW9=OR(NOT(u3),AND(NOT(u2),AND(NOT(u1),NOT(u0))))
ERROR9=AND(AND(u3,NOT(u2)),AND(NOT(u1),u0))

def build():
    herald=program(SUCCESS,target(SUCCESS,4))
    carrier1=program(LOW5,target(LOW5,2))
    carrier2=program(LOW9,target(LOW9,1))
    length=common_length((herald,carrier1,carrier2))
    ht,hs=realize({1:pad(herald,length)})
    ct,cs=realize({1:pad(carrier1,length),-1:pad(carrier2,length)})
    if ht!=ct: raise RuntimeError('deadline mismatch')
    return ht,hs,cs,{'herald':len(herald),'carrier1':len(carrier1),'carrier2':len(carrier2),'padded':length}
