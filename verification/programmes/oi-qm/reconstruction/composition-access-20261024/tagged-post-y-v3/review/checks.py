#!/usr/bin/env python3
"""Independent exact controls for the tagged post-Y comparison; no author imports."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json


def need(ok, label):
    if not ok:
        raise RuntimeError(label)


def code(j, g):
    a,b,c,d=j
    return ((a,b,(1+g+a*b+b)%2),(b,b,1-g),
            (c,b,(1+g+c*b+b)%2),(0,0,d))


def decode(raw):
    return raw[0][0],raw[1][0],raw[2][0],raw[3][2]


def bloch(mu):
    return (sum(mu.values()),)+tuple(sum(w*((-1)**j[k]) for j,w in mu.items()) for k in (0,1,3))


def distribution(axis, outcome):
    # Retained original calibration table, independently represented as rows.
    rows=[((0,0,0),5,5,7),((1,1,1),5,5,7),((0,1,0),4,2,2),
          ((0,1,1),1,3,1),((1,0,0),1,3,1),((1,0,1),4,2,2)]
    out={}
    for plane,wx,wy,wr in rows:
        for z in (0,1):
            j=plane+(z,)
            if j[axis]==outcome:
                out[j]=Q(1,6) if axis==3 else Q((wx,wy,wr)[axis],20)
    return out


def ca(a,b): return a[0]+b[0],a[1]+b[1]
def cm(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def mm(a,b):
    return [[ca(cm(a[r][0],b[0][c]),cm(a[r][1],b[1][c])) for c in range(2)] for r in range(2)]
def matrix(b):
    t,x,y,z=b
    return [[(Q(t+z,2),Q(0)),(Q(x,2),Q(-y,2))],
            [(Q(x,2),Q(y,2)),(Q(t-z,2),Q(0))]]


def tv(a,b):
    return sum(abs(a.get(k,0)-b.get(k,0)) for k in a.keys()|b.keys())/2


def run():
    axes=((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(4,5),Q(3,5),Q(0)),(Q(0),Q(0),Q(1)))
    for a,s in product(range(4),(0,1)):
        expected=(Q(1),)+tuple((-1)**s*v for v in axes[a])
        need(bloch(distribution(a,s))==expected,'calibration decoder')
    encodings={code(j,g) for j in distribution(3,0)|distribution(3,1) for g in (0,1)}
    need(len(encodings)==24,'joint carrier/tag injectivity')
    source_rows=0; branches=[]; reused=[]; rawlaws={}
    for x,y in product((0,1),repeat=2):
        counts=Counter(); failure=0
        for a,b,k,z in product((0,1),(0,1),range(8),(0,1)):
            q=(y,y,1-x*y)
            raw=((q[0]^a,q[1],q[2]^(a*q[1])),q,
                 (q[0]^b,q[1],q[2]^(b*q[1])),(0,0,z))
            j=(y^a,y,y^b,z)
            need(raw==code(j,x*y) and decode(raw)==j,'source mixer/embedding')
            bound=5 if (a,b)==(0,0) else 3 if (a,b)==(1,0) else 2 if (a,b)==(1,1) else 0
            if k<bound: counts[raw]+=1
            else: failure+=1
            source_rows+=1
        need(failure==44 and sum(counts.values())==20,'success/failure counts')
        law={raw:Q(count,20) for raw,count in counts.items()}
        rawlaws[x,y]=law
        need({decode(raw):w for raw,w in law.items()}==distribution(1,y),'full success law')
        rho=matrix((Q(1),Q(0),Q((-1)**y),Q(0)))
        for a in range(4):
            for s in (0,1):
                selected={raw:w for raw,w in law.items() if decode(raw)[a]==s}
                mass=sum(selected.values())
                if not mass: continue
                port=next(iter(selected))[a]
                need(all(raw[a]==port for raw in selected),'record redundancy')
                posterior={decode(raw):w/mass for raw,w in selected.items()}
                t,bx,by,bz=bloch(posterior)
                det=(t*t-bx*bx-by*by-bz*bz)/4
                wanted=Q(0) if a==1 else Q(-1,64) if a==2 and s==y else Q(-1,4)
                need(det==wanted,'unchanged posterior determinant')
                # Construct the full independent resampling law including the recorded raw port.
                joint=Counter()
                for raw,w in selected.items():
                    for fresh,p in distribution(a,s).items():
                        joint[port,code(fresh,x*y)]+=w*p
                need(sum(joint.values())==mass,'positive reset normalization')
                quantum=mm(mm(matrix((Q(1),)+tuple((-1)**s*v for v in axes[a])),rho),
                           matrix((Q(1),)+tuple((-1)**s*v for v in axes[a])))
                offered={decode(raw):w for (rec,raw),w in joint.items()}
                need(matrix(bloch(offered))==quantum,'projector matrix identity')
                branches.append({'x':x,'y':y,'axis':('X','Y','R','Z')[a],'outcome':s,
                                 'probability':str(mass),'unchanged_determinant':str(det)})
        # Reuse u1=x XOR y, with still-fresh v,K,z and actual acceptance.
        reused_counts=Counter()
        for v,k,z in product((0,1),range(8),(0,1)):
            u=x^y
            cutoff={(0,0):5,(1,0):3,(1,1):2,(0,1):0}[u,v]
            if k<cutoff: reused_counts[y^u]+=1
        total=sum(reused_counts.values())
        need(total==10,'reused-seed herald probability')
        measured={s:Q(c,total) for s,c in reused_counts.items()}
        need(measured=={x:Q(1)} and tv(measured,{0:Q(1,2),1:Q(1,2)})==Q(1,2),
             'reused-seed conditional output discrepancy')
        reused.append({'x':x,'y':y,'success':'5/16','conditional_X_tv':'1/2','including_failure_tv':'5/32'})
    need(len(branches)==28,'positive branch count')
    need(tv(rawlaws[0,1],rawlaws[1,1])==1,'strict raw code obstruction')
    correct=distribution(1,0)
    wrong={(a,0,b,z):Q(w,20) for a,b,w in ((0,0,5),(1,0,2),(1,1,3)) for z in (0,1)}
    need(tv(correct,wrong)==Q(1,10),'calibration mutation')
    return {'schema':'oi-tagged-post-y-independent-review-v1','verdict':'PASS',
            'source_seed_assignments':source_rows,'injective_carrier_tag_codes':24,
            'positive_projector_matrix_branches':len(branches),'posteriors':branches,
            'old_seed_reuse':reused,'strict_raw_history_tv':'1',
            'scope':'supplied calibrated algebra; no native splice or interface adoption'}


if __name__=='__main__': print(json.dumps(run(),indent=2,sort_keys=True))
