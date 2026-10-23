"""Builder B(n) for AND_n under the report18 rule (receiver at the origin).

Register machine: c <- H(c xor s), s affine in the inputs. A chain of first-light cells along an axis realizes it;
three planar wings (one seed field each) deliver s via Pascal-mod-2 inversion; a commutator (Barrington) program over
S8 computes 'rho if AND else identity' on the register."""
import itertools
from functools import lru_cache
from group import GEN, I, comp, inv, LAY, word, block_len, cycle
OMEGA=(0,1,2,3,4)
CYC=[cycle((OMEGA[0],)+p) for p in itertools.permutations(OMEGA[1:])]
def commutator(a,b): return comp(comp(a,b),comp(inv(a),inv(b)))
PAIRS={}
for r in CYC:
    PAIRS[r]=[(a,b) for a in CYC for b in CYC if commutator(a,b)==r]
@lru_cache(None)
def cost(k,r):
    if k==1: return block_len(r)
    k1=(k+1)//2; k2=k-k1
    return min(cost(k1,a)+cost(k2,b)+cost(k1,inv(a))+cost(k2,inv(b)) for a,b in PAIRS[r])
def program(inputs,r):
    """steps: list of (c, d) with c a 3-bit int and d a dict input->3-bit int; s = c xor sum x_j d_j.
    Total permutation (step 1 first) = r if all inputs are 1, identity otherwise."""
    k=len(inputs)
    if k==1:
        m=block_len(r); w0=word(I,m); w1=word(r,m)
        return [(w0[i],{inputs[0]:w0[i]^w1[i]}) for i in range(m)]
    k1=(k+1)//2; f,g=inputs[:k1],inputs[k1:]
    a,b=min(PAIRS[r],key=lambda ab:cost(len(f),ab[0])+cost(len(g),ab[1])+cost(len(f),inv(ab[0]))+cost(len(g),inv(ab[1])))
    return program(g,inv(b))+program(f,inv(a))+program(g,b)+program(f,a)
def pad_identity(steps,L):
    extra=L-len(steps)
    if extra==0: return steps
    for m in range(6,11):
        if extra-m>=0 and (extra-m==0 or extra-m>=6) and I in LAY[m]:
            return pad_identity(steps+[(v,{}) for v in word(I,m)],L)
    raise ValueError('cannot pad by %d'%extra)
def root_target(dest):
    """a 5-cycle on OMEGA mapping state 0 to dest, of minimal recursive cost (chosen per size)."""
    return [r for r in CYC if r[0]==dest]
def chains(n):
    """two chain programs of equal length: + chain ends in (0,F1,0) (state 2), - chain in (0,0,F2) (state 1)."""
    k1=(n+1)//2; ins1=list(range(k1)); ins2=list(range(k1,n))
    r1=min(root_target(2),key=lambda r:cost(len(ins1),r)); r2=min(root_target(1),key=lambda r:cost(len(ins2),r))
    p1=program(ins1,r1); p2=program(ins2,r2)
    L=max(len(p1),len(p2))
    for extra in range(0,40,2):
        try:
            return pad_identity(p1,L+extra),pad_identity(p2,L+extra)
        except ValueError: continue
    raise ValueError
# ----- realization -----
ORDER=[2,1,0]                     # P: D->B->A->D on field indices (A=0,B=1,D=2)
def Pf(f,k): return ORDER[(ORDER.index(f)+k)%3]
SEED={'+y':0,'-y':1,'+z':2}       # seed fields of the three wings (same seed for both chains in each half-plane)
def bits(v): return [(v>>2)&1,(v>>1)&1,v&1]   # state int -> (A,B,D)
def realize(n):
    """returns T and a list of sources (pos, field, affine value) with affine value = (const, frozenset(inputs))."""
    p_plus,p_minus=chains(n); Lc=len(p_plus); T=Lc+1
    srcs={}
    def addsrc(pos,f,val):
        key=(pos,f); c,s=srcs.get(key,(0,frozenset()))
        srcs[key]=(c^val[0],s^val[1])
    axis={w:(0,frozenset()) for w in SEED}
    for sign,prog in ((1,p_plus),(-1,p_minus)):
        for w,f in SEED.items():
            # required injection profile g(d), d=0..T-2: component Pf(f,d) of step d
            g=[]
            for d in range(T-1):
                c,dd=prog[d]; slot=Pf(f,d)
                const=bits(c)[slot]; vars_=frozenset(j for j,v in dd.items() if bits(v)[slot])
                g.append((const,vars_))
            def mul(a,b): return (a[0]^b[0],a[1]^b[1])
            col=[]
            for q in range(T-1):
                val=(0,frozenset())
                for d in range(q+1):
                    if (d & ~q)==0 or True:
                        from math import comb
                        if comb(q,d)%2: val=mul(val,g[d])
                col.append(val)
            for q,val in enumerate(col):
                if val==(0,frozenset()): continue
                x=sign*(T-1-q)
                pos={'+y':(x,q+1,0),'-y':(x,-(q+1),0),'+z':(x,0,q+1)}[w]
                addsrc(pos,f,val)
                from math import comb
                if comb(T-1,q)%2: axis[w]=mul(axis[w],val)
    for w,f in SEED.items():
        if axis[w]!=(0,frozenset()):
            pos={'+y':(0,T,0),'-y':(0,-T,0),'+z':(0,0,T)}[w]
            addsrc(pos,f,axis[w])
    return T,[(pos,f,val) for (pos,f),val in srcs.items() if val!=(0,frozenset())]
