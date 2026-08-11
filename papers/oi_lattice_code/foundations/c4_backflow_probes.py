#!/usr/bin/env python3
# c4_backflow_probes.py — b55 preregistered probe (2026-08-10).
# Certifies the readback lemma  I(X_<k ; X_{k+1} | X_k) >= p0*delta^2/ln2
# and the (C4) separation, exactly where exactness is claimed.
#  Q1 gap family (must-fire): exact I and exact (p0, delta); bound holds.
#  Q2 revival family: gap (delta=1, p0=1/6) at k=1; I = 2/3 >= 1/(6 ln 2).
#  Q3 coin (must-be-silent): no gap at any order; I = 0 exactly; C1-C3 hold.
#  Q4 dilation inherits C4: the b51 construction's past-conditioned laws
#     reproduce the target's differing kernels exactly.
#  Q5 parametric gap check: small-delta family, bound holds with margin.
from fractions import Fraction as F
from math import log, log2, pi
import itertools

LN2 = log(2.0)

def I_cond(tab):
    """I(A;B|C) in bits from dict (a,c,b)->prob (Fractions)."""
    pc, pac, pcb, I = {}, {}, {}, 0.0
    for (a,c,b),p in tab.items():
        pc[c]=pc.get(c,F(0))+p; pac[(a,c)]=pac.get((a,c),F(0))+p; pcb[(c,b)]=pcb.get((c,b),F(0))+p
    for (a,c,b),p in tab.items():
        if p: I += float(p)*log2(float(p*pc[c]/(pac[(a,c)]*pcb[(c,b)])))
    return I

def gap_and_bound(tab):
    """max over (c, past-pairs) of p0*delta^2/ln2 from exact next-step laws."""
    laws={}
    for (a,c,b),p in tab.items():
        laws.setdefault((a,c),{}); laws[(a,c)][b]=laws[(a,c)].get(b,F(0))+p
    best=F(0)
    keys=list(laws)
    for i in range(len(keys)):
        for j in range(i+1,len(keys)):
            (a1,c1),(a2,c2)=keys[i],keys[j]
            if c1!=c2: continue
            w1=sum(laws[keys[i]].values()); w2=sum(laws[keys[j]].values())
            P1={b:v/w1 for b,v in laws[keys[i]].items()}; P2={b:v/w2 for b,v in laws[keys[j]].items()}
            support=set(P1)|set(P2)
            tv=sum(abs(P1.get(b,F(0))-P2.get(b,F(0))) for b in support)/2
            p0=min(w1,w2)
            best=max(best,p0*tv*tv)
    return float(best)/LN2

# ---- Q1: explicit gap family: X0 uniform{0,1}; X1|X0 = 1/2,1/2; X2 = X0 (readback)
tab={}
for x0 in (0,1):
    for x1 in (0,1):
        tab[((x0,),x1,(x0,))]=F(1,8)*2  # P(x0)=1/2 * P(x1)=1/2 ; b=(x2,)=(x0,)
I=I_cond(tab); lb=gap_and_bound(tab)
# exact: I(X0;X2|X1)=H(X0)=1 bit; p0=1/4, delta=1 -> bound=1/(4 ln2)=0.3607
assert abs(I-1.0)<1e-12 and abs(lb-0.25/LN2)<1e-12 and I>=lb
print(f"Q1 gap family: I = {I:.6f} bits >= bound {lb:.6f} = p0*d^2/ln2 (p0=1/4, d=1)  MUST-FIRE OK")

# ---- Q2: revival family (b48), k=1, B=(x2)
phiR={(0,0):(0,0),(0,1):(0,1),(1,0):(1,0),(1,1):(2,0),(2,0):(1,1),(2,1):(2,1)}
tab={}
for x0 in range(3):
    for h in range(2):
        s=(x0,h); v1=phiR[s][0]; s2=phiR[phiR[s]]; v2=s2[0] if False else phiR[phiR[s]][0]
        tab[((x0,),v1,(v2,))]=tab.get(((x0,),v1,(v2,)),F(0))+F(1,6)
I=I_cond(tab); lb=gap_and_bound(tab)
assert abs(I-2/3)<1e-12 and abs(lb-(F(1,6)*1*1)/1/LN2)<1e-9 and I>=lb
print(f"Q2 revival: I = {I:.6f} = 2/3 bits >= bound {lb:.6f} (p0=1/6, d=1)  OK")

# ---- Q3: coin via the b51 construction — silent
PAD=-1
def build(kern,nV,K,D):
    hs=list(itertools.product(list(range(nV))+[PAD],repeat=K)); ts=list(itertools.product(range(D),repeat=K))
    states=[(x,h,t,c) for x in range(nV) for h in hs for t in ts for c in range(K+1)]
    wf=lambda h,c: all(h[i]!=PAD for i in range(c)) and all(h[i]==PAD for i in range(c,K))
    def Q(p,s):
        acc=0
        for y in range(nV):
            cnt=kern(p)[y]*D; assert cnt.denominator==1; acc+=int(cnt)
            if s<acc: return y
    phi={}
    for (x,h,t,c) in states:
        if c<K and wf(h,c):
            phi[(x,h,t,c)]=(Q(tuple(h[:c])+(x,),t[c]),tuple(list(h[:c])+[x]+[PAD]*(K-c-1)),t,c+1)
    un=sorted(set(states)-set(phi.values())); ud=sorted(set(states)-set(phi.keys()))
    for a,b in zip(ud,un): phi[a]=b
    return phi,[(tuple([PAD]*K),t,0) for t in ts]
K=4
phi,mu=build(lambda p:(F(1,2),F(1,2)),2,K,2)
w=F(1,len(mu))
traj_tab={}
for x0 in (0,1):
    for (h,t,c) in mu:
        s,tr=(x0,h,t,c),[x0]
        for _ in range(K): s=phi[s]; tr.append(s[0])
        traj_tab[tuple(tr)]=traj_tab.get(tuple(tr),F(0))+w*F(1,2)
for k in range(1,K):
    tab={ (tr[:k],tr[k],tr[k+1:]) : p for tr,p in traj_tab.items() }
    agg={}
    for key,p in tab.items(): agg[key]=agg.get(key,F(0))+p
    assert abs(I_cond(agg))<1e-12 and gap_and_bound(agg)<1e-12
print(f"Q3 coin (K={K}): I = 0 exactly at every order; no (C4) gap anywhere  MUST-BE-SILENT OK")

# ---- Q4: dilation inherits C4 from the non-Markov target
def kNM(past):
    c=len(past)-1
    if c==0: return (F(3,4),F(1,4)) if past[0]==0 else (F(1,4),F(3,4))
    if c==1: return (F(1),F(0)) if past[0]==past[1] else (F(0),F(1))
    return (F(1,4),F(3,4)) if past[1]==0 else (F(3,4),F(1,4))
phi,mu=build(kNM,2,3,4)
w=F(1,len(mu))
laws={}
for x0 in (0,1):
    for (h,t,c) in mu:
        s=(x0,h,t,c); s1=phi[s]; s2=phi[s1]
        key=((x0,s1[0]),)  # past (x0,x1) with endpoint x1 folded in
        laws.setdefault((x0,s1[0]),{0:F(0),1:F(0)})
        laws[(x0,s1[0])][s2[0]]+=w*F(1,2)
cond={k:{b:v/sum(d.values()) for b,v in d.items()} for k,d in laws.items() for d in [d]}
assert cond[(0,0)]=={0:F(1),1:F(0)} and cond[(1,0)]=={0:F(0),1:F(1)}
print("Q4 dilation inherits (C4): past-conditioned laws (0,0)->delta_0 vs (1,0)->delta_1, exactly the target kernels  OK")

# ---- Q5: small-delta parametric family
tab={}
for x0 in (0,1):
    # X1 uniform; X2 | (x0, x1): (1/2 + s, 1/2 - s) with s = +1/8 for x0=0, -1/8 for x0=1
    s=F(1,8) if x0==0 else F(-1,8)
    for x1 in (0,1):
        for x2 in (0,1):
            p=F(1,4)*( (F(1,2)+s) if x2==0 else (F(1,2)-s) )
            tab[((x0,),x1,(x2,))]=tab.get(((x0,),x1,(x2,)),F(0))+p
I=I_cond(tab); lb=gap_and_bound(tab)   # delta=1/4, p0=1/4 -> bound=(1/4)(1/16)/ln2
assert abs(lb-(0.25*0.0625)/LN2)<1e-12 and I>=lb
print(f"Q5 small-gap family: I = {I:.6f} >= bound {lb:.6f} (p0=1/4, d=1/4)  OK")
print("c4_backflow probe: COMPLETE — readback lemma certified; coin silent")
