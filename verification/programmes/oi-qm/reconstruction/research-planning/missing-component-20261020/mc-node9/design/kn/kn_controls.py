"""Exact checks for the K_n form of M0 (owner, 2026-10-22). n canonical pairs over F2; a point is a
2n-bit vector (q_1, p_1, ..., q_n, p_n); a linear functional is a 2n-bit mask; omega pairs q_i with p_i.
K_n = convex hull of uniform distributions on affine sets whose constraint space is isotropic."""
from itertools import product, combinations
from fractions import Fraction as F
def omega(a,b,n): return sum(((a>>(2*i))&1)*((b>>(2*i+1))&1)+((a>>(2*i+1))&1)*((b>>(2*i))&1) for i in range(n))%2
def dot(a,x): return bin(a&x).count('1')%2
def span(rows):
    s={0}
    for r in rows: s|={x^r for x in s}
    return frozenset(s)
def iso_states(n):
    N=2*n; spaces={span(())}
    frontier={span(())}
    while frontier:
        nxt=set()
        for S in frontier:
            for a in range(1,1<<N):
                if a not in S and all(omega(a,b,n)==0 for b in S): nxt.add(span(tuple(S)+(a,)))
        nxt-=spaces; spaces|=nxt; frontier=nxt
    sts=set()
    for S in spaces:
        for x0 in range(1<<N):
            sts.add(frozenset(x for x in range(1<<N) if all(dot(a,x^x0)==0 for a in S)))
    return sts
def has_isotropic_component_inside_support(dist,sts):
    """One-directional test. Every member of K_n has a mixture component whose support lies inside the member's
    support. So if no isotropic uniform state has support inside supp(dist), dist is NOT in K_n. A True result
    decides nothing; full membership needs the exact linear test with certificates (design/kn/review/)."""
    S=frozenset(x for x,p in dist.items() if p)
    return any(T<=S for T in sts)
st1=iso_states(1); st2=iso_states(2)
print('isotropic uniform states: n=1 ->',len(st1),' n=2 ->',len(st2))
# composite countercontrol: q1 = q2, p1 = 0, p2 free (bit order q1,p1,q2,p2 = bits 0,1,2,3)
S=[x for x in range(16) if ((x>>0)&1)==((x>>2)&1) and ((x>>1)&1)==0]
dist={x:F(1,len(S)) for x in S}
c1=(1<<0)|(1<<2); c2=(1<<1)
print('composite: support',len(S),'max point prob',max(dist.values()),
      ' constraint bracket <q1+q2, p1> =',omega(c1,c2,2))
m1={}; m2={}
for x,p in dist.items():
    a=(x&1, (x>>1)&1); b=((x>>2)&1,(x>>3)&1)
    m1[a]=m1.get(a,0)+p; m2[b]=m2.get(b,0)+p
k1=lambda m: all(v<=F(1,2) for v in m.values()) and abs(sum(m.values())-1)==0
print('  toy-1 marginal in K1:',k1(m1),' toy-2 marginal in K1:',k1(m2))
ok=has_isotropic_component_inside_support(dist,st2)
print('  isotropic uniform states with support inside S:',sum(1 for T in st2 if T<=frozenset(S)),
      '-> joint in K2:', 'not decided here' if ok else False)
# biased-mask family on one pair: support a line, weights p, 1-p
for p in (F(1,2),F(1,4),F(99,100)):
    m={(0,0):p,(0,1):1-p}
    print('biased line p=%s: support 2, in K1: %s, guessing probability %s'%(p,k1(m),max(p,1-p)))
